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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEwL5_OZhQQbpGr4gsiCVIHgUtuJSbG-AFljFlerMuWfN3JbSb5rIeFNQHDpOZfPVQzdydI1AxthCLW1qeBjxx-2GbbZ61yM6yjTLyXNgw9gMOXb8lDGaZaBJiUVY9hz_8fAOgQ6bw73IJSnQY-Q6QgqurBUm2SiKFQL0D_giPyalEFoPk98OEmmUQxkn9t7uBYYXFOez9lOpBl4XVIVsDpPc4ZOv7xT8Ro4RHVgchkrjSWAyw_alECLXr0IIale7l3UVTpr4K6NSJgWGlM81x-90c_6uBkUA-ypGyHUwQo9vVxF77wRU6e8NUkkXbTe80fSA4NVjlA9S-uFRzGkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGOQ_LVlCT-tmReaDAfXPAwJTkey-3XxTc1esIs7kMVvRY_f5047n1SVttLjSV72SIGu8yIQIEPZLZJt1dOkHT4-rcaCEXEzsojT5j5uBd-szCGlveWomlBckz3ni7lJhKLaRTIzeJ1lGnRC1hZpQIwFZ_olJyN-fHVuwpRS8gvYw9KgXx7uwKVhH7OkouquC2YBC9i6W451GLJCAh-vqRYpMxIJFxXPjE27wxmHv9s5gENzc-FqAieKych6gPWjSgNzkClX2SI3QoZcIWe7yo4jDlx7sjcbo8dez6rMjK76kxauJSRE86ryRsqRWwOABffAmqNW9ah4kncN0KpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzm5m7dK8V6tganEY3x-l1AfAqIizPLtFZ1986aGdqixA1UR0Zhp0ZfpcoCPuQj7rv4iCo0HiYFI2tqY43h8hkDYVbf8G7IiMVYW5gMMkY5xs6U3aeshWjxqHKsHrYwXDns3VSTid1TqYAVmFfTfuShMSccCoasHcP5iKa6vICbci4n-JLpc1z2H4gpwl8OYH0F9wQ_nDDue_oGGgJKEELqGPAhRqM7GiiZZ01s4YoFT6_lUDnOkc7UM3Hskv0NhZa5ty3cDemrGuhtf8Vp5PD8JGg94voynRwWZF4xq-9vnvSQYaV9ZKx9hMyyhNc1dFAFgxhOLzJ0XTdT7Qbszkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfUBmioy9-K-Xi-ZqisNuFJg6c4BFfvzyn64lW6an0cHWgb0N7eLNmnvc0dXlb0OzLxqjcu1nHXGhqbm0SURT2Cvar7py0wtHxjepwVIdoxk4vgwMCykroBFJ_1ueAgXrnqSSPblqSJK4IE-P3zXUvQZEYmaZC9E3mMr2CyBiL8UbXhvmF7YYF8EqROnL1zyZn0SagN51b5DrfPEuY9to_P6egmQSwgphFpeKJAgduU1FXBTd7msNYuqD7LVB_v2Ht8j8-C5ku8QXrRp7g3tgMcNvX121T2HUBvAvBitbCnpZT_IKy_bfJ-JounnC6_D5Me4JcWECQZocZEJwQb82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXRK09w_PkQlexQ71qs0ketq8WpEH-3ozHeP-Dg1zDDQbvoIUc-OjIGv8nvz6N2SoeIzRkER8IZ3wtxf7gKg_x9M1DVFdy9CPRmYrj2jrYsy_ijIeyKgqIAvMy6MLwgwvzt5nuHQSd_HJeWbHDvii6RWMs9dDJWyeNdRiZi7mSQA2zxEzhbVmSqssMGY0iH4E1zlqgkPQ-VsSqfjK0_h1HrzARFVP4T7MeVWJG2DD97ghx7eQkiZRa6MOphhc5Wpt9o7jBBONldKfHUwL93EU_VVKiHl4-pxS0VLS1fkiAiIYlPbO6UbHV7gp-cGg5qP6ntOxFPoBkL4TqWKS7QtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfLMr3CqfhseGB_zFmjbV2LuQX7z5aMVNn8orJdB1YuzcMFN2D91hNswVDGeaELq99ErmJLX_Cs33YoWT6UfOspyZsJR0xf6BM1wer-xEtr0QfMw5xS5KdG-6gmjCA2rE_6I9mmoIuvry60WPml3lvNhzKSwj8wd6k94mPRGZtAG2vzBZGCZ39hhlk9VIy_dAkq0Yc4bAEpBjhfYTnrH1qua8lLwgeKcCMUAnyMcLManfyufNX5U-1Fvmp_63WMxnby2B6UvHRv1FUcV3LLZScXnMNL-hH0iFUe6kyCBwz_J55d9mFO2Tvi6PeTAHG3_UPH9u7GCWikfn2G4UqZLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE5YjafaXq90Y9zhDdQCo3slCnI8IFB0zrgnydVCqII9oYueFpLGIgGRluuMgcyKWZMgKzpqmjZgoYn1jNGKF7TrE9nzALsVpPKVKl5RAD_RAVFufEMlQEAm8cTle_vQeJTcJpEhpMCNn7zpvBuolHWb8zBV3XEXOb9UjFTQkwRIFgITFFP23Lwjb_4Em7_FiZpZs-8b5DG-nGU-MFihQy7I5P5XcaXccgEvEwgU9UDO6wgBTSQtKocgUZyf7wmmNm89LxTl08yrDFe3LkkYcDqu4_XkUsrVLD59QsnkWjMsbvV4eANwK1FI1kNuijBU7RFh5pK2xhE7OVS9c5Dzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCkujf-bjrWli-B0UZbngyRK7gSPULFpjvcG1TGwCJmaSUwFn0ycje59q3h5u0jA9hI6OEnn4rYxzsBBhqWCMwJmW0nnxuAqVAC9vC2H3bk9drdqV_byvlyY6QNh3jDsFdcwn1_ZtA-W2icT1MyPU_uQuh_UzwC2pNCSoncMx5r72fMWSpXbJEtmXD9DCroDQaqNUMCiEpjrzevoxD9amRA0SAg0fChZEKU7gG9yOkJnkhEvmx1adgmw0gyF6haQfXHT5Y4KkR76rYpbDhRnJZ4Un-Jp1XKINGGK8Q2tIWCE3nvnf1gU7qpYD-oZfp9qeRO2acDvp0qSjsQGShsLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPJU7NZX1brCgg8d6_-PZRmoaVNZgrZd4M_VW0V_VMyzPQLBwkaSKKBG_H2cgZoCoE8YuFjuRslrnBTKBWVHIz4W4Mi9xhWGe1wI-ZKJ_EXJh4SLQBfoNSxJxDEehzWJzDQuvVeVnSshzS3fh3f-2rEnaz5QsrNH5b9hIdjE5JcbKzQ21GDSk2x80W_hplV223AoYSLtoZXp641_YqZjZmYvAf9_ERbgytPFwfwBZT57S9PWOEKK77d_1b0g9-8g8IyIe-cZutKVyMAz1-oV1TPr85A0-GBxW3gkHBns9pB2ASPkD-QrPTMrjX3HDvHB1JFJr_mU85X9sheV4viFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv50TcRvy1Ccr016CSCW9LuwwVhCyzhR23zDXTeOvUb03v0OGnpAVrNnBU4zWiGeq9ZJF7sNlwGbvzN_LyXrpY_SnfxgRzBKqfXlt5QJrljR42QbVqjD_SudEuxCJdovShFqKumzTSgFF3JID_n0x-5hhTplhn945N7UE2LkwHh2EaM6IkLIwEXV4dpa3HoXZVl4yuTQkCzzIyQ74CbYPBLIEWmoQ-twgqK-SkdMJ5HkRcF4uHghl8IamKFvkV64QYqgY8A0unILdnww7p9QtYOM1btlEbeNKpZyQPU1YTNJbc-oKvwd_HMdQZQvRg9MNjxoJ-bRmegH08kG6TdkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-sXnHoTv8hDbc0UW4adhVnjn4W33hOGhO_UGZQJSxaWtBIONdEH8qyRFm9q835cr9g-ZkO-DaUCLFaHFfZ3QMMKG1JTxUUUFnTu4nDXvxJewVHy8fJcGBDOR2jdyJclw6TzYDOsP6dfIzdJKYCibttneMxyKNsWNG25boeTCMaPWsJpcwRFeC8IVKd0PGPuN5ncM4A9rFE6lwZ3n_8Ob-PoUPjXTzb0LtawNgm3yE3vT5gCKANHaVjSkp7uhpZ-lVu24JbmHsYSBAN98VAsqZyi7Z6J9mv-D2Vo6ZlEwl0SoQDtvwR5ehIhmnNUaYUz4OnEcbV7jH-uNQ-ttt5gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSrQhSEpK8UY1nkHnfV-HWxpKoUGc9HKN6AZi73mI9eoXE1BLkp50w2pUXb-iyz8UYA6v6qgK5GRH2_H-xTmPiMlgGZi0LSGx-sK357rym_rKTdFE1rgSwgBCLuNhWLtw-5UoQ_JhPFnHOmE6r56WFcGx06Uzdm0OTEe1uZ3M5JoVgiaLHqN0SyBnRSnTlY9rtnn9ICB-nakWd_UoJ-OI5FCiJE0xiPzmM0AO_evvy5AfxVxyIWx1oNDE2WyhUjpHiYkzsd8nZ-H0gErzoNAecdvBBZY98WmhpdM6mbUVwlfvtWqa5O6kzBaeNWcmbrAtlCLvv69eF7HzICIQXoV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZCQ_bwEq-zQwYIsPQFmXASxDLYfHo35IuzLupVo6lCxNvNLcgbR95g25K1D9JMNRIpBwFVoAcDuBPRruc97gIHDjlZM8PyfDiipI_HgpB2NkLlNewXm5juqrJD0pRqqz-_KoGD5C55mem9CLI7GDrVHuj5UTguP8lT0aNM27_4AS_qVAn87kLmONj3nca17MtaClgEcW7u4Ult3VX8VVV8oFUGMUdU2DGho0OXcJKYBk49MxQd74bZEr38KVOGjd66_4guYug5z66op6N4m9321HB49GBZ715U3R2-s3xTY0WaXbDlQCSENtq31hgu6y9eMPb7Swe-rw4FNbb06zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWBlbI-JBSZ9UCkn2ruA2MD3VUd4TCYxsZBL9E4CuQzCXASdYIrD87x6NaVNDx7FAuucoRO4KJ2lOdWbP01NsdktDMIviNXE16_RNITLx4BuEXybtI76V-888MDdtdMmdacCh5gcLfZXeSfBJh68-ZJFAhLeI9yrvn9kBycRSn_FYb7zWuJXItxUIZ6Lag0U6qNO58xwcRF_QeE8CR96VP8MtfFnsv0HWUKv_Zq8iEF6FzGL4bVVwLpQsukHn49l9nJA19pTlre61ht81u6Zj5hdmQNmx1I0gD1O81nIhn79xboR4LdxWPWpV9Gy39zH4S8FHJfcoWzpHaXEj-NIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX5bzoFWEcsK8a0x0Tk-HWRqFq8PCsDlU5u56OSG159iXGfoSH806QBeRPcLZz3SOLlR0w6Rfcma7L3DM-47Llw2trLbozhEKfiiS9NxFHVSuJD83rPspDe75ZDXX8tkyLFT2sH2d1tLcVrACO8oyqlVtS3kgfa7S3E4eernVZDvRY9u54kEdr7TGax24qXAn_ZRkrUAUwngzn05Guh7rYgn5ka-_iu_x-NDnw_-r0D6tYjedwmuuW3TvRk8uDXQkW40J978yDuk22Opyk1DU5EFNVFePm9zHRHCkrHYU9-FoFf9iKTgPftZ3UQhTC8PyJPNsI3H9rhkIdzHl6MyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26883">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTgJzskv2f5n8K0grfXq7L2yQmiySgCOOhR-FwUFaBm-Om0BpRTgcWuHCkt3-km3Z7miJtR5NLSzNVlwSRo83x0m09YJIFz8IPxFgm5kEzv-9ywCFMWJl6_rCpZoTwAu3B5c0vKqfGzGnZrioOLLdotz4ktTvICPT50NdMgmZqF35FB8T7FllQ6S8AmZXVDLo2KZHW4-Cs26jPqgMV7FXi15-CaHWLJOZuyRjeiOJU7to6B9dgtcNZVqkNF2mkDCEGXYSkUG54fq0YUwWFx5Zy8K2zmV5_Z61QZnLC7GigKTvEOvhD_6-m8xRVEWx-uFDTl2KIyqpqqC-Dg0Vcwdhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26883" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQeRtRsDj71EEeD62mbev9IkfOdyloCVPm--jhbxx5TJjiLKfS7sBEuR4PhTuzJds6cJUVKBBr3SZcT3SiahoiCt5FDVwBEkrTSoDLUpNAOFptpBummoXNSbL3iQ_jBkPMkSCxDdSBS6Bl8lv3BYk7AmW1AN3P99qqOYLMTkMZdLpxhvIRwWiMoCsJD_KzgR2vjjFwl1pTWTk1IA2Hm1gAh1QjF2XBhNfiDu7R6qQvQGBebS_JCHCg3PlTzCtqJH4Qv1319ydpZJp9Ym8BJSBICpx_xi87q6taEAOMh1NNNWEgTw7WcqgykHfKAnhGnxYcJzwqOcuieS88LkvNNbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIRJoy1cFpSpNinA7a2AY0FHClmV0AtV1sdCthqTerWsGH3yOXxw6HFGINdg-ULVYErOOXI8CAlRMlo898WQvaTcgOHCDCJST1d_ncKEGrJNDMmKJxTZRtnzAR38_nFLrJY650lCpxVsKBhS0Z2UbzuHIMYWipTSPZGzvyd97LVNAXbBnj1JHk8n-jbppln0fVCC1wt5gkU3tpp8Wtc9lJiFBtDi5CYqiwU9OZj3Frmpf7heRvAwn3cKVDUHQltL8Dk4CKvVfBPYMKuWbuK8VCxecpj7dqW5lh2kWC_tAugt5pKJQx4V-au5B1vZbCIVWu42RE5Kk7qldNup8mnBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So1ZMWtnlnYyr18cj-wV--FIRNqy_qXuu0c3uodDdDJB8hlweHD0TD7O0b-SOb0Dv0dpf0wlkHgKUC8aICztYb56Blpw7oN93VP5LtkBE97URCW0EaMCPnyh8ScMz7FFD2gQI6I_2e_HOnWe1lT18vtjcyyIFY-aMNFeH7r3-HkVBXuI4cUe3MhGFXzFs3AeVq5sg_bJSkCltHZKNIn3eJq_zYlB5Dqb_lkaT-ILCJEQUL-82sdSFZglid7eEXWPPaIMskpEkbeJ9VxJJ0o7GwsyS5za2Lnb8x7bAiTEUmK2pBcAcJh7dIvjFrCdceWksXfQb97_POuUZnQoOL9Nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=T3jKzdOgoZtjDMoJbTRxJZ86i0wnD7rQnacNPOZVCHYggNx8-JpvLzYIKGNlEf1F_6po47L4_tP9mgM2mqtOSyY5Lg0_3_OiizMM8DvSOj11SqdF1FRGQ9_wTJ6w2JHXvGOg70aUOhfq__WJfRi2KFxJpde5uA6GsOp2kyKmE_GA4x4MtqSraao12GT-t9EbJPR7JhP9XKMPixGupQKv_6U46BHTCKEa9jB2Zn4uNt7j4P9LHN-JjkJotHYooj7OQBheyIbVF54Tt2jEf2pRP8fxRn-UqxQ6pZsXMG38fN74YlZDzB_HNu9LHyhS-LiSiBmXTPhxUnKdKpgyut8cdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=T3jKzdOgoZtjDMoJbTRxJZ86i0wnD7rQnacNPOZVCHYggNx8-JpvLzYIKGNlEf1F_6po47L4_tP9mgM2mqtOSyY5Lg0_3_OiizMM8DvSOj11SqdF1FRGQ9_wTJ6w2JHXvGOg70aUOhfq__WJfRi2KFxJpde5uA6GsOp2kyKmE_GA4x4MtqSraao12GT-t9EbJPR7JhP9XKMPixGupQKv_6U46BHTCKEa9jB2Zn4uNt7j4P9LHN-JjkJotHYooj7OQBheyIbVF54Tt2jEf2pRP8fxRn-UqxQ6pZsXMG38fN74YlZDzB_HNu9LHyhS-LiSiBmXTPhxUnKdKpgyut8cdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=kUvkNrz9qejq6h63SNvNCTj82mPVqB9rGlVUSz2wCQF5xpk18IcXsWb5nah9-ZzSKZb_0YDpeZvnEUsRsnUPkdjnPlwjl-waSIK1sXra8-eG8Dpdo1AiLjKoMkNYZ9GGQGwj-DsIzyzneCXNBd8ZhX26U2IZl3AFq7iWKFi6WyOmxSbHIi-D9jsZSmNtb3ZWBV-5ZuUUkoH6t2Yesliyfu_H4PTU75Z88ch0pj9NYebGsmPVHqDaE4C0s-SNSySJER4ZxaBc0MwH7lfOn0Ik32f3rrealqCVzxBjbjT04bcMcvubyPKDQGe86CYYwajv4o_sNfJXpRFFe_apkuVsSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=kUvkNrz9qejq6h63SNvNCTj82mPVqB9rGlVUSz2wCQF5xpk18IcXsWb5nah9-ZzSKZb_0YDpeZvnEUsRsnUPkdjnPlwjl-waSIK1sXra8-eG8Dpdo1AiLjKoMkNYZ9GGQGwj-DsIzyzneCXNBd8ZhX26U2IZl3AFq7iWKFi6WyOmxSbHIi-D9jsZSmNtb3ZWBV-5ZuUUkoH6t2Yesliyfu_H4PTU75Z88ch0pj9NYebGsmPVHqDaE4C0s-SNSySJER4ZxaBc0MwH7lfOn0Ik32f3rrealqCVzxBjbjT04bcMcvubyPKDQGe86CYYwajv4o_sNfJXpRFFe_apkuVsSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVSeavqFqj_bCVFpHOvBlP2dtgVYHWEz1gSrV7PJSW-_gzbf7en787FNL4MIASSPeCZyA-cetCcS6sMHWVIOBWyVIEXZofReSTikWho5EAzDazMf8YvYBeoKWZJ-sYkclgg2KJWpPfV9P2-rKlz896KcLM_Mgi930u5M4x32axZR698Gh9WW3DaGZui9ebfAxPgDC4MrULOlWvPv-5ZmfSX3qvlEGXaY_I_1WNQuFsvfjzBqFKlA1xPYFOut8X6xiAWXhHYMG2UICcnT_tCkz6WO5iDytF6q2dJ87yMdX3dkMzKdfmf9Rh2jkJl-3URTwLt7oOW0FhZm6vHLOVsacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCPkDSwRxnkbNeqC9x_GvBiOG0qlYiLr1Bh5WhNX52feHfUt6f3L-ofNwnKAvvQW9fDwivFlYpA3z9nLbtG_0pt9DoeIvVsD5c6PcMnU4CC7D6hEs9tdKfApZhRQaJkXzVmuhW4i78ZBRX-SNf7KuaQR01JOKNyEUjCHq-C3AHWSCWESDKu9owHC56f7wUV4Pm8mDdn-bSZ20LhLRArQBe05q7a18Bhdljk89YfEmsmuy07zXaXEeF7iDCJIvyr_7o6D5TTHTGPIXJhyrou6-xfAFeRLK5od2ENBPSFoioZz-mJnXSNmFotKFedifMSRMUn4mTXpwEiFUu29XPFuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=KUSPRFFKLvh4FnjPdobomE6ZkgAhRIj2YtGvQnk1Ay7fDLuBfUe7oiKt8qaoCFkC9bXIma63nEgYRYJLqAjio9uRN4Xj1a0sJ-ourVy0Q4Z8z_d6tYmBfbjAxkOFECFeZ_Ei8OJ8CinD4msfKDAC6wBJZxT0y8GlGWjxZ0sIe7cwAnqKXdLB6i_AHsSWR4IZLylZ7SfGxpaJebhEmUxJx8ZPc5Vj1KVcQkTsXQjHnAoepDbj3dlCSBYPhpuBs3rNxRQCrAZPtgvYw2KpUPRIwPeNgKxMN2eKYpevecsAmOwmsu2qNau50ZKp_54cHhe65YCazoY3D3i6GjOk_QrIIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=KUSPRFFKLvh4FnjPdobomE6ZkgAhRIj2YtGvQnk1Ay7fDLuBfUe7oiKt8qaoCFkC9bXIma63nEgYRYJLqAjio9uRN4Xj1a0sJ-ourVy0Q4Z8z_d6tYmBfbjAxkOFECFeZ_Ei8OJ8CinD4msfKDAC6wBJZxT0y8GlGWjxZ0sIe7cwAnqKXdLB6i_AHsSWR4IZLylZ7SfGxpaJebhEmUxJx8ZPc5Vj1KVcQkTsXQjHnAoepDbj3dlCSBYPhpuBs3rNxRQCrAZPtgvYw2KpUPRIwPeNgKxMN2eKYpevecsAmOwmsu2qNau50ZKp_54cHhe65YCazoY3D3i6GjOk_QrIIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUMuoIxAhpPxv17zDprNL3HGe80F-HKyc9sGQ_F9K4Z30wgWxos5Hl7qJ7FjZCgqNoGeEDnCON_XkHBpoJ7ZYlT_F61PB-4WDb_a--BjnUKxUR6nFFFJ80yRMGxvP-8i4LdWUjEyRkGym9uDGGXrvv5BlhSGoL-x8F0BC21OQ948xMH8ifqHsvb2Rtqn_dwSh9tpXTMmu5M8PQQ0-W9BK2o8HuXi-VflajGMyng7Q8jIx5129L9yeW_JKWmHgARRADS3cTpP6z8xJlKcFlOR1h33QVM_F4JZltuWrEy1BQuT-Lx0OTtKpXMTZMiM1h_yCQTlqg1O2bOH2DVEz9YpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR9qE6oV1nWJ0LD0dG-gWEdHfindgjbJcVyrSrfktZ2xliIt1F-WwD8E7oDaQ1wovLe0mqX992-qlVf9aVdMzV_20f9WSBk_5FXg7pePZCqYilNWUGP_65iktjbn3rEbvK8ePAg01DsRkWsyvgqWk1aGfU0F53LHGgVQCiwX3w_vblpRJwWRaYci1ipW1LFLC2fBiioLwmfA9m1JPuKSE5xlcC07Fg_R3JM3kNjynZKIUYj1iIXEfYom7nA6F11zY0BEZX9R7umGURT3U1U5iYoGIY51JrP0EtrYr8IOTOoLIKMoDbTmZeclOu3JC092v6lEFpZTX2XjhXIlG5HZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=rcdWtDrtT1LmJ6c2rgRGI7GLe0l0ftmrIeByzfdjgmkkkm6gaahVcklSvnsHOZtJsUZSGcsJdUFVAAFfZQHt7z-u7cTXg7CX6tTQQriXWz6kaYSBM97sfTZCy3UBvBjDJc5UQuu_Ph4dHehXGs0_mfjxknnisB9Gldst7YrHrmjUhKmxTm7i697AJ5hfM19A8WEim8WJQnPqKlMp8fQ4xRfspZ7JTAsqDi-A0SKqvZsB23i1Oh-iESTwGTT4FydogHhR4PEv8q9kspsjzxxbKHgy3CF_2N6IkYQOLNRMxTL20WjHtUFSX_qVG3AQybKcj1tNmODuq9vbbOajxHg4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=rcdWtDrtT1LmJ6c2rgRGI7GLe0l0ftmrIeByzfdjgmkkkm6gaahVcklSvnsHOZtJsUZSGcsJdUFVAAFfZQHt7z-u7cTXg7CX6tTQQriXWz6kaYSBM97sfTZCy3UBvBjDJc5UQuu_Ph4dHehXGs0_mfjxknnisB9Gldst7YrHrmjUhKmxTm7i697AJ5hfM19A8WEim8WJQnPqKlMp8fQ4xRfspZ7JTAsqDi-A0SKqvZsB23i1Oh-iESTwGTT4FydogHhR4PEv8q9kspsjzxxbKHgy3CF_2N6IkYQOLNRMxTL20WjHtUFSX_qVG3AQybKcj1tNmODuq9vbbOajxHg4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2uBmJC8DlZMaRpKLBaZKZYpgRl_OnkbJbWX4SCMQLG9YNvpfmWaO9iAnTZvKjjoQa8Cgy9Uv-sn39VJc_poZ6OEHYCjjx2FM4988OuPykvOVi-CKGcSy2nnUPYejLRoH2yt0ChsQi9FC_8fJU_q_T6Ix0aXY5w_eWdsa_1S2NsOOkeaIKuR8HfiqzKyDUtpf8zNfHLNuZkHdhkg6yRGkZxB_xld1FKE2BWlsjbaAc83CWVK1Nhuw9lB8bPI6OcY7M4ZgiMIrV5ojwKrvSWVjgjACgcESlQFdYLfTapy29LGk4WypxABEnlT31r7I34MWXRjSs_jjuZzEMTIULmA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=DgqmJU_ch6yc9FmM6nXNNyFTOlYYYwUqvW3ectv1WCHvXe8Nnh-cU3Rh1BA1MZJI7zJQe-Ol0nECWNYhsM7Tpr5VQ76uDDAZ2tYfaS5W48xL6CFIK85Q2PXmM04Fc0urhk83ZChk5csO9HPjZwfFaIGVwVDIiQL7_eTflQNtf3Z4G3QXF4MeXouBhfb1dqkUSSpp-FLNV24CJeqXFQu9c1cEiTHcxRdAzCwvy9sVK01BRxmM6c9SvQ6ib5YxvYThPGzacZahgjxfDG6440niruJzotf7CsSfslJnpuaVCTQjwX5Kn0dk6kUiuH0wlOpGhihbEWFpQ00OBYMJ5l-k3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=DgqmJU_ch6yc9FmM6nXNNyFTOlYYYwUqvW3ectv1WCHvXe8Nnh-cU3Rh1BA1MZJI7zJQe-Ol0nECWNYhsM7Tpr5VQ76uDDAZ2tYfaS5W48xL6CFIK85Q2PXmM04Fc0urhk83ZChk5csO9HPjZwfFaIGVwVDIiQL7_eTflQNtf3Z4G3QXF4MeXouBhfb1dqkUSSpp-FLNV24CJeqXFQu9c1cEiTHcxRdAzCwvy9sVK01BRxmM6c9SvQ6ib5YxvYThPGzacZahgjxfDG6440niruJzotf7CsSfslJnpuaVCTQjwX5Kn0dk6kUiuH0wlOpGhihbEWFpQ00OBYMJ5l-k3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYUU_9-I0qbnIT9omuJQnumCbZ27S0aY7O-ggy16wXMUhcoQRV7rqccCrYn9vfnGidw-HGt1n5gx2X-9Tb4Hzlttfr-OC41IerS3UYNzIs1nG-i9iLCo7OW562niPVrZSgoj78NoUEbqrMJh-A_ot_qeac33u9DSpLsA_d9koziUTdK3YopNUwCvVbeIG8bqGe9upUqidRlOV3FPIGXe0wFkG03jgGqmo6E4zwVja3Dw7EQvG8DzSm-RltPtTqtpKs5C75uA6WuYfv8_4aNClChPv_H_S3eldGKNRiKOAwzIjKsoymdmrIcgreSlk_W_SFW8ZL18RMtt1TsrdVrWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgBIcg7QfZzZg7ZjSY3zjIXopWHmLbBD_v7tvnSNZ0-pQUOblMFUWz3cBn8tw4xIyDMRRQCghuz4bprS89qd08lysxWyBWg65Rfo29155VXltb2W-7yl5gqbwBZAqwiQ7T0XaI7egmecN84tpCdK4YJppA48jTr76_NufE4afWoHbcrj5xQl2f59hbUp3Fw5wdp2Rygylf-TdWrWC-3zt0mPMAKDLpGPyN8OoNtrCwn03Sxv9eaN64y-a0gMSccpZKUeRP8aQ8S7tRqbkxkCM1HiwbZgU2lXQ2c_D2Pep0Cji6zSu6Q57wPVQQYT64JOJojrWcIUtgZ0OWaY2ZX9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQHIQxWgX_2f85rJmBCg17R5c4v7eWiIqkrNM0-3CYVWiADpjybksrHdYb2b6NQEW4h0gSts4BfNAm2rmqBr1PoShmATiB0ra9FCHaknuWR3jXjbC9EwyyhcovdOOf0RktrpFLz6Qjyuj93OPBZvYkkYweqA4h1bIKqJNG3DQhjW_Uvier69Wtbhk-HrKJxW5NcJ2Yj2irh-tpzDc2uwPrk1FO-BzxxPcAKnTSMR6ZZRpTtxUN7EvSwnzPZSLkT77-x1tktWZhEez2aEOTYI893SHeTc46JE9Fyom4k-NJpA6Ks2uYQzpEnuUEDxzOrfHKD2Fw5naZMEqgVmsOb3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zoq7RpXAFxzSNux5XU9PbULpNDIHe9ywKLHkXR5W3YXpTz2Kb-CPcNmvg8Wl_yz2VPTFu9PImHc6smmWzawrtOfYLBV38Mlg0fw_pH3WRp_70lOa2Q8-kwmVVJ7rftHZfHrPuX2p3HKJHkw4jnYr7e1Vd5xgFMtvgg5wYS-1JDxdAjd9XatHV-jtLDNCDVR-yismH2aMz6B63qOOjew5bSLNcMT5Tjv-L9dWj5bKePYPZhfbAJEziTiOuqAk0wBk2YJ-J2-QmsEmonU0ubWG4mgDXN_U436irR5gf-iRl1KTpNrY1j8FhlCxagJomZDn2eLk0JV-mmWiPysrZR1RDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIz03pUbl99wdN2i1QN55wUEnlLBY5QMZtAinrwUaYphHU2DAHWBfZIJCF1JLp2z3oBPlL0xS7MvTOvdYGDMToRqNLW7ns6et0EPHSGNNujAbpv0P4bhKnsi5_wvHiS-UpVifUfN-mP7jjTHf0of1dxITxQ6ut6458oMNBZDB1Spn2YObw0DmDwBZBOSpA09atTL0Y4AznvQiv2VCbDV9pOagbUspgKBH8mRzi6EJBubFZ2mXhJve39wYNLt3PReRI4Nee9t1et8iAmZK8VtxPKX1fG2DntpqrDOAxKuF_ua812fiNcWlki6iNMJuIeqsCUTyEmgwxX1ZkkFjk9Tug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3NFb-lG7q7nMzpQUyMG0j_n3kcykrFDtlvJa2jt5dpCrZcfDR8mKQXSnSgAKfL-8NHNJdcTfrmmxNk5aBrwTnSQ_J2swxXJ5qrpAiY-uDM8vIgt5v2CDwZzbQr40MFObeQ4V1uFGFkMUmdacOmVyB-smytFlIkHjFiR3cuN93288qTJxlViEC0alue_z1ZYfB6cHItBvomjnUfCdTMEC6dqtFFfIqImMaPvTuhSpfpP1bN2EiFoNd4ifTu0Esxmnsb-l1KXMwoKj01UhB_pqnF83cArcVtCkHj4CVlIzXdF7aNQWXOsTj8v4WB_Oekz6MPBBVWu35YZ0jheRT6cgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdoGU1FmXrC8JU6mMzDDHVDwlIS1Hh2u-rl60XsDkxyg8N6Lt6PncO8E19xNUSleHvIKWXylG7WVcrhyhXZudvjIYYeJZw6o7CiHUB9ea-1Ci-wd738EeUv52IBfsw3wBuflQaW1fVAiehIifdiNVMIpGU9v_AtDm6mpxSSwg1zHFzftvt3MtZegZ497sVJlVc4b2JIVVy4AHRpuCY3ltKOalHmPjW7FqcQ0CGDPwtQPHzYoVkAnN1yzJHl7R_mb2iQKwN8JEUUgMuarQAuHNxVMU9dMRNVNKVHqRCz2lG7sSsZ8-wJdROaTxKiTqomvTW1tBUcK3dNk5HubEgcjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=EjMugPNIch37U2-G2mGo1CPqgkNV8Ouk2t1X0k3lj3UAnNVJQ8suuk5S-WENt5-PsES_6XxXMBmJLqfKb4hQy3GmnEZ2D47gDW_gDxjdcAySOuQeEtEk1RMN-pXSDWsu8iPRdFlu8GOJH3_O6d05BIe2GSgR8DugiOdcdcs8YOnatPKke13B-QCRYv74Xh-i93Hr5b7ubFq2Ao_tRC7q-sZVqz-XYqP1e8hz6ozcErJ0Qgdeoatxodcn16ykrXBAqQhQLMibl45aqNzkqSaaWW2FabSjN9LyxHo7E2H8owkysdbBq3Wb57N_1fbcAn52_09szNduq-9FUk8FC-aZPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=EjMugPNIch37U2-G2mGo1CPqgkNV8Ouk2t1X0k3lj3UAnNVJQ8suuk5S-WENt5-PsES_6XxXMBmJLqfKb4hQy3GmnEZ2D47gDW_gDxjdcAySOuQeEtEk1RMN-pXSDWsu8iPRdFlu8GOJH3_O6d05BIe2GSgR8DugiOdcdcs8YOnatPKke13B-QCRYv74Xh-i93Hr5b7ubFq2Ao_tRC7q-sZVqz-XYqP1e8hz6ozcErJ0Qgdeoatxodcn16ykrXBAqQhQLMibl45aqNzkqSaaWW2FabSjN9LyxHo7E2H8owkysdbBq3Wb57N_1fbcAn52_09szNduq-9FUk8FC-aZPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8PPAZqFqQlqS-Cfdq_eir8V2xK44zQBX5lmSHUhY_Ub14LfjrtKf4rjjN3eKNaXqmz2uysjPbvSpDMkNtFZdS7AbmHXDlNFPaAzSGuz_FoTgqwhGg38whqWzXlwNgaoj4m4IFQLC4rOOMnoW9g0SUVGdOFDCusN9f-KtAjiXRWLpu_kVFizOwT98xZDWsiUGASqnkWcN1q304v9Sm1CFZCix3Sg355oHZVZnV0PGjaNThftlacLX6UwU5sOYoFjb_hfjXj78wpQmsFXkmkxO83jYFmnDis0f1EDwjFa3irI5Q99oCxp8uRas1g1-8BDAhVBQH_v7tgnvrCuJPmUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUzvD0wf2oLtq7HCpJNbGl4wGcabNKF1SaV55ROHA1JL21O9zZlNLekITtVNsszbnzdR9MUewKmOMGS41C3xuyX_W_f1npo60bKxZFDON11PKrEBaL16m507993Jmui4QTUuBu53sv3lDP52TwZprymKkt6rrKdEu0y0Xqw4bAodmM_Zy3oaDIR7K174OBsESeKF-ikxIHRF38JKN-cXhn67ZM0aV-ljmBplaZl02zzu4ceYMdXcOzof_NnVxeJblw-ildV7AgGphIhrjwroh3UT2M3y615M19rL-0JxAjCJGrZyiwZhx8Lxjd6SRfXfoHDpkU2rDG3kgi8S1IiKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpa69ZpKuJ0l7G5hMRGN3FMC6Vvzr-mKARJx6V0yA7e0hgCqRpNswClF6DXN0kb6SzTluJ9Eqs7eWnl8-8aBvyANRMvKGVuDphtuazMQpzbVqLNDYC3A_JoCPsOsDwGKnfuZWa4kxs6cgH9N8JDi2cKymFGLqV1JtaF6WQ2UBlmJ7Zm3RYDexSLfnx1UKqITyFVy-VM-Jm53ulQyhIGtF3THZPEteeUJvmw2sA5aOuBRvcWEKFzajKNmRL_Ur63x_LsWXUWMspr47_cdbrYuDa8udtTDwpnLMuq39Vdvk9hw-u9W-zrPBbeUh9XEVInhR2dA1z_YsmkYmpoTve9pXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqKdyvWfBT981_onn7Hj1fgbLufLGRYDGBd-wNLIuudYRfCKz0cnar2WtgSwiB5oyi-dhzv0FqYEKfIaUGvXeJ1q7i1jC9iFwgWhHjQUh0oZlYPsvcdD51aUqE8VYsNt7RkN8XnwPFMgO0tg3LClBlddo__p1wCe7o4a1_RqQNlcpzDq8K0zR2XCgMZI8RKKdYtEhHrQZRAywt9f5ocF69Yd3J8vOc2w1-R5378koikI0tcCpW641tE8Vz9ox8uMSgG_MTUyZla71JVKjc8ypx0ITtxYLjd7F-s12gsyvTIMUMpNRhutZbR64FWxDNOsu4SuZ44b87wEvD9lzJnK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEM69_XpBF39RpKLQyp4GcSbW-35chAP032gIhHMR0m5WyKEIn5e2ONmOmwPAki5JQaW6OqhTLXnwbycyJ3KwRScNgH_Ev0LZkyGv3ptBY1NBv9HdShCM-AiIo3X7QUJYmOfKZAq7zYTRcxfqUG5QjauXoSEBH07TjMQ21XJB3kxcQsLtQr48cRpAhJxK4B4vCLKgZxUKwEjtTko-aP457pjZr3hz-XR-8jiGgRKZx2HD0AuYHmomb4qQUbQGj8GxIaB6yGMd12_mr95zZRPH_GIbOJEXB7hXRqnTxB4U9A_-Opp5doV1GsyoV_8YQpYEBPaEeif7gUkWMSbFZhIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h56srVmL7MumIo-CA2nAXsnMgEb1Q8E_ia4yzNsX9wOIyHtoEFpZRRw9hoFW_aDms2669o8wLdEp0mArBaa1KFIKfrlGtrrVVPvY_82ROMqLkVn4qN_oVCvTcfVPFRyXrexLjw-L2f1D9CRMaxtfcZxr6sVAyEu0moxKntEm1sn9bdj8coswYHt2_ft5EG2wbclyjzTDkypl1NxBfL5EGY9rDCrN23QdHSLA_RoSalq49tJJyYGuhzA6aijJL6bXn8NJqTK-SuqhrqghT0YU1K4eNQAxYF5WqbjRFSQgAwCeop0Jk_l8x9K2WCX1ecvQ9nDjtBo1X4mxj4dnYAWu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlSimYmAt0fyjeIaCn5Dz_bw1M1GzH48owO1uo1FhUci3tWvju8DnNDOoWr_0RTOQ6TXHNS1-r3XKrmyHesvjXbjkJxMwS_UYGawCI_DSg1D8lMsj8E9MqwinhCR8pJrlOI8965YEu9P4p41KlyrKT3pXir4oU0optvk-isCbIrFDjxyHiyVZW42FtTJiKC6NOr2GGWO-2tD30adbJHOsv_zK4KX4bWqruu2YABFw0mRbFbo3MhbUw9V8OAOuEANy0bt-vIs0VYDB5cZgE5dG20393IO-TIiSKHRyUrPfVy05vYMQVlrO4tCJFr7AZ-auI-OR_cyZx9PHAJPLq9LVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGyrdWOIndwiy6dKEThyKxlG2GMXpDy9HXxR8FKmflaE_huXdbPJbS_rykD8ckNIcnKrlvKgdeXE49yyUkm4WmVK1hC8VWrGsuhAdWg_rHnefC7yYsgm5mWc08nUc5NiPqVC9d8qZSea1XIr42sUtkUVyqtauhAgs6tuT-tQbDfy1BiFeyW5k8lW86ifakR3EOF5DglQ1DBsV6sj9atF5AZqRFwdqfwHdF3Bo-bVLXL7ZbgZ5LMv1nd6VeD5xIKPa35e_3xtQvjsg8Q3AJNenzOFr8HVjmkZFz8hVmjK9d6bYTJo5xJ6C0_MYKJh8-f-YpJhy5I-4Z2tHn4X1U4TpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZgf5HMCaYvohqWRrhddYEe9gauM5BRSfXVG_JpkQkTbqxjudtJQ0C1CksLlYzocn5Tf5RXBN8aONy0CfGCa-_ORGudC6BXMgjXaSIi5uV_dhjxqNvnqkDM6-RX8z9lPiL6k028UbD4hGPIrl3tHREOROeEWew-klAY5XGs6S5pvGcW3TPWgpQDCRL7gx6bztEO2RfKlu3ytcsAdcoeAc_iAajJnhUX1f7HSTUBiPSCHgwKBuhxwYrW7yRAqtkLn31OGhnvzMb4K8Pz6BX7KEBDv-J0qYJK6DHIcdvlebCXTK57YgkS7Mny7jiPvnVpXK3ZCWxSLhMoQsrCDjgLYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF7scEcjOhbbKngkYJLQgPcRAr8kvuCEHGkTVC7tirfVlJp7Jra8rE7wmDsONRtOFW0jO7JEwj61kXNBO6fGsfqkQN6hZZg1MFvNdd2dWnO1TlnjFuxp-A2R8muDuU0GBFZPOWhI3Gp5Gcim4vpd6xLoOeBXBkXO-rDCK4BztB25ec1Btn6Ogii5owmB9V6RN60PEMbJ2lWGbMiN-vcnzMKzxyTXiePAt1sKOTDk9f1fzkgRNkMkQ4aG-xlWKQX7oEW4lbb_o061y3LuQ5CdF8ooJ5uNf4Us6hzidXKFnVqEdRLVMdOekuNsWcHNX6B0ECOVZ8h-NJm-9dITsAgB_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWWHjG3jskDe003mPwpjwSAdLxjyuymyIHmW_NbISJZK2Mb6Xt-5hquoMFVk8WYwy1zVIq2niQRQYB746pbHc9UfiytNTBTveH3lo75lyFaPl3tKwzHBnOzO2HCZZpVmNkL3KFQsl3aGYaMZwU7EdGv1pKFHcOXKvo4K9uUndgsN9AcPYByc4XHX9jwGwp4hEiaJxexrbd5yUxLsRlkk8klZxGIUCaJ6yAimVrsqPE5tZW_SElzjvqM5CnsKpLpBLVrZSsYzXWibneLRzXLXgGfnMYPkWJkldCFyycVLVXT1wFcZ4uQvFL8mRlHNKUTV_IGpcfv_9LF0UEXlzRa4KNNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWWHjG3jskDe003mPwpjwSAdLxjyuymyIHmW_NbISJZK2Mb6Xt-5hquoMFVk8WYwy1zVIq2niQRQYB746pbHc9UfiytNTBTveH3lo75lyFaPl3tKwzHBnOzO2HCZZpVmNkL3KFQsl3aGYaMZwU7EdGv1pKFHcOXKvo4K9uUndgsN9AcPYByc4XHX9jwGwp4hEiaJxexrbd5yUxLsRlkk8klZxGIUCaJ6yAimVrsqPE5tZW_SElzjvqM5CnsKpLpBLVrZSsYzXWibneLRzXLXgGfnMYPkWJkldCFyycVLVXT1wFcZ4uQvFL8mRlHNKUTV_IGpcfv_9LF0UEXlzRa4KNNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScYm_KVZygoHJZMr1XfZu6r609zmXTMTmIl0YVKFoOrqmx-YkMXKxVwr1kSTtBhsH8TGex_zbGhwU6HV4bkNr2g1oQZY0sHZZxhQDlkBepg98afFL8AUy4mav_NvsRkOIhtjSIREIVXh7_8lOY44u8uPRUe3R0IOVBaHn2-Bb4Mydzhb2NoBXGI4hBcd7dkwakoQbpBoZBcaxizeDgY0BHPUrxVGGPkupjWRF5topG0mXjjZMLLUy43FGEShuj4aMheoaWJ9D5x2fZiaa8PQDg2aLKAWVW9nwJInCW7dAzLB--G4Gq-0XfLKmiRHgRLvFzei4YmvGYaCC9XRrrMs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwwOASZvr99SnJ50N03zF8UhN1GRVd3fY5Stg2pWkRf4VBT3lV4IjlGQyjAKEBnu24iYUpCJuxTNBkfhiS128T9ka_fxVl3izIb7jllHGK23fV1_ea5NF81H0aUjKoSK-4CUK4pKuJiJUP8gjuii_pz1OHx9sYOMjPg7RQE3fUZq1G2PrJEX1co0skjKbyGkGH6RmLlcaKKTUNDvI4-dXLZNt-I3zdjBDQSpfmJXMwnO_mHE2cudtydvxxyxXBRebZ5RJ2qiYsUezXOguiOt_w9_uY7MzQ1SE6ypTZFYFIEgq_GsTEt4nHcSgoJJDzrlikTviXZb8yzk4voT4dEk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVmVV5rSeGaGBtdycZ9kDR1YqLMSGlQyoarz6lBR7Vd31BqsPRljX5zWnekhfAHvbtXYyMPeUv1Ta4ETZ3rP_23c0tnzxgVavO1ZDYRVvRqvc-Cdw2PETXfGqqwONqtf2UxmE9sx0Qui9ouncW_XGuQ31bzZqHVWnicTpOIvZwhonW0aTQiqkcsxpvXKOLZAUqsudgyV6m6W7CkrO-7l1SrB3oeKHsy3MyWLnEeXAkE9jn4mXicx4LAr7Kppkh2exDjBCl4JQKmaE9BG5GjX3eCJty7NNg_YqEbVnsSdHmdaEV6j2TiwOLN7ubNvf2wWV1HCG2U3Em5z4CnNRdAF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALLAl9jEqi-6y5zGuamep0Eej6gl16-I8WZRy7JTksGSoUHB5jj0dIyCjY2X60Cf8e1XYVRzo42hc3TWDhP1Dg33EK17fjsshGnwSg98FdnD8FAIuzoRWqBR3Y_RfF6liqq1caGxg2kaunV4ZbWUKSQbSNXdIO6l31uowErFWO7Q9bvGVg2vIkUfcCSc0xVYXZtNyLQu-iyLwNKDyqn8uTpPbHXO5AxO3SI1GxsA5zmNa1FcifkivgjiC_TB_gHHuuxAtdXb2giHzs5xBKNwhh7EyZiksR55crtqMJs6GrRQz0y0wUVW-GwFw_EL34GrAQOk2i7Z5xQmK7Y-NTJTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbkHp_6dYbqscafqOSf_Gq4omQc71nBjigfpECgoDEbrzIw4R-n3Sp43oX9-g3AgjhqqMzte2zhxPcYN2H_jMLpK12ruaKc3zdMFOfaE0yNYGwmcOpKPzWRmo9KTOeZ817ljVY1DkxkcrAW3pmmRcxyoJS4KTB-TWLy2-XSjNYbNbyF70zOLYOJyZj0YgKsybD86rmRGxN41cEuwHAtaeCBG29ct_TH87m7k2DCcKfH6bpT4sE57KlBUWVygPu5E4hdQEfHO3WvfVqcFgwQz06T4-BY7W5ngqEXYzUf6S2LI82EMHTezBTZUR5FylrlMJBYs8kFgYrBy7kwLfr-mbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYWcN0X-p2h8_Et28xgS1viIKWeBzQ25jVxpPC8LKWDXfnuTfHIjZmNJphRWqagcu2ymz0D12jzL7Wa5JfIZOve8KgX5aTybeZgMGtN7YI_yPK0Ado_MsH1IeJDGs8BGYDv5MmRIm_H0Uzb2jBPGo4p82y9D3BgaxXZyHZqCua8LZqRAoMuT4QutVp1m1tzmsp9smY97lJgpy4m-1uZa9ZfNbzvi2VVPQ946j1xLKC67k7YFcWKps-tmRaftG6DtZRcthAXujVe2rWgiaNxsrVcf4oGhhtJU7UUp_5fN0_eRQ0Q2xezPWuN6E7rTVVBHQ3ZegXroaknfpY7TMCY5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM3G14e3SYyJqN8tAxcOzCnQgR73KuBfxc0bkmGQ49ZKSMtrFEVrqUhsy-w9Hsx97PWRPnIQqTsor-heUJdBdOC0KsRdi-MvKiy-Uj0NNyLthkRHABoUDIRFpwTbFVGjD_3OEWuMrN1W81jNkExnaLcE7noEwXPxk5I6kmrcNF7cjbSP1qikYJTRGEa9vIO-ZRcQbn-pzO7GQI7lf5NTyS35Uj_gJtLEXQbk2wWOQT5J-GyouhSAd_UrBBCLvGhC8caODpbAUjakj1eO2SEZ79TJdSh3LEFK5y56DEZtJe82wwjma6vEhnwSaG8fWdFSDl9wAtQXlf_NVb1UIyK98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWRM8XBhISOXoICr7Luwu2gF0mUdqglE5_3BCXtRRVLv5yCZn9lV_ZOg1UUA9Radfz4zpBNK3T0uRjx0sUezKD-qonvK7kHoiRGn9BtFxKCh35thsC-e5qiEOdY0_gMPX_O3G-BDIZZ-vRka6ou77NhI1NIn_QcjKeNO8Ai3HQOEdTvjbTl8islwhqDjvoT2gh8kxsFJ2P44cBNbGrAzb5R3WVar3b7hiAJZdGbloSHUnzUsEz9rJ_a_lf7asbIPjev7oqyfgy73aHmeUUpx9wbuCKyyvh348K9fS0YPE-CMstauQBjdMRv36_1nsehJQRgL8Q2RXwgqJ-XfhQftDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsfLKmbfsQz8qgsu3VxRas5N-0nTqiRX14WHqWd-Qca5vJ9gGW1WlLoH5Us1ev1F41uc5KfNJQYaR8Dlc1izuLxjyHgNqCZXu0d2DWVyctUSQyXplKEuPUucT-bkCds_OSAcRKGkpLjN4HWFO0H7qkRKxQYOd-RRyyoomXDo6Or2ofEPxs2yZ6euho8zYMkceBBoYHalQ0z-mRgkqWrPG3K39wMQu9TzOjGZ9PQ8CishnvZXFEfyTfq6EPswnbz13uqF21tGKgF0nyUPjLwrluo7kJLPHK3GVZGZUxZ-jVglmfYucMiL7adq4zQZSQr3ttjXR6AiiwtA_Yc-yXcc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4bjwduMrnA9lVZCJwqgEQPiUxNDSFLB0WpWQcNnp58onRaoMZH4g9Vj1FWm1UhVQC_siY8nPX37ZjboOQXHvru3OKJ7dzbhV7tvA5NHOiqldrNF8CmJYzWP3Czs23xstVMzhI1bv6jsZ1JtlpHGudaLVb2KhWdsvLeiFhWkpMppdjs3oMHyD4AbXBNw8_YxR1gsfE07ykfM8csWv7ZyIgA-ZTqORGxg0L9SQiJu6uiPv71-2gXgk4Y8MtpUn6-5qGqETSdsbCa0Q6PiDZwjEso4JaSRSygdVfnbb4ucoSTCRMXeDqdvdb2LNbMayqngYCy2IE5LXVjVJQOgW5d0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbohtcPf3c3QfJivN5o2XiqSfYx3WOE-9571WK4PVu8e1lGNctFsZvIckBougwA45Td5nfOb9zBokajXsSA8J6Pddvj49YfCTxAg4g7j_QyE3vQH16KxZpmsmHrTOYfj8ouCEAMTpOMWpYn0G4tuTkzdyedF8Bu_11q4WcthsL9gxrlpovVvogXfy6emgNlJRn_kDNkGXpJtSmx3IuyH8h-JSUXCQIvdVqytvoPCczgRMtC5U3o48Bf1WwOD-XxDimGwjBHx_u3Ee_L3sOIgSVbqFJJuzUuj0r_U0qwl_XHVbzBH_yQ-nOWYfaDwiohO9231I_ntieJYar1m9JdZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=ceiH_o4g3HcxGNf7TgdaCIw8rbQZDyuaeXiq5BcFn84CNRKCEpUB-m4KduaPQ7EUeAOGhBrk215MzjHOINKJ9Yft8AjJYQ0YEHMjLeykiIl6kv8enHvCiY-Ud-NDEOm21eEO7gdRZ1DP5X9H-TJzf9J2YDj-X1N2TLGI8CD0kDDI4Au9E011TcUWH5KO4nMeGgwVG4sa9Xn_ZCrI_nouuQyu_Xy_PXMDiePiLblFCZQ57HbmuyOXHEJr34gtRVSvwOPEVoUdl4Gb2BR7H5x_lMa1We3b9tOjiDHAbDBD9JEKsmYzrlXy_xPEDGSiZQaIXwaQ09v_z-v6M98mQ1VA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=ceiH_o4g3HcxGNf7TgdaCIw8rbQZDyuaeXiq5BcFn84CNRKCEpUB-m4KduaPQ7EUeAOGhBrk215MzjHOINKJ9Yft8AjJYQ0YEHMjLeykiIl6kv8enHvCiY-Ud-NDEOm21eEO7gdRZ1DP5X9H-TJzf9J2YDj-X1N2TLGI8CD0kDDI4Au9E011TcUWH5KO4nMeGgwVG4sa9Xn_ZCrI_nouuQyu_Xy_PXMDiePiLblFCZQ57HbmuyOXHEJr34gtRVSvwOPEVoUdl4Gb2BR7H5x_lMa1We3b9tOjiDHAbDBD9JEKsmYzrlXy_xPEDGSiZQaIXwaQ09v_z-v6M98mQ1VA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvlpmeROhr-k4anRJoM-veXkIfxzXTfiUxwd3YREeigi8fZ0uxbElG_5kfCgp7VdAAu_bc9a49zbKOLNqvWvcfRjtScCiIUwu0wKnU-kRp7UWJVpwWwasNU32xzwaMH4cvE0mq5Qc2rR3ToxyKDXtULs2qod2omCPmLqp2XucySxOaCUsQXUakH0htgr84H429MaxnQ8gpbtoHIbDMCRUSjiAdaMzwFJPbrZ5WIHdwmzRDXFErn8zbe15UtgOxEWLXVBSkvYgSQoBqEk-Kq_2Efwjex6WsqhXyFVp9NMqV3w0-9FxW5jHo4WY5GgxV7-tAprSsAM-7NghY6sAAwKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqr_O1VsIULG_a6x3bjo7DBjkyV0iW1lVH5dhaqNDOmC952GoEFtwEQDc6Gt4gJBFhgjb2oJVEOFKdN-Vb_-bzJvxaGQDFRVRRNeyyYWRrMZ0shXH7KB4rtjJQ4tprroeGNMiNUxmWWnZ7RvJUSN1wF0jFqLAA_4R18Pg0zo5YQE726i0LV7hPDw7di2bTC3Zd7vfD3V8f7qM10mVQUmgrIaQclcCLjwwZgHVJ5BOd_FSU9QliXbsTGFU11tNgP3nsjF_KYZFz9HqlwAdY26ACsDh10ju-VZnEC8Td5X_Pek-0OveNrDrj2kLxgUGvJP-MebppGTgxGqtS5tpblGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfuWJY-tasiM2k3qMXfrBYAtf-B9_BU56z9hVY7fCb7Vmfnk9it7vvGvecrrSVlK_CsiBWmYiCo1i2J1ey04q8M4Pft6AtQtEvD44NB0cS40fb98k9qWBXtI2aAIrzISqFUn0h5OHfbMH7sHAkOe3gEu3nwoEsPs0rxBO8vxLasduRtiIcoks2VUZliSXkNyNdQiDtxMHum6q5fUpIXnvgh6WLnnDNR3-I8iDlVlSOjSf3XJNbmIP178ySRAJBk4C1lmP04nooLhcwmLPUr3Da6A7Y3Zwr0txZRp71auWkm5QNlLdQkZAKNUqn6OVu4fMeXg6FXDc7-YUF7FUXV18w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=K0R4xw7pBEFy-VY1vSDvK_GTQ9kZ6Ndrq6tvyi_2sftXvWVC7Z6wZWr6ydG5oCr7htGVQJRm7gzOKPn1qN_8jLYEqTBtVqABaDrtnclHg9rD5iwAkKA9w0Ru0wL827ZHWiVzyqvHXSXX_ShxRKFAgce9oc7anYLdQADNBqhkMp_Wbzb1eZjs9_tQ7ewqfiA6azmrkzLWTnwUUzkZpY-3N8DKn5jjKFgDMP9_M4EVcXlwZ2m7paN0PgUqYm-cbeNCDY5Lu5G9DDzhAnJSojXuXDx0euf00-q2lXvrRDOx0AGOOFcsjQE9sSWzm-geHqTv_B3vGn42OYsNt1pzvHROZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=K0R4xw7pBEFy-VY1vSDvK_GTQ9kZ6Ndrq6tvyi_2sftXvWVC7Z6wZWr6ydG5oCr7htGVQJRm7gzOKPn1qN_8jLYEqTBtVqABaDrtnclHg9rD5iwAkKA9w0Ru0wL827ZHWiVzyqvHXSXX_ShxRKFAgce9oc7anYLdQADNBqhkMp_Wbzb1eZjs9_tQ7ewqfiA6azmrkzLWTnwUUzkZpY-3N8DKn5jjKFgDMP9_M4EVcXlwZ2m7paN0PgUqYm-cbeNCDY5Lu5G9DDzhAnJSojXuXDx0euf00-q2lXvrRDOx0AGOOFcsjQE9sSWzm-geHqTv_B3vGn42OYsNt1pzvHROZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_wt6BDVjtBTbAfJfhbjUHT7VdwHXPRZuuBzxw-5dB8Tel1i_Sk4M-ppxjL09tc9MOYiztDUdImrTUhNOWGjejWcMGdDiDYn9pJ01LM7STIMdYEtCEfS9J2hKEQQjnsstU33QXUFTOHXIJyqYO8Kpxkx3si43K4Ot7ikkE5jr1Z1_ae2g2zYHko_IhaBH8514SrPEOeXfyF3UsvnHlkOhBoHOlq-crzmCKrKpijMhKNaW40oq5EnUQ1hLzlJ9174w3F7399pSTC1XZItTbf1oFOU0zMAemj0x4_VHiZ22CXa_kJ8KAeLnBpc8EMbaCzzf2vgLhaEzyWG3Eb8A28XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_lUviKB6eonVg1e2wpeDDbPhwpSFdS0RbT3DVWt96MlzO-Sc2ZVLPksPhEC69vjGEZI9j09WWK30uMsCEtU7qqEBQYbiYk-Q1gxGy9ABEKNsm85nFJq-NIbCMx4yrb881lFblPAm2LP3WKs-mvGNqFIqIdl3TOvEwToUkVS2N3CMJ06r3j1RswcOv5WOAenE_h1EYorpBNHz-cXxt6JKU_Z_-w-rbJBm97Ns8G_0w8NTyAnhCfFdqqFZVKw4bDClDruto7sQxzE87by-Kw0_vN9mE-zW1SckpSNdBUTgDlGL1dOao_Z-Nc67V8uU3mb27uQqZwMlZYHvgj0gkFblQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an_3yrp2abm0Q5cGeFBBaYi4T6GpcOEJSX3VWNwy97kqOM0O-croCb5ry1TStqh31G326SWg1sXJ8PbvuJhCfenLL93u8SOUxbH76XdNLjXrvBf9I_1qKJiEaOg1NexYBCSlq_tbJMi2_Wth4nfr0HC3yCR-Jl4qj5T6XgsNn8eSBGbzy4ZdBGYDAOJXCEgYsXXt3BHjF4RANxQCqLOnd_KtAk9CisiP1UcwlTlmhLj7zBnXqj8xpVTbv2v-X6E62EW1EWmSVTGLtniJ2eksT4YV9YELIvBkVfzXe1N-vdMp36ZMejdknPlF7C5UqY869tuzNoz7ec7IoGYaUjcSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=suHwD_VChCeRXnm9t5WJod70Vdmx3qd0p06ei2ZDtDOdvsm_9LNgfGWpZjHdc6pp21BAT8bLtb2FzqYUAwxSPUKeXnhlQcY5W4g0ZPNk4alRCjwdekG7SLYfKn1B9HNGX_U9zU1ilPiogb0oVOVT6b5MYIF60faoFZC9swQKT-4-TcPRCVSiFFRkiZDP3trUDSBhtdLcIlE1EYJhZBYzKRO7RwqvdrgGKQGsD94C_o5NNbG53WTfJQuXq2h7l04iEIjAvfxbXyJcosTVLB78xa2MnhKY4AYsZh1QFEwaIq843bM3lw3hKMn_PTzJyovh5mqlGZa0roklktvNz025rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=suHwD_VChCeRXnm9t5WJod70Vdmx3qd0p06ei2ZDtDOdvsm_9LNgfGWpZjHdc6pp21BAT8bLtb2FzqYUAwxSPUKeXnhlQcY5W4g0ZPNk4alRCjwdekG7SLYfKn1B9HNGX_U9zU1ilPiogb0oVOVT6b5MYIF60faoFZC9swQKT-4-TcPRCVSiFFRkiZDP3trUDSBhtdLcIlE1EYJhZBYzKRO7RwqvdrgGKQGsD94C_o5NNbG53WTfJQuXq2h7l04iEIjAvfxbXyJcosTVLB78xa2MnhKY4AYsZh1QFEwaIq843bM3lw3hKMn_PTzJyovh5mqlGZa0roklktvNz025rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJQsX3LtUxp4su-83lV8Ji0uy4Qj5rAeF0EKBW_UCfM8ES4Rf57hTpYjH08Dqtowg_heSN3FyV-Y15zxszZ5WJJFNq6geB9AnSq9qLKvnnpmuwir9Lp-_dWrrqWBURX7Pd-IBtWqNi-aRLhdjnBWR5SAarIrw9C5vcdOqy6SVx4NVfLBkQFHvc4JqukudLXnUG8NGFYVLfYzujqftB1KViWVoMAgVSVhzBZHVhT5npxOWKNW0kamixkbO90cTCDzyJXkNxloYYglfSdxF56DP18HBVVJFrnCd3Gn_S8dVlGdxdpnHQDGJuPgvQr7xW5VdMLJ1zm7smCf-LApl1bqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=La3XcRCRB7jbQIdH7ofZ_4GJzx3dK039QpH_dAk9qASbIdWDCqpv43CYkepJx7rmJjAVHZUiibtTsA7fUHk0V_xyfCRhb7SMPrmEKvK0jRyEO6CnZSIWXpBeRzrc6GN2hIF1J9hlz62kYQtu-BoIyLUfHyYls_eoo_iVjaf71Py-WsaRCjGfASP2VAHz1qxlCeupQAvnhcU-kSHgrBZeAQl6q34ifHNtbCqBMLqpWxpPsXw1w7dZK9T7uAwHtboLnBh0_s3J3YMHlJHOJa-QAM_ewYiJIU4xKBW6TMjSzM2goZWhFd9JpfN8iSXp5CmgQUSqq6qGADpvRQV9vfgcLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=La3XcRCRB7jbQIdH7ofZ_4GJzx3dK039QpH_dAk9qASbIdWDCqpv43CYkepJx7rmJjAVHZUiibtTsA7fUHk0V_xyfCRhb7SMPrmEKvK0jRyEO6CnZSIWXpBeRzrc6GN2hIF1J9hlz62kYQtu-BoIyLUfHyYls_eoo_iVjaf71Py-WsaRCjGfASP2VAHz1qxlCeupQAvnhcU-kSHgrBZeAQl6q34ifHNtbCqBMLqpWxpPsXw1w7dZK9T7uAwHtboLnBh0_s3J3YMHlJHOJa-QAM_ewYiJIU4xKBW6TMjSzM2goZWhFd9JpfN8iSXp5CmgQUSqq6qGADpvRQV9vfgcLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaxHS9BATazJ0DbSuw_6YPYfi2LjdoWkt8GWSiNk8QB8QQEt7xR6UHYd6DsBm4mQv88JXFlz16okYaY-IcDn49JF1RnBsYA-AKmpdBuChRDaNmEyrT6e5QMsnGGBJ8qMg567iSJQILmoG9H5bV92dfgdQKqBTaILLQFlGCj5PlMc-8b-IYVSB7nT6Dxp7MxnBgjDQ0b1XseCq02zZ_N-kfl0F8X3DFcugcFlWFprOGPfRtgxj2FUX_efsAwJhOjrW0aYDFtKbGKTRdaX1UFrzbs8k8BfxzitVX1B89bQQmJMSNk5r92fAc9z1c06_HV_PIBxetPI75hwJBNroWJl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT9qx-eacvF6aelUHShwp48evGcoHyLyiXKuR1xxXfeCYuF3xa8re1dM7fgY3n6S1HUCTf4ExFyDogPgnsW7j2sdI_Kyrs3cHKIl41VlOTqb_eCYx3AW-6CF0lv_XtAAFMMKLd_xCw4lExqp7r5Y-w8MKZ3n4UVpRuIhyYZIrXiW3QSS9zhFMTMxL_WVy-xXY0NnpBWa2nJa9EuGGGu98IK5w7QLjY8NiUx6AvZjunsooPrgjSzN_dOD3-WOYnt70gdzcG-kiIqimIGzqA43wgHkdVAgoWbjYAfCI9VZnm3LAKVvfhtyucOCcB7lCYC6GP9cEljHRj3-SoIJgp9pMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=ktatidRuytEcnLqOkpjuyQTctJjpbOfcA5_k-bSkXfutvEfizsjdjV0yjody8WzxBoBhDN6r6ZdFPsOivGZPhO5z94i4SUwFDJ9Onqk8yg_8wPiaxptLNFTu2GHaVl8L8_bzNIeVjnQVKt3F3KouRwKFZWqIJmqBvHgYdp3EiY9_4lTsgOVpJ_Yphyy8VGfBAWZ15Ej0Hij2nompsytDKj_jrpKcLZNp35DjPj8cLsqMPcOMLB2fG694A6sODyV6iUuVQ4wIS1OIjYQnozW5xZ1rJpQpiKwZFF4mLt9XWSsLj-MwG97J5_eo6mwB1tnRcKGKGK-BrvYURUXVJWb4M2KhjMIIEccKjMDAS6ujbTuPXld_ohDNa6HZO0IRRTxRhnIvd06tfUADAnnT27IO09qcOvUAutefJoc0GrbuBqWUXhnoXLTkNjTRUJSmdO7bfPHiZ_iYOliuDucWAcBQQiLFn_Yx8KOBLFfvoi2ka9GkAHh3frDm790rU54MX2ggdYLCxcO1eY9cW-U768YPhnMBh_v_yQPSINa0HVz5zdOnovLqUM492FGDT1W6P4cTsXh8FKMGGnpItodJgLv05peSsBh4QmrlAQfFhoG1UXicTDvEWl1nuSuHt677ejkKwfWiNCbURx6nT3IRAYxW0NhKFXeVKJAAAFBghYrEvD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=ktatidRuytEcnLqOkpjuyQTctJjpbOfcA5_k-bSkXfutvEfizsjdjV0yjody8WzxBoBhDN6r6ZdFPsOivGZPhO5z94i4SUwFDJ9Onqk8yg_8wPiaxptLNFTu2GHaVl8L8_bzNIeVjnQVKt3F3KouRwKFZWqIJmqBvHgYdp3EiY9_4lTsgOVpJ_Yphyy8VGfBAWZ15Ej0Hij2nompsytDKj_jrpKcLZNp35DjPj8cLsqMPcOMLB2fG694A6sODyV6iUuVQ4wIS1OIjYQnozW5xZ1rJpQpiKwZFF4mLt9XWSsLj-MwG97J5_eo6mwB1tnRcKGKGK-BrvYURUXVJWb4M2KhjMIIEccKjMDAS6ujbTuPXld_ohDNa6HZO0IRRTxRhnIvd06tfUADAnnT27IO09qcOvUAutefJoc0GrbuBqWUXhnoXLTkNjTRUJSmdO7bfPHiZ_iYOliuDucWAcBQQiLFn_Yx8KOBLFfvoi2ka9GkAHh3frDm790rU54MX2ggdYLCxcO1eY9cW-U768YPhnMBh_v_yQPSINa0HVz5zdOnovLqUM492FGDT1W6P4cTsXh8FKMGGnpItodJgLv05peSsBh4QmrlAQfFhoG1UXicTDvEWl1nuSuHt677ejkKwfWiNCbURx6nT3IRAYxW0NhKFXeVKJAAAFBghYrEvD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=K-CzBPkZoJcnh7uydxc5jG4xO4cF71VwxG1nkBKoat2FYCHFx_OIJtBSHG5zzn7R4YnyX7xN0BE6P4nURHxTQcmrRn-t911ZiZtWu4ppCJA5A65psfkLWQ7K9CYssT21RJ_1xz0U1xWflzih4WtaBl0zYqRVo1Dr3dHO6Hi-h6RnMOa2U-6eYWtL0R0CUDJxYkS34P0dZdykq07Anb0s92ko5rlvPTBTMfkq8hiFXh6igmgNKMohUPEPLtwZMp2iB1cZADguJ2HvX8VINPhMmfOk5U-YztyuF293mf_1qNOVNw9_1fbDWohahYD3hSZgXm-hhIm4Lmz-OLGk0X_xsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=K-CzBPkZoJcnh7uydxc5jG4xO4cF71VwxG1nkBKoat2FYCHFx_OIJtBSHG5zzn7R4YnyX7xN0BE6P4nURHxTQcmrRn-t911ZiZtWu4ppCJA5A65psfkLWQ7K9CYssT21RJ_1xz0U1xWflzih4WtaBl0zYqRVo1Dr3dHO6Hi-h6RnMOa2U-6eYWtL0R0CUDJxYkS34P0dZdykq07Anb0s92ko5rlvPTBTMfkq8hiFXh6igmgNKMohUPEPLtwZMp2iB1cZADguJ2HvX8VINPhMmfOk5U-YztyuF293mf_1qNOVNw9_1fbDWohahYD3hSZgXm-hhIm4Lmz-OLGk0X_xsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTIT9lYwAWWeoTyxzyMDLqjKedDqvRhPqFwErljeLn8YAXUidJysiYnvd1w10X7VqgvVpt2YYemnE_06Ibt6eituIW0zGE31SoBGNXI6RBiQnqgh7GyDjzE_ZWA6gupcVvjKq1gcRyr5FB3MEkMlIvkI-nh43BwX62s6iGwwY42zBb7hm7Cic-y6_UA76Ymm5MVeFUusI0F7UjJowEGCyXVcMzWNI-UgNJnHBYT5ZLISCtpRKfdcwAQH1NnvrHJvEFvyRNp_B8sHN0PdvF4yfkgx93DXjdPIh_X04g1ZflncveNd0OZGMPlL0w3sSvQMZn4iTOKQwgU3b4Og80ZWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgY-mxiAfHMQmexk5YdEpIqymfp-wUAmTQezCt5UKrQOO8RrcXCyZuHiEhfcHuWS_eqSrXu497jfwq8aNhnRTe-2IfHEtRmdyIt_TfKusnL9WKeThuI5to96vihSrwodezP-JOeXhzJCsvf82vQEP6MtozMxDHPZSx3O7UNeYUmaHfL6utyJEuMvZywG-yCnDn2-I2-xhdXEHZ5JUSMq2TqRHvvjpAcgnjpT-Tr2yGdQRpW_a-qkbW7m7IPpolXh3ddt970fvWATQcx-WN4mhRerLn67R4g0SV_XBbW-oy5okVU66xwSiipUwmGBDC1WGEIQdIQnlUFTw2HSbAQj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlC599079eA6EMgOHAs6nmZclAiNAOI8dG2okfN2Qqf6gIu90BKCtRuJfg-ct6qzXaJ7YVx0uOiHBgW_yuiNXkmv_MTIc35KBfsSUeVjS4HtgBNIJ0ezURtm3rHR5VntuePthhjZgfTysoY-dgBpViNL3LvT2hPV4KqY5lRBE5TpWMNJmuJslD0LzLiD7-CK95ubC4Mf0jLL8aMX0ZOpAo0q1Q4zUYSJ-B38BpUIHp4jW-1peDV1h919bBkbHcLLWvIwZa9JhEhgYh-mZ3giqVBIjLUwLGHgeRahde9W35izdQpSkjju7xkpK-8fdSMz_UtiEOQPxKHRJQVQSvjqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1_CcwhdV9NqFRcBgza5gQv6EfeQ88ETa7QY3rYyAHUj7jkgKotjIYHqCEscIOy9HlQlcIaz-6-35kPk1kodURZANcWJrBA02DXDsmVSmtRSLjM-f07vTC1tZQE17_TEI6Y1HqGvKqlQVOQ2-T9wJHi4Qzj79Me46TDKFX6jt3buyxe85phXHHlOu_aSwIdGt4HdIgqqkYOQ1THOkFD2NJEMoSTEZOPDrqStenN1N0Yvd60q0k-6NgxyWSc55IJGd-Kd-pt5NvlZ191gVaT9cbbwKRzy9sBap-QSzW7kNF5q4-HJ7yB7rsaW6jnWLzN9jLm6eyaAzo022C-c-VRWyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbqc2W5arxl1tvB72d-Ar1Ieksy_e9lBd7TT3LGwvanSDbxDKySESxGBDCf-fqx8-20QGy_iFD0aq24Egafv-lofTLXOc7z3NQrHnzGVLbkSdNSauICtw8fJc1BqdA4o-TckggqyYT0yDcZo3NYxZzEww9mZozf5RAs1ptAKVh_kUquIq-CdODBEYUnON-Hr541PpVO9Td478N8qMSPCwkm9GqIBKKxi8Qe5GAQvl0UAqbHGvKmkX4iDgA4ciYc2zpuUaboXW66W1VH4t5_WrV91R-VJvleS6oJ0KcvGfYt2L9qpIe4L1YNBBLdjOTNDZcTxYYv4TmW0r8YZmmp2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP_8hA-3vo13f3v-FOdjo_iq8gIpvlQGR6_a7aUgkdnZpN2xSDWx5qxz8Wvw4i-rne2rzRt0H0GpUBt1QbNqL8Fyz-hvPuTctck-pHnTMjBAkdNkffN_QSDOu1mvLZcK5hLyjPK0SyRJZO9AuRgTwHCHcp87k1VMbsbwEXKhHajHXe9pmSvrQJQ1iFrh4YZNia-wB87q0JO1UJIpznDIJTwPkpREYkkZ55k0FMQpl_1EpcDhyr9ji8IEQ-uS3ID5T9xmx2CQ0RaLGHaxpsajHlFCUC6x86MU9-u3VxCpzqOWhcPV0RB8xwfffw7lo-g0KZfSQ2XBSuJkt4DHl_9cNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwNSfG4N9bKxrTkbUTfuyE031EVCHs3iLSx21tr35EkZKON8rUnPsAI1Jj4nr1x4819NMb94zjNrnH44XFf5QiThWxoaN7cGze6GgkNET1TKIn_tUIp8t2-s9-7hvZTEZkBO3dHvVIfJfp3_SdSXrMAJvxeKRfbpKXyj7KJcmKEB2RWYrT0zTM0lmPOL6XFqbJXqcgSXwwCEoI0LMSm-L6bmdDWpZJmAHhx5c28WH1wKyZa7bRdh4ABH6Ik7sAKJVaZYQLJr8f33g6L7RH9mZi0ZgIOUHONRZEBv6xu5hGp6UQBU5WHL4QpTd4hzNSpEzEoZP1TWEC6lXRsWl_-SPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG1L1qy3qQman4uVP-HjEZXmORNeU4Rbq174uBDCcTPspQI6JSOGJ3gDvLFxaBqVWagEQF3JYmJB0V5BDedwC59OrGjyBY_RjNvbn3LReHGjK_l_2RVy1QbRTKMoNz7Z_CHfXRm-rXuMcyG8CxM7vzriWruA745LkTSWnwJdJ7BZxKD_S1FWHGm8KkPMRRZl9VNpm9m4vXBdm2L3Drab03cuWDG5rDcz3TH_qB0PGrr5HcyGaiIkoQJXTQqJp57aE8ZsjDmfsfNPtuNLQJWwr5kLfy8rUtmmkaioYqySJ_OgdHEH9Prz8wCZehcK4BOiuCpqnfvUzbX5Samv2ZAMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnB6wiDg31CDdJB9oOzUTBvuXBQhgOCVYJn4AQ5vh_pUOiJ2n95M9j0DR7FxYyOBWSP-ixRyA86gxrTcyNVKw3uCLDluDQe20gInesDzUCX4Ak_9Kyu4wnJDW8w7Qdq-MLeCYFqLZKy7hkvqWEZ0oGdc3vxl9Nu6aaNNOgPHFnjxehCvx4wdvE7y9_z7JR0MPoNusB03fu2JvpPuhglgs3405h9AOEq4V1uiRRheLwU9Q8uCbS98kg3gf_2_U8JIy5Z4iVSlEFfYFluwUNam6XQB2hd-ecmGYkMqCQ6T_s-hzV2qlT4IJ2U4K9az23uACBzYUxEqsG3MjQHkTXfdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmXnDZTWw_JZQpXFC-e6T0JtjxAshI0Fzhnu2nv1tlAiiLAZ6tdvu73DUz7V0BGuLqKd6PQozDC4acm0LdO1YNcozFsAOU85qYmhlQXH4Nm8rHiW_y0M-xMVGXGNS0By9TNBjL_62MproWNpISv5vEeqgV47SaPm20rUwUyUHXsQIGd-cDc8maokXhaLyyUFzh6Jjw9JsPOP4oTK-lGu-_P9eUv6ySFjw7F-wsaTLjgBb4m5gKuQeTf9BSvVVnvlITMDV0XhHbznK52qbNMcPGO0iKs0O-K8gvFedQI7Q2UeAlzIm8dRrdzT43maAEA8BEWPFxix3mSaIiKH7CI02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_rLfe_bA_FCSdxlOPYNRKghkNcDfM1D_4iqLeciE3VRt2R3Pi2kR6kybADG_Vp01MEssyltNsJS2M0NN62pslfMpoNfVT-o3QlrUAiu6Jo1OKA1oXJXpL0RX2RM_CfgqmUfK7a7F8vcDCDDRJkO1AZwEGrQwBuauOMCm5049NPQO1YGjKzSdWULAvuEwr-L1ch5ItUG9tZShIrobdf7gbmDoIpy4TtOY-Nnz7AJ2fYTBlaCf3MmSOFChF3edY1aGo9y2pExIe7jkSI3pnHPlzzPadSEBIPiFTJAswM4yRcXMt6xYgU5voHuFLthE3ZhJFqwU1y6ZAgyn83YsvAq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=bn3Jz9o1kKUJPG60aX3YfMmHEd2UHRpf3b6lZyvqPUzpJy4rokGRlLo2zHFOCtBuKDKFSjtPVrFQF8ARQDnOTOg15YFjkyd6iTxxY4l5LIIf9ug-LPTv5oRByLono8cp4YK352EEjT0OT_nlX8jNZDHM0WPWKgHt33MRVPsi29UxXgaQnDvpVfgNPcKrrkFnm7zZCmPfCYWNJEsrcDMWV4wq859uWG7xXnKsPcpOw5mOX72eRFAnxmkrSP__Tn7t6_xTLwJJPmB_nZoDw-q8_0NUuDWJLWp6yDXVhKedMB48aBF87X8kGRAAU_7JT7jnUAcAdbb7b6Uc4u1t9Xz3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=bn3Jz9o1kKUJPG60aX3YfMmHEd2UHRpf3b6lZyvqPUzpJy4rokGRlLo2zHFOCtBuKDKFSjtPVrFQF8ARQDnOTOg15YFjkyd6iTxxY4l5LIIf9ug-LPTv5oRByLono8cp4YK352EEjT0OT_nlX8jNZDHM0WPWKgHt33MRVPsi29UxXgaQnDvpVfgNPcKrrkFnm7zZCmPfCYWNJEsrcDMWV4wq859uWG7xXnKsPcpOw5mOX72eRFAnxmkrSP__Tn7t6_xTLwJJPmB_nZoDw-q8_0NUuDWJLWp6yDXVhKedMB48aBF87X8kGRAAU_7JT7jnUAcAdbb7b6Uc4u1t9Xz3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSw4nr7YpvHuDaSwQKFLkzpuRWp5rtOiYq9R79nxCo9UVUgCR3T8ogKvjtakHNAgC_mNCIBYuUjxmHy4WEEiIyJjOczUnq_Jr5IDsJCZyCfcI78PVDAOtz-PPBTAbwSnW1aSERidCogJg05pb2ZS3rMFSNqXN_s1H5rJzFO7PydpyuW4ozrgTrb_aDgJiuG6ScoXoE-f3QNx2foritL9iDnKtDFvm4EdXr8r5JwbXdA3TAiGWXS3bSW8wPJuoRt8sLlROXzv8st_gdtN4u8l7fp-yE1zaA8tgqKmE_Wka9br69JxF4tdfPaObzTv5-IDDjFjnrG0x8Tk4WcHeaCv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
