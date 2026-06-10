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
<img src="https://cdn4.telesco.pe/file/LGNvF3_VM2GxYZrmEO5j09EAJQ1ibiuTxuq-ypFu7ELdEMO3VK24WkdNqFIeRYOKYtGZmq50G8abAZuEZSfCBIQp49hY10m2bXrYQ_dMQdgbnJ9ZPvzLLL4U1whebE4-Og9D19y4Ntv4ldbcQyNwdvncti56nLZS1d6dbl9upDBQsQFIVlTJwXeYG2EQyMrNC4M3BWIrH6Sbjym3iuVGtnwG3RVFu2BM_m_kp0zdajO-XJL_oRu7ybWqIcRVi1Szp22qwIlGtlFxzkNv1ydMf_VtvLqy6Ruonpgp_8EpIUJ-OU6LHBsPF1SWjYuw8FQWVRvD7Ob2W4YG_yTO-NCZ5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.8K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsWMXuvBZ-ldMBL9BkXvX7q7hVHiz3K0RBMICM1kKFbUucW3yiC7BniS12lEWOrSzUW7OW1_UMgeEdJHGaZGm9RdovelkABpV_bgrjfBsUjEe26-VRcMxgCADfafba6P6fUcC08HTZTkcb7K-_sb2DyhaMLQo8Z1hX4VeW_t9bVyCz-DYZ4WaiTxIayEGMRKK9yvZDZEXRZPHVADn0BOUUmwonLp0b7DX1USfjCrYcmQQP1nxD3ebcPwLumPLwn2wYbWox46MW48FaTRaxKxeOZ-Sl9gpUoE4VeX0r-xf4oE7_BxTd1bVjYMzoLInDMAN5AY-8lLESxZtxP3B7RDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/9067" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تازه نفس♥️🤌🏻.npvt</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9066" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🎁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/9066" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت قوی🚀🔥.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9065" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/9065" target="_blank">📅 17:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دکترنیک ظهرونه.npvt</div>
  <div class="tg-doc-extra">17.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9064" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/9064" target="_blank">📅 17:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐕‍🦺.npvt</div>
  <div class="tg-doc-extra">6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/9063" target="_blank">📅 17:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری
