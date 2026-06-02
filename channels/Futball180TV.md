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
<img src="https://cdn4.telesco.pe/file/LqoIAsZGMD8vZ99jof7rp0L3ax0M-39cYYtbHvnw_sQ35tuiiiUPqA2pWX6VbLz0WXvFh_0_Rtqmp9qq0X-OVXWFWXtmWz7f8FIP4SHOKfd3u7O2ytW4fNEuY31Yf-HiLcQxSYejPdE-GptiYVhC7G_N6645GnTibJf-lk0b__g_rtfN2OrjHSdCSrSdp0zB88WFlKJbGa4iVBbygBlo2jqvgXAbepptdSkopjCiNpBpqMxA5jZzfX-BqJvrpa2U63jTmwaFej-WHDHaqr5OXkt0XYkQK8-J3l8BUlQV1p21FcY0Sp3zuhnm11e_CMVDMB86XF4daJuLZdm_bB7z5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 166K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAKyJfZWjwGezC-xey_7FximuonRqz8EN8xaA8gesV1vpazYrOwtgTHd2lzRD8IaZt3bQ-vXBssxO4bDEL672xobEW3jsZPgsLUfK2hTG6YQTALjFsKMP053qQTyhKQZHj8gq5FY8K3M1bojB4wNjuYTyF76UldSJFILmyCaCcmafEI4B3kUqOwxwr-VyBfYH-oxK1O47hbZou_ZIqs1opwh9ynUl_rxAKdgtqxN13kCGbiiBiwhHWspPFie3qyGs8ULaJ8X0KsV1Yvq6gtjT6RvAiTVmDBt6W7h2I0GNSAwSB5KrYgce39UIFKXqeHZRjuNdEtfPBTdiLEnEFw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loXl1LvGr-zBEZ_Gu-NojzhPs_YiC6UzDOI_xFWYLXqLMQ7WA4oqKTGU3a2RrY1oR-dG4KcXMAO9erMjp_PjT6LvakjQpjMQZTM3ZdA85y57M7uMDt1w3XiaMjUJyQumDIfpSSG6rrTti9iYO8FZGvVeD4IEM-e3ZWiujALhls5vNXKUX0ZTnI-PXE_ZWFqNLs0hvQfBiQ2Oi71eQjYMK9VOimzjrwCxnU3cFqtT7zsW8faUnfG-dauaNkkF7UYp8TN6aOi_dalE80ux-dpWdzUcubNwrJ48ZGA3vq4kPSayL8AmAGByvsCajWkg76VusdF3iDMlKlcLnhDY5sGQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe99EbpPwckEet1TZthEY2sMxmTvgxSe5saY8tMo9C972o0tlihdJDqlLyGDU02hrkQAx46MxNG5y2LWF5vMhtgxiByF0SMs0PiFrhnymb81RK6hYKStNlud46mww9QOQq8QJf-bep0Fw1vquuThFpvqMQWtHetktrFIBj6aG1aP6iJUohAFpTVC-dSGhT3Pv8YbD0SEyfQwktxkiFYxKRfa8aYXEbsZmGJnskC5LyWzrj2B5Kep93pcEy8M8c1OANnjVA0FYgxeqv0i603GPybmF4-E_ioT-VxdJzzlkm5fwx8sX1E5B9bNKhu4lSoQ9WB34i0cvuufV9o7HsIhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soSdL6FVBI2AM1DKkcjGylKj29mIG_53vKx50wYa0Yw1Orzx401tJZULsfulv9WohDz8Ny1nUTz1AqWMtiqEqlcun8E6V9XrjnuPe0J1SvimFuoWYe56IfiMUeEqUlQiAhxb8-ohby_cvcyA40VfeRDX5zlm3jTKFUthK-tM1uiA7NDddRCieI1SwFoM5igQlzsfDQiKebrqyVHsKbln6iSXm4PDJXRTidaDr7ii4rwKB3nvhGZSyzrlau67zxyWogE3Cr0ZKxOz-VIGubWt5m09V_CaONl5D-GrsECcR74joZN1D5DOkllKN-O0jQl-U7MqtYm_m-1c88X9FZwTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1-1lGsi4GmNU_EWSFVk_IvIAR6zOiXZC0vnTNAjthU0R8YJfe3hJzHEZI3rhPHhnOfJYjsF5XtiezWdeh7AwE4EPNDex2nEVp00ohxcJUpsNdU5FWcDdSc0TrtzLLLSGvohxVkpAfJgN1NUd0aAJylwshcQRiKQ9koBTxDi_xgZkliuGRzbeO7xTprBHT26kEIn4_dHgiBZmt7gbiC22yah4lxN2WmdlzG1e-2jnoLWeuqwxpTk_lhb5wHRfE9FJuc4PJHYsOmxx5L4AG_BGCHB3RlTCsTOH2hK_p5zVV7jMgwdveK87B0iQWJsSubxj8pnhridlTm5O98HiJ_esw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVTe_bn2QH3e-poAfv3kePCxbFj4IQ23Ii9XpEo0vSSwNTi-nlHtvYFXtgu4RYIm-Nl5_OUfUWmqQRZDTt0zTY7kNExj7w-ywhV7XSZekb2ut4SYpxJvG_LIrvLQKJBc4TkKYksrV-xF1K9V3jm83puReMRU7nqKNEuo61yI7UNpi-354GG0nCpgkbY3dss6KBR7yp7RpxrRZTMBL2Lk1PlIw-lSg-Mn_vL1a0K3fVuJN2f_IDuvKloYkXIkNjgAjaoCOTTokPsiG6ogFNLKOCBGV87Ub9TVWz0sGp8WVDw5mgVocZCG0Pn9czuNuWuMeDeW16NbT7GBsDlIt-UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsmCQN4sulbG7BvH9ckB9YyoD3z7b0SgrFcouP9gExLclXwUB4aiGnQG4DsbZZZ4HKC7mvCiulBvdH_842WGHpbm9UNiGpDXbpzmyE64kVfGnC1qCiaPjUqrw8InKrPhBt3tXi8ObKmOfB3wsMIiTYkTqRQyHjhitCAnZFo351JBXqewTX8D24lsan-gKjJ2_PPapgAezVS3vgj1Axk7Qrd35b1HVPeKctUFS-uvXaMHpxRQUieB2RE2pVt4WNoHj_442pRt3p2yArwScNb3DQK09Cu56a0z3ZHcutpWzABnb0priZc6utytMqfahkIR_Nsu4thHM75K9dom9B5B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfqCehcDMaD_tDl_sOMz6laUL9Y8iWmj2vo0TFbn3q1a1zMZBpWkUp_mjeODI7xc8axnyT3AgzrpBLiZKqxqSwPtM3uxBnwUAdnBGYJHolv4jrjc0mJ_9mjGDdhWtnMz2cwU4924FFaAJQLebnzcXuK4-7xAEghzcy-pRlfKeKkpHvu8kfwNV-kn2Kc8OulhLCDrHcmotsVoGQ4-K-wYUWVUzWlx5t_jsDWF8DWGp_YuTPW18TvVkEHE8_b3Nr9alpZAvqGZLI9OLQBU0W23bimoI_5HZItzBoiR332-aZHrIrcuprrAwTV2cZTuCgrXqVA5WoxJcsrx6KDLdxBICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOHokP6IgUCUlD3Z1aqb_Ncy6kjKPrpU7OHQGVt4ZHNukz2uU4oh2MISR5AbrX3fBrzd8K_16gVw1PjhyAHxyLfc8CW6BZ9wHmzL0VlC8vYCp8oFKoI-YjJqkwrfgM5bp5ate5QkWUajU0IIzHyIXPSLzgNgnsTKM2AfLnb9npBjRM1s_0M_Qy4LKkgNP6EBxsZG0oYUclV2c-_hBAuiMOa8nsiPTFQ6ANeYcdaaKM8yNEnCAVF4npmFdC8ndQryX8ab3dlSZb5qA1gigjZsQMWEMH6pQNqzzsn-w0ziplZqV4qBLyv8xyBSmXsMZ9q4LqtYOEKMDegonM6AlzqwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibPcxACxTLj3Vd4-jAdTII42YYT-T_tuXwpoYh49B0HriyembSfb5FVjm9a2z8-WJNWo4K_33FCi5s6h2qEU3d_j3S5HheWWKHiS7ELrKG099VO5BVQKYH0bnkpy7bJO3fTrG0XnMxA-oCq8Ph76JGq2Eoaviml3-0IPalw3ucKcaemuGFxT1rXOLwcvCi_U9V-JUUNSqhX8B3UBQ-WUTczSNFpyE4Yy9rCKsraCsSTMVR1L5MWvgZRB7OVWtmcueT1PDsIO-qswRxm6ki6scHvzMM_pIQj1fYU0BO6levecFw8T-QJ7rK6L0hzYR7edIaSSYlDYUuJUBz5x1ZboXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90725">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr4SPJvkOp5PGRyKOF6svF2uC_pMtFypheBaZdDJBxT8OaOhnb_F3nMIwWBki7fKkhhid_QrVsfuLX3SLoy0dsmFjlpodpIGue-EmZFBDjL_YLz2tuG_Nh9unnkrFoPHSavbtKfJ8PAZPGOhhO_xbAZTNpEKYWXEy9sPEtAWYyC7VmSYAkwRAOf80anvfe1fwK_afpYWDyqoD7rBsb-GaYALW7NJGFZKL127tiDRZ5X3BhPj8oNcU0GnEOgOkkIHzjY4euM0heJd1ofUZTF18zu5jzF35hjWv14N7PWNpbBD4__x9gPnsHqdYlIP92oEuMbQcTSldyeky7nf5PBv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووری
؛ توافق اولیه رئال‌مادرید با دامفریس حاصل شده. کهکشانی‌ها میخوان تا قبل آغاز جام‌جهانی این معامله رو انجام بدن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/90725" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAWefkdKtO9e6PRt1YirkiCfpcDiUuNgTms93frdoh0JktvJH7dBu9anMFnoBma3RWP_aVVh62GZ6Uqaiw3soliwcCoZVa0ohzifN-LA0zTHDxVuMU79fI3rEdTLWQ4Odws6d1svKxKl7PP7sV5sXzVtV-HL-_Av5hOvwbYN9VNf6VGnwvUidAZq-hxfVV5wDeNXeaRfBiG3lYOMdfc1PKpc0PKXPAJ2rPj2TvdopONsgfEBFJmGw8wx1cyT0fy8w_hPJmKpKmuRbN3ndggDZDB5fw_Tep14_hnV5QJ7WVV661lIl5_ffV4zJQzvr6GVPocv2NHNTYmUCf6a3K2wiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ادن هازارد برگر فروشی خودشو تو بلژیک افتتاح کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/90724" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تاج: 100 هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/90723" target="_blank">📅 18:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b72747be.mp4?token=XuXY_5dgeE06VqcD9xDtCWFEoP0vJgh_tcGWcyCkBZv_pcR9rf4VJaL_MQw6y4NPDjgkICOOT5hDmhaPCgjUNy43AsVMDJXnfyChoGjsnySSRWKLgGmGpLx3c8iVIAxzh3dkZXOVvy6r3p44QOlPM7CftQVMnQNHC1aGZIhtLrZj6xLEddGTD5bXM41n7pcZDwll91_G-RDTHUfHgc4ccHDmxlnJEsxLw3Nq2U1Gl-J2JG9Nv9mGb2nmYMnR-eb3rPxDh81VG7JWxzULs8HZKImRwAUBqc7sX9NmluRlObh_KmI1ZYyRSNWMBIKJeqzXdfj2clnT_a95StuNUY7uPE2Vig3YBk7JOLwi2zRqsQTnzlOi9gbTaMcVrVXw2DOv7LvI6n6_Vs7uwnoPbHqDrXo7zqmj3MsgfDhL2HBmlcgzhAljk5XjajP0oDre00jclqjQR_LiX8S2go0hB2jCRwPUTsi4_IkqsZJ-h9h6J-yK0kiVCqBEc3r1dtOJ7DXbRpVTfM1MEMX2rP8zy_uT88F4mqonLnrewtD5E0vnLCBas7PS6xKAHjm95FVIW9YfgPprd7a06JxVMrook-HUQCWB8FrSEoudBp6VvhK9OJ-4RG-TwF3CP4jvkCIBxqoRL1VE3sYgpfSL1M7oHW8Fbmfs6rRDEcMZnbmjxug17Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b72747be.mp4?token=XuXY_5dgeE06VqcD9xDtCWFEoP0vJgh_tcGWcyCkBZv_pcR9rf4VJaL_MQw6y4NPDjgkICOOT5hDmhaPCgjUNy43AsVMDJXnfyChoGjsnySSRWKLgGmGpLx3c8iVIAxzh3dkZXOVvy6r3p44QOlPM7CftQVMnQNHC1aGZIhtLrZj6xLEddGTD5bXM41n7pcZDwll91_G-RDTHUfHgc4ccHDmxlnJEsxLw3Nq2U1Gl-J2JG9Nv9mGb2nmYMnR-eb3rPxDh81VG7JWxzULs8HZKImRwAUBqc7sX9NmluRlObh_KmI1ZYyRSNWMBIKJeqzXdfj2clnT_a95StuNUY7uPE2Vig3YBk7JOLwi2zRqsQTnzlOi9gbTaMcVrVXw2DOv7LvI6n6_Vs7uwnoPbHqDrXo7zqmj3MsgfDhL2HBmlcgzhAljk5XjajP0oDre00jclqjQR_LiX8S2go0hB2jCRwPUTsi4_IkqsZJ-h9h6J-yK0kiVCqBEc3r1dtOJ7DXbRpVTfM1MEMX2rP8zy_uT88F4mqonLnrewtD5E0vnLCBas7PS6xKAHjm95FVIW9YfgPprd7a06JxVMrook-HUQCWB8FrSEoudBp6VvhK9OJ-4RG-TwF3CP4jvkCIBxqoRL1VE3sYgpfSL1M7oHW8Fbmfs6rRDEcMZnbmjxug17Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇮🇷
بازم ویدیو ایرانی‌ها برای تیم اردشیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/90722" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3-RkD9102olfCjuHGCvoBjY-dpYJypmp8hJk6aHp0KZP6Nh2tJamd8YQ90QQTvny3P2U0SKBzDHDS_pC_6GBtyUEJIPOhgdKQBSQiDOLoebpkpaXGKNnpBmGGMpeDKT5aZ7L4k9-R9ZEgMHrMQiI13GqkpkRlB9oIQzr4mLVDfHtLDa4cPoOs4plRH66h1SLm--ao6LHR-9aDJQxYJYoCxM7PHdOE5R7Zzk6zQpfB0v7BukCJegZIyZEUmUL5eJawHSn5a_afzFYVOuD2FpNA5_gy5RWdBZXWlwPXWOvYJkbI-wV5QRe7zbNRyUoLO1khc7QuXWHcyIGH1LRpwqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
ترکیب امروز بلژیک مقابل کرواسی؛ خلاصه که اردشیر از الان باید حسابی چربش کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/90721" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IADkr8Qs2eUSWaT90fzbNLJ1OYsgX4G4izFdhHiQKpBkqjbCIpSUGlv2Z1sgXq9gOb-PlvQiJtK9SzhkdroXd1Q51fOvMu4B9oXVS85KlX5QaGv-fG1UoxDxDV2NM87rFqLNM31HJU7w5q-Z0hTCavyCVtJKYwrvoOPWvJAYhhJSpkf1_RhssQZFp4v4V-ew2gfbt65mjHTy42wFBvX8xJ6h977nRtWtYrxhRwyuhDohh6C_p1_OOLo0KH_tAY-brLSWT1C6gS5VL6IMQxzGxMwC0nWhbXGzHBGMoNOU4QqK_anEshkb4N0G2SS_8YR1Pu9cqZyBdrtM2KGbMVDSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه هایی با بیشترین نماینده در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/90720" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRQntoyXLtIryMzc0KKfkwL2CdO3VqHMe266yU6dlTWWuSElTiRtFUgiRq2YxWmPiswleCICtC6Knp-xyJKDGRE6VM1NuySuC-DXno2j_6DcN7B3rXxqSBlETPmgwLjlNsWSXOc-8yCqGIhcfEt7zdHSrIgsjJtFZ8ii-YIuC01Kh_DwbIRPUcWrajLF01Tudhi15saBmlITjh6QbMohHMAenL6QEWhxxWExlDh-O75HFymLvpc7fVwgztrHf2FIW5A_qQedOBDPPysAtn5nyc-gyF_blbCkM_r9cKsM8DuN-uUWWA9HaRY1jTw5TDdA2w1Sxmyg61IIwqbIky5TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
اسکالونی سرمربی آرژانتین: مدعی اصلی جام؟ بنظرم اسپانیا قهرمان رقابت‌ها میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/90719" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNGxF2jRKlj_lghcTBEDg03UMC9ncdP-TGWzO0nWUBvr-V6KpPVtSZlbUQnXAvJl8ZxWK-_sVy56nUIcJmrASr3pT0oGfXsz4npa0nbnQuSffecbDwWAC2GLIIEJghWW0eNUE2Lzm7bMaBneEo-Am8nhllhkb0qZ-sn1_koKJp5B-EinbmZwsIlpmEQcEKFXiS-vdW9-0vTkLB0cNFQ-6DGfWUI6AUBwI-2e1e3cD9AY--UJrUtJ1HyilYe414bMlmVE1UEkX4ZqEscOxAfxyqahTGFexXjq_DKvP-BNYMzVhThZXuhRMt0QNO77gahn2dpef7QTAefbCR_aJ4XNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👟
هری‌کین درباره تصاحب دوباره کفش‌طلا
: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90718" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=ZmLixn1y2vb7JqbPLYfW1AFLr-8q5MQyKvpvNc3J4pYRLVXNXVfS_RL43HumNQn5qidgNjsX9rF4gBB4kCIHWv3fWhWYi0hHn8Uk98fSX9RGvLcNgYQ6UZlx6MM6X6du0pP0l20h84xyeqmMMohrfaWV6QY6mN8tncC4wGmJaZfgIZIc6sXGxXeyDnzfCyFw4yLNpD7VTYZmT0lopdmjKPjxAnq6vkRdknb7nOKZaafCaaJ7zrBCbU6shlQEJw4n4-5g4D981v4gZSa7iA5RMEKbXRgvCZcCzRq8CxFswC_EBZ4LHmcwRWjK_An7kzjR9A9WoIzR4g97HzyQsRDAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=ZmLixn1y2vb7JqbPLYfW1AFLr-8q5MQyKvpvNc3J4pYRLVXNXVfS_RL43HumNQn5qidgNjsX9rF4gBB4kCIHWv3fWhWYi0hHn8Uk98fSX9RGvLcNgYQ6UZlx6MM6X6du0pP0l20h84xyeqmMMohrfaWV6QY6mN8tncC4wGmJaZfgIZIc6sXGxXeyDnzfCyFw4yLNpD7VTYZmT0lopdmjKPjxAnq6vkRdknb7nOKZaafCaaJ7zrBCbU6shlQEJw4n4-5g4D981v4gZSa7iA5RMEKbXRgvCZcCzRq8CxFswC_EBZ4LHmcwRWjK_An7kzjR9A9WoIzR4g97HzyQsRDAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو غمگین و تاسف‌بار از یک گیمر ایرانی...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/90717" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">علی تاجرنیا ظرف ۳ روز آینده مطالبات آسانی رو پرداخت خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/90716" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5iXHd1wXI96Rrc0JUuMTIdF-LIvOwlw_FjWYaJKEDsa7zAK1KZHChV7E2A3xJpvT69QzLccXNkMwXIINEGe8yw7snAzqUQyG4EX5JJcTGSAK3xGLMelYZPn8Rb1DZmpgvxLpnrjW4UryIpG0VFT5QCtgeeXuMmp0TQgK03FmCasapLskWeUjda5zJUmib2Zvml1mErENUHRhWxV7L0GMJaMzNNsNgqEOjQ-2ySqxRiHbQn0rqCh4DKgBXt9xyKYf5Vr_NTc_R-DSVw83YJaSunryziQfXhtdkSYZmuWOTLsGL7B7rBw7SB2muYbSNy3dJd3Y58UgyxK7Hv7fhCISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-GgQO_MiscPwLchJGroEcfZIsi_aWLbfYP5l6z_JcFAJ5Dpa7EYZnw4IB-jZf88F7ABxZH3I-Jqb5sjCseT-2er3LwVbrePvSIBENf3z5xOA2GgfHquxIWX5JXPBU5dWsDOnNvaHi33Gnbpv2CKc21cqaaspEdTdu9Ok4V-Updj26qmA57aP_Hknrs9ZS8D5bZKwFdErVe2Bit2CyE35bdTzQEeln0MjgSUZZXB2y-2Ds34eObiOKeuPBFg5GP4GMkwsFzmOaSHcd1SG1C9IMKZp2ih8sMAqks43Bzjll3hnTFyMn6TwKoZBOFtt2ZTYTnbEcgYhUoYcGc2JgIkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcnPsWhHIwmSqI9OHJse4cnUzGDc4MKuVC2MpMgVcXrPDwnyRwTlohPqPzE_cBkNYcSSfkTePBhB5OF5n7x4M5DfydWdBspbiarcHs14Lko1zkJbrQD3HsQSLEDwwuzKLEufzBwqFtujjgtqfink3LnuahPeISVWtxAk8hEf69Reay1AgOJZICVEmVp2vWO8FouKCBtp6yaska1SGZWr-O9mvHlj91gKTV_2WYWwvffEWWop6wdy9_4KGrgJsL9XbqBQhHQIYsE5fIVXKA6aowxgGajNi_MRrYTW_bgAp6zS0D6Cz52c0bf3eiiszwnTWPW0mH_qmA0JawdWshAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQzn0veKxetOP9LYhWaBNnkJ4sQ3gIrLHrKZ2ctRqfB7aSonNm7v0sX7gRXk0Nf69o5exbcu1LCAaQB4fjshIjdNd8zCiIjzh2O6OyYP9o0FXH-GiZ_GH3stgB_9uN1-kGOORdB42rrxGbN4cb999ouA2jfjlR6eB2nkGP_kMGz_okYkZSV8G7ZUDKS9-b-vTpMIdWO5hbSkfQBxIp1GYxmHSL5d_ov5Dy1Pp-wd0TVK1H0F7t8IRzSdyBIWVFK75smjZlD8iG9E0wksn4MPFUNsC03zehRdppK9njc9lCpV835JAvwwb1eNXd7JLyUNIGN0b8t2w2hJSs_sEaJ_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نظر روبرتو کارلوس از بین نیمار و وینیسیوس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/90711" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تبلیغ جدید مک‌دونالد برای جام جهانی با حضور رونالدینیو، یامال، هنری، بکام و سون
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90710" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkxJOnWPi69M8mcSg8qaE4i83i4A1fUonKJehMVXqd3Y73-_CtaSnXgf87NBZsKpzpJKuuhWDHJjBRwHZXyvlMH8CA7F2c7Nls_enMQ-Y2owZ9YgDyvYg3r10sb7feZZqFJlBwziowV6cGtRZLkgQjFyGwtJsOyRbEz4SWs1TZzLkkcx8w2gEKnTRZmmhSG56vMXVjaj29pJAavHSInO2M1UPCLUGHZXD3Ke80ZgkZpyCV2CQfLGbrt5HlWurTC_97bSDklL6S1Aq3bJIlwum4J9k_cW2hF7LeIr7ahHN_nrmt5uBt2kWNNmM9DLTqoTNDNfCFtITq9TTem-IPRHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات
|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/90709" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH6-3A69Dpaj4cTZOegRpCFvydxe7e73kogpMjg9Rc1iVIigtj96TZJbO2BpbeAeBBVbQWNLY8H6fUBbwlAySKrhhwHn_x6nD0cD2MhorRRYGDac_YB82A7xYy-o5dq4bOO8kpzAml-iSRYzC3G2vMYrBdMMpOj_6g5VpHpcO2rwYjNKky1YwZLAtfjQIO1u57DzgPu1GfWXtNAr8qLzJMlEfPQFUAieixwYXz0xeBMPuPEbkJZUQgn6QfteSqLhXj1oVHgB4ymmhS1wZAaH2Rh8ehrVx-rxRyuK-84y8e7MH1H-1inDM5Jf0979wXOthbWjeUVwXz49AS5rYMtZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی
#فووووووری
ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90708" target="_blank">📅 16:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvcUt0f_Na0WMonfcZkzaQre9cJNcdtX5k0b9qXP2v24z83u93Ewnr8xTQiCT50Mp0v4Jp_E9GzW5knqY0e5-XOlwFvB77Cr0kXjiuRr5kPhKx_2b8fsODbxtbKM472pfyutdPhXuiDkhnGmBdYm70aKVEwtxnqa3Ukje0iCVYqdFrynv6HFT4Ob3Jw2R-hDe9j8Dp4NT6_wSgsytcb5ZkKKKfWqH3as56zIwvAbtgWAu_qCSe34MkuX4tSNYZoHIJkr1dVrlDgHeA1L5zmBuBsLdlMBNblRfXmUn_o95rGiKwZ-p87dw3A3AxhKTbOY4f-FSYJgNl9I6w88IFp5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منتخب فصل لیگ‌برتر انگلیس با رای مردم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90707" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDxTbqA3XvG-dHuPTrefV8KcwffKkPPQLTm0vaBe99GUQH7HFI7TRG27LXD7DmlIyLkV77SfzRmye1AweByWX_FPzQMtxuQp51GHBsaHRqfpN1NPwpdaz2V9ZVk6iT2LDzib9MewT3BWza0duFNBgp0tLaGT7wPAfEnZ9eJDxu0c3Q2vnhb_xdJXi1LwA5bI-UY6awPTwXT_xgYVqTxTq0hG7gSG4MgEm56AUvwvDPAL_bFg3rEwT5ELCE1lK6SoPDT6c98CSiOQTndXMMUVujzzw-Tu9u_OM8TTgRUAgqw_tZO-_k2Gm7qmy1xkLlii3uhhC9dnqgasikv0Fy69Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
عمر مرموش ستاره سیتی هم رفت قاطی مرغا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/90706" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWAv0uNvWnJ8f4oSAdbspK4XLW-BO9hjrhQBSU4-k9pv4vjrHZUJnHXY4e1S4PPvGhvDgLF6wJB0Rm-LSVVKJ2hb0x7my35D6MfqCKc2ieqR8jRxUUD3BqHsKHF3qDmG-YsaOme8mt2B1gQ3wvvhYx1lZOGIXYRqiOew09QrxtT2fAWYTR0DnznK_B4gIWdw9qu1xgefFbhV7MXR71XTvJTvr9OwljBsotQ5smXEizp2zXi8sKC0LiYmifegOvxl559P-zH3YdcSyMFZat0tsMIGug0LH_2kh7BM-dFb-ZnU9zRLjO0EETgODZy25rZgrRabn30cUvmqppFfg5-R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوار جام‌جهانی با کسب نمره ۹ در سال ۱۹۸۶، رکورددار تاریخ شده و‌ تا امروز هیچ بازیکنی نتونسته در یک دوره از مسابقات چنین نمره‌ای رو به دست بیاره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90705" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/90704" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/90703" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDA7XIveJRiSNTQqMbnXLPpAlIpDr1PQAv6j-ucjg_Oi_0fmDHaslAEJn-up_owPY1cFixMUErvVF1C23RlemFmwm45qALoHfp_oD6CYZuq91tYjqp0TebKZUMg4l27APdPQnSUTgAGrDiiHIQ7yKuH47ellkMMz1M6ehB113zATrN9fd6bIJzHv1eZufUzZLmYIi4KiBpX7U06hIihayzOWbS68qGemjiA7uB0Sw7c1QbEf76JQH2w7FSSiB5UE3SevxKjZ7YYGKVkWONofRH7ZU79SWvNwjBoO0TGLxLjSfdV97VG9RK0f3311lKGdgCHHm-F4oOEL9a7oLoJZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👀
اتاق شخصی لیونل‌مسی در کمپ آرژانتین؛ مسی خواسته بدون هم‌اتاقی در این رقابت‌ها باشه و از دی‌پائول جدا شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90702" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇿
🇨🇦
درگیری دیشب بازیکنان ازبکستان با بازیکن کانادا بخاطر تکل خشن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90701" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pavh5YPBqcENEAvAPthc5l-QINzw4LmyqWG4S9rVUBthrObI2e_z41rGMGgs4743eHBAOFFShMKjFYzd06Z74AZLx_k1z_B3KG8lBLvwvKN8lMp7PZ5pAApyDrR0_pmuvYRQNfVVbzZUWqJokzmSMOKwSSsujx9aNG6bWHMMP1RecCoVJs1dYdyojiJwt7SKK9ftpBK1WPviLETesxek-U7BHDnTDry7wJ4N146r-YT9rtEYgTWjR5zepL4zKqMmdgKjQYHjFd1jbTBY4l1KL-wMtRFOrcL5CsxfxSJ5cPzjH5CQZK-fULW9T5e8H60RZN-3dsUGowGSElGwF7A0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
یادی‌کنیم از سال ۲۰۲۰ و شاهکار پدری در سن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90700" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از روزگاری که مجریان و مهمانان ویژه برنامه جام‌جهانی صداوسیما برا خودشون یه پا جذابیت خاصی داشتن و کلی مخاطب این برنامه‌رو می‌دید...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90699" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ4y463bljzHUmT0dBDAf5UgR7Ys5ISwZTHy95n6dubLJhv81jV77FrCJKQhFi5qpqsfLZByoLrgTvmjqvQ4HeW2V3VaQc-_xC7E8A-6g8oIMiUVmwmy5NWKI9Y3Ph6jG5EioZdOKWxarAP_D4rBM19a4wL4PncOVBDV-5_Pw0tGX0vXun1juWaW7JPCH5AkB9-qs3xBPuwgTv8uunQ03cbygBPQvuP_P2fxFzsVNmkms3pLc32ZwO4QFwqPQJl285SubxqCadi7BFuVroqU5oDIcaYrMm-7y_VUlWi-I58sonS4e1k9D2CMp3c_lii36KDM_5_E2NP_MnoGfOejIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🔄
برترین پاسورهای تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90698" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛑
تنها سایت روسی فعال در ایران که درگاه ریالی امن داره
💎
شارژ دو برابر با کد هدیه
IRANBET
برای بونوس ۲۰۰٪ این کدهدیه رو وارد کنید
آدرس سایت فقط با فیلتر شکن روی سرور کشور های آسیایی
👇🏻
derbybet.org</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90697" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REPtvDgWqCiAFjY86aLlHApG8-bd7GBroso-sZ58bWpFPC9kqEVx1PVLu6sHj-CSEGxtvNGvD9MEGAqcbbd9IYhZGRDT1XU6IyMNEXeSAJcIdPMa--SJMD1HB9iFyY3G8aYLK5s_Ogi29xTqhhh7GyHAltXkDNiylI5xqRa88WRJYuHi2ORWduYsxZhvPgCz49b2h3sVfQSwk9vUP7CfnY5ozBACN77XMBxFskKKf6MfIAA1YX_h5Moqm3gkLKoFQUE5U2mPl79D1IohyKX3HQzq37II77tkaVxbB_Q5MbOu7cIQB5c0WLC9SvxawsXvk_ASSzNc1EK6e1t_R3xCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
Derby Bet – تجربه شرط‌بندی در سطح جهانی
━━━━━━━━━━━━━━━
🏆
دارای لایسنس رسمی CURACAO
💳
شارژ حساب با ووچر، رمزارز و درگاه بانکی مستقیم
💸
تسویه‌حساب سریع، امن و تضمین‌شده
🔖
آموزش گام‌به‌گام برای شارژ و برداشت
💎
شارژ دو برابر با کد هدیه
IRANBET
🎁
100%بونوس هدیه واریز اول(
شرایط
)
🎁
100% بونوس هدیه هر شنبه (
شرایط
)
💈
آدرس ورود به سایت
⚠️
💈
دانلود اپلیکیشن دربی بت
📲
💈
اموزش شارژ با کد ووچر
👉
💈
اموزش شارژ با کارت بانکی
👉
━━━━━━━━━━━━━━━
همین حالا ثبت‌نام کنید و تجربه‌ای سطح‌بالا و ایمن از شرط‌بندی داشته باشید.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90696" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkKM7r-FXArisr53MMG5snlIr6Nn-snWWeyxwSHfE8KOH1IEm7QOoHVExRrGVWZ96nQdrAPS_72iI1CEJCGlvKwb-I9R1X3sD2jTBzk3wv4gmUHUKt-ANdqK2htbecxQq97eH71sHe6v-xufRVfPTz3eA3ALSBxUFtB4paw4z1G5nUmr65HjWechWDONt1YW45fJK1DYR7xzQGRgJqvQ6iPjMlHOTf8y_S5cdx5O_WUj1_XiaaSP_bstHMQGuyQbzLr60V-BV7hBBK9p4Y-DD-iN4ZXnoWYzw1YMzUbsX7GV8kzRStmKwmNra4x96fbMwKHZBop-ERMjs3-FTBDLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
مکان کمپ ۴۸ تیم جام‌جهانی در یک‌نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90694" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90693" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuuReujj-MhfcNn2dRK0jfwd6GnptD6pfkkDHjWfL88RhHPBPdQ819kC3B09mWqPHXUlHtkXWnLSGS0rK1ne5IadmQWnGYBsNHeD4nfBJ7G8YwPED1O3Nm0RPnZpqnEJHUrHNaLdBo99c-LqXCUTWqkwTUTgQcq96qHEkFgetA4HMGYDYwJ2D3SiU3AKLxmRs1O054_ynlRAcGaf5q1LHjl0_PicMOatNHOLPoq7E2CdTCSerRDpf2R7TyyLP3QUdqjlFgXbxs8uRd_yQtAQI_bc_6S3qt2hNmVNO8xlah73v2ISnotPG2F0Gt0ZwfZvWTChFKqoBtaNHezexKgHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
با اعلام رومانو، بارسلونا با پیشی گرفتن از رقبا حالا در آستانه عقد قرارداد با برناردو سیلوا قرار داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90692" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW50aFWr8ij5270_hUKafo0GZ9RHWk-RGCTKXYlYYFodcwiK_j29euBNLpOTcdWGFFeS4ta-rzvZB6XIiNTBz3ti3dCQ3QhQ7kp1GlUYa9RGyEFdfy7s4RpPNNkvEuzTNwYmim8FIeYSP6Nu4TYfd7yWU9K4l0aN_czolfyjow3rABpR7jCfWTn-dKZTbwvDbQNYpF0uY6-YvKNrpvcaKQt9GbmVnEly0evGDIatS6Q5bFB97bFWFgQDj7xOKyq8gkijiCa6O4f8rAylUHRjMXuTLJPuTl7hN79wS_7AhY7YZBJV7AQ6W0y8AuiUVobKJqJ1KluVEl0pJq32i55qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه آمار این‌فصل مثلث هجومی psg و آمار لیونل‌مسی در سال ۲۰۱۴/۱۵
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90691" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2IZK2AaFvJELp-xD1nBuQN7G9UN7dkGXE50LlWrP8itMGkf7sEmz6BX-wc2RIfVv-Z23Jcgu0yELR9CFfVAWeWbtJ_ms9Aa1rVujDT-1BfEAJ0K8-Pow6ZaP5GjxpwXofeu-U0t2AuB84Si4efBc_nALyDL_Ok9nNa3qt0TiTtm23GPqWtT3L7WnI9mgAZTYxcBQtIsk-efVMhysNnJJnYsUgquu8htxZhyxEqHbb6afy285E99tb4pByI2aO_TZVKTVoWOBOezBS0P1Ih99Es6SkMF31LDuGfr5fgTfj_HF6fnHzbi-4xsAE6E8EHUqBCKXeZ0YzLMyWCEuMmKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9DSqRQOlSfWczAFAEzHpVRlIjWR7FHzPOFVzDjZ0dKlbdm-0xdA1a7vwmGHZKTClW-8Dh5OWmFLAIDKYIFa_CZkitrem01CF2BW0gJimr7WYO5WzEQccfHmL7Uh9MFjhavRnS_sGUxj3vA3114CNdqV2b6XRdh-de_HTTuOMrp45X5Te8rJJluf8_uBYP8RYqJAxNjfvyqWktcr3BjZ4vWKZt1dU5swrCwUKl6RbKAIz9htvG6QCndvlL7FtK-1ha9czLZnrTBrHITtLZ3rQ-4vtNQPXCseqnU5RPss6FrhXJRj6Bac7R-Uzs6nIZKzE7inYJ63xEFHfL9JjDspZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW1pt7f_eq4HuOwWjR82iWfRL7gHokOoXH0sZ4Y-brrCELYrFbBrgIFZF58o6J3i84GZ6TCx3B0LEUek6R82segD52bY7m2cPr3R_tjxMWND-J6NaIjR1iRxWH4SLGKxu72pnOq1itSvWSw8t8EKU04Zdjs3svAixugV-A3MQRpXTWq4dVS9f3Nj0hp_68V3DX0CcscgDWKGbgTcivDIwTpiI_4m1KAe1zz465ocG4iVWrIZAmZciKvenpQYPT9fU5RL0rw-QWuD1TpI6Di5dwOzQQZ37-YbTTDkTJZUYC_39KrnWiHtt0aNjlLxWWfbYpytN_5GWQdeaHG2CPOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=FR6yZQEy0KNtByQP7kY7Mab28GKWblIHMMiKQhODC-8TT3YmqnDxZRxu8Cgvqjv4G9Rr-IfdI5pEVeyzN2cyujt5XuAiOkVBtHOado2YQH4lJZqVwnJCp3axw0yZvaqZ3uqDw3OvEro9RG4xuB3mrSbpTaFjjOxayPGVo01KKuz9ZhHopEZJn5xPkIABy3phKawItqrCNAdTTEpXPktBlr4_8SPAFSMVDZtsNXsPvUYn9T107NfTW9Yn7dwyf67J_JCzT70cqIZNtq7i5b3hfoE9pelDb4D1xr9hOCwQ9vTwsNnL-lT5nV7mlFAGlglEQ5YaOiSnz-ifGu0pyaiM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
⭐️
یوونتوس ده‌سال پیش یه ستاره‌ای داشت به نام آرتور ویدال که اینجوری پنالتی میزد و رد خور نداشت سر گل شدنش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90686" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90685" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6tkA-q6Hqpi8NcIfSmFP_-kDeEQKkHteEglo4wWBelim3-_Sh6vyEdHw7vZZglaY8O93ablJPjXfvZGEKSyUKw4oBhAuNDZbnqIZ9AN1XWxrRQnpzRW5lNd1dm_J1L57_HompWD8jRACh_YAmzDPQNiihgmycSiBoa3ZKv3w-GcG47Eu4ifshcqzQQgfz85HxHC_ILI6FVxXiebY77Pv1bQfsKpxde5zDquhlj5RWAk4R8DafJz8ZVVKXxhywGh9bi4GPJ15j-sqII0_INLE-fG8SCPvNvK4mGubaDqO1xL8L_ifTk5ZFHChvsUmQVNT2isgc3PuiO0NLqcSJEPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90684" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2AQzWC-pr9fyYMw7QUg2IedOvlAs8cyyZiryRjHViQxnUDTxGy3QUYhvtrNREkcXAaxORse_Sbt3yQ5F6DVU9H4s2Cm66PujOGG32wQeD158f1b75gGnr1cGqgAldQVr7cq1H4bEL6qXwdxpMk9KmyIRegQ1j5kISfdYR7BwZX3ViA83sj__DI4-E6fYc_D9ERNPAUod5fGsv00-LJVcp1V9HEWWcV-e7wNeqXCKPT5L-OziGc6fsatTpbhaBEBl2Qt_Sk1nF0vBH5k7AkGi9TeCLiY16ZtBY3AKynUbFo-i6mKh0EAw3ijmWibN8O_phsuCnOfXEzzwT-zA7pWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو: آندونی ایرائولا به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90683" target="_blank">📅 12:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmvwzavGEvu19_TWztWIszw2u6LT3SSlFsvS-4DTorh0WAMFJY_yMTnORXHTlGCUy7ryl0FPrDGc-kr2Y8maYcgJARFE0_ZzTZKX5tSu505TcrRwXYMUd7K4usDgI7OZFBMDGxnsEfamBfne1skn97yejAxDZ8eoAFpzctBpHrzUpw3oFdtPsCJKJhGUexW-nISNPHnIJ3OVcN5FTvVnS8NC5zAVPsZO-s3zbx7Xkx9-PyZ4kN0erFsG2EHFRpzlSEetFCrHotxirJgEQju6Miud26ADsYDAvfMikbXXJ7R8Jegs_XL3fTuFMyqae3KDruyfWMj0ETPiAWgatGRy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90682" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=A_1YpuBDMfRYIa3u9XCQ-ZAjaMqM3uQJiSPUveMf6WTeTaYzxkO4L5A6Ull0Q7q3WakiU6kGNCKq4pjTISSS1zj48bWx83y-omUJm5Hc_QyJIiqeKUZnDMO1uh878IohUs41pTaEXu3xcs2aBu3Wz-wGDa43JZJJJ2e0vCUbKvtWqGkL7d5RP8rKuuzJrfNPrSaKrVElWkKw1ii8HCHEk_v9q3jqFPMpEdUdU5suWkZw49N-qgLhkieb3ePRIMUo5X0nEtr4iT2KZz2fKfhJMCzEjFeFdJAFIxobl3nCJxlfbOAi5y7Hy_9k4vMK-e3dbg1bgEXQJy9-r8-JSzm0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=A_1YpuBDMfRYIa3u9XCQ-ZAjaMqM3uQJiSPUveMf6WTeTaYzxkO4L5A6Ull0Q7q3WakiU6kGNCKq4pjTISSS1zj48bWx83y-omUJm5Hc_QyJIiqeKUZnDMO1uh878IohUs41pTaEXu3xcs2aBu3Wz-wGDa43JZJJJ2e0vCUbKvtWqGkL7d5RP8rKuuzJrfNPrSaKrVElWkKw1ii8HCHEk_v9q3jqFPMpEdUdU5suWkZw49N-qgLhkieb3ePRIMUo5X0nEtr4iT2KZz2fKfhJMCzEjFeFdJAFIxobl3nCJxlfbOAi5y7Hy_9k4vMK-e3dbg1bgEXQJy9-r8-JSzm0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇽
مهدی‌تاج: ما کاری نداریم مردم مکزیک مواد فروش یا هرچیزی فروش هستن
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90681" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw3buVRaegPUwq9VHNsmWGAhDNy-jC9M9axH9O_bW3IbXf-2JD11fdr_4yKY1PZShIeQ5xCYL85YlgX7Yy4IRH8ihZi-JNke8kGljQoQMXWzTWlOhImQM-HwJuu67uctVS8J8uu6CkV0zNoU1Iz6aerT533xfn2ZIINhJbQvmFnCayd48-LRAt77rnZM7sG5D2OqNt_PBJaxf-sTP6njm58z4CiXvL4idKWrVEDoOeGAUjC6C5EpzBzwGS1z0CsvmNXOLiuUN7LE-P2RV5Imc60-D9dCseNszRWnf5rqTwgkt_7fd2R2IRNywrwS60_Abiw-_e6CPv4JYmuBIHFf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام‌جهانی رو از صداوسیما دنبال میکنن باز باید این دو تا نچسب رو تحمل کنن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90680" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=XsG20Hj5QAOYwV6R-dSOP87AVvdxPEToqULVpbqj9mKtcN2AnzSYGPPmci_4149F3Th2gRW9Qu2N-zQn-6REhEeEKnRDHrn6ppQnjGEwvrvGkTC3oEWBqA6JUZWKi5cZhpiS5kskenJR3Sk4ZcUua2WMbeE8SfdKcMsrWCJUvk36cDgvfPIzWzDAFv0Eom6Iq4P2YvrTpbXBcUBxSs5H6PuQ5I42F4hzftQSTCRmX7vH7boTSNlyia4t09MyskjxGCfB2kvgG3OgJQn6putPfqFUPInSa8Kr1NFH8yB1QH5morJLGCPuw6wd4iXaY8LCrE9wSWC98LwWHTeUD4I2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=XsG20Hj5QAOYwV6R-dSOP87AVvdxPEToqULVpbqj9mKtcN2AnzSYGPPmci_4149F3Th2gRW9Qu2N-zQn-6REhEeEKnRDHrn6ppQnjGEwvrvGkTC3oEWBqA6JUZWKi5cZhpiS5kskenJR3Sk4ZcUua2WMbeE8SfdKcMsrWCJUvk36cDgvfPIzWzDAFv0Eom6Iq4P2YvrTpbXBcUBxSs5H6PuQ5I42F4hzftQSTCRmX7vH7boTSNlyia4t09MyskjxGCfB2kvgG3OgJQn6putPfqFUPInSa8Kr1NFH8yB1QH5morJLGCPuw6wd4iXaY8LCrE9wSWC98LwWHTeUD4I2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇺🇸
فرهاد کاظمی مربی سابق لیگ‌برتر: وقتی شعار مرگ بر آمریکا میدید دیگه نباید گدایی ویزا آمریکا رو داشته باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90679" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=GEZoFa8kj0ayFChwPwDu34QqLvFpdpQV5PfvxzhG_oKMuNE28Z5z0l_hECbZwetEJ_VyGx7jm11fdOUFoDXQXzjVfRYByMHKg7BXHMZimzFHdlxUHdyCuVocJnEfCBO3ei97OkduPhfqUDTZTPgzbrZIeRFBMUegDd9Osczt7j4AzzOfVHTSoOsijycP93oUdTZsV94_PV67olG-OEttzvVMnQcqqLcNnEC9JAbHclY8xDQgkEF52XJUFKVtlKwAb7EZC4V3nHOqkVnl2_VoyJpjg8c32gIGQFo7xOdoy2ZtmWa0-2KFM_RFz4pfIjFfakv-oubZpS37q9tqqj8BFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=GEZoFa8kj0ayFChwPwDu34QqLvFpdpQV5PfvxzhG_oKMuNE28Z5z0l_hECbZwetEJ_VyGx7jm11fdOUFoDXQXzjVfRYByMHKg7BXHMZimzFHdlxUHdyCuVocJnEfCBO3ei97OkduPhfqUDTZTPgzbrZIeRFBMUegDd9Osczt7j4AzzOfVHTSoOsijycP93oUdTZsV94_PV67olG-OEttzvVMnQcqqLcNnEC9JAbHclY8xDQgkEF52XJUFKVtlKwAb7EZC4V3nHOqkVnl2_VoyJpjg8c32gIGQFo7xOdoy2ZtmWa0-2KFM_RFz4pfIjFfakv-oubZpS37q9tqqj8BFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب خداروشکر تو این مورد هم عقب نموندیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90678" target="_blank">📅 11:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlQZ5RzVtXwCl9dQQj0dTY47CtVGqLssRKuHVCoToEe9_G0nJZ2X5vw1C7HXE0vBQsoIU1h-C_k4c6BXQ9R4oOXDiWPUWGyoIeHJF41OD1ujv4-wgiTe9AVtBnjBDlPJnfxkPt5PLEN-n5JjCkn9kU2KgVIyqB38uwMdjaUu-i_tscy0DSIhR89cOG_fgs03O__hHc8E7b-_o5nQZCWZsnuRxEYo3vXJxV01jH0VQ8mLt-aADQqnvLESZlybtzQQJLLLkA_OeODQhkDxrEvBn_AAHaAcjAoqnEWXoKhv8SPcbIumOnMsuGuMxgeJfW6hG24F_Na9GsdlR2GCaNABPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjGALmm6xHR0j5srQPFiSDg0sO4Xt6ovvLQfy7dENkQjRQw6sBIZkkP6f6GxDXfygBPvC59v4Aw9nG_qgEud7eAEwVumIhmGE4mPfaKkbqCHmkT1wHp4UGmvfD9KG689Zgs6EnWgTSAmISmblSvugY21U_JiXt_qNFTtLcDSGcs--HHIg-1Mv_XyNWrFYSZn7Oy_kl6q89Nt9tmMeO0BPhq510tuLW4VDGT2t7g3HTe4rtcgsVUaTvVzG0fSGKBzkbjpJO1vmyJnce4zmy94EXuZ4EIabZ56Fp-K6pU4GlC-fun517HBPLl4hwU-YTjcQkJpHtI2FwXDPgEfhFVgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9-c2KtEdGgqpF8g6LLs9zpdF2g2FC0MQ6h7e11rCML_86S61JvEBRTPk0-vohz9Tzm5d-SjWwnz8NgLU8HN-hBDgXEt9PcZqGY3Q8Ot-BzcOE28n6EfSd-XWXbu0sAsnQyX9NaqHyocDr8tpT4o8stNDrXjDn1lwF0kS_6U97eSAa5IUrEF607hze1FJR-TPSDrZr5d4togtEZeiJFGh6WJB-PlmBbrVqCx_Tp8SWpkfw92vTF5EyKD8IkRrwBUMjmdun3It-fInEjcFbybjDBWGnGIRpgd4K5dBmP68LhrZSjYFL6jPnXFkkKkFIftcTVDOAK97GQIPVo4mYFxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSVcGjeSBM0wm4CUJXXgXlyevVb_m2R0wHd4gkFzDMVCUm3dDBJXfTNOGJvJ6gmpYiNWMR3NriAdEovPM4stT2NNmuHXWzFogCd7aPf9Ok62gzYLxwC5Co9CwXtBQ5bylWpomET8NcRJNLUNBp33dSM7qcal8CGhPmHLmTtrak3oFVXS4HYBo6XKmwfaNTVcItFLvltPcBCRosRkPLKsBXivUluMT7RWjckOgKULXP26agvAYR9B42LP_J7MLwXFKfECBhgXYXqQycvTpgki0b26a74Wm1iA9luxbWCvB82Hj82K--czw8b9K51nsBBw3saeoInqTMn7VsK-AmrP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
آدیداس از طرح استوک‌های جدیدش برای جام‌جهانی رونمایی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90674" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=iRc4MEmk3iK7l2LWDLkOyqfEiSFjyDgfrqneUy2jh3qUqdG2bmblesgb3cbo3V6xSecHg7odm2Q3PStYbSkF3OBu7uOp5lbctDVFJ5KYnGJzGlEn0ZFXyQ-L08lTwrwTeQQIug_i391HfAJyFbfF8hdSCew0gN3SXxBAkgAtV1gTXFoHWe0jSMqAHlzNUvEiiJO6jmxdM16caSBvN2nNWB7bBkAg_DMR-DQijGd29V873xlwiDmjHLJ_WxIUGRfASVwBIhDnKRddUxV-yxBFTHHUdwWdkiVo_WanQGg4HFH1PAS2quydPMH5qAgkuDLnQIKUpwE0r7Mw109ytiI17A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=iRc4MEmk3iK7l2LWDLkOyqfEiSFjyDgfrqneUy2jh3qUqdG2bmblesgb3cbo3V6xSecHg7odm2Q3PStYbSkF3OBu7uOp5lbctDVFJ5KYnGJzGlEn0ZFXyQ-L08lTwrwTeQQIug_i391HfAJyFbfF8hdSCew0gN3SXxBAkgAtV1gTXFoHWe0jSMqAHlzNUvEiiJO6jmxdM16caSBvN2nNWB7bBkAg_DMR-DQijGd29V873xlwiDmjHLJ_WxIUGRfASVwBIhDnKRddUxV-yxBFTHHUdwWdkiVo_WanQGg4HFH1PAS2quydPMH5qAgkuDLnQIKUpwE0r7Mw109ytiI17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بدل‌های کسخل و ایرانی مسی و رونالدو:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90673" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATxrkK1cc630bsTypxryRPrY8WIf5eF47wtgqCS6sES9AIKesX8W_RSK55uKMu5ial78NGry7I9nP74ND9NFMHx9O9D50Fca1ZOVeRjp7emEhc8WRtUM6RJzeHA0THvPX_V5YzQXstgTM9Mjla9YSUHJ7JYWrq_RkaeQCXOvX7vUwas3iuOeYVL6r3Ia8QqohFoBn0yWuSpeBr_x9JnDShRsyPYKryYfhlY6j-7eHUhVd5xntRwm3XQ9iLJncscO_8dDXcGvNKpt9LVV33UAH4BrH2gjJRAUAsI0UuZ_tX3UIMBh2hfU9V_afDguk0TTCwOFVJ0pdYaHaY2zjJJ6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی سکسی گارناچو
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90672" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=vqiDzlgxGmGCgyeTd7nJyTWlKjlZ8yesuygDAg2cEZPMBgg40LOMgdGnOfAKLmw3s5B9E-uMys9mmyZi_Bt-JVXDQ2SwiuhvE4r8crW5pVM5i6mOd8H_lSpA-lzbpgrxIeZy01-DJnOUmg3ajZjJZR9KSFX0FT7vds2RBZT_R-y2-rwaPQLziUXsoE09AOwQ-1cK3nvXNHVXzCPjwJdqAsub04_RpzyYPSpLgu8RZVSU9P2Odm5hJW-t7Wq3n6fh7j1GXm0OylER8W8SCdigyAuB4j6ZvdkemZqZvEmXd3iT5GlMP1s0fMnHWglctH-HoK9XdguTjfvWTegyszZC8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=vqiDzlgxGmGCgyeTd7nJyTWlKjlZ8yesuygDAg2cEZPMBgg40LOMgdGnOfAKLmw3s5B9E-uMys9mmyZi_Bt-JVXDQ2SwiuhvE4r8crW5pVM5i6mOd8H_lSpA-lzbpgrxIeZy01-DJnOUmg3ajZjJZR9KSFX0FT7vds2RBZT_R-y2-rwaPQLziUXsoE09AOwQ-1cK3nvXNHVXzCPjwJdqAsub04_RpzyYPSpLgu8RZVSU9P2Odm5hJW-t7Wq3n6fh7j1GXm0OylER8W8SCdigyAuB4j6ZvdkemZqZvEmXd3iT5GlMP1s0fMnHWglctH-HoK9XdguTjfvWTegyszZC8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
🇸🇳
ویدیوی جنجالی از بازی پریشب آمریکا و سنگال که شدیدا بوی نژادپرستی میده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90671" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=urE9KbnkceMJ4uLlduy-XS604vp-n5cjUWlMU88B8l9BtXlkqMVamBfGSUueeJXwWyBpuLQkECNp3tZBQ6uioTy68H2LCmCnYMB5wMhlDlNlh54o04GTIa7ddGVVwna5Ma4dCQyEkSPAeYu1yzBzl3uJPkJWMeIs6Rs5Xpcu4ymHu-HLj_lj4soaW4QAXOiEbSOhdzryQ-Id5ofPDwNS2SvQYE_mKkW7aziaJ2-4AXgvtaw7qY1YmkPmDx7cVqluoXLTS0QQKyCl4VLbXCdBIjS9b4dvubjOL_P_fmwKqY3e0ybsxZGi_YzGtJipA_5OdhYQ_2AnP3xvqgNqWwHCIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=urE9KbnkceMJ4uLlduy-XS604vp-n5cjUWlMU88B8l9BtXlkqMVamBfGSUueeJXwWyBpuLQkECNp3tZBQ6uioTy68H2LCmCnYMB5wMhlDlNlh54o04GTIa7ddGVVwna5Ma4dCQyEkSPAeYu1yzBzl3uJPkJWMeIs6Rs5Xpcu4ymHu-HLj_lj4soaW4QAXOiEbSOhdzryQ-Id5ofPDwNS2SvQYE_mKkW7aziaJ2-4AXgvtaw7qY1YmkPmDx7cVqluoXLTS0QQKyCl4VLbXCdBIjS9b4dvubjOL_P_fmwKqY3e0ybsxZGi_YzGtJipA_5OdhYQ_2AnP3xvqgNqWwHCIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇧🇷
صحنه پاره‌کننده از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن بود
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90670" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=cCP_2wULC9d3-ntbPvufGVqYEeqk3rogSZ-yayuvwT5Iv4stk3pDg0--MzV5xPkweyuJ1thB9pZ6Nv_nGpXYSLzpuPnTPpaVNAZNsqdYCA5GH-iJ-VyimngCrpQbK4_XhfginuOWkQwQwSpudVL7-m95u_xdw9hFXYqlUXtQ1FeVyTz1TZYDGjd1m02I-k7ZXgDLSUoB5oCnlPrqxcDapiO56Bhq091ckmFkuVCOyNB4Zb_wnsVvKZNq1a6mwTcok_AEPSBjlg93Q0j8d54ddAfW-4Dm1Tx8sbv0ANtp3pwEJ7hHZWRsqYppZIL-MMW2kYqNpopT17NI7SG9rLRzmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=cCP_2wULC9d3-ntbPvufGVqYEeqk3rogSZ-yayuvwT5Iv4stk3pDg0--MzV5xPkweyuJ1thB9pZ6Nv_nGpXYSLzpuPnTPpaVNAZNsqdYCA5GH-iJ-VyimngCrpQbK4_XhfginuOWkQwQwSpudVL7-m95u_xdw9hFXYqlUXtQ1FeVyTz1TZYDGjd1m02I-k7ZXgDLSUoB5oCnlPrqxcDapiO56Bhq091ckmFkuVCOyNB4Zb_wnsVvKZNq1a6mwTcok_AEPSBjlg93Q0j8d54ddAfW-4Dm1Tx8sbv0ANtp3pwEJ7hHZWRsqYppZIL-MMW2kYqNpopT17NI7SG9rLRzmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید هم واسه جام جهانی آهنگ خونده
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90669" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psuKBJRUNNDaK6WEfWt3iNCOK136o4a1r1hKO6lsE6fvdfSGFD85aH7iLsE9RNHG5KJ1QhUOPHe4ydu4qmHUR6mY4MISdGxAHO8UCpDPZqA4fDslkBnd0LuSAEQozQtQi7rGdVFmgylcsYKnYs-BLrxy03hv6Mg8m4Kikef85LCzzhaz6m7alQFoR1SqmVASI4rHQi3m7rsbENMR78d-hHOL5G9rbzAIeCNaW0xFPrDpp6qnw-FP7s-M8RcQNUJU7rOOAtVumO2B4dPnNP-0q-5yp6R9EBdv0rKnYr068z-Ioz7CAP_weKG6zsWCV3Ed5VbWcRGX58D8raPx3S-Ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول چلسی در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90668" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoYrflBxeSXqXIC-OQvgRV7AZdkgUXZFBqQndR8DyEyCIL0RoLydvTv_FsyZ2_YP0YtLoXBSvojwkQebWW1f7wO4H9cv1YjKfvM9t3rwB2by1O-tWtzKxx7IIzjzb2wygz6Rqy6RR3POyS7g55AZzDqYQidW3EOqI56vINy4YiKOfeB8-rmczQRHG0nS5s6D-H5llU0l4Igt7jFkCn5u3CmuF3JaHM5f-ubodc0kiogUtITqi95qT0YHitONuTkw5Kfunnf7hCv_vEo0qkU9vr5M8-O-58hPag1vHVjG0apxfar5_OowjuGz1tI_XD3v49xrID4yu_Dav5dD3VYdmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد دمبله در سه‌تیم مختلف؛ معنی واقعی شفا یافته رو در تصویر می‌بینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90667" target="_blank">📅 10:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=WW45iQ-4KK0XHGXHYtLJkZYsYcqpim8_a9oM7XCSLB9x9clSN4mYoudTxg6fNKUkHfnz9FMvUND99Cty6zRrNDKmj1rjXsdbdrYIzjzbAHHduHPa4qpVpZwGPUocJgXK3lx6LMCmy9q9sGhn0zd9OCWV-aDYZqQBumG2hsV4DAj_6SIW10htXeSO2wihXGcm_A7s4lcLGTqChD8s7SQ6kV5L-9jUnmcz1sDfAF44RIUFvy-gguDoe5C0E4mpzNq2HHjXZJK2jVIS3BPadK0KFZMRmvY6MiqCQcByS-y7Aqa9zCN5V09d4nyYDmvQatUdYYhqGJL2EZfzY98HUEVGMHSzE2nOqT4s57BUk6Ko2EUlD4nXDHQD0EvuxkdcMyf60x8f2XR0UO-pBIXW1F3ExtOsuWU1UUr8SBw09RlkgBZKymPsh_i-xHifykqkrkamVLWm0cS0yAqwEOw1iroCxOr4OF6huKYzp7Hi0aGyyP5uSPB-NN8VJWnk1xpbvm5jy5MjCOZ_Wk8cdkcqIUO3F_7iQk6Loh6_UxLmjwuWt_AED-vODlDeoxQnhpA-7R1d0GvDO_rMlw3cFftabwilJMCr3_oPPPXp4TymNtE2H2FXTXDCix1Ac9MWr0fsBBfjqJmQes_ZQvg1wdYAeM_iBSfcKpdSXtpc6uP--X1n6Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=WW45iQ-4KK0XHGXHYtLJkZYsYcqpim8_a9oM7XCSLB9x9clSN4mYoudTxg6fNKUkHfnz9FMvUND99Cty6zRrNDKmj1rjXsdbdrYIzjzbAHHduHPa4qpVpZwGPUocJgXK3lx6LMCmy9q9sGhn0zd9OCWV-aDYZqQBumG2hsV4DAj_6SIW10htXeSO2wihXGcm_A7s4lcLGTqChD8s7SQ6kV5L-9jUnmcz1sDfAF44RIUFvy-gguDoe5C0E4mpzNq2HHjXZJK2jVIS3BPadK0KFZMRmvY6MiqCQcByS-y7Aqa9zCN5V09d4nyYDmvQatUdYYhqGJL2EZfzY98HUEVGMHSzE2nOqT4s57BUk6Ko2EUlD4nXDHQD0EvuxkdcMyf60x8f2XR0UO-pBIXW1F3ExtOsuWU1UUr8SBw09RlkgBZKymPsh_i-xHifykqkrkamVLWm0cS0yAqwEOw1iroCxOr4OF6huKYzp7Hi0aGyyP5uSPB-NN8VJWnk1xpbvm5jy5MjCOZ_Wk8cdkcqIUO3F_7iQk6Loh6_UxLmjwuWt_AED-vODlDeoxQnhpA-7R1d0GvDO_rMlw3cFftabwilJMCr3_oPPPXp4TymNtE2H2FXTXDCix1Ac9MWr0fsBBfjqJmQes_ZQvg1wdYAeM_iBSfcKpdSXtpc6uP--X1n6Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
استفاده از گاز اشک‌آور توسط ماموران در بازی دیروز بندرعامری و شهرآرکا البرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90666" target="_blank">📅 10:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxYiu4wZ3qmxPst3E-BKc5qWAITAMw4w8T0OOXeBXQCK_QSy6L2r77NT9pUEalH-BUOQku7kux41iZQzM4gNKts9v3i2lJkLxXTyGhCYMJYfOsGxaBTy-8lXKfbt6J34P_LazOZZOnLoO1EHGp9Rmudb27oQJq9UtU6tHMMVNDs6MY_4lThjifzDzOsz53qR0QsSAHCXOJwgQNhLBOhijkt3WcOiAZ4pFPyzTIvBE-_jbXK9CSXiDE1QmsKdEhs7Hgr-XydH7oeIbNvQubfxI02fziA6oWMOc180sLkPmPp1sSnBUbJAy_Ut7ExOQuz5O2uzNq9pOAb1jIXlVlIvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 بازیکن برتر حاضر در جام جهانی از دید FOX
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90665" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95b443280.mp4?token=pzu1LAmaLCG7YPARSY_TI2_QPdknq_TSYOe5q0FU1Fw1nia51jn3RuTz7ymbhWoSFtgFdbTGDMmo-OHuSHHCAGLUS3tuala3Pz0hgSKPUIgLOnA-Rdl_KctQNGkeUTwS6yXhIYLfQG1gjDqTcnxkMWkcd0LCYlBvywu0HSUU1JxOc0LUbPN2bZUPqFjw3fCNsM1Yofu0pgG-5tPw69Ive3XM6nSRbMVAHA7km6JCKupTVJPfQljoYtmX3yw0HP6SEB11bN35kihBLo4_-CkVH_U3UzVF03-gYrbvCYtbZnuw2mvJlnPZ3TLH4NNrGlbw_2q9eJ8iBXRBU63ebh08vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از لامین‌یامال در آستانه جام‌جهانی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90664" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j38rgIf7aiIZgV1Gr9EBwdqqWFGTv38bKPNgcRT93vHFgFLWBp6sWqgSW_beI7XJOmsGhCg-LyrXnvbwjsAu-_GR9wPFLU9z2ZkuM_EMkKQmeCR26OOWO5TUfEiGe1QAAhgynzc7CjC-oqq5qgwByCk-y_QNBGWW9s82SWjY1sVN8jsQX-ChXHiuovayy2M0aKsZwyz7FkcRh56kgiVcXF-y5B8HBPu0UO_86n3vtsJWgyKzvc5ApxFvwFZRGrscYkl_S4RekvH1AzsT4aoh-Qkk9vwOuDRdDV6KdERA7KmE1L892eTWC6jofd7nbE84x1ncdLt20BjW6M-xpSmLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⁉️
🏆
پیش‌بینی اوپتا از قهرمان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90663" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
نماد کشورهای مختلف در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90662" target="_blank">📅 09:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90661">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEllhnUpzCKqJz0pNnL1fgVzlxcmP3g8oM7laX2gygrjJch_mFZux2F2Wl0G9ImfT7Oxi7A3BsxhA6KQEc58TdR7niWce0iI4IK5Se-k-VgveGwfiFmsXw3PcuRYD5eAqO61gopp_ZGObfianwJ4UUqTPyVL-g2_JHahnCUK2ZqkAaEDrKyHMQZjk8eyzW-y6VcYexg9cW3wVSwwMrZstf7rJ3KUuI13zuheu1yG1mzbV13xpHltO3AgXV_-i28eFTqJEjcnvB00Frgdj7t_QJOokSS_NxeZD0lOfS8kQjjHrobxUmP951YudLSGpwhESRcLwWVS_Cg5LJZTmIL3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال و رقیب پرز
: به محض انتخاب شدنم، خرید رودری قطعی میشه. هالند گزینه بعدی و حتمی هست که به مادرید میاد. سرمربی رئال کسی بجز مورینیو انتخاب میکنم و از بین افرادی هست که الان تیم داره!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90661" target="_blank">📅 09:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90660">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=RA9MTBo1KH4JgkhR1DX9KRrgiFQSOTmwzGkACyWVUzGbTQ9l_BHa6IqhI9y6WE5PV4Uw0mw27HtWPiKVzezzqNbeZstWnVl6DlzKLGJk5h1zQwEBzvuVSGEMOCSggzCfthYp5emwuERFcVnfaNhHqtPssG-vEB2sD6F8x20WE13c6Hy-4UTK1qWBbB71hRK4Yc03yFd2at0f90ZWDd8ZccnVBYIkMK_avpa-jabDibzLPmzUbZ7KjpBZeMGmZVYv-yWN_E4rOVgt_vknGh-Hr5mtkoFLZ8LrFb3AtlBgj0PLd4QCH45-cd83TN_5k8nb9KLqZgNNVRR_6YxJdZaAzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=RA9MTBo1KH4JgkhR1DX9KRrgiFQSOTmwzGkACyWVUzGbTQ9l_BHa6IqhI9y6WE5PV4Uw0mw27HtWPiKVzezzqNbeZstWnVl6DlzKLGJk5h1zQwEBzvuVSGEMOCSggzCfthYp5emwuERFcVnfaNhHqtPssG-vEB2sD6F8x20WE13c6Hy-4UTK1qWBbB71hRK4Yc03yFd2at0f90ZWDd8ZccnVBYIkMK_avpa-jabDibzLPmzUbZ7KjpBZeMGmZVYv-yWN_E4rOVgt_vknGh-Hr5mtkoFLZ8LrFb3AtlBgj0PLd4QCH45-cd83TN_5k8nb9KLqZgNNVRR_6YxJdZaAzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
ویدیو منتشر شده از یک زائر ایرانی در مراسم حج که در فضای مجازی وایرال شده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90660" target="_blank">📅 08:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=Jd2S9Uvz7JA70E3OmzyMDJA82rAsej8vDXAodtcDLEqez6avTNA1Fj2XeljEzJDgLh7vzCsYLyf1m_rXx46qTpu_TQkEMfrlFsB6EjLK8hoOTQnbIEkzg3U3x0DUb3A0ILC1UUlVcefsy_5L08y9paaB4RbaGQhImzt0Qd-dkWEjzeikNVzLiX4Q7XHh8kTnH__9_DmOzZxJft6Bh00kEfFx_k-pewoTiD5mPg86Qt3TDxj84aqtMJRJenzDg7Lw2KKwl7nGRJhK2bJQ3dzJDYjkL9qtQH-NQK2kYLP0bnDgofRlqnz29EmQ65yG5sSVrVFNt3rqTQa_EBfPKyp5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=Jd2S9Uvz7JA70E3OmzyMDJA82rAsej8vDXAodtcDLEqez6avTNA1Fj2XeljEzJDgLh7vzCsYLyf1m_rXx46qTpu_TQkEMfrlFsB6EjLK8hoOTQnbIEkzg3U3x0DUb3A0ILC1UUlVcefsy_5L08y9paaB4RbaGQhImzt0Qd-dkWEjzeikNVzLiX4Q7XHh8kTnH__9_DmOzZxJft6Bh00kEfFx_k-pewoTiD5mPg86Qt3TDxj84aqtMJRJenzDg7Lw2KKwl7nGRJhK2bJQ3dzJDYjkL9qtQH-NQK2kYLP0bnDgofRlqnz29EmQ65yG5sSVrVFNt3rqTQa_EBfPKyp5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
حمله شدید‌اللحن مجری بی‌ادب صداوسیما به مجریان معروفی که قرار است ویژه برنامه جام‌جهانی را اجرا کنند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90659" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCBZhuMt6oVSdPZK1NCqqS3C3TGubmpRkFtVtGLVSEcPUxC6q18e3BBAP9vxMv3VLc6L34OBo00AXvmnT4bsp4VJ7tRKS535WA842ePheWJMyTJqqOhAnEdISCfYi0zxYYTop8kh1oPa44WRsC-p3z7yeiiywqDgNo87Cuo6XCfkyp8-r9eb2f48ZgiLiar98Lq2QsqxNpclX0U8HVWSj-OTRnP50PXk7Hfhd1RagAq5vDWMlpq67ibKmnFPQyN9X1ZfTXAc8Ka-L3j1_tyugTnVCOZlUYXIJdeK6f8XxXp2QrLItYJ_vmWibNUBcveIZLdHcJSvrR__MbUal3ZwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
یک‌رسانه ورزشی برزیلی اومده جام‌جهانی رو پیش بینی کرده که در نهایت نتیجش این شده که در تصویر می‌بینید. موافقید
👍
یا نه
👎
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90658" target="_blank">📅 02:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF9jK1Yz5qut7rokJcdUY5QaOMj0_3jmad5fXqV2xRqaYtOQLoafkbimsW7yqDi6mNAvTwGa3_jHn4YC51Sr4fjAxHSeIaRtepU_GsOABbja9dJCvsu55FkFtyNP-jKIeoctbFxvlftAGZ2GSiWXXsSIgSNVU4ObgJ9LgMkNVRuBsJwYeBnP4jdrtcI2C8o_FmSX6m1hz08wiEcoVoEP9KMJs2-NT1IXrhy8d7N3jyJuCWgn7GPkbGkbh-iD6tAsdUED37f1Il2Npd9fuW65Kv-0FF2sTyXnJv4l7Cex_QpHTnxlQlkwJhwOM0hCd4oFWZMiWhZ31NDlkOIS_lwPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚫️
#نقل‌وانتقالات
؛
یوونتوس به دستور اسپالتی خواستار جذب براهیم‌دیاز از رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90657" target="_blank">📅 02:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90656" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=IKl1sV1RJFmVYe0pjo9Ojmft2CFuzj2xL2yQ3ZRWMRPv_7YTIEnam0xfS3NEaHAn9c4-hMzvjsSpl9OEcuygegdt1KiuZ5kOjBwjaCY1ZyHUUfBUSOgfHXwfm4qHMYDTaXq5zopehK71YDTe88UgBVw3j7PBzRREZ-DKzU0SjXGugYb5sMqJCqPbycXtiNH1ouWRKPyjaJzmb-G0c_47d7CCDylB2lduiplTV8-enwOY3Pwgp5feFUS49E8KSfGmk12Fgd0mxUXe_yU5ybAogTvxlmOOIS1Cw0Ce2bqWAeZQ8cuhxsFlpdmrczsnQ1yF96MgY1kwQ9OnuM85HWAWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=IKl1sV1RJFmVYe0pjo9Ojmft2CFuzj2xL2yQ3ZRWMRPv_7YTIEnam0xfS3NEaHAn9c4-hMzvjsSpl9OEcuygegdt1KiuZ5kOjBwjaCY1ZyHUUfBUSOgfHXwfm4qHMYDTaXq5zopehK71YDTe88UgBVw3j7PBzRREZ-DKzU0SjXGugYb5sMqJCqPbycXtiNH1ouWRKPyjaJzmb-G0c_47d7CCDylB2lduiplTV8-enwOY3Pwgp5feFUS49E8KSfGmk12Fgd0mxUXe_yU5ybAogTvxlmOOIS1Cw0Ce2bqWAeZQ8cuhxsFlpdmrczsnQ1yF96MgY1kwQ9OnuM85HWAWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e11
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/90655" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzXTpfY2DgJIocfjxE-CsqzC0LnZZjAmHg_mCzHey9MSP-RMpdKUQP5O596hQDEWflge6UtWQTyvj9Nnnv5EaNBEK6aEL61enJkOxHWllded0vIyRjHtqlpDctoUiDOyyp8MSb0rV9cVwFNzem2RRkWLyRDmCvr8p6kVJ8wyt5jcaVm8mnBBcompuAm1SOpy-pRy8wgpWy1kHBEYmFqRBohkmF-Wp_bv_BUWGDNI5JUdX2c89CmYjF_iiY3Cf4U88OAvuhaWXqQ-0DjV_jQqi3b88DQMUrAvJ525HfIrKUvE0JkWNhVeJ0owfdUGvYzIM3ESUyoAAKb7MKwG6hvk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ال ناسیونال بدون اینکه خندش بگیره گفته رئال پیشنهاد معاوضه والورده با فرناندز رو داده و چلسی حتی ۲۰ میل هم حاضره بیشتر بده
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90654" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
ملی پوشان فوتبال بابت برد مقابل گامبیا پاداش دریافت کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/90653" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کونسیسائو رسما از الاتحاد جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/90652" target="_blank">📅 23:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNBETN84TNLd3mJVNKr7HZmxdxiPR0uJtACymXBhRry-zabsyi2-rjwtL3wWl7sE4t89xF281LRp32VmlReQub4MYYvn-cG6hw2TdvYrWrJZSY_zm9Klz5BRK23iT2Blz9s55znOA01z-4rKBgRdrtn20nIZ5SBgYiIlm73V2FQ5MZZyasaU1OjseyhRtGtIOOdjUVROdD862vHRxQ3k6vOnLgjSviBXCGdA8xCNTz2PV9ypCS2-RiEjsIRp5-4KKm3jpyNOwiSDBh9aHHc3Z5LV65rra5445ukUfbglbNvPzslEtjWPQ5tqBWkdL5jqKDNijvqQXB6xnDgAdXwJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوبوسلای به این شکل رفت اردوی تیم ملی مجارستان
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90651" target="_blank">📅 22:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB6TXNdXELBD--Qvn06ZHGiNHU8DMu92pOQF9WpqAd6Fk0r8KAHSGgzCIFtxe7iv-WGjR0jv4JkXoq2zfQfy68m5fytgKjXbUy_DNLJOYNf5eEnMOCgj8b5H7LqCg89Kayx5K9_GCaHCSrROQrhq2vUvU-RA-Wde68Xjrz2UvT0BhkTWTX7C-T1Cai-xyPWNvEVlOw36JlvUUp5jLX8andotrVU5ZvUHB_KIX2t6KNiRQ478UXO8cyZujBEwBm2S6NDgAXXSt90aBbH-La4HypRF20GMYTrgUHotJWWjEBv6S0nfeFUm5jiw-x832EJY3_qC34ZjfyJkFSo-Qd9-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره پیراهن بازیکنای اسپانیا تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90650" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuFSbRr6xy157ef-PXMChoeZ_l-1Ne4Xgq_3hX5NCNQnzYjHQF8_a2P3J-FBCxJelDMVH4it7U2bHJVJtWAYLSEkXss4NSfW1PiQ9CqfIz9CVfyAuFqZK3PpDnPCfWn1p7DEiAa8nEvuAfzLGz4DiwCaLjf-NXhOEHoWnIUxEC5MgT8nuPNYaOijdzLmCbZhw_G-LtTELfFNmohoTGSVCgV6fKHxTOP_tohO9oifY2a3-737y79bJPSHdNyuaUgRDh4tMBxK0xU7BtCdoZIuzxsz-_OxQpJxodYmVx_JuXNs_lEDw6xohl2xrvKFO6EwBKjURU90vO7LjdOEkDIy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ورزشی ویژه اتصال به اینترنت
🔥
⏩
به بهانه بازگشت اینترنت ایران به دنیای آنلاین جهانی، روزانه با حداقل دو میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی میکس معادل شاٰرژ ‌حساب بر روی رویدادهای ورزشی مورد علاقه خود، بدون توجه به برد یا باخت، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/BACK100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90649" target="_blank">📅 22:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90648">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8W06Uyca5AGJw-EprZqjCqaRHqCMMr6olJPES0YE76_EeV4sx9xUN5_40wSq6GF454wO4PmhXnP9xcVPNB0suCNR41G7JsHYtt2Z3ac-IHK1Y05QOULqT2bxELw-TW062MKaanpcpUAXpgEVNLZT1Sw0IvUHC8DPWEQX1fc4UDIvh5aWIKVhPx3hqV8eHLogBPajgbz-1CpA63Le8aBmJ7FFckLub7iQ4DjgXusAhGfI8aOvU-5k6YFZit2_6AIREPNsbmqyrkhIdnTLeROvCQodS_cf0eEt10oy3lPu-Um0unmas-MbGFk4CJ7u6pYJzZQFrnM9ZPG43AVUTvM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو به تمرینات تیم ملی پرتغال اضافه شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90648" target="_blank">📅 22:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90647">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=np_VUMoYrOYnOmzLV36frFhwiEt5-mmdlQvov_K-LUSRHkddIYmCLMsnwyCNB_z_hUiA7Kb6stT4nsxeqqzUvU7_pLXE1YQL0aWzwVozc70wcWsbEi3Xa9jYbkQKIGv7Zks5A5fOh1a8aBaKvR8I5bQJOau0dDQOQQpUcTApbSZqzY_IRh6P1GK64qlWkvU9smoO_q1vvBMT6QgsnFDvX43yvIm795p7GKZAW2QeD8JVm46JyhQKu3hbQP6JhsvWqN_h1TtBTTnDLLFakJke2jOj3qPclHL3SdiAIQGQ728b8Db1ZUfPoWjqqWfHeWiI02XXKW2gOJi3pFZM74oE42PQwLV5wk8B97FvjT5_wYwctiPCrKZkVcSVl-HneIXNkSDjk97sUklY7S1EloAn6xGkQiFL-05ELL4JAG32rZDduV12zT2aIuoBbH7gyjg3c1qioQLJzOhN8KOKtLyBBbpUjDwe4-AnzWt0tczdUH5Nd_YNhe9Hv6sszZjqNbIDVoMO3k3nuggGmZWTtNVunfPspA6mnTDHGbG0gMizLJFxW1rKjRU_-40Ivn9obFMGenvO7mpv5jB0lrzJ4uodmdLDDzKvNto6zft4F6r5_Xhbor8tIF0j0kFhwaOs8_X1FkAUJ2on1EThK9osB8jL01DsTWOIN4fYzoxPeeuSdQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=np_VUMoYrOYnOmzLV36frFhwiEt5-mmdlQvov_K-LUSRHkddIYmCLMsnwyCNB_z_hUiA7Kb6stT4nsxeqqzUvU7_pLXE1YQL0aWzwVozc70wcWsbEi3Xa9jYbkQKIGv7Zks5A5fOh1a8aBaKvR8I5bQJOau0dDQOQQpUcTApbSZqzY_IRh6P1GK64qlWkvU9smoO_q1vvBMT6QgsnFDvX43yvIm795p7GKZAW2QeD8JVm46JyhQKu3hbQP6JhsvWqN_h1TtBTTnDLLFakJke2jOj3qPclHL3SdiAIQGQ728b8Db1ZUfPoWjqqWfHeWiI02XXKW2gOJi3pFZM74oE42PQwLV5wk8B97FvjT5_wYwctiPCrKZkVcSVl-HneIXNkSDjk97sUklY7S1EloAn6xGkQiFL-05ELL4JAG32rZDduV12zT2aIuoBbH7gyjg3c1qioQLJzOhN8KOKtLyBBbpUjDwe4-AnzWt0tczdUH5Nd_YNhe9Hv6sszZjqNbIDVoMO3k3nuggGmZWTtNVunfPspA6mnTDHGbG0gMizLJFxW1rKjRU_-40Ivn9obFMGenvO7mpv5jB0lrzJ4uodmdLDDzKvNto6zft4F6r5_Xhbor8tIF0j0kFhwaOs8_X1FkAUJ2on1EThK9osB8jL01DsTWOIN4fYzoxPeeuSdQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 سال پیش تو چنین روزی رئال مادرید با شکست دورتموند در فینال لیگ قهرمانان اروپا برای پانزدهمین‌بار قهرمان شد
تونی کروس هم تو این بازی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90647" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBZcxmG22VB8xrPXxEhURmig-eJqpmZ8t9_EvztNRgEQk6H9p3h_Q_n56fmfIwqJkBzgBN-smFhDNW1d4j5C1s3sTNj-3OTRudZN41PfYRO5dHptLfZbFTMx-PawkfKOPf5jMGOotIvFBRTp6P01VwnFeeRGc5DzMoHujoNBhOqCjXmsO-L3IsB7n20UN2rVHRM3Jv9aqF17q9ynQiYXXCvFaDzABiOJMyYMEVXtB9HPsvgD_UmKsRxP8qBZR98_cNCJHXPVNLTOqdbfTLSvij18yN9jCyVit5EsVKkZmVq0KX5k1CRgndJjK8QpdAqTXpTLcn55Q2aVJ69-73Seow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
فهرست تیم ملی کرواسی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90646" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=d5G7PTeVljlPR2skXPzEsopPuTd9aKlq9f5P7wU2fuEzSPtzG1rfkwVU3hhV6j50w7LBmucV2R5rr5tx60vKm8TdN7_u3gC-OmbWBJmO8R5c66Tb49qXkgxDjfAWtwqq77v0SAIJQydQfBvt8WCO1nUg9hTKb5XdEYAwoTn06Fwg-yyWDTbFw8Hi7quLjyRFhmZbVdSji_AEXeqez9dHs_kc7dwE34oPfYVhiRWoaK2gQPTQfy8fqdcGWnMvr8vG0Pmu3lPzfaUUiEn3B_Cj4gIcIjsSkXD6Pp_sTHFGfEPTKe423uz52mJJVM4IPO9LK1kZwPKnE-iZ5f4eMOXMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=d5G7PTeVljlPR2skXPzEsopPuTd9aKlq9f5P7wU2fuEzSPtzG1rfkwVU3hhV6j50w7LBmucV2R5rr5tx60vKm8TdN7_u3gC-OmbWBJmO8R5c66Tb49qXkgxDjfAWtwqq77v0SAIJQydQfBvt8WCO1nUg9hTKb5XdEYAwoTn06Fwg-yyWDTbFw8Hi7quLjyRFhmZbVdSji_AEXeqez9dHs_kc7dwE34oPfYVhiRWoaK2gQPTQfy8fqdcGWnMvr8vG0Pmu3lPzfaUUiEn3B_Cj4gIcIjsSkXD6Pp_sTHFGfEPTKe423uz52mJJVM4IPO9LK1kZwPKnE-iZ5f4eMOXMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که رفیقامون از باشگاه رفتن یاد گرفتن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90645" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90644" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRo1UYyEyxv6pj5N6kGEqt4rdzGIHmCZBMp6cMIflzkKYw9A5GptSqYT5u9JajmpBA7YJBvNpQUg1H0bmheapE_gA9jSlgHE1NX_3u95N6gzxAk073M_JByRcN8YKm7NfxRivmqnMElAehh_7m83JsWc58nAjuZXp7fpeCE5v5Pgr_hKSrMjA0HBdfyLGn4ZlRvI7PZqZfOq5m8RLgzkXnWLaUaAvmq-pZush_myFkPg06ZCZsNqIrqQ3L0h51W6Fzlt_Maz59bXLKUIQEvrOo6oLtN7OeirhFfILKcdsP3VI9Vuc2XwfWxGf2WHt-XCDkwGtKUD3WETgJJCzqfM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90643" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90642">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=gITeCQKS3HkY0C7OpYo2Ko06PXwWrO3k_8vdMhbzxfWrD-Rk6pcUPwlnkxTyPFGV-G2ekpdgmKw-A0_Jrbz8LMKxAyLgrlpfnsxFkHzhikgnwjTGQ6G98oMyCZnYyGaOuYl31oUoEy37ty34hbg8vnewk_UuQrvHLelSU62AU_GM48JlGGwARVdMMFhxF8xS5TE2SWgTBaZkRHBLK6oSkHRs4cD1ZRhQTt5VKDsQA5oU5jFTdiQQ1N4dv1evJTZgnhlte2UcDVDzJBGcnjNGFO9VjY8jO3mG2TZRoIQyq10nS3gG0njLe1nGKgcfVROC-B_f4D2IHgydkG68F7K8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=gITeCQKS3HkY0C7OpYo2Ko06PXwWrO3k_8vdMhbzxfWrD-Rk6pcUPwlnkxTyPFGV-G2ekpdgmKw-A0_Jrbz8LMKxAyLgrlpfnsxFkHzhikgnwjTGQ6G98oMyCZnYyGaOuYl31oUoEy37ty34hbg8vnewk_UuQrvHLelSU62AU_GM48JlGGwARVdMMFhxF8xS5TE2SWgTBaZkRHBLK6oSkHRs4cD1ZRhQTt5VKDsQA5oU5jFTdiQQ1N4dv1evJTZgnhlte2UcDVDzJBGcnjNGFO9VjY8jO3mG2TZRoIQyq10nS3gG0njLe1nGKgcfVROC-B_f4D2IHgydkG68F7K8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
‼️
دیشب نیمار حین واکنش به تشویق هواداران کونش پیدا شد که آلیسون زحمت کشیده شورت نیمار رو کشید بالا
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90642" target="_blank">📅 20:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90641">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=AY7OZCT3UvE4RodXPW896KrtqfKwfBstU156Higgn4CVlA3zkBsJpglibh9HfOJ3m5M4v01wy6aCJRynWAnCNqWpMA2-BICL0VgFWhMWaxK_RcPwNyNYB6vcNtU9gUz_PpLbg8n0AGoC-Zia2I_s9uWbcSEi0__mgqZ_srYnTIhQTmLVkUTj4I7MXqLS8WXZFL3IzsG-puv_D5n0bOhoS8AymaysAII-0PM81KVg01K6ptfANMtizWndMcZELYzquZVAdA09MnN-jpfI4lQwTMygOXnI6Vf-4ocvkz4xTd1uPRxOchYCH-EwDRQlWYw1gnELT_WRvM1dIvkyeBiulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=AY7OZCT3UvE4RodXPW896KrtqfKwfBstU156Higgn4CVlA3zkBsJpglibh9HfOJ3m5M4v01wy6aCJRynWAnCNqWpMA2-BICL0VgFWhMWaxK_RcPwNyNYB6vcNtU9gUz_PpLbg8n0AGoC-Zia2I_s9uWbcSEi0__mgqZ_srYnTIhQTmLVkUTj4I7MXqLS8WXZFL3IzsG-puv_D5n0bOhoS8AymaysAII-0PM81KVg01K6ptfANMtizWndMcZELYzquZVAdA09MnN-jpfI4lQwTMygOXnI6Vf-4ocvkz4xTd1uPRxOchYCH-EwDRQlWYw1gnELT_WRvM1dIvkyeBiulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرین‌کاری اودگارد در جشن‌قهرمانی آرسنال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90641" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90640">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90640" target="_blank">📅 19:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90639">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده قرارگاه مرکزی خاتم الانبیا
:
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/90639" target="_blank">📅 19:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90638">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11054c811.mp4?token=uVdVwCmWmxxOFZJPWROv0vYLcHqzr80MukCBV49WwV_ux3oMRMSB--KJNoVsSCLcUvEse4oQwa-9xG_53K4Yl5kl-d_Wo1Z6Z69FqLdBwzi-hC4W9P4-UMBcVubLjiCcq72w3gz49zb-9OqxZGqrw54aX_E4sk3ceZXAWb9ci50c7oRRMHBeenabsHfCqNDcvuf0ue4XNck7eZwOTEXxupA4FVD9I1uduE_SIGmUONuJCPvk7VxXaP8LWCsMaBmLjcFwmGR1zu8KRbLz2XdVJNzVY68yV77kfdXDFmiKBlEMYiUdoxImE0kELauLqDLl0a3DDbAb6rDn64c0CL1bfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11054c811.mp4?token=uVdVwCmWmxxOFZJPWROv0vYLcHqzr80MukCBV49WwV_ux3oMRMSB--KJNoVsSCLcUvEse4oQwa-9xG_53K4Yl5kl-d_Wo1Z6Z69FqLdBwzi-hC4W9P4-UMBcVubLjiCcq72w3gz49zb-9OqxZGqrw54aX_E4sk3ceZXAWb9ci50c7oRRMHBeenabsHfCqNDcvuf0ue4XNck7eZwOTEXxupA4FVD9I1uduE_SIGmUONuJCPvk7VxXaP8LWCsMaBmLjcFwmGR1zu8KRbLz2XdVJNzVY68yV77kfdXDFmiKBlEMYiUdoxImE0kELauLqDLl0a3DDbAb6rDn64c0CL1bfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام تو خونه میمونه
😉
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/90638" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaoZN6SlbH4apGIoMmdODGmJLtATzXutNeloPwWwoZuEGInB1lnAE89wZW3t0YC11YaSSOVgyCKNPulHdCE0kYg3mH3fi1wYVfTwFZNNSgX1LYH-d0FkEza73Wfk_WgpU-Z834cPbr_2KDJFXrTRQtaM6s6J04pq12gpOLNawsKAQ6D2inrwzqMvX7aJURDNWXRawrOmA51cuVwIiYcZEJO8k129k6mpUnZGiw8o3QXWJP1PYHJpAjYnTYVAOV-GCG3vmJmUVJWIScHbevV-9KK_19vfmMaE3Q-j6k3fkP9BgVmpkK20so1FnmJpxMjqIMHK-UbpkhN0DpUZl_S7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بعد از متصل شدن اینترنت، معاون وزارت ارتباطات برای اینکه پیام رسان های داخلی ناراحت نشن رفت از کارکنان پیام رسان «بله» تقدیر و دلجویی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/90637" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bL7znvxyUAoKb6hQBOMiAQAZIHBjIPRK8URIPfHpTLyIIJuiOcavGuhBbx1mX5hdgiML3ehYS9kOBGy_VAv_tGLlEt5mafpJiKA6psZvJ1mpWwzMT3EDTdeDPAetnbM_i_oyT5vVedgEshPL0M6vclUbwPE6dch0PuPDHDyKRHEZEjU_d8x4PEWGgW5lbvF0pwgLzWzSoox1nDmPHWToyCY1-xnB5dAeOH5JpnenKC7lj4aSPwSEOt6SO1i3lyyiBy5KzFMJ6pKz7mIt8BiCz_QhhvokbACSJtkGt4GThRLh7UDBkeduaFzr_q7fBuRNYyYEaqTz5VUX5stcFMIMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد قهرمانی هر کشور در سی‌ال:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/90636" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=LkvoFRxgaIQ6gjTlNHp7db5kahI-4I8INoVqJEgKpsfzfpUAOFJX45Nj6p9q47-ehILMJXrdFBnBmq9C1VoCd2tGjupMh-HBaJdfoZx1KL-RaRKv2EGrrggENYDiUayBTa3RNWV9jZML01_O4zACqEJTMOPYfsp_I4KQiIhN-_uu77Kl8JZcTYPEcQ5tvqdyBaFFkB_hpMBBS_tdawqeLiI9dgPJ4wxXw0QA0GDBXkggK0wLJac0diS5oBsk7r7tItbi8yQYcxdaWojKO7zQ1aImNjXlzgDA6anrvja26YSOo802U3o2vSDdIY2WSu8-loAFfg5NdV4PGTW1Ni6rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=LkvoFRxgaIQ6gjTlNHp7db5kahI-4I8INoVqJEgKpsfzfpUAOFJX45Nj6p9q47-ehILMJXrdFBnBmq9C1VoCd2tGjupMh-HBaJdfoZx1KL-RaRKv2EGrrggENYDiUayBTa3RNWV9jZML01_O4zACqEJTMOPYfsp_I4KQiIhN-_uu77Kl8JZcTYPEcQ5tvqdyBaFFkB_hpMBBS_tdawqeLiI9dgPJ4wxXw0QA0GDBXkggK0wLJac0diS5oBsk7r7tItbi8yQYcxdaWojKO7zQ1aImNjXlzgDA6anrvja26YSOo802U3o2vSDdIY2WSu8-loAFfg5NdV4PGTW1Ni6rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
Vini
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/90635" target="_blank">📅 17:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=Yl8pe21DAz4mwnHLYiekrIlE88Iyn-5D2_0hU88X2r6IU-Jmeo7wqM73H1e-d9oTvuTxc2M7GNqJEGMACpxYY7E-OZHK57LL8ZFqG1XECS1Trj3CtVMwyGMjaYxMcSGoDZ0V24BSnuqSXlLBUf6RjmY7ag74tgLF3MCbQ4QoYH5nzj-0pdZaBv6MjfNahBSU07mQkqUY_4TPke-8rEOd6QQsuesfIfznuxN7T4MJkJ4eXG2j1vBXjk_SipwLPsozF0x1a48dV7mxQ4hc-fDGGLZ_QXQCJqYWfVJVSmmiER_BU4Hy-qebBjUGQekb0aLegNVwmn8_H5GvE6nHvq7l3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=Yl8pe21DAz4mwnHLYiekrIlE88Iyn-5D2_0hU88X2r6IU-Jmeo7wqM73H1e-d9oTvuTxc2M7GNqJEGMACpxYY7E-OZHK57LL8ZFqG1XECS1Trj3CtVMwyGMjaYxMcSGoDZ0V24BSnuqSXlLBUf6RjmY7ag74tgLF3MCbQ4QoYH5nzj-0pdZaBv6MjfNahBSU07mQkqUY_4TPke-8rEOd6QQsuesfIfznuxN7T4MJkJ4eXG2j1vBXjk_SipwLPsozF0x1a48dV7mxQ4hc-fDGGLZ_QXQCJqYWfVJVSmmiER_BU4Hy-qebBjUGQekb0aLegNVwmn8_H5GvE6nHvq7l3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حدود ۹۰۰ نفر در جریان ناآرامی‌های پس از قهرمانی پاری سن ژرمن در لیگ قهرمانان اروپا در فرانسه بازداشت شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/90634" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/90633" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
