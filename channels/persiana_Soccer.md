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
<img src="https://cdn4.telesco.pe/file/HlVACjRpQNce5LZrKAbtuhmVlQr4bU5kL1_u3beGGr8dZK_WLfQh8bfr75flo-aofB5fWvDj_jAIyGUC4OHjWh1namIO6kbbOOmmNe8G3aa9Qtr2CyLoUbBu5zb26o47QIw6zeIgyiZfw_M9Y0aeiVmBMGFc7U71_jTIxI59FDqdlaNOwx0v_ZrzH-C6j_aU2jOTwLlZGQ2QTJb3W9zFm2fehpsyDwSDrr_0XPOQqwOsZTSr2QYoIPp3xBlW9buD8lbMV99jF1XEUABndeBLdrwlpXPQIMJaAvViZbrNy3os4xcofH6o-rrNJfvmyGyMLgksK08n9rRzZAto8aHuuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 611K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 13:07:10</div>
<hr>

<div class="tg-post" id="msg-28380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌ای درحاشیه دیدار شب گذشته استقلال و سپاهان که لحظه‌به‌لحظه داشت عجیب تر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/28380" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه بکش‌بکشی راه انداختن دیشب بین بازیکنان دو تیم آلومینیوم‌اراک
🆚
شمس‌آذر قزوین! اون یارو تدارکات‌چیه به قصد کشت زد تو سر بازیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/28379" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMq34RklWsXOdOzivHJOZUYbTUU-m1ZAWf_fC8FsSFZGmzImcJPKRl0CIECZz1wBA4Fx5MmqaPvQVa_5DzTT6X_b7FqriZiVp_8aOXwyF4UmdFZ_fZm7fJOcYUGlE5-nBJnmkcswJqYbPz2r8_EF0gDlLnqk2AxYGfQgRopkOLx6YQQqvnSz1Nsm6ejOQZl_FptoHe40Zpml2hdW7x5d96I0Mipv5jR8_gsDKC0EQdEyramm07ueYFlrS9W7T8LwFKjgkdMb3Chx3wN2bBJ3I5AcOmbvTtts1_ecJcIXPccpFgPLebgYgmGmQYQ6KXYnFdzDbQklr05C9XBwuJqKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/28378" target="_blank">📅 12:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدصلاح که‌سالی 17 میلیون‌یورو از ترابزون اسپور میگیره در اولین بازی‌اش برای این تیم چنگی به دل نزد و چند سوتی داد. بقول حسین حسینی از شانس بدش توپ هم باهاش همکاری نمیکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/28377" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔵
🇳🇴
واکنش‌های جالب جک گریلیش، پپ گوردیولا و زلاتان ابراهیموویچ به‌مدل‌موی جدید ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/28376" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta9fyESqt0hzlvVzgDJXJItdTux8kSsVLaJ47U3Ab6v1kcKstglOwjZhDeTynuBfrc0Q9j-JGR9I2teDP_6cp8OjZSsaGJ9vTgOJHaW7dW2HX9ZW3Hqj73j8tM6TKKn2XQyNAYGS-cnxxe_NahgwpAYFlZ5N4PA9m-dH8bnLfxRCTwd0Pc4lq39KxwGWQq3dbEhYtfHFN5hWg5IcJYONxHXOJ9HSe3aCyAw9BnZkFamA8L-C2OedDZJBrU9-f9OCs2xpj71Aq7EXsvV51EOFOB2e0aL3clrdbuKNi6JEjrzTfTbLNKWCw9ydXRXRpeNAsRJGp5KU6d0kQyuljClNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/28375" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ4-ybVGd0NP1sUGX08DhmaHUlSzBvJ2cBLW6iyWUTwSTQ629aLFMIDUtvkTvfEKN-a4mwQiIMue98YS6z7sI_tE9JZ7zeibHw0c-P6HoK0J6g1OQLv5KQR8dAD1N_RL-BkGNhIfOf68747VgOlvCN8tvVOMETB4WH9KcnaAuFmSMTydL8lohb8x7pAGjzjYtm9UDWhbeHwVKFslZUPsQR42qT7nnMVu6ZE4xbktk4lP6Kkfx8a-YKG7g9EyxFdnEmVF4HXe8Xif2ccAVVLYi_yhgyLQ551H-m86CivXoDaaIKyDQdb2vDk0ChT8JoS6cjqADcv2mGXG5bN3wVAb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/28374" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml0Zyqi1wztS82eCGczHwdUnifECPXpXm-aqw0QUyeez6N08CLZjZDxVibdbUVy5ZuaDplms5O9o_EsrhEbQSTS64daSNJ5KGw6grH4nw_4Sn-mkPmOPbxj-KIysSWaApkCj2_Aj1FoXiAg75E_J5oRndv9qW9FhKfT5l7QggC0HZD9E8VlcAIT8kfNAUq-Zo8gUDbR0EWE8vcWtqEUZNWSD7-gBZyEn9QBXsO3WpTYUlsjmH_pumETsqKzQGNdXZ4RPKrEU7J9XqFQIjQYK5G5f55DGMjZjnTZCRXIs3RZ5TktVKTXjxYzOZiQ17ScRFXG-duv1qaDNwD5qfMaNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10تقابل‌اخیرپرسپولیس
🆚
تراکتور در تمام رقابت‌ها: 6 بردپرسپولیس، 2 برد تراکتور، 2 مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/28373" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو برای چند سال پیش نیست برای همین چندماه‌پیشه و خیلی‌زود به حرفای ابوطالب که گفته بود دلمون برای دلار 78 تومنی تنگ میشه رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/28372" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5flENcpm4_hYGD5oU473Ifok-CL1upuxYoHyZ-Z2lnC0gKHkzmcVk8zq7KgPLtM5p6HeAfR9U34XvUQwBywF3Q1rfnO_zAy0QjhMmRA-fFisGLyRqETluzbHv7EUEAV2UX-Jgdi73-whsMiQAuC4w2P0WycS7AR3QiQYYQ2TwD0TzEnt8Fws789EwLZ_CUJbue6DimFP_ofG25zGy0al3sEEEZZ1LluJ4yqQyhyRNuoR7h5dJQdM1zMsD8ELXtdMledVZm8EUZaBnG8vzVBud7CdrrD_sH70PTLzxRrCkhDRrON_jp68G4v28k7Ade75rf0sUdUuKEtcPLbX-CAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://telegram.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/28371" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
این واکنش و چهره عبوس رونالدو بعد دیدن رئیس فیفا در شبکه‌های اجتماعی داره وایرال میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/28370" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/28369" target="_blank">📅 09:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
چهره درهم آلوارز در دیدار اتلتیکو
🆚
ویارئال؛ ای‌غم کمی تخفیف بده ما که مشتری هر روز توییم.
‼️
خیلی‌تلاش کرد دراین‌پنجره‌بره بارسلونا؛ هفته‌ای چهل بار مصاحبه‌میکرد و میگفت‌علاقه ای به موندن در اتلتیکو ندارم اما مدیران اتلتیکو بجای اینکه 150 میلیون یورو به جیب…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/28367" target="_blank">📅 09:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شاگردان هانسی فلیک در هفته نخست لالیگا؛ آتش بازی راه انداختند و دردیداری خارج از خانه با پنج گل الچه رو درهم‌کوبیدند‌. فرمین لوپز دبل کرد‌. کریم ادیمی هم نیومده برای آبی اناری‌ها گلزنی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/28366" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
هایلایتی‌ازعملکرددرخشان‌یاسرآسانی ستاره آلبانیایی استقلال دربازی شب گذشته برابر سپاهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/28365" target="_blank">📅 08:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXuqJNHFpkuYWpgPUPFMu-03fhwnRhjBhMReF5OdRjr-yaPlL6zARhftCs0FNmCQNkL2kiOe0MDPC4LzGHrlqxwQJR81kxBH20FI-M5Yee5RjhCb0NiKQJGtfEZH5AHrCOLHUWkWe8N2-9kCiWX4pMRDoMPiSpHK1p229x8yDTOW322hHO4kR5za4YGLLtO0yHGqjkALt0zs-DRxdF2jExwRsu7Bc-C8CoyVMXQzJVQDLwFTeg116P7TR8bMH2f7P8ggkJRLORIt6Cjl2UZsDPzLR2KcY3I4VtzDBy1Txc4QsXIt1A4gTGLPthNW6M5-u98Y2rgTfkFl_E9FW_da5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یاسرآسانی، اسماعیلی‌قلی‌زاده و حبیب فرعباسی به‌ترتیب با نمرات 8.5، 8.3 و 7.9 بهترین بازیکنان دیدار امشب استقلال
🆚
سپاهان انتخاب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28364" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHoBzQ04pb-XaQxD0h9KuEQeUGzslFy_sypTDbpekdYAvJPfxYEkypxQ3JIE3bnCl-5eFMmOawsOxdGkst8T5h6x_GWGovK619ofvESYSm1WJwcyvdPQZcJacGMDmpaJB_eeETP6xntKHH9fE4u2_x7UgvcD7-PvyknuRRSmhNvRnBBkKhrzI3R1ATHeirQ24rYedsUTlJoHccaNSVAMrTK-w7wjjMhp5NBlIAOw9IRUz_cwn2ETeEn__jPehMUpWx1T13AhytxUEfnwvq_kE1WVaJwfnXXjepACRgv1NCDVqIwF_Rjq0oq7EQiUWUUNiLO-wAYkQ2gyS11uG9DqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بخت در خونت رو بزنه همین میشه‌ها. مردی داشت با هال‌سیتی مذاکره میکرد بره این تیم که‌یهوسروکله رئال مادرید پیدا شد. تو اولین بازیش ازرو نیمکت اومده جور ناکامی امباپه و وینسیوس و یان دیومانده رو کشید و گل پیروزی تیمشو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28363" target="_blank">📅 01:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28362">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28362" target="_blank">📅 01:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28361">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1704880194.mp4?token=cGX8rICQRYlSHo56_vgPZPD6F-PShLt2MgMZNh8UD25_V4QxG9sEF9vGoZNcL-RpASofUq6_iYklXppC0AzuCnbmEPWxO3vfz_geG8ii36bawbGdxQiAJVykwwAHsUhUniOh0CESbOfNt9jlLvbMSQdxEKYFrp9CUGJTF1Vdtx0EhQtpyk3nTJpLeFG3y-sa8NBZZfT-ZAwKXza3sfZk1chsGaoTuMvbltex2GgDS3wGkmF7DhZnD4vja5y3xRh6x9XDCvT4ocIp_S6Df31i-GT4LLnXsePK8jdFSI2F4lNB5XUljQam6VRqxj2VPCTDxbHkI3NQ4Pdj6zCqY4JTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1704880194.mp4?token=cGX8rICQRYlSHo56_vgPZPD6F-PShLt2MgMZNh8UD25_V4QxG9sEF9vGoZNcL-RpASofUq6_iYklXppC0AzuCnbmEPWxO3vfz_geG8ii36bawbGdxQiAJVykwwAHsUhUniOh0CESbOfNt9jlLvbMSQdxEKYFrp9CUGJTF1Vdtx0EhQtpyk3nTJpLeFG3y-sa8NBZZfT-ZAwKXza3sfZk1chsGaoTuMvbltex2GgDS3wGkmF7DhZnD4vja5y3xRh6x9XDCvT4ocIp_S6Df31i-GT4LLnXsePK8jdFSI2F4lNB5XUljQam6VRqxj2VPCTDxbHkI3NQ4Pdj6zCqY4JTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28361" target="_blank">📅 01:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28360">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVpswnX6EfHRfO14WCqf4pwLQFDlNaAm_Lu754CNCnWt9GzUUeJtYem4Gsdq5NtVfSlu3i-9DAAPPFtg4U7XG3YA45y_fB4GDWxLR90h6sTeh1mIPtg4eOlFR2evFaXB8mBc_lTw1CWA7ZUulEXoD2liFsRdr5dvi7OzQ8uEUBgjO7N5kAfIWZD2l1cPF7v85vzrarrqsgF4zHc2_NbfuCfHQifiDAQ5KjUl61gqh1jKyaYRL-meI1uLrzlII7HOnalEpES2fEZVLyJQ7qNIE0IAmwFKhwq_UMCKVXnZAiPs9kSVN-iktqcU6LFZbI9Ak9rrKhg7ljgb46AmSiOmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
جدال سرخ‌ها با شاگردان نکونام و رونمایی‌ازچلسی‌تحت هدایت ژابی آلونسو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28360" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28359">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl0O0h01y_UErs5D45ACImmbXu7Sa8wrkWi-xEvJ4eD654K40LadjXjVPxmYRGPeDpdmm1Hg8esCSsR_apagM47VyXHj2MGqjzVqY-JMWQPxSCw-8ZZweiY1T6H1hEMKj-AH7o7WWIMGW9NnaQ1fCEcqGRFUJJhewkqvFT6CpeCi_c-eJ5_Ae3TCdeaBzVzCixma1dGEPQUjKfpvCrw4u_2KUOLn2ziLraZHOrYcVX43km8KPsEChOliwaXmOYcJs-2Gw_ze63moB16tYc08eb6sy3lIXUSttUpEZ4TllGNhqPQirLpJjc3Qmh9JvLeCq80WumaLWHOAIx1tCq8B4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
سومین برد و کلین‌شیت پیاپی استقلالی‌ها در لیگ، برتری دشوار سیتیزن‌ها با درخشش‌چرکی و جشنواره گل کاتالان‌ها در گام اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28359" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28358">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8dIaNww2fiAoQCPkOUEDAVpWozv_sJw6QIuvp1fxCKly7GU_oL5sfSdsFhiozjKGR2KxGE8w11ZNA5RCbFhh1E2kfJiXT6GmROcJg0jYiDu94NGEyajuVr-5elhg8KfGeUUFfXFVndjnts0GanAErg9JJqcLjv3_lf9Be1jseY_ceLomXW94hRYzJz2ebtvMwxtGNlO3t9lEp1xk1EURJXP5yJaSFsbzCOwEM0Spxntq2q-duMttNH5gPa0itRA3jDnm6jaTman2Y_aWvCmufZrg_WmQ3maYrMFvOmZMlpbq5q9pyd0RXAMfHPjn4IjXBbbVyrbWcq3EUGfXmFEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
حساس ترین مسابقه ی هفته لیگ برتر ایران با بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
تراکتور
⚽️
✖️
⚽️
پرسپولیس
⏰
امشب ساعت 18:30
🚨
ورزشگاه یادگار امام
🎲
با شارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران در صورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa1
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28358" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28357">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyANJEs2Q1dGHOKYz9vB_1w7LMB3AOo6oPYDBq1ljnPrUAQurRh49Tgh65n4SpxgKbtVVLGoMX3J1PH2agX66qRq8NI0GKpan5YzRCGKuWXNMkOACyOW7UHsqtnxqu9-REmOkDAO0HMFY833qYf7s8z9flVmM4kA8FJy6kzRVd7FYWM4AFrI0kRGwddilm1LrzhFrm9-0IGPnUkExjo4oyiU_YmeuvmfwioU50HjvuF9fkvFGkAEzs4obkVcg8V8kGN1XxcCFIl87VsY7uBivSFravOijMR79xxVbGjcYcAk1dtT8RTWOch_7ClBdo-zx4R7z8wQaBlNxerplROH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار امشب با الچه؛ ساعت 23:00 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28357" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28356">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28356" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28355">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHt4lENyG0BIowtgrgfUtnQJbKm9mwB7RY02gbzHDLRGLndMU7w3Wct7MT8gngoFDWxPSN8d5BTwZkqKA-8CZrdjYHUhj3mQEXMnUiUZPG8qJp2U6Xbs-uDKhSQMSyDs9mUA14EmtXSBVusL6J6VLyQRnTqTwxE7u6hsOS4q0kbakKO2BZ3Klov2ITm2Kmqpcqs1H_miDwT8y5KL8-x965o22wi-HrBD73S43bLXHbsGsf0c32Lz56yzAWtlLfTkEN5IqknCDeu0jD8tE812Em4iXIajgEkrxqX52yahi_FB7O3W9zNZ2it9dvzB6g8BBnP9YZ-SH5l-kobJLgD_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28355" target="_blank">📅 00:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28354">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMu0eEq93h01KOgT5kOEjknXLTQogqVHfUbwqD7TI7dvPfWtoowLdBj6Kumwd5uAd2eEcPHOYyC-aKNL0V04508R1lWSL88lx92R_nYDHDB7pVqtaJ41iO-ccQrjD_kGVB41GBSUZoYsPmUkABtV_1fd--IoalaObsWyf5LgjYofUnnYNqSH8UL9YNLa7-IHY4KNlqAI_j2SBeLAG2CuiPySata5d8JnqZrwllNR-kzv0z-pj2K_YlgTrA6Td7yD6CLNdDIjYaI8P_ITZ8JUxqd4VWb3_kVWUTJJTJ44MsvfoamlrQ2fHeqeFmXlDBFIfIJqB-r4eSxtx3t66pFXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28354" target="_blank">📅 00:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28353">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkHpdaLRiwKZAiydvOLFKVM7ugoM7DicuS_YZmi9GBP-dlbzFEuYC8Trqcj1MRVYsnwDw4u1i1o9OOvFEVPh2yckwfRjMIsquQZShborgP5B_dQKIgzDHQY1qhSQnnBCpJHrLR6DKBGv02bW_7ZhtGqn0t8PbkqEcIwGIjpsRIOYt2kNKCmZHRziR4Z9-BIhnUFdsSG_gOSUIHVSGK5t6Gf6vLzJzhdVVnKtPoDDP2ic1uljIuwp3i1CvsIvjguO9txu4LnGoJf-kExTaJ-2b4j3dQX5PgHg9-EIASPI8vGFqvy072E0y7ljanTMcek4KEFDLnwzz9HnqsyTGGLaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفاصله‌چندساعت‌تابازی‌تراکتور و پرسپولیس؛ هواداران تیم تراکتور مقابل‌هتل بازیکنان پرسپولیس تجمع کرده اند و شعارهایی سر داده اند تا به نوعی شاگردان مهدی تارتار نتونن به راحتی بخوابند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28353" target="_blank">📅 00:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28352">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه دیدارهای فردا ادامه هفته‌سوم لیگ که در حساس ترین دیدار تراکتور باپرسپولیس بازی میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28352" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28351">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay9qXdFC-u2wRdABsvYWCMJkZjODX6kz2G6C2nPsaKukj-Bddrw71XTZmUSv5lvPB89wyCC4R5fSmvS_azzFKRx_MwmmaAx5HmjPqNGP41TI9x8ItHSp66VrnZgF8s56woxcw99pciFqUL5ktY_TFw3XbtPilzuRwvOHR-gup_tPB2OBplE9rITBZgGJ3UPd9tcZ4qZUqspD5mHAK6btpfmvyUx4yZ5tUH8SyEXOoxSTgMn-H80ot3zbWKt6JEEujSGTZ2VROTpvj0fPZbj_0p6nNJbr-pKVrbZNi7_48IXTEtr9td0N6F5LeVOBcQ2OJPWOhv9rqIHK0adQ94eRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه کامل دیدارهای هفته چهارم لیگ برتر که قراره روزهای جمعه و شنبه پیش رو برگزار بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28351" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
بانوان‌هوادار استقلال در ورزشگاه شهر قدس در بازی امشب آبی‌ها مقابل سپاهان در هفته سوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28350" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFmhJWt5Qb1E4f-xgg3_9p-CyQqyhIlYxtG1l41l0Nty7k6lTMOQlG6m2BTCSdc-Nx9zX0IIO462Aft7ch4sVoCCzjBcRcj8luSDsyY4qkOwFT47n-ca2BH3-0CgRPL7iFiEpqoLGeAiEzIwU-x4nGjaY2ElaK4Ku3VPQJyuH9RBQ7G4MmlYgmGOnVLmSfI4LZeNR-6ldVQBAhe9fciYIfmtgGuh39PbXj5Zq1Q1WFCvvXeYYwjBYZsy8rQx4ASDou4xAQVZhHyQeirgxdo3RRfOltXbePlhzjh81LFk-jTyU1tf8QGTP4Rl0XRauBwbiUG3Vw4ch-v7G3cEX635g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfpTpO4oTAWrpPnBhwwaXH53y6xZIAasKvrdmjSBlchlqFnX9GQ4LdJIVuyNvUKIn5hq8E2Omf4VTUnR--ROEFVs3EkKPvPx-TSBnqzp0P3t6rRmcFXt5cFiQG2WUD47NBEfsglLiCGIJLCmnwottfb5fTrVzAiWPPjqE2DpuuFypKZNf5U24mWc1h4tOS2ym-OJPyyDcr02HWEjy-9hK_jM9oSPsTk16B5b9gc_Xj82TpeX3MPplsFPq5DcbfxOnDc8pJXSi-iA6eGwGlPVPspjpKcSR8hc7hPuuBzUONd0udw-hFxrDHoCNpoqpL4QV2fAeDVuZDIDPTGkceunRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
بااعلام ایجنت مهدی طارمی؛ باشگاه الوصل برای‌خرید مهدی طارمی تنها 400 هزار دلار به باشگاه المپیاکوس پرداخت‌کرده درحالیکه این باشگاه یونانی برای جذب طارمی 2 میلیون یورو هزینه کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28348" target="_blank">📅 22:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5NA8QmTWfv_BQSnmwNSc8ZUXd8baPiyYiMED5qWBiEaqKo8Y0aI7hVBX9KgTQwt2HX13u3Da0KYEfimXTkQdbVxSqABoo5jVhaCjfmhA8BKpz0fB2h-erJTLQujtBFwqiaNfqjhoAYgFOKUQbR6derVTuHB-Vb2wr58fTV35YvcVKKvnEEKpmN_W081VEmvZ18pwumlK5IOhkc0AA_u0A0gBXwgTj0fTgNioQPX5D6xW-PTD6j1GylY4WuDY8Ig0n3X8cNsDncI6CUtu2wAUw8FGCSuTt0GxIOD2S14OcpYJ8pg4ZZfedcK2AwFqHdHK5KUtskKg6l3iIPl5BN1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28347" target="_blank">📅 22:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulAgyuE3BZ-oxH80iv_ryGrZoZ_iSdRfG97kiX8pZxAzr47LB-GsntOeyzSi_ajASyfoLsl5WtlbIRUAU8Dwih_Si0WVEaucPL1kko6hHFpZbC90puxUwxTQbkrfZ56YwFXceHVBMEF_dhabOiRDYW5-SMtucUiKezl7Dw0vibtkHvIJERFMYoiNfj3RO5uZyW6Pi2vU6FELI1Odhft21aqLYzVbFeBGRdq5G8tHrnpy_sSSabjuSBSumcTXJKgGl5a943OjYZr8d9Q7IJxPpIOB78uBPu8uT5yTgoalpwkhcFxPW5nQvMkNSCrE_2QQ2SzyVgKyEK2EAeKV0CsYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بدون کلین‌شیت بدون پیروزی؛ حسینی به‌دنبال اولین برد مقابل‌استقلال؛ سیدحسین حسینی تاکنون ۲ بار با لباس ملوان و یک‌بار به همراه سپاهان مقابل تیم استقلال قرار گرفته و حاصل آن یک تساوی و ۲ شکست برای او بوده. او در این ۳ بازی گل خورده و اصلا نتوانسته مقابل تیم…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28346" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djOiflUtgY359mZRZogfv_6rGevLwAZyj-wT5y_vgwxbBZuhYQyrvu4zkVL-TlXm0T7swsLVzBCkYixlkW3iKAdfw_KDpMFRc_TOKrJYe0gPljtPtZySgAl-5diXl1VCRi6QKSbe_TD1eQE41FOgngseAop4Ho0EnOQ0a-43aJcTNW-zVoLPIMGx0py0I8mQ1od5ZLPMHgeYRQLh7aiaPyZRDNBW7SR7H4zhrRpqCfYmJ47VFgPmaQrP_fUFA_kWf-P2JHUtwU2f-8ACl6v31ybTpuICDAXY7PcSgvaX3x62vg-cTnC47eg-s8ZM0CoTNoiyG9ETBCs6jSTCRqfghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TezgxwTB_I4JOABEWv_3eXz0MOflU26HKkOWdAwUM0sakJWLTC_3R9KqXdU2eWXOzlm4gVV7GeTVSNRUhh1Y4SMtikPost81-ByI1Z4nINxwcrrL2bldfqRmcKZ5g4a5EqX_fxR1fdnc94H_q6U443OG9MQFEbNIkuJ6MZwQsT7V5CSb3MVWFfh2EPFJmFrUwe82tviSCukyt8v6g-eDIakFhkXHl8mfIv6lsWRWe_46dELeEP9Vl1Sd3d4fBWSs3bvrneMdATvQNznYw_leFUumQ5xLz8mixqxTZ_dH5g06LayJOQxA7dgAfbAVwk3tQ9Xq_aOO-P0o2sc81EOgCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جواد کاظمیان:
اگه ازم بپرسن بهشت چه شکلیه، میگم این شکلی: با جام قهرمانی و توپ طلا، کنار سرخانمم مونیکا بلوچی عزیز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28344" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVapUqfVjFVfeDXd6jer0ybQ9gPX-JErckBEDX5ZCVz1nfe4j667nBm_2Zj1ZYIVZE1Oqe4Q0-gLEHsOKbxSozcg_C4oNeSpfsDm7LqgpYP7iz84TYH4nPKnwerR7hLnelYydGExdXD7dhR7eYtsMF0sPsVoBWQmICChG80j_Ul5G-Byhz2UfoEMKm5-SFHk-0WzOdmGW0ds8io7ShxSwe_5gpjFMBsowWdbYrGk4f_YcU5BrjX9qbyLBDRBadrAahsRwKAzt68NHdOAj2V_MHIc58V_dfZbXiRO2HgZLoCkC8x3TXIBlhZuvgp4Ss6b7ik8v87W6xQZPtfzqWCSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28343" target="_blank">📅 21:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD3sKnt1LjDy8ENt5WTpcm-xFH95yHZosaP3WTpl9ymlV43AKDKWOAxPnim0cnaJr8IWrqjybnxYSBkhBNlSm44eLrzAJZJ99-eLpfmkZURfDg1vAi9hdvX_OMn3ss-M_PfdBpj_cg-ySIuim8tPu-AYphLdeoTch_vsSB78KJLaW4VB5lTBZgc1wJwMpYjkC4SHY1jDi4_rh25gLxg9nc2-5kEnwhjhMFskHGCAMzxMmgeVtl2D7kgQrBipLSwOIP3aRmi5hgwJmhlRk9H3ddnMacg8WtC72VkZkBZiHWJWWWJEcpvnZGhr8CcQ9JJ6UCFxkZcr9WApSeLHwsvk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
به مناسبت بازی امشب بارسا مقابل الچه در هفته اول لالیگا؛ نگاهی‌بندازیم به اسکواد نهایی تیم هانسی فلیک درفصل‌جدید رقابت‌ها باجذب رودری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28342" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28341" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeQDzBL1wwWCR-Rpb0zqLua_E2x_Sv2VxWZlQgssPBQTvyfQuzEyxuKaqWOPPSMXZCRTQGlNLMtib3fC2Qfx5lAGPd3p__eiDcIKHod8E-0K6uE1OjdeCnrwh6hbfAyinY0S8PdFpZWMjGCJubD6IeHxokc6G05yVCatDGDoe5j2oGxI6mkISJUHkIOVOmsI-_uLe7x6SKUNbhGuUHukxaAcenD4HnfwApyxn_NZarD0jCYGXOh8WTtRLseK_WBWYh9YhITnD3eyYqsj7BDUDJGjL56HBgxwMYJTEHQVU3BPw_thjdJl9U8kofkHHH6PJm7gBqCzUISyukVA6JKDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم ملی امید برای مسابقات آسیایی ناگویا اعلام شد که امیرحسین حسین زاده ستاره تراکتور تنها بازیکن بزرگسال این لیست است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28340" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO0moOmX0NFRuqPGjtJJkHVmvJMj6onHDOc3bxIQSlWffv1RcuojUMknTmFXB0xuTbH1CXo3MLJRVQhfEtKpXTZOxus5HnF5PLAsyOqvgXaIjEmvMKvJt8-7KzGVlC5UoOEoZMuMYLqcZkNeuWcLrTuEf1DYiFhp0uYe52MxP6N1u9dkxvCzuxcW9TguWlm_VTILPfBiCLWoymM856f5w9G_3Oem4MjruzOhW_8vGcqtURG9meEedoHX10JUH8BXCbFM1D5KIVD7GJYu1IbI93k-fjRImrYBUmepYl12HQ27Wq_F60zqz_uhxr-0saaUIXph7-GrG_OjN1PyaKGDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28339" target="_blank">📅 21:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYmsXiYeOqivvq4qyXCyJ6oZGChpUn8_lw0Dr5HG9sLlBHugLedXWOU-KrD5Zn--QD0LIMiCwHVqJbjIYxYGOwQEnHj6p4xEUCJzKTl761L06CTKs0QIBWJBnEG9Vjmxv_jYu6sPBOTbia5TaMUnLMzo3yTgDCIG4MbJiPi_C0Vch9xSQB86naO3KF9Ulnf1Jk1BQofmj8NPebY0jrSzdnDXI1cQ12DusNLM4nQj-dr0GaVziKJfABSeZuPSjd5ULyP9DQP8_cCf7XYDtw8LWcCEm-4ZAxcj3NsTRUzl26iSUSH9yDqVCMZIJ9_tEXaPwxsHoWLZGLFM7eYW9jFI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28338" target="_blank">📅 21:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAjCdbtFkXx4mYlX3R1-lW9pStwwF9fKRiEsJOeLxNfqyA9Nq_SkYwzHbzfjGDNKKMvJqF849i25DXPQqzbAflyLcrzLVS1T0urtgxYi_ZNmsw72kjNUQS9N6nvOX2PGOWHb3SwDIgoM5-Dpz7pRv-_ro1CghVL9qPeRRPTg0FqhIJCUsufH2YGDD4OmJwo9X0zge4ip16DPU2myQ1pyesZwRHPvhbp5iG5IUWZxLN9ycW8aXMmtiNxvVcA0I_K0yCZ9-dMd9Lwd7nXOTjL0nv4VYARN2gyOT6r_Sg1DTf-KQTlIeVfIeTzc6vuxWWfF_yUGOZwBipsFBRmeKyxmIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28337" target="_blank">📅 21:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28335">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDHAl9uMk-4D-DwV5k9GboQ7nwnm4cZNrQVks4P2c6YEtsXPvITBFpbhRNnwEoMUYSEDlv0PwXQ8CZp3fxKB-o7aKiXX0B0Gy_Jlmm5JCtIBktfTgEf0YrJQeUQ3KnqBoyd2pRNLaZ4UDJZre7E_6Cc7kzI_DA_id8erqqpqswwnWipeX8tRAIVdtjNnu2EahwtMmvcUTlJpuPptd0s_IlaUVE7AHyz1QGVpZgkoa6dq5ubUYOq2j2cY3xLmyEMcd6bGM78-l1TU5JFUPd3DJdAcPk6rEoyA_hDlqAzl8aBFhqwpeMEbLUmQGTk4iV26ZmHBff8rH8wrmUMROQoKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZiCTQ210nxxcu3kYXcHVHr5QPGCe3q5MeLZ-c4a_pEpcJ6RqC55w_1FgS7z-s6BMuRAVzH8fGi5C2Kz6VWjbwBIFi7NE88wN1bDl93h8iX5ROZQsCK09LVdgqVcrH9mH3-_nP0ZvGb_TImUTWRGs2e0TaWwHFa228y-_00dRN5Y9b0SGn2PKxE_oekQdQu-aVFvEfPx5ZwfxKBEgad3_6a3vErn48SvPx8YjOgBxsmxVG8U1mPuN9RjkqsmsRelgakmLIUo9_DdbrmkALmCaDcYXQd6gB8SbetW5YFjMSQ6xO774av6AyexIJ6mU7RmTe0gxM-ECss2R1fBxzzb_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدار مهم امشب
؛ فرار سیمئونه از شکست در گام اول لالیگا با گلزنی پسرش و تساوی پرگل و دیدنی لک‌لک‌ها و کلاغ‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28335" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=d0e21s-TxypGj8Fm5yzyiCuS4_jeY7vBq6avhKfvAYOGM-fLN-osEfkNDRi9q-3W37R8aAp3AFIsbFKbh55JnT8bFlfdJlszoPCMALTOJ-QQzzeyTL5UXeDZjhZ4_oxHdeKpmWbkEvYWlj4v_T4n0B89UsZ4hgwZsfksnZw9UAO6Eh_xVThrnHJyNxr16chEotpGJ5fioh1_20b_Mk0cID3h5-qRdtPgc1rbFsjE-toNT2qYPY5le3Bw8E7JyP9ViecLRxqRoyc_kJZf49fLv9SVdybRuvH3-jjbheIX3QWJVLRiL7t8Juwo3zHgrSidVHcFeQornkWuXyOTcvuzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=d0e21s-TxypGj8Fm5yzyiCuS4_jeY7vBq6avhKfvAYOGM-fLN-osEfkNDRi9q-3W37R8aAp3AFIsbFKbh55JnT8bFlfdJlszoPCMALTOJ-QQzzeyTL5UXeDZjhZ4_oxHdeKpmWbkEvYWlj4v_T4n0B89UsZ4hgwZsfksnZw9UAO6Eh_xVThrnHJyNxr16chEotpGJ5fioh1_20b_Mk0cID3h5-qRdtPgc1rbFsjE-toNT2qYPY5le3Bw8E7JyP9ViecLRxqRoyc_kJZf49fLv9SVdybRuvH3-jjbheIX3QWJVLRiL7t8Juwo3zHgrSidVHcFeQornkWuXyOTcvuzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28334" target="_blank">📅 20:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_QboGA2u7_K_ObHFdRekO6cLT2YdQ0fonAws0Df48_uo6sZNmcwsBd4jzdCT5tBdvJJk_IM03kdBywMfHEBTViYGtD-oeJy17HjvsGiPf7AnIr-dCG32hMeALtjAcJozzg1sc0PwVBj9M0YAD_lQWMAPbj_xnRtf2QiIBmwtmYbeCIO5qQm8rnKdkl2PuINeBHGAtjb5Bvoh_fDDPdqiEMso6m_2zCpdEOJValE5pDnGM5aalt-OJL1TUO4P74qJYkoQbYwUtdIf3HvD9T9xeRYzzeH6U41J2cFjF0RYdiZpObApagurmc_4_xb8soszrFRklq1XYjpVeWvlHKLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28333" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQCYm7DwznJrHE7AV4ZkNUYitXF8nePDr9GU4trgJaDeNc2wJF_C59-S7Lz_7L2dOi-UpKqVPsmYaDp4WhfeukkwUZX0VjjLCuUT_fKX4uU_shWnfdiOZ4VEhn3ubYFYCBOmgpzlgu8_WACP3A8167nYlslbfD77GN5qTTlW_x60IfGeM5H6e0jo2lzIWIVhSzwKyjlbr4yK5L1EeHCs39-PHl2MUX8mzMJh9tJXftW9jiJr8tkJ6E6b9JEzfO64sDyXaxHxpcE64kurcSCUuaa_YF1NckB9vqOdh4wQI1r8_2irvZLprhkIhkWsd_rrLfEaADO_8NPtAnwTlN7i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28332" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=jvo-HYwGRp3VLFze9rb4dS-z5SVeoOB3Vc2-eN35tztz5mepD9IRNvdqc2kdTN0FkoLtKLzcYWV_k5DM62tLV247ynD6-61nFRCzAU5vBjSJ9uBDVmvyyMmxiNrrULTTbznckhRakyRSyqF8CV8y476jl2SQunhQIDHMCGUFH_RaRNMiiZ7hiO1kQFhl7UgrNA0BToJBzovfpVPxwEkShcBes4ibqLbjADmdyjQAIZ8zUXjg2Avwo1HtZk6YTCOZ_QcJix97ju-eQIk3zY4mONLaiyG-KIPuW0WXY5pP1h_xOnXdYf7_6h4OWXaiLdC5f6cGh8p_-HN4_hHYjzhpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=jvo-HYwGRp3VLFze9rb4dS-z5SVeoOB3Vc2-eN35tztz5mepD9IRNvdqc2kdTN0FkoLtKLzcYWV_k5DM62tLV247ynD6-61nFRCzAU5vBjSJ9uBDVmvyyMmxiNrrULTTbznckhRakyRSyqF8CV8y476jl2SQunhQIDHMCGUFH_RaRNMiiZ7hiO1kQFhl7UgrNA0BToJBzovfpVPxwEkShcBes4ibqLbjADmdyjQAIZ8zUXjg2Avwo1HtZk6YTCOZ_QcJix97ju-eQIk3zY4mONLaiyG-KIPuW0WXY5pP1h_xOnXdYf7_6h4OWXaiLdC5f6cGh8p_-HN4_hHYjzhpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28331" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=FvsvnJ2Uu7LIPqGwgLc0BQzIY0Ua7mRt6n5kiFWg-1NDo3SG9F97sJ4AVxrjHeUjBIb4_KUyGPCobsAcrDQmaLyoQmrCOupSXokZ1uN8wfLxTgu7oSTXkpO9Fe_sPgd8u0lNGF5J1RbLu6jhEndvf8Rm4K1fWg8z-0pilaXlif0laXUWvh_BA-9G7ybd6WkFVrU3scaWQ3801t7wxCzKuDw5Pw0g894wafob0z82Vlwgx7WD7MXwEj5v_GxCXmfJT-Ldn6w0BTq5FQXoZ2NM3Eg-w-wslNDK1-XTHWIS51c9SJVdY6GcUSO6sUKNOedfZn6Fk-zfwGGnjrqe9fr9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=FvsvnJ2Uu7LIPqGwgLc0BQzIY0Ua7mRt6n5kiFWg-1NDo3SG9F97sJ4AVxrjHeUjBIb4_KUyGPCobsAcrDQmaLyoQmrCOupSXokZ1uN8wfLxTgu7oSTXkpO9Fe_sPgd8u0lNGF5J1RbLu6jhEndvf8Rm4K1fWg8z-0pilaXlif0laXUWvh_BA-9G7ybd6WkFVrU3scaWQ3801t7wxCzKuDw5Pw0g894wafob0z82Vlwgx7WD7MXwEj5v_GxCXmfJT-Ldn6w0BTq5FQXoZ2NM3Eg-w-wslNDK1-XTHWIS51c9SJVdY6GcUSO6sUKNOedfZn6Fk-zfwGGnjrqe9fr9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🤩
پس از کش و قوس‌های فراوان خولیان آلوارز رضایتش رو برای موندن در اتلتیکو مادرید اعلام کرد و این بازیکن درجمع‌شاگردان سیمئونه موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28330" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28329">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=XmHIxwUkVXLnvY5wxjw3jarBGKRKXFXWiHcAzH6uFbnIDf8tz9intGxdUQx6amDxjDtTBIqR84mHyY1RnmVpMWkb8zJvLMwt2IN2mAIVj7837S21FNRhUuVZtd8fa6AWMlcmr_QJFTVS9jlbheX42UCQ1SG0B16JmLA2rwuthUcig_v49lGO3dxYsDjgM8bp_QmiTvC2CUm3A700G8pPiMBaad0_QVxQesEplvr5Z16vjq0ZI4TnTXmo8kedRF6R9ese6xyOOUlwKJAgigxuZNfysEVBQPXRSsph9KS8Cy8PioRooh69DrAVoZMzkXj1rjRXxloHoHrDdoIWDixhOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=XmHIxwUkVXLnvY5wxjw3jarBGKRKXFXWiHcAzH6uFbnIDf8tz9intGxdUQx6amDxjDtTBIqR84mHyY1RnmVpMWkb8zJvLMwt2IN2mAIVj7837S21FNRhUuVZtd8fa6AWMlcmr_QJFTVS9jlbheX42UCQ1SG0B16JmLA2rwuthUcig_v49lGO3dxYsDjgM8bp_QmiTvC2CUm3A700G8pPiMBaad0_QVxQesEplvr5Z16vjq0ZI4TnTXmo8kedRF6R9ese6xyOOUlwKJAgigxuZNfysEVBQPXRSsph9KS8Cy8PioRooh69DrAVoZMzkXj1rjRXxloHoHrDdoIWDixhOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28329" target="_blank">📅 19:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=LX6sTBXcAgzpEm-Pe8AI4L3i9AhxaSPEwv55SWuznulRVDU1W6sRAOh1Ln1S45usIDDqz_Twl7VTVRzq5A0olmV1XJUURlBbeJmq2tqNJ4NQqwuTVRk147oUAxL-s4MgwF2feWwqWMWmsGrOpTfCYHxKIsoseP4DvOcaq-X2p4b6VMQH5tIAQteuu3rNPdqxYIPcD83wxQBs9Hgq1gx5qOFURhIi_r7LUpYrdx9aqYv2eoxXr03uek1pljungZUnfyySEU2HOJvdkN5tzxV6FjgVn18JRzZrDjrqObJDeG_GbKMSQhLxaruyUXMCGCH3R1RKXdsQ-cFYvUk_c12hag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=LX6sTBXcAgzpEm-Pe8AI4L3i9AhxaSPEwv55SWuznulRVDU1W6sRAOh1Ln1S45usIDDqz_Twl7VTVRzq5A0olmV1XJUURlBbeJmq2tqNJ4NQqwuTVRk147oUAxL-s4MgwF2feWwqWMWmsGrOpTfCYHxKIsoseP4DvOcaq-X2p4b6VMQH5tIAQteuu3rNPdqxYIPcD83wxQBs9Hgq1gx5qOFURhIi_r7LUpYrdx9aqYv2eoxXr03uek1pljungZUnfyySEU2HOJvdkN5tzxV6FjgVn18JRzZrDjrqObJDeG_GbKMSQhLxaruyUXMCGCH3R1RKXdsQ-cFYvUk_c12hag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
شعاراحساسی هواداران تیم استقلال پیش از دیدار با شاگردان محرم نوید: سپاهان دوست داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28328" target="_blank">📅 19:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=DSCG3INgyWQzLoySpSX59t9a83iC3CqBzbtfPn8h3eB4Nro0kWBAQ6qlOJNj9lXDrkwvK3WBBs4rhMQaSra8w_y9Scck47pro7yN1CZvEptZBUxUm1QvkT_COzoY91bmidQSr9Fcb3KT_H4lcPmtJhXpPj2m11-IIPfuSD-PXjCotdkiOy3hQfBZ2mYtioIyNcK9FOqNsye0YvWZ5L1fjmP4J4He7Pz579jqY_mlanChofFxfhEYrtiyk9dWKHndjis28_5S2YBVuxJH4hKo0dJBS1DGYXWeBa0zoTAHVZbTQsXGoF2ZfB5zan1J8mTRCf7i-AamxMQOZO6l_8M4sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=DSCG3INgyWQzLoySpSX59t9a83iC3CqBzbtfPn8h3eB4Nro0kWBAQ6qlOJNj9lXDrkwvK3WBBs4rhMQaSra8w_y9Scck47pro7yN1CZvEptZBUxUm1QvkT_COzoY91bmidQSr9Fcb3KT_H4lcPmtJhXpPj2m11-IIPfuSD-PXjCotdkiOy3hQfBZ2mYtioIyNcK9FOqNsye0YvWZ5L1fjmP4J4He7Pz579jqY_mlanChofFxfhEYrtiyk9dWKHndjis28_5S2YBVuxJH4hKo0dJBS1DGYXWeBa0zoTAHVZbTQsXGoF2ZfB5zan1J8mTRCf7i-AamxMQOZO6l_8M4sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28327" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=IhDG-xgwDMOPcj2lIZ_fSQb0PKq_ZsFH6HgzUofFaGGanKfk2fg59xxdmpK-EJ0cWrHoquVN-uzoWTaFq3rz0cor8G493yR2bqGv0r84nAFE8yD7O3OMM9ZJJEVHNqtzPuU7XuiBK3o1As-u5JrVgBJSHZzXN6d4gkluVkd1v_pHMKEw13i17YIQWjngD3mWvH_DStgrvAfsvenLPe7urmR_V-qFN0TUaoqZt8NtPUQLReqZg48ZXE5_6WhF_nXaC7kH0QoPZQtiPxfRnMZXGxhrlmuaSkli8gR8a-OxzTeo4uEGT4UxsFFFZdqXAwjBUmqT8vFQGH1VbEZ0B2eFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=IhDG-xgwDMOPcj2lIZ_fSQb0PKq_ZsFH6HgzUofFaGGanKfk2fg59xxdmpK-EJ0cWrHoquVN-uzoWTaFq3rz0cor8G493yR2bqGv0r84nAFE8yD7O3OMM9ZJJEVHNqtzPuU7XuiBK3o1As-u5JrVgBJSHZzXN6d4gkluVkd1v_pHMKEw13i17YIQWjngD3mWvH_DStgrvAfsvenLPe7urmR_V-qFN0TUaoqZt8NtPUQLReqZg48ZXE5_6WhF_nXaC7kH0QoPZQtiPxfRnMZXGxhrlmuaSkli8gR8a-OxzTeo4uEGT4UxsFFFZdqXAwjBUmqT8vFQGH1VbEZ0B2eFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه بعدِکات‌کردن باشروین حاجی‌پور:
بزرگ ترین اشتباهم وارد رابطه شدن با این آقا بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28326" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTjgP0nXbefQNWmaNXyX_g53OHPjbGf4Z2XAuw31zAVtDZXFMUyAL8qWKllPTlvq8Xs1-6izpYuW2b6MwwwGKXDmVx1sbzeyxtCFoh_qbSkNokPwFrtrEZtHg6uWx_nujkecvEf4q-CRUjD_2xOL7Rcde1_GiONNfJqfQCsPDt8W0Qk928fppvu8VxNH4d3aL7XkR72MtYvMPwXJ-t5YTNsgagFB5mxACaa8TJOPmCsjrNeHDRQPPbuNbaSL2msmzPaHe4OVTu4bABEta7-sb_E2o7qvH1OPuqJirnl7Iug5e2HPovukMI7qK9BUt7JSZvxXtzMiGrXLWoZcQKcsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
10ستاره‌تیم‌منچسترسیتی که همگی بعد از جدایی پپ گواردیولا از جمع سیتیزن‌ها جدا شدند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28324" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgVls_xQsRgQS5GeHRNhL9fN9aMTBaIpzHwko-4xtZNDkQ_FnlwW3idMLaSxtya-uFnhs3ULaJmzkYCMWw3wqvgaI0_dvtrwVh5ytVLe1-gWh8jI5hGnsDI6SUdGzAFslqzftAbrvroFaQRX4WA0hWDeyADcCOjRPxIXXEN4ODXNf5euF2_3MVfQqqzoBvdGEBP60g1Gf20LdsirSIVMzqYXgvsO1NnMp58UsaJRk7QfUtfh8PGB5rZUD3RHvFd2QT6N1O-BiE5kcanUBDOmg41P3RC97YyWuMCnLOVB-_YuDx0WxCQ-_B-ewB_ZRpauTa-KoO-N90ereK_IhT023Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28323" target="_blank">📅 18:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U299K_PZBSWCNCVbd69isOnXFBmGWzuHanCU0OMiQc_ZhpLRn1Izk6pBuJd1W_thH2uDwL_qLM9JlfSUWeEF6A3MC50tcp9_yjyKDT_TbuL7yx5Q0lGmALgiuC4CudZd0nlg7VwLDDCFRexSVCN7wNHtCmPINrgpDhYbKfzZUsKEm8soHHXUJya7ksnTl55fJGWJGQxIdSky_lWwctmOHVp6gUUEI9JmX5Acl9TR4v3G5H_NY5YozgEbZIToO_85v4x3Ceq6Ks_rqCnklybChVXKegEeEReRXGs6vVWtXl7odl9f81-1Ic0nIS4A4LkgGi5pHwCmTG7dQ3a9TlG8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28322" target="_blank">📅 18:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qppc-m5_1VBjMpJK2P0rrvnqd816xROAJ6Z7r8ckFvEPfbSdxV3JusIX9efIJQvKmssN7iWZhxqfsbxqYPuTWpCrBUNmTJZlutavPmCJn7kqm5fp845LIN8VmWONY1gsvLQ4_7d0-LLyAi_4shp3CMnCGouGJ00z3RN7zxFmjrLQRFvkEcszhuAEhTdjhqmiNYq7JqQjBkd4m25oPoZaFkxAJmMfvmPpwtwwkmmeRqlHlFJHoi8Y5636hgatgvAW1DcUTZ3UFeb6gaTfSgFdzCFedcgqPD_6N08VIkUXibTOvbiH0jyNvhbJIYXoVhr16Q9-U451JZyVOaMEe6JOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب استقلال برای دیدار مقابل سپاهان اصفهان؛ ساعت 19:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28321" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdVAuig3X--6KeFBKdnIiZg2cqPJRwt8OSfkNFvh6BTs50rOLYcKGP_v6qwkZDRpazsCiKw-5MJagoAk6GelAop6xZJ7zopDDmwAAm6_hvCx9-O6TZM59iBMnyf5hA4QuQn2_BGuiw2lo6D_BecnOJmrjLxuqeY7BVuRnkgG6kyn5mIm4-4QN7H0O_ZPZutTyOyY0WVoIj3SxXA7JB6LG-mWH02o5ogv7NFYaRQxFPdbZ-dEM0L6iDe9WTBC6qM2vSgog42ZhFiI3uSWZdEnZZ_6PfTubGUthKlclc9Fmxu9JNN_3jL7APgnUCkWzSA3hGUFjjgW7PyCqF3tITc68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28320" target="_blank">📅 18:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1FyfxfX2MsqNKXTHFmAJYY1B4R9sTjakbNfeR_q0Q8LLdF5XU3dLEwAOJhCFiRJMOczD62rx-Eo8gY_WsNK7vf3Yq75uaIoJCLIU0ztySoqMrNH_dPQRKugWyVrxSpFSrMaM5g_UrRM4wcHVzAz3Ai4hBRZIbwfCN0xuGfOXG5N4RvVD9lFQec-HfA3ItSJtJgL_lks2NG_ZQ_7Zn7uJaCXcwpKs6zv0ef1HjwB5nGKCmJtxKCFHDhu7brKt4nbwhyv3faXd-5KcMDyyDD-ZBtcKSirSJ2aWQqzVWRQXJO3iSBOLh824AF_UA4Oqn_-t97YkC7rfGLhs3bj-piHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌‌ها؛ مجید حسینی مدافع تیم ملی آمادگی‌اش را برای بازگشت به استقلال اعلام کرده و درصورت موافق بختیاری زاده با او قرارداد میبندند. حسینی از نیم فصل میتونه برای آبی‌ها بازی کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28319" target="_blank">📅 18:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOdrXF9wqEAtx6YljMaaWK0sGJkoxGKHm-Ava_M7J8REdUZF05idBES1uLtieIFdratJf0jtyfJevXOHNYpUvSRfMALs2t5Kz-1W48U5l4MqRBktVgH09LvnLEpRLC1iZejgIRmpKgTz95Zg2RLt7UAqDdridhOUvGU3DlKV4mfiaK8iBwcc7dNcqvQuln8Hu8tPsL4VWapEsqYskinz3NGNL2vJgjWBwAB5xbSbKRqlqJibeTbp-7mPb2WXu5A8bXLqRnNsrR5xpRqAG5-DtyLYkwTihxUAUtHowCIen6mro-rbaMphnhjiI0XLf3yi7Y45M0aHdEW51zhGjFj7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28318" target="_blank">📅 17:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28317" target="_blank">📅 17:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28315">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5-yU-FZmHu1AjnDA5a6XesERKeBXzOv5BKdFo90pD0vJq9jQ9f2qChQaHU9p3kwssRzS0IhYmLF-fKl9DvTeMySO5kmJduE6KH2ReXGT4dQ9S2fZEW_h_02VMvUcR2l3AQnxBZZZ8bydq2WjXm7oVCqWjk8SxpEVWSEgMoRbAO9PHd1QGXJPrQgV4FkR0RJi7re5Q5zR0qlaQ3mNPWSzNKx_PIEJNROZCH42m64Q4w_kQBpjIDVU6sPVH495vHPMhKK8BSgkGtSAYcQuhvI1Tc-5xqpuij4iZr40r1jSsA_ra9Q9PMTOdCSHg5EQF8HJX3i0sNtHehlLOl2WKhHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=A_wHGJT6UXdvP3J1J_GFZdVnVL007tHPwVqdb_FEgubVTjVUHXnggsuP1lMz7XlF3fRaflrIW7-PuWxOv9_bNvm7V3U4gDoBcUjfxENXp1xcWYs6F3U7kQyqocwnCUoxMKCJdM05HIBQQ8dp3ji4xqAX13NIrNLq0V3HXCJfvFcCfFqqtLxfg9s60T_qdDGWS8G2POaxjhMF_QXEZYVUnWv7FuwORR7SiaBInOR8nSo2eJ9XejfNCv9agzailDWyA53V5lCiAcYL2LR-o_T1-CfRfR7hOGkRf2MNH7vUa-H1t7VMpYECKakhK8ZPJLP4thPZl5ttWSb6bGE6-07L5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=A_wHGJT6UXdvP3J1J_GFZdVnVL007tHPwVqdb_FEgubVTjVUHXnggsuP1lMz7XlF3fRaflrIW7-PuWxOv9_bNvm7V3U4gDoBcUjfxENXp1xcWYs6F3U7kQyqocwnCUoxMKCJdM05HIBQQ8dp3ji4xqAX13NIrNLq0V3HXCJfvFcCfFqqtLxfg9s60T_qdDGWS8G2POaxjhMF_QXEZYVUnWv7FuwORR7SiaBInOR8nSo2eJ9XejfNCv9agzailDWyA53V5lCiAcYL2LR-o_T1-CfRfR7hOGkRf2MNH7vUa-H1t7VMpYECKakhK8ZPJLP4thPZl5ttWSb6bGE6-07L5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28315" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28314">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmh34n7gMTUNBhD6Ekolz7SJREj1Bb4MWRA8oKbghv7bkAqeUmbSiilBSNTyazHNmF602vMPnq9xISf3V2QzCqLFATsZhL2bIOaxSQ824baZ9WLesYNbUOgvxVY74aJU_C295sLtCaP_zZV66wgtQnWQd8vxLTwVe7RHSAzhv7WZ0kBWJB5meZKXZ_xjnXRvhhDcipWFvReHVTeKZrBGF5p_ftFudkqOl-AuvqjclkUi-KES5tkasOPtbYKj_fRcQPwg3ph_EHjhTStzL4C5UKw4my7N19uLCQifcHGXMhSrd6khTrLNtT5yxdzPpnwNHY4smJcbA4W3xRgfU8ZOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمد عمری ستاره 25 ساله تیم پرسپولیس دچار مصدومیت جزئی شده و ممکنه کادرفنی به او استراحت‌بده و دربازی‌حساس‌باتراکتور غایب باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28314" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
🇳🇴
واکنش‌جالب پپ گواردیولا به مدل موی جدید ارلینگ هالند؛ هالند دهن سرویس بعد از اینکه بازکات کرده اولین نفر با پپ ویدیو کال گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28313" target="_blank">📅 16:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr5zZAgIQi9h9endlBlGtEHHbCu_KSCMP4VRFCZCKDafQMg37aXRVDX1XKXg8qd5wKJR_wuiNv9PRVclXjBuiINx6G2OS986jPmoBDc4Ppax7TcCCCPq_hWkdz1cedIyBWsZYp6Br6b1gb-EP-jwBJsz_3qL9vGLFQHKK96t0MWszZNhunMku7tKxxha43b1LYvcQlw_d6V2Sxp3G3zvBCm1UA7iuKiOcLOeKFxWNKeyT2is74o69F76Bj3XosyHEvUZDaijeXnU2KzZatETKD48UjgiB49DDw1_aRMlzoaudHSfVLPZuEvFcCKQUeMwBd42K4nUyMqbD3_KQoPp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28312" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnt7SWENw6FIfqB3M7NvuWOyJmtppTXjpilkL7YDX9KTaSsgVlEHF8AZWxQJxE-1Z_hCgMw1bJdOaEpxRdumnQ2b8_JYxdvBKTxLILjrkhoRKOskfl7e7aiXRJ7FhDeicZHZ-4FqnGwYDXVaryq41fGH5ziosNu-6-TJYZGFqRigl9iAZaqUuRVy4Cm_oX_nQu3kpQ4Lljj9UnfZ7iixAlfnCEGQ9I17wrDTC65zKUyd948DxX47V5yUNVtsszRvq3YQDkwv2lVUu7SFC-ki0EWiVYx2sSvBbvCNbJ9PmenMFam3dLl4nZdqhAXl0AqyAa5-M0o8YfgM4AVs1JMtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ازهواداران تیم شباب‌الاهلی امارات هستن که علاقه‌زیادی به سعید‌عزت‌اللهی هافبک ایرانی این تیم داره و با پیراهن عزت‌اللهی رفته استادیوم مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28311" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu1MCt1A694PY1rfme5B9qgmHo2-P3enRiAWD9sFiBNXY6kNlLKrYmq0Aqqj6oqS7ZzWc4BiMV15j8sdlPT4N5cb5p9TcvZZ95zNAHEZDkzpcz44s5H-7rN5Er0VsEcvs930DB4_5LDri5WAY4OHGVznJcqbU3TRMVAgU_s3UaLjjLHJi7YpDeUEuomGpfv1iMQ6WFlibXTDpUlliYFUdgekvdnp2LJ83yecqHhHtAgVIRkXgMHuYwWyMunt6b3jaJ99ESshFWZDrpTYltc9lLzM0McpRxPuguoxwkvR_fohxdNuUPMIfWgyz3fhTH-GLAKqZHnmOKt0e-TrP0ZeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28310" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28308">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28308" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28307">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMduFw8TSGw1cJp4FuatQjkIMA53Y1inTXjRRm1nan1up80ywCSBjRjvDnSomv0BsB9oPXQ2aFImb3IYmjdaPBMa6p0fx_m9fJq1f1a2Zr2bfhm8oOYmjopj3J1dzalltkHqw8J29v8stcIMJUjk9l1f4Ua81z4Hb31nmzVQRF_mQD9JS89ykMkoiOP9TPjAfNnl765Mlp8-QAL5o0L1wT4gZNM5mq9wm0eG3RLuA8BKtc-WPb6hV9rFqkRU6Xp5ykwT9tWfH3v9Tc0FxhtnR6uoY_b7A6dnIvPCYF1SK0Hq-yo4nvYsu0MKaV2L467JmVvwrdJzwEs31ssuFRa74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی بعد از مدت‌ها موهاش رو کوتاه کرده و مدل بازکات زده. ویدیوش رو تو کانال دوم گذاشتیم میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28307" target="_blank">📅 14:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28306">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌سم‌رو از فصل جدید رقابت‌های لیگ عربستان ببینید؛ چهارتاشون به یک باره خوردند زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28306" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28305">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/powXykHs7Fs8jmvfNxd03tZIOdPynUmOz6JLj7cHXPcZTTDnTOy_JKYx_fjy2ZNMIzRupH3sWsJc5rzq9me_S3htf0h81g-hDMUz3CiR_oyGX9Yq7SWPb6Ey-1O8Q1Q6QM_mw5sMtlfP6ZT42MmnApV5O7CRcV_XMiQtraNZER6EGy6JVgYn4eDepRjkq8JdJ23YmBPJhM4l219ZR2eZCCpZrNydyV9EhSqp277h_MV3-DwDEBjC89Tvm5SAfavIuNrlYujjiFgLiDzw1u1QiQ7Rs6EtJ-q8ATii-jbzE4cpY0SnAf4CE8Ohq_TW9RcLLdOvoOeFB9EODrMK8o_pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلار به 200 هزار تومان ناقابل رسید؛ یعنی هر یه برگ دلار بی ارزش برابری میکنه با 200 هزار توما ما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28305" target="_blank">📅 14:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28304">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy48jQdp5YAe1uwZtr801UpApzssTASmninC4PjfOgBPmFVMBnT0j71g8nN8ePeZMXk-g_CL-YaEWyXna14TLt-OJYPCuuUPJ385OL5pdi3ifHr6XyV56tXfa8xuB12zPw_bXgyT6PUJZJfVt1rChVJymbnEqmcF3wSLSfApllkXQvZuvnJQY-k9agMXMZ0nyoGlT8HKXaxr2kq-Eg9dbd7RRUEH9cu0eP1ZGnQIdUXPsFKR7xtd8Cr6lPG68rZGnbPzFFURHEOh3Y7g_xiuoyVZA-lgasfzgzhlvQQY7-eLT7icJrZzJ_ooydAw9K4Wd0Bz3UFVhKtmypsa_Dha_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارلینگ‌هالند مهاجم نروژی منچسترسیتی موهای آیکونیکش رو اصلاح‌ کرد؛ الان خوبه یا قبلش؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28304" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28303">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBEJN3tB-uJl4Q3rU2mDRGwBAXqupXKP3sBgC7bJsHocJbFyP8XaN_k4W1FXFNdNPZ6UaYNM7KxJhLhez1rwX3lopbJEWsPr3-g4-PK0rvDRpHKJ6R1jRlI-Olm9_nU0Ji6AttXNdaWCX-XvA4gMfuuFYIaCeeNUuIa1snNM0Re4_rFbAVU_bD_W4tLZ_NfYmhH9Gow2qLlRFK_fBMEq6U43GldBsmVUIbNBS3ifFcATUHXcvrQoMYetQpoRgiMHxnxIo5g3AJTS6CbWHWRBJRtvqwY55JXIEU3b_FG_-doPnWg4Sw8OdUUd4-Xu44G0Zgux1Fr1HkUkAy1j88lIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛خبرنگاراماراتی در ادامه خبرش هم گفته مقصدبعدی محمدقربانی یکی‌از دوتیم تراکتور و پرسپولیسه و سران الوحده با هر دو تیم ایرانی برای فروش محمد قربانی در حال انجام مذاکرات هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28303" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28302">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=BfagRPc92vDxK4_0Ll9CQh5av2LIKsddKETOU7ghCjuvKacCyy20za9rKHaFtWl_UPgM7bc8xqns5SNazUXIGkSfFx8pDQhJ_ehuwT6nqwnvpuKeJXBrwIdQjTFWwMTqWWXPE1_K65fC_ml2Mq-WamcFLfIODttTyJMLxTx2u6AfHMHVxtyHTsRUmbB2BynzTyFhMGRtEQu-ysFtfhOzdJMfnLyKlSBz3agp1Ns07Zoebe9ffTaOjBEDOM0-a6XFxp9QsBxgjY5YWSQKrFuNu96MKLMKkyXkQdxuKjN6Z3suSeoLaac-1qH1gQcXoTOxj1e1Q0EGN9zynWUyXtCYLV_Z8iwnU55a4cj8nHRVkYH9kBMVUoqDdQJ4gZseX2tUzHKIi0YgQoYs9kVK72Nx9E0xTtAA_n4lVprIY5eEi5sTJLAwa4DbT_lLBHOJZJg03_sGZN7xTIuLEoUVv7bemqGAqTa0Hlx0veZZ1qUaFOTI4KgH_vsCrjUZytwSrwK_Dxt-6HV6hWm62oFvKEVH-JUt56Y5X2ZcWK3u_nYhHdw6HtO3wd1n5fMBZMjIGNw4vz-hMSbFF6l20nHlfWJb-r4FvLplZ4rhWo4v4fbAuH0hJp-03EYEcou8XWboW4vTTF6867RcWojwB2hcLNOKj5zrgdMDehSt4ZDv6hbNQKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=BfagRPc92vDxK4_0Ll9CQh5av2LIKsddKETOU7ghCjuvKacCyy20za9rKHaFtWl_UPgM7bc8xqns5SNazUXIGkSfFx8pDQhJ_ehuwT6nqwnvpuKeJXBrwIdQjTFWwMTqWWXPE1_K65fC_ml2Mq-WamcFLfIODttTyJMLxTx2u6AfHMHVxtyHTsRUmbB2BynzTyFhMGRtEQu-ysFtfhOzdJMfnLyKlSBz3agp1Ns07Zoebe9ffTaOjBEDOM0-a6XFxp9QsBxgjY5YWSQKrFuNu96MKLMKkyXkQdxuKjN6Z3suSeoLaac-1qH1gQcXoTOxj1e1Q0EGN9zynWUyXtCYLV_Z8iwnU55a4cj8nHRVkYH9kBMVUoqDdQJ4gZseX2tUzHKIi0YgQoYs9kVK72Nx9E0xTtAA_n4lVprIY5eEi5sTJLAwa4DbT_lLBHOJZJg03_sGZN7xTIuLEoUVv7bemqGAqTa0Hlx0veZZ1qUaFOTI4KgH_vsCrjUZytwSrwK_Dxt-6HV6hWm62oFvKEVH-JUt56Y5X2ZcWK3u_nYhHdw6HtO3wd1n5fMBZMjIGNw4vz-hMSbFF6l20nHlfWJb-r4FvLplZ4rhWo4v4fbAuH0hJp-03EYEcou8XWboW4vTTF6867RcWojwB2hcLNOKj5zrgdMDehSt4ZDv6hbNQKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
به‌بهانه‌دیدار امشب‌دوتیم استقلال - سپاهان یادی کنیم از تقابل فوق‌العاده جذاب این دو تیم در شهریور ماه 89 که هفت گل تماشایی در برداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28302" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28301">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=kQQo2BaLBNCMVAdpkzT2cVbFXZ7EImakYsukD0wyDet4DTf5SdWGQDc38OMwe_houCs5m8Pg-Zc5ldHD36JDkYzvqQ3RdL5ovanDnKeq7u383kmcWFgkfc5Gtflqkuyyiehm6vFrc13TT8YTqhZ4bIBoNoIa5e-YSJuPx9hyx0y-wTm4DTfeMN6Aq3rnT4d89hZGPpyapIm4bwPMGcUha1tMwcri5qKo2mdVIlfXi1xT4hM1b5itexhe13xON2T81-6y_Px45n-ki8LvCXamqD1w8OMdaXSZcJzj9Fp4b-civfVv-VKRfQbwdbBUgEfzKi0Rhr-n5TTAjbx4HdTJrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=kQQo2BaLBNCMVAdpkzT2cVbFXZ7EImakYsukD0wyDet4DTf5SdWGQDc38OMwe_houCs5m8Pg-Zc5ldHD36JDkYzvqQ3RdL5ovanDnKeq7u383kmcWFgkfc5Gtflqkuyyiehm6vFrc13TT8YTqhZ4bIBoNoIa5e-YSJuPx9hyx0y-wTm4DTfeMN6Aq3rnT4d89hZGPpyapIm4bwPMGcUha1tMwcri5qKo2mdVIlfXi1xT4hM1b5itexhe13xON2T81-6y_Px45n-ki8LvCXamqD1w8OMdaXSZcJzj9Fp4b-civfVv-VKRfQbwdbBUgEfzKi0Rhr-n5TTAjbx4HdTJrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28301" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28300">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDzRtccbw-CsmeegCl8USyQ00ucsYbOewtyg__qThg4LUWFPX9_h9-7iDEAUb_HrH6EMCRH_x9x1qtFIN3Ol5-GxRFYQPGRxnfBcD2IOPV3hWJqdjm4F2W3r34lkTco8Sa8Ji9gzKJ1ccKq8FX-6sgtY5xxoJIhlVe2vC8bKjGz8Nv4DL3XQg-uYuJAh9yW4Sb1Y8qjhQuu2JQuPEwmJ5G7oeVJujEguZgY1UxoDn7nvpivC0Z89ZhGOHO7rPAxhNU0S2aTWYy2rZZ9sdgtchDNuf4viK7PpHfPW-yM2kIshmzd8vwxQFTSoDtsmqLPCQZGZXW_ZTTBmGktXTyYbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28300" target="_blank">📅 12:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28299">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTSV_h4sfQPjN6W3qgnZ-mhgsBtVVdyAMHpYG2dPf7f6bqLQCKQLkHZ-wBHbbRNmyGF81JKaFTxYWfYvY4Xw2JqfvZDKrJxYS-9ugr16kqBka9CXQzD7AlXryGQhhZVz8-IrZuPh1WzBM7bxXOlKHmfdRSCF5u05jdGoTXmSSOlIocO4nAIBJ-0JZpRQMfbTXqBY_bNlDJnogK8iOFtBP5QfIgP2JflNxOJRXKCOde9RCy_uK3sYS4iqZq5Vr34WERoFzEfgEUP7bdjGcThClHd0MM2xVavkUBfB_cb03lgonHUgGH2zz8J1YMBzW5TZa0kpNJADoKNbcSxS-1L7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟! پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28299" target="_blank">📅 11:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3ahb3iPa7oq6ALtQvpIcLztDoNqf09kOdWfFUDIuPmdlSpYoMmiFRPWV_RogHTBbDiNt2Ie3qfQmmwZ5mtJD-ZGPnvqOcQyMoZhxGsP_aoGp8HAj0YaqaGdRH9lglBV0aY2s6sGxCvdnd2bHANaJRWd0FTikRpq657QRILFJLHJ4QalAvlCm4YHIukQpxTxPrqmpwROPEcZDyIWBnwdBaB7po8aS91ylutmcgsftYVtFdWO27TLQZ8yw7HuBmshLlroPgzKmOvlFHPH0tgatCCkmp-kRaEtu_OZmZExgkOMBq3tBMF0jcKsxILdLh3KR0YRYKnl2m1ETXaOWN_b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه‌تقابل‌های دوتیم سپاهان
🆚
استقلال!
‼️
این دو تیم تا امروز ۸۴ تقابل رسمی داشته‌اند که سهم سپاهان ۳۲ برد و سهم استقلال ۳۲ برد بوده. ۲۰ دیدار از تقابل‌ های این دو تیم نیز با تساوی به پایان رسیده است. درتقابل‌های لیگ برتری سپاهان ۱۷ برد و استقلال ۱۸ برد…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28298" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cvd0ZkNioYVuFHjPjXGnyQrJ3W-1QNzH1-SQTDm3F9cM6nnhbNOuzjWQuzuYjP2OjFjqVJoCEExnkdkhnlBEBdh3XqbwWAzsvBVintiwSA05oRVIujdKZSSlgHuHl1d75YkDFabKYQ6gIFbn3cKsFYfR-8Sy6WsJEZsqEHeifWpXj7nnL-wy2EBcFa4tz670eESfG7VJkHIdnLRJP6Gb7Aeq-E1mHNbs8GEDzHH6JkmAsHlEGmFmOCAY57L3NW4NepHpphOXmyfMwleuqlhHQx5jRvwRCr_4bMKTYCFMWcOb8Mr9J38k-fz0KZgWTRnEUYHi9zecNFJIu9kzVlE8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28297" target="_blank">📅 10:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgzm2bFQgpEjSAhYH2Ed5TGZwdM_RKAfb40Fgp4gowacCRZpEW-nqYiJWstvWhRxMmmLjVj77mwDMrlpirO_YsUpCpH9jpjE_aiN-Tg88Ffy7AZ57WbhImlXVYO3swk7uEqtxcHeXwTEopO2CKf-Qmi9_tunn4SsX-mRXoxJHyATEh-Mr0CZqUYJAwQEn_9GtcOSTi_ZJkHuuehB8Cp0hIcxPcbBSmOCbbjlbe3Pq_YZTR0cst1_SnwG-tFkjS34cT9RkVGg58lZM9VWwxXX9tJTK5jcRGg9VcWI6KAdgPHH7ge8K2LeSGEeONH4Am9nNsMk41r5vmEd0Lffv5Mzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28296" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVKkqvxcSkI1VyyA9c1o3m0dsApoTm210VdpHyt61Zv9b6_clJegZmpcsG6ffhlI75-LmkEQiwYFvvITL-cgmV-5wQ_roGoA7TVNaE_nt7g-VXrKDU4copAC5Xd54RJ9OEn3an9eXDxmGZx4yD0AOl0zQ0c35JimI3r8_4qZ3dpuQ1EdQYwy4-XGPfb40d9d0zEinBKfjYAIpND5Nr9IYw_xG_VpxHv63fwZqwVr5kpbLRDyaLuIO0yJwQdrJ1LAxCf32hnAGajyJObGOe9XWBh6SWsxYnFt70aaNityVse3Qm_aaEa9_vR6sJCZFefKLRlYT1Xx_HovLwPUfr0ffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در سال ۲۰۲۳ بود که لیونل مسی از یک رستوران درمیامی ۸ پیتزاسفارش‌داد. صاحب رستوران خودش سفارش را برای مسی برد و از روی احترام به کاپیتان تیم ملی آرژانتین، حاضر نشد هزینه‌ای از او دریافت کند.  اما ماجرا پیتزا فروشی همین‌جا تمام نشد!
‼️
چند ساعت بعد مسی یک اسـتوری از پیتزا با نام رستوران دراینستا منتشر کرد و همین استوری، باعث شد، به یک‌باره‌افرادزیادی به سمت پیـج پیتزا فروشی هجوم بیاورند. تعداد فالورهای‌رستوران‌که‌حدود شش هزار نفر بود، در مدت کوتاهی به بیش از ۱۰۰ هزار نفر رسید و این‌پیتزافروشی خیلی‌زود برسر زبان‌ها افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28295" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=Ai06Tw2j51VqNQ-9aT_NDh9LTraeeWtOEL3Q_qrDRl9EsdLUZzesK4A0Z5peP1RXbJaiR3_68QUaNHYUByfB46CTaChGuyMDbWZzqc6maCYV_cy2g7cWO_TFjDAItFz5238RDYO1ftO0hrNoN8aiNMuZn_CHBeVaxcL7HshfSzvxYPH4Ul_-eI_zd4_aoZUe7ItvtiNwagsjeaqzNYKaRAPnzx1iFMVhdmShTtA4dK5PlkK_O8p42reHc1Rvk77PE-3beo04TUarIv_N0l814Zg3lOwuqQm6uc_9_ghf2kdetrAvHO5688OOaQc2RWKpg2Em_KgcqeYlg2v0emkdPFkkkYpmJeAGM6O3BK3T2Y2rQtPdyxzWVUlsQY_r_24wZ9Ve_XWSw0FpqkfSmNHUeg64hRAJ2nT14oOGxXijwAOytIaaZWfSsjrchU5XBJe30XmnYyPHWO3FnQGvcSYA_ZRH8uoT2XYiRjqNev1v_ilC2gqYkR62RakbXJ90ycQ_vQ3unqmphJyU1nDycJdMTe5wNPUynVP7l-HEIkxqTWINJR1V18XT2BW--Ew9ZVds3QKgDBmzv8ICIAncVCF8zcXpHChBiGG5KE2mIQFJtQPLJmKrVjHdSgqC-y0_p4p9Zwow-SqMtkf1MA-1IUIHda_yAcbLd9YZnCT9vzX5cAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=Ai06Tw2j51VqNQ-9aT_NDh9LTraeeWtOEL3Q_qrDRl9EsdLUZzesK4A0Z5peP1RXbJaiR3_68QUaNHYUByfB46CTaChGuyMDbWZzqc6maCYV_cy2g7cWO_TFjDAItFz5238RDYO1ftO0hrNoN8aiNMuZn_CHBeVaxcL7HshfSzvxYPH4Ul_-eI_zd4_aoZUe7ItvtiNwagsjeaqzNYKaRAPnzx1iFMVhdmShTtA4dK5PlkK_O8p42reHc1Rvk77PE-3beo04TUarIv_N0l814Zg3lOwuqQm6uc_9_ghf2kdetrAvHO5688OOaQc2RWKpg2Em_KgcqeYlg2v0emkdPFkkkYpmJeAGM6O3BK3T2Y2rQtPdyxzWVUlsQY_r_24wZ9Ve_XWSw0FpqkfSmNHUeg64hRAJ2nT14oOGxXijwAOytIaaZWfSsjrchU5XBJe30XmnYyPHWO3FnQGvcSYA_ZRH8uoT2XYiRjqNev1v_ilC2gqYkR62RakbXJ90ycQ_vQ3unqmphJyU1nDycJdMTe5wNPUynVP7l-HEIkxqTWINJR1V18XT2BW--Ew9ZVds3QKgDBmzv8ICIAncVCF8zcXpHChBiGG5KE2mIQFJtQPLJmKrVjHdSgqC-y0_p4p9Zwow-SqMtkf1MA-1IUIHda_yAcbLd9YZnCT9vzX5cAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28292" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwN73Af-PX_CaYak21JSvf3fs6BoFNZkesGZdGrzwkrs1PPDnvHd6CMih8CRGg7ilU7AJqe7eg8Jl_ZYvHRPDkOahdEK-zPIBgb7JL4BuQOhW9TemWVE_N05V8D34scNxO5IZzXNS-OLT8eHZRIls2_LfTWv84u5NxHmNViwMQhcVhbZeDtOvc6YqqnDZ-rcbozrF_ptWJq2D-5NDxkZL50SBBwNO6s5esyADrvxepS1TAViz4uBg9NzPg6q4OGiC3LgOS-ihrh-2YmNJKq-6NJHstUaSCNwyeyoJ-5iCFS_X53DQ-8AXnPeasTh8lCzd-A9dvoi0LLJH9Z9iYuu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28291" target="_blank">📅 09:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=cCf32W1OpRPg6ffGnupM2JPWnCsE6-wVUOrasfeNdkbb9-v8HcAXtoym0fCokHKmwRgj3BGy1h1hCb6dsu1HugkCrgClQzEcR_qxEBghLKP7OSLUpFV83De5l1Ria8FUV15te5OwxdZdSzpzYkY0FT76Q2-gkLLTCRlZ0WnFz_TljqXXupNoiymeOgv9AU35NW2AaGH2yJ5ZJiW-jDGbnuEtYpVePR1uxy8HEZwdpGxzVj55NNEs_2ec2637AmCKsDpf1nSV-V-H5_xkKhC4IOYS_m_SCe1e2W3uj_D2etZBjdu_AMpIRk8Ngjvo3nU4a6_htFcYXPfKmHHU-D-SNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=cCf32W1OpRPg6ffGnupM2JPWnCsE6-wVUOrasfeNdkbb9-v8HcAXtoym0fCokHKmwRgj3BGy1h1hCb6dsu1HugkCrgClQzEcR_qxEBghLKP7OSLUpFV83De5l1Ria8FUV15te5OwxdZdSzpzYkY0FT76Q2-gkLLTCRlZ0WnFz_TljqXXupNoiymeOgv9AU35NW2AaGH2yJ5ZJiW-jDGbnuEtYpVePR1uxy8HEZwdpGxzVj55NNEs_2ec2637AmCKsDpf1nSV-V-H5_xkKhC4IOYS_m_SCe1e2W3uj_D2etZBjdu_AMpIRk8Ngjvo3nU4a6_htFcYXPfKmHHU-D-SNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوم بالارد ستاره بریستول‌سیتی رور گذشته این سوپرگل پشم‌ریزون رو در دقیقه 85 به بیرمنگام زد. گلی که اولین گل رسمی او برای بریستول و نخستین گلش‌درچمپیونشیپ‌بود و خیلی زود به‌عنوان یکی از مدعیان گل فصل و حتی جایزه پوشکاش مطرح شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28290" target="_blank">📅 09:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📊
🇵🇹
🤩
تفکیک‌گل‌‌های‌زده کریس رونالدو و لیونل مسی درکل دوران‌حرفه‌ایش براساس باشگاه‌هاشون.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28289" target="_blank">📅 09:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d382486c.mp4?token=qfEOVJ5TvV5EtWoSm9WdLhf0RnDed3avdsU-OMzXfy5FKCgal3NI2n9N1lWFNAG6q_lBEAF8yaHWKPwjIyDwBbbU0BM3XjMpLLpJAX63saw-_GNNli2pnjphsmSAEBnuDwROvHsTDRnyCVzkrCX2gf4TnUpaKIDGtdP98COcZLydyp0hBOTJbH8KL92hhAMVwHJENig96pO8y71HULGP8EwPnHaPJTkheRYjwZYY-D8TWfnsH_IYrrD4KWjNQ3YiTk6Z4PjAQ5k2G3_VS8Sr5oq0EoSsNwUcFko7LRizTx1swJe-JpI2k8uuGRM7tsnYQQde9flgpvb0ODrll6EOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d382486c.mp4?token=qfEOVJ5TvV5EtWoSm9WdLhf0RnDed3avdsU-OMzXfy5FKCgal3NI2n9N1lWFNAG6q_lBEAF8yaHWKPwjIyDwBbbU0BM3XjMpLLpJAX63saw-_GNNli2pnjphsmSAEBnuDwROvHsTDRnyCVzkrCX2gf4TnUpaKIDGtdP98COcZLydyp0hBOTJbH8KL92hhAMVwHJENig96pO8y71HULGP8EwPnHaPJTkheRYjwZYY-D8TWfnsH_IYrrD4KWjNQ3YiTk6Z4PjAQ5k2G3_VS8Sr5oq0EoSsNwUcFko7LRizTx1swJe-JpI2k8uuGRM7tsnYQQde9flgpvb0ODrll6EOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28288" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKFTsR5BVL5DI1lSzIReX85nm9hzu_65r5Ig-otnN_tkh_pMn5eGCGCghorygyA247H0L2ltABTAVj2HykpV1W3mhK622GytX5MfwXC76CN4Yz1cO-I6EySP491trADsEJN_riWGocUpbnIMwhHmLTEpY2vAdl-IgmV-paQ4565NkTXtq3GmNYqpqXcgBWmagmUwoqKqtckuTtgNiFNYMXRsQ5thAE8hrNCabjsh-2a4ClMR6Xl04UkyDJCMGILWxLFxLlijRmF1KSiiv8CB2ICBYOev3iaHrtBoj7Pf0TJcI0ldlLnSIsGMPV6UGSNujgTfAQvAK0Yricf_C2Vfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ مدیربرنامه‌ های‌ یحیی گلمحمدی در روزهای اخیر نشست‌هایی با مدیران باشگاه سپاهان برای پیوستن احتمالی یحیی گلمحمدی به جمع طلایی‌پوشان زاینده رود درصورت شکست سپاهان در بازی فردا مقابل استقلال داشته. درصورتیکه توافقات‌نهایی‌بین‌نماینده…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28287" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUpRepZXiDcYRldnru_uuG67guSypCFVQR3avLURO42VnyEMuQa3JIYpeOV1NCwdKtpaaObABVHd047JbyBCKDEYiNFOVng1jcCz-TZhgOpuOWGjTSfzlLGE0lFWM7qxrluytQaw1rZKgDn4oZbM9UEOoYa11pOnFpmdjX5gCkyLBdxCgcGsSg25BGE-Aj-xA5lqaUQkBQ0PR2cdUvdWOHGtOBfbiSot0RRkXpeaxpYOv8tNH8LmPU-3c7jtVWQcyegHyusCywQlfndxbATspYOQsqmMF06W47Gu6_3moEHpAXNPHQ7X456cGVawJ6T7KdZcTHusH6wTkjZqa7qcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از تقابل استقلال و سپاهان درهفته‌سوم‌لیگ‌تارویارویی شاگردان فلیک برابر الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28285" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv3GiEDxpr4cI-THNjhkvNnTqj9C4o1dTfXYyaacwlzimPnR6R27MVAvS30kIQAST5PtfLOkT4BpWMHC90mX0jiIJ4EQOwWaaXg9Njsv3nJmIYICFpNJ4WTeyReQ7yfaOeZ1Rxtej29SQ5PzpHDlq-frPk5mDDAiKq4AGJTHtPYGouRLqW0lFUY3zI-pq6de1RJQPljF3wX7qo0myXsP27sSh0nJmNvGuHz5cjYkv885jBJsoMEAb_wH-sg8mx_VcwpQSLbWseXyo5zruLy8AX1yB9SEbezfw4kIHV6K6xufyhVcVZh1JgT8cR2a8WrjETxo-9xRjDwQHIpEIxpyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
بردارزشمند رئالی‌ها با گل اسپی تازه‌وارد و سومین‌باخت پیاپی دورتموند مقابل شاگردان کمپانی این بازی در مسابقه سوپرکاپ آلمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28284" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLsFrok-_zJCPmU4Hoe085waELudl_pwfNSWi---7zzZHUiUhOEKCBUEDOusf30Kpp3b5DeNbwCdDJAmiCaqPXneu-tq75pAr7IsAqxRT5m_qBB9Q2-4_Ui4EpMSxp_KSts26yojm83KcEtL2sAZ0NSuQ56PQ94oOKKXczHWPea_RBgGMHS6X9THnTnjvqELbAN9eQkJOH9VnG56T-M0pxqne3brfT7b3ez69CwF9IwQKGXFhqD3vExt0iHq9zMi906WJLL57zHF95cVTT6HEcaJhM13dwAJ_jl9roy2SBZFO2CBALfanSIcuLy1C_lK0cKPSupMBlZ49jb5cjdRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28282" target="_blank">📅 00:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMZ4j9trVBYgVLk8it8ESWWexaGgPeV1ZScqZFlvzLYQsJk0YGK1zVYIZu_IF8vXzIspFZUNHZufuKiZOhFSd3l-MPYWmxcUzYbaaucwpGFMaQhF3hWPAIlFWRn4GLVV3y97QkWEInwokef0l8EX3_XceWXuM2csYby76pRpRSy4txnEBO2L3bdCFloKtpNe5WILVMy9LnQfiT1Ej_jQYA1x2gr4-QI9EgRt7bW6Uep7BLeJNcx19v-VuT36l-DXFBqboahcjGet7g9Lmyec4uTQGCX8HyNJmAMv22YhRZwqosMCayklGQXVfJfTqRkqWsArrl9YgthLlxHAUyh3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگردیم به روزی که هواداران تیم ملی کلمبیا رو سرو صورت خونواده داروین نونیز مشروب ریختن و اذیتشون‌کردن داروین هم برای دفاع از خونوادش یه تنه زد به قلب هوادارای کلمبیا و باهاشون درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28281" target="_blank">📅 00:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1ZJQfyex-fgt6Pi2SfH73eBgW1Lc_AgclRagXY8wmMClxYahLH64wJTzET_R_o7NQTjozrPlFwH-dhWFOb9NZHmKGqejXiNInbDmcizj3qc_20C7fDQQOXtTaWRx4ug90YSiiqgE_151W-lMuuv0efnUxcUfjYa8MrMweQ-ZMLhMPcsBX9avUiRGir30KazRCmZf1pY2mO3LZJh45JBetKfIHPWK-A0bTKeew1gLW6Dam0oB1H9Wrl6S0sC3DHNlYEmKiX_Z17_Qrgm4ZDFNKyyW8nj8DJUiqAnBBd6E2ymij1Z9NGzeNr1UAUQf028l-caHwsaU3QiduW_3ByouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP7C3tNNHHxq7b3TFB3t2OaZ-PcgbLz-xZfPxtJmSw2EnV7QvF30uiHgAwpDFeM4grYxDfTPQUUxfsgTaEUBXAMyslF12Gz3C0K0Wl64VCyK_bvIwND5ae2zkLsXVVoadyvCnawQm8voNk0zbJun0QhVvsRbkZYdbJvY6OLlJzREY7mVwrYVQvao0HYzi6-8rpAdQoUt-ziqQqNBrAmJK2p2sUWTUhg5EPGhNCVv0khUkfhTR2R5DMlOHGeBj32SRxo3FnejqpL_5s7k8HWCz0Fg0x5UtkCyquX6JEK-f_EzknHTUJCXFAMTAbOwgvmDEQ9hiqPrgs8juC1lIB8OdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28279" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phh2WLCa5O2zOg4MMVl-ipXfk-9huohMxHrrNV6-FoHyaoTOcsoO4B_7xe9uihE8X6XXMX4CC3louPluDKFKyocbqAAPjBG5Cj4YIwxv0pM69m6h35-zf9jTemGR0v1Nzzc9vFX8niOleYP10Wza7VwOSdBSF9J38JAL9Igk_84emhquWtmoIq8lA13uGjP4v7emGG3Yg_erwQRiKiF4xmN7Y-xz4AXBU9koNd50xsY4ZxsE3Z7MbHNN8J0QEIxq1n9rPFxUHLVslBtkRHlZjLnLGT-uSL9WDVqRjiHkL6H532Q3FT4pJlA9XdQ7oTcLCjv1eG-WhmGqZQPZ1eJhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ احتمال‌دارد یحیی گلمحمدی بزودی‌ازهدایت دهوک عراق استعفا بدهد و به لیگ برتر باز گردد. بوی یحیی در اصفهان می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28278" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO-8KXtDaC3gkMLtU92aYPo40QdK_P_gOeMQea9mrMfQoR2dbRbyx4RzclciL5GqCoIrKh3WFh_8J4UI-kHZt3Qus1PWcdajKCO8GYmeKU0C17SVJ006UssnQLAI-7OT2Q8eiqKCMTRX1vs7cZtIwH77Pbztjnvz0OwmgtVdH4bh3grRFmals662zzRYZ7OVFWqUF1_BQikcnDUhdyYDIDX5LdL9tTPOlpu-pQ8KE7iYro5zLGmsXDTRVTJlz6_LXS0oiFwqxYTXUnJrWR7jP9A5-2X9UQoOFP_d4hqtlMuCFfXlQzbdRccYMRTCSCV2VmTREb3nHwPeSDnir50aUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپر کاپ آلمان؛
قهرمانی باواریایی‌ ها پیش از شروع‌فصل‌جدید بابرتری‌مقابل زنبورها در سوپرکاپ؛ کمپانی فصل شروع نشده اولین جام رو گرفت.
🔴
بایرن مونیخ
2️⃣
-
1️⃣
بورسیا دورتموند
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28277" target="_blank">📅 23:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdAZ02KuN7-mRiEhDWAUUDqgbdtCUkJTbJt5-gPpT2LMqrBqBTZeWNs_o3i6DdVZso3mKXfSxwLn_HNgPIwDEVqYAVA-TSqpePIqHNYTLS0qa3SXcDV7-p-7ruo5XLkr66-PdOZKlnbiY6qWBs1E4TKx6su7Scx7_AFxtyxCiAe6r6hwInKg9QMS9wYCJTtYUELCUu0Cs5vkM6PRRdwajHVD5b-mzVrseH4VLFCcP0LH1m9o6ZYQXOd0XriwMDcIA68uqwfYnCpvcbKL48f0kgp3o3CmlL93wyDbdbmR96FxQ3THYvy3NGXZS7qDVdfBHzX9XddVxiA116sipcCjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛ تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28276" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD1bhZhGtJPXx1auBLgR_ofE7u4G5i-RiMhNSOSfYEJbOPmTWWkzafvVZfEj7en6Lm82nYir322bDLP0skkL5Be1BjuprZTXPmiJenTBfbVu0NGy_091YoBBmwAbkjfscTFYF6A4uzCawPcTL79Lm0YxOAwLYPNIbaGJiCo_rsO4YNmEMi9iEDSmqJvmYZuP76DqYlddBRpuUvTcYg1aApYRbIAsgfOl3G39lHMYR1XgrCkQhM8-v0cQzmNv7aNopJ4FdET2jQXxUiyX5QKr_PRNE7BqCBqTMtYCCeGwVUKJ-lu9Qa1NAZBqp1xjl4PWEu8V-tFQB0tY9HiZD1lRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛
تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28275" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=U1GtVRDvXQOskKtP0JPP_IjZBF_zVC-DjnQII48XGA2aAbHLCVAh0q-wryL8Q5HvSM7PYeIvaKoIxWlSgjK80r6yI2YnD7aY0kcNbbP9nSdf3sRWekFPr72a_EZdoUC3e9YTyorCZ8B927gwPWjaEhFGB2JGaY1qYZuYdWrnN4ES2YGn-7bziOCDmBtQoMkuB9XaNudIv8w2dBg6Qvv9CD8ISu0ktUwSSeLIf66OP4biPv80yi0O0DRoq4PsUH90Ly-xhjxeGDJSAob1CZLizfUYkXC41un6kcUjR6IcnOIp6kM5Yr2_VQvr0OFkx1DCEjJnMmau2Jm7_Q7I1BH8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=U1GtVRDvXQOskKtP0JPP_IjZBF_zVC-DjnQII48XGA2aAbHLCVAh0q-wryL8Q5HvSM7PYeIvaKoIxWlSgjK80r6yI2YnD7aY0kcNbbP9nSdf3sRWekFPr72a_EZdoUC3e9YTyorCZ8B927gwPWjaEhFGB2JGaY1qYZuYdWrnN4ES2YGn-7bziOCDmBtQoMkuB9XaNudIv8w2dBg6Qvv9CD8ISu0ktUwSSeLIf66OP4biPv80yi0O0DRoq4PsUH90Ly-xhjxeGDJSAob1CZLizfUYkXC41un6kcUjR6IcnOIp6kM5Yr2_VQvr0OFkx1DCEjJnMmau2Jm7_Q7I1BH8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اون‌هوادارمنچستریونایتد که قول داده بود تا منچستر 5 تا بازی پشت‌هم نبره موهاشو کوتاه نمیکنه رو یادتون میاد؟خواستم‌بدونید امروز 683مین روزیه که موهاش رو اصلا کوتاه نکرده و این شکلی شده:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28274" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3pSGQ4RLKQzqemIBQkPq-DkYL1kA9_1eE9X3kTdjDnqZevZwqVAjjjwzp2GbMhQh1hzxROmHcdyojIwoh5-aQHHwilUH7COI70CtmutcIqlMHVguY0h9bGuCyEAJ0yiUCjM0z-vESe9ZO9U_r0KwEkJS33nfxkebvDub-oqd1hYngICSwEIojxYZeFscxX-DoBZu4tY8Kf6QoFxbkOyKH09YpibtrtVF_RXoYLdMC4PazZyOUdkamPWckCEYOMmnASK9BVru3zBuJy4mnQtJpBuq1EzIWO4IfAXBJDGOhnC4xohC1C4Bo6xPPl0qQj9JmZetQhvh1zcYeS6kMaP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
العازی‌خبرنگاراسپورت‌امارات: محمد قربانی دراین پنجره‌از تیم‌الوحده‌امارات جدا خواهد شد. این باشگاه‌بزودی‌ازپیونتک و اوندر دو خرید خارجی خود رونمایی خواهد کرد و سهمیه‌‌های خارجی این باشگاه تکمیل خواهد شد و محمد قربانی رفتنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28273" target="_blank">📅 22:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=vSr_QjZCeJEe7DSQsRKomydXConsSSkD4UtOwNxPrOgeR6omYhfzzBxp8xHEU4cOnMZjOWGvAof5y-C7Tw_31zEDCbGDA_BFuDyiVNDuUPCwygAjvhWl_-0a5rhAf0bbFlcNcQvK4u5fO9mXREtgWZZKQRPCtaO-2ngeY_OuZuDDn-U0YeteS_7sj0CDAjLwj4J2f987BuureGn6PYgzCbGlBnm94pLtr_1y6oIe-gbu-QnPn2pl2pi_YqztrzoZkYpSpZ9XwaE9CbxYK93qE6Vlg9cPDfFNhTAxcy7QAqAG_vtoHd0ZiZFCB3qiQviLyTTwPaycCv4eP3nCfsGsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=vSr_QjZCeJEe7DSQsRKomydXConsSSkD4UtOwNxPrOgeR6omYhfzzBxp8xHEU4cOnMZjOWGvAof5y-C7Tw_31zEDCbGDA_BFuDyiVNDuUPCwygAjvhWl_-0a5rhAf0bbFlcNcQvK4u5fO9mXREtgWZZKQRPCtaO-2ngeY_OuZuDDn-U0YeteS_7sj0CDAjLwj4J2f987BuureGn6PYgzCbGlBnm94pLtr_1y6oIe-gbu-QnPn2pl2pi_YqztrzoZkYpSpZ9XwaE9CbxYK93qE6Vlg9cPDfFNhTAxcy7QAqAG_vtoHd0ZiZFCB3qiQviLyTTwPaycCv4eP3nCfsGsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28272" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=a3NDoBmXLqjQQvtskQJ6kH4m9-BI4F-AYBEt6j8iUsNtE62Me7T8QNWocgTrhz02rv2pdw1dB1rfAAoMZOnSSdC1fTA_sUoW3bHVXBr9JhMdSp_fXSpjtwCYGmEkOvVCo9ktQNWj3QweoxHoJ8ztglHCvIHnHZNu1snxg9hs4slZ6MLKkL6Vwob7AO0xVBPEJg8-TNL-X1akoDBT34DnXKPyJYObxB1yVPnmdoPZJ4QpUTw-TBWahLejJodYCDXQ53v76_re3ltFnj0r7S8lloTjCdk-TFKXVVE4LNFkn42f_zfHY9ZbfdtrrW3LalnWLyRgPwuXaEO1WKBGzIZSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=a3NDoBmXLqjQQvtskQJ6kH4m9-BI4F-AYBEt6j8iUsNtE62Me7T8QNWocgTrhz02rv2pdw1dB1rfAAoMZOnSSdC1fTA_sUoW3bHVXBr9JhMdSp_fXSpjtwCYGmEkOvVCo9ktQNWj3QweoxHoJ8ztglHCvIHnHZNu1snxg9hs4slZ6MLKkL6Vwob7AO0xVBPEJg8-TNL-X1akoDBT34DnXKPyJYObxB1yVPnmdoPZJ4QpUTw-TBWahLejJodYCDXQ53v76_re3ltFnj0r7S8lloTjCdk-TFKXVVE4LNFkn42f_zfHY9ZbfdtrrW3LalnWLyRgPwuXaEO1WKBGzIZSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سوپرگل دیدنی امیرحسین جولانی در بازی این هفته فولاد مقابل شمس آذر به سبک تونی کروس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28271" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28270" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXvqwAGd5FEAmYM3p0tC1VHEcUFuvwUSDby2rY7ddUK6nV2GRIwmMWME7cuVAhP7uMuRQyv778VRJt6KARmSKk57HJCHd9KbglfGNLMF59s2M6F39ImasNHmgUfmWWqwNfAv461UoGdaUKG3_LWpSrlq-YFQeF6-ZtMYjV0tMmHWy1saOhCMN7N15k7fa0A6Zwbmz9NoCjLnicC8U2WuuugjBi3LNJi6mJcXdHxOcjg2hvKzFsqKrOHifUteWVN_Eo3PhLFSXFXOnt3vEWV-Cl0R-s88aQ25wSW4B3xEW_zO3ytXF-ouPtqAnfSPEf4YRyRwOGnChnHG7cjV1I0b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpKDGwSB_EkJpNQiEgj3drA7NgzvaDBcUfZ_jRGlhrT-xeAw_28AaBuYLm9NbDn49hTZN_sWb492gn5MwOXfvcsJl0UzOinj8aHSXTf5fGWUSu1wd82hgXtkiYsLMOyuPKI__ueYAESLITj5DlsAsnSl1P9zLJ5SYfJEDA8cLWzrQK6_Mz5PhzpGG0SQexje5dKXBl1cYB6fsOd3GI5SaU0-zaB3WvEN6XTrYpcefRWiv_u1nKtYcWYLcs0G6CMANvg5ecFTvzMHWUTdU0cXrtylm_MTNxQ5cHMA_w5KamTtPewbKbKXXVNfepTdLIP96_ezZ21Z1QebnhJwGbdBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛
مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28267" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