-
ترامپ به فاکس نیوز :
به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/IranProxyV2/9062" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8Ft89EfucNrTJkwvLe_HcdIEVY_oZDbdqM9CBSR10uAf9XVwbw1uWXQrCgoH8dUWYZBXpzLpP6j93aqzEYPVrf_ilQRSkkKGqzt85kGakC5WtPksrWUW_iIcpMxegt2l6gZQIjFWrfxlq00JVUwXpdvUdpH8gQQXfL2mS5f7amy1Mjs2oPmgva5ZbFWKZJyP-KyF6OzXGRpzMi9YeKcto4W7446QhmwaiK_zgWwtqw_MBZ9B3phnRho_R8VhpjDlEwzj1gWAcO0JtXsXQtZu9bB7a3FXUr1p_5NDTGDxGURCFbsXKNTPqB24YVbd9tHe4Tiyu39-54AVQcuddkmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری-
ترامپ:
«ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد!!! آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!!!»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/9061" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اکثر نتا وصله
🍸
✅
vless://9dbaa630-c895-4883-aa8a-20e8a48ff4b2@fff.oakcup.ir:2052?encryption=none&type=httpupgrade&path=%2Fapi&host=Ip.oakcup.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.193:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&mode=auto&sni=ssj.new-persian-song.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://0c09799a-47ca-494e-a50e-828632ef9d81@199.232.78.159:443?encryption=none&type=ws&security=tls&path=%2F&host=bazaryabab.global.ssl.fastly.net&sni=default.ssl.fastly.net&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://5960576d-829e-4d09-8232-0e80121a6fe4@45.130.125.162:8443?encryption=none&type=xhttp&security=tls&path=%2F%3Fed&host=vi.mojaz-persian-music.ir&mode=auto&sni=vi.mojaz-persian-music.ir&alpn=h2&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://07dce2d7-9849-4e22-adb9-36d2763c3b89@snapp.ir:2095?encryption=none&type=ws&path=%2F&host=api.aramonlineshop.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@141.193.213.11:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://cabbfe13-038b-4dbb-9c45-5079c829abfa@167.82.0.1:80?encryption=none&type=ws&path=%2F&host=max-gb1.global.ssl.fastly.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://8dc7722c-2767-4eea-a28b-2f8daacc07e3@sca11.myfymain.com:8880?encryption=none&type=grpc&mode=gun#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://fc965ad9-bdd7-4815-ad71-b39ec5972dc1@89.116.46.68:443?encryption=none&type=ws&security=tls&path=%2Ftsghdws&host=octopusss4.com&sni=octopusss4.com&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://44b3ee72-cffb-4d66-ab7c-3138b9bdeeef@54.36.162.217:443?encryption=none&type=tcp&security=reality&headerType=none&sni=speedtest.net&fp=chrome&allowInsecure=1&pbk=upTVUrc_t7xF1ULni8pHRDhRES1sT4BDm1r8rugTzyQ&sid=ff815f58c7e77aa9&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e4e7866d-920b-4a53-a8e2-6ae9b2a42fc2@47.77.214.201:10035?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://ae852d97-85f5-45cf-82a4-254eba345480@144.31.131.33:443?encryption=none&type=tcp&security=reality&headerType=none&sni=cdn.cdnjst.org&fp=chrome&allowInsecure=1&pbk=djH9iD2QV748ocK-wPH7HvDd03lu88zHhS4G-61w6Dc&sid=a120&flow=xtls-rprx-vision#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://d3d59da0-31a4-45da-bf9e-373c6ab140db@62.60.251.131:45656?encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e0de62c9-f317-4275-b7e5-8da7b7fa9bc6@77.110.127.191:9443?encryption=none&type=ws&path=%2Fpourya#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTprMWRCT21PQjRvcWk3VW1wMzdhMWJR@82.38.31.192:8080#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/9060" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=45.32.233.182&port=8443&secret=dd1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=mercedes.nine-gear.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/9059" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
♨️
مهر:
شنیده شدن مجدد صدای انفجار در جاسک
✅
موج دوم حمله درحال انجامه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/9058" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
لیست جدید پروکسی متصل پخش کنید مخصوص نت ملی و شرایط عادی
🇮🇷
https://t.me/proxy?server=87.248.129.106&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.235&port=4455&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d#proxydotnet
https://t.me/proxy?server=protocol.fast-mt.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=free.feel-fly.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=www.alo-otp.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=172.65.104.042&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/9057" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
✅
tg://proxy?server=5.78.53.137&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=5.78.57.102&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/9056" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=rec.nolags.pw&port=443&secret=dd0603553657b3f54b6bff0d3759e8db1d
https://t.me/proxy?server=5.78.59.193&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=office.proxytg.live&port=443&secret=eed604acbe90be65ddf34629f1e2234f7d6f66666963652e70726f787974672e6c697665
https://t.me/proxy?server=feed.proxytg.live&port=443&secret=ee7c1dc73472aff6b273c603d9713900d1666565642e70726f787974672e6c697665
https://t.me/proxy?server=87.248.129.222&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9055" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پروکسی نت ملی میفرستم حتما ذخیره کنید داشته باشید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/9053" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مث اینک این دفعه اوضاع واقعا خرابه، از اونطرف صدا و سیما میگ ما نزدیم، از اونطرف آمریکا میگ شما زدید پس باید ما بزنیم، فک کنم آمریکا میخواد شروع دوباره جنگو این دفعه بنداز گردن ایران
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/9052" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پروکسی فول متصل،ذخیره کنید
✅
tg://proxy?server=5.78.48.55&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.42.228&port=4455&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/9051" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
تیتر شبکه خبر :
حملات موشکی سپاه ایران بزودی...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/9050" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
بیانیه جدید سپاه : حمله شرورانه آمریکا را بی جواب نخواهیم گذاشت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/9049" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به لبنان که حمله نشده جمهوری اسلامی بهش بر بخوره؛ خاک ایرانه دیگه، مگه مهمه براشون؟
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/9048" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حالا پاسخ ایران چه خواهد بود؟
🦦
بزن پایگاه هاشو تو منطق بگا بده مشتی
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/9047" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سنتکام اعلام کرد که حملاتی را در قالب دفاع از خود علیه ایران آغاز کرده است؛ این اقدام در پاسخ به سرنگونی یک بالگرد آپاچی آمریکایی در روز گذشته صورت گرفت. این مأموریت، پاسخی متناسب به تجاوزات غیرموجه ایران است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/9046" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
صدای انفجار در بندرعباس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/9045" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qundKWpwgYbDj2lmeUIefwkeKXdnmk_ExBRVCcwkGHe-Nbz6KVitLc6vcxg1nsC88HWEvloQB6aroIPBEdbsiZXcx8NduM89j5XE1MH8YjIjVKtsdfT_gwD-EcwBxBhJqZbp2OlGZGGmBJrJo6J_NTzHc5aIJO0gMrgFLnth3wnLQEi5_T8g8GBuzYUMv2iwpdxT0EgpEmaoOEFtEGkeyA-3xq1FyjvingIkugDsRl8Mzy3hil9urRqo5wOaNUGLZ18kEgI6GkYqtoX5DGBvC7jWlpL1nt1pOVQA3eZ3cs_D8JA_D4BMOcW7vBRFCS9Cu3zaL-N_zIV8C52mwiJQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/9044" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqxPeGfxrevVxuQGEKIsed88fWxlxhdGUt6lvMUY4YF_2O5I2hwMtVPMrebCw3If9q48qKuzf0sEFhPHUEPDKP2CtUJA61aZjYgLASPw-JznWxIpu_7WdVX1iv7d8316tw-0_bnl-8NJ-HP0jUoj5LSBB-Raby8ssMBIViaW5JWg-aWHIsSyIZ0Ti9HB-nd95KVnEFhKYMExRcnrRpQW72Biu2mcu0eG3iEJvwX09n6junV2OVVlIS4e_I17sFRi0aFyw0fisN3avH9cy_1ttFrJT3wdQm_-K4awTMrV_U_7ThwFjKttU7KpMtMiPnoRLHA1cJhStr8a3U9ETvnrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تونل کردن ترافیک ایران به سمت کشورهایی نظیر اذربایجان برای باز کردن سایتهای تحریم شده مثل ChatGPT و Claude بدون نیاز به VPN، باعث شده که ظرف مدت چند ماهه بعد از عملی شدن قرارداد انتقال ترافیک، رتبه کشور اذربایجان در نرخ سرانه تعداد پیامهای ارسال شده به ChatGPT از رتبه 44 در اوایل سال 2025، به رتبه 6 در اوایل سال 2026 صعود کنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/9043" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=5.161.143.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/9042" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا :
دیدار ایران و مصر دیدار افتخار همجنسگرایان رنگین کمونی خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد. کاپیتان هر دو تیم الزامی هست که بازوبند رنگین کمونی  ببندن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/IranProxyV2/9041" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9040">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2TlX4r3c29aqzLE0_6JJmVU9iVuGveuFmFS2xyoeVREyA_xzI4t7dgTFMeBEE2ekKvm9uh0CoyjFfZz366PWy2inE-wAEsOuH0iCvCQhB4ezkNV7P2WlNrID6VFvgCTgKVXv5MGsI8yHkMgFznIc1XYj3fdSaPmpT_2nUlyx-6C0iR5NGJ72vf5fazg9O45rbNpFCGYTIOHiSdz89BgSam5iD_XagNHTkCDLkJJcUehB9IAHJMfbxZ2G5Y03jihnjYFfzbxWLWVtoaN8FutmPCT4GGbozHx2NyJHiW-ZeAP5PQxXM_mgVbWISkqBImLSfpwrYFpF5bCuesOd-98dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/9040" target="_blank">📅 17:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9039">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d4eb1900-6515-494e-85c5-306bb9594f56@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=vo.new-persian-song.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/9039" target="_blank">📅 17:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9038">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://10a6b923-e349-4594-92bb-d81a6245aaec@172.67.74.10:443?path=%2Fdownload.php&security=tls&encryption=none&insecure=0&host=sertraline.adaspoloandco.com&fp=chrome&type=ws&allowInsecure=0&sni=sertraline.adaspoloandco.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/IranProxyV2/9038" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9037">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=135.125.216.18&port=8080&secret=dd112760f4d4ccf54d5c3bc40a6776c73b
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/9037" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9036">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعتی🔥🚀.npvt</div>
  <div class="tg-doc-extra">2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9036" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
