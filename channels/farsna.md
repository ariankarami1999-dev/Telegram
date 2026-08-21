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
<img src="https://cdn4.telesco.pe/file/m-LA2pxGF-tJhsVWVm5_LwrkgQsLYWftVLy5LYNM7nMwdAMrfP-eWuBa5VUID-F-cNR-wo7yOz1Q_yzcCy2wcp34GL859vS23__Q1gEVdSF8Wkc22GirpHyfuN0cp8Qufp1xrJSvhZkdE_4eANcNKI_FgaB-lCdtXDng8kMNeSH4NK7mxm8ATl8IOjqW3FmXOEKS-g9jl0dxb8iDUilAX-IdjcVVtAudMUSnHaLN0y5MAMwM0aXNGpZui6wOT1A_tLVVHDPzw1u0E7VhJGgOZRtK96Yq6sNZ9wu-G5Im7Df1-XqCx5KGl6fTc3sZ2m-fMnXowRGV4ynoZ98U9tNNgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 07:38:34</div>
<hr>

<div class="tg-post" id="msg-457311">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/farsna/457311" target="_blank">📅 06:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=cJNqeYLhSUdjyPvr1uWYU5UNu9EuHLO6Pws6w9DEVFe4zSg0tAy8eSy1Pyz6rnoCg6i0QlVX0RS--qfK6Qlzf1WYnYkp_4kK0bmj9T8oCfJbHcEH0MlRk6CXMHPuRFUISvPtAOGwQiNbJSXCeYgWElDTYJQjWirjQP3yVpp08Pw_OStpFmkc0bvPnfb215tlYRu2NmIPpmPp6v8QBmgA1Nykg8c8wt_y1Upzysv7vccdqWmOhIJ5a1IXIADDtqCCkjdOofu3uff2WmiJQNUIZXEsOBTYYECKPZQeokbcbSmhBeX2x5xpnF0JKFX89f07GAy5ig-OYn0M-0XAZnVGx7g8TmJ80oFJbdJcrly2UXskJKcc-uwNBbw4h2V8njhhv56PxBnnUNgO3K_dY2b6sArIg4TPKe-56W_MTJPQxLHNTE-JV6stEnmNoRRjDPgpcwHLLRnUopvYFE-GrwjXevEDZmg4EUYMcLTYBPppY1Mh5ThvazYG57cTMzUZUo2WWTO7TAOVB39PR-wLz39PC9SBWfxGUkfHFrDK3zly49XL7wcRPp62KwMWA5a8j7m8ebeeSeiYYF6kWOoSP8KoG3qLQi9kkPSkcrkHUWxVDBYUo-mRPIEyH2OxjuH3j_NtNCAbfBPEFFruH13NvOYjJRFC3N068fMHhLOalfudd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=cJNqeYLhSUdjyPvr1uWYU5UNu9EuHLO6Pws6w9DEVFe4zSg0tAy8eSy1Pyz6rnoCg6i0QlVX0RS--qfK6Qlzf1WYnYkp_4kK0bmj9T8oCfJbHcEH0MlRk6CXMHPuRFUISvPtAOGwQiNbJSXCeYgWElDTYJQjWirjQP3yVpp08Pw_OStpFmkc0bvPnfb215tlYRu2NmIPpmPp6v8QBmgA1Nykg8c8wt_y1Upzysv7vccdqWmOhIJ5a1IXIADDtqCCkjdOofu3uff2WmiJQNUIZXEsOBTYYECKPZQeokbcbSmhBeX2x5xpnF0JKFX89f07GAy5ig-OYn0M-0XAZnVGx7g8TmJ80oFJbdJcrly2UXskJKcc-uwNBbw4h2V8njhhv56PxBnnUNgO3K_dY2b6sArIg4TPKe-56W_MTJPQxLHNTE-JV6stEnmNoRRjDPgpcwHLLRnUopvYFE-GrwjXevEDZmg4EUYMcLTYBPppY1Mh5ThvazYG57cTMzUZUo2WWTO7TAOVB39PR-wLz39PC9SBWfxGUkfHFrDK3zly49XL7wcRPp62KwMWA5a8j7m8ebeeSeiYYF6kWOoSP8KoG3qLQi9kkPSkcrkHUWxVDBYUo-mRPIEyH2OxjuH3j_NtNCAbfBPEFFruH13NvOYjJRFC3N068fMHhLOalfudd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی منتشر نشده از دیدارهای صمیمانۀ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/457309" target="_blank">📅 06:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWsugOXzC9v3oqiR0BGQHvyZU80EhCAzFypFtms-rvAIItY65gBRu-_it3LNm9NC6QaFFwY29Y20sx-8_dDq0TKeTw8IxActuuYh1MGQJbTj2EcRqyWo81HXoBjGlK-JmLQticlsKeZHTybiiDZvfdR4f2XgVTrnmVjqiNbt7BX7AAMkvsyTh3P4kLL373EL2983OmI47F7ADdtxk9aasx9KP5k4sw1ystEXT8-fRVWnEORzCtCk-gRWmjPtIlQ7_XugnMS1NPgFTRydeOYbBZMjDCNCdkInNVnEKYH1mtJjZG84WdGz4_dLu1k526QtKZk612cn3zZ_G6hQr8yErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام روس: فشار حداکثری علیه ایران راه به جایی نمی‌برد
🔹
میخائیل اولیانوف، نمایندۀ دائم روسیه در سازمان‌های بین‌المللی مستقر در وین به ترامپ یادآوری کرد که فشارهای اقتصادی او علیه ایران همانند دور اول ریاست‌جمهوری‌اش راه به جایی نخواهد برد.
🔹
او نوشت، ایران برای دهه‌ها تحت تحریم‌های آمریکا باقی‌مانده است. تهران در دورۀ نخست ریاست‌جمهوری ترامپ توانایی خود را در ایستادگی در برابر فشار حداکثری نشان داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/457307" target="_blank">📅 04:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512caf8e7c.mp4?token=QhdQ2QM1JldCGaMrGrPC6r756INTf15BQ7uThVfUaxgUXFiDDzO8MpziCbEXpYwcC_TfgkyDcP103YbJ3zMTOKZ61jv2juhXO-igHc-Q_7QBKRyiLt_6nm_tjb9LZl8n5MBXfsUVMrfVZjQq-1nKJy7Z4jpwwFZ3CveytOFu-gyyWhhNWGeNnJjqmkpnCmbeFwCuLcuFTDTTcrGlJNyhogYamr-e1OleZYQv-2A_bfljNi0Y4r1LWYXAkS8LMpDXLBmBECgw0AezI4xFqwziSCOKI1mwaL_j5pKZIQrEIwWq6t8btCAvdsbm3XsoIN5MYGSm_YIfrkR25fKV1nSOsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512caf8e7c.mp4?token=QhdQ2QM1JldCGaMrGrPC6r756INTf15BQ7uThVfUaxgUXFiDDzO8MpziCbEXpYwcC_TfgkyDcP103YbJ3zMTOKZ61jv2juhXO-igHc-Q_7QBKRyiLt_6nm_tjb9LZl8n5MBXfsUVMrfVZjQq-1nKJy7Z4jpwwFZ3CveytOFu-gyyWhhNWGeNnJjqmkpnCmbeFwCuLcuFTDTTcrGlJNyhogYamr-e1OleZYQv-2A_bfljNi0Y4r1LWYXAkS8LMpDXLBmBECgw0AezI4xFqwziSCOKI1mwaL_j5pKZIQrEIwWq6t8btCAvdsbm3XsoIN5MYGSm_YIfrkR25fKV1nSOsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چقدر چاره‌ساز مومنان هستی؟
🎙
استاد عالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/457306" target="_blank">📅 04:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e851ace3fc.mp4?token=HuXeQOcQBOLCY_Moa5ghImGZw34OmM7FivpIIjuL6k4ERd5v80D2N4ndyQJ3KJ2U0f92lvFCPuJ0CUnZ0fC5AkLWCoRTtjSYuUlZqk0zFb8jbW25KQejkEh5VtIjELwNe3BEwRRzQTkIAodpnQ7C_4YqnBv9gSSBMzTexbn8HgE_ThOMEyp2QCmFoGeHcq7_u7rOBqgSK3km8pWbDa68815DYBLiUNWmbAbbhTuURlpdWXz4CHMh7ojTtuZ-kls8XchZ_iRQQ9OQ_60piXvmMvMuHRFHIBtOM7_zomcW3vdiM5M5sHErkVvmf_PsXXG1b3ktkibOKicISiRUpjdbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e851ace3fc.mp4?token=HuXeQOcQBOLCY_Moa5ghImGZw34OmM7FivpIIjuL6k4ERd5v80D2N4ndyQJ3KJ2U0f92lvFCPuJ0CUnZ0fC5AkLWCoRTtjSYuUlZqk0zFb8jbW25KQejkEh5VtIjELwNe3BEwRRzQTkIAodpnQ7C_4YqnBv9gSSBMzTexbn8HgE_ThOMEyp2QCmFoGeHcq7_u7rOBqgSK3km8pWbDa68815DYBLiUNWmbAbbhTuURlpdWXz4CHMh7ojTtuZ-kls8XchZ_iRQQ9OQ_60piXvmMvMuHRFHIBtOM7_zomcW3vdiM5M5sHErkVvmf_PsXXG1b3ktkibOKicISiRUpjdbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ورود جنگنده‌های رژیم صهیونیستی به حریم هوایی لبنان
🔹
رسانه‌های بین‌المللی گزارش داده‌اند جنگنده‌های اسرائیل بار دیگر وارد حریم هوایی جنوب لبنان شدند.   @Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/457304" target="_blank">📅 03:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366444aced.mp4?token=a5Y_fwfEh2j2F7gdjdaOhxPCr5fiCBheTyuSBCMdsYWSk-6XXG1LNesgKC1POY5FIyTz8sTEuzOPnHIfGL3jidY0vsJbtCh9Wv5x622YrFjjWXkD1K2TWBvDNLoYePOjbcjmA0fSe9MuljnZw7yCVNbvqqNcIQLbWerhm96XBgb1CQt-6TUfhywV7LM5ZhsKa9jEGHUQmN2TyDlHN_5D2ejME35zG47rF4o7qcWeARmuI_S_sfWvxZbwdp7DU9yF3jRutNPJtUnPVLypCmNCGAdFQZGwW2H_gxQnlKBRFj--REwactPdpLNkcQj2vgXNwICncyYsJ1viXfj5azEGUA6KNEm5HexXbUg0usjyYHxQEdnDREVOQj792MRCD_um7sLA6Zq5r7lV7SkqEgPJx2_2FqwBbMxXQ0aO0rUbs_MYpJPT7zSN63on44pEUvkHUaz8YKFC5ai8qvu6DMoZJsfbK1Nv8bhOlrBVHiO7EsdBQEphRZFIzvZ5WUftrspruo8K9ThoyeV3cUuYgjviUUjmOECgeS9m_wz5fFEGUZUkB93jCptZR31Oh6R2GeoOd-LAIwhIMnuniwoX6yPkOYQNYcZ3zaQgzk1dlC_eL7HbnH4bQZzcS4eodWsbnsQnC1sRChEYpUDBzzhgLzQK9fxKEIvBFtEOhZexLI1FPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366444aced.mp4?token=a5Y_fwfEh2j2F7gdjdaOhxPCr5fiCBheTyuSBCMdsYWSk-6XXG1LNesgKC1POY5FIyTz8sTEuzOPnHIfGL3jidY0vsJbtCh9Wv5x622YrFjjWXkD1K2TWBvDNLoYePOjbcjmA0fSe9MuljnZw7yCVNbvqqNcIQLbWerhm96XBgb1CQt-6TUfhywV7LM5ZhsKa9jEGHUQmN2TyDlHN_5D2ejME35zG47rF4o7qcWeARmuI_S_sfWvxZbwdp7DU9yF3jRutNPJtUnPVLypCmNCGAdFQZGwW2H_gxQnlKBRFj--REwactPdpLNkcQj2vgXNwICncyYsJ1viXfj5azEGUA6KNEm5HexXbUg0usjyYHxQEdnDREVOQj792MRCD_um7sLA6Zq5r7lV7SkqEgPJx2_2FqwBbMxXQ0aO0rUbs_MYpJPT7zSN63on44pEUvkHUaz8YKFC5ai8qvu6DMoZJsfbK1Nv8bhOlrBVHiO7EsdBQEphRZFIzvZ5WUftrspruo8K9ThoyeV3cUuYgjviUUjmOECgeS9m_wz5fFEGUZUkB93jCptZR31Oh6R2GeoOd-LAIwhIMnuniwoX6yPkOYQNYcZ3zaQgzk1dlC_eL7HbnH4bQZzcS4eodWsbnsQnC1sRChEYpUDBzzhgLzQK9fxKEIvBFtEOhZexLI1FPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غوغای همدانی‌ها در شب ۱۷۳ حضور در میدان، با حضور ابوذر روحی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/457303" target="_blank">📅 03:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457302">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3723379f5.mp4?token=vj9A5GR3r9UIwYtppBvcFoWINxny0HtNO6LvW7z1TEyJ1nFuWZm43DVqmQJIl0YBS4l1VyRwhg66slr9rxOfjnyICl76NCeK2AAEU58FHEbseXF1lewSI2utbq4KlQbLtvoj7OTFRHFCxkJEaJjUn02suu1qxYs_DlNp0xxGH9bYC5ucPfEPGQaiz57Cntjx6KxO1T8BBkWsOqP0eZ52nBqnLkDIfku_Rw-x6t-UBoRQm11NuDE82t_75aXtv_7OecqmOB61hb6ntULs9bDDb9770VlORQJpPUFyYoJgWeP40OXhqOWLvYRdEVZoLd9NQ729ZHNHPAuIf3kdDm5A6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3723379f5.mp4?token=vj9A5GR3r9UIwYtppBvcFoWINxny0HtNO6LvW7z1TEyJ1nFuWZm43DVqmQJIl0YBS4l1VyRwhg66slr9rxOfjnyICl76NCeK2AAEU58FHEbseXF1lewSI2utbq4KlQbLtvoj7OTFRHFCxkJEaJjUn02suu1qxYs_DlNp0xxGH9bYC5ucPfEPGQaiz57Cntjx6KxO1T8BBkWsOqP0eZ52nBqnLkDIfku_Rw-x6t-UBoRQm11NuDE82t_75aXtv_7OecqmOB61hb6ntULs9bDDb9770VlORQJpPUFyYoJgWeP40OXhqOWLvYRdEVZoLd9NQ729ZHNHPAuIf3kdDm5A6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ قالیباف از حرم امام حسین(ع) با شعار مرگ بر آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/457302" target="_blank">📅 02:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehn8Wehl2j8t64TnXvBjV6vgLUbU8auNjgADPt1jhXz5h4X7ms95pH7iprQA_JuihBf64D8WbCCJZwkph0GNYQg45m4sdQHtsN-0P_t5yny7YrZjedk2GzID3My7X-Wa57cvwi0kj9SoDpHmatwOJa2aK08MydsloXaJqTSlS_uAZyCszpOkGDZQ1mGSLZPnZw6TkzhA4DYol7fKQUAx2s-O2AOfu0uQidPVEWi6gcg6a2EHohq60mWL2YW9BWbqa2oscHp1iPzxNQKUWGwW5-gUtxn59T7C1rWmAZ6qugfb_wC6Cfv1VaeXs7d3FSlftqIbqb4v1ruj7UPTCvxLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هم‌اکنون؛ حال‌وهوای مزار رهبر شهید انقلاب در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/457301" target="_blank">📅 02:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cc33636.mp4?token=TnHALfZTPNcOmKgDgWC85TSyWQRAiMd5DzEyNa0doOM3zN1SFiOPCOikE9s0kVYUeIaaQ_cGcuHGynLlLpYnZPG2Yt3GcyHVft9xe0qaMoh6JTUVaaWkqWOwNcQdv93FQbnbXQEIpKCMVc_0MMcspWfv5kd1A633VofOMKVzVgpj9HetVoSLefQO_zL1ib9MK5T5u2N3cGW3abDOhVuMOuDkDuPzgafxWTHdXz_NU4A-H7P73QDZjiJoFljGQz0m5VLd_orW2V7xhzl3CIMpHspbi_31jmza1zfTEBDgjaVF5BfShe0428cvRpmTSj8YW_gvRydrgAr-U1KjXLeDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cc33636.mp4?token=TnHALfZTPNcOmKgDgWC85TSyWQRAiMd5DzEyNa0doOM3zN1SFiOPCOikE9s0kVYUeIaaQ_cGcuHGynLlLpYnZPG2Yt3GcyHVft9xe0qaMoh6JTUVaaWkqWOwNcQdv93FQbnbXQEIpKCMVc_0MMcspWfv5kd1A633VofOMKVzVgpj9HetVoSLefQO_zL1ib9MK5T5u2N3cGW3abDOhVuMOuDkDuPzgafxWTHdXz_NU4A-H7P73QDZjiJoFljGQz0m5VLd_orW2V7xhzl3CIMpHspbi_31jmza1zfTEBDgjaVF5BfShe0428cvRpmTSj8YW_gvRydrgAr-U1KjXLeDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع ترامپ از حمله به ایران در میانه افزایش خشم عمومی از جنگ ناکام
رئیس‌جمهور آمریکا:
🔹
چاره دیگری نداشتیم. اگر صد بار دیگر هم لازم بود این کار را انجام می‌دادم. آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند.»
🔹
ایران به کشورهایی مانند عربستان سعودی، قطر، امارات، کویت و بحرین که تا حدی بی‌طرف بودند حمله کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/457300" target="_blank">📅 02:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQEwGz_1TJu1khwCqZJR_YICCbMt-nrJQecf9Hwkg8D7g0vd7U_KzJycQ2z0JDmaaQAJKN-ceNHymmdsyuEZfiXdxen5PWY8uBCb3ON3Ap4DAFNyZcA0-P3aMve6pOtwM-YPnF5px5apYM-_okdVLcJooNazxjn7foNDVOkKIj3dTYE3CgpPX-mOeC71eLllXjYHYIG_bzyFic1RLcks-mXsBKt3T5If7eNv6Y7PvDQzZRZs84FHszrEoA7XLtoW4Q6wCxZwsvNARtOEGKSQOjDy6-jWUcJJoe3rZoSywlR9WYqNbfxXGJq1J1WU5-4s-0rehuOuP1nAHacjF4GCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نون بیار کباب ببر در نمایش خانگی برای عادی‌سازی لمس نامحرم
🔹
انتشار نوزدهمین قسمت از برنامه «در جام» به عنوان محصول اختصاصی پلتفرم نمایش خانگی نماوا که اجرای آن را مهیار حسن، بلاگر اینستاگرامی برعهده دارد، حاشیه تازه‌ای را به وجود آورده است.
🔹
مهمان قسمت جدید این برنامه، السا فیروزآذر (خواهرزاده تهمینه میلانی) بازیگر سینماست. در بخشی از این قسمت، فیروزآذر از مجری می‌خواهد که با او نون بیار کباب ببر بازی کند و مهیار حسن نیز در کمال حیرت این کار را انجام می‌دهد.
🔹
به نظر می‌رسد «در جام» تنها نام و هویت خود را از جام جهانی به عاریه گرفته است؛ چه اینکه از ابتدا تا امروز، به جای تمرکز بر فوتبال و حواشی آن، کوشیده است با دعوت از چهره‌های شناخته‌شده به‌ویژه بازیگران زن، حاشیه‌هایی از این دست بسازد.
🔹
بروز حاشیه‌های این‌چنینی در بستر نمایش خانگی، بار دیگر لزوم نظارت هرچه جدی‌تر ساترا بر محتوای عرضه‌شده از سوی پلتفرم‌ها را برجسته می‌سازد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/457299" target="_blank">📅 01:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1265e6e7a1.mp4?token=NpOnKXimYmLyQHTY4wo06tPKw-X6vzEFJw9nZJt43cWWsMwFj8Y10AgtyDZXSEvHQa12cC44E1NNxnBTxnT7718puBtEqKtCBGffAvxEGL4CZTPM3BIbqJ0MNBlMPEAtDYWIBHrW3hU3MCd-NWmbSBipwmBoQ-XHWl5SmzOOnedHjYKMLxy9eUDOtoI_l-RmO4sGXUYTwzlNip21Ha0Eb-j8-j7uYOdVToDtJs2NtiyyfRt_VUi5lxL50CiDBv-juZm-BAHjD9bGxlrhvay22wflQHY4G7d6n5Ip1ZLObDACqxD4Kqs0quCncqzw116RJdQFaB8NoaUWnuR3TH-SjlGELKnnQIv8PB7vSS59EpVMuXCda-KAvuWixRWxUpkiJZuQ7d3wiTS5q8JCWr5UqfDEfVGgaUmxHCrgljrwjCqAt-AV6kSzcX-ell-3v0ew5IyFoeHYd5sIlN8bxVyyArzpBwYpaJPogVjN8Zye8JtQwUUomQipiEla6tzfZqYDdn5JcvEnVH7kKOcVc_OO2lS3GvWjRVULcEQdmhqd92l9Qy_vYxzvIplsoUFB2niJHYaaLFSV-pjLpFwbIIrGKwGRZ6Ia4Pw9APdjA-XrLEsdjFg9riNKXcKrVm5lh0WU9TYwnJDswB7cVGn_9wjJ1E0bToZnX8WvroVPC4GHcFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1265e6e7a1.mp4?token=NpOnKXimYmLyQHTY4wo06tPKw-X6vzEFJw9nZJt43cWWsMwFj8Y10AgtyDZXSEvHQa12cC44E1NNxnBTxnT7718puBtEqKtCBGffAvxEGL4CZTPM3BIbqJ0MNBlMPEAtDYWIBHrW3hU3MCd-NWmbSBipwmBoQ-XHWl5SmzOOnedHjYKMLxy9eUDOtoI_l-RmO4sGXUYTwzlNip21Ha0Eb-j8-j7uYOdVToDtJs2NtiyyfRt_VUi5lxL50CiDBv-juZm-BAHjD9bGxlrhvay22wflQHY4G7d6n5Ip1ZLObDACqxD4Kqs0quCncqzw116RJdQFaB8NoaUWnuR3TH-SjlGELKnnQIv8PB7vSS59EpVMuXCda-KAvuWixRWxUpkiJZuQ7d3wiTS5q8JCWr5UqfDEfVGgaUmxHCrgljrwjCqAt-AV6kSzcX-ell-3v0ew5IyFoeHYd5sIlN8bxVyyArzpBwYpaJPogVjN8Zye8JtQwUUomQipiEla6tzfZqYDdn5JcvEnVH7kKOcVc_OO2lS3GvWjRVULcEQdmhqd92l9Qy_vYxzvIplsoUFB2niJHYaaLFSV-pjLpFwbIIrGKwGRZ6Ia4Pw9APdjA-XrLEsdjFg9riNKXcKrVm5lh0WU9TYwnJDswB7cVGn_9wjJ1E0bToZnX8WvroVPC4GHcFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی حاج قاسم برای حرم امامین عسکرین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/457298" target="_blank">📅 01:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkSQ5MlvqdYjPTW0hVsHa4f3-_ynHqZkjQ0RmWk_7TZBjZjvP87LosBB4-e40XHRea948drjPsxHJEaLv0aDhJqeen5ZlCeTZfJ68P1_3r5kO0-dz1MZ1MCKk4IfaeunQBMGFm1Be3GJ8OWQ8oLY10iwF2RNLeDCcls15t6YGfw8BA4sXS0Mfoo8tyVpUagL_QRrdzP9Wv63dJPsza9Uf6JFhnWxOjBQp1Y0QB6hLr0T7LAoVD-_w6bZA6XILNZ-devst-39Zvyvv637lbLnGEEe6_SfMHqikBLUm28s0WESUmxMyYZd39sthRG2vUzU9VDJ9ywfodZtN8jWvDyfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار بیرانوند برای حل مشکل سربازی
🔹
طبق گفته میثاقی در برنامه فوتبال برتر، علیرضا بیرانوند و امیرحسین حسین‌زاده، ۲ ملی‌پوش تراکتور از گزینه‌های تیم فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ ناگویا هستند.
🔹
حضور بیرانوند در ناگویا اما یک جنبه مهم دیگر هم دارد. مهدی علی‌نژاد، دبیرکل کمیته ملی المپیک اعلام کرده مدال‌آوران بازی‌های آسیایی در صورت مشمول بودن، فارغ از رنگ مدال، طبق قانون «سرباز قهرمان» از خدمت سربازی معاف می‌شوند.
🔹
به‌این‌ترتیب، در صورت قطعی‌شدن حضور بیرانوند در تیم امید، کسب مدال توسط شاگردان حسین عبدی می‌تواند برای دروازه‌بان تراکتور اتفاقی ویژه باشد. چراکه او در سال‌های اخیر بارها با بحث وضعیت نظام‌وظیفه‌اش مواجه بوده و حالا حضور و کسب مدال در ناگویا می‌تواند به نقطه پایان این پرونده برای بیرانوند تبدیل شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/457297" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfGoqV2mw16JdxDzFrXDpLQdRmlJsl7cmiOF18aPJZWq7Fw3sAgnXPi21oYBE8mBk5abk5uGCmBSbNQbngqIWtMgl10FA1qBCfQn_GaRDoVZoZSujiwLz0jl7G0hYjT10y2WEQpQthh3xlzDMcmH1QbAVbC6Q8KLwVqbnAnKWglTTpXosihnILORK37eIEO6L334wAXzVHXyEEbYBUmfC3-ZPBK2wFHKGZT98aJeSd_3eTh3pk1UlJl8eH57l0sjeIBQRT-lR5bpbrjhekBU9Jn1Z2huhFXh7ckKNgZKmvD_SvVC3Ov6bFP9qxGwwUV_L-rqeNAqUnMq4Uj60D4xww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران مصمم است که مثل کارتر، ترامپ را نیز تحقیر کند
🔹
ترامپ چهارشنبه مدعی شد که «مُهلک‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است» را علیه ایران اعمال می‌کند.
🔹
اما سی‌ان‌ان تأکید کرد که رویکرد جدید او، تاحدودی راهی برای حفظ وجهۀ خود پس از شکست در وادار کردن ایران به تسلیم از طریق حملات نظامی، یا ترغیب ایران به مذاکرۀ هسته‌ای از طریق تفاهم‌نامه است.
🔹
سی‌ان‌ان افزود که این تازه‌ترین «چرخش گیج‌کننده» ترامپ در درگیری‌ای است که آن‌قدر تغییرات تاکتیکی و تغییر مسیر به خود دیده که شمارش آن‌ها تقریباً غیرممکن است.
🔸
اما بسیاری از تحلیلگران تردید دارند که تهران در درگیری‌های کنونی در برابر آمریکا عقب‌نشینی کند. ایران دهه‌ها فشار اقتصادی از جمله شدیدترین تحریم‌های جهان را تحمل کرده است.
🔹
این شبکۀ آمریکایی گفت، ایران می‌داند که ترامپ تنها حدود دوماه با انتخابات میان‌دوره‌ای آمریکا فاصله دارد و به نظر می‌رسد مصمم است همان‌طور که رئیس‌جمهور اسبق آمریکا جیمی کارتر را پیش از انتخابات ریاست‌جمهوری ۱۹۸۰ تحقیر کرد، ترامپ را نیز کاملاً تحقیر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/457296" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند.   @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/457295" target="_blank">📅 00:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/457294" target="_blank">📅 00:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fa9c666.mp4?token=JDicpo7mPuX-IbQmZOLgwiT-I-KMZWr0_WQaA9Rw2v1poiT35emGzV9GMi3fn8N7cjHHMvGF4i7j67Iv2jjZC-_sHtWWSjJNNn9G0n0Pg8E_K-QifuU6YxA9CCBRSbQBXokzoi4gUBqhnAEvReujqJD2yBAfvMH5EY46r1qepcOBBShqOzofh2udssvK2OL3Pno_IA3lSbrQeSmDSCdXEIOL1oL1CjdUXo_kto_cP-Tpx5z8gWFy6eA7OWa_sB7Diu-_TV1iIIznnZmuoDLtRQh5kXX96Hrs7qsSu28CI3NhjR67huj-Q8flJGmgIhmd3F00Omyd0CNiqm770UB1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fa9c666.mp4?token=JDicpo7mPuX-IbQmZOLgwiT-I-KMZWr0_WQaA9Rw2v1poiT35emGzV9GMi3fn8N7cjHHMvGF4i7j67Iv2jjZC-_sHtWWSjJNNn9G0n0Pg8E_K-QifuU6YxA9CCBRSbQBXokzoi4gUBqhnAEvReujqJD2yBAfvMH5EY46r1qepcOBBShqOzofh2udssvK2OL3Pno_IA3lSbrQeSmDSCdXEIOL1oL1CjdUXo_kto_cP-Tpx5z8gWFy6eA7OWa_sB7Diu-_TV1iIIznnZmuoDLtRQh5kXX96Hrs7qsSu28CI3NhjR67huj-Q8flJGmgIhmd3F00Omyd0CNiqm770UB1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ انتقام بر دستان مردم کرمانشاه، در اربعین تدفین امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457293" target="_blank">📅 00:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بازی تراکتور و پرسپولیس بدون تماشاگر است
🔹
سخنگوی سازمان لیگ فوتبال ایران: با توجه به آخرین استعلام از ارکان قضایی فدراسیون دیدار تراکتور و پرسپولیس در هفتهٔ سوم لیگ برتر بدون تماشاگر برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457292" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe5d1196d.mp4?token=AmJukHeDRZ1yDKA6JQ-anDzOAjQ35XoLVotvX_4njZvUjwG_qVnaniiYivG9fWNo7C8CTLs9P546JmYkPe7qUrhD5zJ3ir51Bpge6btx2Ps2_25fdf01IHA6qnYZcAAvfHFI8v_37G7CKx20UUHd_0cuI0E9VOvf5WtKem6fHF61obo0V513l2ppcl4uHVO6I6wngUPj5BKu0TH5Koz9QIF8fJndpO0A5_KC32b387n0CmBz7_Y4ZAqEU4FxJJaREH5Xx-bFBugweeA1S6TAgo4OXrOxo7wMvk7ofytT7-5Mr0JUd3QYT6gqSV9v0HM90pstOLx7Vsz1JUos-gOnL4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe5d1196d.mp4?token=AmJukHeDRZ1yDKA6JQ-anDzOAjQ35XoLVotvX_4njZvUjwG_qVnaniiYivG9fWNo7C8CTLs9P546JmYkPe7qUrhD5zJ3ir51Bpge6btx2Ps2_25fdf01IHA6qnYZcAAvfHFI8v_37G7CKx20UUHd_0cuI0E9VOvf5WtKem6fHF61obo0V513l2ppcl4uHVO6I6wngUPj5BKu0TH5Koz9QIF8fJndpO0A5_KC32b387n0CmBz7_Y4ZAqEU4FxJJaREH5Xx-bFBugweeA1S6TAgo4OXrOxo7wMvk7ofytT7-5Mr0JUd3QYT6gqSV9v0HM90pstOLx7Vsz1JUos-gOnL4ZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۳ شب ایستادگی در خیابان‌های شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457291" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5a2cab7d7.mp4?token=Y6p5yNEb7AFf5kc_-0KgJBVrNaZyz45BmlAkdqip4EL_NOG-L3GIDunhO0SJtESoPQI59fhTp3ffC_9xHenNzrd6YGl670Cp_3ylRhimppsi_Qw_MwvFVVDa7tY9nu8hYbCNgwLa-1RwQeK49bNOoVMQt8Qe_LTiGnmHGZfmWWDuIjIAoPkwgePniY9HYyEUttX3s6uL3b70Maj7rML6xY-GLaWanD_UQwELencu1qmWXifmSyFbM_yeqCAChn02Bcg1zDtdgRBlZCItpToIZ9JtNSo2oYiHJfHtc9novP3FdoaXmaQgetPK_Wl1I9LMouzqSVT0IM5WWiY_Z9nE9Jp1wRdfmxNEcmComlVTFMOqIt0AxbccY6KCC90a91b5joiALplKG9fKuHGlHltOoO7p2R_Aj1beyks3adN71nYTuaCdXzDKEBpZRx0u3bk8Qdqedbt6rcI6omZfj612lizixUtd8nLeDx_Zrzdke4rLbRj8uvuydsb51Qaqzm2k5Y2AlqXCvIy3CgYFn2bVS0cC_Smb2_UoIUdZ7m-5BSBJoyxsEBbVbkJi4ebnKXvCLSVSCbgRAdtaacvjEOZTf17ugNezMW8NO1Zl3wLrc-3qox0WrGTyxCGEbwc9nJfxtc-L9DY9XpLZBoLZsbkgu3qpQJncpYzsfmkLp5_AQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5a2cab7d7.mp4?token=Y6p5yNEb7AFf5kc_-0KgJBVrNaZyz45BmlAkdqip4EL_NOG-L3GIDunhO0SJtESoPQI59fhTp3ffC_9xHenNzrd6YGl670Cp_3ylRhimppsi_Qw_MwvFVVDa7tY9nu8hYbCNgwLa-1RwQeK49bNOoVMQt8Qe_LTiGnmHGZfmWWDuIjIAoPkwgePniY9HYyEUttX3s6uL3b70Maj7rML6xY-GLaWanD_UQwELencu1qmWXifmSyFbM_yeqCAChn02Bcg1zDtdgRBlZCItpToIZ9JtNSo2oYiHJfHtc9novP3FdoaXmaQgetPK_Wl1I9LMouzqSVT0IM5WWiY_Z9nE9Jp1wRdfmxNEcmComlVTFMOqIt0AxbccY6KCC90a91b5joiALplKG9fKuHGlHltOoO7p2R_Aj1beyks3adN71nYTuaCdXzDKEBpZRx0u3bk8Qdqedbt6rcI6omZfj612lizixUtd8nLeDx_Zrzdke4rLbRj8uvuydsb51Qaqzm2k5Y2AlqXCvIy3CgYFn2bVS0cC_Smb2_UoIUdZ7m-5BSBJoyxsEBbVbkJi4ebnKXvCLSVSCbgRAdtaacvjEOZTf17ugNezMW8NO1Zl3wLrc-3qox0WrGTyxCGEbwc9nJfxtc-L9DY9XpLZBoLZsbkgu3qpQJncpYzsfmkLp5_AQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی تراکتور و پرسپولیس بدون تماشاگر است
🔹
سخنگوی سازمان لیگ فوتبال ایران: با توجه به آخرین استعلام از ارکان قضایی فدراسیون دیدار تراکتور و پرسپولیس در هفتهٔ سوم لیگ برتر بدون تماشاگر برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457290" target="_blank">📅 23:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418ad869a4.mp4?token=SeceZI2SpP74lLkpPu_5zj06wsbvfNU-ELf72Bbj0_9HzU2o8uG5mv3NA0k3J6husXA_-84iaVhFPL0UQFnBkVBkMLhf7a-0wrC8-gPWFQP2rJkCeYzEsejPjy0iATLY944MyjyzJKhm_RnwPMTMqbY268CA70w_0jiTg-so7-onLyR1L2YCCPyoMb61J9rdjvubFb0P5uASEK2_pc4Tne2C7pEZa-y0Q3TwUX2thET0WkBGdbAQSHlXmFx7x7Y0WdgSZNGiRf3RpP8vrIF5gIBWafmbFy2bLjf0kfFXKKMjhaB939rM-9EScDZSUdFBtagFv20YJA1WwTHgHVLxtikWSu-xI2spfK1UzgwSabFutNXJBJ8z73bw73dJc_eeI7hqKr97rIxCBu7zN6blhph2-M8hhoEMTOzquBO5yfTshg_6m2TNkrKI_NOwm0f6TXnLyFKuDhwGOWFM0BUGIjFJn-JMB9TgYJBbK5bHhaKRLdU0aaGI7mT666rSh1Vlmqo2HT6sbv1_vRFP1CzaO00HgfWt-InE6Hq9VRwwpjXdug8OMFiBgfzFvPbzT3VZHXM58Yt34J1tcXi1WGzaaXTaVd0Me_llv4GJ2nz_2zZV0_PrjmdRn23wWSNvsd3Ql9FcbvqLDLiu_8udrPf2DGJfPhLgbplTf0T2SRpK_rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418ad869a4.mp4?token=SeceZI2SpP74lLkpPu_5zj06wsbvfNU-ELf72Bbj0_9HzU2o8uG5mv3NA0k3J6husXA_-84iaVhFPL0UQFnBkVBkMLhf7a-0wrC8-gPWFQP2rJkCeYzEsejPjy0iATLY944MyjyzJKhm_RnwPMTMqbY268CA70w_0jiTg-so7-onLyR1L2YCCPyoMb61J9rdjvubFb0P5uASEK2_pc4Tne2C7pEZa-y0Q3TwUX2thET0WkBGdbAQSHlXmFx7x7Y0WdgSZNGiRf3RpP8vrIF5gIBWafmbFy2bLjf0kfFXKKMjhaB939rM-9EScDZSUdFBtagFv20YJA1WwTHgHVLxtikWSu-xI2spfK1UzgwSabFutNXJBJ8z73bw73dJc_eeI7hqKr97rIxCBu7zN6blhph2-M8hhoEMTOzquBO5yfTshg_6m2TNkrKI_NOwm0f6TXnLyFKuDhwGOWFM0BUGIjFJn-JMB9TgYJBbK5bHhaKRLdU0aaGI7mT666rSh1Vlmqo2HT6sbv1_vRFP1CzaO00HgfWt-InE6Hq9VRwwpjXdug8OMFiBgfzFvPbzT3VZHXM58Yt34J1tcXi1WGzaaXTaVd0Me_llv4GJ2nz_2zZV0_PrjmdRn23wWSNvsd3Ql9FcbvqLDLiu_8udrPf2DGJfPhLgbplTf0T2SRpK_rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا نام شکست بعدی در برابر ایران را انتخاب کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/457289" target="_blank">📅 23:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457282">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsPIFUQMM2EuTOcTWmPWv32yQllS9JRXfseAACPBDHzLdq2XwAuPGQ196Vv0PkA_apWAkhClfohTsS2EyYAGBi1ZBI8QLYXzBVrQitzTIopSyoXamFZSIwZ0QTvmo1zvepNIhmkYOAgzotttsj4bsyjDmwg4Nujc_3IBugfnv10zuDxBEJ9CVYhVwESwFrVygXF_rZoIxLyuyVjaqURw-u2nlSWWKQAWmxl6DIKwY9faQRjLQSr9OA8HfnYmUM3WaMvLh5jabN6Q8YOBpoVfdMnZhznUIoOZkDe-m_ms0DXbollPUk1DyvGPBh4iMq7EPIwJt3QMaVhgQAlmIXAv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDefABzzHtVGt9FjSYBCcrS3Fjqr3lYjlQ_qpkrxsWSRKFbyWZE5JjuwYswEexNyW5CsbDIy44EslTrgutjNwjMyJBuos1Xh5WDaXTbrkiY7VNeOfB2cJrhDITyQQPAUhdsBfLxiC2vA2Y9dkVcs_vSWi4nD-YT7RJUF6sgjNtdvXtw7pEbsuWlHKSUXxT_qz7RVapev2iJ6qWciRmifBA0ILNVTdzSdRSFZUZW4NkQMndB5cMtxd8JYxkw0rtjWFxAlvA-nHm6yGrPbCYuNp7nok9zAgsxpUOQxB6Yg8qLqd6V7Ece8lmEkwBR4EHZ4Z7-BbZi_BVnJOTx1D8qh5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTJgL4k-AjDB_Nu5fKXs1UAWMCcsptUcWUTuFcb5ygklg5GYwOZ5IAMXQmkT8uEEzc_2EbfEixE-llLqcutpiQ2_Bzm7np0zB-1n6JQf1R4c9vudy2XXSqgz1Fb-brBsB4gBk_tb3NRJ_qMqSaFjG1wI51UOChVA5VhguA-5OtPtRPHKTczAni3204U1bYpX44MfdUH4ONMYJ-Xc0xFPhi3zUuKmNU-Naba0HQiMtjCPWXtcJZtLXYEzpigE725QKGq1fuU9jgwsD5-vygEUf8ygXxR4aripuG8YnfF_wJ6ZUGmRIA4Uire9Xdueau5B6YZrplUsTXHkEDPiAzQztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GR-zanHKhCpyl3y4zb9RRY_ZB2z_EM19IHU29TAOg7rPv8kEhrx2GvgjeFW7mGBoxXKe-fzjMl8eWRH9qSaj-Af0b-pTGeYawJ0WXWXtfakD1q_-iEP23jn0MivkJXIXkdUvvsv3FECt-CkdLVtK0xFPzePmlZm4h0iY0QXoBNdGrPJK1NtIuHLz1QYbLcOZjnobmc6W1fWQkXrIaL7YcFT7s_JreqrNZJiLGzFMTAIOk0KhtQthOZHoCGX6jrKxnscCVWKR5CpW6XBzSZV2Ql0yYJVp5oMJ65DBQjTfowIY8GrzGv5sbcHd7MJtqSeACvM0ypsYtK6EVWLgBmPtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W54_BpPJLZNgHVENyjVLc4IXz2LqNzP3D6-85Fom2342jD-mVvXYdARGHferp58BwxENl4qizjdQ1v6cHUlFFrQT4naA1MSJQ7JjWVbhQ8fYbnD-Ck7MToUkO7mK3GUjtuWvvRYA8ZD0SjFNu_-L0TjJQaLOysFezC_wDRQsHdksQ-hpNZz3VfORBvYsXTwRmAWcZUxhayDFER1KWLL3R6fsEf01IEmSkJ35aJKVlqDbA-zCJtSxerFJPmusbw4in7JWMg0o7YJWAKC1BQPhGw8pDmifeno_hyoIVTwhiwDD9zRlr2VU2YMHQoNFyFXjUyxWKUxS8jqiZoLz172-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXML-GtSVe-moo8mypkT8bpq8tszBypPFbTqr32awv8853pZ4GeqOyS75Ef-zRzgeZ26neOQQ4q0IqHayiKHQv2lPcKw9qqv0tQJqwyDf-4V9-8bXx--TjIt5oejc_6E_ARZJYhzpm_UUAPew6lu-MV5eVDpWH5fL2dESbEndeJBSDJsUTfLQUNKGRUbNYstzijy0Sii6MxQkXWbCu97w-8DCg6lLW8X4lJbwZ09UyDwF2JpPFhhUr7PHSUFX8M07oHQ5qXnZl2KW9-rzvDN3qb8ms0-FwEajuwIPFdOS496PlwoYm-LHGT-XshRcGG2xW-9u547q8NGZzWcnSNfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6F6HvPep8J4tRh5a44TElTeyYqGTqsoma24JQI1IzDA64Eg1qnRstl3b224w5U4oZRBFKStDYhBIaN1Q2DLIFSjppsuqaMTRehG6A06Nun6L7IfQR5q47l2SZWb5KNshSU-3opI8kmB-kFEHrEAI6wbxDByKq1q1o7fMKLWXL6aFT62U9QyKGDzDjEC0LXGp9DWJVgqTRk4RaxhrjlZ_Qeay-4BjxyP0jd1I_VtekcbJbWNDn3FdjlO8OQV9_N9tgD6Ez_BK0DihZLamdgQ7eH1-6LS80EKqnbo5fLFr_oAsYDzg7qNa1EEY3zXoJf72u4NcvBURCXgfj7uahzJHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حضور مردم عزادار در جوار مزار رهبر شهید پس‌از مراسم چهلم تدفین ایشان در حرم رضوی  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/457282" target="_blank">📅 23:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457281">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=WNG8wNnreNcpTOi_W3Nlv6ZXj2WG0yrQu-Bj8EFsQmjaYzk__-_0UatmFyKlO9GM2g7qgcqJC6Eu42iKIbuj1vjlMwAhZ8ARq4vVy1wh_sfzSYzjBPovgN9h0rEHnf2JkNTZNwQMU2ONdOg4FC3DTX1Rimmt5msRaoHT41cRJB8SI5o1gGdA-gPg4A7DIn_EEcPpuWjVJgRXFQTMiO1Qa0kaaF_MwkHrk2EGrxDWCBCH-iuYWRD7rmDczv2uNIAlI2bRpzpP_tN0nlhGLqQ_V9Hf70TeoG4R64T-n3BFQsSFPPGQukT74MoihJxbIb5RkMtJTX2iEeEL-eFP17LOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=WNG8wNnreNcpTOi_W3Nlv6ZXj2WG0yrQu-Bj8EFsQmjaYzk__-_0UatmFyKlO9GM2g7qgcqJC6Eu42iKIbuj1vjlMwAhZ8ARq4vVy1wh_sfzSYzjBPovgN9h0rEHnf2JkNTZNwQMU2ONdOg4FC3DTX1Rimmt5msRaoHT41cRJB8SI5o1gGdA-gPg4A7DIn_EEcPpuWjVJgRXFQTMiO1Qa0kaaF_MwkHrk2EGrxDWCBCH-iuYWRD7rmDczv2uNIAlI2bRpzpP_tN0nlhGLqQ_V9Hf70TeoG4R64T-n3BFQsSFPPGQukT74MoihJxbIb5RkMtJTX2iEeEL-eFP17LOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات پهپادی یمن در عمق خاک عربستان  سخنگوی ​نیروهای مسلح یمن: در پاسخ به نقض حریم هوایی استان صعده توسط پهپادهای سعودی، ۲ عملیات پهپادی موفق انجام دادیم:
🔸
۱. حمله یک مرکز حساس در فرودگاه نجران
🔸
۲. حمله به تأسیسات آرامکو در نجران @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/457281" target="_blank">📅 23:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457280">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32aacd7cf.mp4?token=J-IkyTVrPOVttuJY5qcrLqA8xr-jaQ9booa9xrNGFOTPpoT7LkEIgCZ8SPSFt2XngL4wUMS98sbpolLmdhyqMMLMwcSuuZNEoaBrLpVOcdjLnIV4e84ZexrdA7RpEilRYV1uExU7OomltcClt5FljJEHYR08CUscBv8NOrnX5qB46oSisPyZbzVxE_a-E_9XUFiHdCajaXcCA8KJMcdHlDmxRq5V0DnuxrwIz3IdrkfqOvraU7iiqfc8sqNicz2Hehp5LgLqMmNFZYHRh6nl_0xWksAGMxv2Jk82A33RZtjkD7n92f-jvd4ch0aU-AidHSLu6csj9FD4IA2TuOnvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32aacd7cf.mp4?token=J-IkyTVrPOVttuJY5qcrLqA8xr-jaQ9booa9xrNGFOTPpoT7LkEIgCZ8SPSFt2XngL4wUMS98sbpolLmdhyqMMLMwcSuuZNEoaBrLpVOcdjLnIV4e84ZexrdA7RpEilRYV1uExU7OomltcClt5FljJEHYR08CUscBv8NOrnX5qB46oSisPyZbzVxE_a-E_9XUFiHdCajaXcCA8KJMcdHlDmxRq5V0DnuxrwIz3IdrkfqOvraU7iiqfc8sqNicz2Hehp5LgLqMmNFZYHRh6nl_0xWksAGMxv2Jk82A33RZtjkD7n92f-jvd4ch0aU-AidHSLu6csj9FD4IA2TuOnvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ تربتی‌ها در ایستگاه ۱۷۳ مقاومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/457280" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457279">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reL7l_xUQHAcr2bROEUbJiV_FzvUHWc0YabPLFyRFYcV9Y8JmgvL1ce3bbWfkiCyLyEljXg7UW29IKULQ9XePDd6191ivGuv-Z8jxx-_6vxgnvoBtseC9yntr1cV_gVw7rLlIWE2yJXc-XkaJB133KUwlsOMofGlqcfo41VTsLIyG7roGWWAgOtwhAIXkJZ7psGflPfHS7Fkh6A3MGDvVyJdIDQX6IDoFPJbmXhv0GOU8ujqGaw4rUlh0FkPhE6JO-u1gY19iucK-77UQjyF9yMGTRpC-1hA12rx1urDvIxri_mDdAGxewIpWPZvCj7pk3c4MhsMBbJL4eM1rV29ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: مانع عبور ۴۸ کشتی شدیم و ۸ نفتکش را هدف قرار دادیم
🔹
سخنگوی دولت یمن: نیروهای مسلح یمن از ۲۰ ژوئیه گذشته تاکنون، موفق شده‌اند چندین معادله جدید را در برابر عربستان تحمیل کنند.
🔹
نیروهای مسلح یمن توانسته‌اند معادلهٔ «محاصره در برابر محاصره»، معادلهٔ «حفاظت از حاکمیت یمن در برابر هرگونه نقض از سوی دشمن» و همچنین معادلهٔ «هدف‌قراردادن تجمعات و استقرارهای نظامی دشمن سعودی در هر مکانی» را تثبیت کنند.
🔹
نیروهای مسلح با جلوگیری از عبور ۴۸ کشتی از دریای سرخ و دریای عرب و هدف‌قراردادن ۸ کشتی نفتی دیگر، موفق شده‌اند محاصرهٔ دریایی کاملی علیه عربستان اعمال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457279" target="_blank">📅 23:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457278">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDPf0lGApZblCL8qEQFbyC7z0mqev9zO2ggYyKz2pJrtVCGSoKlVAztn6FhB9afaQonEhZCxiqpyf2GmqikhZWtyyYTWdh_ywGbogzYnYdWHvboa-aNz25ZcT5vZkoNis6MxwtE_8yEXYlBg75kjqEQwYD2Beu2MsanwXngOaGCbf-XFqTZN3gMLZdREFALhHoRi_W0_Hq8pcPzZ8xcN0RLQMNFyY0GEixRVvbaE2R4yT0Nn3G63CfJzyaWvuOK8F5zPaUQBZuULU95kweCGiKI5Pt8s9RsEG04CSsUnqLJ57XNrfHpf-VxbcPC7kkdlgG2HWjymdmPSVb5sL2nCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
هشدار دربارۀ خلأهای امنیتی کنوانسیون دریای خزر
🔹
بهمن، کارشناس مسائل بین‌الملل: سکوت این کنوانسیون دربارۀ نحوۀ عبور و انتقال نیروهای نظامی و امکان حضور نیروهای بیگانه تحت پرچم کشورهای ساحلی می‌تواند زمینه‌ساز حضور نیروهای نظامی و اطلاعاتی بیگانه در فاصلۀ…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/457278" target="_blank">📅 23:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=buc1D700o0QmwjSd-shXMehwjiIC0ScFTgCXGY-saOR5Rwl-RzdW3SaruSFfxdvr5VsZCFdvvFYP9ElZd6fzGVdMT_OkVlFEWfG7onC4Of9hERBEyghV48EhEjxBGVWRWsfegGF90g_RK9AP5ibzgsT4RQETyp5QXMyZu62GONt24QnuuU5BfpVhWdb-K73UdS4FPMbx4ELKV1_192z9LGrrKel8tspJaJwbPR67ZKhMa9D68Gk2LzMpaajJeLAB_6SO7xI8vxjGc2GAS951WkdbHfJAFeY-mHo4X4_YGMlF-D9WFsAIe6oIGNCp1vbFPltFVdp3zFNgKhb6up1BNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=buc1D700o0QmwjSd-shXMehwjiIC0ScFTgCXGY-saOR5Rwl-RzdW3SaruSFfxdvr5VsZCFdvvFYP9ElZd6fzGVdMT_OkVlFEWfG7onC4Of9hERBEyghV48EhEjxBGVWRWsfegGF90g_RK9AP5ibzgsT4RQETyp5QXMyZu62GONt24QnuuU5BfpVhWdb-K73UdS4FPMbx4ELKV1_192z9LGrrKel8tspJaJwbPR67ZKhMa9D68Gk2LzMpaajJeLAB_6SO7xI8vxjGc2GAS951WkdbHfJAFeY-mHo4X4_YGMlF-D9WFsAIe6oIGNCp1vbFPltFVdp3zFNgKhb6up1BNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی مرگبار در آمریکا
🔹
برخورد بالگرد پلیس با یک هواپیمای کوچک در فرودگاهی در ایالت پنسیلوانیای آمریکا، یک کشته و ۲ زخمی برجای گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/457277" target="_blank">📅 23:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=XmhrGWs_E6tesSku7OD4Ex2Akca85fj3AQ61gwnKseMnd8UBYYXhYl6CnJyobmsNvQbM5IVDgONPVGf3g1p37gRxbECCXLhE4ucqOAPIP-gET-QDGpaFCHXbPUkqpCZ70F91RJL9LcWtbPraw2yQcn4iSbswk8Z3VT4U4Jx4EqpaaKF8h3j3lv4fH-Rbsa3iuJceHI9MW2swMfYeLiCNNsgVQmABaetnIBJfh9ORmSu09LDID4DMbP3qGWqNz1Cy6uLjaXEieR9y1ZE1h_EpZLd_qZya2J0vCOgmI_J_-amrpYBplkBMwayzvzrRPbnpHWfNCF1wf_O6dw4IaBcfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=XmhrGWs_E6tesSku7OD4Ex2Akca85fj3AQ61gwnKseMnd8UBYYXhYl6CnJyobmsNvQbM5IVDgONPVGf3g1p37gRxbECCXLhE4ucqOAPIP-gET-QDGpaFCHXbPUkqpCZ70F91RJL9LcWtbPraw2yQcn4iSbswk8Z3VT4U4Jx4EqpaaKF8h3j3lv4fH-Rbsa3iuJceHI9MW2swMfYeLiCNNsgVQmABaetnIBJfh9ORmSu09LDID4DMbP3qGWqNz1Cy6uLjaXEieR9y1ZE1h_EpZLd_qZya2J0vCOgmI_J_-amrpYBplkBMwayzvzrRPbnpHWfNCF1wf_O6dw4IaBcfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامهٔ تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
به‌گزارش الجزیره به نقل از رسانه‌های محلی، اسرائیل منطقه الطیری در شهرستان بنت جبیل لبنان را بمباران کرده است.
🔸
ساعاتی پیش روستای المنصوری در شهرستان صور نیز هدف حملات توپخانه‌ای رژیم صهیونیستی قرار گرفته بود.…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/457276" target="_blank">📅 22:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ناو بحران‌زده لینکلن عازم آمریکا شد
🔹
ناو هواپیمابر «یواس‌اس آبراهام لینکلن» روز پنجشنبه پس از یک ماموریت ۹ ماهه که بخش اعظم آن در پشتیبانی از عملیات‌های ایالات متحده علیه ایران سپری شد حرکت خود را به سمت بندر خانگی‌اش در سان‌دیگو آغاز کرد.
🔹
حدود ۵,۰۰۰ ملوان این ناو تقریباً تمامی این ماموریت ۲۷۲ روزه را روی دریا گذراندند؛ دوره‌ای که با گزارش‌هایی از کمبود جیره و اقلام تدارکاتی، اختلال در سیستم لوله‌کشی و آب آشامیدنی و وخامت شرایط معیشتی در داخل ناو همراه بود.
🔹
ناو هواپیمابر «یواس‌اس جرج واشنگتن» که در ژاپن مستقر بود، جایگزین ناو لینکلن در منطقه خاورمیانه شده است.
🔹
ناو لینکلن اکنون در حال طی کردن مسیری حدوداً ۱۳,۰۰۰ مایلی به سمت خانه است که انتظار می‌رود بین چهار تا پنج هفته به طول بینجامد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/457275" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxO7XMNqx-YJ0zoed3MD0_6G-2NTPVlPoPf5Yx_ENlFqTFv5rTQ7AgHOLJN6mIEsxU5937v8mYSZOx1LxAj3kxqEDig62rr-hHhqa8z6IE2DddzqpLRYnlOAAtanij0kWORetcl2odEOGwt3V1S4kBYEzs3j_IFZ9b4BmVnuC4toPIPEoqclhd9qWTyYxP_O1NkJ4edU0IIkSs6ZK7Bkf9_WC9G4-cYwY1_hte1SOsJZM3ZuqOi7erHb_MqzeV5Rxf4w0g0w9dj5li3d8MH4WRYgJzM8GRr5k4aT5zZb8OAa2MvAAJ_6BxUoIMBvmkqS-0OSxKc-Vpx89uH6Svicwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: کشتی‌ها
از بیشتر دستورات آمریکا سرپیچی می‌کنند
🔹
الجزیره با استناد به داده‌های شرکت کپلر گزارش داد از ۱ تا ۱۹ اوت، ۲۳۶ کشتی از تنگهٔ هرمز عبور کرده‌اند که ۸۳ فروند به‌طور آشکار از مسیر ایرانی استفاده کرده‌اند، درحالی‌که تنها ۳ فروند از مسیر عمانی عبور کرده‌اند.
🔹
براساس این گزارش، در میان ۱۱۲ شناور نفتی و گازی عبوری نیز ۲۱ فروند مسیر ایرانی را انتخاب کرده و تنها ۲ فروند مسیر عمانی را برگزیده‌اند.
🔹
الجزیره با اشاره به تهدیدات آمریکا علیه تردد در هرمز نوشت این آمار نشان می‌دهد کشتی‌ها در عمل تمایل بیشتری به نادیده گرفتن دستورات آمریکا دارند و تعداد بسیار بیشتری از شناورها از مسیر تعیین‌شده توسط ایران عبور می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/457274" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af02dd1c5.mp4?token=cCxEbh7pR3PXCRglQiEUbZldoKjqU6OrUaEwoZz38iOdmXVfDIEs5oGURiX8H8WPHOQKfBchmcgTHfUVxAIPAzqfc_iFOHvlQX_I3H8eIstE8HLZSUIq5jaKC84P9v9WTbK-ks7mQpOjn4Q6TrwSY_z-9CE81HSThP8VxdDHARbUsmm8pHj7Yu6jYiJUBtgdbnLGanG7xYoXtFbCSIZI1KSshN-vxkWZ7_YMv8vg3rd_tYBqY5UX8P7BRNELzodyx9CO65OuEkyFpyB3QGaMpiXU045G9KXl4REaZwaCFlnGTIpMBPJNuvwiy0sE9D5cfJPGX17Bb26LesysqwX0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af02dd1c5.mp4?token=cCxEbh7pR3PXCRglQiEUbZldoKjqU6OrUaEwoZz38iOdmXVfDIEs5oGURiX8H8WPHOQKfBchmcgTHfUVxAIPAzqfc_iFOHvlQX_I3H8eIstE8HLZSUIq5jaKC84P9v9WTbK-ks7mQpOjn4Q6TrwSY_z-9CE81HSThP8VxdDHARbUsmm8pHj7Yu6jYiJUBtgdbnLGanG7xYoXtFbCSIZI1KSshN-vxkWZ7_YMv8vg3rd_tYBqY5UX8P7BRNELzodyx9CO65OuEkyFpyB3QGaMpiXU045G9KXl4REaZwaCFlnGTIpMBPJNuvwiy0sE9D5cfJPGX17Bb26LesysqwX0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتی، عضو کمیسیون انرژی مجلس: ۶۹ میلیون ایرانی خودرو ندارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/457273" target="_blank">📅 22:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e0332a80.mp4?token=DQoewvEv22GMudTeykeSwU11jfg4jQTwSVKNw9qcC3gLHs9nG2PY__UUNEIGeGqbUjwdPu4VmaCd1wLwgl4q4jW2r7H1YRJtHbCfFkaGFgD5ghYKLJZB0-4jveGf5b8UPsReJmQu5MJ7LOk_CwrjQ1VzZcGsOcfqtfeEv4AOw0B4gtLONHvoYB5AMBrmMM2El7vb-YRaB2UJQ3FJctr93wok8MMvj8sDgclSYxg9rmjFiY_V0JOZ3jpMn2HbMuZoijumPLNSwXCQfRMH-X0YYfMFR4dUSmxtK254kKkVurQNqeC8mvXH304KbyI0LX5RDXYYyYy2eZPiJ9Wgo2rhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e0332a80.mp4?token=DQoewvEv22GMudTeykeSwU11jfg4jQTwSVKNw9qcC3gLHs9nG2PY__UUNEIGeGqbUjwdPu4VmaCd1wLwgl4q4jW2r7H1YRJtHbCfFkaGFgD5ghYKLJZB0-4jveGf5b8UPsReJmQu5MJ7LOk_CwrjQ1VzZcGsOcfqtfeEv4AOw0B4gtLONHvoYB5AMBrmMM2El7vb-YRaB2UJQ3FJctr93wok8MMvj8sDgclSYxg9rmjFiY_V0JOZ3jpMn2HbMuZoijumPLNSwXCQfRMH-X0YYfMFR4dUSmxtK254kKkVurQNqeC8mvXH304KbyI0LX5RDXYYyYy2eZPiJ9Wgo2rhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم سوگواری شهادت امام حسن عسکری(ع) در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/457272" target="_blank">📅 22:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb32a4ff64.mp4?token=aviM6OEQ1su6klsI-lF-J9rNbr_eAP_a5_5DgNFjXoREh_f01OVjBO_6_3aqJbfr6Sh_KZ4qy4g0QYEmecwfeGIn9OWbRZcxHICagO4FmwcT_w5LW3s6v-y6UAdjs16YwYcsIQohVDdvQZItugfhXE5iaVK8rynxEkkFiYkZ-NYEIPlybVC4x0BbPCHglTfXd0uF-osd3aE8arZ5o_Mmz6keCqWW7Z_ql9mdSwIrtuCmuvC1XIFK_ZMBsrCoYMfc3bDLlhqMLGxmnzXzXZvs5LXBCgkmfuikM_gQRlcPZfk2uQTa06TXYOAOVFcLivAwch_wekTD-ct9m8Gk3hyD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb32a4ff64.mp4?token=aviM6OEQ1su6klsI-lF-J9rNbr_eAP_a5_5DgNFjXoREh_f01OVjBO_6_3aqJbfr6Sh_KZ4qy4g0QYEmecwfeGIn9OWbRZcxHICagO4FmwcT_w5LW3s6v-y6UAdjs16YwYcsIQohVDdvQZItugfhXE5iaVK8rynxEkkFiYkZ-NYEIPlybVC4x0BbPCHglTfXd0uF-osd3aE8arZ5o_Mmz6keCqWW7Z_ql9mdSwIrtuCmuvC1XIFK_ZMBsrCoYMfc3bDLlhqMLGxmnzXzXZvs5LXBCgkmfuikM_gQRlcPZfk2uQTa06TXYOAOVFcLivAwch_wekTD-ct9m8Gk3hyD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره رئیس بانک مرکزی از توصیه رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/457271" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1fe95072.mp4?token=Aapeg71Rbyxvu9AQ6_nU17PUwaTEoWK27zHArm9gnGXKKBOz0vRDbA_VCzdQB6DeXBTDmXtliPxnpLPRu5jPoo_I_Qkzpe5U-tjj1wyFcRx_ygdz6IjLa-r7sbXazak1woKAAlxwvjBEtcaWgz3_N2aWWjekKOy0ayZAvE_ega8O6jeCNmwkGOBGfHD_loFb9vz1nZNoxiETliwmpQQIApks3gngLavWKYKlX43rNSFhKGW6-Gz-a8JPmj5jUgs_l8I3HCKUV5SA165Gq6B9Qnrgk3UsjPYe0DNZPo7HNIYM6-NuCP_W9mMzzwfo0Ytv1ehmhNmG5r2MJf9PP2GoVKY2wCspakkSk2qLeJ7CgLN095Lph5XWrxxZmjhW0R_24Y5Uq4NbvNVBtZdkH-0MdObiEnQCRNm_Hy4B00QTyg1nZ2hvnVsEclz5hC9xkZR77mpiqoSCnYYYoQvySTITZbEoXlcE42ub7GS5I15TKWPhcdhLvCfe3Q_mw46EafRu-j-kyHzYGN4j-QCZSsgG9DRbwhdd_fvcIC4cC9fxDtgnuB2Df9ZNnjx7N5FcmsWkb4EC6_ZMUzPfNuDhAQP8nkdc6CmwE7hSW-GzOBJimipS1NiGD7cA5PZyNOthhsPyEOlGX53AXffszLNx-qVh3JMMaSRrnl77fJVQsg1VGko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1fe95072.mp4?token=Aapeg71Rbyxvu9AQ6_nU17PUwaTEoWK27zHArm9gnGXKKBOz0vRDbA_VCzdQB6DeXBTDmXtliPxnpLPRu5jPoo_I_Qkzpe5U-tjj1wyFcRx_ygdz6IjLa-r7sbXazak1woKAAlxwvjBEtcaWgz3_N2aWWjekKOy0ayZAvE_ega8O6jeCNmwkGOBGfHD_loFb9vz1nZNoxiETliwmpQQIApks3gngLavWKYKlX43rNSFhKGW6-Gz-a8JPmj5jUgs_l8I3HCKUV5SA165Gq6B9Qnrgk3UsjPYe0DNZPo7HNIYM6-NuCP_W9mMzzwfo0Ytv1ehmhNmG5r2MJf9PP2GoVKY2wCspakkSk2qLeJ7CgLN095Lph5XWrxxZmjhW0R_24Y5Uq4NbvNVBtZdkH-0MdObiEnQCRNm_Hy4B00QTyg1nZ2hvnVsEclz5hC9xkZR77mpiqoSCnYYYoQvySTITZbEoXlcE42ub7GS5I15TKWPhcdhLvCfe3Q_mw46EafRu-j-kyHzYGN4j-QCZSsgG9DRbwhdd_fvcIC4cC9fxDtgnuB2Df9ZNnjx7N5FcmsWkb4EC6_ZMUzPfNuDhAQP8nkdc6CmwE7hSW-GzOBJimipS1NiGD7cA5PZyNOthhsPyEOlGX53AXffszLNx-qVh3JMMaSRrnl77fJVQsg1VGko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این رفاقت‌ها در تجمعات شبانه شکل گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/457270" target="_blank">📅 22:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4515138cb5.mp4?token=QCln7ZQGEQBTRW_uy2KeeaIAvF3E6CWh5wrE6pSzoxeR1FsZm7xZ0UR-nZ4CfrvPx5Zc8s-pscTs4YhQYLLUWmkeuBAZJHtl0XBbM9JBe6iscu-P-EUF01Q4jAWZMyuCVjCsuG86vC-p7gTivD2c9sBoCfWvDbpi_7D8-3fexxE4VOL5G9UtyL3OvXDHP_2Bolff0nt0JYu0Jb69Nl-4Le5Gb324H2WS6GLSG1hKF5lvjZNc7VkCe5-XCJ5_Kvkwz3rrTTc18dOi20PNip44WP-qBy5u3_Cw20osK31R90-WJ55hfwJua-fvFEV7o3mfURv2Fl4mm10Vso72L02XWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4515138cb5.mp4?token=QCln7ZQGEQBTRW_uy2KeeaIAvF3E6CWh5wrE6pSzoxeR1FsZm7xZ0UR-nZ4CfrvPx5Zc8s-pscTs4YhQYLLUWmkeuBAZJHtl0XBbM9JBe6iscu-P-EUF01Q4jAWZMyuCVjCsuG86vC-p7gTivD2c9sBoCfWvDbpi_7D8-3fexxE4VOL5G9UtyL3OvXDHP_2Bolff0nt0JYu0Jb69Nl-4Le5Gb324H2WS6GLSG1hKF5lvjZNc7VkCe5-XCJ5_Kvkwz3rrTTc18dOi20PNip44WP-qBy5u3_Cw20osK31R90-WJ55hfwJua-fvFEV7o3mfURv2Fl4mm10Vso72L02XWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ چیز نقش و جایگاه ولایت را ندارد
🔹
سخنرانی حجت‌الاسلام علی علیزاده در مراسم شهب شهادت امام حسن عسکری(ع) و بزرگداشت رهبر شهید @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/457269" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65b52ec31.mp4?token=vxvmCppr-Jx1cA67kdJDlpOfT4c53sPofIWk-YEw4PUasRXWtgLiWPWWdkSQ2L8xnXp33Ar59iIhi66qBjiR5cMSezVOUYJem7Y1dKFP9q3pBS_Charovb0TwTgUIzC2fIsrIdojgrnK-IX9KETgJYsrxIa27Hc-UywDQLtLYJUTHfGYrWUcEGaf6kSywzCDpTpXi77Y1x4OMr_7G9VOZ6pGoxVtRdCm-QbZY2os_R6m3MvPSNdcmD_oqvN7Wd0Nnj2jCICUWHY31sooIZZB79Mq3rRLxUNDMffLxgRuUcB6UgWw_p6PM1c_cC5YqSg1II5PeIxiF9M5bzoaRpwMQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65b52ec31.mp4?token=vxvmCppr-Jx1cA67kdJDlpOfT4c53sPofIWk-YEw4PUasRXWtgLiWPWWdkSQ2L8xnXp33Ar59iIhi66qBjiR5cMSezVOUYJem7Y1dKFP9q3pBS_Charovb0TwTgUIzC2fIsrIdojgrnK-IX9KETgJYsrxIa27Hc-UywDQLtLYJUTHfGYrWUcEGaf6kSywzCDpTpXi77Y1x4OMr_7G9VOZ6pGoxVtRdCm-QbZY2os_R6m3MvPSNdcmD_oqvN7Wd0Nnj2jCICUWHY31sooIZZB79Mq3rRLxUNDMffLxgRuUcB6UgWw_p6PM1c_cC5YqSg1II5PeIxiF9M5bzoaRpwMQoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت به بالای ۹۳ دلار رسید
🔹
قیمت نفت خام برنت در معاملات امروز با عبور از مرز ۹۳ دلار در هر بشکه، به بالاترین سطح خود از ماه جولای (تیرماه) سال جاری دست یافت.
🔹
این افزایش قیمت درحالی رخ داده که نگرانی‌ها دربارۀ اختلال در عرضۀ انرژی با بسته ماندن تنگه هرمز…</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/457268" target="_blank">📅 22:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQAcKsimD2Kj14iO8bECz3ha0kP_-Jk3NhLTU9qKxXb4oTwM9B8XGIuZIG2ZBAhSiqd5ggxWd4UlFMVoq7MJx31NlUj50-3ioN7XeZ8ZKDWVeGUtGFdna3XCRtaAPjIUNnrcTPWSmvg8dwkYzoXl0q88icKIGovYZpv_lAh9V5yJaKVgZ-uvLF6sFhrEBSOMjKKDt6gHKmQMxjtGpVPYTM868mq1ZeBifwfwWUB9G-yzWx0FP2g9pwXSnksKDXEwS5hn9IPvNZr3ZE90fzkIx0Wfvf6wA30bwY_E97ZrW9rdYub0gMclsjMrJuq1BtehL_tuD8-PIJWeRzoXnPpzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل: ۹۴ درصد مردم غزه سرپناه ندارند
🔹
محدودیت‌های رژیم صهیونیستی موجب شده است تا از جمعیت ۲.۱ میلیون نفری غزه، ۹۴ درصد به اقلام اولیه و سرپناه دسترسی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457267" target="_blank">📅 21:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxLKP8k8Z7FZ6lkSHfCqodSBL09xAuo2skkk5NllH5UCNzqczJpT9CU7ECEbm5HNqpVxnvWR8w0sjcrFQDOlhXR04zUMkXN_6129Wy-5E6PzPcBwxsXvgJ_fSAj-PmNg2FL_p5ZoKlpbc0_JixwZrhVsdV3ZIwKo2gJ_s3nIp7dGOkB9fmX0Tlci1OOZaZHVgV3JU1md-CRHkCYTHqQh4mNAPBByukXxJVfk_3SrdtGmBkBWcOEUsAtGzwONhyCTExdGa_fX_ziTrqJvBY8gWg3u9a83iLAL80AEHtzpOTqfjs_hpHMaY5IKuBL0WpKrpyBaiqXutcxItDwRKJK--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcJJ-nMejfzABQab6mP0SINS65kcvCDCMWc0OM6CxUDPJH38kMrhp0BTFpFt2p7GdkPU-TT23U5DqJUBUVbr-hxX2eeqWCU5-aiMAhiAWzPGjDkcB1r45JXwiTPM9Y8CC1bF7GuY4hLPMZ2mm_yXgiR0UJpVajTFuI4RH3_dpTsgMo63uGJBjYFdrp5jn44wMb56VyxI3uXl0xv08hfoHAq2jEHyqBTFTNu2FtdmDE37QwBf102I-tr2mZtfImNdIKjWxEeQ49-pJ48ZYW-lvh60d9fnyEJrETEDtXSgxEO6L3O7wIvLLqWGUKD9yPnxP-idup4F_G5Ia2ceS7-gLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JimeD72S5TC2ty8R6D0hicdKCBN6UaZE4rh6XyfhZWzbkKankEQt3uRqD39iArjo74zLThgQtxylmQXZ2OUGcBLTK6_yvyt1DM20ZpBjZguqw8dvMDSLZSyCY5HYvRk2lumkW7OcfafQ2Vir-kA14Q-r1vjlh3UGfIv4IWzF9rq9XovjTQnGL69Fk_hCIuKRraPvZvIVX5cxTpLkleVtsMbMGI2n2AlevekDVaa6M_3QcKjIgZeDeuCZRI13LkvQhlCZBXeLT93tejtNdNkvuQ3Cdbg37PAkUiRjj7A2ZSXQtgv1MGOMw91kh77IbdOkdAH5aD1WRTvtCkY9jn40nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqMPsL_z5b-N44RSfH1fMG87MB4L5OMGWYDdtzzZs7k4zCs4-wxvfDSlPDekAOrNeaC9A0qbT0Naea4tDcok2dkMHnVi8krN1LyQlgn-krW96E0B9DdZ8S6bF2yqzlHV6cwITYydv9M93Poc0r75rJGWQfPJY32Z4wYrHArEl6m8xjmV9wJYkATt1quwC70ObJm2LizYz2hH7Not2N8aPMk_QLzOcaajXi6SBPMwQQNW7Xm2U7biyhCvKn-pZmubtEXHKHSCBkNZMbV-DXSSAVSC6l0UnsCiRVgRW1BJe8oTlQ6l0N_LTywdc2twbsWqV_DG2QWwy6viLoC8ISFOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ok9bYGFpGh6A1ZgnDR_plmQ6013iDeDfTWbDZWsFgA_PGDq80j_2QZCsKX1qnakRxYxzHhuAvj5kQaDSG1YzBPrv_VDby4ysikpF_aNy7zhfXlq8docpVA-ZoYxuC3PwA7v7FR_5A8JJngEYgnG7bu3-3ClH_Xyg5xfc7t6M6nwrc57NJkas38dlS2yC1LJXZ6Mkh3CRx4FUgvA5zAxdRiImYq4tVmgeaR1UQw0W8zhJ6DYugkGHvRWyr1sh-HWRFjDIQ1W1gaDrYddOLYlYqtf1rKY0v0XtvKuGt17q9TicJEzeUAUiG0_Lz4qt8759WracJQyqW04KJkxiYmdHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICNno4-ahuKGqs6V1Y-FyISchJlhdmVIDgaYlcfV6C0l9TY2ARrFrnhbng4KROH4Jzcj9IP_3JQO0Fq-0BLp2BNSSHskCFFTtL8qOAzskmFTRA5Kggsa6PLDhbbFJBnIvOKM00TnLcMu2e26jsO6YNkNgN3yTe9RMc7RFLmA7F6EK2erqGFgMlrKFOE8s0rVM4bt88Kol4GgHlikKl8I33BhtuYw_6QHQGenZB8fAujSrdxZC0HQhW2O5uVKfyyz7SCvUbLcFLAxzkqTzq7vFY2mX1qcpMPl6XXCXAlrnxvhRdw59soPjyv9dwQ-ZebpNqF3k3Nvv-dU6RIJZlK_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCurU5VUszhG20PqQDxt4NBVfKJ1BYAWhNkQnnthABA2if-WErZj-kYaIQSJM6cKTY6WPkIwGP2ydj0Npnk5gExZVMmxikM673tJwaj_kWEc8JGFC5CZ77ldJr6k9pLnPRXAzaZ1SAVsLxPi2G3abhzHjldGTzlMn_oXGZBZ5PhToOCQ7ZlphSJgktglRSrMTBOO0cOavgs-EYo3EJaGokoUROGwzqcjvvv0Qoxl-MfhpGYZznH5Xd14lqJuC8frWbBs987Uczohc_I-gr_RuxRexy1dCkM3FiKlYUH_HfL6zgeI2JfMkkDyovzkyAPsq2w4XZOgAqRO1POuDoIeAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اربعین آقای شهید ایران در گلزار شهدای خرم‌آباد
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457260" target="_blank">📅 21:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36452af25d.mp4?token=Hpr5S9vytvJEnptgtC2P8xbwxhAZT-ZV0lboHf-LjIuDKqs1nlwCfp-rq3nDhQrYSZh8gf-Zs0eM8ExRJEElPPmrLMLFnyVT41JZZPNONqYb0DVMw9TZYG8iIKMT476lWAWil_2Q0rwzOzI-UHxwtN4na06ErjVzQcwP2UDvxc11saPjZNdfV3l2AXUFEUVQ6CDlEam5JTOlZYt-aQR41iPXMP6p-3DqMY3OPfHUsnPds2yxM14gyMWYachyd-Mvn0jkq1lhWz5FgLLuQ_-LyTfi7JtbluEk2rRkWon0Nzrlw7MM8nJBWwP9BCdoGSvHPcBTx43SbMqZ2za9gSy_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36452af25d.mp4?token=Hpr5S9vytvJEnptgtC2P8xbwxhAZT-ZV0lboHf-LjIuDKqs1nlwCfp-rq3nDhQrYSZh8gf-Zs0eM8ExRJEElPPmrLMLFnyVT41JZZPNONqYb0DVMw9TZYG8iIKMT476lWAWil_2Q0rwzOzI-UHxwtN4na06ErjVzQcwP2UDvxc11saPjZNdfV3l2AXUFEUVQ6CDlEam5JTOlZYt-aQR41iPXMP6p-3DqMY3OPfHUsnPds2yxM14gyMWYachyd-Mvn0jkq1lhWz5FgLLuQ_-LyTfi7JtbluEk2rRkWon0Nzrlw7MM8nJBWwP9BCdoGSvHPcBTx43SbMqZ2za9gSy_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۰ روز است که رهبر شهید مهمان امام‌رضاست
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/457259" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO3SbxGPlUBtUJG-0eeYfC35eaYRY6L7ZFeYTdy9Mq1I37-DdqEXvQkbS1ps43Kl-XMyYF0EoIIbzasqnRhNxGRI0GZdJsZsnID5v3PtFfH-bRvbcxiex9_OvUxK4vdCcMD4jhOplWSmh3Hhb6X8OjHFnEV5O5wQEud6TE5svd7ceHdY_H6t-zE2TRy_1X9YmhNBJxTGRu4pUnIVA-foe5UziLQKj5wlfOqFUp6utjVPLL2_6ViCj3DU90ipjSYsG14yGH9UYqOYJ_P8bkJkPDYngVIQdeXoITC6hat05a_XWaGVUZlo7Um2wdHuvzUM6OAuA9W5Abi-jMR5dANfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش بدون قرعه‌کشی سایپا از اول شهریور
🔹
سایپا از ساعت ۱۰ صبح اول شهریور، خودروهای کوییک GX-L، کوییک S، آریا و پارس نوا را بدون قرعه‌کشی عرضه می‌کند.
🔹
متقاضیانی که در طرح‌های قبلی موفق به خرید نشده‌اند، می‌توانند از ظرفیت‌های استفاده‌نشده طرح جوانی جمعیت ثبت‌نام کنند.
🔗
ثبت‌نام:
saipa.iranecar.com
🗓
تحویل: شهریور تا آبان ۱۴۰۶
⚠️
این درحالی است که سایپا هنوز برخی خودروهای ثبت‌نامی قبلی را تحویل نداده و در بعضی موارد ۱ تا ۲ سال از موعد تحویل گذشته. متقاضیان هنگام ثبت‌نام باید این تأخیرها را در نظر داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/457258" target="_blank">📅 21:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اعمال تحریم‌های جدید آمریکا علیه ایران و حزب‌الله
🔹
وزارت خزانه‌داری آمریکا امروز از اعمال تحریم‌های جدید مرتبط با ایران، حزب‌الله، کوبا و روسیه خبر داد.
🔸
طبق این بیانیه ۳ فرد به فهرست تحریم‌ها علیه ایران و ۷ تن دیگر به فهرست تحریم‌های حزب‌الله افزوده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457257" target="_blank">📅 21:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">◾️
به‌دوش ما پرچم انتقام است
◾️
خروش ما حی علی القیام است
🔹
رجزخوانی میثم مطیعی در مراسم بزرگداشت رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457256" target="_blank">📅 21:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAdD_rHcCi6uBNkqWr3fczeVO1NH5dPbzJzGgapvhcPRKDeNy3dv4si0IEN-yP_U9jeWCJDjntK6pZc8y1dR4E6O0Mkfq1L2j-2WTwN3bNto3dMlxrMBSkyamIPLtb75GL8_mr1kdvLD-jCCgPH04-nwxNjieFTvPDMKyc5KCW0ox1RBUwLkZVb0Wzun4hNHjcnIJPwXq9_t7l5dMFyy0Bdq9GRM0BkCyayCoCJM7cdiewGD2HUOhr_45cuLKYZy8NZUkfuIyhAvI4xNuK0szxS7ZLpP_-yKVKviZwNliYYUOc28VqrTUlqPlandJm7X4E4tKb6XmQW6VqtiOYNl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تأمین برق صنایع با اولویت حفظ تولید، اشتغال و معیشت دنبال شود
🔹
رئیس‌جمهور در جلسهٔ بررسی اجرای مصوبات تأمین برق صنایع: باید به‌طور دقیق بررسی شود که چرا برخی مصوبات به‌صورت کامل اجرا نشده و چه سازوکارهایی می‌توان برای رفع موانع به‌کار گرفت.
🔹
باید به‌گونه‌ای عمل کنیم که هم چرخ تولید و صنعت کشور در حرکت باشد و هم صنعت برق و سرمایه‌گذاران این حوزه با زیان مواجه نشوند.
🔹
همهٔ بخش‌ها باید ضمن حمایت از تولید و صنعت، از تلاشگران و جهادگران صنعت برق نیز پشتیبانی کنند.
🔹
مردم باید در جریان تلاش‌ها، محدودیت‌ها و اقدامات انجام‌شده از سوی تلاشگران صنعت برق قرار گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/457254" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJa2kOLd27ETgyUpSpmo1iMtyaL4UL1wvzOfUXuQAWqMxgZRaT5Jd3idi5CDjzVQ4A8JVaorrF59DIG5i9TrgXektELGUrvZW0ow6G9IkY5VeQwXv1tNeiexfG1CKxQQPhBNp-W1n5VQJNa01a2rYEB6BoLaoBlmPeLQoCcyhB_tFw-dlzwLH1M5K6dInyrlHji2ZkNYlBr2ucP-TWRq0aybqYlK6wwUw8_QErpl22e0btiZ6yQzGu0nCzEjGeJkWCnJ_bjcq9_2vOyFEASZjR5XbDZtYctLfwOF6DUP9O50dvf28Huux5vmqTdEqyrWOX7X0xVojcVlbnje4YIoJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون از افشاگر وضعیت ناو لینکلن انتقام گرفت
🔹
یکی از مقامات آمریکایی به سی‌بی‌اس نیوز گفت که سران پنتاگون برکناریِ ناشر کهنه‌کار نشریه استارز اند استرایپس را پیش از موعد بازنشستگی‌اش بررسی کرده‌اند، چرا که دولت ترامپ در تلاش برای اصلاح رویکرد این رسانه خبریِ نظامی است.
🔸
مکس لدرر که به مدت ۱۹ سال به عنوان ناشر استارز اند استرایپس فعالیت کرده، این هفته به همکارانش تصمیم خود برای بازنشستگی در ۳۰ سپتامبر را اعلام کرد و به اختلافات اساسی با دولت ترامپ اشاره نمود. اریک اسلاوین، سردبیر نشریه نیز علناً با رسانه‌های مختلف درباره اختلافات با رهبران پنتاگون صحبت کرده است.
🔹
شان پارنل، سخنگوی اصلی پنتاگون، با انتقاد از این نشریه، در ژانویه در شبکه‌های اجتماعی از «به‌روزرسانی استارز اند استرایپس برای قرن بیست‌ویکم» سخن گفته و نوشته بود: «ما عملیات آن را مدرن‌سازی می‌کنیم، محتوای آن را از حواس‌پرتی‌های وُک (جنبش بیداری) که روحیه را تضعیف می‌کنند، دور می‌کنیم و آن را برای خدمت به نسل جدیدی از پرسنل نظامی تطبیق می‌دهیم.»
🔸
شرح کامل گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/457253" target="_blank">📅 20:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1ee013d6.mp4?token=ihkN-Nbu8Sq_XvBmwa9leamf1Rv9i78yv-yoJonkmZY_GsP79B2ZBYDaOxy70E-2XTOXjEwHKYZw5XFLn3ivk-pCu81raBBUW-jLNvTiIWUo4ITnd9ZOkW1nve4_Vclv3rJpDgdvg7uoOM7H5mudr3UNbX6ysIXWXQ1B2SJnfCRsMkZKsTb-gu1_TlB0Fjl1HhNTCNmnSDdryIeuWHp_L_8CPtXtb9kylPKM2VEHSBzddxpel4JoD1gviUPYPmSgCcNAZeFJn8GXIIGHIMwAvGuEhHFoss74nxMh3X5IxtrbV31fomhOPFqMJWqd65L8nIBiZYcUnCQ0EX90FGjjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1ee013d6.mp4?token=ihkN-Nbu8Sq_XvBmwa9leamf1Rv9i78yv-yoJonkmZY_GsP79B2ZBYDaOxy70E-2XTOXjEwHKYZw5XFLn3ivk-pCu81raBBUW-jLNvTiIWUo4ITnd9ZOkW1nve4_Vclv3rJpDgdvg7uoOM7H5mudr3UNbX6ysIXWXQ1B2SJnfCRsMkZKsTb-gu1_TlB0Fjl1HhNTCNmnSDdryIeuWHp_L_8CPtXtb9kylPKM2VEHSBzddxpel4JoD1gviUPYPmSgCcNAZeFJn8GXIIGHIMwAvGuEhHFoss74nxMh3X5IxtrbV31fomhOPFqMJWqd65L8nIBiZYcUnCQ0EX90FGjjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای شهید ایران، ای خادم شاه خراسان
🔹
مراسم بزرگداشت قائد شهید امت @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/457252" target="_blank">📅 20:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da04981558.mp4?token=m6ewfcG9mF8gVR5_lUuCKJQ1kvrvCEuGkmQsSa4XsBezYaiGxHM5qf5JXlO8rrtAKKcrfQ3epj36tKQjmpkVW5hO9Lqhbv-2eVaGeiJikic5WYTJfXx_W1FsCdrOBxdNhgkvK81i5hSKMNVokfs3VBhe41quFLsHl8ICtwOA8UtEk1vK7vdpyo9ot4Dp-8AGDQ_wh2TbMKsyEGUimNUBtRmqe9lrmT0eJy1AhCDVGs4hdMax-jnl8l5c6Mf9FZFcJCRxuhCF3b38b8DMXvZYLIBjfLb7RY7KdQxEAItJwhlsyJg0BH0-qFIiMz_mJUely6No9phMsioOmS8zO1zy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da04981558.mp4?token=m6ewfcG9mF8gVR5_lUuCKJQ1kvrvCEuGkmQsSa4XsBezYaiGxHM5qf5JXlO8rrtAKKcrfQ3epj36tKQjmpkVW5hO9Lqhbv-2eVaGeiJikic5WYTJfXx_W1FsCdrOBxdNhgkvK81i5hSKMNVokfs3VBhe41quFLsHl8ICtwOA8UtEk1vK7vdpyo9ot4Dp-8AGDQ_wh2TbMKsyEGUimNUBtRmqe9lrmT0eJy1AhCDVGs4hdMax-jnl8l5c6Mf9FZFcJCRxuhCF3b38b8DMXvZYLIBjfLb7RY7KdQxEAItJwhlsyJg0BH0-qFIiMz_mJUely6No9phMsioOmS8zO1zy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌ احساسی دختربچه معروف عکس جشن فرشته‌های بیت رهبری از رهبر شهید در برنامه محفل ستاره‌ها
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/457251" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7VaZaFgLbf2fE179lRZs26QLMW-dv1-BUhUMarjCSmN6ejpDq4ZsnLjY6O18QkXNxzWppoRTONVOCk8kCckHXrvKiIecI4o1KuOroZA5oo1E54anHddy0Tcz4kQfMm2K8br5B02wtdbwrBXZjbFy2bE6ZH71NCMVzRn0-zZliZG0GojPHyU3-2RVs0oQjbAgS91DrgQwTvd21XULjuiQRctGI2Pk56skoG3aNRrO4N6T-EQjVnTSHrP-HXKiwwRVSFEhyZVaxAkfhZOjMlxypj_906gTeN0vam4i1OrwepEZiYIKUIh1iqgfZXAAccgL8KAJ7BYgJJnmmam6p6bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستکار: آمریکا به یک نفر ویزا ندهد، تیم را اعزام نمی‌کنیم
🔹
سرمربی تیم ملی کشتی آزاد: برای حضور تیم ایران در مسابقات امیدهای جهان در لاس‌وگاس، اگر آمریکا حتی به یک کشتی‌گیر ویزا ندهد، تیم را اعزام نمی‌کنیم؛ چون ما یک تیم هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/457250" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e2d1dd4c1.mp4?token=Ds5SzTL6V_d4Gz4Lh2U2KdhMjzzcWs2LTdbt_jgdgvFVLfhJzkr80rTqai81gkaVTnUeaNb9lRZ_noQ7lImOs9o5msBTlMyUpsx9xiUHMWDdzspoiXxVkfs-k4FXODxn3BpDj0bfreOI4XjpdMblsfTUlUsmI7gRNEVOIO3PeXLLD4bsLmIvHEniEjxBosRNYrivjkRVNX8tBcE1Jaj-C4Gs_8nbok8NOk-3ftFJ9mQ6ta78NxZmQIouPcb62782Z99cAE8glFNmRAMbxJsaCn-qWlj04xGeCdw3kwZngy2WE_O9Bw3r7rocVBLjrBsOzUjlolyRoLFgUiYGlRVGFVtrguAR-FWDCGVN5KYlfN91Mr7tresP4zZduZeTykdvUT-i8M7t3nkVpTqTXTvwW_XtCaYQRgeHbV5z6NTm1JIfSd21X8m2fBokKJSIUB4YRgambfbJs0wZaEXdzNCtCSsTHg2O9__7NvLWiFZtGzcE2cCwvK98ki9BqNvzBeBsbtcz81q1KhC2Hn3X7pr3P-OuZgjz0QnHA9_XKlO3PfcxTi5MZPIgrwWrRIgMeGR_eImRi68CWu7RFeAAU7xkdHfG9VEZa0aGVry4UZrfZflgJN-eRt192WuYcIAQFATjJtoz8LiOoKRDhwcg20ZPfJseAEbLT34kEXw-sIl1aeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e2d1dd4c1.mp4?token=Ds5SzTL6V_d4Gz4Lh2U2KdhMjzzcWs2LTdbt_jgdgvFVLfhJzkr80rTqai81gkaVTnUeaNb9lRZ_noQ7lImOs9o5msBTlMyUpsx9xiUHMWDdzspoiXxVkfs-k4FXODxn3BpDj0bfreOI4XjpdMblsfTUlUsmI7gRNEVOIO3PeXLLD4bsLmIvHEniEjxBosRNYrivjkRVNX8tBcE1Jaj-C4Gs_8nbok8NOk-3ftFJ9mQ6ta78NxZmQIouPcb62782Z99cAE8glFNmRAMbxJsaCn-qWlj04xGeCdw3kwZngy2WE_O9Bw3r7rocVBLjrBsOzUjlolyRoLFgUiYGlRVGFVtrguAR-FWDCGVN5KYlfN91Mr7tresP4zZduZeTykdvUT-i8M7t3nkVpTqTXTvwW_XtCaYQRgeHbV5z6NTm1JIfSd21X8m2fBokKJSIUB4YRgambfbJs0wZaEXdzNCtCSsTHg2O9__7NvLWiFZtGzcE2cCwvK98ki9BqNvzBeBsbtcz81q1KhC2Hn3X7pr3P-OuZgjz0QnHA9_XKlO3PfcxTi5MZPIgrwWrRIgMeGR_eImRi68CWu7RFeAAU7xkdHfG9VEZa0aGVry4UZrfZflgJN-eRt192WuYcIAQFATjJtoz8LiOoKRDhwcg20ZPfJseAEbLT34kEXw-sIl1aeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور فرزندان رهبر شهید انقلاب در مراسم بزرگداشت چهلم ایشان  @Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/457249" target="_blank">📅 20:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzpx7xZXnIA5mcLhx4kXCNpnm0W6AuIaSdJYGG01aIWiS3aCNXzuS4lZ44AsyAicXR44oVuORBpOAxWry2XR9UgmguaE-_-4sln-asxDeR8Sn4IbIYRAJbILhcPTdTXaI3x_LJv1ciNwVyLjDkIxkqccbF4hIRfu3MG1M7hSUHtuc7OZaoUnB4EUg73txQgcNPYemGCVESjOtYI70t4AXmFxITUbCUbq9dqn23OFOa-dHUEH_gqh3KdP3FjiYd4z0rcDMQbBs79riB4CHUX7O10DLN7ktC_Lp1Cl3Hq04VvEOycyBVClRyDVyXknIX-WvzMplCZJB7oRkKxdfN-OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور سیدمصطفی خامنه‌ای در مراسم بزرگداشت رهبر شهید   @Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/457248" target="_blank">📅 20:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=pdyKxcTTePFVo9kUN1ywrn0d5EVlaK6IteE3OYgZMtgsVuKcotI91N7JexsZWjjhLxN6z9C13TMDfLWgQJsMXcCWTaxSGBp-NBl8KR2Idf7AKisii0mx9oO0bocYOByyqVXRMR91wI9rsY04P8grBVXTUCj2vGHNbL1VzClyHm990t_EqKI_45sXeDaXKr_v6Yz3GaxxdRpw388avanagISdwD1sLO5K0KcxcVx7g3xdbOlJqcq6r6b5VGsLqitYZ_fFsyL69dXqVIejO_5YMR2KN-tV5vh72l6BQNNJy5vmeEJEJtXPDcI_vSOX_BFVg6kIWTAubeE3ZGqKoInm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=pdyKxcTTePFVo9kUN1ywrn0d5EVlaK6IteE3OYgZMtgsVuKcotI91N7JexsZWjjhLxN6z9C13TMDfLWgQJsMXcCWTaxSGBp-NBl8KR2Idf7AKisii0mx9oO0bocYOByyqVXRMR91wI9rsY04P8grBVXTUCj2vGHNbL1VzClyHm990t_EqKI_45sXeDaXKr_v6Yz3GaxxdRpw388avanagISdwD1sLO5K0KcxcVx7g3xdbOlJqcq6r6b5VGsLqitYZ_fFsyL69dXqVIejO_5YMR2KN-tV5vh72l6BQNNJy5vmeEJEJtXPDcI_vSOX_BFVg6kIWTAubeE3ZGqKoInm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری منتشرنشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/457247" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457246">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d1470a7d.mp4?token=uQ0szn_8kQQQRImiVTxxysfjwu0socz4MRL-sXAZG6Y4WTfWAt0NCFxGQe-eMNV8mrHVLkso1xs9UaIOiqkEBaMXEBmkQrY1jFn3_fvVwdzA9luJXP1gUVZzYy4rvqKOtfzGlEyH5KgGjkVVoOgJn2P4hcb-Fc-Dvu3h0nOJfGZFHaDNOmk4DAqfsQ4xPo8WaU6cE4n13F1O_1Tt6hxHn6WVWmVbjhPzK1qz9MlxcRCTNxdPXf2tpOl5rAEpvPkivTbAFmWt5OfmAE0UerDZ7OCr_IM4QZ93-jWgLOfpn6CjxecxJ09S8jrATrtfqU1vsIRfPVPRw4g9PNg2enImxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d1470a7d.mp4?token=uQ0szn_8kQQQRImiVTxxysfjwu0socz4MRL-sXAZG6Y4WTfWAt0NCFxGQe-eMNV8mrHVLkso1xs9UaIOiqkEBaMXEBmkQrY1jFn3_fvVwdzA9luJXP1gUVZzYy4rvqKOtfzGlEyH5KgGjkVVoOgJn2P4hcb-Fc-Dvu3h0nOJfGZFHaDNOmk4DAqfsQ4xPo8WaU6cE4n13F1O_1Tt6hxHn6WVWmVbjhPzK1qz9MlxcRCTNxdPXf2tpOl5rAEpvPkivTbAFmWt5OfmAE0UerDZ7OCr_IM4QZ93-jWgLOfpn6CjxecxJ09S8jrATrtfqU1vsIRfPVPRw4g9PNg2enImxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سیدمصطفی خامنه‌ای در مراسم بزرگداشت رهبر شهید   @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/457246" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457245">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fddb63e3.mp4?token=dxPM14Ace_ZrUNMG2gsJ9JMnM9MP2aeHrtrA1F82Ik1YJiDnfXZ5wcnt5YihPo5vnRcQkQJjBKeeB0Ox024J7nbs-TI7afDXjcO4bU6lpRvhbfgsr5iYwromqozxHLG6hDl1wb_Z6zB8mfWHgGEQrr6zfPhnUEm3eLfJGwFhNfTjU9OlMhRXvfxAymR5HsVGP-lT6uF4p9gEy_-kvpigpIUbPvHfTejjMryc-530Ki7c0pPcxKwNYIWJotScjODGFyIcysM1qC37Zpix-YANQnKJTJDnwwNRIR0kNo-6BdRuhyXMNmKUc9D0nzVbs-3JYVsEh5I5ROh_JU9FtDmtTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fddb63e3.mp4?token=dxPM14Ace_ZrUNMG2gsJ9JMnM9MP2aeHrtrA1F82Ik1YJiDnfXZ5wcnt5YihPo5vnRcQkQJjBKeeB0Ox024J7nbs-TI7afDXjcO4bU6lpRvhbfgsr5iYwromqozxHLG6hDl1wb_Z6zB8mfWHgGEQrr6zfPhnUEm3eLfJGwFhNfTjU9OlMhRXvfxAymR5HsVGP-lT6uF4p9gEy_-kvpigpIUbPvHfTejjMryc-530Ki7c0pPcxKwNYIWJotScjODGFyIcysM1qC37Zpix-YANQnKJTJDnwwNRIR0kNo-6BdRuhyXMNmKUc9D0nzVbs-3JYVsEh5I5ROh_JU9FtDmtTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از مزار نورانی «آقای شهید ایران» در چهلم تدفین ایشان  @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/457245" target="_blank">📅 19:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457244">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeY-pbYiuWFd6ceMGMxQ7aWmGBkQqf0Tr-FudUjHrVNtXTnxYjikRw4ZoT5QUfljffl94i0Jr6jilhsA3ubapfYpAhn3_LdEUXVK2Q5M_lCisJZ4G3vmSp0PPh4WzZUYrsN2esxVrGHB-cFWNi8YwAwNHqoP3I7JBZz84DwMuzO35O6srnNA3oPRuS4vi6bCwAHRTjC8QjniN_68nYCXCJXqXoSOwNWdhvp1lFmvxJ-opZSKEjy8E9R3NUb95tfeUR3wK6DuikqAPrhZmMwHA0zPi4Hzcey7U7cO_lW2PxnlVWew2qanzu-qoXyGAz2FdwJi9a8bSTN06X8WPNlrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رطوبت هوای بوشهر به ۱۰۰ درصد رسید
🔹
بنابر اعلام هواشناسی بوشهر دمای هوا در ۴ شهرستان دیّر، تنگستان، دشتستان و دشتی به ۵۰ درجه سانتی‌گراد رسید؛ هم‌زمان رطوبت و شرجی هوا در شهرهای ساحلی این استان تا ۱۰۰ درصد افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/457244" target="_blank">📅 19:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457243">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD9QDWshNz2DMnA3cJPI_749zPUIAnVybNz6mevOpL6wSDiq3ugHS-Pfl8mDlrDGdXL0Jfi1yx9_8rKane98MLavjtHPX2kDD5HAXFkFliIgLnVb6PlOUVeLM63YZ4vbD2bne9_aSP9P4T9JF8-zfj5fNOPJt35uxfKgqb5N-btoyCzfH_mWW5NeZFsBS3Bp7BA3Yzr91SJlJ7Xz7zFbancLUPDHb_Ex50LgM7lw5ruktq_dqlLOhkyc9W-a2PFeg_ZAH54LB2qm4NA41pnJBVV22WaFQ5V6qN9Arqh6zTNs6f8cQrsN9AcwagklZ7PN0fyKU0214rMcUtcJ1nhdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حال‌وهوای حرم رضوی پیش‌از آغاز مراسم بزرگداشت چهلم تدفین رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/457243" target="_blank">📅 19:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457242">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۳.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/457242" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۲.pdf</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457242" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457241">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470cf5fd23.mp4?token=uBmth7wSvuXp05kSoT16-KbnpsTQMi2_D1SkQCQl5d2w8-5IjGHv7v4f1k0JP7-2Cu8LiD01sjPpuEB_dETTuDfdO4P-WXTxqc2ZIxenRxtKElOOH3GJFAPj8dg2MkgzjQZKUydCPXuUIRyxQnXnx8Ms4fnk8-0ZwiIKLYe12WHOhaVVEw4PIOWq-wZycTzb4fR5obHVu7jiIG0OrOnFHOwUXSRb1L0RdhY_nPvVgluJgZHGJmE011U63UQr3WdsPNFLvoFAcZqOjUX_WHKOjWHsUfw_C6phV1LhvPgcU48wNKA471DmOh5aDlJE28o9lBvJ4Cxh1ccxu8JMRh5xcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470cf5fd23.mp4?token=uBmth7wSvuXp05kSoT16-KbnpsTQMi2_D1SkQCQl5d2w8-5IjGHv7v4f1k0JP7-2Cu8LiD01sjPpuEB_dETTuDfdO4P-WXTxqc2ZIxenRxtKElOOH3GJFAPj8dg2MkgzjQZKUydCPXuUIRyxQnXnx8Ms4fnk8-0ZwiIKLYe12WHOhaVVEw4PIOWq-wZycTzb4fR5obHVu7jiIG0OrOnFHOwUXSRb1L0RdhY_nPvVgluJgZHGJmE011U63UQr3WdsPNFLvoFAcZqOjUX_WHKOjWHsUfw_C6phV1LhvPgcU48wNKA471DmOh5aDlJE28o9lBvJ4Cxh1ccxu8JMRh5xcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم رضوی پیش‌از آغاز مراسم بزرگداشت چهلم تدفین رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/457241" target="_blank">📅 19:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457240">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادامهٔ تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
به‌گزارش الجزیره به نقل از رسانه‌های محلی، اسرائیل منطقه الطیری در شهرستان بنت جبیل لبنان را بمباران کرده است.
🔸
ساعاتی پیش روستای المنصوری در شهرستان صور نیز هدف حملات توپخانه‌ای رژیم صهیونیستی قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/457240" target="_blank">📅 19:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457239">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7846e72a4c.mp4?token=o4ppe74WTVu8sTubd13_ZEvXK4830-RPwK1DcPCDa8-SsjxJITQ7b_Ep7tppKgM--B6O7Ul750m8xGtvOAHiGXdN-8_rI5OcNwG4W5ewj82T_3JP193ZlTXCLyKp1WPWbVkfX5zf3aWEEuLJdYCOvD3JAi8Gcfi3EPA39Q6BZ-j-Yt5DzFyS39ufph4tyWWf-0nnLzTc7L3sX2FMJFUncrKBFo5R0yGfNZWfsiljRwKPj9rRjl5AiqUh-I15K29xD3EMIzjrsTuhsXnlQ6PRp4-wRY8GvVRqV6c6eMCabuowACI5AlVu3x4SrNy0hScfs4i7cfXMoJqvzHS7JoJShTAcSApHtnorGEhJwY8djkuq3nIs2rGV_eKxhAfKqfhWAqgjHH_rOJ-i2w1LD_d1aWfTZIcqQVglME1F6IBMsI_TZ0oqpjGYZBWepOKGvIacWbxxS-zBdwgQ99kkDRdyLHXJTtY_jAG24fq059dP_ldReuBM5QKK0g77z47Bw1PxKWWOsJu1D6W-UwXoUU5DyELHt7XK7aYi7oTllEZvDShX3wGk_jC1rGXz24H7GLoS7EWK_d-XNm7urNBrjjU2OSuLcTuy6D82HY0sKaXdYHIM7dn9Dhk49mc82GZwT3KveEYWGUFAbgQkoc43nkBXe0yMULxDWZcSPnKMM2_83Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7846e72a4c.mp4?token=o4ppe74WTVu8sTubd13_ZEvXK4830-RPwK1DcPCDa8-SsjxJITQ7b_Ep7tppKgM--B6O7Ul750m8xGtvOAHiGXdN-8_rI5OcNwG4W5ewj82T_3JP193ZlTXCLyKp1WPWbVkfX5zf3aWEEuLJdYCOvD3JAi8Gcfi3EPA39Q6BZ-j-Yt5DzFyS39ufph4tyWWf-0nnLzTc7L3sX2FMJFUncrKBFo5R0yGfNZWfsiljRwKPj9rRjl5AiqUh-I15K29xD3EMIzjrsTuhsXnlQ6PRp4-wRY8GvVRqV6c6eMCabuowACI5AlVu3x4SrNy0hScfs4i7cfXMoJqvzHS7JoJShTAcSApHtnorGEhJwY8djkuq3nIs2rGV_eKxhAfKqfhWAqgjHH_rOJ-i2w1LD_d1aWfTZIcqQVglME1F6IBMsI_TZ0oqpjGYZBWepOKGvIacWbxxS-zBdwgQ99kkDRdyLHXJTtY_jAG24fq059dP_ldReuBM5QKK0g77z47Bw1PxKWWOsJu1D6W-UwXoUU5DyELHt7XK7aYi7oTllEZvDShX3wGk_jC1rGXz24H7GLoS7EWK_d-XNm7urNBrjjU2OSuLcTuy6D82HY0sKaXdYHIM7dn9Dhk49mc82GZwT3KveEYWGUFAbgQkoc43nkBXe0yMULxDWZcSPnKMM2_83Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور داماد رهبر شهید و پدر زهرای شهید ۱۴ ماهه در رواق دارالذکر  @Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/457239" target="_blank">📅 19:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457238">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c3a1416d.mp4?token=uSNi9lvDkUvWK3ogW3Wo05Bf5uVQGyQexvmF9fyVgQYhrcuezu8e9xf2lhHVtWcd5VttoMNa_gQyArSNuYj13Q_-RqAjE5-DUiV-CbUDXArfbdliwfbgxxoM-1VMpewLI8VrpFTTDUPQvtIsBrsm0KO0cKH0jeAEkZm4ZBuon0KOXE-JOO9v8S4Oxqcl2PZsq9f51uuj9YcKnHr2oDBna3qJyKlVRpFFwSdfN_oRZ6ofKBtWbOzBwgj8X0OEezYd3QgzH1-DAaBWcqDz57EdG3mMmkYZbn2nT-xaATxU_1rX5moD8LRUXDqHIlt4nnJBCaU5MR1fIRU-VFfMElQARw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c3a1416d.mp4?token=uSNi9lvDkUvWK3ogW3Wo05Bf5uVQGyQexvmF9fyVgQYhrcuezu8e9xf2lhHVtWcd5VttoMNa_gQyArSNuYj13Q_-RqAjE5-DUiV-CbUDXArfbdliwfbgxxoM-1VMpewLI8VrpFTTDUPQvtIsBrsm0KO0cKH0jeAEkZm4ZBuon0KOXE-JOO9v8S4Oxqcl2PZsq9f51uuj9YcKnHr2oDBna3qJyKlVRpFFwSdfN_oRZ6ofKBtWbOzBwgj8X0OEezYd3QgzH1-DAaBWcqDz57EdG3mMmkYZbn2nT-xaATxU_1rX5moD8LRUXDqHIlt4nnJBCaU5MR1fIRU-VFfMElQARw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنجشنبه ۲۹ مرداد، بعد از نماز مغرب و عشا
🔹
مشهد - حرم مطهر امام رضا(ع)</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/457238" target="_blank">📅 19:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCuFBbgogIWPYMuTchCiLiBG2JxFFUMYzozx6fmGMCOroaa_79fW-5V12eG1rPE66Q-s18sg0kuyLF4WRgyatngAZAzC3t31YhHzTgOxC2-_qyAopRotzvVO-7dtSFudsyRLKdpqpfeTtDq7Ge1KvTPXzg0V-61pEA5Z0gvLJBp1jlVXd9BY7tOYDvsAZlsgoPUyhT-p2hOVGt1ap_pRTOnJGZjAsjgmwiZGG50iZBGpjFoU3q_evz4P6HTcc03F9N-TJ7GbUtQ1BWFtjaA5C-t5IB31qx3FhaiSyQt2L7ZYThwxyEZxHvijcbRvhz_PLNQlwJtMgROjAaokIBeHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cp76NI6NHikvuRQP6JroF7nos4KZB934TGoaRbit3Hrg06let8tiGH0_OioboVRPPbToKoep9eR9Q6i8NVjRdWGtloBsYppKiE18kTxyMF0Rm8IfORDxGVo-qnqG6Rhlh2RoxBSIh_ubP0ibj786hBU57UQfbi6B5XoWDmn1sLng17rNXkrYVgEyyaG3IFJKeVLTdy88bLi1OqDWej5L3M_g92OsJRiN8Xj9D2pSkaXk3lq-j-nAdYSiQVqnzx7VzB99NJcTOXxZ7Nkhg9ud2MJulSgc_8eo8qlsnpImptanSko4I2gTdmDy-VUahim18kn_L2404YPKgMZ7OtIbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvFyemXeHAIDhw010Yl9_rCg_igLOrQ8m5tCb0LQm5Sf573kbfR06aKBVNhsew9CbjO53faSeC7uA9HjemKYnlFE8a9HVMXE13R095SXv3hlyELTk5J6X81oNG1J7mQzUeYVcggXx-Vb7AYxHWbsAzDyM3vUbeQBgMuRTAd-7e21_Z9Eh6na9GXInBuFW0OJBOo3H_yxjY8jTpwAIcO_T3wF0d5f6kZxLwOjhULynZ9NdmqsZIgNGWHRzyVfX_QMlH_Nko0GyUh-fi8_U6qoknewTRNVq5cNvvswQGtTo2CekHfRuzZO53ikMrAujeamMZveVHZct7ISEMo91MG_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v98poQbMJIlYg1znU1lxoNJVZnaig3BnPGxz1PYi0IJFGI39wd4o7jlHmUigLL7SG59XCZIib00efyab_RjjH8aN5nNtKejhxB8LZEvBZxk6d8HB5tvo9_5RJFP2Ukjq4nOkkiAAKZbYXhQ-F42qxaGph6Pu3Q2NV7d2kIJL1jF3AU9chbsojCim9111qq6afzgZhV2ThlIv5NxNZKsKSFtfSxDnmb1YbsnKE-fpzoY-OTYIBoff68B1iP6yAVx1dlKt6A1opDWsWvYko3Sf4hICXu0ZFAnSmATZ5RJWu8rZlj8RCQaGnbAOtznynQejEeYaO-lpHZ9VmYvo7VTqJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قالیباف: ایران و عراق نمی‌پذیرند پاورقی روایت دیگران باشند
🔹
رئیس‌مجلس در جمع مردم کربلا در مراسم چهلمین روز تدفین رهبر شهید انقلاب در واکنش به اقدام مشکوک رئیس‌مجلس عراق در انتشار نقشۀ خلیج فارس با نام جعلی گفت:
🔹
اینجانب در این جلسه حاضر شدم تا سلام گرم…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/457234" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=pWfVwdorb2_mqpZLyLgzvqtQLg4-OAqGBV9FFXSYyApaWx42EaN_G9UTITOMmTdveHKFM6An0JJFvs-Jc1Qtwl5kSHcd5btWiX-ZUqHTVr4MwWmWA7FfuAMy0JQYdfo84qEcx-QFzhZzRXhEsGjTgUziDoY_12g2sCP-j96jqrEzLTB6dGgA3243zCLBGkvBNZDC0Mx4Hyqum7CcvB1sU4VEcMS8KX9l_VppNClr7PMiCqpAK5oVFT4uYrZ4s4Aa68rAnIK_xN6g-QHN9cwSU9C8RqpjWNdbzzDYYHkfZiQl3IEzV4WfkdUEtPlgjqS5WyUyZF3b1kvtspiSATSkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=pWfVwdorb2_mqpZLyLgzvqtQLg4-OAqGBV9FFXSYyApaWx42EaN_G9UTITOMmTdveHKFM6An0JJFvs-Jc1Qtwl5kSHcd5btWiX-ZUqHTVr4MwWmWA7FfuAMy0JQYdfo84qEcx-QFzhZzRXhEsGjTgUziDoY_12g2sCP-j96jqrEzLTB6dGgA3243zCLBGkvBNZDC0Mx4Hyqum7CcvB1sU4VEcMS8KX9l_VppNClr7PMiCqpAK5oVFT4uYrZ4s4Aa68rAnIK_xN6g-QHN9cwSU9C8RqpjWNdbzzDYYHkfZiQl3IEzV4WfkdUEtPlgjqS5WyUyZF3b1kvtspiSATSkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قالیباف در جریان سفر به عراق با مشاور امنیت ملی این کشور دیدار و گفت‌وگو کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/457233" target="_blank">📅 18:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c9075005.mp4?token=Q6GhCFYITFQ2j10v4dubfj3T-i4kFhbLQ13MxmyimXmpDN8JaKVrB3mc5SP9TKAB7NZEpVF52nHn_bE8sFw79_7C_-NJQ6d9XAUsOaKjCVFiJ8z9qm8E---k6yvDm1P1d8F3Z9QJgIJXUEfxqb_vcz42Rq0dl8D1FoFTKAyxalJXia3wZp7TFEv47KWnTQ91v4XtDfqBGxEhVNI92-7_O71w5Y0yHn_DjQe05ernhtjERaayekp1xAcjiJV3tLRHJY4Pd-IYUyFshSM6AikKGQUoqRtAYKmMVv_53ItVyMWLMkY9PizK5YzQKMY0bXVzwXXUyW4YcGjl1L2GzVO0bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c9075005.mp4?token=Q6GhCFYITFQ2j10v4dubfj3T-i4kFhbLQ13MxmyimXmpDN8JaKVrB3mc5SP9TKAB7NZEpVF52nHn_bE8sFw79_7C_-NJQ6d9XAUsOaKjCVFiJ8z9qm8E---k6yvDm1P1d8F3Z9QJgIJXUEfxqb_vcz42Rq0dl8D1FoFTKAyxalJXia3wZp7TFEv47KWnTQ91v4XtDfqBGxEhVNI92-7_O71w5Y0yHn_DjQe05ernhtjERaayekp1xAcjiJV3tLRHJY4Pd-IYUyFshSM6AikKGQUoqRtAYKmMVv_53ItVyMWLMkY9PizK5YzQKMY0bXVzwXXUyW4YcGjl1L2GzVO0bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم اربعین تدفین رهبر شهید در کربلا با حضور قالیباف و مقامات عراق
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/457232" target="_blank">📅 18:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIOmfLd-MH8wKxZWK4O2AotMpfP_4M2ZNEvXQQGlpcDi1c4GQkMje8cpnXL3SfJ5YaKTytMwZ4wfMs9dodIZT9dzSxOJxhkVxHTo9dfiLjWHUvgxz6EIO9yB-n1TglkJvN8vMnFryxvBD6STMqK-hHhoZa-uJllPhS7Vc--zzytwPsHxj6ISFWOzXbt67UD18fWS8_RBln9QedzSamS4Ql4CBRkPb7dqUDbxCXfjryNxVdhaRzRazKUKwWtS0PY0mymb_TIFuaQvVidUFxX1VA-3ajyPDn2fkMAy147JmxxcfVj6qdgbrwaNpL1DkqRf04hy62HrACtz3AKvaNmFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ترامپ به تهدید‌هایی که برای ایران خاطره است
🔹
رئیس‌جمهور آمریکا شب گذشته فاز جدیدی از تهدید علیه ایران را با کلیدواژۀ «کوبنده‌ترین عملیات اقتصادی جهان» آغاز کرد.
🔹
ترامپ البته نمی‌داند اولین تحریم بانکی ایران، آبان ۱۳۵۸ کلید خورده، شروع تحریم‌های سنگین…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/457231" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfMs4aFSOuBsnsSR0j5jjbLd781etX5KGympaepYBtG10qgw-YteMkF4H247YHV7KEq_kVioeTkQ7cnIkI2Blg8gtS_SwqAPj8X7adnSRsqZJl3aSC4loLHuGtfo_IElLFchjqZ6O28Q-9bWVzFIBEnW1eFS4WJ5SV90d3ZtmEZCKHAuRATaiftT7rEziMdzuHAen56La2ly-QsY8gL6udeVuXQ4mj_KSPqu_D4xpziFRqZB04rn_SQ_9Wr-yvRroEb_Yz1hJ59inLYeLpOLCTaEsfL5evwxE1IFFFvUSD4rZd9JlAcH4yzg1RoILBuP9xM3W9Qd9SNECDQZkjid5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ایرانی‌ها از خوردن مرغ
معما شد
🔹
تولید گوشت مرغ از ۲۳۰ هزار تن در خرداد ۱۴۰۴ به ۱۷۴ هزار تن در خرداد امسال رسیده، این یعنی عرضه مرغ در بازار ۲۵ درصد کاهش داشته است.
🔹
با این حال ۳ روز پیش وزیر کشاورزی در نشست خبری گفت «کشور برای همیشه از واردات گوشت مرغ بی‌نیاز شده و هم‌اکنون وارد فاز صادرات در گوشت مرغ شده است.»
🔹
با وجود عدم واردات و همزمان صادرات مرغ، کمبودی در بازار نیز دیده نمی‌شود.
🔹
با حذف ارز ترجیحی و گران شدن نهاده‌ها قیمت مرغ افزایش پیدا کرد با این حال وزارت جهاد تاکنون آماری از تغییر میزان مصرف مرغ توسط خانوار بعد حذف ارز ترجیحی منتشر نکرده است.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/457230" target="_blank">📅 17:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcGB2bqINxrp0RK5BecLNCqwmCjqD36pv2KbwOwM8vR5reXcYPfFLLMIoH30mxEVs5nR3deaxNJeR_YPN5UakuA_sJpnxSVt5051iKfMQaB2cV0rNImlexmUHW1o1STTi0bq_EJSDo_662wu3dv5fvpNOBUk7l81mA_iIsWJBRFSEG1rSn6xWl_DPzRFt_Y9547jk-BGoxiRBAbeakwJSrNma8D_CdeU2889IpAbIx7X9eTSxXjbt0jWLheHsEM90yCtsurZP3x5SovDZ_Av4Zag03rgB-slyktj8-KCzM1XuYktlLP5iIXnshzi0_oZeNbh3IgQ1a136WAjh3b-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام برنامه‌های صداوسیما بیشتر دیده شدند؟
🔹
شبکه سه با «کاپیتان» و «محفل» در صدر پربازدیدترین برنامه‌های تلویزیونی در تلوبیون/ کاپیتان با ۶.۷۶ میلیون بازدید رتبه اول و محفل با ۶.۰۶ میلیون بازدید رتبه دوم را به خود اختصاص داده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/457229" target="_blank">📅 17:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">🎉
۶۶ سال همراه مردم، از گذشته تا همیشه
🏦
شصت ‌و ششمین سالگرد تأسیس بانک رفاه کارگران را گرامی می‌داریم.
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/457228" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/457227" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عملیات پهپادی یمن در عمق خاک عربستان
سخنگوی ​نیروهای مسلح یمن: در پاسخ به نقض حریم هوایی استان صعده توسط پهپادهای سعودی، ۲ عملیات پهپادی موفق انجام دادیم:
🔸
۱. حمله یک مرکز حساس در فرودگاه نجران
🔸
۲. حمله به تأسیسات آرامکو در نجران
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/457226" target="_blank">📅 17:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت دفاع: تجهیزات ساخت صنایع دفاع ایران بلای جان دشمنان شد
🔹
بیانیۀ وزارت دفاع به‌مناسبت ۳۱ مرداد روز صنعت دفاعی: جنگ نشان داد هرگاه دشمن ارادۀ ملت ایران را برای دفاع از خود هدف قرار دهد، با ملتی روبه‌رو خواهد شد که نه‌تنها در میدان دفاع و مقاومت ایستادگی می‌کند، بلکه با تکیه بر توان خود، از دل هر تهدید، قدرتی تازه برای ساختن و پیشرفت می‌آفریند.
🔹
جنگ‌های تحمیلی دوم و سوم میدان واقعی آزمون توانمندی‌های دفاعی کشور بود.
🔹
آنچه طی سال‌ها با دانش و مجاهدت متخصصان ایرانی در صنعت دفاعی ساخته و توسعه یافته بود، در میدان به کار آمد و در کنار ظرفیت‌های عملیاتی نیروهای مسلح و ملت ایران، بخش مهمی از محاسبات و اهداف دشمن را با شکست مواجه کرد و آنها را متحیر ساخت.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457225" target="_blank">📅 17:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dt0Lij65J9J63dBYkTUInUpU7t2FE61d9u2zJLJeu60jQUzyu2rgnnMDsYP6Ofk0NsOGVdpyOLjHwKMK8tbq7Eb8jdtjyaL-FYAQ8oh03gtw1aJ5JefTFuov94m-p0_nPr37gN7q56PUBXIqRWP6IE2BbAISB2K6IH3lLW4Vzmc4Yje5xY-MfuVIjr29du1dmjfWHG3nPx2D3JK3zQUtu6xuTUVLOZSPCHeZwSl6xbJ5F8nD_4UJcBNKYNQjMCBIN7553YehoYb_oqOosX0lpPrOh2jBn2IeJQU8jqyTpEj518xeT6VlI2GTXObAtcwQDDI6eHESa-oOLf0rFI8T2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSDZbRaA5Egnc9-9ZPv4TjMMl1N38bi0wpGg10J_cswB5UfmQwZRYFNkgqB5NISi_W_DisH4EbvPy9QEnIh5pXGHt9REWnf4TedJ6kVhHFX15YHNkIfTV-fXsy082wA6n2tfLMFSd8_SGro2iem9HlIWJdHu0jDHRk_3gmSOj5UVN_UG9d8ZtNtYhQ66CtAvAbgYvfNcqCc9XvwXbw2x24QA_DdRN9Z2-VspBhJ7iXHxFvE60J41q2VtPafP5E0Xa-gwzB55LaaGm98KqgYQhhm_iW9ds-8nCE10RdEJ2rM6UT1dBqGPmIMYEgJZNyG0LIHKUMsW9L_PchQTRSnhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUrznu0lBCxHF2oMoscbWU8_wwIBMbhLGkaFbBjU6FxVv7rcSMRRZzbZwjth0bbxD-92a_xdP8TUWLzv9mHy0RDIlTwiPG8W0no7PzgOALrtzmrKIqdcw74MvZvG8ImeeXWfKByFt1DWI1ujQCXipK5oBSClcgSEnxffLIeKagOfRAnw3xO1lDRndaJgUdWzlRvpgFeD_MeDcBjzFcf1xcw-pAcCb6EswCIeVjeeujj7lLj2nn2VRUaONNGPt43JzIsrg8MiNTTETqKPzzAGNxNbNr9rMebXz_iiBhdeB8HDc4sHNHwVoHOYNlTkPmzAdQg6WWStFf3kVB8VCxy4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJwYtgcSYHRvXH9u31tPfUpk3XFXVdHMRJ3vb6tV99lJBrJctEpygaRaIIy2ZPVeMVu0tWndK7tgy03MaowUVnlqp6ymaaJK3VeAGKbmnFrRyS6rqF9POzlJ2-DfZbYKoB3iiZHajmIENvSTcpgDlPd4LZqH_jzbAU7SgBsUPXsOMYOKlr8WTmfKy5IMUB68rUnzgk0-grrtLjTZotH-W0ELdIDGWD-O4RwJqCPd-WhLQY1xDge8GNadrqNArn4Mi2rKiU7Fa12co1EYsJvpMgAoZYbTorKYmvPcU5vHwmZZB8tAKnEGpqy1nMzlmzCNXBiDUsiiiMJ3DL1W-B4cVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dKOfQqg-3G9CIy14_KGXMSix3OACujhFvRfevKznKyjjy7VfZbsggijQY3IPEKmJIWodu8E0YZuQFUux9Wu12VCO8N6rZ9P1Elb4-OCRI5IiR9rNUyVwJTXmI8IAuBQJiTtn4FNFmYX8gqfB4GZ5xeVBVdKQpjHLDG5X6ZXW7J0vVCZMcKlC0r4yvFurfpSD2oe7Wo6WcpCbOt2oysbPYHRRTDunpMjlSO6Fy3fKwibMojLDlvy2yG9-SXoFiuXW510zupUqYih20CQ8RsbS-2TI4Ag29BsT6KZweLeDGmdfGa8utKtqhNhCd3Rt6f3KVL9L_7v1X3HYyeO-KlHjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIjs7yiCv93F3H7ZYFOA9YJII7iQFrRHqB5_yDFQPQGfNgTB4ouD1kmZLC1llVdTOXCIMH1Dd4Mfin3MBv-5VFSy8IsAaELktAlLg6_mm3jVFQaiDvI9O7GoQ-Bcx2Z9PEXsCL_HK1jB9xOh0x9rHwiuT5Szm3BuS4Xytsal5G-aQp1AavOJ6r2nVLSP53__zAtpdBcW2vj_I-RFFFaM-lwYVjfxcreTOX6zoV7OAuT6RR0KR07dJktRJHNh5M1yIs4FcRgS8UwsOMlkEYcstgLyKLjjxxONTwuVmSkkr-Fm5W3JKCw4eJMSDWirqpBp0CTCwur1sfkaRUCDAoPUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ssg97nm7fsnyZ9ciTkWPAS_BiKc9w4_cO8gM66tDC039mFoJpVEMvinBAPAcznF40chwTBmtRWXwNg8UACxsfvqm1_wu_M2v9WISLkTzQX7LJ_DGGEXogiE2CVdzudLmyVfw74gaAsdzdQ1kWmgkiJt-nKP0PIgVEuNnzXx46TcZRRqv9_WKxcetMtXVRsr9njcbMzNmNmZNDAFyiXjcn3mxAS7U3YbIMahO2aBRnbzPsbrFHWKXjrtfQ15rFIx9R3jnQxqkfykoevgL3HR4nXPV-NFlk_CmV8gwGGVHeFjJdsROdaDVwzJiwcp2YxfvXwLlJ6xx0cJr4oeVJ8b1iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاراتنیس روی میز قهرمانی کشور
🔹
مسابقات قهرمانی کشور پاراتنیس روی میز توان‌یابان ذهنی در بخش مردان با معرفی و تقدیر از نفرات برتر به پایان رسید.
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/457218" target="_blank">📅 17:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjQD2UYVJj2xokEaYtqgs3rNrx5Tb5kHoxjvO_F5jahUDI-xfZyb4-AZ5z4-M0Thp5BvzgCb6H44BkjgGVT8OxhiuOpVVGoDQtdUPtextK8y7CwQ1oK0sC7ApBprSuUHCIe4mb1fb2xG3qkPnE5FgUiaA2mb6DVTsKgsmNtpm1ZPOFC_Lt-OASVYSDxXHfHZ6I3R5YQRJwoA6n0fJOTJS1Bvaue2vrgwDIHTk3B6PuHzq-z4iwX6iiMmuJfJtheiFZc6Xe2-yGmUQhoLeBvGPjVqYlPEhAj0e26LupZbjz3i7QveodUFaastqXEojplDB9okcPR0hwkCRZXy6tJcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ مشترک مصر، قطر و ترکیه علیه اسرائیل
🔹
مصر، قطر و ترکیه در بیانیه‌ای مشترک، حملات اخیر رژیم صهیونیستی در نوار غزه را به‌شدت محکوم کرده و از نقض مستمر آتش‌بس در این باریکه ابراز نگرانی کردند.
🔹
وزارت بهداشت فلسطین امروز اعلام کرد در شبانه‌روز گذشته ۱۰ نفر شهید و ۲۵ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457217" target="_blank">📅 16:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
همتی: ۷۵ همت از اموال بانک ایران‌زمین به نفع بانک مرکزی مصادره شد
🔹
این بانک ۱۱۴ همت اضافه‌برداشت داشت که با کمک قوه‌قضائیه با آن برخورد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/457216" target="_blank">📅 16:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYRb4swhEW1pExai0tYYxs9v1tBMq_JjXDK3OM6t7pkh9zlTVZy4oy6oKpWkUzAuHlxwYxcNYMuzJH4KxhRE7btQks5qCmUy_Tykm8mxXdsTZk-u4Q_5cwM2_UWvyZ9NPQLihuHEWmjp_cvqunThnjKDvxnn9bY0YMnir06GQprPcTmOyIjyyRCiEDmsbXWAjg0tyeQtxjrTkrIrra5oRv69oRskX_mcdEpWsQ70qQb1MMENusGGSWfyI5bqmFbLnD-v_ioZGocrRVVPVvYmcLq1l63L5zzH4g0VaDAIRmhnVfHbcmwzscruwNrNEC79E8ghdMHwT3PnoPBaAKS4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی ۲۱۱ تیمی به‌خاطر اسرائیل
🔹
نشریۀ اتلتیک از طرح محرمانۀ اینفانتینو برای «جام جهانی زیر ۱۵ سال» با ۲۱۱ کشور یعنی تمام اعضای فیفا پرده برداشت.
🔹
رئیس فیفا در این طرح قصد داشت بازی افتتاحیه را میان دو تیم فلسطین و اسرائیل برگزار کند که مورد قبول بسیاری از اعضای فیفا قرار نگرفت.
🔹
این طرح هرچند در ظاهر منابع مالی خوبی برای ۲۱۱ عضو فیفا داشت اما در پشت‌پرده به‌دنبال عادی‌سازی روابط فلسطین و اسرائیل بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457215" target="_blank">📅 16:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133c6b21d3.mp4?token=Bpo4aEQHYJzbwtZnUZ7AKlTOwTKddTrAkxRXelWmJPQBILG0FkLJVTI1wu-EKwW8xIuH_krW6BlWF9FELdFATfqPQJJwaabkvRuwGXm8E5OV-jfALyQcmzGaR0AlfNTwAnLgZuxEwwUbe9bGGbcipKDkU-GNR7QCNfaPCaZq5UgWifd2-8mVMoHbBd6MJ2ABC7S_2fDmP7nEwtMxUDgllisPe-IgIjPX1RM1e50KNRjMqYyvxtQn4iqXGF-sXddTji8gz8bGleWbbKtPClbMMdEuF0ucu9PDRctswAh4uvhPgs2Ru_TDqOSAB6Yifq5OBC11TwqfeYmPpkTyrpgCSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133c6b21d3.mp4?token=Bpo4aEQHYJzbwtZnUZ7AKlTOwTKddTrAkxRXelWmJPQBILG0FkLJVTI1wu-EKwW8xIuH_krW6BlWF9FELdFATfqPQJJwaabkvRuwGXm8E5OV-jfALyQcmzGaR0AlfNTwAnLgZuxEwwUbe9bGGbcipKDkU-GNR7QCNfaPCaZq5UgWifd2-8mVMoHbBd6MJ2ABC7S_2fDmP7nEwtMxUDgllisPe-IgIjPX1RM1e50KNRjMqYyvxtQn4iqXGF-sXddTji8gz8bGleWbbKtPClbMMdEuF0ucu9PDRctswAh4uvhPgs2Ru_TDqOSAB6Yifq5OBC11TwqfeYmPpkTyrpgCSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرودگاه بن‌گوریون تعطیل شد
🔹
اعتصاب کارکنان، فرودگاه بن‌گوریون را تعطیل و ۱۰۰ هزار مسافر را سرگردان کرد.
🔹
وزیر رژیم صهیونیستی کارگران را به گروگان‌گیری متهم کرد و خواستار مجازات آن‌ها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457214" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5RqprwS6DZOj-MoXhIhgquO0QSINk3XJ09XkrJl_xnO13FeoURkSOgnDkMJCWBxvRkm4PjcD6R1SZDBNh_dxh-QwZ9TuxzV1eKn-Vl8nyeiS3cFvAXSzA3OMrZCTrDZoT42OPlHN8SJ_YE6p6RwfyOvZEMmK62UEKqH-Nnx3I2PnOhGTmx3Vn07P4oDEwEF9D70qujYb6hAoCOSsTLs1pnOzXNWPTshaWL4-qfIiuCihJ0BN8vgkPHAq6hjZoByVE5xGP5oE0nEKpQ1zsem5KMv_lAW4yfvmgAm5ULKn8CqjWsfWSZRmJ9e41tXUwxIziaPgLGeMHbUTw7mNtydLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.   @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/457213" target="_blank">📅 15:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13f937c0a.mp4?token=De2YVJvKxDjtvLoZU4mBGaPaYkmmiAkfz6anjBv-OBQkAmK2GDf1v2NNfefJCL0XALUipaYLu8dci46UonzeRw8SAeIkomB9n3kWyNnSwy15xYHiBZrNHtGDFTM8x_83B-fUyEwRc_mFbkAVTXOVrg2bJ6P6Hx5Fw-kaAiEN02ipxUISecZPwlmD1vX6i0eaaAPUjbKqTW7LwwdfPgpaGTMBiNMtjX8xw6defUtXfRtgPguFgV2rExKv69JAJjJ8AWeYMnrgUh0fAuk0hzMgcY1IqR2k9V-FQAcsux5i2IXOL_SSyInHko5bFEvNrn2sDhToBtRWwS7oT7JdeN-Egg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13f937c0a.mp4?token=De2YVJvKxDjtvLoZU4mBGaPaYkmmiAkfz6anjBv-OBQkAmK2GDf1v2NNfefJCL0XALUipaYLu8dci46UonzeRw8SAeIkomB9n3kWyNnSwy15xYHiBZrNHtGDFTM8x_83B-fUyEwRc_mFbkAVTXOVrg2bJ6P6Hx5Fw-kaAiEN02ipxUISecZPwlmD1vX6i0eaaAPUjbKqTW7LwwdfPgpaGTMBiNMtjX8xw6defUtXfRtgPguFgV2rExKv69JAJjJ8AWeYMnrgUh0fAuk0hzMgcY1IqR2k9V-FQAcsux5i2IXOL_SSyInHko5bFEvNrn2sDhToBtRWwS7oT7JdeN-Egg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس:‌ دریای خزر به اندازۀ تنگۀ هرمز اهمیت دارد  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457212" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgvOl7ddcU9WUCZKeVtKUmtsSh9tB4fjaWMxXabMU5ydAS8dySxAfcMyoY3TPP60r3OhYat_y1bGF2AdlNm8bVA7hpB-MMRjdNpo-ZQLyG1O0t0LVMmAHXabgtLb4lSpcfqfrRnjCKiGiQvVD6-sXrU2vGhha_SOmraV4HGJ2WsibmsP0O4rDEHRj8eEvO4W12Uj_0Il2DWQkZC60sgtsz2-Wr6Z7SDlilE6pfZVRgAfmatWXkVgXzQa1FZha2mK5WD77RiS_1XLA5d0VX8Oi1yy7nQtjzL1AXPjj3ND2ZKcDW_TksKZFnvFG-bkXmT_0XqDo8wrtSQthlcEnQhLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k608Y3GyrjbSQMXPKp3HkGfTi4cYKa1zPWH6bQDZaUPm16Y12UhWfSpRr15V2bdM8ckLlPnW96usHgl3aODTqKeGsolN2podDRXA1Uta8H9e8wGy1y1KqO5V29hVpK2K-e5J3GKy9UsORUIuYYt1nbyPXEr6I4CMeDsvia79AibT7iBGCjYrmLt-iItAv4GdrYwOvzMTJr83PI57bKqM9GvgMTe9Ya-9zBwLFeWn5Ey-b88_lgxuSB0_chmTZyADi4KYxIqL0pYL9-4TU3W2_oMfWpUM2xo27KJcr1vWw7mw63R6qb8NHMqbjbKmhBiD7aVyYwv1lyfetmXp_M61QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA90YPuxW_vJwNvExru_dMCkWJkRCFrRGjN4cgS2xUH8Y19kkTsmkQQvU5YcYs5TMzCr_AYjztV_hqJN9t52ogo6wkaJLrLrE0AkE42usaT-tRzCJWyIVa-_YC6msf9-_ZiRRtaUzn7fLwWdp53FYn9madmpcfElIlO-bbi_mw9KrWxACMfccvh1agMvSL1cGNncrAzHxAyKfQAo_0Q7osvSMIlNZTgUcApe2pNO4PoEWMu-xnD7KYQWoZmTLwYZnfY7AsPx2KpBkLukgtFEsT7LJtitGwrxemNLZI8AyjHwqvxgM2kkevDNZWoqTmuwhSGq-rNwd3V66OyNFxGW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gI4mZm1Be7dL71JHlX-Tc7NzSNWDa5ips8w85_HcNeDMZSwW1VfJzZW4IV0XnCZ5I3OFohru_w7QWN12kl_vC6S-8ACcJknjO6YJrimIgvFhSC9aFGtEkormaEDIY6O8-RyoEVBE9QWJZo8aBGuDG_84Qg7iYCWkqy8l9HJvoLqg47HC6cMyiP_oIlXp83Sol3KLoC9rv5FqI2qWwnbai-Ddv6yMRBRBBuQmEHwnQcYc4FBma1wFTamcmbFNicFRFNtHEkGtSAZvJF9ZURqfYGOVgWSyIwbKONbLgKQSVLntBzx9OhvhSA-04aNxMCxb0npILauaGU7LU8x6muxk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH6uM5Gf5fVIjcXUJT7fHM4DF9HR7cJVLgn4qkDG17MCXZNnWCo0ZKYv8ux19ndd3w5bOvPLmCrGR5Ibjd7nTCrLDdFk3LmCBF9qkNItY7YD9Xp6t3WP3ifbTlVfn_sv-W-ZDZ1VL1yeida9icFzB6r6CMUuir7de2TiVgxQSbcxV_PNJFSXsB4GtMDR1xQEJU6m8bUmvZnpIbDiSgV_RXD1KdDQEMQgMnymZltePh_afn6-8sFD49V9fBNtl0DiY3uM4kO-5ZIW6TnxI4bSZW_rwlApTlCjNbe0p_xZTYnqGN1jPqC2FDYCK3ZaqwL01bePyAOed9eXU3qMc0lSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQuVkYqOF9WAh2jvKcyLH86wbrM-QjMM9Q_JRFvcMJiYmMLTYq-xl8-b5D8v2a5C2CFiRqp0H336BsqsdttAdNbKEm7b9Qn-_I4jWr3liRlqlxk95abYtCtC0pecE9HW5vuCgSk0Bi-ZuQpnJLYC1Anf5O-BkXDu1KstTz5q8vjxSzgDLPxyreYQ2WroX3rMFCfmwk-oR261E7R6lEEosEaZXNTY_QaSXlJXDCOO7PIOUbFsgh-GY5Xx4oMjZys7p91ReDeIEAs_xMrbD84ODa4RaOzzBSry6urJpdZvanv49nTSLL2Nwx9WsEtgvNNRYBB5F66EEYT2rVYVX08YXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsmrnYLuDXeht360NUaJ9e5iJdQHX2OEBZmQrwNarRoTDGJh6fc2_1bKahKNKdE-zQp0k2Ptl4HD9btacPL80gKBGtUBveLp1hGlgk_n4UFNaiDvXGlpQUjm1OGYDjzbEMlp1wfGgS6e_FoBDMhzIX3qSKJdJYl7WgMT08f1MnjigZWuAdBY5iL2nSDlKqgJL2RhoZn0GuKhivZn5X4d0hVLXrZo6qnpj0hLTA95u4DfooIgxBewdDxLnePshNQ4Nd6sfioS-sgWRA_MqDl9bksxgxh82_RZvE1eW107YOgv5BHp9Mzcy06RfWkAis_viJhLKgDx0jlrowTkF87lXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رواق دارالذکر، ۴۰ روز پس از تدفین رهبر شهید
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457205" target="_blank">📅 15:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42fe88d48.mp4?token=isN2PjDopaPX9sXqqadLautMKO9ynDu8U6YZD9iY7AzP-h7jY8idPzMarfClZ2eSTkf9MIFOAT5a9_4exz0keMtNGou7yZbyz_M6A6Go1ek4FYa9KNVasnhoYHQyjkpAexDESk25NavCMfLnIUvysAZ9kDjv5Y3hHDCM8gRXEfrpNOEQ3l7tDNWxajtuB8g2r04KEgjsxYPRZrovovrlJhvbV0aidPw_8MBVuztB78fxna_QwTY8nIrF0NKtzsNysxE0IXu6mXUY-UAzQnb9hqhd7UpwFGOdzlr1c_7ltTekio_FNbvW2dQwTGMzzY2-47iiOA0yBWpQP90DunQ2IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42fe88d48.mp4?token=isN2PjDopaPX9sXqqadLautMKO9ynDu8U6YZD9iY7AzP-h7jY8idPzMarfClZ2eSTkf9MIFOAT5a9_4exz0keMtNGou7yZbyz_M6A6Go1ek4FYa9KNVasnhoYHQyjkpAexDESk25NavCMfLnIUvysAZ9kDjv5Y3hHDCM8gRXEfrpNOEQ3l7tDNWxajtuB8g2r04KEgjsxYPRZrovovrlJhvbV0aidPw_8MBVuztB78fxna_QwTY8nIrF0NKtzsNysxE0IXu6mXUY-UAzQnb9hqhd7UpwFGOdzlr1c_7ltTekio_FNbvW2dQwTGMzzY2-47iiOA0yBWpQP90DunQ2IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از خاک تا عرش
🔹
ویدیویی از مسیر پرفراز و نشیب زندگی سردار شهید علی شادمانی؛ از نخستین گام‌های کودکی تا آخرین لحظات شهادت در اتاق فرماندهی جنگ ۱۲ روزه
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/457204" target="_blank">📅 15:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1793614afa.mp4?token=XjxnGARPktwwHNMpwM9Lbqh5B_n5TWjLLarRY50dseohgZ1KE4OunqebXfFEnj43atxgAa9rOVzpJ7a-ZgY_gm4pboP5_utOg0PrqkJFUU6fWkKOsPqcM44F7QecaPhUTZDPo62haQ0rPnXYPUTksu0MJQa7pX5sbplAYN7Mflqos_g11G1YDXHJVGlPQosMNKucuOo_5lf3K3pLCErntMZBRd4RmRu0pz7xVgjflpivWJLmQNJn6p8S95nQTfCc79VrbfuzgcI_gHcC11_rUZuFXO_rw9dMcJehdY7pQm22VlStAQsN2OhJGH_Wtp6APImAXZPHnUgGHRFfYWBEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1793614afa.mp4?token=XjxnGARPktwwHNMpwM9Lbqh5B_n5TWjLLarRY50dseohgZ1KE4OunqebXfFEnj43atxgAa9rOVzpJ7a-ZgY_gm4pboP5_utOg0PrqkJFUU6fWkKOsPqcM44F7QecaPhUTZDPo62haQ0rPnXYPUTksu0MJQa7pX5sbplAYN7Mflqos_g11G1YDXHJVGlPQosMNKucuOo_5lf3K3pLCErntMZBRd4RmRu0pz7xVgjflpivWJLmQNJn6p8S95nQTfCc79VrbfuzgcI_gHcC11_rUZuFXO_rw9dMcJehdY7pQm22VlStAQsN2OhJGH_Wtp6APImAXZPHnUgGHRFfYWBEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگاهی که پس از ۱۶ سال برای نجات بیماران سرطانی روشن شد
🔹
رئیس سازمان انرژی اتمی: قرار است تا پایان برنامۀ هفتم پیشرفت کشور، ۷ مرکز سیکلوترون یا شتاب‌دهندۀ ذرات رادیواکتیو در کشور راه‌اندازی شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457203" target="_blank">📅 14:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مدیرکل فرودگاه هرمزگان: پروازهای مستقیم بندرعباس به رشت و گرگان پس از وقفۀ چندماهه مجدد از سر گرفته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457202" target="_blank">📅 14:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457201">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3e389e3f.mp4?token=fp9WGYeojoS4BGtK1oVKaLnPEar1QdcJBsgVXOIZPe4A3PF2TD7kf6HVxz03NzSXtcb-Gl1E0RPD_Z7PXns7tI1KzVjygXW_KaIBUZ6af1-L4ROmgcX5cZfz5HIUAtKU7vSokhA1qDO5dqLoVvJxdLRiitnGW2boV9QNyMtt4qEJQset7pIDFIBkrV7qQYbR_EI9cRMJgxqaApcjXrLPML3rx4eYMg6jH1J88CsPGlxKoAItJi3CgKIo-XI2cF9t6FK0BNMVK24nmtM_MCyDX7413s6B4Fzo97f0Aavb4oNVw2gvHCm0QUisTJaeFRVH7iAS_8N3v5LBILtgkXzaILOgl4WrMwxqgxdLBKv-N32g_vkk2M9vX7pG-40MJqb-mf_KMK0qwh2gVV0Pl_101ls3h4RXZIU_ZnTdO_SwgyWrfCLSBhvC_RmcwTAkVIePxiijxTFC5CfKhbZoKueG_A-GGdiZ5ay0qXIfNbboeCglILJ3p1fanWZPJo8hbToIV6ownoCacIMXNoOQkEN0V2vPODgXhkhgpvVWJSniWkqW8qOl7tpxk-9XyxBpidio1OZiUuBt9Oedb5dRfdxPab726kUqEjTwH91Zoahkka5OYS7IL_n-gG2iqvRpx83cX8zm6LdEZh9ikgsd4nXvMKmX3fEclNouJRHFf-Zd1Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3e389e3f.mp4?token=fp9WGYeojoS4BGtK1oVKaLnPEar1QdcJBsgVXOIZPe4A3PF2TD7kf6HVxz03NzSXtcb-Gl1E0RPD_Z7PXns7tI1KzVjygXW_KaIBUZ6af1-L4ROmgcX5cZfz5HIUAtKU7vSokhA1qDO5dqLoVvJxdLRiitnGW2boV9QNyMtt4qEJQset7pIDFIBkrV7qQYbR_EI9cRMJgxqaApcjXrLPML3rx4eYMg6jH1J88CsPGlxKoAItJi3CgKIo-XI2cF9t6FK0BNMVK24nmtM_MCyDX7413s6B4Fzo97f0Aavb4oNVw2gvHCm0QUisTJaeFRVH7iAS_8N3v5LBILtgkXzaILOgl4WrMwxqgxdLBKv-N32g_vkk2M9vX7pG-40MJqb-mf_KMK0qwh2gVV0Pl_101ls3h4RXZIU_ZnTdO_SwgyWrfCLSBhvC_RmcwTAkVIePxiijxTFC5CfKhbZoKueG_A-GGdiZ5ay0qXIfNbboeCglILJ3p1fanWZPJo8hbToIV6ownoCacIMXNoOQkEN0V2vPODgXhkhgpvVWJSniWkqW8qOl7tpxk-9XyxBpidio1OZiUuBt9Oedb5dRfdxPab726kUqEjTwH91Zoahkka5OYS7IL_n-gG2iqvRpx83cX8zm6LdEZh9ikgsd4nXvMKmX3fEclNouJRHFf-Zd1Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آزمون سراسری در دانشگاه امام صادق(ع)  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457201" target="_blank">📅 14:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkigA8J0yAnL6tfUbeSRuwvk3SPckVVejGjHUzEIPpCNtVNdlpm3nlq1TSP6tVhT11kdzfHTki-COroa7hBGgtIQ0dkdtT1k1lOLvqKoPmCIzynrkyplYORnHqumWgGCAzvF2XLtDenzfyjv0GJRj8HlvvilxpAUtah-lkqiNrXi5NtqrhMJv_ElOTMO6cUKvlR-u1__zHp-pq9De9_1HwoSPmGA_kgYpEoTARuNlLvqSknTTGaNiSL7lFQRCa-2TOYOwBkFylwpW5tq9bd_OYsVg2eFDmKtuOhXzMUZ9bMeZHVV5-83fv5n8jPArrEJl_Co_Bu_7co_BJPG3obmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رایزن فرهنگی ایران از فرانسه؛ وقتی «مهد آزادی» تاب اقدامات فرهنگی ایران را ندارد
دولت فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی ایران، را از این کشور اخراج کرد.
شادمهری در دوران مسئولیت خود، با برگزاری رویدادهای هنری و نمایش‌های ایرانی و اسلامی، تلاش کرد تصویری واقعی از ایران ارائه دهد و در برابر روایت‌ها و اقدامات مغرضانه علیه کشور، روایتی متفاوت و مبتنی بر واقعیت ارائه کند.
نیلوفر شادمهری پیش از این با کتاب «خاطرات سفیر» شناخته شده بود؛ کتابی با مضمون روایت تجربه یک زن مسلمان ایرانی در فرانسه که مورد توجه رهبر انقلاب قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457200" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457199">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
📊
عملکرد هشت ماهه منتهی به ۳۱ تیرماه ۱۴۰۵ بانک سرمایه در یک نگاه
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/457199" target="_blank">📅 14:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457198">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/457198" target="_blank">📅 14:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341e45a744.mp4?token=EdsaX_i-XJClq9FL6zUcp4oePtfMWAnn24wcYH5QkEOwy3LescyGNJfy1aDYCSIgN6KFr7uFRQwrbtKQe-1gswtNixa8ck2sONZyuZTjxEcEzOqxuHJnSRK5AoI-ValMxoYT1cltExM4Z8KPAybxypbEO5JGUSnJx8np4vj4pYaagbcND6Q6h2yqE7iZm4FVJxwDHYqnqjiSN07sbnw1tjg1A0gSZ0JrBMKSXvctkhBJB3XF4_0y01jSj8udfa8LS0gKpPYFc63n4_DeGgUmfA2YW-cRYNOfmo44DtCRlpfQrTPgt_7RrlIb5NOKtw1VJwEgDymSGhYby2zHqrqLdCzITCfLPGsJXMCTGUk6DJQqYG1icr37TTpDWry_496fr57uw0dyeS7bhyjPNSkO81TvWqN0zGcIvTiALG_cK44_q16lxgWWtbFr3kfS45Gnn2O7A9Cmgel4XwFtk1lPd2-eqkqLNu9OxJ8QKzENNIKxssYoz9XeiePAbe-PFjsIRgVq_auffHI37OCeeIe1ZjMWWS4rfyQGLW1Vukir7IH4B0KUt1MEj2TLWHoNuSfwyjTuxNyvXORBbSgfbZmZYmJ3udhEj0XYhCN4XMB3y8bGPpfhx3IzkJkejLie2ux2vOckwDfXsG1Vb5yl556ZdC7cW9uvXNdjmKWz3NaJlFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای یک خواب عجیب بعد از شهادت آقا
🔹
در هرجایی به آقا توهین میکردم، اما ایشان به خوابم آمدند و...
@Fars_plus</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457197" target="_blank">📅 13:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457196">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiFyr9838XiovIzFpy1WjlaVdC4okY6yRB7W_0ehHhfPyRgSBFOwiXywazOkUk4uk3EcptsjAGG5zmLDKXvOPD3UsWBPaiOTIFdOLdt0sGcm8S7ecgppm4GfirpXEfVCAy_yflBVp1x9flXmT_yOe9s8TwKOg0GxFcjkmgcX2M9zLlG5JkMZtRlsuVcmXCFUMxklEWw2C-2rUwKBiDbm12H1p1y6Dp8IwUQ0bXVN0_fGcAve9jI747yYUc8M_q2AswD6mwkA5upESKdwCGAID4ey10wQ3NoLLyE9TV7Qp4PuBn_sStwq1pe7IHHzcHRQXMvToNz09uVEPxyLV5QxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت به بالای ۹۳ دلار رسید
🔹
قیمت نفت خام برنت در معاملات امروز با عبور از مرز ۹۳ دلار در هر بشکه، به بالاترین سطح خود از ماه جولای (تیرماه) سال جاری دست یافت.
🔹
این افزایش قیمت درحالی رخ داده که نگرانی‌ها دربارۀ اختلال در عرضۀ انرژی با بسته ماندن تنگه هرمز و بن‌بست در مذاکرات، بار دیگر بازارهای جهانی را تحت تأثیر قرار داده است.
🔹
به نوشتۀ الجزیره افزایش ریسک‌های مرتبط با ترانزیت نفت از تنگۀ هرمز، مهم‌ترین عامل جهش قیمت محسوب می‌شود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/457196" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457195">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVGqF7VrXF2kS_yv23voidq7Zxi2ckIg96QQtcT9npJ3kPA4dKGrwduRNKRY5jP_0PW3IN25a6y0nb0QOCd9ErrZW7SBLP5KrMVuhJj4NQIsOjL1bSk4v0Dmdl4g1XBwV2Rj2C4XNzlHOT1aQEE6yZnYrFhzuMHJrfTOt080lOcC3KgZwtghPzedAdymz6DKq2dTmCfKRG5vvLKghkZpVtJneZTDeMSSNJe7wf1u-eotZXLwRyw6RqUDlX3jq3vLV5hoOkjZAnexpv2FxUa56jKyWVgw2vRbFo0284P-o5ne2pLcRbn3JqDTLS0pDIafu_ByzdI_k4OdZmxTcZ9c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ دریایی برای یک نفتکش در خلیج عدن
🔹
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد گزارشی دربارۀ وقوع یک حادثه در ۱۳۶ مایل دریایی شرق مُکَلّا در یمن دریافت کرده.
🔹
براساس این گزارش، یک نفتکش که به‌سمت غرب در خلیج عدن در حرکت بود، اعلام کرد که یک شناور غیرمجاز به آن نزدیک شده است.
🔹
این نهاد اعلام کرد تأییدیه‌ای دریافت کرده مبنی‌بر اینکه شش فرد مسلح وارد نفتکش شده‌ و کنترل آن را در اختیار دارند و در حال هدایتش به‌سمت سومالی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/457195" target="_blank">📅 13:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBtrogEf6mZsVSCk2bicyhYqKHMh-xEiEfFSIkal_4BsVRmtZJdb4jsMvAZIthrhP21Yjc7hwkKiluciLefq9scUhpMhB8kzys45z-AXqGGDKkJNh1OqDBgG4FaSL1U64balxJHeK663cMnWk_SxXpfkaAN9qOqbNFi_SELp7cQxY8XVHfkVnKMBWnFqDP8chNdGhotXwKllOYofJ1apZBpNbs_KC1xQxGNb1GYhFU6u8XwjBI168MJxO6DU3zkCTTmaoDqJYu-hPN5Ci370L6ZZ0xmXpDs2fAtiAbrE-ZpJlsJtHNS9z3s7vb3Hzq8l3-1BjuiwkEen6FbMRV1KYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCFIdRav0jP9R6YWxoulq-EZ7KNZNTqOyO7Uwi-aTmwoO9ex_ntK-zpPJrpVNyPelnLQ-7lhMHdxDOSsQOSLhcf7RBkDKIJCnKJXsKl4JR-4T-u88A1oJARt0kF0A7dN6mVG-lQNHv_Xz2UsXn-F6Sm1ephEe3fY9E2M2YsiGXd3vS9pEmQoYBk2vOLTMf4zXbn0aRh81OD16MNTrsaaEX6PmUWqUi_HG9LXD898IX4UZKEFF9K-T5RMO7Ub3QK7zZikFTtJ35w5n3vA8vNazjITLpTtaTezAeet5MpZb7-vzpxAwvWplRGLvuzC4utkHN73pBa-1FoKHLwKLlkYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hENDmd4aEqnjgx15deDNE9hlB9EPd6t5NBfpultlfEfSXRJEHqV1rvF0AAPX28_JaTrJ3FFyfD3t0oVAezK7O1STU628-fk7nArZsq8VoBgSI7EQSjHXGi5yQFO_VQL3IplqEIdGt6taON2OGMRrbBnFhN03-5hlUg0YCZoI1uxOBQrECwyFwE7iRrzqGgWkqU8eBXLRwIqo_fECGZGAlSVTGtXaxjGGfUtXpaL3KOQJhWe2IrxGsOM4vFAoF1UySdtGvsmBr4fyMzoGmOWJqRihrmGlb0K6ibrRKTl5wa6BZP6W6oesHl5zFsYpTcoaAdhYM7dOIwNw5ArrmSBSQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d097d3b42.mp4?token=J0SUGa_lMREK1G0DDXWAZhWTVtz2yIO7rNFlYg1TZrRTncsKChCPnqSLHoEbFSv10_U3PSK3m1Sucy2Dsj7LqhXtYu4bYJ8vMBRFLVLpi7E_YhEkjSUbqRamDvutgbWgXvlzCKSa36yWGD-idt1w-AdouOwpniv60Pu3hHiSbb7jxUT8Tv979tg38jfwXrkb9MVB_v19OQFrA0NPnirDsQhRufK7B6E8tGGi67z4XqPMSmJzCYcOrTpTPx3K5JAZT6NafPEZlW4Nl4BuQddF6NH3wLAN9a_UhlfB5Tvc5aq3WBvNwWYiYbJYYIfrPU3C-QtgOUPfmb3kZptFJF8h2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب برج ۱۰ طبقۀ ۲ هزار میلیاردی در اراضی ملی میگون
🔹
عملیات اجرای حکم قطعی دادگاه برای قلع‌وقمع و اعاده به وضع سابق یک ساختمان ۱۰ طبقه و ۳۰ واحدی غیرمجاز در زمینی به مساحت ۳۶۵۰ متر مربع در پلاک ۲۰ منطقۀ میگون شمیرانات آغاز شد.
🔹
ارزش این بنا بیش از ۲ هزار میلیارد تومان برآورد می‌شود. عرصۀ محل احداث بنا، جزو اراضی ملی بوده که پس از تصرف، ساخت‌وساز غیرمجاز در آن صورت گرفته.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/457191" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a88da1c3.mp4?token=TqXJPCSFDJcfdZqrYc0fVY9HhLHEKZARJm5iHHuIYAdIz1StsOLEjsJg_KQsRmBvRAOIpfFY6SxdipMNs1p1V-Tbd5b1bcC4Vvk-RnS8P1kpOvRc52sfGwOcpEVFvKJRchvoNBk9V6aeZQvK0T6bM4btUHJFfNTnkS2ThnOt4nPsQYH9piE7RePTKCGEQ29LEwVlc4FPml3OT2zk3AXlDLnR4Hesg9ve5TOOwAl-1XiElIDc1o6cMPEupLDfE3mf8AN6yXf_mYdJGEbTpyFWgl5sxKFR-_tC3EyqY_ApSnL2Vcw947EcAVYSH74Y8IpZvHtXgnDlBytRxwA_I7kswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین عکس برای کارنامه
🔹
براساس یک داستان واقعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/457190" target="_blank">📅 13:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb2b16fd3.mp4?token=DY9NAZ_GHP-De6Sj0KH34YRbsSB8HIKjQ7N7qBn1jnKQTmhJNtBvQhYABUWknPwzxAt_X429C8PDmpXllXpomZWq5Yxfr1zj5Iwo7MHUn-buSn6VbpjEEeHamGziCQehQBZePLRWiBcJTKnkg7XVldWEI6UGp7qRLBZf12jdlnNNzkebh6sjijRfE1GoPF5NtqR0IvDIEGnHzODzkiT9vDuVnRwQ6B5TOhZzob6qH2vMS8DDcEGwdYzRl5RAgK1q9_2bDCmxzhZ0OJ9tizlM-JtG9JU360khmK7PeCQVd3GuIgDii9CYKvMNxos0txPqZfAiNxlBQIUEH7-8UKeXcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یابن الحسن آجرک الله
من واسۀ اشکات بمیرم
◾️
سیاه‌پوشی حرم رضوی در سوگ شهادت امام حسن عسکری (ع)
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/457188" target="_blank">📅 13:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpxnptoLqDDDfznJ5QROzEhFe-Gm_0oY9GVSfK2pexbdml-VzOp0oMZovhYv6UGCNn6zb7071J3DCeIS5BpBL4djRWbDVdAqtuEiWcnpoCPUo1MsV7Ui-KlCGRTzb-z4gAatDrT2vXlNdGj2fndbT0zEH-8xQqAy34Jq2XEo0rDITKaHQkg4k5lipLr-fHOTS-hTAQwWcX05sT9UKeUoYl_HkuaGp6YJPGcTYHQn-238xDA52A3FwIQawQ1V3XcPeikZ-9BN1uKFtb9r71HJnT5GMwqpu9bT-2U_N0Bc4sthhmquC5ULQ6LK5OZUHeTGToIXWRynmFz0dMoy_awzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457187" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG-j8ox84LIkQstS5gNIfYJimlJ1xBDS1a087rNY6JOKVWT_2BNNZA9_Bu4JkraHPBAaJUZrpxb2xiD4yBidRxAmd9z4V30w-y2k5bz4oBHMiWaJAilGSwJRmxdhSQsPsu0YaoEQMPp34H0ah4Dqo11oVr54h3LLPtSvwYshsa5qzlVT-F0s2e2y9llVmAKODs2KtR1WPrrk4AVmGEMInppsok7ASCuDGVmWV8CFoL5J-i1OXO6sEO0nnZKRze9q1R5ak6RHBI8AhMvyjnIc6jf2DExhKZ8wId-Mutyu_W3Z2_RhRj3BsvSwhgcjrT4ccYYcuzVf6IIiJ2zQAYs1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_ZiOzmkXMy3gg6_kaEzwJTuIyLnjayzxi-_L6f3TXhpDeQE8YEIfxstQJY49mc1VTA9yDAeT8PAN2nVPITYZJOESurqWrLYU-bOAscamA71HqXBrDG1wytuD4nyGvMI7SccQK2BBgJVkJp9RSqMiomulo_RM-K_-8J7NDXpBwOXl68HS8jjwse_alij3N-ztPsK34NQb8fXnlcwGUVHI-min65Mw1qxQqsmnXLU99mP8iQcoD2ZGunFcjRmC8Br7ThD7CeOsYuYqRCrEMWNmtb_WYBKickQtslUYcFdTHm3nW0BAGKCDb9KCoNAfNpWRJCWQKVx3b2j7he7Vjaqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn3PCuBoWmGK1fXv3Buc71EHqf2ZRVIOrSd0iCWo0sqh35Uf8hU1PlqcQKnpcjLcqYRFdNE-Wd_49nErA1W0sLpxLurH7qKIVWxh4ei6Mii4chFq3o_MAZSiFvboTTYcwR48asYprXbThMaZqde7a36oDE4oDmA-nOIiBcGUjdz7VGn6Ahq_k83r282eUz1-t8H08jiS7gI_fnySMdBPJIwBRXdfABbdnTH489mviOEejOPi981WKVBLLCC29Bz_xOOAJ4rimeV0MSFmnHjKgAgHGHQFf9gO1KJKilwigFTk2hdQhJOwM7IsQuBGnKWY69QGpJ0UKuDcMGUWRaH_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0bkjyzq-KJxW_1E-emNILkefnvdfGeoghxI1YCFMMpxW-KvH91Yp9_-KlSVYxB0CYbzIfRLBffvIgv0Ht5dLXSEIFKQzShPIvod0Fp8AvBiu2MpP-NpqRR57Oq-KDrMYnBw2ujI9svyKDnFofwazWXfNcyLEcL-r8yPaDKXIWSWjiEFYVcV0mJaDf6C3tp9hYu9_dUeJ_s4-_qqrG2nTlY73m3faRR-zSxiUH3hhOYtK2ShuNpBGcN-g2HuawuzojBr-KKuzFo5iyplwTNAE77PlU0Cj3LNcCUJ2dUM5ulKyelAZsqJLxLy4NP1m4pYXuMQ-onE77406C7WOXtoQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: ایران و عراق دشمنان مشترکی دارند
🔹
رئیس مجلس در دیدار با نخست‌وزیر عراق: ملت ایران و عراق هم دارای اشتراکات جغرافیایی، تاریخی، دینی و مذهبی هستند و هم به عنوان دوستان و دشمنان مشترکی دارند.
🔹
ایران و عراق با نقش‌آفرینی منطقه‌ای در بین کشورهای اسلامی…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457183" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=RrAD8-JPBVun9TOPHYcAvmIw7hWwiN5xWGrnyIjueyW4VGjMFzValjCd0OACzzxJBA5AzTLTPkOAeZ_7W3EsCi4Twn_K6viLRbQqBiHhueygFS-wP4-tngkzyIdsG5vv85o6rBTEM_ALMGk8sBtcuB9e3sR2xCw7HJIPQwN9v6e_nP22vHCvz8Yrw8XTqD1R_L6hNgeyD-iuh_S-asFJl5DY9mfYThVMJYWkgo9j4YPpi6PCd885qFW02G8_7TQQ3Sm2O93z973434D9EymMos7cvxABaLHJnHB5jyTVn6hOFTHuvh_tz2km5_H2JcSOY9FV-YmrxhFfgoR0LtKUDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردبیر پیشین نشریۀ خلیج‌تایمز: کشورهای منطقۀ خلیج فارس از ترس موشک‌ها و پهپادها، به تعامل با ایران روی آورده‌اند!
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/457182" target="_blank">📅 12:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JupuXNwozvWA-U_DrkQ4ByvfXspJbeYmH1RqPDM2JBcGTZvJOPXDtJKXA58Wa90sXp9fCQP956OlZrgaU2NMY6IVNOsiSm6F8cnHIzcsNPQoIexDXh7KZ7ijfTTEOwcS5-nWt0U4mlbRlouYZRPYAYqqqQbxW0oMVNaQrZAWrKtr5Yq9q2kxgc0_Sj_s7TQ0w-AonffJy0IeZBjTzvhSwpNuG_8UfTxWZDCc-tH4w8XggcIVbFpMGufx3eX92d2VKZPP8CfnAFlU8HkAK-vAQnYy4PA5mRwYJOE1fKvty3_wTPauSJZ6nQvzw3vKKW2KsH_xQGjAFvcWZGoegw0ZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در راستای اجرای سیاست‌های کلان شستا و تاپیکو؛
💥
پنجمین محموله متانول فن‌آوران در رینگ بین‌الملل بورس انرژی فروخته شد
🔶
در راستای اجرای سیاست‌های کلان شستا و تاپیکو، پنجمین محموله متانول شرکت پتروشیمی فن‌آوران در رینگ بین‌الملل بورس انرژی با رقابت به فروش رسید.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/457181" target="_blank">📅 12:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨
✨
شهرآسا؛ جایی که هر تراکنش، یک فرصت تازه می‌سازه…
اگر صاحب کسب‌وکار هستید، وقتش رسیده از تراکنش‌های روزانه‌تون بیشتر از همیشه بهره ببرید.
✨
با استفاده از خدمات آسان پرداخت و اتصال پایانه های فروشگاهی و یا درگاه های پرداخت اینترنتی به حساب بانک شهر، وارد دنیایی از مزایای ویژه «شهرآسا» شوید:
💳
تسهیلات ویژه با نرخ‌های متنوع و اقساط بلند مدت
🎁
جوایز نقدی، هدایای ارزشمند و تجهیزات جانبی ویژه اصناف
📈
امکان بهره‌مندی از تسهیلات برای پذیرندگان آسان‌پرداخت با میانگین یک‌ماهه و سایر پذیرندگان با میانگین سه‌ماهه تا ۷ برابر میانگین حساب و سقف ۱۰۰ میلیارد ریال تسهیلات
🏆
تقدیر از پذیرندگان برتر
✨
و هیجان‌انگیزتر از همه…
هر ماه با هر ۱۰ میلیون ریال تراکنش، یک امتیاز دریافت کنید و شانس خود را برای برنده شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
💫
شهرآسا؛ فرصتی برای رشد کسب‌وکار، دریافت تسهیلات و کسب امتیاز، با هر تراکنش.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/457180" target="_blank">📅 12:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/457179" target="_blank">📅 12:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krkFfkuLDpM2vfZtVuNBXPn2d-pm8Y-teJ-okxs23KKQI0mNrsDzq2mZzW9S1LIW7fiTnnonxlp6Ig1JTMVvFf-hBEg9j7qI7ljENncZRctkMxv_Xr0xfaCtr62qK9TJ0k9BEvj6fcXp2z_dEkdyYt4TBJVOITY6kZmSzlvvQlfxhR6SrKf4UoYOXtHQmE3DV8x-NJr-A4k_kErZUgpcU4ZmAWudyZKoi_NhBL2XPZGbR0J0-aUh4McZc_rs9o9CtpU5lJTZPZ30IEwcSBCyWFS_ht81t0yHqk2piWZqEY9d948kP5Xfp3ZPTGPLbkq_jis_XMvG8rlFvexlLd2hjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اهدای دست‌نوشتۀ سردار موسوی به خانواده‌ای با ۱۱ شهید
🔹
دست‌نوشتۀ فرمانده نیروی هوافضای سپاه، به خانوادۀ اسدزاده بخشایش که ۱۱ نفر از اعضای آن در جنگ تحمیلی رمضان(۴۰ روزه) به شهادت رسیده‌اند، اهدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/457178" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgASHl-1huyjSODFd1ix1DQ971VPnIFIqGmaj2nDGjMLkyeRESGxHXxIn88scHnorMpWTDpGL9Xwt82OtY_92TompQEpsQS0EmJuEwq46ChonoyTHmNQfP0X171jD5GwFxBhSltipMey94FURQBkJ-GA4WfSa8VbmCGq58SzKtvF5ZtVFLUHFIg6rE2wIz7AXzmaOL-7w8EedKhrq7xoL3E3d3a-K1DoLzYXz7pw3jrADTTlyBdh6K1h0gcjQw5dSvVBrk8vcJCjwi9MpUrtmdb4QxuI-7ZBQbq2mVlPu8-xBFScBnprnxAdoobJek11JbwjzOHYmODF4JxyqW5uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXuFsxJkG0fXbZGg2I0vIq95lRDvjjtsK5PN6rLZf3ywKxSzaz2sbg7pLTFWDjkIMBXvlaIsW81C3AqPWMDKjff8Fh4_7uXuDKdkNz58kCBPwNGPd44B3G4911eSxVUduxblclv0YjDHuX_rqhXrFJ7I0bI5YMEdbAunuwCEu1ZDEt9ajm-hJfcKP50VqS3L6mwAjRzITTGMcBpEA6nDjR9ozQ7OJ6I1RmWJCSsoGpDgS0rWgC6ptrtfRprGm70HjYDQGSctKByW45APX5p12lembLjp1t9kFG4C1bKmN5CrWywBFnpwz5MOQSKjUpkcitmZFxhUmmKn0yqsIJ7D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M38bEtqoxDGmOI9nqJt7p50QbETcX-vY_ZSbkXpWD6iPIdisRhemFPNz4QbjxyVYMAZjo6cubhGxFQ6dV9HF4p_WpNA4qQm8088aoPeJ9QYCl7HBv2fQkcNcyB1bvD9yPBOgptnZdO2axlHT1n2pWtpZjQiBh-zBSAM6jIApqsK11zr7SUPQqof8HsOUpC0MbcM7Q5mZq41b2h84ngpqX1HaLeKpKKSbT3H-aMl-YQERu--4ejn1PcHaJsGpR0N6HBT4GQnB2LcvRkLfCsQukZfdICmrA2s21lr21Pr2-2sdugPwDOgDzMQIeWRCLvgrX-0R0aqud-BBpAKRjiPgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0qo29VqEz1poGbg8_bxuI7mnVn0PZ7uHUpuy4h-vPiMlOp4-xwTbtSKNusLKqw9ptvGgPTO5u-TyzLT4qPuNK_o-thnEENN46h2pRJPkjlmIAaLbC6aOY4FrEtpGAVqYyj9VKjjsrpT-ItZDHyLM1wX0Yy3NVdh7J2w2zRMb1XbTOjlhsIVBvsWKxFP4_QDkf85xv-MsHsYvZXzX34tRVuv21-A_WJEEYoArYUQDWpxuAmLHQgM2ZecmyRbC4fIklzR0iogdK7OCp0cfADINMWIM_UV8J2J_uyBOImGqQ6lHnRcspLWVpmFYMBYbYydLiTWbAbPT47gP0A68YCvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHDeMe4mHv6rL2hCiHAr28O3NUkx_2Fo6jAWXw4XNCFRkjxdCDoDOHTH4GmS5ICb-9sJ53u4CnbGTVpj5wnh002PgCQ_sejr1MGuGPNREfCX2stWg-sPHR-870_CdsHE6zTHi06Hpuba8c2xpoh4hNriZZBAyjE4RTH-IXGerZBG36g-jYs-DkHuAz8VttOI_81a4DJfo2E3YloZYRSK1zWdKGgZhhGVHl3kYAqDVtHRDCrKZQB9NiuS_X1LBX9jM86F3Zad0PGMTkSxjUS5yn4rvSuFa_arm78gJcWZhl-UdVMJNyLcO0q8N-UbVXLrSFuMD_AvG3JS3PI4g7bfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCZteIDMj4w-w5IRdCdI-wPzvnr1pOG1bSQhAEtneSw2sQgRD-ckSBoHXgsiaxSYZNHhndhcWq2OvnTga3KFnXW_errUxl1MSA1aRKUxwcI6lyOtvXaCJZjbr6bCWBau4C9jc9XTG2eSfH5vD8LBJwH1FMbaXOf-ioXmiS6fxf_VmmNoJJCb3fXbZ2MZuXK1-01V9EaSf8FwEWJGcM7VU5g-ViovEX_9rKBT-x2BYFa0xISo7Q1MxCIAm8nfha8w1bgSuhTBwt6SuWePeCY0yQjhCKzOcvWWjX-4l28SoEV24PHY24pJJwb6x-I6vMfzU0nk5bNKT2Dr60JjRmHmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfROrwGW3cLZjdYYkshjKdWhoP1f9QfBOrTrWOjtW5JVXM8MDSk4c3F4CJXcSTLht5fCwTeXeKCUWlnFzW6g30ICBp1l2MpDL3aq46wQ33DUTtmMHG8z0OVHFIE6lnK0XygNBuJncbCpRLW1jIxN6ll3TjmIoeALxgueYyiWZQnP3ujLSoWP3Qs_ICrmZMEVg5omF61qpEuHgm95mwe8fXTQ4rUPR3cRNDb6aEtddjuqg3d591D45o85h4lD63URsUiXLGGHmAo_Rbm5rQrnwYSg0RzNRIgrzhaz0fXLcQG8WvElmhvQB3dTbMiTGz1ueCinS5STdQJGu5Bj0eLPOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر علوم: بزرگ‌سال‌ترین داوطلب کنکور ۸۵ سال و جوان‌ترین‌ ۱۲ سال سن دارند.  @Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/457171" target="_blank">📅 11:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f312278eb.mp4?token=ON77ZD9kevPwl7Ie3TktU2X79kAVKHSiuLwJLHkuRYbKltETIW88u2fj0o47QU79BKYWf5AxyopKbojsw9QuEVuKKOGUKsIvMFBMYxH3Y5L__vq7ifTfLEmQbjUsLjslgwtXnT0yiho3SWMlCfufyPlKHa99-b8Q_QW4QHAHTca0-Tsw5cE7Q2ZAfZCQ8XcSi95iPkhpqq6777vROwhaMcQkJHonhZGFQMgRwvOjfW8fRA-4mfuNOpZLVLMbC4Cb0BKU5fWQamhMNcDkQGh9o1tYZYtxdmlws_u3PblSPwgh6OVYYlRRgKL74N6kFQLdFOERBq9BJR3YILHtGQhbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دود حوالی پالایشگاه تهران چه بود؟
🔹
روابط عمومی پالایشگاه نفت تهران: دو تانکر حمل و بارگیری فرآورده‌های نفتی صبح امروز در محوطه بارگیری پالایشگاه نفت تهران دچار حریق شدند که با حضور نیروهای آتش‌نشانی، آتش‌سوزی به‌طور کامل مهار شد.
🔹
تانکرهای حادثه‌دیده مربوط به حمل نفت سفید بودند و حریق در محل بارگیری رخ داده است. نیروهای آتش‌نشانی در محل حضور یافته و عملیات اطفای حریق را به‌طور کامل انجام دادند.
🔹
در این حادثه، واحدهای عملیاتی پالایشگاه نفت تهران آسیبی ندیده‌اند و فعالیت این واحدها بدون مشکل ادامه دارد. همچنین این حریق خللی در روند تولید پالایشگاه ایجاد نکرده است.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/457170" target="_blank">📅 11:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbmlP3pU_GDTs8Al-Ak7H1oT24IcnHgNoOdh1Q6xClIqCoowVnair4fJPpAgMHcLlhYVtx8DsBoRrjtn71UQL64FVivcL0gFJS4fFhku7xmWyJ8bfVIbWhXgHAgb_OxqPvfAl_vBRLanq8OP5bpbmlNc66G4gMlK-14e7KNImSrNSCBvOE5YOZZJB4mR9D7S7XRdJ3m1PrynrgqB5AQu6SXISSZgA9jopXR8CJ85VvBauLvK3eos4U8OW_1TZfZ3GfObyXGl00el0NNf5o1tJp0et4uSqeYgagB0Dr-YogrSG0eU5FBDsQc2A_o0sjpJ6HQgZO0CYeyYShWpKTg4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به مقامات آمریکایی: اصرار بر ادامهٔ سیاست‌های شکست‌خورده، تنها شکست‌های بیشتری به بار خواهد آورد
🔹
تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی آمریکا از بحران‌های مالی داخلی است: یعنی بدهی‌های بی‌سابقه و افزایش…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/457169" target="_blank">📅 11:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsM-QQeHDMFbHWFhIGdQnb6FBKp2rbNbaWoaLdn1aspwRydDbgzFRCt984B1OlCAQwuJ9u1SDNcTSAqQ5C-UZcLC90Qz-yDEIC-O8R5BSU8ch-_TNbt62Y2CKYHY7HjlpAUE8q6SSnYr-Mds88_VLkN1Yat02AAH4viRAxG5hjdbOLZokOHhnk9Gyel8hLCVbD1tD_G7m3GAT4IAbs8BJ0Y9PKzLEEb-f_uNji2BdvHDF2B1gnnEe496x6c_OGtmdm7jdr-ptL7zV4gk1JnHEmjckZSEVsP0upx2p_EbCByUd4k2XcxDLUOiei9NU4HjsGW7lDYyUEVPAdyiMToBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس از ایران، بازی اسرائیل در عربستان را لغو
کرد
🔹
«جام ملت‌های ورزش‌های الکترونیکی به‌دلیل ناامنی در منطقه به‌تعویق افتاد»؛ این بیانیۀ سازمان Esports Foundation از لغو مسابقات به میزبانی عربستان است.
🔹
اسرائیل در این مسابقات برای اولین‌بار در تاریخ می‌خواست یک تیم ورزشی را به ریاض عازم کند.
🔹
سایت Al-Monitor صراحتاً جنگ ایران را عامل ضربه به پروژۀ بازی‌های الکترونیکی عربستان دانست و تعویق ENC را در همین چارچوب تحلیل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457168" target="_blank">📅 11:32 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
