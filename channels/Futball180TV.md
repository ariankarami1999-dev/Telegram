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
<img src="https://cdn4.telesco.pe/file/fc8MANGoyFNWxknRR5CfwsiizoY7uJ93h8rrzsZ-DfY4Th2vF03rWinw67vXyoQzFa4dgKTY0lb9K_ldPqFXbJ4oXMbbO3KbmU4_0hxLDpftP-YW376m7eW3rDHlaBvY-WwjYTp7DY9jj1lcOsxn8PGZ_rdU4KSMz93c4UQq9OuzEnYt_fta2X41BfGNYROmNsB2x0F4CT2Pmdsy9sJEjpcXMMuBo1QtXvTtiH8z_Y4LbkRqx41BWmUL__BK-tzMJoLN9uBu7OtxBCmgx556uKWRx_mnbFH5JtSii3DMBEu66uYmWGT5Q-qCBJCLjGZY2LYV0PhbFeaPA-hvow_i9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 126K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 11:30:51</div>
<hr>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=WFyWC_zdsaJjFxW5BMbniDoV88mPZBEhT-2_dnbuV4tOcJ8gfQNfSE7bDI3-eW_9IN7jXfS5-ExANJ82l9tZLk_o3OEVqaiSpI7JFBQa5sopzziDfdHOWh4NG9-ZntcJzYvvS7ik6JDg4CwUzIIgxmyGWx7T2AxeudK0FtMPgqfZSAAcShj0zDKizJ1kUTBZn0T4UeKnPOZgptngcQpISerSjj7HHb2fh76ldlTw2aLVUGBWYYq9TEuDlplip13_3cNcKZeQu_bdm6E-sr0UWoPT8FyjEQf9j7K2UBLGhZdypKLMcA7RzZ2gORde32Z_neexbZzMHX_kmzp4qdn91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a196e55e.mp4?token=WFyWC_zdsaJjFxW5BMbniDoV88mPZBEhT-2_dnbuV4tOcJ8gfQNfSE7bDI3-eW_9IN7jXfS5-ExANJ82l9tZLk_o3OEVqaiSpI7JFBQa5sopzziDfdHOWh4NG9-ZntcJzYvvS7ik6JDg4CwUzIIgxmyGWx7T2AxeudK0FtMPgqfZSAAcShj0zDKizJ1kUTBZn0T4UeKnPOZgptngcQpISerSjj7HHb2fh76ldlTw2aLVUGBWYYq9TEuDlplip13_3cNcKZeQu_bdm6E-sr0UWoPT8FyjEQf9j7K2UBLGhZdypKLMcA7RzZ2gORde32Z_neexbZzMHX_kmzp4qdn91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
آخرش کی برنده میشه؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/Futball180TV/90447" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8501f73.mp4?token=sVyCB0AgD__uQjncilmASWlrQZwQANE6um94kwffg6Z_mAAl17WavjZ_AXlAwPHTPstHdSYTGZOzQHbUF7sALt3baC9F-tH8kiAMi6ZF0URfV6u3JOr3b9ilBNGS59a0c2bpnQyOMQCJEPHG_bdVs7400pLYRKJ3QE_O5GGEHUCpqEL_OMWUVwMetpIGzzjB294cJf44KmyEBeFGV74qTsqW68WrVfoLrrzF7XO6LYgqhXREx2gpjvzhiQJ-Imc8WOrVEwB3cQdjpqcVqx7MmWP4FPjSIE0AdR-3m-ssAxtFAubWsbp0uHDC9-3H-dmnKYhhIbKsBHavbd3OJD0jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
مدافع نیوزلند رقیب ایران، در ۴۸ ساعت ۱.۵ میلیون فالوور گرفت!
یک اینفلوئنسر آرژانتینی پس از بررسی تمام تیم‌های جام جهانی ۲۰۲۶، "تیم پِین" مدافع نیوزیلند را بعنوان کم فالوورترین بازیکن جام معرفی کرد. اما حالا پس از چند روز، تعداد فالوورها این بازیکن نیوزیلندی از  ۴ هزار به ۱.۵ میلیون نفر رسیده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/Futball180TV/90446" target="_blank">📅 11:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpMdd9kHIvLdOgTFT426wLpfDU59QbWIaLfL4vm97KIaiDbEhPdwjYtepxwHHUvj7YM2AjO_poyCgMzBTpJonZbPU_yxhqI7R-Xl1WBJFsMR0JKtpGn0fmmIehSFJSfZPwktUmKIxl67QTP-wYYddP3kiIeinci6cY_9LlMFTGSmnEtf8oHx88uJ5CTL5psy7hMKOUi5ztyS4bZvS2SMAQ6jPhQOmzznGHPJvleFKcKQcY_wbJpF7fH1bq2_HHcEWVFBuPf54wL2cOfk2VBiXIePw1zYhQCINJsHFacr6vafvth24bPCK1rTt-379FeS4UByCwPBsdq9bCm-8UANkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کونده با پلی‌استیشن‌وان در اردوی تیم‌ملی فرانسه!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/90445" target="_blank">📅 11:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⭕️
کنکور سراسری ۱۴۰۵ در روزهای ۲۹ و ۳۰ مرداد برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/Futball180TV/90444" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNiBtSWpn_9Bj3qZgHbofU6aoHAaDDu0z-L7vwode9laOpz3vWHlwrnNuVjExOaIYWm4ozAkwAwyUKMRFTpFQqdvNJzaNPnD8shVLGa873WTGfxJeD8CoS_8aJzaxQ0tPbz4nmmbcL6TPzphcI_NiwBKzY8hWR404n_7GSYXoPZDMhNUNYemx_MibRS5xysz6Lw4NebjUx1IbazpaA4ZojuHlsJl8KJGf5b5ehMpbLfWie9qh-yduVFT-o_xTqi476IC8U7E8qRj0ilxFFQ_dqHaMSv3CpxeVqg9Y-PJFlgeFiqhSbzqoIb6TJHJ_BXZsSmAmxfOg081htpllpwZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🏆
باشگاه‌های
قهرمان UCL بدون شکست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/90443" target="_blank">📅 10:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=JeHbocjA6-mKjBIBr4LtDN4C2qIinqytZIXgALp5y1UvVP_vj68_0L3vcl72xci0BWzH_yK_P0B5X0tJNsyGLFCS_zvCdMVA_hvFCBj7Qj8y-5IR8X3NFWSjddUeBOHDKZioKO2CDeP_0yfTjlJ0XZCvg5nMyipnKQTBAm5HaMstY2v80U8wlJ4rBN6J8zAmQ33o1NeO6ABWA935JDV-LJye1ClueQ6wlYQhVS9368UhTQJgRYz48VA3Ykc2kt2CBr2gBau6LAPujLcH7laJ4xswNPOgwGSE8zuYuVFh5RmS3oBixiJXQNKGbIuirbRT9RyQMwIYJhOSXCUdZIbhoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bcf8f7c1.mp4?token=JeHbocjA6-mKjBIBr4LtDN4C2qIinqytZIXgALp5y1UvVP_vj68_0L3vcl72xci0BWzH_yK_P0B5X0tJNsyGLFCS_zvCdMVA_hvFCBj7Qj8y-5IR8X3NFWSjddUeBOHDKZioKO2CDeP_0yfTjlJ0XZCvg5nMyipnKQTBAm5HaMstY2v80U8wlJ4rBN6J8zAmQ33o1NeO6ABWA935JDV-LJye1ClueQ6wlYQhVS9368UhTQJgRYz48VA3Ykc2kt2CBr2gBau6LAPujLcH7laJ4xswNPOgwGSE8zuYuVFh5RmS3oBixiJXQNKGbIuirbRT9RyQMwIYJhOSXCUdZIbhoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
اردلان‌آشتیانی کارشناس فوتبال: سن و سال تيم ملى خيلى بالاست و ريكاورى سخته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90442" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLrqzCZABlAsEgHurk38trN8c36IyOTxpDAYbcr8VsShFTg-jT_FY9BN-Mmec0dtRcqX3roS7O24GolesTd1vMMD556UK35o12SUqLmj_qxTOtDwwyCw_xma72sNud53XKp3dOtFebSzF-ObrmZLr9iPwmM5eTiAWIzTMzNkaJZtdRfyVxTKARfWzJ7A0s8AWSBNTxyAZN7YQjMXZ1WXRtQhwPCCZrGeL4_mneYA6JraVrDP1Zi1oQmUyEpkRKW4K7KFDIudkiFjxmfY1_m-wTRf8en6KshLFNq2aPVTgPfxm5VHs2D5miJHFi7u4msVmK_S42aMFKYDG2cTklxegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/90441" target="_blank">📅 10:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=ooMOXIPqf_rkz0d4Vv2Z-QO2zNcxQwSGYAJkotK8vtWpYpUgpdo4g6O34mKLBeHpVMmQrXCfK---HXImKoXur2-EIHv6UrmE4zgswsIXexN3BXWLZaBhiERCfHccoDMc5U6-ZMAzmzlRoT6IdSM0SxclJYP0L8dNCuyxHexRQuYNoeLLTcpfUY4Y8IRUfC4lIR2wATIeGvWhqbNp4mSEjbsmmwrNP7siOJoGfx4w3eJTmfVzjU2RDVB74sgcxUVZShLJGRP5eg6KkPTMsz9al-H-YXMx3rZ54LjT0L1X4gjr9A03_vYS1OrsF6-fF3utpBYSi3MrHiuBXOHKRtJLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6df1df4a.mp4?token=ooMOXIPqf_rkz0d4Vv2Z-QO2zNcxQwSGYAJkotK8vtWpYpUgpdo4g6O34mKLBeHpVMmQrXCfK---HXImKoXur2-EIHv6UrmE4zgswsIXexN3BXWLZaBhiERCfHccoDMc5U6-ZMAzmzlRoT6IdSM0SxclJYP0L8dNCuyxHexRQuYNoeLLTcpfUY4Y8IRUfC4lIR2wATIeGvWhqbNp4mSEjbsmmwrNP7siOJoGfx4w3eJTmfVzjU2RDVB74sgcxUVZShLJGRP5eg6KkPTMsz9al-H-YXMx3rZ54LjT0L1X4gjr9A03_vYS1OrsF6-fF3utpBYSi3MrHiuBXOHKRtJLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
تمرینات فوق‌تاکتیکی آرسنال برای فینال امشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90440" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyc8L0KG086jiRpuEDtLbFy6J9Yncg4JJaj_F-e5Ptc-QTusT-O3SCOca_d3BWZQiyYQpSWqtp9zGlgObED-9oKDYItImV5PWGUHYE5aZ4iv_CM3zWeu0vOrTT8dXktA_Cz3sjXkGI-U1JevPeKc1MFXgoYtLhXQ5fcBxDjhJh532ZrsZtpBYMCN6n2lN4DSVVlnL_gFldOBRlB6rsn0Wm85-8_Vckq31ArY7vqREGhOU85YZ6Yic_hcYh0t0ec1iFGg98FQIUbOF2vUcajByrTfanoDv-Eu9gVWE4stfshth0Pwmj-eZTkXOr0iKejRyW5Sqj0xqKFRiH4zsGDTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار یامال و دمبله در فصل‌گذشته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90439" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfCVpDuTvO6KhzivpKyJZpvfUvaPnLLJLbaB6ruZLNXcG3t4y7MAP3qEgTcUWp2L-JwZjHx11KDiA7Nv04LD5cCi7gqt8vevzp4_28P7RIblA6PwQI0CmrQHhY-afvtMdvfpuNm0QUW1vHdqVdq59HeD3WexGqkbcXCBt23Z-KgXOi4CH1REpNyz-0iNlvYoSI8Mv1drSBTImlAGkapBa4XINNAh_7S4MORXekppwTdu7NpMVYBvHDTR5CzghgeIiy2LlmCobdz1op65Bk9hvqKZXAcokOPU1RjlcFCaRee7YRig9NmbPS-0PVEjWDr6jKtVq_andbsVv6hlCJUCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آمار تقابل‌های دوران مربیگری فلیک‌و مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90438" target="_blank">📅 08:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZGdwz5PnM1mscdMsEAwK516bfk9X6BD0MCRKQXvEEZkT-5jMRPg1eX3sfA8XDHgzNg8xcx4ScOJkYGlVMawLlUeRG_dfUMiCc2sCbVk1Zs1IDQ25ow9doGHmq0kNFMgcwXOuGno2JxFYXZzk5oNHuAcj6cHPhWkV7ZvdRmiHsZP7m5Jga7d61m0D1rmcl9nm4Tfe0X4eiyIyGE-AHpvb20Er3JXeiZHsazOxqk89vnQ6ybjwUlUDGIGO99Gsxgxe1oLh_3qNPWS5hfdhSbaq3bPrT0BSO3HxbeBDEkBpY0868xGDao66ooUDkTlbBIDTkC1L0dg4ZhkrUgRvxPsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و عملکرد رافینیا در دوران فوتبالش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90437" target="_blank">📅 08:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/90436" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_iSDQaNz0h0DAqU4Tj_rtxMcrOZMXmzL_0Wsz2_CGhF0pkkdctQEeBIGAKykVprcLvWXZHlO6bRoWFnVu3yq0X-YX557n8BUz_XWuQXdOmC7SCjYZCYlsbQr5MKANMLc-isNVTcAKFi2PD1XrkZdgsHLhn-nILje3uZHKuYa8Jbk7kkubVxcmhUQrBYnOqfy2hsd1MjbY7dQuf3aYbNPIUBDeJAxgG_WI590OV3EVDOS7MDAn0dC3yKiYuWdz-SP70dFAyhVgwxKSORJ5gpb_Ik-MmmSqYVzywHoCFkdvUGdSzRwNI-KCcSrZdUTmA8NaDJHDK-V0guyczCUiXUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90435" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltZDc578FFEZf2ApRAdm1GOzIVJgrrtrV9VzF9Ixc1Bg88LxUK_2hweUVkVHomk2byjamg6Yg4qqtgjOPvnu2ga9UgmG-hbxbBeDUl5_aDPU5_OtDemtpR7U0crSWjIH8AhGYOd7k7WXeNAPkOqgHxGAs2DYWEgKnXLRHn1NW15-K2miUbADfSt9rthGs5zVHgraa3MJEC6PRYaDTmVyjTGpMzJB9lNYRfsevGbdqpIkyIgW8zHuOqHnrip9gLRqQ6jK39lIKRYqGSWrv7hHE5F414iblzA-YDujrL7RPIp45klPqZqOaYvuewQkZSzz3UybfeqeDUxrgD0e7BMWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو با پافوس قبرس قهرمان جام حذفی شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/90434" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مجوز حرفه ای سپاهان صادر شد و فردا اعلام میشود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90433" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ0v2i_izd1AazGWeYsjgyqevLO55GYS2FqDR3hbJYN2ti35bRPXxJXRcZ5TXuomFpJWY3vXjNXtTfKfOcODlsxaXoZMJHbenX1xXPaoshBR6tcN2uBnYBSd2MelJYcTlQ3qvpUwUDNRteh5aOJ_MCKyxhWMblYj3FKs6aGz9BKtkBZarEjrkD_nw6KIknY5GE9siX0ykY5Yy_h0QY0fUEjG8OceeqY67P2e9N-dB4efwbpOFQ-iDFx7mZQaVHkpkEXDhc6uWJAM--7WsLv3oWCN-bH79tWgcze1_U3ccbHgQyYYl2hMc9V1JSMXzWk7IRci72meMyKj20G2XbvfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری و رسمی
گوردون با قرادادی تا سال ۲۰۳۱ به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90432" target="_blank">📅 22:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvwq_I_DoCkKethVsn2ofHsLuIVAN3j63h31gXGvofs9jf_gQHCix7lfzhU9VcxAXxQeG1Rs29uqf4mm_qnGaFTvNWjPXbQgWAf4fQrWHg7Ak4YFQgQi-8ZRUjCkQLUXH6sKBxTcd8lcAL8gR2IZyBvkfRzZTXcStsFMXxASxCelTHjRl4_wL2EPDJNEyYQGiSfCQ7uNDVoDnUeYoO7fD1loTed6glYljVvEqoOWiTxCQeHK6IBCBmh5Na8Y91n2cyI_7MQuF3Dqhbh99WLRp6uner1wgCyYSj2PKXN1vJnn697Dbkfkahoxm3AaKfjYxAOCvvJmOObnx6E0bsfWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دورتمند
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90431" target="_blank">📅 22:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnkizbXhuwzsUYjuQ6UISKXyQd16krr1ok2u4ys9-CI1jjugFYekNqK8vNCVX-iHlO737J5wbfegWZ4cbp79JGsPOKuyM2azwwbpXQRmtia7cXOPa7vU53I2-s1fMviyYlO8dEKGUQ0HmKLwLMXtoMk8RcI0dyk8Oz1m5X75nel_5AICbMZCwOxL0_1OkcEiXakpSKfyMAHQfW86uWNxy8YX_FtPU6cRgekzln-Gw41O-L3VJIXamaXoIWKY3ZHVqi6g5RpqgMbYLzVtVwaUIwvhgS58qW4ln1UYkLCgzeK4Jb7I7qtS9LuNx9C58HF227tOOPhXGfWcTTrFurAZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتلتیکو مادرید بیانیه ای طولانی را برای روزنامه های اسپانیایی ارسال کرد:
خلاصه این بیانیه این است که اتلتیکو مادرید به دلیل نحوه رسیدگی به پرونده جولیان آلوارز از بارسلونا بسیار عصبانی است و معتقد است که بارسلونا به جای مذاکره رسمی با باشگاه، از رسانه ها، افشاگری ها و فشار از طریق خبرنگاران و عوامل استفاده کرده است. اتلتیکو تأیید می کند که این بازیکن برای فروش نیست مگر اینکه بند آزادسازی کامل را بپردازد: 500 میلیون یورو نقد، و او تا سال 2030 قرارداد دارد و بخشی از برنامه های تیم در فصل آینده خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90430" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎙
لوئیس انریکه:
به آرتتا می‌گویم تو هنوز جوانی، پس بذار این پیرمرد دوباره قهرمان سی‌ال بشه، چون آینده بزرگی در پیش روی توست
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90429" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYKiqf2QXeXwfkWB8VrCZ4uNu0v_PxwS-BLpd4hg3FwKLLrlqhCyhqyvkrl31W_GDRFfI5S00vhBo75AXXk9ZVmlCsr3CNyVR37WiS3jCBp1SB2rqTasEAOapDT-gvPFQa9v_Q9WCA7ltDS5RrEwrMysS-7rhknzn7mjGUFQwLp_qXt1fjJY1QDyMwpQAe_P4x1OqLNvCff7LtooJATEMHdBqu4hr6PB8mvEsdVyUJ1TatGNUy4uYSah5nNSCzPsFMKQhMw3EagQ1Xun_EJyiKpDuqtMDLUkDQKVbQgMT3kXtkqhNe44Fo_muh0eBCvCYmm9NMez0Wsx_fiO8-v3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در ۹ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در ۱۴ بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پاری سن ژرمن در لیگ قهرمانان ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر آرسنال در لیگ قهرمانان ۲.۴ گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90428" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5ed95013.mp4?token=Lbpdq6UQupaDyIciLZ_TRDgXR3U7c1xZDFGT8QJ8eRMueN0JMFx6hHrYlTq13OUOQmMqMfX8sFoRtaFLEvfe5c6zZb0uN711Yq4XANRk7mVqefMgFDDSYfLi1U6_PAhRm2FZb8sLotRNGsBviJyALOAlG-XTXgW5stsQu9ouisPdHnYgWF_UJTzLmRtHGdLz0gds_WSqpeNwcpUu_Q8W4SWc8JOmlVNcRtkS_mrJtSGvZjNo8H9ghP6hvcxwRzxQ1kCe4pMFhKVXEx4-QRvEiu_DVF3t4o6nXAGoZr_MhtxvnKxbSAV0mu0gg7adnx1dpkefqs6YxKqRBmUUNpJ9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو جدید اتلتیکومادرید علیه بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90427" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrUPSpUX6niMz85UzvycxAjY-si5d_eWhrZKJnhhxbvBP73y_SsHyH99CSK_fng1QxfbcMDHGNjnfhoxdXlomL2mHLS4rzvbGa1Rw8NCphc8xpecIa0TVA5SnSMVgRyuhe0LYCRbNCNDqi4Y5uQvLjCUyC2fJ1hWUY45Zn8xTE3bheUUycuhD-86iOEXMhumOvl_tUqUV42lEv8YKDvBdP1d8Lx2kafzy9fO4bEX2eSRp8v8zJHY6YyoGhVZnhU7uNPUffGATdW7kEnlbrfYoMPzgte4aniBJVsGPZ3i4e331Ka0bo_BeO94_Ba1ir3e6fUxMid8jxMmHFI5mlv6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:  برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90426" target="_blank">📅 21:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تیم ملی ایران موفق شد در یک بازی دوستان ۳_۱ گامبیا رو شکست بده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90425" target="_blank">📅 20:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e3caa05f.mp4?token=SRIdOaTqu7fu0WibDFkDaj8N7IQxorhY4b58eN6CUV0JMmijQgxI0DAaIRCuvTAThw16vsiXCIRyjF-zboNs6_8e7h-kiHCSe7VRtYYqVaEr1NRh60SOKbAC3VeFfyZEikmtD7C8nouc-OgNu7PUahAbzUj-GyJ2X1BB_i9ktCki9l6Wo-UKtxSjP5YMXAeYATPPQxJWE7T-1gQl5Y9h2LPQl-i6B8pWOzPdlzNGe61EbPRT3ErzOsh7id1q6_N1DwSEQs6HhcmRPWc5OV9WZBWEQN08VN4Z-X75QQpEkHgQ4oho4Kog8h57HRiSHgskRmsFzTt_-gl-ti9BTc0lYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم ایران به گامبیا توسط طارمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90424" target="_blank">📅 20:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1fd30abfa.mp4?token=bVpZT36cezftsz9UkR0fJl8zNX3wevuy349wyNKogcRQj33dI_cOwdm1xW-6_8bCpAWAUKdKajI19RXcwkNNyfeb-GLs8Muxcdrf16o_qXONPRtk5iTw191YWPghvBwsgxOA63ep6jD6zAzxwdG6Lj5Y0kH7dswf6Ppn-c0uYUOapVCfEt1Sd9334Je8hkyxuE6T4PMXX-28lyEPuOP0TbHR43ZgAZtkD-2m18GHnoVw6ZfVUrXVT9RzlFVKgx7bM-v9CxuwietHUwotPBvWYh8ZpZOGgPtOwACLxgQEJXc0s2zljjgUNoULMiVVrDEra9gqZeWPX5v8fD1znzlA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ایران توسط رامین رضاییان در دقیقه 59
ایران 2 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90423" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7455525379.mp4?token=kquPwNNFGONdBcBgQPlsZt78rlmLlq05ShdKviPCmLRVH1emYePiVKQ4YRBkLQJi2XXxMxeJ6cQZwxPu0hRWkxfYF8OYw41zZSL5G85o5Iy7IlP6QHNvROF38IpHnqOfxnHe1YtNK301OIqJUc3prHL3UCXSKGDqLcZIwJeW0T088aYlTO_4WJ2wcMaV4T0d2ATHMlz_-o4Q-BTwC8dvdRIX2Eh56oQzeduShFOIgpTVO1DC9dhFB8Ty8ca9nYRzxxhiicTl9aRpl-KchoDRc8UX8aHphvBBS-Jqkd6GQtmbO_e1YQJZirxjifrbr2LzFZNLQgFMAkTHN8fsXlYZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ایران توسط آریا یوسفی در دقیقه 47
ایران 1 - گامبیا 1
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90422" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90421" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7061278c4.mp4?token=HipReiACZHoFVo75iOTuJurksAOhzg6ljE48ZDaoXOtr97iucCeR5i1fzNLU0NQMTCxWZ200kNgQSqk8z5xLaGNsJ_-Z9reklJBQnRHXa5e28b7WWTk1dz5CToB9Z7JbUZmSYt69imoK-k6JhYfe2crypDr7f-5pHihIhpNCe41Chj3X8P2MjgX_lVm-ZXTU4WvkLYqStRiMW8_ouZ7XimVxRY3F5cGQhv6imme-W4X38h54VUzesoTIo4xxUrfD93pxIlemwZT2TqmdrTeroNvwzr9z0r2eOEcDYvhLbpWaueW4JsniaPSoW6Afb4x4a0lLl_uwnhCT6SMOwvUxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول تیم‌ فلک‌زده گامبیا به تیم فلک‌زده تر قلعه‌نویی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90420" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWeTIpSZH9vU-QuXKvB_SwtbE1TiDUCUbgrQOYFNtMOaWQwGddEmnnxQUDU3MBA_-WYLPHDXysg682_CmWeu2gfFrCUPKR0r0AAHcsbIS-4ahSXGNqRbxwpxeq0C4qgz24lYIbL_MLsQsx6eCezi-T2T6FJmpP5sr7tjAuwgOlUCMyXedEG64TaH-7rozEyzPdnwrEy6ZqwOt4NQ-nSW4Z2sBmCw8BZKmaP554fYoQWInzMu0GLYZCImPIEmnhaCMHB_0umw8TT0DOKBbgaxosTWRCUDKQPP3QBXzE15_K8JjfjiNAvsiFSnW52536V2OFnkFZ__viCDq44Sj_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانه جدید اتلتیکو:
برای این پیشنهاد مشکلی داشتیم، چون متوجه شدیم بلیت های کنسرت فردا تمام شده. پس پیشنهاد جدیدمان را با ۶ بلیت برای کنسرت یکشنبه بهبود بخشیدیم
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90419" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90418" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoPTU0nditKWTVjm6FkiSnMuPBVV9CLxfGYWV0ouUzyxjWocOp4GnomHXz2xXqFroJqM1dEhxZ7LRYWLROKoBK52H3wyE1N98BlBHtCWIzARgG9H5sIgdP1SwnIlERICsuvFN0dSO0fQZN7wYikoWRy_gM6nW72zmw7sO1kxEfkh4uhXsH8Vvgv6-P68zhMtu7fU69kriBBoSBaUruOrCqY0WVnCOI5FRL0Uy8SEMGYfAMOhmTdA-klvHejV64zO5mjPFuyxbD0vWprqf6Au8wj__YfSQB3mSsXJ4mXNta-5cTxJnVUUaKVTSNUCGZUBSoePbG84Ly8Yfq22bO1lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90417" target="_blank">📅 19:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl_oljQWGX71WWhk_W2riclgEvakVJGcOZm082teTxPYnhNyeA19SZ124o34NhdUCj1bWqIDxmaC-epj0NJmfkrm3FeCk9igheeYZhOyptHGA7Ks9XLBMb7S_nYLWJX9OsN70v53k4TXcmnRia9yd_6ZBrY3ym99JtMZnU7Tb7do9eteOJyrAKMYjPalKu4z9eHDCDTrkRNVdSVntzfpfCMZzSDacIdJqmZYNt6xUvUevuOvO5Eu946ni3RSqO_YYqzncI-73ZRlkaBi22MdRdw2sKZlz-s6D0UDHYmwdewjRsmaJdWBqp1zVega8nMavMfz2F858znb-tDgJWSq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
حساب‌رسمی اتلتیکومادرید دست‌بردار بارسا نیست
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90416" target="_blank">📅 19:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb_lVxWJl_o4JygknDnrVdD7w9LohIBpckXlrCyzKmEFdMFSeJTqbsspgytCpBK_ue7CflNTVAPprU1ut098qG22-Gczsj-NRNKE8Zich67VhhSDQryHVMzFgB1XZi6fMRasNxdcDpNdNrOiQO_L3DLsnOSk7-hNKLUIvoKGvYBjAgHI9j-Rw4asS4-WTGrC03nuJyzolnxcCiiYKipoaX_gtXVEpe89Pnqb3p8IsbwOFCTMgKXYPONcIJ31nOyyJFxOPZeLhNDhl_yEb0HH6X2ml_jlLe6xOthrtQVTF9NCmo99W819Nk-gX1w0BuoNkVYrK7fEi3wA2B1UqBfd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90415" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krEkBobuxPipiwBmC7mcgPZNqyGNGeCdXv_To7Wub4KRToBoHCeWieA5fJNiXFXPWPkHJxMDzuiFZGtWJ6oipUhRsDXg3PBKJHt6BRPtJ92ksDdXkGsxi13MyEUu0oCvN0gn7TOTHjMyuFvosdNL0NqXcon92b69S_sAnaKeyx9_IX0XzdWLWgC7DRbps7aVRTVll2Hw1BkTeCMGGNoiKgkAPuf2LIqdGMoIvFdTb1g-HHcXpoN3iyyEy1QpwLxBq0vnpFa4HtjKopiNzEsO_2RubmGXbZQL49_zl0jxln4P3EYND5mpP2Df9FNKOTdXVv0dtYzJFNQIOs0QJ3CGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه اتلتیکو دقایقی دیگر راجب آلوارز بیانه ای صادر میکند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90414" target="_blank">📅 19:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
دونالد ترامپ اعلام کرد که محاصره دریایی ایران از این لحظه به پایان می‌رسد. همچنین اعلام کرد که تا ساعاتی دیگر تصمیم نهایی درباره ایران اتخاذ خواهد شد. به گفته رئیس جمهور ترامپ، مواد هسته‌ای ایران بزودی از مکان مورد نظر خارج یا نابود خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90413" target="_blank">📅 18:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایجنت الهیار صیادمنش اعلام کرده در صورت تصمیم این بازیکن مبنی بر بازگشت به لیگ ایران، اولویت او بازی برای باشگاه استقلال خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90412" target="_blank">📅 17:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDsLOC0yhzu5vP25kCen9Ws75unOemLi3IaN6bzxilu1DQOf-cnDDBZtBxMRxdUYAI-glB9w02lVn-tDspq2YXOlNlyHOuUau67OdD7rzgL2tnnC21N6ol73TLLiJUc89XCMVEy2Fz6VTLwT9fmGXT4TwyhKMYzSqRZa3gWMxROxBXT9M3ejDTMi2c8c_aTMod1zr7_nRBD_mav_DNc28P5v8NgaML5WtdUF3Yt10C3IR6E-zVFPOYvydtxuJ3ZKOzHNSGUVhK4qqG2FcF4TQy524mhtLMOdzEvP5S_72b_E3-nQBG0Tsg27se7AUlPKw1Otbgh6OG4VCvpTNvh3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر آقای‌گل‌های تاریخ ادوار این مسابقات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90411" target="_blank">📅 17:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90410" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90409" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90409" target="_blank">📅 17:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97be903d17.mp4?token=JPetItp0ju0cCAm2YGQcdqDIZBeFAzxcqSeQWCv_EEWysKlDO_s4ckd44XE6ncZaFqVKVNcI9j6lvUlmgMEDtyHVWLyzsQw4oc2rB7aQQMFraZti63i5O9wfPmpMHNSTLddwmx_NtCtJ6STF6n-vZ2XVtWZnk0Xaa60TTsNIKbaxKiVaJ9uK24V9UIovn6qAEtabyBz3JkEjTT-xcSaXq-fU4psPOy0bgW0nJUBvQquf3RsFn6kX6kF0FmKFzSZe18zInNSwYgQpHnGTTISEidWHaYIt6RhPaevOO-kIxcjqzQHmMEcUK_1TuVKqdO0vSEKHdW2cqWkS2oQ-QFbmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل یاسر آسانی هافبک استقلال به الحسین نامزد بهترین گل مسابقات لیگ قهرمانان آسیا 2 شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90408" target="_blank">📅 16:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgM1e_A8qpw-kZYOJ68Qk7s0Zfkwi_8mVah51T9HxxZ0MNnobUdT_aO24_0lP691RWA1esPZ7rKCl3F8lRJaYG_jTdsNbTD2R2ii78_1FpAREROPb6ZhXn7tLCWa5iP4psYrL9WII58_04BM5cr4sAqZS-LKFqnattghyKUXJcdy7QV4QZl1N-oFoTW29VifXlzRA_4R5j3XiSN6VF48w5DsYzUuZtBwfTue-J5KycbkDsuCHEaYc7n8TxiOcKsOQ7QmxL5vLvms2Q4GPswclej6c_6q6NDKJ6N4eCUC0ZyFg6uZW-JsLT08dWWE0658LATtU0TFhMBs-9X5il6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تریپیر مدافع فصل‌قبل تیم نیوکاسل با عقد قراردادی به ولورهمپتون پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90407" target="_blank">📅 16:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9vvmeIcOf1mD5N-tki_KtXfZSKaUZ4rkUwb-4TFhoZygjeB0EJmeGBZFnJCcFeVOIku0NNKF3dleIQzhNm7KdgaKpivYhB3hAo3JwAR7NmayJfR53Rnr4zrRbJa6Oupe87L_khpcV_ZbolUYBdwVXb359OqXzsjZ5O_s0hpEfP-2KQClDkC0M_ncVHo1fCw9QBeFKkH50eJFdkhL-oVy1jGzIeq6-uOKEnqyDEPYqyIejMUCM_ND6N72y5sluVpiMmjIZopz2cGzA0PgSwGyJ_gq6mTzJ5peD7FFlQcAmcirabvZs66jOMdv8i0uNvDjFaY6AvfrlWBhup6j3Hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مثلث‌های هجومی آرژانتین در ۶ دوره اخیر جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90406" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usmMtdsnhEA8K7dh29mDRywEUFTmaR8_uvWGSmbyXiL8Cx9-gcida-J-E8SPrRjdjrbMNtlZvcp7nWW8-j9voBFvHk8Jx2uVgfGgmYBenXk8Ye528K4IKGQGTHHd857ZOjYwZeDfZqoisOfFa6qbKJc8ood2gPMoMMXYrhvumQiyrzGhPefs8ag8zix86KclapSdZnNvfnm9M0xYoiwLFQK8mSiyhPlH4J3ZDucRlfdK6cigtbIbNWVmWYbdIFt0-Bv3h_B7ehl8nZ3NcXNfGyfuEgIyuCnjJ1S2UzBEUArzEmmIswdj9BcXBwABb1kUSvAYNIJVceITL5Wylh0pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↪️
🏀
سوفی رین، مدل OnlyFans، ادعا کرد که یک بازیکن بسکتبال NBA مبلغ هنگفتی را در ازای بکارت او پیشنهاد داده است.
🔍
اکنون کاربران در شبکه‌های اجتماعی تلاش می‌کنند هویت فردی که این پیشنهاد را داده پیدا کنند و تصاویر جنجالی این دختر به‌ سرعت در فضای مجازی در حال پخش شدن است.
1️⃣
داغ‌ترین عکس‌های سوفی رین در کانال ما!</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90405" target="_blank">📅 16:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfxgu2NIP9ytYfcFk1lkX-ZpL_o7amC6RHx6pJNNgfiN6Pi8JE_QwFSiYX9P51dxEzMKB0686oXF56uFN2inE9XHYo9r-VVqwre55YihE9QMsZzZ2KIB6OWFPgDnwo5iFQL3mSm3Vhkd_8SJvjG2RtO0Vwt-dOx4xAEX993GttEOJzCq3o5p5u80Ucsc8ezOn2lJcXuvkE24zjpXz4risk-nShI7krYxjqEjX8o4HBFAc2bqya6E4sjai2LARaKPdudV9VGND0j8k7gVYXix96xMQ9mR9jBn_nyVqe094Xfr93ogIBnJRr3SJ-EmhZEuNEoj7rTTBVKR33E4TajBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شانس‌های اصلی کسب عنوان سوپر توپ‌طلا که قرار است در سال ۲۰۲۹ اهدا شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90404" target="_blank">📅 16:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3204b2c2.mp4?token=KuY09Sq7D1fqcpK2EcDoF_pYhvZ0xVyf0TjYkwTEWCtNZHitKyG1FCRSv5V6YAb8g37r5PjDuSthf6TljSk7i_qgCk0JDwRSUu5yQgNRk_QmAhyLrVLPMGBDK5YskQwipMFp9-3FCj8k3QSnsi2T19k6nhHwJmSLai5_1gsZhXq0WDSfCeOjzBairrWZLea15tgt5leXhYsvLI2oWs-AZ4kRlYJoyn8KzhThIVzmR03x2oLuk-6I3rNu1tf8Ht9NLgn0p3TkTKfOvl_PPhNb3Er4ZBdafYVyJZT9CWUOOYo63tKVsTuJlZqIGeEnis_5ISeOSOeXOH-0_RksccR-YrLpXyqGpd4qkXwyvLCV7xdtgLZfYJZ-dsesy9Qm-jIru4mwSBncn70P-r2TjpqSuuOUIKUUXBfJZb9Yd2rk7izE6s_ke3Ru7o9gNCxaTH15-5Oy3q-5ZKNUzsa_Kj4VA6bJ5FjR_uC4ieeTWtUsydqgYvZMQlQJjQ3Xe1L_efcnNegdLOQp9l-aOrKl7Zk0FadSnD_iImc4ZkNEAXj0274f8fv9lykFFxgrdTNaoO6fpNu8s-cgnMudKwCzEMVUJ15xC_ZnqgdCrNakwhZzFbBcJpRCSsuIcI1uT5FphxDJ5Z13iVVV6vseHwaPbnjghW_7_s5A3BEhYviwPls3QuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روایتی عجیب از کمپ تیم‌ملی ایران در مکزیک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90403" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAfNhvIz2uv3jNOvHyqBzPuSWU90rtJIYIjWTwMM8JLgM70P7qLBdwSOfBPsMvx0JrlaHd4uTL2nM05QJbpsJ8R75cqNgPfKVbRAc4-6JN8l68HexapRYdVOFLqEdZ4qku2qjYkTtsIVKLBAYPUkhHuOXeRSdKuI7iYLrqWFQmkDSW1v3-wyZ8fsWNi7Z7QaJ-vvUvlIfmNpEEMFBXSIVrexVClSOfVM_w2D6HErceJgxL-LCtNO32yAqfvCxxc7TMr2Se76t-YG3ldYacmWZWiqpQQepT_0FQpNYCV6HIRq3QTppNU66J6x_9hplxjsAS65sf1DyS_fCB5UifzGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی با بیشترین پاس‌گل در قرن بیست‌ویک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90402" target="_blank">📅 15:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb048df6e1.mp4?token=Gm_HKPNlbQ-kGGitWdsog8yN10XrXEFqyDQSqRmfGQx1cnVQIZKfCzB8nnQn5kbKdrFnOYv5ghAU_EEPEfsafM7w9kbXLDieMutw5GTv7qmNsDIZeMWcLsK8ARhQH9F0BNrty6pocSVGWMcJxDyrD6pEawlElzbUuBLK1HxeWvNQD0AaGe-fz2plj5ICKHM7t1SVDhFqzTkg6TxFko-etnozADFqoMi5tBdc17qNUc45NnFrbMAAWkCAV7EHb-5Y8st9y2qmdgKoDZDGDO3FbfL7ol5R7-7fM3pDVXTdXAEweCqZFSl5ZfV0THPDQ0j2-FQCwi7pTPcZYUkNZT0afA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت لاپورتا رئیس بارسا در ساعات اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90401" target="_blank">📅 15:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBbXqgwvtueeo3sCofWVfx0fMrg1YimEDr5_KveaOyzMgW5lBejRYanP0xq5nYeV1TGDiCGzY9wkdAxCA2Jyf648K5OgD5_hIO8qaKF8Rpc-NyQI4Q0I6mUdc6h8w9ELoJRkY817Pc04GPfAbLep7NV9Peo9kJW42MH1Bx4E84g3rP1MdHMCNrtFAjaMD171KyAlDbk6oH-RG2_I5AcB7OMbBAdt6N0ZS0HMu9IAW_rMPttl2-a70cURlOMAQof4o6wa9RS2RcUdfUsDqXnaE34oAiQbXrs776ghOC9wAs29mBovA99vweZ_uwwE2zrqaMOA215PQFPxDT6xRs7M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب احتمالی بارسلونا در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90400" target="_blank">📅 14:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70d85d83.mp4?token=HuMmEq_98ZXoclSAkERc4xRyMTIIaz-kjdtwlPEwqqwfa-MGnFR7CMVqTmFC8Pugk7PT5dkFyRpHkBwTiqdWJTNDf1tJbYwgwy6Kvo066_hLfYW8_bpXj4s0UqY1jwEp4N_NRmiFjAjIl3TMewqIa0vguoehIFixItn-XOEeuAOLH7SG-Lso5bpuPVmiVxOimJc0-m95ZsFQlFrnwUfXrdIpa1MXplsG4PCT8hkDzKI0V-qLoXMxgGzvrIeLAUNkmi3dh3-TIkTpQUAPyUhtyR9DIht-iWoOdmTe3NGHQJiMakPlV_s8-Rvuu4giIqHUl3aC5IqfPI7WdHfJgyKQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
حضور کریس‌رونالدو با جت‌شخصی خودش در پرتغال برای حضور در تمرینات کشورش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90399" target="_blank">📅 14:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vC3OUFnDLLUviANm_ImLOsZ6wnRfyj4ylggtCklAZ8V1tv-NqagwY_pyWzJm7u9PjclA26ugxMBa5JTMgdx4TedBUHh4d4IDfyrhssI1MFUNLj9eAFDLGLSLk7rLqWiy7uKG8DCwwEeeBji6_GboLXOOewdPg8xPfSGugdwqah2aMhtfjcL3nWh5dh4ywMCooldB-TR1oPepXvKDIa5dCexsJTbEzzjyv51x3JfOeqoPSBxh-CtBMc4079zaqFd3IWKTg3A4yeXRil5oKXSgRm4jwczEdVUmO2nbsp7JyaqjSZtQwFLhxqod8mDK7781StRTFoSXcxsSLmrLxRcOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ نیکولا شیرا خبرنگار مشهور ورزشی ایتالیا اعلام کرد که قرارداد احتمالی خولیان آلوارز با بارسلونا تا سال 2031 خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90398" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcXQEHDx2ViB-uQF8SzSrMAfpgO1fh0wfx3WSssr5TcUzekpPF90X2xqS09z8o5ln8lT0xvpMLjMEMiHKzVQjibtEyLa8c4itejMQFCdueMx7A6sAyZStkFZjcBimcc38AP45cvaZm7dNkYOfzYBeCw9iRjCKzXysGj8szipfNvH4s2husx9iPm7mtYVzeYUnkhWu2w9hmX0IavDRB57z8Sz9DMEcf_qMvd0yhBcXVeD-LHAvtvFS4biJKGoF6CZwvHoUspjErx69hTbk5KGitPHrEcB66z5X0r13YMDKBajop50SahxqZbZrABsUiaM5GeeRbq2rtP9vaGHO8ewKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
به نقل از مارکا، ژوزه مورینیو اعلام کرده که با توجه به نقل‌وانتقالات پربار بارسلونا، رئال‌مادرید برای رقابت با تیم هانسی‌فلیک نیاز به جذب حداقل دو ستاره تراز اول جهانی دارد و برنده انتخابات رئال‌مادرید باید در این مسیر اقدامات لازم را انجام دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90397" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری از رومانو: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90396" target="_blank">📅 13:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyuOnaDLAFvvUU-YrKXyLhS4ElmukDcBB4J3Rxi6Enceh99YMVpjhhdiU5z0H4ttYffIzfwqLd4MJ2ELXoR7WQmhHt-3UIdo6fqkpQ02vp_BblpVuX_OQ2XItUsAjS85x8s5UnuvpRe62DgtA14i06QJoSHYBo1UIFYzBXcMW8Fnq7MaDifDaeO7dQpG1V9d0_AsInOUuy342KEv1541UHmOiC6BYl0bILimHzJcq0-IEW9rKE1QqUl960Fo5DdGzvVUEhXzg56Sr-D-qeXP0ZySkrHg3bjznls-pnG5FrAu7ODuR20Py5URKQUtuB0bRSIPd6AKUNizu8JOTJ4OGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90395" target="_blank">📅 13:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp6cYFBJALxtipSx3K-8YEyDv6Ow-HQ9L-M4aLDuaELpsSwo6k8bI6ZPC1YTDs1xrtS1WnjX-zXYNEnmA06egGyUan3uUUUuV90AV9xJdO6QkJWXLmnPm0rdlJIv-RgqPiwOjWxifZXYX6rXLGgSg6uzJWiAV4pnp5i-4mbBxs_7i34xckflNsOK-ecNJ7gzffb9BJHmSPEjNsEHm_c23IklU9jZ7ATGDg6lf_TxSsILh1axHGXVxF7Cd12sklxQbEnE2xY3f4nrXtE5qKP0fnEO_3_eld0HPENocWpAu7Pdeqke-ceuT6lxBmvuWjrXmjhlP6aJ2zPXcN8HnEZflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
؛ متئو مورتو خبرنگار اسپانیایی مدعی شد که اتلتیکومادرید به جذب تیجانی ریندرز هافبک سیتیزن‌ها علاقه‌مند است و قصد دارد بزودی با ارائه پیشنهادی این بازیکن را جذب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90394" target="_blank">📅 13:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3D2TDM6vryHk-B8a1sWoIKNDD_KOrWaXnTBRgWHHVK06TAroieSKZ2FaH3XdCgq09uwPLrCqdpf26Qm2d8x7Xsy18bpxtdrmak5pQRIbCA7aqLWuIR_ceiqlnXsM1hzqSMeJR_Ln9-Lb0qX1701rQqU3TA6nnS3CsPw_h-aPGewjAsbFJagF7UsWm-zi-JQX2YaYmhggSBx8Ik8L3MMpeiNskDMV_6iDnEhDRqA0sb26rFweljt_dzw3I42Wt5IQ0nlY3sMKyazQTmV6UApH5nFwtRFTFDPa-4AjxgagT6ouMKS8dE-kh9n7FRGvx6MnDWsABp5WMGV_lfYiUwCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ روزنامه آبولا پرتغال مدعی شد که مذاکرات بارسلونا با برناردو سیلوا در مسیر بسیار خوبی قرار دارد و احتمالا بزودی منجر به عقد قراردادی دوساله خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90393" target="_blank">📅 13:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEEZxaO-VoP1rXJ2U625byYIyx2ERsxl6FEK_RJ9hnWXpOGCVNEohDtWpynbp_v88u5MXYnY2tiipu8W8eZYwlB-iLxX0pobqkbr0rO0m0NdMqB_0kyN3KdUeKIRibqiD_3Xg2oNiwV02QDuRtNGJ80du5QZgr7eRiMzU1-ipxv3-PY-4YMJp1iKR1XooTHp7h2jfHrtGYavTwparfVjOek-P3tqahdq9jHph-df2qUlf1jy6vPA3dSazBG7_g-RNg2kJGmP5NSUfvHuWN-oVOK-bc34EUvRQ50vV5iL5t7DyyKwqnQsZ8ObzLqxKvEkH2kqXIu7RinBzCOKJV5MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوری
از رومانو
: بارسلونا اولین پیشنهاد رسمی خود را به اتلتیکو مادرید برای خولیان آلوارز به ارزش 100 میلیون یورو ارسال کرد. بدون هیچ گونه افزونی و بازیکنی. اتلتیکو، از وضعیت 24 ساعت گذشته راضی نیست، اما خولیان درخواست جدایی داده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90392" target="_blank">📅 13:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg-WUNJRh_hKeBNM78c3dp9AoQAg6E401lOl9r7FvoRox2Lp9La72LYkyrKImPV7dfwqaHrmhxf7SFoeMo83isoub-3wDW06QDRD94-ZTBqzy07WizZuOZFvK3CSW0Q8FiAy65hfpMJduwjXFrX9fBxvxJM5e-Q9umnv0oE1wsDLW4RJ0r9iLbiVTyT59qNXTJdvXjeSFncrXro1Z1zZkb9JYYC5O7jQxgFFt_PfFGZphCdSBueQzvGUlimP4k3Z_uA4Prk7n5uNWMzxsqEsAO50Ilrg_qnczyoDOWrmY72sPRZ7fXjF6j0QgX-9tkIUSGZOZX02MLH9RgU2mKufTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عمق‌اسکواد ترکیب آرژانتین در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90391" target="_blank">📅 13:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766445bcae.mp4?token=YpB8fxlrRir7j_LRvIiUOMco25_v64xCs3_9sHQUk38ACi9WlpDirA36281lmH0BVNQsuGV4BqKk3qNHaCCsDVfYvgc8JgxxuIxoAQ4jul-qKw0g381s7M6iam0wp0gr-qxh-T1L2Zidh03pK4K3VJFA5whxrPRrP6grwJijoJdI_A8iOiWkBfLbjewHswuB-rWX4QF6xSnv5LtU_1mkHrOVeBFdLCtCm9KXmXHwUoGZY0-w0OARVN9IdhnWNBDrAI43ldlZxL64mF9EVBGjPfdwfbERzB3UUnRtgmYW6WKpQzPWZ8AvhYhX9A8DzVewf4LWovtuau2-EM8ods0t5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766445bcae.mp4?token=YpB8fxlrRir7j_LRvIiUOMco25_v64xCs3_9sHQUk38ACi9WlpDirA36281lmH0BVNQsuGV4BqKk3qNHaCCsDVfYvgc8JgxxuIxoAQ4jul-qKw0g381s7M6iam0wp0gr-qxh-T1L2Zidh03pK4K3VJFA5whxrPRrP6grwJijoJdI_A8iOiWkBfLbjewHswuB-rWX4QF6xSnv5LtU_1mkHrOVeBFdLCtCm9KXmXHwUoGZY0-w0OARVN9IdhnWNBDrAI43ldlZxL64mF9EVBGjPfdwfbERzB3UUnRtgmYW6WKpQzPWZ8AvhYhX9A8DzVewf4LWovtuau2-EM8ods0t5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایجک گوردون توسط بارسلونا به روایت دیگر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90390" target="_blank">📅 12:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEeItu8uWZmeAyBGoNivUyebK4b1AZxCVujePv3a0yl5Ody-GEnvFwvxLob40GoKVXv6F1DUrUWkVTuXMlx4mtgP05356zktrFlwT7UG534bfvE7FsbkQIjpYjdfK_VcsCsQbWLbPiBGelOnoTFnQNcpIVONaP-ZEFRP0WjGwCe-5iGKJkgBEzgV5vqI2Z0RWMLZkj0BiiIUnboca3UReaBcOv7LwaNdteUdeVirsLWHRizbkIeE4YaCHIIsb_ozXrnGKFQd75UJHtiKfDo522R5k3r18nRJHpk0XOJ7yyALPqPghlAsv5Nj2jGgqDk52vw2E6a1Et5Yq0PbKknnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ باشگاه بارسلونا پس از تکمیل قرارداد با آلوارز، بدنبال جذب یوشکو گواردیول ستاره خط دفاعی باشگاه منچسترسیتی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90389" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90388" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0iAL8u9Z0tj2zpYmpSONqKHCgUGd0BoocHwiR9X0jWUU5V9T3kr5Eq8zZZO-Y01tbXqt74Z7xPrDPe9A-qHlnjgczOf4eFbUZFRvHan-_GzDwHVAjWE2iVeGir59wU0wRrZrNMv8yeIcR4h8Wg1fSxYwSmTovoxIrEbrqzNYAMKyirUGf4XsKm-ymFku4W2E6i5ij6UEPz3aEscK5jLA4h9YzqFDGBnb8PWAHlL7UmVImqHoXarHLXBl219RQJco44OJGAtHgjBROzQmWFw-kOdm5hQZYEDVbEEqd3ttSxKn6t9XIx4fy7tl_dBHnyWe11rj3TO5DrhTdHbFolYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90387" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-BPfg43c96Sp1mb2OdTX0AOeSd8w-B7Gq8hEPrdoTycfF2GHwdeRqwWOcXmWuCJF5830Aex-HCtwigj7ILTsMInjhjXtSMiJOZamrjDcnzxUnNl6RPLp5oVkfY_Yf8jan8VzwILgS8cl5NlDPJ8bvDC59c6zwucLUfbw3xlVFF4Bw3yhDVu5Q11LKqp6--vwIBP-_NKLlwspUhh_FdC5mnSg1XSCjRcrszI2d3D_EksXJ-Tcv2kSDTlqJbOX8lLNvq9NqXDKefzyByBpyYNU34c6lhQealbeNU2pxsjLHkaz-wBfjGzqubg4I95FlgPtBRrzJxVCOgPhF3ZwRaPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
؛ رئال‌مادرید با ارائه پیشنهاد نجومی ۱۲۰ میلیون یورویی بدنبال جذب ژائو نوس از پاری‌سن‌ژرمن است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90385" target="_blank">📅 12:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqCNwoHU8rvENG9HebZOt_MvMYNTbh8-A4kgpPQYCbY2OKRjMBGnMxkidM1-A-D1ndINVSb72lzOiNa_m4TC00I3l9G0H2SrfsLYOgMg0IYRW6jnMv4C2T8fXVEfCglUd1cQnAZ96f-k6VZiMDNfKpNXVHu3_Xchqe4zaUdwwzr3seUtnkQ-rEx-zdhI3UXeQSv3y9pXsQpMNN4TKdHVTa7S73a1PUgANhLvu9m0OE_ksr_8hqXlxGwfYqcFfBY_bc1Jwf5ZjCq4SxrK7ygUHtdIuWZUS9KMc2GQ9wJR1mfgHMoQ6jICPROKhxNikqfuiZ4wUISIn5ZLvLWAjlKE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای فینال UCL
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90384" target="_blank">📅 12:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=fU9DXDDk02hUkkQPcBjet6P3D9g4Z9GCz2cui8DoAvAvoupSD1ShGRDzKrZS6knKOguzDq7IRj9ec3U_nEG7x0yPGirgQjgK54cq70VGyXGnCFzIzLvGrs65aaauXM2S9W7FefpMEcei1H8VlQwuSf5LyEsObsxZuU9O-uZ0lZjDL7p0UMq78-ZE4XQB6aT5pD9qkoGKmHrIUMR6V4YVTp7iFDNLW8GUHgVHyS1wWr2b6qiQKqDH9WSabTj-lQS_28L3dIql_ONVUaKhHfzEFBI1AvbA8KfXfu2pUwM7SC68CFOXXfyiNXgCr1dw2b4pZC1K_l_BYEd1G76u0hiVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bcc3a9e5.mp4?token=fU9DXDDk02hUkkQPcBjet6P3D9g4Z9GCz2cui8DoAvAvoupSD1ShGRDzKrZS6knKOguzDq7IRj9ec3U_nEG7x0yPGirgQjgK54cq70VGyXGnCFzIzLvGrs65aaauXM2S9W7FefpMEcei1H8VlQwuSf5LyEsObsxZuU9O-uZ0lZjDL7p0UMq78-ZE4XQB6aT5pD9qkoGKmHrIUMR6V4YVTp7iFDNLW8GUHgVHyS1wWr2b6qiQKqDH9WSabTj-lQS_28L3dIql_ONVUaKhHfzEFBI1AvbA8KfXfu2pUwM7SC68CFOXXfyiNXgCr1dw2b4pZC1K_l_BYEd1G76u0hiVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره مشترک رهبری‌فرد و شاهرودی برای رفتن به کنسرت ابی: پرده‌ها را گره زدیم و از پنجره...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90383" target="_blank">📅 11:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M97mePnUH0hpfaIc7MvDXhtPiWdZ6Wry1BEW5PCA41H3uuFE9_0SObY13UrhRlMtHyx7Eiu95gG0hZRRbxMA_JlvQEGkUZdSjnaWx4oYeAqry1vlzpZNtBnxipY8ldktu8zf332sdWEjdcY2_KLcjr7_lqYfPKN7I3vs32eGeVf5f8LhpvcSDiKCKchy8cZMfRb6yjHr5DmBTQLx-y3WHIm2LRtKiEuBykk49llFQqDZKEGUWyTkTyTvBTSNCBcSyR_0NvZocNRtcpfIOK_jwSnJ9NhPXS1bdr4GOwNbZ6J0qyi2AekVK5LO6mKZXZ-dVjY_6MxXToEz2-k7r7YaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ اسکای‌اسپورت در خبری اعلام کرد که ابراهیم‌کوناته ستاره فرانسوی لیورپول در آستانه خروج از این باشگاه قرار گرفته است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90382" target="_blank">📅 11:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKApjsEHnSMv6NxpEYbdyIpr2ktSvX0VQ9bCpVTzBAClvpWCpTY5PXyQ7I0qd6SfUsbCUyTQ6TLoMFUF5dObLJwFIEoeyVd9q2t2HHEAIFxd1jV7m4-JzdFfzIN37IHmoKQHWTdyNCsTZYc0GHSfpXwXk_zhLYtddXhJdz6dFTarMdA0kOyAmCiKLlDPhbrJ9ogAIAwO4dYUuvE1t8vhle1wiN7RX5ct0vw8jXjSwnUGyEzgPl_suXI2gBAW_9XKxU0Kx4JNcnRgzWDxSKrJKnk7Mk3MVXmYQeGKkI0quecNbb9vhlBX_hbEgaqnZGMxpv7vqr5TPIroBcteZPoKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#فوری
؛ باشگاه الاتحاد عربستان درحال مذاکرات فشرده با یورگن‌کلوپ است. این سرمربی اعلام کرده که در ۶ بازی اول فصل جدید، دستیارانش هدایت تیم را برعهده خواهند داشت و سپس وی به نیمکت اضافه خواهد شد. درحال‌حاضر منابع عربستانی از بررسی درخواست کلوپ توسط مدیریت الاتحاد خبر می‌دهند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90381" target="_blank">📅 11:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbjiiV4jWkVlKyd8xJPz1BUdDq9Pvz18xRuDJJwWxceDyLBUSxyBbyoJ8gZaINZgxhBdiglOBH-qz_wGY8hEco1LoMq84eeqopGAxl3WQuDwdWpqBMRqoWD9Bwq9jcaQnviSn7eLxmd7BtkuRBfBup8_WTee0oJ6eLqQ1uaE099_6Bm01X4uDHhC5n_TurlC7KupeLUtk1GBYSZ-Z7yTXMdSXYe8PLXuwOXcU2_48yCYGqwtdMU2FGnx3TIbaP0ZUBgMqm9EyrsbC1ApEqsetC02CYWEDUCd5jNqaauOBJnkOOsZitiNtqBiGotZnhKAqllUNmZVEcd7FZqB15vAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
استوری ژائو پدرو ستاره برزیلی چلسی؛ شایعاتی پیرامون خط خوردن نیمار از فهرست این کشور و حضور این بازیکن در جام‌جهانی در ساعات اخیر منتشر شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90380" target="_blank">📅 11:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVKkgLRb0xINz5eDK9z7BbuXRHyADdIESYBQ7p_1_9gQ63hjhJmqmS1i3fQUAXtUmJMRpuRQAzMvHyRgUcDun9iPugQ8FSXIf4kywckfs_iiObzqIW37i2h9hxC0RoASqPyqr9ZJZtksnQX4jukgqtfIP32Tq58aFXokFgFGOei1uWI_7XFeoMdb2ZcCEsylBFLOwe1OhSd45MY9cebuoSibevKqZt2UTIN8_PiX6CDiRx7WHCZ2GFZGwbRML4NS2LrgMYq-TDKYFxTZ3N1urfsZPHtkHbk03tNRvxekl0abhpfDweODedcvz48NuwnR5XyTJ2e_QizQHe5tVoy0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🏆
ترکیب احتمالی پرتغال در جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90379" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=DmqDfDS79qaonHi6pMbfmzYWl9361xcodlE6QoyAffmdw-huQMmU21gqnlBF2MBia6qVc3IwgzXUB-fQQVg_nKdG_kOo9Z2pS4fSu9AEmHKXpfyoe_YT7fotFKca0pByMqYj6DTroiTtBc3aHPnPRPG0nX-fBiHI7le7jwmq5nBgzHBTeLYONfBEm4nABTYKJxtIdDKXkcSZeCO_0DkuvB5vJAVF5CoN85iXHHdQp2sc6a9vU5HEJDQPjVZ12xgh26tEO433y8Xj23yZ1Luo6fI0-9eNWjb7NKMmKa4UkPeLA5Z653jbFh7KnNXPNbIBBVvhkLjYsstTq6mG6LoMEiiyqbpAPVq1jQC67NTXObvfGa5pDFbJW8FOxxEIbeIoiosf2zf8Yi3zk7Ty1f6At_l_mTeIa8EP7j6SRl6jE7St0XZvc6ogjG50NNx0nJ0D2ozlx_ggo8DmZ8QQ94F4riekaQMaAVuF-P7TaJ5OFqhrs7Gx7Ab5XggbMOxk2Wl_XmEVJ5HzKyShau72J2OrrSYnblhEq2QGSy4-qaDlRpRSjSD5l1RckOnJidLXukj7naRCshLAZ7xv4-mDI2QwkKyiM1nBUTbEw60CrbEGcTELsvEdVHBdJYmepq_FVta1n8DebSzWHlTUfezOhF2sQpJM9PIiDpB9iCxLAH2Gr4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20638b4d5d.mp4?token=DmqDfDS79qaonHi6pMbfmzYWl9361xcodlE6QoyAffmdw-huQMmU21gqnlBF2MBia6qVc3IwgzXUB-fQQVg_nKdG_kOo9Z2pS4fSu9AEmHKXpfyoe_YT7fotFKca0pByMqYj6DTroiTtBc3aHPnPRPG0nX-fBiHI7le7jwmq5nBgzHBTeLYONfBEm4nABTYKJxtIdDKXkcSZeCO_0DkuvB5vJAVF5CoN85iXHHdQp2sc6a9vU5HEJDQPjVZ12xgh26tEO433y8Xj23yZ1Luo6fI0-9eNWjb7NKMmKa4UkPeLA5Z653jbFh7KnNXPNbIBBVvhkLjYsstTq6mG6LoMEiiyqbpAPVq1jQC67NTXObvfGa5pDFbJW8FOxxEIbeIoiosf2zf8Yi3zk7Ty1f6At_l_mTeIa8EP7j6SRl6jE7St0XZvc6ogjG50NNx0nJ0D2ozlx_ggo8DmZ8QQ94F4riekaQMaAVuF-P7TaJ5OFqhrs7Gx7Ab5XggbMOxk2Wl_XmEVJ5HzKyShau72J2OrrSYnblhEq2QGSy4-qaDlRpRSjSD5l1RckOnJidLXukj7naRCshLAZ7xv4-mDI2QwkKyiM1nBUTbEw60CrbEGcTELsvEdVHBdJYmepq_FVta1n8DebSzWHlTUfezOhF2sQpJM9PIiDpB9iCxLAH2Gr4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🏆
هواداران پرتغال در انتظار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90378" target="_blank">📅 10:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=dh_yt_5SZREAcg7vTs-rLP_S5hRW-HTgDxNZO7bsTc0S3U_B_HK0uudfzSK10ubjjj3IFtbIo5naE8uDlBcmhz6g-XMGnrO48DG_km5k3rf3OoLkRSFTEreiBJ_0eLrQOmc5IkgrB6Qu5MMp-1n1P73wcqhqDIaeXw-5AQQklLgSFEqa4aKM-fToq8jNYVny93S4ZkJf8-i6IdcOP-6xhSvl_cNeAMx0eNLOt5VIf9GU7zYKRc55orLgLqlg64O4_N_WAu81iK_9pvM-HS87toJoztp9c0pvKflaKnoj1GEhNZuYIV0yuGioAGhqKJT0hTcZ4pW4WocsBHWDKzBSD4YMtvfooo_9MTQ7NNmrvIa-fu9ScTAlj_Q_w5WRyP5g439aI8ewV876U-BvXAazqLaOLaA0w1xLUBejn5gICU18A_ZOM3Gs5lStpkf4cgocg3u2pUqbbe8yCK49eSwZmy9RUMUhzU9w65_Li3T3GKG67euztHDaJscFqrq_rZN3RW00kbajSDb2UHtQWhvdc2oBRjhvgdsNBOIhT5_dsK9Ai1tXVCQsYMPYBiIyEEwExMqeXrCQBNhdsQhsXwEOhCDsDNXpom9T6T-4YkYhVrO_67FKCB9xzHN3NTqEzJRN1kEzCyO781wvqfzQAK-k1uH-R64Z8iGjE2ZX49n070s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=dh_yt_5SZREAcg7vTs-rLP_S5hRW-HTgDxNZO7bsTc0S3U_B_HK0uudfzSK10ubjjj3IFtbIo5naE8uDlBcmhz6g-XMGnrO48DG_km5k3rf3OoLkRSFTEreiBJ_0eLrQOmc5IkgrB6Qu5MMp-1n1P73wcqhqDIaeXw-5AQQklLgSFEqa4aKM-fToq8jNYVny93S4ZkJf8-i6IdcOP-6xhSvl_cNeAMx0eNLOt5VIf9GU7zYKRc55orLgLqlg64O4_N_WAu81iK_9pvM-HS87toJoztp9c0pvKflaKnoj1GEhNZuYIV0yuGioAGhqKJT0hTcZ4pW4WocsBHWDKzBSD4YMtvfooo_9MTQ7NNmrvIa-fu9ScTAlj_Q_w5WRyP5g439aI8ewV876U-BvXAazqLaOLaA0w1xLUBejn5gICU18A_ZOM3Gs5lStpkf4cgocg3u2pUqbbe8yCK49eSwZmy9RUMUhzU9w65_Li3T3GKG67euztHDaJscFqrq_rZN3RW00kbajSDb2UHtQWhvdc2oBRjhvgdsNBOIhT5_dsK9Ai1tXVCQsYMPYBiIyEEwExMqeXrCQBNhdsQhsXwEOhCDsDNXpom9T6T-4YkYhVrO_67FKCB9xzHN3NTqEzJRN1kEzCyO781wvqfzQAK-k1uH-R64Z8iGjE2ZX49n070s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌موزیک رسمی جام‌جهانی دوره‌‌های اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90377" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhNL2zZglO1mGjPDUxktOfn2ajqPyueBQ8bI3Kv85bWJkqbuL2sndsa7IuNOgyZ40vgx2AQOzo5FgpYhC4hJJIjJ-fkwhOBrrntk8QUwDxxrF_LFQvF1OLZp7ICqFmlF-LKBBRzeC2KdSeM64q_JPlk2XoDDKAt3vroaSJI5oHrCO4DO5GH7xe4Bf8mUOP_w5cZznbrvlRSIAfMGRkP9uY2FfALKhAr19sXEZDC-ypgsl_7sE_7Ezu3wkzqdlS_xG-vP6sRAOH4XxzZzlNR6YsnujwrDOxOq2kp3xnEYJEW6fzNNsv5UpGh1u1Gm8Xyzb3jYTs0vUFiq-eqtFmG0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جدید یوفا از جانمایی ۴۳ دوربین پوشش دهنده فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90376" target="_blank">📅 10:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZSFIeyzhqaM7z5IFQxfpV6Ns3E8k9YXUR4ippWDSkrmISB8yh6ZkLlS9UxXfj-vJCcjwGTNaMAJwuSR_JygMLWIpVgGszZOuDSENr-z6ld5JpiJs6Jbq4NelBSPi0N3psVQtQzB0XP-yDaZlQyfrVMrPXIVbMv2Uz6oGcwMkf9lQstjvI7i2HeVgGkaF7gsP6PA75kfEDhLoMRMUa8pPP87qmktfNVJ2Srh2yFaSl_p5JYh2hwyM2Vx3m9tVI1xdw0vaFvQYJLzT3ihmlYharSOplkBmJoovhEuQ2FMZKZl4iZ9q-675wHe2w4iTOLi8atenSnpgo9txDVlWwDEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ترکیب رویایی رئال‌مادرید که البته بیش از حد رویایی هست و احتمالا محقق نمیشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90375" target="_blank">📅 09:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
کار گرافیکی فوق‌العاده زیبا از قهرمانان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90374" target="_blank">📅 09:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac09312735.mp4?token=UNvFLiflzNky2xKNiQOytMd8TWh4LVGmSmqY0xdiAG8SZ-2-W2UB03L-ZIb4VOTVjeHqYH_4Yok_4UBHLajTaYxJ5Ya_Kx-5fs_lXcg_7fix_CdWMRAWSrQ8UQZc6Q7GMg8kLeA3q0hR2jPKJA99q2tpBAS4qGq24pJfttYR26VsHeP0xrk7_CfuEbPtWl8QVIbO8PY5gNyr9U_ASVGe9ZU9eFQX078onVJk70nu5ZGYFnJa95Z7LQQ552MMB_Vz4LrTdcWrkoraTaFWgUj0rJGkykoAvnUhwqJkAI1xNSZEHT1RIKZEXUUyazoJWtjQlCldgk5bmrGpzkZ0BrOY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac09312735.mp4?token=UNvFLiflzNky2xKNiQOytMd8TWh4LVGmSmqY0xdiAG8SZ-2-W2UB03L-ZIb4VOTVjeHqYH_4Yok_4UBHLajTaYxJ5Ya_Kx-5fs_lXcg_7fix_CdWMRAWSrQ8UQZc6Q7GMg8kLeA3q0hR2jPKJA99q2tpBAS4qGq24pJfttYR26VsHeP0xrk7_CfuEbPtWl8QVIbO8PY5gNyr9U_ASVGe9ZU9eFQX078onVJk70nu5ZGYFnJa95Z7LQQ552MMB_Vz4LrTdcWrkoraTaFWgUj0rJGkykoAvnUhwqJkAI1xNSZEHT1RIKZEXUUyazoJWtjQlCldgk5bmrGpzkZ0BrOY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سانسور نام علی دایی در سریال صداوسیما
صدا می‌گوید «مهدی طارمی» لب‌خوانی می‌گوید: «علی‌ دایی»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90373" target="_blank">📅 08:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI5Obv2_ZNICmEfN20JJjC7Ftt7Gq1dG13mpAwfDlpQJ7aNV7-RFRObnhDEc0IcD3cgy9Fq_QUN8cdkVGfFL-ZXR83AUAQlt4wBTo8fdq4Dnt4nYrSgIiVZSwptfS0fsBdi83TmPpj-o4-_e0YzMeYayYRwnUeOJPhLyS_u2gop8lLZf0rZ_cU5atolKoxcyMqEkjYV8DNmEOFWQmHyFXS0PJtmpLkAcUzbWVtY3p1Aa-p5WLYFW_k2dVhEE8hkpase31_d3QVLncVzLBfwVhX4Ah0gOdWJPf-p9e0Vn5r3Dryuy0Bk1vScEb-mkd_zc9kJ47mv00VYNsQZUMcpF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
لیست آرژانتین برای جام جهانی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90372" target="_blank">📅 08:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEYRY3ymLekdR6OGlAtb1N69RdBgXTkLrEagqFFgaTgVBxyb4ORodUinl4_lItQxqDXZHkPxVb03f79fuWDm1vAdCcShyyaT7o9e9D2X2JXeqFKveQOnJ332JTlViSBxn0nA1YCz2FYE0ylJYeBz54Q4hHlf9UrRc5AmPVcj-bzFheAMQlQ--3R9ZIfUPFkr2fOvPi6ziHYzAdv9yo35MS0Ed3YOFo-IG7FUPdHgSSt0ZejNhr-AcROfaO281lmuHGLj8xMgeGSQOcMnmHrO1LhhQOpZFpPfSXkelk5wO-eWgh4XvpkXad_OWtUzjgmFkEIxbs4mWifoSNGlBVWbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل بعد بارسا:
😳
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90369" target="_blank">📅 00:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=UIyKNZPtUFkZB1Q0d-hSv9Vg4L02qt9k6MyZz6FO0NQOOuB5cWiJGf6-JlsvBdhrAD7tQeXTkLsVProxvXKZvHH1wLBBkRTSl1jNPG6St9LCJ7Q062Pmf_zjJ-CKlYDIiSc_uUlZkq4vC5oj4Se4uuvYWN0UJl_1doWOmlPmQpvHKn19qqp3t1JbSLcR9VXYq0W-1fjNEcwtI_GvVgzBiX1HwgvDU6HXKF57woMy8XdAglmcUIqLlunylBy6XV5vjfrHz52uZiR_3MAjOZPJf1k7jNxeWkCQlLHwy2_w6wWzsz5jFCWIs-kmDO23rGPgkCvX4X8KuKnqyw1eo0Ozeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5c4c6ab5.mp4?token=UIyKNZPtUFkZB1Q0d-hSv9Vg4L02qt9k6MyZz6FO0NQOOuB5cWiJGf6-JlsvBdhrAD7tQeXTkLsVProxvXKZvHH1wLBBkRTSl1jNPG6St9LCJ7Q062Pmf_zjJ-CKlYDIiSc_uUlZkq4vC5oj4Se4uuvYWN0UJl_1doWOmlPmQpvHKn19qqp3t1JbSLcR9VXYq0W-1fjNEcwtI_GvVgzBiX1HwgvDU6HXKF57woMy8XdAglmcUIqLlunylBy6XV5vjfrHz52uZiR_3MAjOZPJf1k7jNxeWkCQlLHwy2_w6wWzsz5jFCWIs-kmDO23rGPgkCvX4X8KuKnqyw1eo0Ozeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
سفیر فرانسه در ایران:
علاقه‌مند هستم همکاری‌ها و تعاملات ورزشی گسترده‌ای با باشگاه استقلال شکل بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90368" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=hF492416nLTe28Uk73mPgMmcc0BBdIO7tOlxfsUrDYT9cmLSMxRTWj9Tyskhklz71dbSAraeRpglQYaFRn1zcZwEgk-qh0F8UHomo_UVMS_0KqhPb7JYbO6KUOlDC09oYrqjeBvvKSiy6xLxstjnaEdtBVAgZIx-JcZRS3xUJ2J2WvMOHqg5zlDVGCAhZDiUBVSfYMEUPYBxkn-TqJ8zLfQXwPoxufiw0NSdto-yuRHnR0sHkcKqjwrpdkSQBLJBb_1seA7RfNAyBaVmhIdx8gsNTU6z3r9QdQ4_OK4nJ7z2KXNIYl22uj-i9JIS_NAAnvcTg1vdG4YyYObmEgXAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ff0dd9d2.mp4?token=hF492416nLTe28Uk73mPgMmcc0BBdIO7tOlxfsUrDYT9cmLSMxRTWj9Tyskhklz71dbSAraeRpglQYaFRn1zcZwEgk-qh0F8UHomo_UVMS_0KqhPb7JYbO6KUOlDC09oYrqjeBvvKSiy6xLxstjnaEdtBVAgZIx-JcZRS3xUJ2J2WvMOHqg5zlDVGCAhZDiUBVSfYMEUPYBxkn-TqJ8zLfQXwPoxufiw0NSdto-yuRHnR0sHkcKqjwrpdkSQBLJBb_1seA7RfNAyBaVmhIdx8gsNTU6z3r9QdQ4_OK4nJ7z2KXNIYl22uj-i9JIS_NAAnvcTg1vdG4YyYObmEgXAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
رسمی؛ با اعلام باشگاه النصر ژرژ ژسوس از این تیم جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90367" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پاسخ اتلتیکو مادرید به بارسلونا در مورد جولیان آلوارز:
خولیان آلوارز فروشی نیست و باشگاه هیچ پیشنهادی برای این بازیکن دریافت نکرد و جلسه ای برگزار نشد و از ماه های طولانی دروغ، نیمه حقیقت و داستان های ساختگی مانند خرید خانه ادعایی در بارسلونا خسته شده ایم. این رفتار یک تیم کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90366" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGJ9KT-ciFS0qZ8klYz8NA_H8xb2ayTu3LO3FX0es8NTGBB_pOrnjpfwheoOrmUrH4LIJROQrNAUdyxOKC-B2VgkfJDQuP7ZOItmXWI4CwaNirBRs--zrJ5eDn4e51-HRj4IpIZDGMutYpajmDjTUOiW3OHztbbxgfKTwmD-xcxnDLEtQjb9r-eH9cy41NAmOYgDDlE7xzZMCa17GSByLNSdFwq7x6rU7ES-WjB3GfXUShfA8IVRnMhIECYFaaJgjDbUvgIAkeL2Vjs0IKJpwJIqHF0j7J5QhHXH1uRibph26iksxg6cckn6HZz4413CSud6oqEp-TugFv60QaBJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی از سیمون جونز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
:
•
💬
بارسلونا در حال بررسی احتمال به خدمت گرفتن پیرو هینکاپیه مدافع آرسنال است!!
•
💬
اما روند کار دشواری است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90365" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHS_ffnIa_XeJZG3rhqgMRRMHjoYf-cJsMpRLGXv3fs-xriWEZ2gsGczEIXs5hvznnTPJh3og51MfLQ7ANHqowQHs8ubqlWqJu-apj6idOLNNitb6mbIzOzukThw_6t6UWVH5eqJcntzKG_bXHGTmcZ3nmeJWRIk6pp3_caHzLkH9fBPT03ovKQyQ3rQpe2P4Q19w3BDYbEU4SMpuFxZNGyK1uWFa8WZymSR_aMhO5xMMvDqcdOLDEDkNxXkSPAa8dHcEwrL4ZsxAKJhsURMznHoXfRB53qpZGQ3pw3CIvv15FG5WFeJXoLlsH7CBiVOPQDLFVsPD6P9s2ReoxFaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozp_8iYtohvno6Ctk0u8CLaG2gQFGcvYrYOxcmMJdtn9QMtyUkdTi9Y8xud7kKphBml41voKkSDw6J81qENJ9ueR0gnWZkEfKvk4UNdRhjRolEU4v47znvg0pBAtKGfuOhS-g3ISt1TY0pXKZeNM-46pMiHafoi-PoyddyB97glI_QdWjH05k6snGAAODEVofN3b8tM4jpS_a-B_grhPcPkcO3CfDUnjvNYNB1GRJcGombw9Mx5wWrvYsrNVFKMsyfSpWpHzFOUPnBSIQrQ3DkKxS9JGlnqmjwJ-MoPH23c12iQA_ACgHU-AQMkbCXF1NAFGbTLSItxlbW34c-Au5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6guq_qNCO-i37JWZ7D7tf4fvmDnTtvvi7WCDNvJQ2_TSipFPSnhrXP4jbr5NbHSsqpwGHiwSrLYjFkuOHkmSoVQ_MkMAM-pHov-5a-8QYx-CBkoO-mQFrHOmDIPC2Uh7XD16rWCgL_eF_PLiGHMielyvN6C9VNv0tcl4j6Lhw4uA6ZuV4v4X4Q2Agha-D7Wh65MnMCk6AZHN68GG9ai6e8Bi8oOa3mo-xh1O6Y5mATMPNExwa1Pxz_AjN2INAMmLxBHS0JryleoBJU3TUF5DjCtKt6FmWguU0vhF3HpUdIieQ-ihChU_1c8GyN_KjzKSJSvxKZmVfIiq_e7kVLhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qciZb21VeJ9LitxMqweINlQ71LH8fDri5KJlR2-0NGxPOAYYcJ3W-mauE1zvABvxFz0E5MecHM4-0srCkWIgk7T8W3v3Fk8B7n0zhtFMLnpkKBT4IUJJ1aV6WyYRJlrKQIqPk1nMvavuMIB-0UTNp0gXprdzkYPw2NGFscl9AhZeBr5vKC3xC3MYuhAID8ug9ePBMCHprc2CVP7Xod3t49j8kpn_vzfyFArFJTjE7-vJO-FaSMTHXHC_N2syUQIHiYhfJj_b9btO8LpZiTPimQP3FzTvCW-N9je2a1uJIC0DtbXmulnFPm__aqAYqyjeNzwC9f0p8mwgZjhXT8atCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgyw72Gv-COZrnOUQ-S-EKvMi6PLgLfOCcHAUe9JmlRa8oJaEmsOu27fkUKTgSCdK4SROv_ZPME3mbv8cFVoyLNGmnkD4yjvSXcbh1iNHg8ymOeT5nqzdXnrZMNT-HQsPVDjpP6LfkJDCT2hk3HRrgQ4gYD4Ms5X4VIk0Fv6NSRiV5lNJKtiKUa5yQTw638zzdIfTFbsDyphNMjBxrpfm6BcZoIZABVyyO1cuOcltK0uXPRpQlmtaJei2QyD20QvILNx0g18k772Y7YB_iDM5CffUlwiHw6lUYPLiAf8YPrV4IDQHOEXH6Iq8daxqzd0n9gQfyET3Yxnpj-Bi8Xhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ArjD2YwVomjhgOBuvh3oIEUfX1vbah5IoXZJNmLgSXZnFMmU4xKMDw7NBWVDzJp4rHks7VWusxozyrlNoosPQAGCPTCbssNjKppLoHouj8K4CnMn8cf2q6spnzLuKSUGoJEv6ey0zR6IfNeJep4hkim13QyzI7-7tFgYkkQzweqGnycxyA29VFSTt64gdbJycdL0iqVunc_VxEfIV1lrflX2HDulwUngB69YfRfFPnfSBOi5EMeRs1K-VRSx5x1kidJre4gAXQd4PvHRdwMZesGRMcaYoCi0mQlqs92dmcJCVUcwddaP0_bZtWAxJJE3VnqlVa6lp02ZgBDLKviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKDGS_DofXvAHKMTiA4UnV2fg8TEKxutYMCi1wiZqZLfSoxt2O9Stho05qyWDG6brkcoQaZWZJtzxKetSX3DFPn_l6FPuPoVzhbGr26qG5y60I5BSt2-IGybFKGLGbhQX02sPovZzkjsJbT3e-mUwus4UQAjQOvd4JnhJTojnlX8o3SMqBXtgCCwq57IknIchwkhVbVK_Oq3FV-2d4ifKrEvyyXD26uP56I1KQh4GYfVs7IDr_wCmTzz2DN4Yi-8YYjITB3H8g98RDT75Ajod9uylJgSHNLdnxNR1-Z0_tYLzCOpf3w7bxUDYT-OxftTDFVjS3BrHiGyuJcZzxjrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQp9InKieruJSmaTe6dz0Tnp-blxFrWqsecPuMCq2JRpGFUXoRo5L70KnH0LncwLylmRxmYDMOlrjOqFTB30vtnF_KkFinXuxxyxJEokngvIhI1fnJKhhFCm5aRkXE8aFOuDhAx9CcNHhb5NR468RpnkIDTNgbZAtKHZmqd0Vlc01obB7MLEJOnoe2nMpJVox90W20zyav5ta1LVdyIHLnwGB82pbRGst_1CPXFycHR0814A-FlYFjBnWDzU95j-yugOOuN-RxZL1Q1f18C6WTjF5d-wpVxprtPHfJTBUViOqcyxpA_bDBGJt-iZvYZIcAaZZx2nis1B3442jIWccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPznXcIdWeQKMmCoeTG_mgYD6Prqi6nO5VHYNl_dLmSumtKDx3H1Wmpqshe6vN8BoZzM4XyZg-LKsiA1aVz1F8exC4SzVLy3LU650hJETgBAofZX5nyGFiJCSDrZerzncDnrYhaEAkGy0BAUVZQ7bSEA89mj_RCoAamTuJR8XO8waY3T76eJqx__Y63pmIug8mFQji_5QYu8dQg4yPJ9wSmE1RCIlGZY_PkVtr-K429JzT0T7Psn5YhknCsk8uspzwimDLKiWcte-3cf78bRatw9NlTuwf0e4M362SOp0p6BfUY8uoZmcrnoBr5WFeNy0_VGUg-CrGlq40iBiFYRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf8I8A39iU9oUVHl-ULrgXxI5tlto1YkOi76D23RocZgUTDjOQ_QSIJkHJTc_wQvcZ6lKW8FXGYbKJkLeysKok6aZ-bwck6PxYRK_AaNqsSlihAmQwPVTqRKevGGnGyvv_yd-MrBNfRgjGhA06i2fV1VrUtoMjigoLvZMVturSgCwBoWeZmh1k6I-9ze1xiAgk3oAHOZd3vsN1ABLZ8evXcwVIeaA_8URQRUhCByg_1awFkrd8nMAtxQ9M6UDYfVi94Is9f1u29AC0gS1B92vMq3l163SfhYMNYq7oODZ0CQ5id9Nmviwx2eoVs994W9qfwqccIQWEi_Hi7x8GkknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1Iirs7_4LG-XdSrJ1zzqcEwLal-TAEFW4OtG-sQtR7M9bvK97WbofwxeYPcjC181pe7OlnRq5hLJjT5gNVDmtpKlZ7WbNXtpJftdSwRwTk13K1MmF4bAGpQ3kxPuj8UNM8DfZEgwoOXbqgdoTb3JRy6kxHy87JwrsK8UEuTvbCoG8aNNLVDgYjYXEFk4JqkIq2RvhIWozi0gP_OLEviMx86fO7wIyU2BuPakUA1drovc94GBPsq5riAdPOohVY8mCxGGjieWnmHsqyZudHxthDVaKAx29PEKn9qc0toUm7wL9y66q9jnaqig6ajri3VkrQfK8Bbk5b_aDhlQQowCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on5ssYRji4SplunMgSjKbaG66FIm0S0uyvsKeEA8ub-mdZcs_ijAO-006hdARQPWs9fKPd1sVp8bxIgEmEzpEizSjVKmX-XgxJTdyC8UgGKNIyEGbtjoreAHxADt3M6VzC884WVaHOnk9Pdl585fPgExwEXwVksFBPY-flRUfjmcJMIcjOT6tEf1B-Rq6tKUJsQAJN2hkptKc1HggXqIGqiTm4wRzcgXKi7R3s6KsNC7texQMH8HSBjO3XDE3uU9cqI9Sh-UzgFSr6Vql4zk2fCSjoy2SweeZ2adgAc6hEXkS4o293PgDthztXu5jw8W77j4u7Z1VTjD80sYkS80eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lESwUkauumHG2SkNkEb91og16cPOvOC6hN6wUXGIvCVsBqTiEYze7jL71at3iTQEvz9lfbkpxEfFJGJyweTX-15s8lUDRbw04LjjOYSH-hVsHhF-8jfYDyonkKOMLr-wKKqT6lcEui3S3-1URqysljn1Y_G70xjed6RYvoLDtmLvr3wR_mLnBajNgVh-fAKbVx7SXJZAXSixN_TgzIl6bdFCvZS6kqsmGzICKAX7lSHwcZ9lYVHeh8IU1IlnQWfOsfRe1yCWtu8nZyDrmgZXRfe8dYJPKU9jgENU6SJ6uq0cKE6X5rsBCCfRC8Hy9rh1rGwWvYMMyOYt4pUdJIVwoSBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=vX-onrmIX0xUg2AocwbRGIi9FqDAWpVtvoKnd0WOW44UsGxAFwP0ldc0oJ9EIm8rTEeNWIfCQHTGQy7vUrC9VU6tDD3ZvgRENv2Uq_xL2cn0a_JL_mk0hyxByqx7nRn-BmDszh2-fjYCIZi4WderOVtHhKP-NG_frGr5c97IQG5ayTEZi03DH8Trj7WOO3PbtC3Xh1kT9TTxrTVC6PL02uxksCr0dWUs-_Wg1cMt4aMYAIrSVLjt-qACpV8eAzMloTv07XHLb-wTGM3-4LUy2tVjKqguRbDLuYXprRV4kVAXCdAx5Z2gxT9lxqowEziqvK_Mhf3HNQvKY1IT7b5lESwUkauumHG2SkNkEb91og16cPOvOC6hN6wUXGIvCVsBqTiEYze7jL71at3iTQEvz9lfbkpxEfFJGJyweTX-15s8lUDRbw04LjjOYSH-hVsHhF-8jfYDyonkKOMLr-wKKqT6lcEui3S3-1URqysljn1Y_G70xjed6RYvoLDtmLvr3wR_mLnBajNgVh-fAKbVx7SXJZAXSixN_TgzIl6bdFCvZS6kqsmGzICKAX7lSHwcZ9lYVHeh8IU1IlnQWfOsfRe1yCWtu8nZyDrmgZXRfe8dYJPKU9jgENU6SJ6uq0cKE6X5rsBCCfRC8Hy9rh1rGwWvYMMyOYt4pUdJIVwoSBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spZNVrTJHOv-q0GWI2aKTMXDGMM-AUzkscwK4yexcJoxzfLbnvVv3WkbQbRT0YQxZ6UytkNdcsKO_DoEqO86Nd_FIZo8-VnyFRduR5h-_A_515sedpGKIdGoBIgw6Okx8yitKaoSCScPgFV0DT_GfTSnQ8cTOfeUF3Wg45U_l-EwLv7UJ5AoVmt2CtHeTHVX9ukAi_VqoqKYa531qhS5z3QPTdUyXvmxosQuLdYbjfqP1X8snSMKCFC0hqTmQJOr396rNDlZK7xN_OuFu4FT86lHIadXloDvIwbDPEQlylsjPkI7Gr4A_gfR0OrSPt5btkaUmq7htDmSIIfKGiKEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-rSyfpJBhMUrYoqkmEx5SsifxHCyGvlPGsBncnB94GYE-kvUUZKz3xvGX2S3KsfpGRhW0YweAqKszBjyt_A3b0Jwjk3m6BusdODLf2uNuFm21Dssq3JADPi87ZaHfLhjKg7BTh2TPgbQ9cSBy10PuJNV_GbNKbc1tXw8Vcy-LvYW8KJVAAoU2zLAx-VInaPA2m-I2gH1H0t0A_EV4Y7dzzSM3Xf6c5VzMO70PaPXPKa0irJoBWO8mbRhDPgDH4bAvjwhAgxOauzTMfZDrRZTYxW7gTVfFG7_eVmBe6UnLKFWd7Cs9K9IjyG2aIwnBlKIWHD-i1Y1l9mRFS3WoJYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDi3MHZn8gh1qIZTHQniPrIWM_oofSoEYTeb6Fn5furUvQHXuAugwtgPOtknhecessDkOiLOPMRBzwIpVDIHUMrguo3ECG6-p_B2iy0mNYxvI85k7D4aa6lhO9NinAjZspcg4hhnujMjaDDiUBW5SR6-_C7kwepnrktMZBbkEbS_uyMfzHmC2vCwezDe49CE8wbESzGtagZbcQhayAkLu-AGD5I36ieMgupvw8zSB3-6viSHg1Ht_FxJxuHPglH-V5HpNhV1T0EBg9jwx8d4YiGdSJyEn4J7wFNbF-XC2d1MulB9BVao0k-og_TICD7J7gZCA5lDrzMZMHRL004HAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=OjNCGgsL0aOHOEw2KRr3Jq7qyI6ADWAhtDSGlmZbHFs5wdlQeEw8xPXdtCQ7H2AVHscCL-Xf5gGEtt30sAXxdYOnz-obCajCCc1ViVTPw1O_OBg22mQ3lH-ajvSNjh-IOJzvptJWON1pLjPRixmP9pzEnR51bgG05T0d7ZKM2UNzs8qlNpZrzGYF6ywMI-mFB2Kcf4_UiPoqT21cf9emEPjYoeExtKG7V2EZVUV5q4XcPzJUpfttXJVmAluu2bG8duCMp8oaEFcKcynrvirckIqyTWcfUgKZhY37bcFqapg6yzHXofYat3-_dCtSny_iy-D3B5svzSEx4o5Z6dZENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=OjNCGgsL0aOHOEw2KRr3Jq7qyI6ADWAhtDSGlmZbHFs5wdlQeEw8xPXdtCQ7H2AVHscCL-Xf5gGEtt30sAXxdYOnz-obCajCCc1ViVTPw1O_OBg22mQ3lH-ajvSNjh-IOJzvptJWON1pLjPRixmP9pzEnR51bgG05T0d7ZKM2UNzs8qlNpZrzGYF6ywMI-mFB2Kcf4_UiPoqT21cf9emEPjYoeExtKG7V2EZVUV5q4XcPzJUpfttXJVmAluu2bG8duCMp8oaEFcKcynrvirckIqyTWcfUgKZhY37bcFqapg6yzHXofYat3-_dCtSny_iy-D3B5svzSEx4o5Z6dZENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