🆕
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/9036" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9035">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📱
یوتیوب رفع فیلتر می‌شه.
📔
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادن که فضا رو به شرایط عادی برگردونن و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/9035" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2XaD96u6vPLYc5bExbHm0sdpUJqZqDqH-80K5IllF-_6Z5P71LaFeOgUXpnXNYAf0wcpB00D3I1xmVyTae_hb3rTgFjTwm8oLXBLXuDcYPU9_8QV3hXpJAKC1E1tlU5PMSt1IH6uDAkPNAIPWbM3Kj4mDO2q-UK7nGIbmQ8wHI7VvfrpAJEdZl0Q3nBlOyV05Urqn2qf9f_-DeUYDv845XBMdgFpZwHh3LN1URLmKo_84jCYUictsMcYNWgJjfCY0iYDMqMaxAzkn-apf-dipRh3OaNeVCgUzWE3WAw1KAzjqhJP3mvv8j3799nef7Uqk2saGLDHjNw_64TO2XnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به ربات مراجعه…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/9034" target="_blank">📅 22:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Use1iMBMUILS0XORpp0by4o6ykrGL_Rskprk-HNqqby6PzB7oFYD8NIIOezo8u40hEceF4kH_et0PYMB7Wv5pfwLkeEye2Whx03MY06psvcmcX_4V4wfu5ya34RoZyIaZAqpKx52t7U6fImokT_VsetPZOlah5OkN5wFrJcyo_AruZLA5V8V_bcpg4Ny0U5rMgTdYgZMFMjeBCSfxfAGykRnL1mUIx-wdvqw4wzPgd0Eqne6la_LqIhOoBO90f-jQwuwzzpbcCiFfrj4pxl1SYnZwwN5-jgJMgbVHpP_eppY38o2GLBHW-dXrrYKtWXpwyl6O_loancT2uJaS4aKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/9033" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=178.105.226.182&port=443&secret=ee396219a1e9b2aebf6f245a1495777811706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=orbit.proxyonline.online&port=443&secret=eea49899bfb9f5b061d6213e6f6480ea006f726269742e70726f78796f6e6c696e652e6f6e6c696e65
https://t.me/proxy?server=94.183.221.165&port=443&secret=a252e3eb41417da5e2332193f25bcf34
https://t.me/proxy?server=relay.proxyb.site&port=443&secret=eeee9dfed6b3721e5b2788f5100af2ff4272656c61792e70726f7879622e73697465
https://t.me/proxy?server=5.75.200.229&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/IranProxyV2/9032" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
مث اینکه جنگ فعلا به پایان رسیده، هردرطرف از موضع خود کوتاه اومدن ولی البته یه نکته بهتون عرض کنم که این شرایط فقط تا پایان جام جهانی فک میکنم آتش بس برقرار باشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/9031" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:   نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/IranProxyV2/9030" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
👑
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/9029" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=fresh.nolags.pw&port=443&secret=dd691fa48fcc661b68fe4f5200c5b174f9
https://t.me/proxy?server=91.217.166.212&port=16&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=fool.feel-fly.info&port=25565&secret=7hYDAQIAAQAB_AMDhuJMOt1iaXNjb3R0aS55ZWt0YW5ldC5jb20
https://t.me/proxy?server=91.217.166.22&port=20&secret=dd1603010200010001fc030386e24c3add
https://t.me/proxy?server=91.217.166.21&port=20&secret=dd1603010200010001fc030386e24c3add
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/IranProxyV2/9027" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/9026" target="_blank">📅 13:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دوستان احتمال داره دوباره اینترنت بین‌الملل با محدودیت یا قطعی روبه‌رو بشه.
✅
از همین الان برنامه‌هاتون رو آپدیت کنید و این اپ‌ها رو نصب داشته باشید:
• Happ
• NPV Tunnel
• V2RayNG
• Psiphon
• ShiroKhorshid
• Http Injector
• NetMod
⚠️
قبل از هر محدودیتی، آماده باشید
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/9025" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhgXkaupsfZ4SP4HEedwwhxAeXVSTOGZgVW09tDsRANfPTN_ffIDhbvS6DjAW4da-KkllFHx1-l5QiQLQ-DlhU0FOfbJ_HnDACwyM3nF1xB7xTq10eSMq-KpipNHFvNrZyk63B9VxaYRqT_LlunFw9_4Hqnt1NwsOYORazlBicyKsmRQ72wRf3KmoLuFwnihIs7_ofpBaSGNlXW6b5-XXisS57J7v27KwLqtRQe0Ai8EwJnVf6ISmDVBQT9cZ5TrSOKf5ZH-lx2mbRyRlbwhYMWCGZX1vSuio6-zVsVJVXNl1lMPLl1sPuSvykln9Gw1qzLhWm_aZDvNkYINiNigUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/IranProxyV2/9024" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=s3.mowork.twc1.net&port=443&secret=ee90872f20ccc37e3aa2681602f51df71273332e6d6f776f726b2e747763312e6e6574
https://t.me/proxy?server=s4.mowork.twc1.net&port=443&secret=ee3e9cfe9af4494731b9a566075ee8c3bc73342e6d6f776f726b2e747763312e6e6574
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/9023" target="_blank">📅 13:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
vless://a78bf929-6883-48af-902d-7737793eeb17@hu02.sonicsonic.icu:443?security=reality&encryption=none&pbk=z-TKWOWgZLfzQ-wNdwXQqVwaUgCmbchM2Xtrk1NGynU&headerType=none&fp=qq&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=hu02.sonicsonic.icu#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/9022" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=imtproxy.ir.imtproxy-ir.info..&port=443&secret=ee16550001232d00bb5190728b72644171706c61792e676f6f676c652e636f6d
https://t.me/proxy?server=65.108.154.5&port=443&secret=eecdf95381f978fb348f233a14b2251e6d7777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.148.135&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=5.75.206.125&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=91.107.167.170&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/9020" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پروکسی مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=91.107.156.186&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=153.80.241.214&port=80&secret=eefc56fb73c972a2309c4787bc1364c2207777772e636c6f7564666c6172652e636f6d
https://t.me/proxy?server=51.254.130.47&port=8443&secret=a84102e409230c3b69dd4f68cef86baf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/9019" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
براتون پروکسی نت ملی و اوپن و... میزارم، حتما ذخیره کنید و برای دوستاتون بفرستید درصورت قطعی اینترنت استفاده کنید تا بتونید، حداقل کانکشن رو به تلگرام داشته باشین
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/9017" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری-آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند.
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/9016" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
دفتر نتانیاهو:
در پاسخ به شلیک موشک از سوی جمهوری اسلامی، اهدافی در داخل ایران رو هدف قرار دادیم. اسرائیل همچنین در بالاترین سطح آماده‌باش دفاعی و تهاجمی قرار داره.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/9015" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد  بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/9014" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پروکسی | فیلترشکن | کانفیگ v2:
🚨
فوری
⚠️
👑
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/9013" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ارتش اسرائیل:
در ۲۴ ساعت گذشته بیش از ۹۰ هدف متعلق به حزب‌الله، از جمله انبارهای تسلیحات، مراکز فرماندهی و سکوهای پرتاب موشک در لبنان رو هدف قرار دادیم. این حملات با هدف از بین بردن تهدیدات علیه شهروندان و نیروهای اسرائیلی انجام شده.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/9010" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/9009" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🆕
خبرگزاری فارس:
در صورت ادامه حملات به تاسیسات انرژی و زیرساخت های ما؛ کل زیرساخت های منطقه رو میزنیم.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/9008" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
مهر: شنیده شدن صدای انفجار در جنوب تهران
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/9007" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
رفقا جنگ جنگه مراقب باشید از یک سری مراکز نظامی فاصله بگیرید ،امیدوارم تموم بشه این جنگ و همه مردم ایران سلامت باشن
❤️
💎
پروکسیارو ذخیره داشته باشید حتما
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/IranProxyV2/9006" target="_blank">📅 12:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD6qhOhkaI7DkuFztSSLFZQyy_c-l6es-KcbEs99yOiONkwsj23ppOyaIdaPV-6ylfUNgEh2zV2OJIjxg2j5ImVzB4vvs12rsCnwvatU8yJ6vXmvKE__ZvcyUtnpu5T4J8gSYF2T0Y__jDMwGScawpOrN2uFR5xtdLDTk9frKDSsqcAwHwGGK38PIhKAAe2UiFao1yR_Vcbg6ys1hpJEbBqvf5oaXYyizYIpuo2mJysREZdgnpWG225-Qe6_bz63fscpebW5wYdcWJffgPz9_GGfZ_YpYU-ZdHQjsi-IC3dnjZft4g2oFD74GDEMyR7ZOnEeJtgVHr8bltR8Rj1G1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون تهران
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/9005" target="_blank">📅 12:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU8rNpdAfWrqmUUF5Nsha1ipbPGuXhbAjuG3ooe2bQTlys2avMuJDqlKJXuvbTQLd0jm6jdeVMrCFflfY2GYzS-cuW1mRfm33NEHwqUeNaJOJ_WKIqs_BXSSMCHPOJy0NR6Aek4QjI4Dnu7ehoVL3omKYKNcg6M9LGuoIQORov1VLIv0KujmjZO01Y57WTrtajpx-vCrYk8CNSshqxpWQ312elH24O9xrFgcn-a0V5mY4aPyte7e89CzEZmzfVwDdeIqgqDqHID3zcc8QotdzTk5cK6YlYKgFJhQRRx3k9lAQeajUX1ai1mQkcJaX3EzMpymsxkV7yJ-Zj6pQAsXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تهران، شمس آباد:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/9004" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
حمله اسرائیل به فرودگاه شیراز
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/9003" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
لشکر 8 زرهی اصفهان مورد حمله قرار گرفت
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/9002" target="_blank">📅 11:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
❗️
دانشگاه عاشورا هوافضای سپاه مورد هدف قرار گرفت.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/IranProxyV2/9001" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9000">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
❗️
وزیر جنگ اسرائیل: شروع کردیم.
Proxy
|
Proxy
|
Proxy
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/9000" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8999">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🆕
ایرنا : انفجار در استان همدان
پروکسی نت ملی:
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8999" target="_blank">📅 11:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8998">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8998" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8997">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
تو اکثر نقاط تهران، پدافندا درگیرن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8997" target="_blank">📅 11:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
بنا بر گزارشات دیتاسنتر آسیاتک قطع شده و به دیتاسنترها جهت قطعی اینترنت آماده‌باش دادند.
در صورت تبادل آتش بیشتر قطعی اینترنت بعید نیست.
اگر فایل یا اطلاعاتی به صورت آنلاین دارید بهتر است همین الان آن را دانلود کنید و تنظیمات حذف حساب‌های کاربری به حداکثر زمان تنظیم کنید. راهی برای وصل شدن خود حتماً داشته باشید.
چنل مارو حتما دنبال کنید، ما هر راهی که برای اتصال مجدد پیدا کنیم حتما حتما براتون قرار میدیم درسریعترین زمان ممکن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/8996" target="_blank">📅 11:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری-صدای انفجار در اصفهان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8995" target="_blank">📅 11:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8994">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در اسلامشهر و ملارد و کهریزک و باقرشهر
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8994" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8993">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری-شنیده شدن صدای انفجار در غرب و جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8993" target="_blank">📅 11:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBceiR8egHusRyqgZmhifT8nL5I9HxjkWdSZ9SD3tCa5Y-ZHQnfx1ngP-23V3vYRc6wbBXqccUDA7_dsW-RMaXdQCJhcaktnp1j1JYXseQA0r7ldYwctFyYcVUEb4nriO0rNM1iG82-CUYggGmhWy5qOo-A8cq51FYLEF5NwuO-w0BfojIUZTEJjSViROoQbc_xNZ-iz_OEUk46uCBXTm4FwGbDxwPUz4hCE7N99k6l5uDKYcL3JE4Ay_5k7RqnX9POgPCqBdJW3400jXHI4VeoUdfGKvBK5j5SXJdctfH9jri7jm6eMm6neAQhnv_WFHX71C877E-M3jOgtVROIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وضعیت آسمان اصفهان:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8992" target="_blank">📅 11:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه: حمله دشمن به صنایع پتروشیمی پاسخ داده شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8990" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=KHgqaHk1gyAmw-gMpDK8VVtNNLII4ZCvbiXZJS64cowU1VbN4tSLaRG_mOS-kMWhWf-VYYSn3Bm0cTQyFnUfy6759sDQVQvNormHJ77n4lFKTmKWkt_pqz2OJ2ALu3ImQpAeauTyRY_Ae5HiT395slYMZK29pG9huAVAmZJpicLv3clIo5Tnl0QbBvMZOzmXz4hwUkO00UFZ3PciNFNLOt1OwTcnRWwzM4Cv6btyQjz43neJiqWD9z-tCPqU38JbmUAydNJnYkpJUURROT0nfD5xWmPqiblqy8UOlj9iDkXTmCKh_OnzRWG-ynZ8MEiqJ2iwVnH3Yx1DYONwhjwY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9354396b.mp4?token=KHgqaHk1gyAmw-gMpDK8VVtNNLII4ZCvbiXZJS64cowU1VbN4tSLaRG_mOS-kMWhWf-VYYSn3Bm0cTQyFnUfy6759sDQVQvNormHJ77n4lFKTmKWkt_pqz2OJ2ALu3ImQpAeauTyRY_Ae5HiT395slYMZK29pG9huAVAmZJpicLv3clIo5Tnl0QbBvMZOzmXz4hwUkO00UFZ3PciNFNLOt1OwTcnRWwzM4Cv6btyQjz43neJiqWD9z-tCPqU38JbmUAydNJnYkpJUURROT0nfD5xWmPqiblqy8UOlj9iDkXTmCKh_OnzRWG-ynZ8MEiqJ2iwVnH3Yx1DYONwhjwY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم‌های اضافی از موشک بالستیک ایرانی که در نزدیکی یک شهرک اسرائیلی در کرانه باختری اشغالی اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8989" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=goO6PyEG10jhDOaXv7vvsPfaH9W0EG_IttJcwu-WiVs8mOJYO5J4V4R0Sv5_7o4j_AnUvqNEZtw862gOc45myTexwY0HdvWbKymM7p70di4XII2QZ2xef2UuTeocmPyO5WeONBOZ6zPT31fs1b-lryJ6kbW4Bo4zsg0_-bmRI4wLkaadVKmTjNVlBNNsHBN_y4gbjs3i7cblB1t3wlB_6IqDYOv55rk9vPofiQkEzHQ72QltFnZIBmeP1fMkUh65yZ5-se0y0YLPYPV9w8PwzrpdeS2s_70XRyYuj2bDGQKIl-CvLeeQd-Y7wZYC1VWu3_GlU_YfeqgrcdkC49WTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88608e0e82.mp4?token=goO6PyEG10jhDOaXv7vvsPfaH9W0EG_IttJcwu-WiVs8mOJYO5J4V4R0Sv5_7o4j_AnUvqNEZtw862gOc45myTexwY0HdvWbKymM7p70di4XII2QZ2xef2UuTeocmPyO5WeONBOZ6zPT31fs1b-lryJ6kbW4Bo4zsg0_-bmRI4wLkaadVKmTjNVlBNNsHBN_y4gbjs3i7cblB1t3wlB_6IqDYOv55rk9vPofiQkEzHQ72QltFnZIBmeP1fMkUh65yZ5-se0y0YLPYPV9w8PwzrpdeS2s_70XRyYuj2bDGQKIl-CvLeeQd-Y7wZYC1VWu3_GlU_YfeqgrcdkC49WTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از تأسیسات پتروشیمی هدف قرار گرفته در ماهشهر، جنوب ایران.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8988" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
رسانه‌های اسرائیل:
پس از شلیک یک موج موشکی از ایران، صدای انفجار در منطقه مرکزی و تل آویو شنیده شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8987" target="_blank">📅 10:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
اتحادیه اروپا: امروز تحریم‌هایی رو علیه جمهوری اسلامی به‌دلیل ایجاد اختلال در آزادی کشتیرانی اعمال خواهیم کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8986" target="_blank">📅 10:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
مدیرکل بحران آذربایجان شرقی:
در پی حمله ساعت ۵ صبح دوشنبه به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8985" target="_blank">📅 10:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فعال شدن آژیرهای هشدار در اردن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8984" target="_blank">📅 10:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqQ49kNezVdRvSAjZuQAfVIRmFXfLDFtdU-N7B792OV2v6OtCYG8nBeOnKyDp7iPuNdpppUh8EURk06PMS7qxKGIzXls82lLdHWe2TdQ01sHMB-VbMNFGVLEdhVH3TSPxBvHs5EVNIPxS5t-V9K95mxJ-QhBRvgFF29doqF-z5XHuP6MgbPZEwB5qKTxhLZ9zYJ_sHuJgf7I4QxF1SZJjF_neNlg7K0ajfK3T0MYpRU-BzDhZrZJYxgsP-xd6U6LqU9pPFyidjWY6JeZMMYTfpQjHhuxWP0D5HatlTG03Bt0Pzg8kWKOu7FCsEBQT_3afb4cDwTPN8e3QpFEHHjIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جالب ایلان ماسک: جالبه بدونین اسم تنگه هرمز از اهورامزدا، خدای آیین زرتشتی، گرفته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/IranProxyV2/8983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فوری؛ موج جدید حملات ایران به اسراییل هم‌اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8982" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇾🇪
فوری؛ یمن تنگه باب المندب رو بست!!!!!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8981" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇷
❤️
فوووووری؛ رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8980" target="_blank">📅 10:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
⭕️
🪖
به نقل از منابع عبری ارتش اسرائیل در حال حاضر در حال عملیات در خاک ایرانه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8979" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سپاه : عملیات نصر شروع شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/IranProxyV2/8978" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8977">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
انفجاررررر در کرمانشاه
گزارش منابع داخلی از فعالیت پدافند در کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8977" target="_blank">📅 09:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
⚠️
سازمان منطقه ویژه پتروشیمی:  دستور خروج اضطراری کلیه کارکنان روزکار از این منطقه صادر شده است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8976" target="_blank">📅 09:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🆕
کانال ۱۲ اسرائیل: طی چندساعت اخیر به ۲۰ هدف تو ایران حمله کردیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8975" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
کانال ۱۴ درباره یک مسئول اسرائیلی:
تأکید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/IranProxyV2/8974" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2zzkHhJcLV8VVT14gu5RhQPHmC5rL6-YHaTVbLmmrqgoTvCb2aItB09d8F-hPrYGlLNuAZdOIsZiEHtMDGi_CaEl4Cxw1bDV5I9ZSmHFKjuBzCk_xN_7lSsVx3V4QsAgfrDBvyUt4yD66hQmfmYevO3vG6CvK9-zfuqTSE3bh0pzEJtFbiAhObEtUaSFOu8iXbeKuCMcEvBnAsG9qISddCsgFesOF40ZL3VSLJZ6xKIZxO9n4vElWEEHtgZB17wlPx-SgmstNfcYv6ryai9VyWT3WfgMGTkve0QClrNfBYoQeSl5nPngBj7uXJ-Nv_35tiwG_nx9O6NFMZsnQ3oOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور مورفی:
این جنگ برای آمریکا تحقیرآمیز بود؛
ترامپ دیشب گفت به نتانیاهو زنگ می‌زنم تا جلوی حمله تلافی‌جویانه‌ش رو بگیرم ولی اسرائیل ۲ ساعت بعد از این تماس جنگ رو از سر گرفت و ترامپ و آمریکا رو تحقیر کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8973" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4NN2Jg-Jnq9PaA3WngJjJKP7nh4sNN4H4JvLBl1-y3gJtPpnVdHIFeBmd8Z15SLG_mBczVfUgO-NrhExiilEGZ1Vdczz4q4ZBaIIP6RuhsKJYFwjrf7K04c7metm4Gu6yDB8oRT6CsTjszQ-m_YSwifUxcJBSWpB79oCSJPBg_ILWLZMKkzFExyxSRf--ENhOK_t6OtoneN6XBumjeUMBSkEwrcHBRmqhM3yJRXvNn1U8JUdqKtmZC5kP5GrizCZSTUp_emuNnRunkTyzNIRYZCKi_EuC3BVbCs8QmfSOcBS-7IXdn6ZhbVYtQjZT0uKKoFrK3bRUCn0ZxRLFojlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم
:
سپاه موشک خیبر شکن و یک پهباد ناشناخته امروز استفاده کرده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8972" target="_blank">📅 08:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺⁴.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8968" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📶
این پروکسی های تلگرام رو داشته باشید متصلن:
https://t.me/proxy?server=www.alp-drtop.info&port=443&secret=ddf0eeb0bd9adc4fd4a93994ee3b2a216b
https://t.me/proxy?server=167.233.66.2&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=188.245.196.78&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=87.248.129.107&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=178.105.225.211&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.107.246.35&port=443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=secure.bits-lab.info&port=443&secret=ee1603010200010001fc030386e24c3ad37765622e79656b74616e65742e636f6d
❗️
با اکثر اینترنت ها تست شده
پیشنهاد میشه کمی برای اتصال صبور باشید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8967" target="_blank">📅 08:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlUx1rkDnKMRJ8Oi-1G2ZUiqhmdc8QkyAuoS7WJXkqyj_Lc9up38d3ILHf5bXykgHVBtGiyHMX1XrUTta8-oqSIVyYRHj7mrplGSdkCIlD1KzSZ7skgPtBJ5aZNUjouGG_ew4SA2AhoVOHtLHOle67A1VdTuDxGz45snsWiXiN3KFdFFgp1-IfdkKwrFbssXXygwBk05qFlI0LuPP8x8rQesChcmq4AVgWmeZ7bhd8ZJ0hEUmEDreogwoJTX6DTuUTLT6iAn9Mg80bhx-1quMiNWE9bWZvdKH316gccKPkrsF4zCUn0eONAg_SH7rq0WPlVsextPlCBfsQPzgIXKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه وزارت دفاع عربستان:
دارن بهمون حملات موشکی و پهپادی انجام میدن، دستم کم دو انفجار نزدیک شهر ریاض گزارش شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8966" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رادیو ارتش اسرائیل
موج جدیدی از حملات رو شناسایی کردیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/IranProxyV2/8965" target="_blank">📅 08:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
اصابت چند پرتابه به پتروشیمی کارون ماهشهر تایید شده و بخشی از پتروشیمی در جریان این حملات اسیب دیده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/IranProxyV2/8964" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=Wr1FQ99QPd7LEs5AYw6xURBAP7X4Sf8E18uEbffWWBQp0HVLhO7PcRfXJf5YP7M9b7lls_mLT3IWMfEkWNGmCEz6LDRNUKa8RJfBvcb9Qjq5qzXSTSTTrX9tKUxA9g4t1-ePqjgBtYJGkw46glA3_PYMw0Ro624NfUHuxucuyxXnHGK6Rym0UOnAsdikNnJJPQkhx9u6SAbqzrLejiq1rxRa4h_b47l-U9CERV_YWHVlL6kBf8Mb8P62924ctchc9LT0PK2uZf7PrugDj4FZUEPT9faNBzaFc1O1Fk9m7B4W8kw5a6NIbtt3VQ30ggz4UZFfgXSfz4ovL4CHAnHcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc73ebd9af.mp4?token=Wr1FQ99QPd7LEs5AYw6xURBAP7X4Sf8E18uEbffWWBQp0HVLhO7PcRfXJf5YP7M9b7lls_mLT3IWMfEkWNGmCEz6LDRNUKa8RJfBvcb9Qjq5qzXSTSTTrX9tKUxA9g4t1-ePqjgBtYJGkw46glA3_PYMw0Ro624NfUHuxucuyxXnHGK6Rym0UOnAsdikNnJJPQkhx9u6SAbqzrLejiq1rxRa4h_b47l-U9CERV_YWHVlL6kBf8Mb8P62924ctchc9LT0PK2uZf7PrugDj4FZUEPT9faNBzaFc1O1Fk9m7B4W8kw5a6NIbtt3VQ30ggz4UZFfgXSfz4ovL4CHAnHcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از موشک‌های ایرانی به یک مرکز نظامی اسرائیلی در نزدیکی نابلس اصابت کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/IranProxyV2/8963" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmp-bNkphjk-TdovaJ2rRmytq-uGsCQDxBHmwEpFL9Yf19az8iWSZgpF5l1nwibA6BaagWoshSrArW18NcivWF7UwN2Cq6w8wlmf7YApHFPK9vXHUPD2th3r6_w07XPqG-TpE3wDa5B-khznv4LryUS8iwCO7hFo7AfWE1f_YY5ZbTfkbv4mkL_Pq--q4IxbXUWGoW06U4RUCsIYsZcWduydtUFCg1k4lzsa37wOs7pLibQ7KhIR36ftTt1a4WPu0rHvB20OOGHZrp86eVK9XdNLW52Z871ERLdYJxn6ynPpDz_ix2Ffk_Ei-pXYFFHKaDucu_fTFfNU5VdxsylDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8962" target="_blank">📅 08:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
مثه اینکه موج جدیدی از حملات ایران شروع شده
از اصفهان ، ارومیه ، خرم آباد ، کرمانشاه ، ماهشهر و آبادان موشک پرتاب شده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/IranProxyV2/8961" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
