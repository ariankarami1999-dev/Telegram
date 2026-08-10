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
<img src="https://cdn5.telesco.pe/file/ZEzTZQGvM9NxmsM2Qm5055YaR0sFNFYwMoiiUsJvzvmx5b_EBeMtBCyLRd9pd7a7QlhG-y3DWv5avILRclvKBuXpkYlfaHt_YIdDX_2hed_qDe_nOQqq9zjc8MmKn4fza_7sRwhgiBP-Oou3vHFvmK6QDjxn8349LS0k4bV38JQEei1uV1qGe2zWEv5_Cjbra9isfC7AgyXv_stE_O0gCjlZbqSMrt9dB-LR02Yl87mx3dGwP1WF_XA8sLB5Rc5zctH8JjI5p0t3Y8pH5jnYcO85Hantv_s4c34q6aRKYNNQSvxZazOU8b-WfxYFJxGSXZBnpajlgrKaCi4ATdwqQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 480K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 10:18:45</div>
<hr>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3E7Fx3MB35Ubim0LOVN2qzQ657VJORaiq2NL28S2mSZcB6xO_2-2eMTm33teP7iCcFtMwud5Qk_TMhRutXuU0ss0k60s_GrYFxEFrkdzhPcWPY7mQjjpV9tiytgySthTAUXFEA770FICvmihWhZVlaUhVDxLWH-z33214o-Giz20-LOcjSjCtxbYu79eWXkzstj-UidYaGiCjMPZQEpXn2DLElEhZiH2vTdy_ZfJ0K9rBzzBlaxiGRDzGbnwcp5fDtgInxEs3yWNd1zsyjpTGidhdgkuSyUS6CVChIIIBBI8AaT2UTaZRwix_APCneIM8gi33_2O-g3Uu5pVB7MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103227" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/103227" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/103226" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqfkDrF8WRGwr4QQ5yxZWthF1Ftsf5pxZrxXIfZ1wVsYouR7mV9UpsF1PDyhzW17dKl5MZNgxcJsIv-EnB2Ica0fH9mWN135SJ0l1ccFwrf-wIFIpBgMTfsGOYOXl3KxmONYPfQDV05KXGUnhG3wa-8GDUgPxn-kubBFQ1HemsfN5agDEjRoGhplTh57edPdKjn4MOlgQjzycHpo6i1lRzL7bOkNBlW8usUSKqzSaL9kk-Y1lpMng4_kaWuUQkJbMfIAUixocUU_6I8Qi2fLxDlbKUJJAuby6LDyMo1WNA0AcLu6HJRGgZrIb5Q-0Bk5Y4AwtYrqgfjGyseo2Whcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
مقایسه آمار فرنکی‌دی‌یونگ و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/103225" target="_blank">📅 09:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIHAdALsxGa0XN7yYoyXOgN4gf3482RX4drsrHk0V36suknCXaF0sHRdldegRCfeBGaRJGVHBCyU4EbnlUK352L5fA4A0FDbF-iBOzV6j-G5gz7Qstju9AxOvLWz6Em-_PjhZwsUIlcdpkrEzLlkd8DPjuq9r7WEuOgYFD_qg6EzmCPSJn1m0Qh1slx9ogeVTxzguVLYDjxRxDI_pk_kb4LGM2NMkdezw9ebh4lVikRiDXuxrYtWzB4bZ4zIPSv0m1W0c8R4XXWgBEWlfRRJQPG-ERYh5GAnCrVLt_sxdgJ8XDH4oyimNczfxS0CM0C6Kr5rO3D6HRtJ5EDW_aEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط هجومی فصل‌آینده الکلاسیکو
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/103224" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👀
🔥
برخی از گل‌های چیپ تاریخی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/103223" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsRerGv4jJNIx6hPFSKOQn1LjXqWqTJWHA40fFFJn3bSI--rdlNFkNlXVRaLtG5A8I99ZOOsTNR3riLpNoBzPxyEPQmI0ZHGKaFKBJ9sLGA7WYlmbm4-vBSX_BCSE_JgAAy_SLZc9oxt8aR7Hi29dBqpaXyi3dPbp0K3s17CwxWd6jxGT0uLmfosqhvFtBT3r_uS4Wgbtm8sT_GLWMmZwk_JaF6UMvjWC6h3-LwHg8H9s-xOjzpsrkocTHkNA7N6x-x7529_p1gcn6q0chdj0V7VWr-JAeePgpTUrtIa5DYOZ9xW8JiJERqd4P383qUtWaWMB2Rx-4ER11-JS48bPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
نشریه‌تایمز انگلیس: هری‌کین بزودی قرارداد خود را با بایرن‌مونیخ تا ۲۰۲۹ تمدید میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/103222" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DufT3vobUjBpoPYXv--BtLkR111_4s6l_7sYjqHZHb2xFBQZTnxaRt1LBwKSVS4vc8UudAp1oP_pNaVMKCC-H-SZG6D56m-fpGN00YDaIW3Dp7JvCevRGKemlGf-ON_xnySu1vuolfW_Xvs6qLyF3tnXx4hCX2a0fGRHPnLOfWfGA1vHuwIwH675Q28acRlxZPVkkxkL3OogGNgcFSgwYbVCCP1Z7gvncY4gbd_8E_b9zI2mp-Tx9Tm-EhRq_qOmdYtbR9pnTekHvp5SjJwIGxKYMX4XJBtFLaZT4z0OSStbcR2TUHDG8oD2Hlm82qAV65Te6Bei96iIDljGO1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
#فوووووری
از رومانو: اندریک خواهان موندن در رئال‌مادرید شده. از طرفی استون‌ویلا و رم برای جذب این بازیکن اقدام کردن و مشخص نیست که رئال راضی به قرض دادن مجدد این بازیکن میشه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103221" target="_blank">📅 01:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ5e6mY3QeFnU8bn75Vz1AOPXETzA0W4REzzX_NVRtiXnztIVE34zJW34hWQyBA551GY57B_ANfHACi2Q3EtzH7NfGtCTyeFsRpPRuDKxMIM5ZRyuZ_swns9VqRB1GBjeM5wMatoqslXTLTM4-i1t8jN2AO6ZKfKQzrv1QGezWuuZdCzKeiAJEzJQRcAaBwybFsfeJT5G5k1ljbRy-yFUp8lhpzI1-o_D3Tjx3sp_llT9UC195DVYcnZ-nGZK2LU4pGXGCXwJGu_9s_zQnXEesph8y_5vMbbKYudQZuVEAGJ2_sEXeJQ_4wt41Vc6t7tqH3kt89Se9OtNq13KWci-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: کونده مدافع تیم‌ملی فرانسه و بارسلونا از یک تیم در لیگ‌برتر انگلیس پیشنهاد خوبی دریافت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103220" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
👀
⚠️
حمله تُند و بی سابقه محمود فکری به عادل فردوسی پور: زورت برسه همه رو لِه می کنی! نرسه هم دستشون رو می بوسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103219" target="_blank">📅 01:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🎙
‼️
📰
علیرضا دبیر: شبکه به‌دردنخور، آدم‌کش، جاسوس و کثافتِ اینترنشنال! من محکم تا تهش هستم؛ مسئولین هم نترسن، بزنن، بترکوننشون، به مردم بشناسونن این کثافت‌ها رو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103218" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtwyVXo_S9jMSPHASo2jiFGOUPxJiqz9gPdHzKdulrynJKL3YRHe63zroFYeVKt5WvmGbD8G5pR0S6JWvrVEsReLFsKLWpHmfJ-DRwOc28c-UR5q1es78c4qOscHQd5gvk31zdFc6VcUfLU0cGJ_G1xErk6_LcORidtpMXJyhKcTiL42NEpl7dzgBoyvFtDUbCNPShYuKnH66EqfXxzgw6diws4EWZIXF5XyF1dHAG56mCGthfmRbPduJ1ENMOGTWKSUW7uNHes0TEMOtlTpbXamdUTdtFgwoeb4UogBW-VqhcIldgt84ZAlr-68prniPZDEfQ6sgsW9oGPJ6YjcOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇹
برنامه فصل‌آینده مسابقات کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103217" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103216" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103215" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBZTde2oc-lDS7_fDEUBh8byrE-v9H6myCxhz6BFlSvhbx-rcpjEtJAGbJ-9qznEVtwKPxygmp0YjpPoo6-P2k6hG1vtcwJn_5D5QAMass1xZqEeuES4E6tjOX422GDxYFfHMQx-aPV7JTbZdIpGXsLL8mqPt14Hfu83Uj6NMzJZWLjJk4KP4hRj9AGy_DyzrckEuDl2Uk4Yebt7OLMbJxbaQS34goaqsgGu5GUYwEPkXku7hH_0_aD18VDCVYXFIhA_DlVVxcL82Pg7TygdQth5iqgLddk4hKfMb24_qm32eBoWiPFSgY3cevrdsxhy7rdcs-tlS1T2Pq3RRNkG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔴
#فوووووری
؛ دانیال‌ایری مدافع تیم‌ملی ایران با عقد قراردادی به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103214" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
⭕️
🇮🇷
سپاه پاسداران یک کشتی در تنگه هرمز را با موشک هدف قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103213" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQWLkqz7EV_AuSkxfE7KA07srHfLPzUrIZNrTWAyof2pLxGvGN5-4DI1Dlf5YKcZZ4FcNiyyASY3KfGuQe_xHYXZpCnqpKrO20on_UeFwVnEQUkQkqdM68le5wvYSogTnaxzgEHK8J1nC6HmRi-TexdQCoVYNg0f1AZ2mQbuAwXM_FaR8MSawoFAHtNGFhbP441Hk3XhsN8oHF0pze5XEoPVPFAd2ubcxCBh2yVws39Pg6ZWo2QTRIW3N0kyyd3op1y9nBb0MRmFfUOhgxCOLQBVnQkMrHlAWAT6wWHZFP_yOog-VdwyM3mu0ogRC1U6f8P5uSpD-i7kqXHHmQu6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از گستون‌ایدول: کریستین رومرو مدافع آرژانتین به اتلتیکومادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103212" target="_blank">📅 00:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
گستون‌ایدول:
🔻
بارسلونا به خولیان قول داده بعد از صحبت او با مدیران تمام تلاششو می‌کنه و پیشنهاد مالی چشمگیری به اتلتیکو میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103211" target="_blank">📅 00:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJfbmyBQL1VEDvB0RDB6_TzG_NNPjtiwc2z2tfO7I_n2pWC18_QTGLWBtlJBarDBxopMeIKtrcSZkk7bkjVfmA0Mut1FLdGKZ2iwWuH7T5VSH6mv6m_YrVUIN24FmWmPYoC6L2HPwUPPg0p0rPLstNRAdMhrha1YvlZlxTl9NqmMFJ38pMc_0RcGDfdV9nxFfl1xTvW3VUSWf22jDdTO_IkzNmdKBYuSG0A9eiLEqOs6RjqWlGPBu8sf4qizijGu2g1HG3Xu02clsHe_syyPffs2Z-G0DIF29c-LAcUYZEFm5vHYsrh6WCDvISuLwFrhxCA_o5sSPzHm1bbzLR4jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
و
#رسمیییییی
: داروین نونیز با عقد قراردادی به ترابوزان‌اسپور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103210" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103209" target="_blank">📅 23:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103208" target="_blank">📅 23:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103207" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffgL7QWJrRks1NcfbKoC6mHDzJn93kCAubPCIEBbttNT5q83w01mYct1WSbJwZhABsUG-4_60wraS7AEy3_JuiBAqgXRT8YciBuKOo0r6SprX5cwbtV2LgxnutcIaHfTWsqxFky2R6_IzQDKxrEAFDtYdUftXau2pLQLDr-FQTHXVxR67HjyamgWBdzX8A9FP5tI16TuAQWtLGWm4PVHT1IvMN4nvvfYYt-hXt3RP2ONRqKTBVZaibeiJFKiXLcIA1eOYa3_-CwDQnPFn-3dUq36nHq7RcgohdfnCb1HUkSdU4Lrgo-jyu_nxVrLGkM3eGxuM06-BK3BbFUFXDnf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103206" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImaqvA_tjidQvD14m0vPHgIGCM37ihyLRFYgpASQuN2CC2cDGFTDY35TC8CcAOPwuztoZHkAd2_AK5uHevOo8sAv7lBXjgw-ox14EHxHgNRd6_iqXKv3ffVn0UJ5m4CxTbuiuZVpMYGyjvYrixgKpl6Str1rN181wtQmNWmf8qoF9vaud97Lb1c5d3jhPsje36ByYKnmO-siYWoR9Aa3PkoIVd2N8TTo-0YHhl2DY6WT52jtBoDYXEOUG5IxNBPWWIq76AlqRrnJB3y5SdJ0_v-CLlM1iOVSWoa5xUYj5YyrmBk44HcOVUnfFwJbkEaXbeuSZq_C8Vz6_gtjYcCcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABBr1vIea-hg318ogCBL0_BC-tWMjblBYjYKT_bfdBN4_DwaWwNCHERfz7vWtCKHCNU9AcdnAi3S6-kE5P0G6XT7nqVH1qdPuHot0vRDt38SEp6PNCq1tHNXMeXvPK77XtC-AEqW2GIZxU-FyrRSGGcDdaAjG56kB_muGBigIK24k6mjO2JpAGA3eCfDhpEwcb_mHcJ05QHvc2s057zhu4G24cIXk7BlR8sfr8KRRTVbZjErwl4HWyb0jYFdlpu6poV56Sa-HUlgvfGiLTmjTnd7-0aiXuqskLLgG-csHMkPjiZcbOo-U12CntuJqsDWvp06d-yMLXgOskdFu7NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zI79B5nl5xozx4cnbeDh2xzBsF0mX0ARyJBoaeg5o1J0OXoTvFztdeCVcPTEFqYFAcCd3dPDDojBrMTzaXYR_hetCuL3C2wSWw-Pv91ycOS4WKU-XlFabtUAXYxQ_ST_xX_4-rMQ5KWQ_flyaGtdjv73WPfBoJJdHzx6ssXUlypUgs02GzP9l8Hrlp1YNa6IQH-BvI1Jgmv4Hc7Wp3eCHn0bUOhkf0jhTS_dbxOKng5ikSKePZjeJQMS9LQg071jDM_cLrcU4HhgwF9AlLfM1-QwqplV08pBs-C154taqs0b6ma04k-2qwQ7GRULMrb4ErKA6UsjhnSxsN2L0ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7-TPWmyDPZfqbJS5JYKqGlryeJJAEYC12C1NybTrBv6wv9btN2u0HYxvdv5hhTs4vWBR71yX31yeWi50cB4870YHAaRiGnBhgzhR6Lvx-HIkX8S8LJXRoUmNFivwUH0LccH1hMsaghuKKLXfiTkSgBethqnfOqPyTfZQofiNwhAqy098wJUGKKVtb6naq0JQHBnPCbziNWsUSXZ7HLJxtjJgDXFfW36vKlba8bjRe22doPP6yIOCM6BvL8IhK_oog72llwmAEFg8STSGzpUJcrdGe0nlmJcdoqgI0nmPvMdqlzMXekODjx8h88gVE6-WZWfW8RU2glyq3GHMLZl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_y6FbsRXxjyLpz-rHLoOD1PdWglJJnS1Ktbjw0ygdgSdNR1en6lvyT3q3Lwv08uzD_DiRbwzk3GnQ1sVmyKJuEIqs5JAkrLBSZdzxslqwjqVWR97eOAeuSIDpnwj9jMigMo0R3fzE-xw3PN95p2sl-tLJh99u2LTJ5f1rmc5FjZFH6E3QuwncxcmBp25HnS2H2ppKV5l_CxszqrfwFpexdrmPZd-AjUpmrb0DFhUoUozcU31Si7TLMzpFeJA6K_Io6UD4aLlXqSk2t3vgqqeYqxrYoJ8CdJyUJ_l3kBaDJ59RGQFHanG0F6xNxk1CFruFxwywaccMM7QxYaIcTfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD4SZq1X7nNg7uK-Xe5MssTrZxZp2nk_-mjnFku5MuYnvR8ZXWissRvgoHKZ6POPUh5Lq0rnEGjM-ouA9eC-JNswUoA56iB8vdXsyNzN_YR5iWCqVaLCFJ6rgy_wCD-rnSsDBIgruNXnBPYwOTErDMl-C_MMsayrsHne9gWdaOdtWy7vKPh2b3wfLhIjzUCoJ9KI0X96NgKo532ppOmzdj9IeFCldNEb6_xQ58ZcW7y9SaMH8j7Mnm_T5FDzq8Ylmn_s7Dd-AShEQZUywEp9mgSN_5YcL15VHAbDjR1oehfLqJQ8fFvlGTk7jXQ_Hde75RRXOY8Ogxo_30kDzD85cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddhPEBKNoIgJKfgEmkmRq8UtZU5CM27aSYkaBETdq18N54h9vWcIUoTC24X11iVHVZ8JbZbdYiwEN5wiQkczdDo7R1-iSbAoYTZE41OMqLFnBO8Xa6k7SbncEiNIzm71E3VranoFCbMAUZg4FPW_3Bgqedfel-QMTmZBRU_91GTyjSd0JrgbvTKH_ocQOCNV5ISwFnkkQGbf7LUd4V0IlKBxIoqdruS16lx-YY7iFgDGVz3PIdOOGeREpdGKW5GYw847dDVlyzpH2zow9H4xgT0qGlms8ZuIslVqJzlny63KIILEdB4qC_DNpmuq6VvGAEMqCf_jqs92XoxrKe9fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2O3JCe64MnBitMBtTXcNhwG0ff5wt8bwG-DR2sBZtcWmaLfr8dMlp57vOqa1XmfspOGgdd-GkaNrFFurGnpVRwhcbMx777wLLDxl5FD2T9XocPkQZVBjKQSkQrtAhjQGJKKToe0SKNE2k_JRqkxMbuyGo59idsH0mfN_v8UfvKwUzQqvVQ6uy2ev-LAn9vVFoRW-Fy-3Qj0sOIevirbkd8_DdmWnWKgoeN6CKSSd6RO5ZSQP2judBx6S6lNE8LxY_mqBaiGTAm1OOmUjyL5emdUf75691nATbJVAnBIQQ8Btpn7MWEfOBWJHiG2ixZXVl4cj2qgbfs3sLZ5vN7_5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqr8okGDATIV3dIjyAo8imPsa_BPsiWprqshijNJnanmYUvPsUDl-YOKKXxfmHwB9eS0EBuVPLKQsdZLwmPWE2qb4QQnpdwJwmp9fV8iczPubZZRFaNsb2iD2ynphpqpY4X6aqcyAx7NHG6-cdbLnyyFHSIAh8Ge5QL7aEM3UeCsv-mDUuC1MjfEjVVMh_2-rnP4_8i2loUVUnL9VvlGngbqnJLu20aeUGPnzuJmT9x62AzqpHuZM1LIfOG40j6e0RkAp2OtHxcY3P8Jimqw1H9r4ubsT69pKAe5NQ9GZItrri1ezo46wtOf606Rk8jmT7lF-wVDm0ub_CfUEAMDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQQ7rDUZ3QC3znHgPPFK9vpXwxjSmnSl-g8qhjvC-q6aUS6dKfVnLDMaTDNMykNkIcu8Rfdpn45Z5G8Z4NnU6HGTJBVqS_vYfHYpQ4-mZ075vuh3l9PcRB-D9xlbDM-jnBIX9ec1hXi1FpzqI4cdXadA39xcVrMjc8p4JhuN2V2kiVjbFZXH_gtXt3vRDBk4kM2PKP6NTYKNYCxP-0ghh5KgQx2vdkLTF4gw38WFKhBYRzejdOwfBdUA6KZyofwS1yd-qrKj5DgCpq1HHrB8MUffbQ1P75Io9zWUtHfANzzD9fJmtuvdrX0-0YesXxt9A8V027qGqJrrOI3UeGaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfDctse4xeQkE-hovGGheMkWmjnyCrutgzmSvSf4-ewXWmfdshuwKZsciSs2uvpu_WjreBATMg7GwMIkUrZuzmtcdGWIQnNHpEh5tAxJnV7rEndjht3DLiORQrgYNvvzMZd-eKMsotI7-Q7-CqHFR3pxIxw3mdiaoPMUIdf3yK5rNFvQ7qxgzJfrJlJK2CbLUBfkacMUbpjGv4gU5uFUrjWf3eEEZAjhUJlcBuv1CnO0se30x6lnx75kDY9aeaB8DarzqYeSrWLH3SCEGIkqT_tADiLvlGlQYB_-3lB7bxAYkM5C9Tx9ZxDDMKvZg25DvxBN83ZuaQn-k_qF7Dvgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ6AUWioAofUF_sWFx2HY6cWXSz4tkAdrwANW-72c2dYRHiqsj7ck69v509PHpMYTSQhKQs5-km4WhCEQQeYiL-CU6zBtHgsmpcY7FQAfxOm4yHZW0HWQY2GNFb1XhQEkjjVMAZHbs5MgE0OHt8yUBe--APuZ0EzflIGnjNizQOTaTlMRky6W9fBGIUD-e2KXkjYmtau6CGXDKiryc24BXuOPD_NitosetSshJMbsg8XGmu6JuZ01A31Ml5BX3LsY8oc5YeTVNzEaIzXUFXUoy7jbv-eCAD7YGgNMNnBu64DhG8FAtYzbVu8bxG27BmmzO_E6kOn6f2zJ74-Rq8-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl3HsosAcFYH5gS5lXyIhfDNGnmaIi6S2tFfCX-yTFd1hKtEaiyQbQl5scuSiVhPUSfedTfx6v8c6Zvr_iSG0wa-gg40clkQSv1DV58YYkhwZ6Tk8tX5xgYhh2umPRHYsdB_nABxsL_O6hoKtpEPJbBZnpFK-lOMTGAVxO31n5HdSEecYgjjZ9-QXATy3PSVfeJsv0pFXJ0_ot_3iinQ_J7tA14qzwt3vXBwgy1RwtKHEk67s6kuLNj2dK9o5MLHfBeaxoK_0mYfit_lw49zsKvcjPudcFvDtnP4QvE0du6ohohuZUQrERWkFvOZeUWKS-0nUXk6HWsKAiSp39b86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJnbHt_gp9Mblj8ZFZd07S8ZR-5OQbQP0X90ZRoHc0Nw-A1J93Fswf4oW_xhOvIxZJefq_Mpuca84c4BEHIKGbszPG1w6YVeVC9WYpKH3DHo52fGh9gYDkns3yv74a6x_sJBN_z02IYCPOhuQ2ODTIu_x2cp3D3DNhjeN_itN-OVlj38F2V09CN2L5wfkk1GTe8x6bzcnh7MqP1Oa33tS-nhPGhdWOmWdvRAVVrUC5-7xApytzotz4Ws0cpZ58faBAqCxvp_fTqX_t45qWRUIjXruLnM6tTP9g4d5fQzy7P1akk7RdmFG7CwC0LXElcOPsNNvITkUOLjNUywLQgH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFcQZhplobxvvPBEmMA8NtNaZdg1gBG-cRTrRMq1JC72HPoZV-quiZ2v0d_wJMgeBg2Tk9dEtIJWMprRu4rm-5ubrUaG040qE-KfYwjdQdMYI8sE0fQgRpW6ajIiT1HOFg0JN4u4drTXRnxyjwuV8pK23JNs5zQ4x0BMKPXyePE51Tf5FWruvxpahzEHraQ71aqUCEI7zPGHNVKQBsO0yNiV3Fhp5hX8qjIrZWq5seZpaVXmOE8XBrt9M-nCOMbTPKL8fAxkbGSOLZz2G2TrDz9xul6ynVltPIxytTc4Ryexbo9TdIQ7z83PYLuwb8Tr2HoDGRcqV_kLIs-ZwMNVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPXDTCBrGfVnQEjIOXs8OpbWwpoOpth2TijGKXvVCJh9dkOzP21O6SXQI_Q7pUcJuy7pMF9io5JTAKmxbLP0kP0c5dR_jzGP1lgCxTIIQSMvZKMSVVpFMuJRhMgeAchBA0RGzzSjDSuZaRFZ6_Kxk3a495ip1IwrwrwkgPqL37Gw6aGXppqmQp1CedbvpnxLCPxL23AXoBJ7U61NQwCcRizFw5QkyCx1sRgWiAJtDy0F3FTe4Gv48bLDUre3ekGwjaYJ75TIKorfs6Lo96PitNHAUNkMlSabCW7-1aK0NP7ISEOkNI22IEFsgnDr5jDTgfNld-7Vav9wA8qdokMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103186" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ovMbFwDuLwqZSARa-fIvumr1PnU9_DXvPhxSd7RSzutp0Q2NU-6_wMtQd_LsUfFZZz1u3G71OfSj7urY50R5QqgJ1ltXliy5EREjqnBPcOQuvzdLTMLOUxIRFCQW1kGJ98-vkkCgSBRLKkLFXbTkt7PHqurZPl-LmoLwTkeh8teNJ9NMfH5_L9XSDMvuNXk_uCPbudF9UnnoX-5Onflvib85PhvAmw6bDyqVYirvdP-aBa17VsgQriAtunvAmWJ9J3531o91QNHBD5pCaX54Mtc7WkgtzV76vxEgaViE4ZL925_0H7QgYAPDTVoi8NR0gq9HzeMGA8s7Vb__zF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103185" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAx74HTPwcJl-3yH6CcZCuWydHlQDM7JK5bJjJ-nsdMxTD-h8bsYomsk4RxS9_JSZBaz8JE84ZGyYlqeifmoR9U-lWMBkzuoKAP4nhJdtZOK4RIFC08iYXbC8Ys3UimVPT1aUDyjM8f5CHoHmi1a1hY1ONRmeSekKr2w2k5pa9ePwhNCM7Qs770gA6E_C39SdYnBl9Edq92zg3WSIJ-aF6-ud92eVFVsp_LzNl4hjZd8FQ2csoyP96WR9rqSQjBSQGj3JAb7_QBR6iCozFGfucPpaVa9RMzt8qrc5ZOHdOxJ9PfApt6jiQ0I8UuTHstouqDMs3DLiNKh4iujXSLR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuiEMbwUFY34eHdqbE-IQgAy3kIqgqu74ZZB2wsZRXxP0-WPBZANu6x9hLzGlajbYd60uwUDXRtdI2wszDf2bb8KhCFK0Ztfj-xArtRQ8fWJL3os_V9qn_xVMeb0Feto7PH6x1P1yu4ydJhYwOJXYBJRpqO_AEMmlyojdIrAB5QkoIpaLkCP9BHMSHCF-GXnTpt0odb7wOXVWIim-QoSWErZhTXkaPbn_hXkatD0SgZw9swI6ULoDwOs0RoSvkS1V78mIB8a3QQMClkqy3LzEC2MGKDKT-iJlhHBxlmnqg5H1IwhYdDBPJioRm2RBxCS9GR6DIe9jDIpEP0UV1q9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC0x5rT54DEN-D4gevkT-BuBM7UxRhuArJQqmJKzmXtcKy8QXRtcoQ-X_ILAGxDATAPEX5P-Z7WozCOVz5bCrOrOpe_aPV67KYJaVyKk8A881YI1TeMqeSnFdq_vcgJeBwqktqerwXwDorqkSadBCCiGYrRgN_c5GR5SkBfxrIvJoCGP1iuf2KGfQfV9JrrNNPVS0ZNqHVTismMwSW_ImKQ2DRbgaAmRo6Pk-jDZP5AYyL6NQ7kttY8JbwmCe0VIuY_o8FVTlrz4nCQQ7BdJAg-F73CdTDX4WCfkJIFT4Dul8VbGGd1RgNHcxhH43iVS9WhGxFxEMBgOGlBXpGosdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyvU6GuStavzjZlqNlT8LCxAPpKuk5eTWmWP7Nt6P6fmewbPYqxNUklURhc_f-vJVsDvXdYGek-G-pvmMgXLfX8yEnFLnO7liHiKIgiJQ9UJolzP6eKRuOhU2dZVJrdvWJv69AzzoawlqWOI0RLASLjVjleP75DhhANNMld7WcEeAwKXy5RCp5bT09E29PViYnnOjrBQyAUevO6fLu0CStcE7cOOU20lbcTVgJ_Viwidy8nCz4jhyAMSqxQ2KVZzWoSAgTFEwMVOdLkrTBkYClUDMI6ZNHKQZlouIqhYHGZ6uBMzevFvVwMnpb-sIN7qrQfadye1h9A8-BjLC-U4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چلسی مقابل دارالتعظیم با پنالتی مساوی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103176" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وسط مراسم معارفه نکونام برق تبریز رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103175" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKRbatB-o2F-01y1DBmc9iyBhhovw8hh13qW3GFjPdNEiGlnjEeSPzkUrn1zXLnkWSvfUNo0I2-Hmr4M6dqq2o_mGiQHathDC0M5TdEUIIKa9BJBHAdrf9rTg90naM7_T9R4sN9WN3TkExrS9AmJwgDPDqi_1CeRQwVSoSrJbvtejyppME2JyoLeN3PwNxN6ZXaRqg3ToJKEpmEqzXlQtz3X76x-kaDvg8OeixnBHhAA5xFXQ46nVGcb7ef9T5B1-z4yNH4Gc5MrIlpNYAsD2sI3-shMmPJOK5pRAcYDk9Mo6WF17EmAUPNszegQ5rXdhYWriPgWGacxsezf2SgtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه دومینگوئز بازیکن 16 ساله اتلتیکو تو بازی دوستانه به سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103173" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjHqXBDlf-9KkykGigTTVCGot1ZMEkLelYeFvd2gRQ6nhGP-L6cVOB5K8KPlwyBdZ3BolqJGFEDrudAJuRdv6Uk0L4uorC5eHFpk6tfrKZZQ8HoimSyKyXb-3y9St1i6XrOHz5tMhGtFgNS3iOHt1LH8jq4nVsMFMOjdzy90QBPLdWQk4Nh5GOzGy0KJPcEPTiqkqbdEY0w3FHfEzfIiv_xJH-ZTvaqLSMTz-wB_M2frz7CiImqFqzfg1VLg5qetwrz61RWkXIloVBXJUbLxHVYtF9R2L_RAAtT-TlljECJ3s1OF23LqTs1tjpwwz_rQwQiXkzjky-FGRkD352T2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8pDCAV-DOS9zpr1NcUxzGyu9dnl69EPeFbTiciQdkpm3eFd2k1xtALEyDrPOMYNfZw_XWDv-q3y00RTFtPvUfCnlyd3UEnOdBHHrd31AYOkwl1eEQBA4oqz3GtUOQxjkjcM-QK771UeSCLFEBawuv02HCe_S28R5KFOXFTdyA6Yt04DcZYqLGe6cvJ0Ue_GZP5AJ6dxf7AkaITpbNkLZiPmLCBjeOWGLrWgpoHNynLYvS5YBuJ_BHrwqiJYvzyZnzFjDAxI_J8_tclrQxBRPuzqpPi744O05jdkrZg4T2t9KUaqBFpWki_HCSkBBd6TGPMINSESRhyyrL5zMJ8Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN3QANWX6Y4IZspuGMIg1Cqw2s6-swU0iiWnerdC1cX_gVfBFMaRb6-nNLmAEUo4ZICtdeIO-lSs0C1VIUO-xw0PyosihrsM8gwgZPyMy7k9v1EzaaT4Hn468D80Tp5YtXr78jLzTSZyf9Fp7pNlB1KpldqXqP9Zi3yTmrf8E7qbu9GG-0XHW1n4hcYWskVrCNTldWcjG55u4SlGEuA3j_T7WO2dO4zM0Z1p8ttQMNXQJw7VSkT193bRL37e9TCmU5OqqNCC1_VQiA9xZRezpqLobcvOu6_N-h--e9SogBWvS399c2jhlENIb5eNT1iIPjC2cs5QR0DzlFmHk3ApdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB6sbYtEfJZr4aqcJNaWSi4lZRZ5p1Sji5RsWhfg9hEFmXAxghXi82LECIr5mpKhE51_5yMJy1g8YZzlbZ8-qCFUPaTfPa3R7m_iUz8qtJ_KEoqLCeDrzQUHD-EFksFfr7HSDkuXSpIyUEbK1hHyOOFXiV1jrFWizc_OvcqLgNToWezyCyNi59CEkHSdsbBaXZNG3jGDoVsWyn2_N210-Djj7L0Q8yXHh4QBKwgf8WmHe10uirPPx6XvktaCN8-Nz4m5dCFvE50EEfwaFavRGGucKLPMPY0e0Q7UC2JrgdTn4I4MmwUGg1JYmf9_svEg53NsgUSU8V9uQuEWbtW1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5F4M3NX816YsdtHJz-G4mSRVJa4n1Vt1IA1l_hKS_T3eXle7rJsdMu9x1nFA8FHv5bcILfDRUbvhFEqgnONyNdoRhnyf8_f83FwHvA0NIuRizDNmo-o1O_YEBfs8YavvdE5jLnGAQcWBVtUYrE4wErCH8t_vFof03ZB828PShdarNIwLzShFyMqPrLoNlIMqOtNh_zaJNeTMKIsJBtl5Yi0Hy4y5ZY-JfKbepRLLfR2oo0-zO6Oarvlrkbu5CcEuzRjXhcOWkLre1-6OT6hrqYLaunFvbBI7c98orAc1WB4YfTx1KvLQLDDvcnuzOC35XCmk4uPMsqbop914JhonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103163">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRDtYPowlbrdvoGimkTm99fK88Cf5JTM--XbVhg7TdleMm_l0j0lN1Ej3WXMWHVRgD_60QxsellOENCvH8Iv4X1wfmNrrwfLWuZW5Z1sJ0JRrZB8SAxzo0m-6irumEYjMAZOLWLVlhVPu_VJAHl89dzLBTogOxYOBaDSvFwJrklekCK0nbz4XVGV1aENckTs3TBdyIHoOmGN-dcEXu2_XiY2FH_u7X4FsIi0-hg_Q05a0VFKD2wN6XJj6756_ycWTgyYm8f0cAI2a2lbcGOQ10Y_pYmK_qMjtCVSIPRD9Ox8OQ-LaRlpBqNhVcUbs_ABDfLk5hKTEqfqPAPVRaTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آرائوخو وارد انگلیس شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103163" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103162">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVYxjH-gejZ3pd4WaEb3VRtQG3Fg0UN9riU4mbCNuwPL_gEVfH4Cwq23DwnkQt_6YaSrRClqjjFjlSzzo8wJR8Sfr-zf86IOcLBzXoFNTRTEPFVY9EmQyNID8gJUqgDCtOE3pBPtIl739uLRCA4JbhEDNm8BEedUy8KPlw1GjOVmGrbj3goOfEHvCSShUsGuc5AsS2z0ZYlq2nYCQg7TeU0kX4MCXZxN5-E8HcYilK0vIlgrfidGUTW8B0_b-QcmmVQ9kYrmFLwmZnjrNMLgRkTCfcXcL1cy2OrlzL-SajmlZf5QUSKpC719OPEtFmRyrcwZi_XbP9AcQjIjnXu6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
هایجک‌های تاریخی بارسلونا از رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103162" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103161">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
یه ویدیو کاربردی برای دوستانی که حین رانندگی قصد دارن ویدیو بگیرن و همزمان موزیک گوش بدن؛ بفرستید برای دوستان ماشین‌سوارتون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103161" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmF_DGhb6m5u9AiHvms49l2E7ogfjR62Iu0BSU-KntJagcw2TLSfK9ep2-eV74sVh-4ceF2F3AN2D8W_mHMwzl2iVOEp-SWrNEVKoaNDTKt8FF4rTg4ab1qxk-fI2KFypCyA0QD7kDsn_tBAv76zScKcvwxNj8i0T67y6Q8PSmBBBs23hW9jy_553RgotrFeQ0mizXMs4O359hj4OUDbfwIjadq7eOKmWxACAyHLWIPWMl2Z3qjZ933iqwc-VGzfp4oFlAyKcboVtnWBrmS2I8zysCfPiNnjMgpnrfF_jJjIJpMiNF5UMQO3gBHRv6ub0TRhup4-JBoHZMInaEV5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuYxYB757tUjG0Xmy6G3cbGaNeWL76En0z_dcJtL_Zxlq96gSQtDsqYy9ArZ4PKn4Ygk0-gPqKBb-hwtFCizB794C_KrdzINzGaIXHs7E2fSOXDTYbpx5jD0sZ2HM6eaYVr5UEWwZkb7hZntLE54d844_C7b44mN7lFRsBeqHA07rxvaosWD8cgYKzwsePv50L9aKD_O5RHZUN1ujFqq05VHGM_KcnfWVb0lhUEgaxmBrHU8FczAvM77kTo_9iA2dxbFNXeGYvZVNAUbwvzPzSYydSQKfprTh-P-gIIAZw59_GR_IaYF_zl4VgTDyR7yJvp415jvp6yJ-j3etH6jmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
ترکیب منچستر سیتی
🆚
اتلتیکو مادرید در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103159" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=lkUllnGBaaePAekI5sonCVzf1_u_4sZgOj_P2W_BQQXGd8TXm98Yt5pLLetPGsdo99nG_Ogzvqj2g9kdn8_Sc5nNZYw9CeHJxV6-fKR2DQZO5LbCtd6bfSefqqcJcd0Onz2RlYOhUAleVTIIgxFRR77Q_n2NTcPRVpABzjyth5-pvhzLXhyS8y6K1C-kA-IgmypImUVD6MNr6yToz_cTz73zh0cobwDcg5EuXYHJHRDnlPbci3KyXvlJ3HEcT9Pw0C604PPgRKaBiOxavvhd0GqVHLcxek2mycTEWYROgLdyFVUJET7_dTu66aymgjusgdd2tq_Q1kz_j_JDaDDc5xavU0MAe045T3zVRlcFIcsmmn-brudsHmu_UhGtJ0hbOrUO8BGLISlNx9y2gVvju10rH6vhgyjTyMMfatOTWpGPjSUyU6I_oZ6_9Tt54cqzB_lE78fUSp1-maBA8WRQ09z5KdSv4V0u9aKU7FgWPa5dC46riLFe2u881F_oBwlUAPgykIh8PrCNpIz8Y6iDH9wnl-4KvHyUbiN9A4y0XJ3iwRutksnJjLepCGLt8atr-bUrclja6IRpmYG2cZsBR3eSq8JLmFEXE1OeoMpjUmFaTj2tTZM1zBUtfobEk2f0PQoPYT-2nZxMzrvEkLjAEicL95RDloW4IHtQIgKZ8I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
⁉️
بهترین گل‌تاریخ فوتبال از نگاه امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103158" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf4e624Gi2jHs4S6qgzeRG3hsUoZBClbjUTn9NjI3OfhI0pEISTtFL5DGORZyavrDAfsCFe_2EJicLlQ6pFuFfJWpP4GG18ly2dVReoxCVKZxGy0Ogq8A7eTcrKsAJZlGou0iTTpFhl3xu_eMuwSSKQb9i2rpSUDqSZBEg2C8I9wgsAcVx6Flp2wbzjUqzuXe_DroWeRcXP2q4JljxLeDJDSDE0jRgRoVlW6D1Uh0CSxTca-xkGN-ljlSB0dSdggGTojMMfp4OZdNwPxxl0nYLzURzPERSHXjy9j60wVGAxcc6bLYq6kmnycHA5FJvCy_CrDuEVJ0HAM2Hac1cIyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گستون ایدول (خبرنگار آرژانتینی) :
✅
علاقه بارسلونا به جولیان آلوارز همچنان ادامه داره.
❌
آلوارز تمایلی به ادامه حضور در اتلتیکو نداره و احتمالاً دوشنبه با سیمیونه صحبت خواهد کرد.
💸
بارسلونا آماده‌ست تا پیشنهاد خودش رو تا ۱۲۰ میلیون یورو بالا ببره.
⚠️
هنوز معتقدم شانس خوبی وجود داره که او در بارسلونا بازی کنه
📌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103157" target="_blank">📅 13:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=i7zaqTtm8OQsTm0Y9yvJvbh9XQ9X6_Zxk5qL5JuxDHoL3iyBye-Lw7UnGU_zAWzMwy2tGwNn8B-qaQ0RKSl5tN97UyVdtowqaxB3Kc3SE40Y8g0qnQqmj2CAeSPB2W-qbjH_aL8w-MZ2Gg4VjSNmts5OJAexDXfGBXl109Uq8Q8_4TraEU10UHBjzDlInMX7Rgakzj1yclXUvrd9cUYWuZ7aabFTM9JEcvYouy_b-2j5CDZ4_KKDRVr_xkWC7OnlFL1QlZKH_ngxmio4cSOq7C9rcA4iIW1GeOCqaYdSnbSVkHaMEgCNG0o4f83yZ-VLd1w1emB45ORqfFUUOPIZJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تخریب یکی از ورزشگاه‌های اوکراین پس از حملات اخیر کشور روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103156" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3i2XhziiZ59SnrW8wanlJLalk2cmVpc627fg8o3uDSfZ0YMbjM98Oc-Cs0JJqAovQoKSUDZp_IhXYe2SGg3JfAOmPa0lD5M2ZI8Mu43otZK02WrlnjQDRaT4J9FGiV7nWw95NmzpZJzGaPhNLqBozNM4gohgqKfm3Zkcbf04fm5QEnAoq5N3FiS9QqDLh0dYdnbRBA1wqLAsKeSfUfl0nHij_op3mr9Gh_zEeZaDiNsBLu6pC7Y_IZhTh7jb_tSilSZ92T5OBmRS7wupbAQIVKjuS5a3g0MaiT-8r6Bj-FsIuInK7YufgO93NoX2CUGT4_sanUTDU8uds_gI7lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیل‌مالدینی با عقد قراردادی به کالیاری پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103155" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMXhNSok93UIaQaEOM_N9mRMoNx52BG0AlpuaDUvvzE_7q_MxE2TaDQVZ2yDzh0DYQdZ5LjuZBMJgbMZ0zSTyqGnWxKHk-GQN7GfqSOVaUpAxWvGqscyTtgEmh895MfzO7R9hP-GRohleGC_IkMmVaSNPByhLApAOE3_TiBKMGxPFhMKoh1hFcT_8ZYH_ssVJuD530UKvohCpIj4EcE-U3WB6QhVXY5Bfd45mh0iWGGhpCLKDFdh5BYUioabKpaeLq2ikP0ZRZQPK_CO2PwF5lp8p--K76XFHY9iTQ-MnreqnmHKZTLj9B26cL9m6NGu1C1yQukKLX5EzQBu--xuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
😳
😳
ایران مهد عجایب! یه مرد در طول روز، زیادی به خانمش دستور میداده که براش چای بیاره!
بعد از یه مدت، زنش توی دوران پریودی میزنه به سیم آخر و وقتی مرده میخوابه، قوری رو میکنه توی
کونش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103154" target="_blank">📅 12:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103153">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoJtC48a3himsg4LHQZHLKnHsUu7oIXXs9OhXfF0S6dIKptBCctlSyO-i8ldM3AX_3KOA5szoTBlZ63vEb4OaBzm7b_GS2P-afQrbJoMjkPlh3Wy-DaqvL1irfCNSfNjy7m4omwZoJSG4IZzS3gyVEg-GlTg6RAWE5RgfGlWsqpcb47UvOrCu1mFcCFcZjfmjFPWroJb8_aeFI4MA0Mi7noyGo1tl1bRWDVo0MlkeS_zVgVNx7TNtJB4RG_GnO7p9exHg5h3qGrzBBwDUWwf2ZJ6url1w69LcIYDse8cbK6b_TKJNXFF6p7Snjns6wUdJFtl25R_3G1X8e-SUDgJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
روزنامه موندو دپورتیوو:
❌
🔻
اظهارات سیمئونه استراتژی بارسلونا را تغییر نمیده. هفته آینده برای مشخص شدن سرنوشت انتقال خولیان آلوارز تعیین‌کننده خواهد بود. اگر خولیان نتواند وضعیتش را حل کند، بارسلونا سراغ پلن B خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103153" target="_blank">📅 12:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103152">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVDp3B_5R5mCIPyxvv1SiOLzIszgtkNgxgY8LDBZSO58AUk_WBWPWuZ0PbP0JAiB-g4NbEljYOvuEf6vLZHaPx4W71RLzxQgRd7W7xvKF5yp9Btu4dbkeARAT8aRf5U4UD43eoH-Dg_1k4P9Nr6Zn2pHqVIjLKthqERpv-abcG9CV4PGFsgESVxLYwSkYSfrGuaHFhg8dIL_PgaLumDv2XOZbq2Erp6m6qxFkWkCAErU3H2B6yg8HkIWMOI77mYh1nKfo_QNuGxXm7Q1vMN5qWOstoEamuNMYMO0M9FcueH7k_SlHthX7AZ5jdRTv1COWVZ6TcFxWVdpXvFrivnRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
خنده‌های حجت‌کریمی و جواد‌نکونام بعد کودتا علیه محمد ربیعی در تبریز
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103152" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103151">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9cB75soBZR3a7wEF1Wd4-V0VFbglnjGiUaHvZknOhB1Md8G8o_bof0SDqNrS0CY8fWWL3LpCXwIKBxDEn2uirCufXg238kDrQPcKYSEySJsAwyCNKCXzx35uW021lnKvduyTB-pZDVmACS8sLNMR3mbhqccfCYGe0kz7bKJDj9FppkKPfyfUVWen-H5n6N3BFvxio5JjmFdpbI-L7qpQt5OwB6zT-eZ2KGUNblHp4N8fuJdpjqYds1MZfK07MvXGEYFpQTiAwabLywf6ROwBKDGe8qtFEXjyt0FRgAd6PBhp_oIzL9DYLLHFf0Xa9M5dADxlnA-MBOpesnxuqt-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۲ سال از بازی منچستریونایتد و رئال‌مادرید در آمریکا و حضور ۱۰۹.۳۱۸ نفری گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103151" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103150">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103150" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103149">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWWx7iWig-cR_mhfrVAXbbx7M9o2Uvcx7Cjhv2PZrO7MZQRgsR3QkzH2SFv0RxcyRZbfJp_V-0c28JX6alQYqe5uEejBWd0DzNiIiE97j5wSsptJZ-ByQdoWAKdAoaz3yYzQRBMUKGnxnexLnShx_E65w0FdrErN9KjL-ZqmOmZh5OpthgAGc8IQY6qAkwvjb739UDN7H82zfv948dWacyAJpvI7EY2VUE5k9XYjIoOxEfDfy8ZF7vBfDJaHoHXy5AgIgDW8-HEmXyhseHP9n_nQBT8O_f73dEWiYzTsE60W2XWFKLEJrXZ1NcfCwSJOiyIliCepa01BrxHaQQ6txA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103149" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103148">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یکی از جذاب‌ترین دربی‌های سالیان اخیر منچستر و تقابل پپ‌گواردیولا و‌ مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103148" target="_blank">📅 11:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103147">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh7M0x--iXl1GVOv0hohUwNktEEww73Tez8gZ7vt4bqVr2ZAemfBZ7UYX2fahK3rq_UafUCb-4L7_FFJ3Oz3BN-9-MM5a2-W2l7_fQS-bNyy3Hgl2_o8NomVBhbldVnBF2fN-olag5OU1yvA3Zke7lgWQTddR3xoa7WLwHwa8Mk-LadbzHgcmoMFdJUAe4gs5mTNCCy-lcOH_rA6ow3TQnglXpUv9kCwvA0mx2-zLEFr5v7gDaQDXqVBJ0GgoFntQMF0olzq3YtxotT9jWTOZTCubN7xq0gb4d49H2yEi9lMN3uMOvumtDTqZCaN18cTp-MtqQ-712S2QNE_wsMHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
فده والورده:
من انتظار نداشتم مورینیو این‌طور باشه. او خیلی به ما نزدیکه. گاهی اوقات سخت‌‌گیره، اما فکر میکنم همین میتونه باعث پیشرفت ما بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103147" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103146">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=Vb-WQIzb7gSQP-BDwePMON-iu7gcd4R3JHkeVJAay550CGvm-qjxOtMLF7txsRzwrX8FqPhtEfkmxePoaTPZ94xnJ_6nne3uDRfoffyMcfCmiBqr3xO4JKDBnXELQJQGJdxs5Ic5qU64DUFVclsPLFsq1T5fViRz7I2u8qd2cTURq-HemKUdn7ejdo-5j_Hc_K0HG05MSIfUp4XkgC6eZC3jNU9R5QmSctA5yyc0-vwOFjpGHFlVMIH2DLATS1JvO7B2ydTkehDBnii3cBEtKM5PoaV1KaQXjhLivIyH4gF5FHgCP4iCovLBgqD5XRA0BhL58LP_ZRpWYgQRxa2leQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اَبَر قهرمانی وفادار به عشقش فوتبال
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103146" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=t7LdwZTQeNdGAI4OQG_KAVJNX-cqSvlCvFXvM9B_iXyu9F7TsTNJkQ823fBnxGm4gD1Wg1ofg8h4GaipWr7-6Yfw5zhF7Hzj7jZvRp7LclCgvNqE3il7CcDYj4K9rqJMai3gNWyzTMy3CvI5rhuSh4TpSEYh7cUHi_VSlhUxE_HyTKHGfqdDHS5NVWvkiPj9eWSJhcm-AsJN-csjmrLacoaEMx_aoZSNStAGDH0Z--10VWxL0cQsw260WvnX8qlXlNuy_TzG-XDgE1y7LctmjPgeknJRO_Tu99Z13HSXwaE5bwCTbDnw-miGTyy9PV91Z7gclLWl2GcUOMOHfdfLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
والیبالیست های بانو رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103145" target="_blank">📅 11:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqSgYhnAaSVIN-4RQobCHqw5sbzDefvignjHd9PfchZL5LK-x-MTpTCbC1T4ZNmQ7Vh0nEqA2iV872WfStTqhz7gNUJnYjaNN2D0jEVyvKcMoHFSXcNR0IT8x6Tgt3s05CXssQPjM8fdI24e8iI9i0_PXFUdVeAFuFAg1KXyXgK-2Y02SlWwTcZgIDfBiqI62ICISXPIbhw6hKllvWv0Fe2L_I1fuKloAK8018qQ6v1MtuWcTfHmJe9saZ38VmhQS-F04mnCw9PbpuTOhjS5Al9TecdFKSUHCMRN6BVGcsJsP3xmGACX1UhrhxzrjiI3yE_zzaK0cUSxcamTEh9yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینزاگی عشق میلانی‌ها امروز 53 ساله شد.
🔻
فلیپو اینزاگی انقدر تو دوران بازیش روی خط آفساید زندگی میکرد که عملاً آمار افسانه‌ای داره؛ تو کل دوران سری آ 300+ بازی انجام داده که اینزاگی دقیقاً 368 بار آفساید گرفت! از 125 گل رسمی اینزاگی در سری آ، خیلی‌ها معتقدند اگه VAR اون موقع بود، حداقل 30-40 تاش مردود می‌شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103144" target="_blank">📅 10:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103143">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=rGuGVkXgEx5R6KdaGNya0gKMbU99IDH0HRqI3YDMilrkuzalHfA2ViyRXcLH12OMPzYbZKQDrSmfgqdPgYL_rHyJynIgGNdu8lPgXMJZPw1BO5HzCtL8-6DaXh399970ni9CuiX5vLPdwY9Q3KSnsxOy0KA6dy5NkraS4k-uy_eeJ6ww1gk_G9QssbF8yrWixz3N3FLT_QhEj3_cQqF-nZZPjYpPhwdwLWUmENMN1Qxbz4YNpABnzc0qyIuCbzgXHfJZQ46l6UPYOaU5VbdHyYHzug1mnOEmJTpOzoNK9qjMd7bMHt_tFgJS-OEetqhX4xiFjHdv4tFXoHJw6S_X2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شغل لذت بخشیه واقعا این فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103143" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103142">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=jrLQKwG94GW_k3_36-HLThAP0hRDtoSoQ8lWKFLhvLVvJT1p0Yq7qBB8Z5t8iO5W0kqWzdCp_a7y9g9rx0hGyGxn-g7ht5H3Gz8ybjBkOms4sEEcx9VsStwGuvpwNkP0ETW2PwqTNWtVfW6qRzYoFVgIWFx6aC_4zNjsU6VIC9c-rNuv_CtuWV7ZTaEBrArISExc06NaJz1nHOh5vSvl8Xs9jsUHSMA_ONtpMwsX7LVeukBQKjjk3uapvk8q_9TOU1Hu-DsHT8HGISoNAqnhHHB_X8sth0xL2t3lVL-QJRbd_3cl8gK-vc90LuYiehvgfIy9XGU7mHaX29YsCUMSh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=jrLQKwG94GW_k3_36-HLThAP0hRDtoSoQ8lWKFLhvLVvJT1p0Yq7qBB8Z5t8iO5W0kqWzdCp_a7y9g9rx0hGyGxn-g7ht5H3Gz8ybjBkOms4sEEcx9VsStwGuvpwNkP0ETW2PwqTNWtVfW6qRzYoFVgIWFx6aC_4zNjsU6VIC9c-rNuv_CtuWV7ZTaEBrArISExc06NaJz1nHOh5vSvl8Xs9jsUHSMA_ONtpMwsX7LVeukBQKjjk3uapvk8q_9TOU1Hu-DsHT8HGISoNAqnhHHB_X8sth0xL2t3lVL-QJRbd_3cl8gK-vc90LuYiehvgfIy9XGU7mHaX29YsCUMSh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
هنر جذاب و تماشایی زین‌الدین زیدان در کنترل توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103142" target="_blank">📅 10:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103141">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_vvj3xtJEmoHOEiXkYfhVNW_NojHSRvUZgCO0al4kRO0gn3m3nLgMYWM7WacZ-i-bC0X8HwYhtTDGqj7o0gs-NG-K4K-P1mr4NxsSU_l21tr6OXf3b1Q8fpv6IMeOYBBHVGkjIAttc7BdQDoA10RBlu-Wps7B3fJ_Z0BAAmB-ISrBb1CytIeyIyIi_IS81vPb8yfoi_8sQ4GaDXGTbdajL8oT9x0KXmU4682nG1mB6SLBKQcvT08wcEM_6SjBvr7aGkwS29tmnRwUY-c6nilkk3iH82s8rdnyFI3NhxuXRCd4C4DJIz6gez0lt3dNrFpG2nbXBN8B7g7pUYlIm05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو: رونالد آرائوخو امروز راهی مرسی‌ساید میشه تا تست‌های پزشکی خودشو با لیورپول انجام بده.
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103141" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn3iY7zbfHulAWZlvsT80fR-n2uvdqxr5iLe82bLcWIcEPWSkxcTPJiQX9RCEbE6VYleDlmApBrJI4TiZdCVI8kuOvV08DzEXCjMWKbUl-1rbBNC961lojJ0Zunxih4wWrHwwKoPfkTQBrf-Tu7vn_Ac0Ro5opqBOiFhVYAw3gMHfpUoiTweX1hN3DlDqutF0zCdB4XiiRUFZeoI0ooFl4GpuViA_m2v7rW-OaB7s77oMbigBLWPfhL1TddNbZhx-JpbmnNIFkdYPAsO5JUgAF8QMVn3_eqL1KhkDJWbJWoeU2Hm2GMRW0bx2awyb64igWUNFuVb82ca6L_wv0WWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
آموریم با میلان هنوز تو بازی‌های پیش‌فصل هیچ بردی نداشته! حریف بعدی میلان منچستره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103140" target="_blank">📅 09:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رقص معروف لامین‌یامال سوژه عروسی‌ها شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103139" target="_blank">📅 09:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHOHMKSE6iD6yz0f4zB2v02utv3VmjflRaaL7TJIpFZg_KY-1eYzNzsjYFkAwY-nZqBA-eD093Zvuk35rKDlQLEPJ3HscPUGqnlj0ds-W7y7vi1QYsfcao1hxhxZQx8Ia7Oqtx2O_3_o1_7_xFkXinbWFQVc8N0x7-Me96uxj_m57_ah58lfBkXR523KmZkwKpYaiwlFvS-uVA5PNIx_k6o54yredjKa32Rdd3fH33OsCw6yIgaoXbx_3M_PbqvHVJOVmV5dOy0A6aT8eTs7OF3Iz-foFefabbrAsu1womQ7DP8pCE4I6yKlhDZAJ3QCNyisfpzpx-RfDFZPUXEHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوووووری
؛ جواد نکونام به عنوان سرمربی جدید تراکتور انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103138" target="_blank">📅 09:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR3OZ45RTN6ry0V31xjzRz9jPObINSF5h-gw_5EWbPHpJ4agtNDJx2Ai8sIe3Cj7uIn1un5kLtOXUdoJ4OABfySjf9i9gSm--L1_RM4nvFHLszS7V9g6CG0Nq3j-fZ0YD-kris7w2Put3YAWx-8OWaRSUQYkuOJoGgrpKSqZR2iMqCA9pGgwaatPihpLyiQMUms0L2p_3OZ-9UALUPeEyMltyNCEcuso8dqe1JXTfDni6VBtxpq3gopDtsd9HZH4KXSE_BIFgPfcVVZnnPSnAjvkovS-TK5Eu_yTkKzhIxEO9J-6JCoXbBS4d4XWCnz2v4IVF0mzK2OonXlJxWKElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💥
هرگز فراموش نکنید که لوئیس سوارز چگونه فصل ۲۰۱۵/۱۶ را با شگفت‌انگیزترین شکل به پایان رساند
🤯
🔥
⚽
⚽
⚽
⚽
🅰️
🅰️
🅰️
vs Deportivo de La Coruña
⚽
⚽
⚽
⚽
vs Sporting Gijon
⚽️
⚽
vs Real Betis
⚽
⚽
🅰️
vs Espanyol
⚽
⚽
⚽
vs Granada
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103137" target="_blank">📅 09:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730562ee98.mp4?token=eREPAKGsTQZDBW0LaSdAYuUflnkk74R5Xt585Ov5m6RbSnx-OXkwlNKRZKn00zQeYEDIoIkprHzyM7G-esxY-UhD5SI6vXfo0SfIVjfkYkDQUtZx40CyQtEP7fM_6Z1gksPF6t6flDGo2TXX-ACh13oMaea8nAApRd23kRiczWl2c3tO70IxhBikfvZaf7Kmb_vPCKp5PZcMNuxQpVe6Z9gpGivj8EkdgqXbvo2MdXNH2K2rvNMNOIxO34yLopINv-bG2JmLnq1zXWwEj_IsAC5I_0P2mpq6GwZeTyOxPJ_0VvlocD8bG47_DqxQMdM2lPi0kjNAonTlt7ikc7_fIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730562ee98.mp4?token=eREPAKGsTQZDBW0LaSdAYuUflnkk74R5Xt585Ov5m6RbSnx-OXkwlNKRZKn00zQeYEDIoIkprHzyM7G-esxY-UhD5SI6vXfo0SfIVjfkYkDQUtZx40CyQtEP7fM_6Z1gksPF6t6flDGo2TXX-ACh13oMaea8nAApRd23kRiczWl2c3tO70IxhBikfvZaf7Kmb_vPCKp5PZcMNuxQpVe6Z9gpGivj8EkdgqXbvo2MdXNH2K2rvNMNOIxO34yLopINv-bG2JmLnq1zXWwEj_IsAC5I_0P2mpq6GwZeTyOxPJ_0VvlocD8bG47_DqxQMdM2lPi0kjNAonTlt7ikc7_fIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان یه سبک زندگیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103136" target="_blank">📅 09:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhFLwIHzo3z2F_R5IbAKBB2US2oIMpNphis8qalBPnD95MJpQwB2_uji9gWLks_6wsREde94FXUoYHbNkHTCiiqy9lCIbzYAfObHDbBdcCkv3AZMYRFnk36oRYR5mBd0UAkksO2QrKoqEIJaAvMZHC4I2Jj-HKhl5FhZ_5Yg_orD49uWLUp0hbE1Uku5p7Uaew9RCokB0rLOSzqKQ0KR4L1ieSEhgI9tHVsA71gHtCcarJIUY1xNGabrlhbSF0ZtEfn5STX3wSITnT-Vhl89oEo8wKoHOiRpKAD4AzOEEfDrOMmX_DDljsR4cJbAy1D8jxUU3oKYKY-fbIXBOwSfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره مسی هنگام ورود به روزاریو
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103135" target="_blank">📅 07:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ejjDEIUMdJyMyzKrdXVGOfctnkA8Ptj-uJ134SjJTuUOK0msjNYw1G6BCvZ8B3zj1khw-7C3U_I216HkOb903_ENj6BnYxjUYfhXAS-D9I-fu56TqER4WsuZG4bQVMf3_rjuCZWoP66GXzkpWhQw3Q9_IlJeZN7fQ_WJDgJL0L-4VlduV27epOO6qRLTGTKw60lOxtI00CLBpzjabc6snwJO1jSBiV2ZN_HO-l1fEz2RcmpOAKAWvX2wgoda1BMXn0LpVcsVp_VIZ2qgA5boQeZZycW9McpHI8XwB5m6ZYXPVdehMmk5Yvl5R8kAW-pCWVcm-BTWBhZ11OvbM7fIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ejjDEIUMdJyMyzKrdXVGOfctnkA8Ptj-uJ134SjJTuUOK0msjNYw1G6BCvZ8B3zj1khw-7C3U_I216HkOb903_ENj6BnYxjUYfhXAS-D9I-fu56TqER4WsuZG4bQVMf3_rjuCZWoP66GXzkpWhQw3Q9_IlJeZN7fQ_WJDgJL0L-4VlduV27epOO6qRLTGTKw60lOxtI00CLBpzjabc6snwJO1jSBiV2ZN_HO-l1fEz2RcmpOAKAWvX2wgoda1BMXn0LpVcsVp_VIZ2qgA5boQeZZycW9McpHI8XwB5m6ZYXPVdehMmk5Yvl5R8kAW-pCWVcm-BTWBhZ11OvbM7fIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رودریگو دی پائول، گل خودشو با پوشیدن پیراهن مسی جشن گرفت. لئو مسی به دلیل فوت پدرش، خورخه مسی، در این مسابقه حضور نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103134" target="_blank">📅 07:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfkBmBhifiatZ2RIKZju0I0D19l9CIGsgiYDpyR4FJB0OuKbp74jdtdtRRpSVzXByrZd5BIuQ41s6aJJCCAtr2MdKUEcimJjvtk0ALLPPGdkpZwiRPX2sDxbAxiSNkXqM-22f3U4GcAfSBy734BYElu98Gor5G-xRg9v0ndoSJgk8RxP11yFmAbsjoMiKFCoTjGdhpJqhCR4tKU3YpeNE9SzOOn_S-7Y54CbOS0Wz5C3tmhCgJ8UpQ4Q8kOjZWB2TvT-uh0V84NMqsf35n6ZJ5Jq54zlmj7HI3aYO3mxbq6tiHpG8u8C4h5-IHE8tUNkJOzQ4Y1T7rcEMQh5ivu4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اینستاگرامی لامین‌یامال
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/103133" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=solEQaath5pfdYU1zm9pCz7Ai6cx52Plca7FAxeAfNnHdoG0DeIuOTHux5iIFEmELxZmAazEUJBMkQrJbusTdh-oBxExcCrm1FtXB3oa82v-YvwdkpfJ1R0poySI2OT4rq80Cuw1vgKhu4sK6i4Kn28oYEdsG56EGeB96K1-orhjlxxeQHcgtOHWhA67Vz4FoK-cdmPIl2wdBIJfEea2LSjTRQQRwGltN3-I10lyiuzRGNzVSFdEzpijW8rjoMWi0UrGMNFPZFBPkeh0N9ECANpbhou0Z82zrHXMy_LKX9-kakGr1S_8PjbaMru1uw8lrlUj-bDc2MIUSj7g25wHMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=solEQaath5pfdYU1zm9pCz7Ai6cx52Plca7FAxeAfNnHdoG0DeIuOTHux5iIFEmELxZmAazEUJBMkQrJbusTdh-oBxExcCrm1FtXB3oa82v-YvwdkpfJ1R0poySI2OT4rq80Cuw1vgKhu4sK6i4Kn28oYEdsG56EGeB96K1-orhjlxxeQHcgtOHWhA67Vz4FoK-cdmPIl2wdBIJfEea2LSjTRQQRwGltN3-I10lyiuzRGNzVSFdEzpijW8rjoMWi0UrGMNFPZFBPkeh0N9ECANpbhou0Z82zrHXMy_LKX9-kakGr1S_8PjbaMru1uw8lrlUj-bDc2MIUSj7g25wHMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه اصفهانی که قرار بوده برقشون ۵ عصر قطع بشه و نشده،‌ زنگ میزنه اداره برق یادآوری کنه که در ادامه این اتفاق فوق پاره‌کننده میفته
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/103132" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEk2ZXdEQcvCtkNReBCpa_nWgXxXIsUVUPmpUzWw2-M69Fxu5B76HmYNNt_YtIT9i835t6jWx_Cdyn9sDCHIhIs_OgwsTb6BV2mq0Dpq7vmIVA0HPTnpkCslAvAEF-_XkfIwGntJbggYSjWtdHQLsFz4Dm2BIbdFY-HoyEScDI9iFaw3YWnA1FbrxL1yGUbk885_LU2HHOMercxXLkcbiZ0p_Cn61GCH3Yvn1ss8E4rdGYEI3o5senswk_mZL7iDr5kUvnN5jkfiCLifhNSaa8mwuAN4jm00GKdFOGpNbDVZUezhnYNsNcg8KgdWSLU5hMEnHNasoIM1J-Fl7mYXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیو فیس و این حرفا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103131" target="_blank">📅 00:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrru77Ipq0AZp4xlxs6-eau9jxVmftTDJj4jwHdMnamgLdSE8xFxFleA9jCeKZyZrLoiekvtNWnAGhotN9NWMsbYKsHU2LDkv4J_oN--1ZUJARoWpxlhwK_15GOOhaOFbPHIFaNgO6dIgPJfcqv6Wc1AnZIK_FWH-NZGWpC7TID5b1L62q_MuLSakoUMS8nyrCF0mFQzrr1YjY2l-tMMMPW-ROWyOaoLwltHa9mXOTZtUoi-VkT-9FkJZikyLz5p2h7ubJADde42u6dPaTGUsAoFNQ0dbDYSjNfrupBxNfhguPHEOyGIMU_6rqqjLb8Pib7S4AQyHYGMgkzDu6_6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
👀
فلیک‌حسابی کلش کیریه که اولین جام فصلشو از دست داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/103130" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=FLNGnyEhrY-KyTUz1Vot7rDIx4YQCq9B1bwGwSV39jisIo95BDVzglhoX-_IBxPaUmb-Jjb5FUgpDJZRBgV-crHYpgkzhl4hFupL53ETHwlqot9edCO_HYrJSPmbPqUkwNWk6i4dcRaP3Ghc4vlu5IG_4P3peMPF4Ii6Hnzu0QVtcCCtW2sUV6e-gq4bOINkVMrTuDC9wLeM6eRR3uQswe2VfWNWjyRguIxQeGHKK7nnsQkLORvjzqhZV2uBV0nW7R2x8iB2Ku8V1zZreKCRainQJ_rmx0nI9k_GMWTtOcAi6N3toAnuWJd7c6yRn7G7mVGB0CX8HrZ6nd7HtHTfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=FLNGnyEhrY-KyTUz1Vot7rDIx4YQCq9B1bwGwSV39jisIo95BDVzglhoX-_IBxPaUmb-Jjb5FUgpDJZRBgV-crHYpgkzhl4hFupL53ETHwlqot9edCO_HYrJSPmbPqUkwNWk6i4dcRaP3Ghc4vlu5IG_4P3peMPF4Ii6Hnzu0QVtcCCtW2sUV6e-gq4bOINkVMrTuDC9wLeM6eRR3uQswe2VfWNWjyRguIxQeGHKK7nnsQkLORvjzqhZV2uBV0nW7R2x8iB2Ku8V1zZreKCRainQJ_rmx0nI9k_GMWTtOcAi6N3toAnuWJd7c6yRn7G7mVGB0CX8HrZ6nd7HtHTfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
تک‌گل تیم اودینزه به بارسلونا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103129" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103128" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=MLoXu_Vk3Dp_OazOqBd7j69vq8NanCgFHvxa-MgEmOdIHyHVALZjV-gVJen5l7gm5dFrFT8WMaP6twcV7fp6QID76iT8hVz_GAOT2RwNJxbEBEGRpMCV6BLMR8sJ8Wdf8IJznEbXu1evTovf49ybWQLOkEnaeIzhFNJwrIBQsEvovWkrD9gNF3rRiYhj665gb8Psqzs1be9YCaf0fJBxOQRAzUDdlRfb55YtTT9wkGT6epO4SRzrDxhFdcNGzJz6AJ0gN4WuhUYrojEu2hVtWQWNDIsSuwbumh7csVNAqPC1alBWgTaKe-DuWVkskPq5McdkTLwtIJaEZAWtIP6OSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=MLoXu_Vk3Dp_OazOqBd7j69vq8NanCgFHvxa-MgEmOdIHyHVALZjV-gVJen5l7gm5dFrFT8WMaP6twcV7fp6QID76iT8hVz_GAOT2RwNJxbEBEGRpMCV6BLMR8sJ8Wdf8IJznEbXu1evTovf49ybWQLOkEnaeIzhFNJwrIBQsEvovWkrD9gNF3rRiYhj665gb8Psqzs1be9YCaf0fJBxOQRAzUDdlRfb55YtTT9wkGT6epO4SRzrDxhFdcNGzJz6AJ0gN4WuhUYrojEu2hVtWQWNDIsSuwbumh7csVNAqPC1alBWgTaKe-DuWVkskPq5McdkTLwtIJaEZAWtIP6OSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویری از مراسم ختم خورخه‌مسی
🥸
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/103127" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103123">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6jnZKkWi1o0iK-BNniMSvCLqY300s-aCasoLwt6dokbfCyXjP3el9KCU_3US5e35is0q8r5g9oKo2TUSDfOnUc8NycD0r6mLbUTUk8mruwepnIBFJbvPq2mZBxmn8M532iQmtxP4r5KL0B9L0RPtz7q8zzrFj_XYRtbsPrz5aEmeyd6JtHvPWBSCnF_0eoJGzycetYiMhIsbK7X0hzKavdHnXPigcrdarocrCRetWk_2MQlQ9NBDipgE3wqy9z0wNoSnmsJLaDlTNyI1dEjaujyAoYF2iWUBlOfNTyTVBsnOZgBTsNvQJbND2Y9qU7IsJNl8RESfnofxJJFThzc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=PZCcrQVbgJ22tTsV79rW2On8UNEkXLHx3L7yp97NlI72MBBKXmCnuswBfbJgs6r0XtrKf0AdBfm1GTiZmcFdQRYDBGxTb7FMjH80p-l7MqUyhS4u5HlZkup9b7f4fZFE-vO-Mmm4PloBwXy6VC1RX43lJKz5R9N8bkTRK8yxLYnowY3hJn7hulhltI63oPMTBsr-aegcmMfT2mNpI5XAZ14E44WcBzHFVAtoK11bmzjaf5YQsv__G7_il6ljr79yRQ9jJ6YvAajUicOyDS1Am83LEmF_e-LvhwdTUSQuYrOfXId3pUEsipRWR4KxzTu5IOpb7DuX9qVt8qZELbvQnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=PZCcrQVbgJ22tTsV79rW2On8UNEkXLHx3L7yp97NlI72MBBKXmCnuswBfbJgs6r0XtrKf0AdBfm1GTiZmcFdQRYDBGxTb7FMjH80p-l7MqUyhS4u5HlZkup9b7f4fZFE-vO-Mmm4PloBwXy6VC1RX43lJKz5R9N8bkTRK8yxLYnowY3hJn7hulhltI63oPMTBsr-aegcmMfT2mNpI5XAZ14E44WcBzHFVAtoK11bmzjaf5YQsv__G7_il6ljr79yRQ9jJ6YvAajUicOyDS1Am83LEmF_e-LvhwdTUSQuYrOfXId3pUEsipRWR4KxzTu5IOpb7DuX9qVt8qZELbvQnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103123" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbVQMhxTYDQYtggQ720qW3o35CgETYaVEf71QtAKNumNQWxF15RMonv3fW1pNTWpHhm6c6a3wQp8UHHkFNSvOuMSWce3uQ-8jdNt53eHTiE7UmtyociwpoMyOjM4-naCl8LACYrgRj7D7qAW6O4GAEbOcKy3ftC6ZmD4AUYniWFXVsgvnXqElHBbdj0k2ifKwdeRt14kI7_VCxjl1Nfg3cbrCUtcxADrigZnbtTnaooKmvHY9JWCGVRVwUJ0CWym3nR3mthYcpI0ohIifQIf_iWdunCO_XABk8wzC-y_BMrlI2BmIhL0I3UskqbOyMeOI4yzvEPuqG68wJHVoCfhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات رشفورد که حسابی داره بهش خوش میگذره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103122" target="_blank">📅 00:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7Bw7qb2blVodt53yG6PXRupgFoSdDfgShyL-our3-_pGdiXD7ey3rZuCL1e186-mtZgE06ZLrlqj9zt1sUZpYV3_cKz2PZ3EsbBFl5dbXQP1PKGX27OeyXYe78BXUvjGGUzBq__NNixdGDBnnZKhnMkNCAGSvRfBJBCR9_A2VNfGkCvfb7AlaUFwtcNRk6FN-7cWUZ0ITWph1Ifi7QKK51w3xkqE168A8Qh1UOb9qiidHakdDqcKvaAluKXm4a6fPVXc4CW_zpW2Z-xdlafpXBS0RBkB23Vtz56LY_cJngCRpemU8J0OjvnEr35YpMfngTB1MFH5IS2WOHabXWTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_CyJljtiEgOA_wtUTtcq2KihZ1ITMTV-VqgZbQVdDtH9FFOd2C1O3LerFJHd6tbFAWwhr7xkOypKZNjO36fDnvvJOjmHnMJy_6DsTtMP0dMpNXPmD32XZQ5BLla0K8FZDvoMdEwCo1l6SirKfOb0wgaHw5YeVHcmaq4A7xrIZIi2Cz-EW0K6eiaJXMwtPmnYoiyQWxfVyhWYPCEooYwd_L1aBwYAHuiKCKlub6EzAQsBPZ9Qk6FH1M2OG5xzJalrsyKzEUmVo5S6aePG7alDsVbp31TTqkfyJZvMOtgHGNUSfiCq_V0I9sRF7jHmlwEz4SERB0AxDOkavfXY0RJHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
گفته می‌شود فران تورس تحت فشار دوست‌دخترش برای پیوستن به پاری‌سن‌ژرمن متقاعد شده است. پاری‌سن‌ژرمن پیشنهاد رسمی خود را ارائه کرده و حالا همه‌چیز به پاسخ بارسلونا بستگی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103120" target="_blank">📅 23:55 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
