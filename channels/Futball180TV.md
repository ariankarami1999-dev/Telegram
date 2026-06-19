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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 673K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-94415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=MxOgnG9Gg8CoCL6Sd7qC0PEutCHKo2Dx7382Xm_1JBghkggXQe097iyNXCRsVS19U7s__-J5pzaslAVpgg87eriN_y4Jp-z4-fYbRRj7L6QjVPyuQNkX7xL6SsnV09yaIeCSPDTbUjLvuT8raW14ucTHEev65xhnn5c1OqbnqGnjNfRjw-yXQPPxIB-CGEWuzhl6m0lJJtpaf26djvQPOPJ5D0DsJ3Yru5B2_fnzTvdYF7NajoPdo3Cug0i3Sg0puvtRFbmVX99VIP67595f1N87cnL9p1OPt-NM314cMuyM5_9Eq6u10iF_DZnWKA_gr4suvAN3-IdKrHXn1gPpQVs77DRewxOV3KITXwQYzWEi1fXCKaqYeAM9pt7PjqceXB9qOhMHn7gySln2ZIMB82nOEeZSCJi3gJn8pZ8E1THpxNBvofOKD-hEiAZYRNx1TMB8_HQ_FmevVK2gz8gwoTCNYhpiH8nLVxCDm9X2taZv3sVQs0uw1doIBtgBL__vffC9PIPnUf3bCnereffvVCdgwnTNBJfnKcKWmG4YmAkMrtVQX8DeX46VOkKTNBUIBj_CCjqgKdoYsDP9PQB7IU0XF4nKSj6NiOQ1DvjuUo55yMPZ2amRmY-0l8Q5zcllfqYFORbvVP9GUE3ltFUlaUmgWf0bdaLR5evRmyUg94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=MxOgnG9Gg8CoCL6Sd7qC0PEutCHKo2Dx7382Xm_1JBghkggXQe097iyNXCRsVS19U7s__-J5pzaslAVpgg87eriN_y4Jp-z4-fYbRRj7L6QjVPyuQNkX7xL6SsnV09yaIeCSPDTbUjLvuT8raW14ucTHEev65xhnn5c1OqbnqGnjNfRjw-yXQPPxIB-CGEWuzhl6m0lJJtpaf26djvQPOPJ5D0DsJ3Yru5B2_fnzTvdYF7NajoPdo3Cug0i3Sg0puvtRFbmVX99VIP67595f1N87cnL9p1OPt-NM314cMuyM5_9Eq6u10iF_DZnWKA_gr4suvAN3-IdKrHXn1gPpQVs77DRewxOV3KITXwQYzWEi1fXCKaqYeAM9pt7PjqceXB9qOhMHn7gySln2ZIMB82nOEeZSCJi3gJn8pZ8E1THpxNBvofOKD-hEiAZYRNx1TMB8_HQ_FmevVK2gz8gwoTCNYhpiH8nLVxCDm9X2taZv3sVQs0uw1doIBtgBL__vffC9PIPnUf3bCnereffvVCdgwnTNBJfnKcKWmG4YmAkMrtVQX8DeX46VOkKTNBUIBj_CCjqgKdoYsDP9PQB7IU0XF4nKSj6NiOQ1DvjuUo55yMPZ2amRmY-0l8Q5zcllfqYFORbvVP9GUE3ltFUlaUmgWf0bdaLR5evRmyUg94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه حنیف عمران‌زاده از کتک خوردن مقابل بی‌آزار تهرانی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/94415" target="_blank">📅 13:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElvdNpoh_FKeV5Hq1E8jXt3QXFeiI6P2eLMFm06tTxhfwtgmZ68YBbcc4V56GCmCeXIBEai_nyh9UY0kONtIyyOWiWCmymqQbsu6S2segRKccEBXv3_6XKFSuB-DIyd3Avmf2sUJkVx54BFFBSru19zytTJCLN_6Ujbl1aTR3FQjCot3L0N65Lk3PLXO6DQdvIJOKQvMAiUICyvV3EEKCJe8jy484HtWLFgk_xdLVJeMNSqidTxOZ02ZclS00ePCNxv4elR3jo34qSgPoK2zWZi-a0Ky5NKjzN4t7qlzz1TpnqKckviSxP3PLNvfn8hQXAQZUyENlNlvRCPX0-GPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سانسورچی از دستش در رفته یا اثرات توافقه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/94414" target="_blank">📅 13:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwuyLfMLY9vLsKEEzpvw8VSE_0m2e1DQFOfXHAJdicT__Fa2dMdacAcQ8pA34kMyB_fMbPbjpbDgVpAu2DQM4mV85igE39YL7yDN1Hcj3esPaBfbe0-0mrObwgxfls_KHiptaWj7JujViErBp2ICQmisVdDusLkydTqHNc8_v0fQ8Xvel99eOzQzzwhvUu5uxtKzPnnVeFyrQYyqFpvPGQOvJgD2JjoHRB_FspZjDEZ-53D_22TNUh3ihQyuiWAhsJPNo_flMrx5yVvTPc-yBWKsq_kVAleQEjNCEXEdfiduzFCpVpuTC5OeXq81fKpMrWXbU8CV8lnct-99WRyykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/94413" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=BuTLdleEZE3uZjNQJz-nMsUwS22dfT0AtPMif6AOrKtakYlhOtrvaiglzJMQX_HP9fH6bGRFoM7mc0D7o7D24mvKgCPbUNZ3WsPqWfaRN-SOsGjEIMr_kD1Pb7yjgbMyLw4eCrLuOTcABGAYGx0tkQysOX0zomkvHTnn9hn7XwA-jDS0oWHK-ZgE7TczNKprIVCxYFdJ9Ta6TLPtLbQ5OChOVvGMR5I2v59cO6oC3Itz5IUHORZK1qdQjlWCRgi2VgjSPk9jOXPyMSFrL0q1F6_KMBrjHk84JSepBLlhDGsJ8Kd4l6byhwMMFELXDRC2ee4ez0l3S0yAdQQkNymSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=BuTLdleEZE3uZjNQJz-nMsUwS22dfT0AtPMif6AOrKtakYlhOtrvaiglzJMQX_HP9fH6bGRFoM7mc0D7o7D24mvKgCPbUNZ3WsPqWfaRN-SOsGjEIMr_kD1Pb7yjgbMyLw4eCrLuOTcABGAYGx0tkQysOX0zomkvHTnn9hn7XwA-jDS0oWHK-ZgE7TczNKprIVCxYFdJ9Ta6TLPtLbQ5OChOVvGMR5I2v59cO6oC3Itz5IUHORZK1qdQjlWCRgi2VgjSPk9jOXPyMSFrL0q1F6_KMBrjHk84JSepBLlhDGsJ8Kd4l6byhwMMFELXDRC2ee4ez0l3S0yAdQQkNymSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیک نشون داد واقعا شایسته میزبانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/94412" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=XxuiNcj564onp7TpFIAGBs2H6ECBv0mRw0d_8t9Epq141Veb-kWzob02-q6A2TITlMQqYr4HD_a5VSUlKJSviQqBpJ-myL7HmmOyfyMwn0F1usTwRaqNMVZgV4HS4D3inujXhh3uK035Oaz8K4oWTtqGCIMS-8cl9YsaYrDbL2P2bQLFJ5cfpwCCuOACqglFmfMhNHNQrXGLk0TPUE4vsICBlAriEHgCyMyAeb8PL5LYDieevx9hEh0az0iTVgg8J838Fu9i12o0ky6-G7gVZ-8eB8aLWyOATgRjA3oa8b8ZBhNCyDBxtf_GQpYa4kxU4igx8VIu2ODhIjua-mpnUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=XxuiNcj564onp7TpFIAGBs2H6ECBv0mRw0d_8t9Epq141Veb-kWzob02-q6A2TITlMQqYr4HD_a5VSUlKJSviQqBpJ-myL7HmmOyfyMwn0F1usTwRaqNMVZgV4HS4D3inujXhh3uK035Oaz8K4oWTtqGCIMS-8cl9YsaYrDbL2P2bQLFJ5cfpwCCuOACqglFmfMhNHNQrXGLk0TPUE4vsICBlAriEHgCyMyAeb8PL5LYDieevx9hEh0az0iTVgg8J838Fu9i12o0ky6-G7gVZ-8eB8aLWyOATgRjA3oa8b8ZBhNCyDBxtf_GQpYa4kxU4igx8VIu2ODhIjua-mpnUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی بعد از اینکه در مقابل الجزایر تعویض شد، روی نیمکت جایی نبود، بنابراین تیاگو آلمادا جای خود را به مسی پیشنهاد داد.
مسی قبول نکرد و روی زمین نشست.
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/94411" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04815885a.mp4?token=QisFKzIMEAWfa-6S7imxPs0qxl6CyZpNLVTHQiDa-sktyY4jfHCIX7dy2KphQ2gIUS_7Xbli6Iu9FajkF5I7nwFjUlhTMvVjIfoIIRouublZXBGXHKNpfrO7lW7UUR2SR7utAXLfsKTl0qc2djQt9Gq3Dt_2e1iDEag53RnUju5hL-PAhsF4bphYM4dOtVAtV_vc50d66SaBqpBuRCHMfbFSTndIWvBgMqrihefvCtDkaQSr898sbmfmeV_j7X0K4fQ1eTFjo5w5w5U9CO00hm0IpDB7upoZU_o77FeraxKtlvJ4WsMseBl0kZzTX4cGr9WuHrWhWHmo2EGJxqxy7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04815885a.mp4?token=QisFKzIMEAWfa-6S7imxPs0qxl6CyZpNLVTHQiDa-sktyY4jfHCIX7dy2KphQ2gIUS_7Xbli6Iu9FajkF5I7nwFjUlhTMvVjIfoIIRouublZXBGXHKNpfrO7lW7UUR2SR7utAXLfsKTl0qc2djQt9Gq3Dt_2e1iDEag53RnUju5hL-PAhsF4bphYM4dOtVAtV_vc50d66SaBqpBuRCHMfbFSTndIWvBgMqrihefvCtDkaQSr898sbmfmeV_j7X0K4fQ1eTFjo5w5w5U9CO00hm0IpDB7upoZU_o77FeraxKtlvJ4WsMseBl0kZzTX4cGr9WuHrWhWHmo2EGJxqxy7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
مامانا اینقدر سر به سر بچه‌ها نذارید :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/94410" target="_blank">📅 13:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=THjzw3mDreze6gMM119EePKSxNtbpKTNYLLys0tKS9B2U9p2XoMvvSbY5sIKMuUZd1dMLD2GPzwZt4I4hSqODfOQ_grLeigotz7AOUBfBY9MpjF44bA8_aNfCt5vIghJ_ntAlTngBxdvVsUvON3TumgtBlm6o8kp_eY_LO05IdHA2PL0WNARoGnG-rlyi08vqzqxADL8kkfUcyvEMhUCXWDG1Es_Y3_HxpbtgLyJSF6KNhOPgARVbdMabvXWCe6q_SZuZFkYdv3YGMAyGQV2aOEfoGJxrZau-eH_wa_etFxrzQ0Y9lNZ-Pt12pPGiskcFRbqHRuPf5hqwl8A_U0Z_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=THjzw3mDreze6gMM119EePKSxNtbpKTNYLLys0tKS9B2U9p2XoMvvSbY5sIKMuUZd1dMLD2GPzwZt4I4hSqODfOQ_grLeigotz7AOUBfBY9MpjF44bA8_aNfCt5vIghJ_ntAlTngBxdvVsUvON3TumgtBlm6o8kp_eY_LO05IdHA2PL0WNARoGnG-rlyi08vqzqxADL8kkfUcyvEMhUCXWDG1Es_Y3_HxpbtgLyJSF6KNhOPgARVbdMabvXWCe6q_SZuZFkYdv3YGMAyGQV2aOEfoGJxrZau-eH_wa_etFxrzQ0Y9lNZ-Pt12pPGiskcFRbqHRuPf5hqwl8A_U0Z_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94408" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6a57InE7fOUZ8DtKDdOI_BUFkKevip9aWJERDUH7iZIFgzATTw7JsqMXHJSWYvNgWElS1zHylP-Q_ypt0kd_BIAliOKFe9VzilnY21_21hexCDdLV5CE9mPzKZ_Mr-xDyxaU8RkSIWsttlft0VMOWhszzMZE7l-iWM3wrZWnR1lY1MPN2qewmBbHxZO2Om5U4mcW716XBZhi6zVsY5OsWnewt6kgxl95yy2JNI1_t0YaA29g5JEYCQ6vDqVVgRaacLuXkCssF5wxHwW5oxZwEFS8PiFbEOO3oCvXZLKjlrL2KmpPTt4f-mw3BFF5qPFP_20NRj11Pvy0eVMUv7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات ۲۰ تیم حاضر در پریمیرلیگ انگلیس فصل ۲۰۲۶/۲۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94407" target="_blank">📅 12:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=L8X_ooGEpT3IuAAi0yicZ6oxJccSb6tWi7cn0VvtMlIVW_df9OZQsvtu9pDoM8WK5x4LAjPcQPbspbfdJjrQm64Ha8a-i_0DrHE6gGOykSkp2yrgcmEcUdXLQUF0PGqg16T7m4RAWK5qMgAM4ROFHGntVC3KRzol7fE3nT52RNLU-5U80HCZBDZaIHen3lBdKj_cF8V2osxmIj5AQJwuy4g1m-miCZrlUhhwLWQNFnuccbNCGwQHg0VYafKtOkjkJOd_h_Yez-LSRVhyid1_1Xk-sFieDtGp8lWF7il9ETL7rzOWjtHjBkhih4jdWmPtTS5-x9jrYZEGjZPLFQKGAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=L8X_ooGEpT3IuAAi0yicZ6oxJccSb6tWi7cn0VvtMlIVW_df9OZQsvtu9pDoM8WK5x4LAjPcQPbspbfdJjrQm64Ha8a-i_0DrHE6gGOykSkp2yrgcmEcUdXLQUF0PGqg16T7m4RAWK5qMgAM4ROFHGntVC3KRzol7fE3nT52RNLU-5U80HCZBDZaIHen3lBdKj_cF8V2osxmIj5AQJwuy4g1m-miCZrlUhhwLWQNFnuccbNCGwQHg0VYafKtOkjkJOd_h_Yez-LSRVhyid1_1Xk-sFieDtGp8lWF7il9ETL7rzOWjtHjBkhih4jdWmPtTS5-x9jrYZEGjZPLFQKGAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94406" target="_blank">📅 12:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=dRd-t31w4GUIhs22fiSZo87iQS9RyZd9ydyjgf4MyWSuHQpfTuJv-NcMeOdTrvVkKQ8LYhd10nM3jKfGBeH8gkfRLTlj5_al20Quo_7UuIiwkkJuidmzbHQKGVpiJZTmdi8MOrtT1y6_r5gpQf7qqLghW78fV0kKc-dMa5N3ge5iujxIWMI32vLmE_c9sUIc_DJEtDkv-0IscHR-D65fOuhz7EjbqqyR3V_Hh_mtEVpSuzCRWzEHeH83peCdcKtJQVJewpS15OyX-_GYdWbSAKLa5yzs2dltAMf3vIc7xLN8e5qzOpbHD7MQZSsWubQyLxRqKtWF3mVkSspxnc960w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=dRd-t31w4GUIhs22fiSZo87iQS9RyZd9ydyjgf4MyWSuHQpfTuJv-NcMeOdTrvVkKQ8LYhd10nM3jKfGBeH8gkfRLTlj5_al20Quo_7UuIiwkkJuidmzbHQKGVpiJZTmdi8MOrtT1y6_r5gpQf7qqLghW78fV0kKc-dMa5N3ge5iujxIWMI32vLmE_c9sUIc_DJEtDkv-0IscHR-D65fOuhz7EjbqqyR3V_Hh_mtEVpSuzCRWzEHeH83peCdcKtJQVJewpS15OyX-_GYdWbSAKLa5yzs2dltAMf3vIc7xLN8e5qzOpbHD7MQZSsWubQyLxRqKtWF3mVkSspxnc960w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇲🇽
درک نمیکنم چرا خانومای مکزیکی موقع شادی گل ممه‌هاشون میندازن بیرون.‌ نمونش همین بازی دیشب با کره‌جنوبی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94405" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYMVxKe1YeFqZkRHswtNiwkmPBgbbWwDKntmcbua3KOBTG8b2yztQYkc7Xj17MN7RJngc_yWCcZPTsPtBebWS2fFDZSelw_PfBehVNkssagqfmy-9t0xAiAH81RcffFMJuI_9l2DmuKN5fkA9GfhQUdyXJfujdRcHxzwXthCMQNwi6Wv9_XucnV-a0S1Dlp9mlEOSzOCpJKT3mfRcfjPIAFSsWRgdcEtqM9eZMhLVdjKrtWADW6GX2Gq-pcC6Vgv85txroRUYZTauMgSNpH2rXMreNwzfQadvBtWIdYW-pWbNAXxWzQdJNTUb--fahpvw7f0EQNcw0lSK4-6GfSfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSZOt_O22PIRwsnX6a0GYsPM073dzLvw3PqhBvhvZDbI5oQ1Rs3TFgkx_nbPNoFSZ2-jEQsSOTsPoQ-cMr1VdoA-3EWcKfYtj3Tq7e0t7mouWyyqST0aTvBNQWhG559TlnqY46s7t-9uR1Wk6g7qooWk9ocwEQDh3ana3fU0TQZ-NiIIYByphRbdkQCH4zTvrO0Mfgskoscb4PCNbRA-UI_nmPcBHUkwmUrho_e77xjCIeHipsWAYk7XEd8mPaV0oshm-hfhwYj6HXusZiLE2FNG95qcmxt2Grwg60BOV7hgVLJGcTQk84rkXo5h4n06N-LB6w_tApu002u8W4pjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSk4c_94T8IeRtLvJTBgF1LZA7ISZbKKw50lRiDrF5_81mYkaSFJ7B1KqRUcg58oCHlww5kXaDbeYz7Yq-EJoIaDzF1ZcSBIAimXwfrF0_hMbIlwbdoGHBKXtC-xDm4VKrMDHo0MQ9dakbTH8jMbDnvUsPdi75bdEssK8rzaknxTNf0Gumr-ogORNlKhUdFKcm78cmUL9moYV8_3fXGjZJ8uBsitb7HqqQdB66pShbsIfY5QfhohDRU6tvTdx65iLqCNUi36s8GXegiBlsrbqQq_e9VOF6MGf6P6Z3OVgUiZMhjcu2loNC-gnwH0K3qJknNxlMMV4RbvSQDfXFz7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb7-zawFBnH2kcg-c6xxVbJtfkUEt2pOyvKbjsUfB1rquegDyn0k84392loL2ij85jqAYg77KZEFkmfreWnmXp2WX3n5zeVMtUx0cQOnAsXaa9gENvNNBgRumz-sZHDzEpPpas05AAMZHSq4Md8JwQawwPrk58nh1mkSOBjNW58aecwiIH4DavZqiJ6cXP6jN0-rl13JrYd1ETn41ALjVNZMPc2Paeyz3ZouN-IYYrB5vkSAc9NYbd9tRo8MhDXT5erEf-Y_USfn6fCw63LQD3D1XpbPui11WOjRy5uvyJE4PSx9ucmW215UMY7FD9JaGHIclftJoUpeZcy1Z2J7rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94401" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpxQwIciqjjabzz4_B5oDxY_Dl7EGOXonS-vn-WYOjLUp5CVohLrDCHB_TAgmCb3qePZ7lNKHpMteYyXFJcMY7eHfkGVQ4sdj1-CWDsgZyloNsV_xfRkAQVqEM5BCOrBk4vGCI0HaPce_5sHhdDBmnfSwduCSZDDt-rSY6wCgeb-MebnRIuI-3ZMnNPfUF8VDJnsYgAPUg96izdKtfmmjQKBkB258z51diDDvi_Kn9bqYGS8n5BLs6DOWleDwJ08dzyL2QCpr5iUjs-wPi_2QPgdwCFHVV17pPkdijTbfVkGJ_aoI7EF21PsLYaxgK8rOwdLOpyTd-pO78BJiiorSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94400" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AwKnkQuh5djKr90PHBd1Tbzdq0gomm4VkAVi1qmv7bUekOnw4XXIrASpezYpcklDZ4TOdlRsf4obmwNDPhka_xBnf5a9UOxM0tTZ9TszHsHkK6M8JkAQPmSCummrNR4sqzGN9u_NQEgdaworZTla_AbTN6raMMPfnAguoklFKuA0ekLmObrrhquNF-XcJwu-sqh59RQwcJBdzKUVF0RmDwW6WQFM1QQNmyDsLYhsTVLFRHrxXSTb6GtY6GQjxYa-3J0Bz4DMfsex8iOZv8JBneSY23V-pi-Js9a5wgSMB6_6KhPZdrjbqmaW0394sMxOfzNnjMbz8C16jsL6xHIXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MqhgbHJzTZIzvQaJr9WEK83fscuk4eJ9OpGDJGc8kUC_5bS1y1ZRyI_s3dJXEwXfFEDaa1wv7EOcQsXw3c4t87Aw6f0J00RsSz4wOvhO7vplffLmQqUDP6bmi2hk6mRuw88KZ34sEm7k5lpUvQnhy_KA6CwSKMKoNMTmyJDU6Y1SezMAC3YNgMk8Vz2povGxvIEp0eVW2Jt7AZMNMNxsb94PhWtLv59INp2OtrYAwGOWWoxOgyLRC_x8eeW37stWHZxANvAVttf29t2Zx-_ORfaTnHvVX2bysdUZCdc8ANOTUSJhlZulzZx5PMb-7uNz0Vtw7mSlBML5BD47y_Ejtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJjBzkjaullQK8V_p6ANY6KqO0-Se_SGDc5i0HUCrgNzbhS7m1A5MwvCeU60SKObcn1XPOSexubZsqgznvwlokFMR-KDo57eFtN0jwwyxuGiJOJuqnqNmJ1etkZ-2Bk2FX20izRM9ldakruFxEwH8goNGsYsZGTewPTcnSfsrCdd886J66dhYUDvMHjxlt04SAVgRjrhB-jTowAtree_9KSt6DOPES-FvZjwnnpYU2G7ODk8UyVGyvlaxpmYDHwlkNTkcDaDt6tzuKQWDWtqrOWIkMSEcrN01sO1gHIqDPKKQjekc64NrwJSCSsBz46kt9RtudaLRoXcNddMKq-DbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
🇺🇸
پولشیچ ستاره آمریکا: برای شادی تک‌تک مردم خصوصا هواداران عزیزمون امشب باید استرالیا رو ببریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94397" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=q57eAOAOEN_LMAj1XjGO22LNewtAvgR7_Mr7-7BX1UyIbfSw1gqDNbO3xhhXdZVMRLQcak6jWOyeTydTXv-ZkABi1yoaffkeKgF3hPIsKY0ADmu4NK4tQuMQK_hiN_qAN-xdigK0G3e8SHX8VGXie3k2yTOZr4lNPrYFGgJlock7vfbIXOilo1LBlotMaRvEs7mE0L7oRq3LyiNjGmmd0rAMjTZYFwyLoqZ0IaJQeZHfF1JNIcEli6Lbq3y7B0KxXAlyn6j3y6E9s8fGF34WKZGXEMcwVUqjsEJpkNQG6qD2fm5HSLtLLXC55MxinK__T12PV5TD_XiIATy2q0ucsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=q57eAOAOEN_LMAj1XjGO22LNewtAvgR7_Mr7-7BX1UyIbfSw1gqDNbO3xhhXdZVMRLQcak6jWOyeTydTXv-ZkABi1yoaffkeKgF3hPIsKY0ADmu4NK4tQuMQK_hiN_qAN-xdigK0G3e8SHX8VGXie3k2yTOZr4lNPrYFGgJlock7vfbIXOilo1LBlotMaRvEs7mE0L7oRq3LyiNjGmmd0rAMjTZYFwyLoqZ0IaJQeZHfF1JNIcEli6Lbq3y7B0KxXAlyn6j3y6E9s8fGF34WKZGXEMcwVUqjsEJpkNQG6qD2fm5HSLtLLXC55MxinK__T12PV5TD_XiIATy2q0ucsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تعجب و ترس عادل فردوسی‌پور از تعداد سگ های مازیار: میگه ده تا سگ ژرمن دارم
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94396" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7Nmh0LQYeXK57bat8Zi8sbqKsuoFr-OF6k65oI2kGekAdSY9xgH3Qh3e08D4lb8yPXrBMjcMGcq-U5uo0R2Ztr5BlUdRt7hr9M2FZA_KLGN32UvnqzpTRaEApsyAl963I9UazFh-49UlZguyj2vo5aK3A2-nkAu1AWFIdsEfrNk70dr-hfJ1cfsd3w8msboDinTqoB0WcP9GDGm-r1yGM_AECU6tkGBsot9hr5jCjwEtZuCuORSXt2UcD6NxqKL_CrWDbNUvIfUIQfvX71dlF_vgsZ_QxVDtBjzPEvS4RtgJx0PtBKT5Z47iFue0Tznfkuzxm2d302sCSv9OZTxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
برنامه مسابقات هفته‌اول پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94395" target="_blank">📅 12:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QARw0YyfuSuuDrD2Etno73UToHF2htlegOZLcA-fLS_lqrm-5dJlyzN5gmahFcsyH9KVZi_JcysC4kJlABTt2qDeX0TajAYcc1sgsqoTQvmsb7VnXIVo56JVdUEGthu-vlg7E7EJ1npK_jdDXFN1GETeUywPkC1AkRbooeVGw0xXefWyWJfl6cUZ-HvR68FlEsT_IGtc5Hu56ZKjSN3hNTqV0laE83tjwv-pNl_5gNlEzlxeCi-rSCc9MnCohPVsA-sq3npb6CX9WOUfNRr2s3k0pyMZLYSYNKWg1pPMyFxnRSMGaQYIC1GHptZJTtDCigaKslzfFXZOzkDhuRXHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94394" target="_blank">📅 12:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94393">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=LDGC94vWIhAV5DH5mtLYFhXWp3FEHKmXz0G9W7g_GVdzYXrgR9pmetWblBLrMzxsWfjWiZpb0tZiKcryx-h4CXou3Gi55zvCMXmwX-7h_9_Jl3zJdMFj0jkhEF0C1I9d0unuPGZZinQiV9AVC_uW8a5JlnclmMEil2AXZf523gvhlWCtcrD5B6XPXclRf3hzqG9Yjj533vgc5qvwsj-sBV_2s3r7JXXGkMa-tLjyI8DJ4qew52cDwJaQ9_BrabazwArnCXaqd9oRVKpukR7vTCzuEXxveEVxVKdR650krJBEvXkJCN8BzC_LcLnOjG1AD73sH2X09mBpqIu0RaaMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=LDGC94vWIhAV5DH5mtLYFhXWp3FEHKmXz0G9W7g_GVdzYXrgR9pmetWblBLrMzxsWfjWiZpb0tZiKcryx-h4CXou3Gi55zvCMXmwX-7h_9_Jl3zJdMFj0jkhEF0C1I9d0unuPGZZinQiV9AVC_uW8a5JlnclmMEil2AXZf523gvhlWCtcrD5B6XPXclRf3hzqG9Yjj533vgc5qvwsj-sBV_2s3r7JXXGkMa-tLjyI8DJ4qew52cDwJaQ9_BrabazwArnCXaqd9oRVKpukR7vTCzuEXxveEVxVKdR650krJBEvXkJCN8BzC_LcLnOjG1AD73sH2X09mBpqIu0RaaMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
روایت ابوطالب از ماجرای پیرزن و رونالدو؛ دیدی حتی یک پیرزن هم نیومد ببینه چه رقم آدمی هستی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94393" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94392">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=qDFc9q46Rd91h2gY9Kl7Oo8LAxF8LsxQgua7lm4GFRt1IqL1z9YUpuIPyGxWSQpVimWxDJyTWDA9mUwMDPQLL55Z2PZdHRZ6iwAFrlJMgs9YGkys9oIuVq-kFxep-mBS2rON2Sopg3n6BrfKY0pMq8NQrwKdyqz_B8BYf8TLhSc4iP9bHazwUCTogU-Z9jf5FAS8yhnr2jfH8108th1V16q1ElZ97GeqquKxYRuAVXhK8MHUivwGLAPriZjnmbUsNrERSAmdtSu_K-ReUHZQj8GbmQ7etz3yU6WVWSWAE7fUyZoEmLutNVkqcKd68ZpQ7afr8Nsw4Pf7VTfpP_ytBEXHnb1yR3Dk5ZuUjvuGSXtbZ7TlIRk9YxkdBTwtYzPdlrC2CPHiumD2GPgI8ZQatVKOJUwRGArCMN07kyBeXMMkVGrWx1FwDiiwC99kzIeKEYxtmKxLoJ6_cnjM1iYJSJRk9KANOSwoCVU8tXhfQ70rkwRu6Q6LBxpXWpe0UDEdKiqxa-204W81qCjCZJNmN2HOdbQiFIFJl1OSpveMoC8ySQR41svLTj2Z8lS-SVOv27iqQScOy38wYI5m1iTUUrOY5T66kcUUNqvSxhTY9JRSH4Cb2YxfREUqzfvYg1r8apqoC55Up6-nkp64vT46gzwXBPpVV_uf5hODOKs2P7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=qDFc9q46Rd91h2gY9Kl7Oo8LAxF8LsxQgua7lm4GFRt1IqL1z9YUpuIPyGxWSQpVimWxDJyTWDA9mUwMDPQLL55Z2PZdHRZ6iwAFrlJMgs9YGkys9oIuVq-kFxep-mBS2rON2Sopg3n6BrfKY0pMq8NQrwKdyqz_B8BYf8TLhSc4iP9bHazwUCTogU-Z9jf5FAS8yhnr2jfH8108th1V16q1ElZ97GeqquKxYRuAVXhK8MHUivwGLAPriZjnmbUsNrERSAmdtSu_K-ReUHZQj8GbmQ7etz3yU6WVWSWAE7fUyZoEmLutNVkqcKd68ZpQ7afr8Nsw4Pf7VTfpP_ytBEXHnb1yR3Dk5ZuUjvuGSXtbZ7TlIRk9YxkdBTwtYzPdlrC2CPHiumD2GPgI8ZQatVKOJUwRGArCMN07kyBeXMMkVGrWx1FwDiiwC99kzIeKEYxtmKxLoJ6_cnjM1iYJSJRk9KANOSwoCVU8tXhfQ70rkwRu6Q6LBxpXWpe0UDEdKiqxa-204W81qCjCZJNmN2HOdbQiFIFJl1OSpveMoC8ySQR41svLTj2Z8lS-SVOv27iqQScOy38wYI5m1iTUUrOY5T66kcUUNqvSxhTY9JRSH4Cb2YxfREUqzfvYg1r8apqoC55Up6-nkp64vT46gzwXBPpVV_uf5hODOKs2P7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
جوونای آفریقایی برای تیم قلعه‌نویی چالش رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94392" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94391">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=nRKrzZz5L2JsBkTti489s9Qw2P2N7-HRgWYboruMMbC2t5cVD3ChMwEm7k-LpFLqK1OWc_IFi-Mzw1LygHDuwLm2w_8G7mfJsO3LAJmec4vkAI-ibu9rQaZyW2wvEPUFuDSAeGlLLnRyf04wW6wKKAFSQOkJsB5148Du5DTno1XMWJr3b9gMxagtGFowukF0cs6yI9dn4PNmQdX8QGFmzZjGDa7jnG2XFEXLC3fDpAN7YOAAk3nEHegwbViPn3iVBnNTOpjzXGDm6QMPfyNYUjHEPp1TB-ETYwksY_1aZpb2wFnZKuW7VPEazv7p5YcA-MT0BCNwiPY1APgFN9U_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=nRKrzZz5L2JsBkTti489s9Qw2P2N7-HRgWYboruMMbC2t5cVD3ChMwEm7k-LpFLqK1OWc_IFi-Mzw1LygHDuwLm2w_8G7mfJsO3LAJmec4vkAI-ibu9rQaZyW2wvEPUFuDSAeGlLLnRyf04wW6wKKAFSQOkJsB5148Du5DTno1XMWJr3b9gMxagtGFowukF0cs6yI9dn4PNmQdX8QGFmzZjGDa7jnG2XFEXLC3fDpAN7YOAAk3nEHegwbViPn3iVBnNTOpjzXGDm6QMPfyNYUjHEPp1TB-ETYwksY_1aZpb2wFnZKuW7VPEazv7p5YcA-MT0BCNwiPY1APgFN9U_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94391" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94390">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول لیورپول:  • نیوکاسل یونایتد × لیورپول • لیورپول × ناتینگهام فارست • ایپسویچ تاون × لیورپول • لیورپول × فولهام • بورنموث × لیورپول • لیورپول × منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/94390" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94389">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۰ بازی اول منچستر یونایتد در لیگ برتر انگلستان فصل ۲۰۲۶/۲۷:  هال سیتی مقابل منچستر یونایتد منچستر یونایتد مقابل ایپسویچ تاون اورتون مقابل منچستر یونایتد منچستر یونایتد مقابل منچستر سیتی فولهام مقابل منچستر یونایتد منچستر یونایتد مقابل تاتنهام…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/94389" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94388">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:  • کاونتری سیتی × آرسنال • آستون ویلا × آرسنال • آرسنال × چلسی • سندرلند × آرسنال • برایتون × آرسنال • آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94388" target="_blank">📅 11:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94387">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:
• کاونتری سیتی × آرسنال
• آستون ویلا × آرسنال
• آرسنال × چلسی
• سندرلند × آرسنال
• برایتون × آرسنال
• آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94387" target="_blank">📅 11:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94386">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=fxHGlT33wml-iUetIarSB2_2Ukn2L77D5b9GQ6coe0C7n3DzB5EFnSc0n05mcHyN2qBd6W59Z1KJsjEFZ_XSaGLaL8bK3hCc-nz3ITS_bmJuTAyfCex2eqqyYfnDcsHTLzJgyqhBwZdz8Y9nT8QF4S6vX04SefIXQm9rMoK3Pt3rbYBFEaHN67VlNvFjikdApf4z6KFwVILPtkFajnASrWGAfDp0ubt3WY03oCSkd3G0OfqZyeLwvOSYfP1dLoblsaTXk4yrkx74qdSDmDSNJxgmAFpYDuh-L4s-AgOFhArkHemv67BB3gENVKtkpEQXhU5xM72WrOzc4r7Ko9Qzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=fxHGlT33wml-iUetIarSB2_2Ukn2L77D5b9GQ6coe0C7n3DzB5EFnSc0n05mcHyN2qBd6W59Z1KJsjEFZ_XSaGLaL8bK3hCc-nz3ITS_bmJuTAyfCex2eqqyYfnDcsHTLzJgyqhBwZdz8Y9nT8QF4S6vX04SefIXQm9rMoK3Pt3rbYBFEaHN67VlNvFjikdApf4z6KFwVILPtkFajnASrWGAfDp0ubt3WY03oCSkd3G0OfqZyeLwvOSYfP1dLoblsaTXk4yrkx74qdSDmDSNJxgmAFpYDuh-L4s-AgOFhArkHemv67BB3gENVKtkpEQXhU5xM72WrOzc4r7Ko9Qzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
هوادار ایرانی حاضر در بازی مقابل نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/94386" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94385">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-6dC_Wrk46LECRiM-VKcGVXuH5DYnrYzSXpcDG8SLx7ED1Mad_XVPdvB5PJ-tfpwRz_Ezh5BiEOerFQvXTODMX9L9Nw01Nouo95j6xvuIo--HUkIsft3txIwtOnlMcroRXLgTosXRUf-vSzonbxv3S6GlJSDGEKA-XtzGSP4PVV5b5sA-8Bbw5bB3icbKUsXotabG-lZqzLcfuh-tez4oDr2ROvQOkPvQlzLZCzm6dLQ90Lc9Cm1H3mn3zXhqEl9DoHjIFt35SQ5fOW5PZ1B98LnKsHgByyYN4XlEhzUZAxXKnP7VJCbansw9Z97wbgPEzuo8rqe-UqbcN_gmIANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد بازیکنای رئال تو هفته اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94385" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94384">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrETddE8BHX9U1cs4gAxQ88P3Xia1PQACAnQ74KtUY4LfTpQf2bzQBafZP11YoN3scIKtsirPn7XBTOCHk518oBPbTa9PS99-x_6fI1XpYQxkg448GpoafHOZQo4NPFvJqyqX_Lwj9-m3SMTmD5XUa-dZcQtS-zIE84gdHxiyDJ1L8xZ0HVwJ1oO5hZM7wVJNmdoC8TEMe898rONwEgiG9WTZ_u4yHCRiAvBxDVEccC4FXAiQpQxIIc4baL1ay6K9JSfvyHD5dHozFi71m8Vw-ZYSoQlvdR9novhft_x0qdZdk0B1j-5KYfbuKrMC09NAwG_0a3Bw_4L8eiI8GzRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز ایرانی دست به کار شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94384" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94383">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INX8eVCZrCyKEfxHWcbQkGmAQh4jRY8d59_He4CyNoaRQ6Ez1PnKzXaKESXYLpJAdV9uDCrfnxVgowL7txgrkrqnZkmxQhTAf5q2zfZpDqKV6kLGeRRc85O0mWaosB_VIf7j9ux_ilcaq01YiupRY1WXJVU_VpNiBv7D92xaszrdhXcBr2vMEpYVX_2pO8ZMbkZKMlSCg3QL5kPmS3q8kLYpzDotgDufiWDDax2kBMUsNsseOVF26uBIQps_H4uvpXyLbAjd-dsglLRe-TJjG1fFpfJ5Di-ySnuf0BkEULlU7-gVlkvILhBs4AFsSssR53X5x_F_6ziiYS2nT25TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خواهر کریستیانو رونالدو با لایک کردن یه پست علیه برونو فرناندز خبرساز شده؛ توی اون پست گفته شده بود برونو با اینکه بازیکن بااستعدادیه، اما توی بازی‌های بزرگ و لحظه‌های حساس اون تأثیری که ازش انتظار میره رو نداره و وقتی تیم به رهبر نیاز داره، کمتر خودش رو نشون میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94383" target="_blank">📅 11:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94382">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=UbaRdWP1_T8MHB49PtezqC09A4jDKlYxSPkApoAiBC_wggd96jz2_eulQFClM_4K4zOXcDBMiaeEBpRnNf80hEK57e9v6Vv_5Dn0EafQlbKkEp218D9xvTY4v8mSo-L1vh8E05smr-jLkGiMMt4Flg69cO3Z0zY6Chr_5fnW1Iquk7aDRUiCUMXEXGVuWoPNMIC9HBaJOasbwU72xJj4pSWFK7wxHkx8z9UW2U7WQ37SxZr9szJybx9mtwJVz_xkYV1KZXwqa6ostUValNqNWqDnv6PJkYva-X-dZ6yeTmhaEAEflY1DjYLrrAvT0VlVyuQGTzABTkgqNRNoiHkYhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=UbaRdWP1_T8MHB49PtezqC09A4jDKlYxSPkApoAiBC_wggd96jz2_eulQFClM_4K4zOXcDBMiaeEBpRnNf80hEK57e9v6Vv_5Dn0EafQlbKkEp218D9xvTY4v8mSo-L1vh8E05smr-jLkGiMMt4Flg69cO3Z0zY6Chr_5fnW1Iquk7aDRUiCUMXEXGVuWoPNMIC9HBaJOasbwU72xJj4pSWFK7wxHkx8z9UW2U7WQ37SxZr9szJybx9mtwJVz_xkYV1KZXwqa6ostUValNqNWqDnv6PJkYva-X-dZ6yeTmhaEAEflY1DjYLrrAvT0VlVyuQGTzABTkgqNRNoiHkYhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحبت‌های بامزه ابوطالب از کراش‌زدن خارجیا روی رامین‌رضاییان و میلاد محمدی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94382" target="_blank">📅 11:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94381">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=TxVQahaD_hhUj1gySpBeBGKZrc-w8ylj68P4VyExCz1f6fyXVQC5wahnnxKjhAzXSA_VIk6_l8htWrjUI2L9XoRzvEW97tLikWC--m5EEiL24gexCw1aD4NuCSMEYYBIN5RCiO5HyinlttUPCKQpRia3BTfk_kXlXkvA-bnuIRaVMs96nKDCBVT9en28JBx2gRzoYjnZd-LaTp5qZZD8YFYZsJo6nMumXTao7JVI2J9SZfbUlwd3i535o7aRNVtKiEZ3acSTyr168UpqRHfBW9NyEdTy6Py_bxenyabLkiAvGBEoKREGXgWW1R_gwzjpTXhw-MWdDTLDRcxNAfqwEjujSD7mWd40KkupBqtQQa2cZhHJS96lZ2HK9c4VRyqfxo-YvBYp3hmNXfC96bd2rO9QBbuh6EzRm6WxwFpCCJuH0ZMK-2FF__lk-J3GvpqbeiZ2rTJv_JjDVULbEhbWWfbW2pkJVdtrbHPOmr0yxvMi_XygAwVP8JGJRIbKmGbcl4HyioSWLFl9X9OTU6ke-kbSZa6kYPdXnSnQXbodJTTXop4zox2qD-t2LvuROyBWyUdiG7kA3DFw7wD7HKkg4bQKE51yz8vdmmi0r0TYzmOanTfIpulrjqHMdDhnFYeEGdp1REfiWQ2oOi_VOMmbKDK0qPAyMGVZgKWuujP5Z5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=TxVQahaD_hhUj1gySpBeBGKZrc-w8ylj68P4VyExCz1f6fyXVQC5wahnnxKjhAzXSA_VIk6_l8htWrjUI2L9XoRzvEW97tLikWC--m5EEiL24gexCw1aD4NuCSMEYYBIN5RCiO5HyinlttUPCKQpRia3BTfk_kXlXkvA-bnuIRaVMs96nKDCBVT9en28JBx2gRzoYjnZd-LaTp5qZZD8YFYZsJo6nMumXTao7JVI2J9SZfbUlwd3i535o7aRNVtKiEZ3acSTyr168UpqRHfBW9NyEdTy6Py_bxenyabLkiAvGBEoKREGXgWW1R_gwzjpTXhw-MWdDTLDRcxNAfqwEjujSD7mWd40KkupBqtQQa2cZhHJS96lZ2HK9c4VRyqfxo-YvBYp3hmNXfC96bd2rO9QBbuh6EzRm6WxwFpCCJuH0ZMK-2FF__lk-J3GvpqbeiZ2rTJv_JjDVULbEhbWWfbW2pkJVdtrbHPOmr0yxvMi_XygAwVP8JGJRIbKmGbcl4HyioSWLFl9X9OTU6ke-kbSZa6kYPdXnSnQXbodJTTXop4zox2qD-t2LvuROyBWyUdiG7kA3DFw7wD7HKkg4bQKE51yz8vdmmi0r0TYzmOanTfIpulrjqHMdDhnFYeEGdp1REfiWQ2oOi_VOMmbKDK0qPAyMGVZgKWuujP5Z5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇧🇷
طرفدار ایرانی و خوشکل تیم‌‌ملی برزیل که آماده بازی مقابل هائیتی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94381" target="_blank">📅 11:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=eJEzaX10-SfBiM3dDDg_Ul20Q8QKkQ-1CTw_NdY2d3lAusq4RJDjkK-ETVw_op4tcvtnFhCputv5jGOf0OTEfpFZeiS2UzLH_oF57x1rp7CS6XAxAAlYw1PGmv86EU2dsUpPDnHGYED2fDNhURP0cW_510ZLysipUuNCT2MzFKfKSxcA4fcPp6VWVhi-kVpjCxMUdPGuJtQDsm0bEAf3rLXzRIn6lmkt6WCmX70ujMzDhi5ZJpJlGRzbC3yYg_ytyJJ3NY4VEMO9MFCw3Uysh8o9QTdZuG23TV1D1epLHojnn-BrGa-3eeFgmxaRbieGnN4Ap8VTAcJrWGUk7SgK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=eJEzaX10-SfBiM3dDDg_Ul20Q8QKkQ-1CTw_NdY2d3lAusq4RJDjkK-ETVw_op4tcvtnFhCputv5jGOf0OTEfpFZeiS2UzLH_oF57x1rp7CS6XAxAAlYw1PGmv86EU2dsUpPDnHGYED2fDNhURP0cW_510ZLysipUuNCT2MzFKfKSxcA4fcPp6VWVhi-kVpjCxMUdPGuJtQDsm0bEAf3rLXzRIn6lmkt6WCmX70ujMzDhi5ZJpJlGRzbC3yYg_ytyJJ3NY4VEMO9MFCw3Uysh8o9QTdZuG23TV1D1epLHojnn-BrGa-3eeFgmxaRbieGnN4Ap8VTAcJrWGUk7SgK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
جشن صعود مکزیکی ها؛ پشمام از جمعیت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94380" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=d48XIRZ3LCpuNTKboUB9ROWtYMZg__mTDOabRC6VZTP58LEFaDF9IuWjSYs3kvn5Xi2oI4JBqupNFGunHgs5vOd8VnuMajk6U7yERdFCNTgD3QoTGSQLrgoA6EReO2OonISXHvCfl5PLCRIlMrvY35dfPkQMBVkG_5ka0Xaqa5h-5zz8h2d83ygq6RRhxDdfnUyDSbvhril0VOvMLpp-uKyjBx4Aq0B4s-fXpvY4WrqokLn-6LsmBnhDjhYOOfHmIfh_b1W9v_KxdK8OfRWaZXMbppHDUpTle7NW6XzBwH1AXUvcvTMSYLm149YmY8ZdGNsIeUS1tVCiSoktLUcL5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=d48XIRZ3LCpuNTKboUB9ROWtYMZg__mTDOabRC6VZTP58LEFaDF9IuWjSYs3kvn5Xi2oI4JBqupNFGunHgs5vOd8VnuMajk6U7yERdFCNTgD3QoTGSQLrgoA6EReO2OonISXHvCfl5PLCRIlMrvY35dfPkQMBVkG_5ka0Xaqa5h-5zz8h2d83ygq6RRhxDdfnUyDSbvhril0VOvMLpp-uKyjBx4Aq0B4s-fXpvY4WrqokLn-6LsmBnhDjhYOOfHmIfh_b1W9v_KxdK8OfRWaZXMbppHDUpTle7NW6XzBwH1AXUvcvTMSYLm149YmY8ZdGNsIeUS1tVCiSoktLUcL5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
شادی هوادر مکزیکی از گلزنی به کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94378" target="_blank">📅 10:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=B0VrosqOYM20qfSkn8o66suZUyPoRWffplGocqe2lP9UABa28EAprgwiW0dFI3i8R7eMfm0SPLouGfxH4O1UJab8QqeDGGTnUQlv6u4R__Wk3IRZ0PETB8WFMg0nX6hpVRIq0epn9w53ZyVHsAxcsL1xlaebTXKiIDn0bkmcryq49Z2Deh1NHifu3fiEnVK7VWHQf29qmcW1Z7-1gTnCiIOJECm28CzxZ6zwO1G-nEZXib5cLI9h_yE-_u-Smmpq0X93iRWS8r4luQgOklKEyIur5jqulYr1HUbu6dPnlcrxwJ7-vb5ZxzlEi1_hc-5C7IM4d2yDtxeHhBOQiMTVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=B0VrosqOYM20qfSkn8o66suZUyPoRWffplGocqe2lP9UABa28EAprgwiW0dFI3i8R7eMfm0SPLouGfxH4O1UJab8QqeDGGTnUQlv6u4R__Wk3IRZ0PETB8WFMg0nX6hpVRIq0epn9w53ZyVHsAxcsL1xlaebTXKiIDn0bkmcryq49Z2Deh1NHifu3fiEnVK7VWHQf29qmcW1Z7-1gTnCiIOJECm28CzxZ6zwO1G-nEZXib5cLI9h_yE-_u-Smmpq0X93iRWS8r4luQgOklKEyIur5jqulYr1HUbu6dPnlcrxwJ7-vb5ZxzlEi1_hc-5C7IM4d2yDtxeHhBOQiMTVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇵🇹
آقای کریس‌رونالدو واقعا زشته دختران در و داف سرزمینمو ناراحت کنی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94377" target="_blank">📅 10:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=m2fVM0o0vy6_mZtiI9a0Iyor4wdL__bdSeLAac2aXyjXw37SVYOgfQa0sxqqub4PU-xcEV7YUMAT5uhZzUUph1CPg5F_9DZcK-F0JGlUrZBVkZvoUgusU3AwrjOWOKgMeWu3sKPvUf41pVRgTOarb0-wUbJyBwmhd3NnkXgquW6RHWdhoYBJ05f4Fo3ih0iDO1E-lHXu1PCR2QsMdnmBa6TKqkxF_unZjnahoqPF4c13MQLslgp7RRew4Bj7dbfVeVpe6Z-8u9BVIEd5Vh0eHWRQSqfysWxOs5935aDuRVJ1-SGBFnefchu0Pm2LQZJH585z1TF-KFjYh7aa9HFi7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=m2fVM0o0vy6_mZtiI9a0Iyor4wdL__bdSeLAac2aXyjXw37SVYOgfQa0sxqqub4PU-xcEV7YUMAT5uhZzUUph1CPg5F_9DZcK-F0JGlUrZBVkZvoUgusU3AwrjOWOKgMeWu3sKPvUf41pVRgTOarb0-wUbJyBwmhd3NnkXgquW6RHWdhoYBJ05f4Fo3ih0iDO1E-lHXu1PCR2QsMdnmBa6TKqkxF_unZjnahoqPF4c13MQLslgp7RRew4Bj7dbfVeVpe6Z-8u9BVIEd5Vh0eHWRQSqfysWxOs5935aDuRVJ1-SGBFnefchu0Pm2LQZJH585z1TF-KFjYh7aa9HFi7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
💥
هوادار ازبک‌که روی رامین‌رضاییان کراش زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94376" target="_blank">📅 10:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=S37W0ZUgTjxviREbpn4wiLJsN6PaODC938Cd5_fDNb43JES9JkUTv6mdpB6jTny8geJcFJb6BoM-0PQOLFS6YszWaNrS3c6h5ZzBcprTs0AVXGuPe-pB24kVgMCWhJ18tPw1UhlIUmpca_ZiMdoOGPASLDHd986PcWjL1rQRQKu_SnferyanTVDwsZ784S_ACTBeuKCm66e5kXg2HIgpw6MGlyqvHyym0EwDhXbrHrVcpGpNswzwiPcSIQdW3_hUZL0SZkCtQrcz0uWFdjBRNUS94TbUmV66fxGscIRhCr7V8T-zUBt6mKjhFeTbWRAszvYsjaz8W2U_-F001Pl1Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=S37W0ZUgTjxviREbpn4wiLJsN6PaODC938Cd5_fDNb43JES9JkUTv6mdpB6jTny8geJcFJb6BoM-0PQOLFS6YszWaNrS3c6h5ZzBcprTs0AVXGuPe-pB24kVgMCWhJ18tPw1UhlIUmpca_ZiMdoOGPASLDHd986PcWjL1rQRQKu_SnferyanTVDwsZ784S_ACTBeuKCm66e5kXg2HIgpw6MGlyqvHyym0EwDhXbrHrVcpGpNswzwiPcSIQdW3_hUZL0SZkCtQrcz0uWFdjBRNUS94TbUmV66fxGscIRhCr7V8T-zUBt6mKjhFeTbWRAszvYsjaz8W2U_-F001Pl1Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
🇦🇷
همه را دیدم و مسی بهترین بود
آرزوی جالب خانمی ۱۰۴ ساله، که تک‌تک جام جهانی‌ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94375" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=FKRcUs6iYnuHZkyycDDmTB25wtnnkGbSBjMZReTlk01ZM3NCpXX1vxp96vvivOyVfhedooCBv0JUylg-m4xzWBiBZkToLjgci9T2NesYZWsL1epcWJpJ7TrNtTk-ANo-TJu5Yj6nrshfzCCmSaANuAqBt3aW7zqeNAM-EBSeafkSNtPOrYPeWx0m6ygX6ONsbnddXO8RLz8Vxvm58o2o5z1k_IqXknA46DTQjCrFLZl2Wkjf8P5iYjHoNoyqUOErpe4Z7fsy5arPrc7YwyPB6wLkVTDpSJyWSKBEq_45A1c4ZtxTZcFSNL8rkHmX9w3oRYiX5rAOAOvTCna9KflUFL2z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=FKRcUs6iYnuHZkyycDDmTB25wtnnkGbSBjMZReTlk01ZM3NCpXX1vxp96vvivOyVfhedooCBv0JUylg-m4xzWBiBZkToLjgci9T2NesYZWsL1epcWJpJ7TrNtTk-ANo-TJu5Yj6nrshfzCCmSaANuAqBt3aW7zqeNAM-EBSeafkSNtPOrYPeWx0m6ygX6ONsbnddXO8RLz8Vxvm58o2o5z1k_IqXknA46DTQjCrFLZl2Wkjf8P5iYjHoNoyqUOErpe4Z7fsy5arPrc7YwyPB6wLkVTDpSJyWSKBEq_45A1c4ZtxTZcFSNL8rkHmX9w3oRYiX5rAOAOvTCna9KflUFL2z7Hk9XOfXGo_z9FBsmgdpzIO1GxV3v5H6ISYnbmFPrtB_SUAZHNB3VzMmbRYuPgpjiSrmmugWT--d_gHTEfA_qPYC0brjNC6yI-WVgcy0LWlK_VXd76vOodbnomAl4KC5xrZck9lLIVEBbxa3_6KGPos2xedfsLzJcpsr0-wF-OrZgf-irUaV5IwXmmadDs11G8CQwDc5RV5-rm8PD96MrkMYGpNQyRuxGOFjoJuJ2TqNvv14H3MEHKZg5nSOhgUwodTUh_kC1Iao0csK3Co8-AXKACOPY1DGGpSA1Oqqc2YToBr7B7yMzOwXcDaOcK4zRImenQJe4-jqxtQEYrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وقتی فوت‌موب آلارم گل میده ولی صداوسیما دو دقیقه بعدش صحنه رو پخش میکنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94374" target="_blank">📅 09:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=EfOm8o6KKIbAsXx5DxNy3v-NtM3ZthRiVRlTS8Eidgwosfs4cCSJ9XeHukPUqIUOCjooGS5GX95E2ZQKtxs2XP5odEUoP0IxD3cEs3eDHcerV6LhMEM1h4GSdkHRUUDePEYzKJiQ3FyfjBhhivdY1UoHgK-ecS9A3CujaKBdkQyNQy-xp19_v1gAbA-tD2H6W7Ppa7K7Q7B-zKvaD8qirc8EllA6VDpyR_Z9tpt2-moaDGS_6ynTIx0Ijonzo39I7RbnfvWbg-nKW4Wby4fRfRUcabJDIGtJeOg8oxlXzMwUen-xHAWzrOZNCJrBU7GDZ89XSJW0LuHj5_4fnN0ciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=EfOm8o6KKIbAsXx5DxNy3v-NtM3ZthRiVRlTS8Eidgwosfs4cCSJ9XeHukPUqIUOCjooGS5GX95E2ZQKtxs2XP5odEUoP0IxD3cEs3eDHcerV6LhMEM1h4GSdkHRUUDePEYzKJiQ3FyfjBhhivdY1UoHgK-ecS9A3CujaKBdkQyNQy-xp19_v1gAbA-tD2H6W7Ppa7K7Q7B-zKvaD8qirc8EllA6VDpyR_Z9tpt2-moaDGS_6ynTIx0Ijonzo39I7RbnfvWbg-nKW4Wby4fRfRUcabJDIGtJeOg8oxlXzMwUen-xHAWzrOZNCJrBU7GDZ89XSJW0LuHj5_4fnN0ciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇳🇴
پارلمان نروژ تو جلسه دیروزش بابت برد کشورشون در جام‌جهانی اینجوری جشن گرفتن. خداوکیلی کشورو میبینی ارضا میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94373" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=IcdqtGSfP3hLiMZenwPp_TT2BvufoS2QRxAI54S8o0T8eoBDj1mhtAcD4pr-whSF_un_tNKLFlEp-QFggEPEjMeV-OT58LLcckDZFYTW93elovMKlcEp2F7lICDMa-37EM3ty9lfUxWDm4rk5aZJvWM6fucV4akGbm6HQ1BmEr59bbdkSVrapULSB6wa9koPE9LXec6260XbRFF7SWCCfOm71dUi7ubr6yhPA46r5uMLJtEHv9Rpaej0opJzgYJdMwKhov9R-npZXW8BDn-iPCMH5jogvOBiPqaBQb3vOveozMTuS6FuYxv6tiPDpvon1Nqu5ssrCD6661rTXDsqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=IcdqtGSfP3hLiMZenwPp_TT2BvufoS2QRxAI54S8o0T8eoBDj1mhtAcD4pr-whSF_un_tNKLFlEp-QFggEPEjMeV-OT58LLcckDZFYTW93elovMKlcEp2F7lICDMa-37EM3ty9lfUxWDm4rk5aZJvWM6fucV4akGbm6HQ1BmEr59bbdkSVrapULSB6wa9koPE9LXec6260XbRFF7SWCCfOm71dUi7ubr6yhPA46r5uMLJtEHv9Rpaej0opJzgYJdMwKhov9R-npZXW8BDn-iPCMH5jogvOBiPqaBQb3vOveozMTuS6FuYxv6tiPDpvon1Nqu5ssrCD6661rTXDsqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
🇫🇷
دیکتاتور امباپه تو تمرین دیروز فرانسه رفته جای دشان نشسته و عملکرد بازیکنا رو میبینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94372" target="_blank">📅 08:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSJGGPD7ggA2svwyXNXCSPON5xxbbFpWjkUVweJQEUD9nPm3PcqGIb4ImDN0poAPomd3M6V-9WhoesE-3TvQa53RCn6dF8JgD0_vdOyLstzP4MQ1hqEKRT0x1TTWARu8VmXy21Ka0fejgLHz3MVxWfm5MKkR0bv5wm72URSdz-uQ2sjr6TOMUKY2jFSkjtTzhnt3dgTIK_8VKYtg-LZnaBK0oF0rbhckgtgUQTVRrd57_fLw08xfTT6z_YzzIi6eIl-2Y24nCUZgXb9eHR1ZwjVJILMHf3kIVIF-YvDxESq_QETwQwrgB3CcGdIu0xedmFgZW8ze5Ax2tHy15KVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇦
#فووووری؛ اسماعیل کونه بازیکن کانادا بدلیل شکستگی استخوان درشت نی و نازک نی حدود ۵ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94371" target="_blank">📅 08:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94370" target="_blank">📅 08:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyNX-WADRY6xAinqEH9xcUSs1BcySafhrbCxJVl7fEyyqslb1YiFBHvnCfDMojuloRUv2hdgoAJ2szmCCk1uHcnSqdnvj8sG3MHgLDEmCFUoYDWrskT18eL5MEGykQ1aAQNOHb4-vTlXIS2fqV8qtMw_qTvu9Mc6wgqxeQPopqKYWDbRSMsVUHYnzTC9QFyppAwUadiYSu_pPeZEnuCD4nOJwMDVv8G6MVzh95AGR9EzMKyUSiy05HwDUbJhaYAosHz6HBbfc-8EayPmQYJVKardd-hRPAPl6wGHkP_4D8D3uU1f6ETmW-6aj1pMjpdcmJmktb2DVCVaVwyMuA8DkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لوئیز رومو بهترین بازیکن دیدار مکزیک و کره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94369" target="_blank">📅 06:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drtfcjlHqnMyNA7Pv8zWD_4qTe574jwa2C6w6SzBvIR_Wke_i9Vh2sX9OibiaWsG2OjSsRRap2yDlte3oloT0sZ5b-OrqjsXw2nDdGklVYzJRFeaVAMnoeyPGNzEsSIXZ8Jw13yBJv6jK6fkCGI4Qy19cw8SaIOcVHoKcHdk97Z1V-p8cLfwgX14l-IVcfPQnMTMQRGR88V_fBrFiH4strFDrPE_VNmH_zZrooCZZ_04PWzu8Q6VkvvpHprdtA9cHJB1PVYW6_z7CLIpAHxE7iUgGrqTZPxAKxPr6_PNeXzEwwM7LlVbs7It6bDhAfOujtpYrf6CvddM2Y__g_3ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه A جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94368" target="_blank">📅 06:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94367">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw-PQY2QOhqCAclKtUA4RbrvsSdyEWkf2MzKIxlN6DgSJsP59XLotqhOZCQx8WA6n_A6HJKVDAm8u8SXVPyCtvih7MHgwOQTgLFIl3mGUXsE1pC_OpYpXDWEFyQEsYvbCdFd7_PZhEG5dvM93aFPFb9JA2dl8tdDnOmSMtKuD4En1jEaaL77CaxL7qb3Jh4fTXzG-Uv69lQ1ugLaECdyqPdQjkpgHdFDFOyM0_cz4V4j6syx-KEaocoiOY4nRnRxFdVnpmXXQyM9oYbSmdTR9NG9fgghhOX0GZg7SBmRXGlB9NinX7zVL6NFO2zgP2_KIFWdaF9fo3xwOf5w7VfM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94367" target="_blank">📅 06:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10d309995.mp4?token=dH5s7-bH_1ct7jbhCQiPBWdWesy295PjlZTTGAtRI9ZSWtBLo4Q2lKPIiEpySZppQu0OSak4aid7YvNw8sMb5yqt23jPKYUKT-Yda_bYVDktK1q7ORURmo3IDfO6rV0jJygbF7M6cRqIdgvXNWi4OPbCQqHOGkoqh0hN9PkkV4Pk8BRx11b2OtoXTEfYu5Gp6drUC35bEaeg4z0cSs0le9PpuiiZcpGerwijpWs-5_jCjXmzK-GV4WLrarPBUv842xvFKuKrivfmSHeiRXSHSq_NwgDwDrWtUHxiPOqUuj0q4DGVJ7-qqdiFgvxCyhOW04uYVwY2s8WsCQeN-QNCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10d309995.mp4?token=dH5s7-bH_1ct7jbhCQiPBWdWesy295PjlZTTGAtRI9ZSWtBLo4Q2lKPIiEpySZppQu0OSak4aid7YvNw8sMb5yqt23jPKYUKT-Yda_bYVDktK1q7ORURmo3IDfO6rV0jJygbF7M6cRqIdgvXNWi4OPbCQqHOGkoqh0hN9PkkV4Pk8BRx11b2OtoXTEfYu5Gp6drUC35bEaeg4z0cSs0le9PpuiiZcpGerwijpWs-5_jCjXmzK-GV4WLrarPBUv842xvFKuKrivfmSHeiRXSHSq_NwgDwDrWtUHxiPOqUuj0q4DGVJ7-qqdiFgvxCyhOW04uYVwY2s8WsCQeN-QNCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل مکزیک به کره‌جنوبی توسط لوئیس رومو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94366" target="_blank">📅 05:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلر کره رو
😂
😂
😂</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94364" target="_blank">📅 05:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مکزیک زد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94363" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94362" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnBuiUK36y6fa2tzyCwQiXqC9Lh16NRmIaw4FuZASiPV5Ercm_CipBV7_3ysdA1FZu4K1hZu7SGLj1BG_oAy4bW3yjZT8-oH9HSTi5ZB4SOhTwZOkFRREcJLQ8zn9Ar9GeZbpp1jVujy6r0cIIQPIMtpJPEkwFJSV3Y3OXFLhwVdSS3OKcmB0_Si9IJLk4D7Cdzb8JsBtrUWhNdsn7Wqy0zGT1ThL9Eyi7sj-YlPE1BhjGv8jEq0kJ5-5qfujw2Jk3Ov0GFxOl50dzVbd9wnIPjPl248yt5lDvsZqZ9FFCZNb0nfQdO56-8wfDTJbXXpka_EC3GefTzZTAZA08tINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STOx51UQiO5uh36mH8HI3jY7temzF6jePfOJ0Pv78RxakuIm20Hv2BXIwvnnVgbiAG4iW4zJXrexzRAY9aqAPS7fpBWqpIPNROCUwXMYanNkK_s0jwPixTMjgsc6R4c5TLtMIZlFDK1Az1EeXWePrRUwL2ObXoJsicIeQ6GYrcFc-2mjkqUSLAYFFFN1XVZxC2S1SUA0dF3TU95wx837vAlKsamPsI0SO1KiPBxdhoaUbadPGUJTNEteshjzzkDT3dug1CadqLr5BZCKkXbCBNOWwyJYqzfYos7qCsmTp9zzEHhjjVHYWSVzmmp-l10vw3IroGah_vbm3oG2tOjQ7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لاشی داری به کجا نگاه میکنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94360" target="_blank">📅 05:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAPJeK6n27IYOHYb1nBTWZ5655N4ZfcdpJ55zBHAhdVm7TAq19HRZmQ7fEW5ZjB76sKzjrDb5KZ9-ShU__E-l9kYhBoj7PSF-HVrICAJoEU7cMkBpsXjhjhDtiBJE5oOWHZC7jiAnYZZpeW_dYFRSY3Gil9GrBwFqlFDz0MVJe5bbApg8iUfILOdiQ8uDscXuGf5Kshm6wQN8lii0BcdDAB6XFA5hMkLKcaafbQZDylj2AmOsLFJ91AR0vuoRxnXl9GeqaXnrw_ng6KXAFxQKzgbXb7ME-HoQyQi8DbP_9JW-2eRrtDEjLn7oZ2IGNGaDj_jdgr0XdlL99yjSNo_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کوچولو تنها کسیه که میتونه بگه از نوزادی طرفدار تیفوسی مکزیک بودم
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94359" target="_blank">📅 05:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پایان نیمه اول
🇰🇷
کره‌جنوبی 0 -
🇲🇽
مکزیک 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94358" target="_blank">📅 05:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عجب بازی ای شدههههه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94357" target="_blank">📅 04:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=lWfqUUa9MsL6wRktYQHYIvnGtZC-duy-ShdN1abPxrbvdFfYBepYEuiqfeqXXZkQJFZwofvJyuJcBmx8j8YgW97yV58G1ctZT6DVnSyXkVRtCbmKnuJdoPn8SV3s5EBq4uve_ZINJL_-p_SeCPlYiqQ2vLSBKekFtyyAXlvcsyWv3Wld9_4vTeMN5P8VI9sfGtqPkeyfK-lvNACHxbcHsbAMx_KNbO0eJ3ZOr_3XBPWOTqzK48iYL1y8V8oo5fxP2yT1EcmWLSM23zCQ26qFs3iHMOJFg_siYxymLP4m4Di_opVXfUKc-z0j9mzQT-3m5_Ywdrn3oAmZXLaFhvvsZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=lWfqUUa9MsL6wRktYQHYIvnGtZC-duy-ShdN1abPxrbvdFfYBepYEuiqfeqXXZkQJFZwofvJyuJcBmx8j8YgW97yV58G1ctZT6DVnSyXkVRtCbmKnuJdoPn8SV3s5EBq4uve_ZINJL_-p_SeCPlYiqQ2vLSBKekFtyyAXlvcsyWv3Wld9_4vTeMN5P8VI9sfGtqPkeyfK-lvNACHxbcHsbAMx_KNbO0eJ3ZOr_3XBPWOTqzK48iYL1y8V8oo5fxP2yT1EcmWLSM23zCQ26qFs3iHMOJFg_siYxymLP4m4Di_opVXfUKc-z0j9mzQT-3m5_Ywdrn3oAmZXLaFhvvsZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمامممم دفاع مکزیک عجب توپیو در آورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94356" target="_blank">📅 04:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JurK5lqF64iJxqmvUT9hoRGTYLb9bj2gsrch7x9pr7EfXvD3TZ5wV5EE1e0MTKuPso5TM8Jn8SGVn37vt3s2Ksr_pD4gynnI2bcBU625sbstQXu-YzRkTDqLS02QI1DRlCdMGYA50r0y4VwoIrxXQ-jWSx94P_8Kjlg3dz_xNwMDfOJKjCPfBUn3tCrXreiDerzs51Yxz3g2w2yMlw_ec2vr1imuqkoNvzEdloIXATeYbeL-S7H0HonJCaQh_zRwum5F3-IhCi6mhe28j1gVq6F4U6H5SI5J9rhM__0fF_GvXYuDWutDWYJJllob6Ka0v0i1RHi-DayMd6d7F7nZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94355" target="_blank">📅 04:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=vocil7r5lsLL2y4Dw8-3Wd0iDGzCqAKrWWkptLD0d7q_mO_zFTEf0cJwHDFs2VgYjC0ulM2YmzUJFC2mjdLUYxS7Gs4hBJF6eXU-Lfdr-eibXnhR4_DVrz_G4fteo1FfkXFiFgi1ahI6nTTUnkZDhzbRPSvJlS8Uc-oP6UOCgvjyO6G6jXhLulXhZN2KkBycutQan9J3yRlGIoOIITEAkVRk2LagAsAqTX108-_S4FFGJo1WrprGLj1RcqSKvJaAYEPoppMflgZYhgfFDZ4x12Cm2-W319hbUmKjsrhqHwp5nzMuoXIXZ_0ry0xAB2BVLxqO7d3sLt25ABxM6sbEnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=vocil7r5lsLL2y4Dw8-3Wd0iDGzCqAKrWWkptLD0d7q_mO_zFTEf0cJwHDFs2VgYjC0ulM2YmzUJFC2mjdLUYxS7Gs4hBJF6eXU-Lfdr-eibXnhR4_DVrz_G4fteo1FfkXFiFgi1ahI6nTTUnkZDhzbRPSvJlS8Uc-oP6UOCgvjyO6G6jXhLulXhZN2KkBycutQan9J3yRlGIoOIITEAkVRk2LagAsAqTX108-_S4FFGJo1WrprGLj1RcqSKvJaAYEPoppMflgZYhgfFDZ4x12Cm2-W319hbUmKjsrhqHwp5nzMuoXIXZ_0ry0xAB2BVLxqO7d3sLt25ABxM6sbEnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⭐
هدیه جالب یولیان ناگلزمن سرمربی آلمان به هارتموت شرزر ۸۸ ساله، خبرنگاری که هفدهمین جام جهانی خود را پشت سر می‌گذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94354" target="_blank">📅 04:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بریم برا شروع بازی مکزیک - کره‌جنوبی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94353" target="_blank">📅 04:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWslKHE_uuMdAkk320v_aF56_nFWT693wWVxqsvnMFRAs2QMucydiBZxeT1xdaE67RFmRKA7M3NaoIOdxHQvgiEfSyC6ozS7bo1fiCykveA6WpUntJFzmhuxIINxtVpzQd9Bf7ASGgWfRgb1zZTXDL69tx-adovye0epX5J8b9KwTzSWB_I0JNpubRIz8RhZIdsQNzzqUBtPN-BnongLsx7odXzDj2HTWkwScIYZYJHFSSckXoPzVn_PE9GMyRQSZ6QLvHUtZj-yr4TbxP0-oiQPxRNoXTq3_WfeDXyKN2ihBGZm-ZzTV4ZAjOQfr5gJisrFMPtGRz-rplMFnN7kVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSeAbNRQrT4NJKwNbQf3GBGp552SyWuv3emw_0qtEiiK32es4iRJT3lMD8raDrs7z4diSxxRUuN-Miv_ltEBFCtXxK43yE4ru94f4csgvC-_ue2hPWKB7OVv9zBvZjeG48jT9wqDvhP4nR2iAghEgxRzV7V2c11aj7Q_GBv7goFZ16yYz7YQyksNbuvIrMNq_wx4scDed_e4zmOrZVC3TABrLpGfAo_xkcGlq3SiMTuApUAZHAYsQsqPSkhif5qddoH0J72XgJs1eXYruD-n0w8GF3nwPNihnEx_FE00aSfifd6lRlzyjYuaY8kNgRnztDwrTu2nzHASusGbOqKTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXkEJRxMxDEMABvkjFYipV9e2XqYbRO46OKwl5z2lFVWMCD8uQPG7Og0cej1so4V_6Zmrjghf-RB_KkFUf7ynB80yek8qFOeZ_USwoLikLk5TSPUyC7eOg70FcPMvt3O1VoTIgVmZ3q_5D6UJmX1yYrqqf-tAiKcLZj5QUd2w9Deb2TgjQTo-UNvqQJuNpIgX06E6Y3QeKO0F2O0kL8WpgkaKyJGZYfKypCgIMOrvjrigsCBPQY-hvQHbOmkkHJaCnapK-rJ1sGvVBorAFylvXqsJlYWwWh-ZNwaEobbnjDSoou8y4T932Sbx--IAhOVFNjjBiirXknQ4YdUZdv6jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قهرمان دو دوره متوالی جام ملت های آسیا مقابل کانادا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94350" target="_blank">📅 04:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c256eff540.mp4?token=jD-kIUWZjhv8_d4_jr9IlaRiyIEKU7VyWWP4NfrVu4InYYB8OOMUUhggD8cnsT7eHN3WtpVl1KfFUL6uAv6ze1qrr0ME7IZhoByr9xxLVx9TdDB8gPgTp5CESEzd4o7jA3oERJaZbfNZv9B3eQCZmkSWAg0Nrv4JmywYj3FX8qDiT8LnFpDPFh2R6s-WprA3zhhjZhqY9i3HwVYJbZrD8BpoGpqTxTxwludR3h21emtJsvE870lubqgELW75zc6-ckvJSSH33gJYv8lL-xDYPIiE8aTtaSbYZ-lxoLxJwQALiQNm89IKjIBc1Zc2G6U6V1FL8e8ogMrcGHroyS564g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c256eff540.mp4?token=jD-kIUWZjhv8_d4_jr9IlaRiyIEKU7VyWWP4NfrVu4InYYB8OOMUUhggD8cnsT7eHN3WtpVl1KfFUL6uAv6ze1qrr0ME7IZhoByr9xxLVx9TdDB8gPgTp5CESEzd4o7jA3oERJaZbfNZv9B3eQCZmkSWAg0Nrv4JmywYj3FX8qDiT8LnFpDPFh2R6s-WprA3zhhjZhqY9i3HwVYJbZrD8BpoGpqTxTxwludR3h21emtJsvE870lubqgELW75zc6-ckvJSSH33gJYv8lL-xDYPIiE8aTtaSbYZ-lxoLxJwQALiQNm89IKjIBc1Zc2G6U6V1FL8e8ogMrcGHroyS564g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇲🇦
بارندگی شدید در شهر بوستون قبل بازی فردا مراکش و اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94349" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz3018yVS1JllsTJs2BiKdDdeDS9VRD7aG_1AmYwEItjLDvmtXja2MywhDXAbFfu6DUdpNu8dQRcUQBuhzQ5jt0PhqsjVk456nrr8mUpywOem3c54OgSWqUGOxvPsPj5iWJpzzEbPffY7HkhTMoiQT70xViCa5dSMZlG2s2z3MN1ZOAXqColY3IkWd6RkE1X0BwWiG_DZWxP0GSi9ZvyJc9UsdCN-J_-S1zuxS4x_QYSztjl0NKHvHjZFzmWbQlQzsx8URoYMlbmg6e8VliP3FRvFRUXtP1C5gwDioEhTlw0JdnOj3gHGOedyjBXnFupjpKPb27rX50a-MHj6mxKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جاناتان دیوید به عنوان بهترین بازیکن دیدار قطر و کانادا انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94348" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgQQY2ZlA00WxIQbjghdXygGUc6vVSz1-zT29lWvd0Ks8AoPYngLmvbjzauX3MSiaEpxA59ylAKen5Nu3U8GX_zvmgjnkm3gizdX0WojUj_5b7HUo86JfedKSPfagk2uqiwDWj94IxMglpWV9FUf00HZt2vOODIsT7ePmpPiL2jzTVyZ4WoH94WpaIymvbT2WokLcPfCZfP6WvyfydnXHNcCvBL-qKldDH2-rpt3hIyMXXNV1Sldbyndikhlnt-V5kBH7434pSXqmJOd9ITLJmX8wGP-PO5_kMy0SyTWYVS1W-bdvR25zTt-FVK7oDY9nW3vvCvtGvV-Tkh6V8y0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
کانادا درحالیکه در جام‌های جهانی قبلی موفق به کسب هیچ امتیازی نشده بود در این جام‌جهانی تونسته 4 امتیاز کسب کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94347" target="_blank">📅 04:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d24c944.mp4?token=b_J9BnxvvMVurf8DNkFmjEENSYBIu8bM9gcLS_OEyWBL8ZKkp3MSqddW5bN2wE4_bj3tJurET4bCI67svLVTf_psQj5HixWY94kxWQjQlrXilLzLz7Cpnj5M3faSvnDLlc330MHavMgqdgDhToJkXmr2BYgYUfRRbRh5jfvAhVrepqBzltdwAfo_mBsRG4ciKGc0xeJ_9uQ9mDSB5KUW3S8j-hakzVub-mr4o1qQAdL30ix190Tp1o6oAT_i0OptKdAQDmZqJZ4FUgAPWOGsEvvt3f8xX0TzsIbJhvbmSTbfTuCP_4HMLb-09CCWCJE8EnomLzmAzU9Ra-0Tmxt2nmHdcP9KIqwldDlPCmnQlJZn6xw_4Ix9tF0XfPoYUDOO1I-PTEIOoF7wYLj8rSVAAnpajqs91MCn3npP3_8UbjiBodLvUMgbAnR-AUl8Vb2CBhZxdqNKVJ8AjIdOTCFupaf7ccB99uhLpIwgRqZaoQnrpBriWjXcz_Is8KfXQc2eVHRludriMZs3pYaxGW-4ZQT1v430GGA57S87uN5OFvEuekRNdU2MqCPz9HATPe9M80HJB7XMIelf_7ei4IFDVCn9CEmLAqwtem_FHNJjPPeOyn7OWHeBULrMdqJYn2-ktpMRqYyinetmN-QPepEl3ztLQSv7Uqo32kdJICHxrEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d24c944.mp4?token=b_J9BnxvvMVurf8DNkFmjEENSYBIu8bM9gcLS_OEyWBL8ZKkp3MSqddW5bN2wE4_bj3tJurET4bCI67svLVTf_psQj5HixWY94kxWQjQlrXilLzLz7Cpnj5M3faSvnDLlc330MHavMgqdgDhToJkXmr2BYgYUfRRbRh5jfvAhVrepqBzltdwAfo_mBsRG4ciKGc0xeJ_9uQ9mDSB5KUW3S8j-hakzVub-mr4o1qQAdL30ix190Tp1o6oAT_i0OptKdAQDmZqJZ4FUgAPWOGsEvvt3f8xX0TzsIbJhvbmSTbfTuCP_4HMLb-09CCWCJE8EnomLzmAzU9Ra-0Tmxt2nmHdcP9KIqwldDlPCmnQlJZn6xw_4Ix9tF0XfPoYUDOO1I-PTEIOoF7wYLj8rSVAAnpajqs91MCn3npP3_8UbjiBodLvUMgbAnR-AUl8Vb2CBhZxdqNKVJ8AjIdOTCFupaf7ccB99uhLpIwgRqZaoQnrpBriWjXcz_Is8KfXQc2eVHRludriMZs3pYaxGW-4ZQT1v430GGA57S87uN5OFvEuekRNdU2MqCPz9HATPe9M80HJB7XMIelf_7ei4IFDVCn9CEmLAqwtem_FHNJjPPeOyn7OWHeBULrMdqJYn2-ktpMRqYyinetmN-QPepEl3ztLQSv7Uqo32kdJICHxrEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کمم به جو سکسی هوادارای آلمان در حمایت از تیمشون کف خیابون بپردازیم. هر چی عشق و حاله برا ایناست..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94346" target="_blank">📅 03:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJHIXsdWvtL4507e9Pc6d2C2Xm8J3Z-VmN4q1uO5T96D-txQTGU0ujM9ejYgMD3RIbP_rkXoR8I22aB2PA95sqoegVVxq6J0BjlrtSF2m7sbdMzutx-KfzDW50hJocvrxLxTpSeu5zBzZILn13MwNLQ0ziaJRQNESKy5rOcpJ4YuAZDXRr2-LTRB7ZSov09tFX2ZZx6C1dZW76Jw-QDdLATAML9m5JBhtUau1Swp2By2BP9g4EilNyobEbNtnJStoXCCrKSpAJI2b6H-viW2MB8yJmK_BKUIsoEBw6TX_-0m8WV9eGQyNzTDiynu2usdOP-6zMjDJBB4GIEph4kR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
این جام‌جهانی برای رامین‌رضاییان از طلا بهتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94345" target="_blank">📅 03:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3P_xgzTi4Sfn6VgZwXYqK2BB7XoI-tfZN4dClBzL5b4lSkdsry4YwUKLUYa3577pGujKogk-PCDBWDI0Ei51VrGji87_P7Mjujqs0AQ0osdyg9Q37xE0-v8msfkbpb5Js7YH2qBIU2Dlc6oy8d02cGGNkNsTcAuOaXYW5NJvsReOGP4cRG6vB7T9YvxjS9XeHxEl6jdErlRksxVdQb1mIB49d6dKxnhWiZ12F2RtWQJZQjlB-WTHcJ2pweydRGdxkshvxJoOgHu-Dy83Yr7NN8za_0E-MWXh5xut4pPj8mcqvPbadbghTuVNY4h4viHW9cdfr9ryRI_ejLlz7Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه B جام‌جهانی که تقریبا باید گفت قطر و بوسنی برای صعود باید برای جایگاه سومی تلاش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94344" target="_blank">📅 03:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9jGHx4-AZByKewkogkhEgRQkgGGkAwgDcQwdbZRR3gOp7acLLhsdTKOMZ0b1vLUhYOkxLjMX55-iAxMbZQt4du1Q1uZWyXaJD71lDI-ByrF5MjtYghZBI2Y5NmEi0RG2JRYl8y1NMW1s1YFemg8XTmfbMsRt5C6a98kFwJV-gOuKCQJem1V5vXCgdlgyrJ_gSW1KEDkDhvPRX8wwd8x4Xin7SoI98DW4_H5tT3Gjoxk4gnl4AYkfgLcGynHZfFLeyfSOg4YU2cMDyYGS3gJMLwX9-k7OWBV6qL2IVVWc0rjMuKpTrAdFd7b3XEAOfapNTeCL5QBPyNSdCfAf-Qryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94343" target="_blank">📅 03:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=Sw6P4RROAr31yFHA3k-NFfgpF2Ex2yDG4AVN1-t9dOvZ76EAjbnA28NPr6S7IRhriAaUCesY82iuhbXd1iNaZ1rEMInLA-FsZgQc0btokTdnfJn-igMKdITqCwApOHisSNcEcOQQNfE51p1wr3iu-8GpDEX2gxWK2e5Wgg_eXeyFFX60YJ7D7xV0N1lMxg3eJ2MNiTnoP9P9rYssr5-9tn-G0W3UwTueuz6j7Tso-Uo3hDRhFrfiuHC9DD5jTfsZrELQKqPOp3k5-uXU_qwK3uEiagyrg1X558m15xYFiuVYDYGijoAQfunLsUW2eqxrd95oAO8SdeSziaxv3qJ1iHr6JblbCcJzlrdiPJ1-KAdOe1vhhCO830pk9jrHrWM2-7iW1zauiVmSn-8_LTrm78TWOC7dfNXCIvY8OdBDNe2czLTt3bZPfnPpXYqzKdfiv34BHEWetrMWOOZbd3ayI-GGZMpBJcmcSzi4TsV4I0CjlNBrLQ8Y8xmu4Tudb2EHs9rdzjApi6Ldg5KiJnlPkKhVwrrU9kFYyiAvSJwl69BzAOa0zD-2mJXn7lA5F8f5AdsuZiH80YDp2j6XH1VV-qewVz2rtNSW6apEkFwC4pkhIrHNrP3kHw8yShxGvcRyJ8GOo0DRKVUXbqPcbcystEsNHJhIvM_rgXg_HZ0b8EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=Sw6P4RROAr31yFHA3k-NFfgpF2Ex2yDG4AVN1-t9dOvZ76EAjbnA28NPr6S7IRhriAaUCesY82iuhbXd1iNaZ1rEMInLA-FsZgQc0btokTdnfJn-igMKdITqCwApOHisSNcEcOQQNfE51p1wr3iu-8GpDEX2gxWK2e5Wgg_eXeyFFX60YJ7D7xV0N1lMxg3eJ2MNiTnoP9P9rYssr5-9tn-G0W3UwTueuz6j7Tso-Uo3hDRhFrfiuHC9DD5jTfsZrELQKqPOp3k5-uXU_qwK3uEiagyrg1X558m15xYFiuVYDYGijoAQfunLsUW2eqxrd95oAO8SdeSziaxv3qJ1iHr6JblbCcJzlrdiPJ1-KAdOe1vhhCO830pk9jrHrWM2-7iW1zauiVmSn-8_LTrm78TWOC7dfNXCIvY8OdBDNe2czLTt3bZPfnPpXYqzKdfiv34BHEWetrMWOOZbd3ayI-GGZMpBJcmcSzi4TsV4I0CjlNBrLQ8Y8xmu4Tudb2EHs9rdzjApi6Ldg5KiJnlPkKhVwrrU9kFYyiAvSJwl69BzAOa0zD-2mJXn7lA5F8f5AdsuZiH80YDp2j6XH1VV-qewVz2rtNSW6apEkFwC4pkhIrHNrP3kHw8yShxGvcRyJ8GOo0DRKVUXbqPcbcystEsNHJhIvM_rgXg_HZ0b8EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌ششم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94342" target="_blank">📅 03:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جاناتان دیوید هتریک کردددددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94341" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگگلگلگل ششممممممم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94340" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLs8DR1rD-Wl_L-jxTjzEWBVQTjyqT5JPsI65LMv2_eMnAwStkIXL1mFB0i4_QfNEHFl_Gfi_cydub7AgtLnZm7KTh1vYEE_vnxycxmOsJmGXm9xOGY0jYnlhxbZlxPxc5VH3bhzRTCgTxJYIgfr2KXIk-y6N5HPlOC8Ly77_oRHHYHdwWQhLfDaGQhyeHWAyPY9Qw1lDxQJeaJi0HO2oUTCuKOCnSHPbF02BCCU01ia-V7RRCFHYAe5KbxKhOl4WHTFicUGPX0kmngNGHJx1KyYg9XCR1xkBxa7RWe6LpXK9YT6jIYYIQuD2maMMyNq7ng17RJVzH7HjYre0oI2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فووووووری
؛ با اعلام تیم‌ملی هلند، کوینتن تیمبر بازیکن این تیم بدلیل ضربه مغزی خفیف در تمرینات روز پنجشنبه، از حضور در بازی سوئد منع شد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94339" target="_blank">📅 03:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94337">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQjTYPaBZ9IvDsDh5wwf9hDJknrhoXqU4cTsC5HtDpn32RVkhG1Klj6-R5QbND12VqgiBhY6pGsczkVb8PfQVrYQslLQx6V-fK7m2WuzEDp9Xn3hwb2PdTK1cr-ClxkjjT4N95ne4GnTiSAEvetXhriSP5j_oA4z6g8ndnp8ajxLUfL2Pr1GDUSAJrS_kc5TwxMhhpG8Rt8mjpIuksafZv_lcbnWI4z6jojfvcGnINWWal6XmvmBg9sYo4I5--sJ5salIv7OyShfElPYxH9T0vwyoauxqva8ZIAlu1ei9xOZ6AeNKCSLhbZ39ToFnyOWVW9nodkLgLUADtSfa1o9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxggmGsASc7F7q4RuAxp5J2XaLM6tXrvNrg_Ja9YMD6dM6Mvmtbn79LDYBlEixS70Z2iXYZeQdI7MCtDSBpbyPV2MPbNhwVQ78idnCJtOP1fruOnbuNQiJ93Tzn6UOMrWxqFEzyB67oe8ImzbB2PdDPh5Qw0MHJLWgiz-5Vjp_5-wxj7e_ed7qFQ706meA20e7gN7JepofOGJE_1u2C0AQyDfA4HJtiDriXmM5XBljg7wl3H7NldJ8Mora1K7X5xAzqsd-G4lQnz5UZ2l-EQ7r1acyBoTrGro8CHNZyuqKEQ8RG3A6EyaRql4G5ZSObvSsrJdGwsuD8n8WypmG1w5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ترکیب کره جنوبی و مکزیک؛ ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94337" target="_blank">📅 03:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94336">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3ddbc8ce8.mp4?token=mYae2dtgsg-MX9SDEKt8efdVXcT6Cqg2t7lHkjHuPNGOP2fTScE-ymTaSvgFr8i86FIXnN74aaGbTIHDMZYcO1TiPlFw7PVJrfSbjkaKcRdKk_zEizdnlg8xegr4jvik31YF-l7jzP29W4KdomnTphqRhj_ttxOvlC1M2Q7SsR0nCrogeKPLfklMe-tsSbcnaWFyHM7FNCgtfO1CMbn83Jdsr4bTA2E15EyN07HMQ9XHzVV0XY3ll9FUk7fVSH564I3di_t28VrztCdtF2McrrQxWhCKtgHquvaC0xLSxOaBDXhbuENgEXYNQXm-C84XoS9yHGkwI61y9EOJiklDJ6-Ag6mG2RqZVxps7LmXYs6qVXvm0vDNpvjtgIZ9yid_gi9fiT3wiT7TYTJ7EIN628jq_Hd9n3xWAis9XAWPatquxbcg1UXfCYZIeCryvenmCcip41ry5bbhg4BaS9ZXVFtg1OtAf735Rs3buPbm9CGK03kZNj042sRxqOQFP57PGmA6IWgD8p17QxeGCN29t4ncF4tNKHhI0GcWUl1z5GZrsiFb25yNOKUOlhACYj5ynwtrw9sGSPDohPzQAgNbJ13bitcngjMkQHFaSO1kqFt2AA75Lq8MgtWWVK1y_9eiQDGIO3rn2DbrripPd9GIbmj7WNbcJuGzkoO6yQB5r64" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3ddbc8ce8.mp4?token=mYae2dtgsg-MX9SDEKt8efdVXcT6Cqg2t7lHkjHuPNGOP2fTScE-ymTaSvgFr8i86FIXnN74aaGbTIHDMZYcO1TiPlFw7PVJrfSbjkaKcRdKk_zEizdnlg8xegr4jvik31YF-l7jzP29W4KdomnTphqRhj_ttxOvlC1M2Q7SsR0nCrogeKPLfklMe-tsSbcnaWFyHM7FNCgtfO1CMbn83Jdsr4bTA2E15EyN07HMQ9XHzVV0XY3ll9FUk7fVSH564I3di_t28VrztCdtF2McrrQxWhCKtgHquvaC0xLSxOaBDXhbuENgEXYNQXm-C84XoS9yHGkwI61y9EOJiklDJ6-Ag6mG2RqZVxps7LmXYs6qVXvm0vDNpvjtgIZ9yid_gi9fiT3wiT7TYTJ7EIN628jq_Hd9n3xWAis9XAWPatquxbcg1UXfCYZIeCryvenmCcip41ry5bbhg4BaS9ZXVFtg1OtAf735Rs3buPbm9CGK03kZNj042sRxqOQFP57PGmA6IWgD8p17QxeGCN29t4ncF4tNKHhI0GcWUl1z5GZrsiFb25yNOKUOlhACYj5ynwtrw9sGSPDohPzQAgNbJ13bitcngjMkQHFaSO1kqFt2AA75Lq8MgtWWVK1y_9eiQDGIO3rn2DbrripPd9GIbmj7WNbcJuGzkoO6yQB5r64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌پنجم کانادا به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94336" target="_blank">📅 03:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94335">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پنجمییییییییی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94335" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94334">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانادااااااا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94334" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94333">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Goallllllllllllll</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94333" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94332">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b4f64290.mp4?token=CQ8e1DwrDAyGC0MoQ_UfeWGAbfju-h-N-BxlQ3gdFku6V18MyryWDUmneY4cvnJbWqeDMwC8iXmwnmlI_ugEU0JpgldWC_m7EMZFjcbHH0EubwQ5H-fj_0faBEaYFj-BbYgo7YVXijx_Xzk-tDrQQQf02MQB2eO8ax5Yb_c3UHSmgJH1ZRT1OWgG78F-vBg4XyxQz-CKXRyeELuM0FzR1qcyAVLir7wsudaWYdFljwWrHt5llTDPPVoX20NBK_7sxULoZOCebgjz0UBR2OAcsI9yoCsXCpPgrvOrNQAvCER4HcGWz1rbfjIrp8NfNHccnyEQJySWCDAzHLW6H5uN7S-QgzrIl6BrffzKNWgKsvw8DQvBT58rtnVGpRh8IoALJq75xyy51AkV5pWuPwrwMkPkRi4rmp5SSHctkPc3RgKDD6iHUt5cvPURDI_qZEO6Ntg5v2CY2l8GRsnEF80o8pkVjGWO6t9MA7-cS2dfl30YrbwLESnqZmu6ioWnVqKBHm55PHbKSQ6NQztfMjPm9qZqbCTPTCATKLqfA96vmkZnmZixVhuhQe5fxWj3LtrSPmI8k11-vmcvfRGpEDkKJvoycllPN11TTcDZSO5gsfKW00piovv30LhuMnZ91G2xb9OMm3gj36VRw0WC6d7i_jXgE_nC-K1eUZBT7punr7s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b4f64290.mp4?token=CQ8e1DwrDAyGC0MoQ_UfeWGAbfju-h-N-BxlQ3gdFku6V18MyryWDUmneY4cvnJbWqeDMwC8iXmwnmlI_ugEU0JpgldWC_m7EMZFjcbHH0EubwQ5H-fj_0faBEaYFj-BbYgo7YVXijx_Xzk-tDrQQQf02MQB2eO8ax5Yb_c3UHSmgJH1ZRT1OWgG78F-vBg4XyxQz-CKXRyeELuM0FzR1qcyAVLir7wsudaWYdFljwWrHt5llTDPPVoX20NBK_7sxULoZOCebgjz0UBR2OAcsI9yoCsXCpPgrvOrNQAvCER4HcGWz1rbfjIrp8NfNHccnyEQJySWCDAzHLW6H5uN7S-QgzrIl6BrffzKNWgKsvw8DQvBT58rtnVGpRh8IoALJq75xyy51AkV5pWuPwrwMkPkRi4rmp5SSHctkPc3RgKDD6iHUt5cvPURDI_qZEO6Ntg5v2CY2l8GRsnEF80o8pkVjGWO6t9MA7-cS2dfl30YrbwLESnqZmu6ioWnVqKBHm55PHbKSQ6NQztfMjPm9qZqbCTPTCATKLqfA96vmkZnmZixVhuhQe5fxWj3LtrSPmI8k11-vmcvfRGpEDkKJvoycllPN11TTcDZSO5gsfKW00piovv30LhuMnZ91G2xb9OMm3gj36VRw0WC6d7i_jXgE_nC-K1eUZBT7punr7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌چهارم کانادا به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94332" target="_blank">📅 02:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94331">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گاگلگل چهارم کاناداااا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94331" target="_blank">📅 02:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94330">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94330" target="_blank">📅 02:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=hhKXgUd5OnBqe49uJpA2KzvGKdFyVt0IvUo3n67Y5EN8BQd3wMDdKG_pjZVfRRMIl9cy1KDpxnMO0XpGXHWmMmOZPP6aDEKy-j7ZnzyL_A5qA6QcvjtaWY-8MaXRoypwJgmXj5m9LXNGsn-qZbP-7F1zb6NRD93HHLn_TZgPRg_X3hA2H8ca_iUM0Y4zNyuN9sq2nv6daA6bRYVUz2SXjVZvAZIBm4Bx9CFNNYAaD55PyP2NmyRtUKgEmGZAentmjQUinMXw8H20ZpeHJd7Pb4BpJT5zqVIlJQLiRWEeEE2copHakutpQo6a_pKMXSNlMZfXndqWo30sS97vXQHUiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=hhKXgUd5OnBqe49uJpA2KzvGKdFyVt0IvUo3n67Y5EN8BQd3wMDdKG_pjZVfRRMIl9cy1KDpxnMO0XpGXHWmMmOZPP6aDEKy-j7ZnzyL_A5qA6QcvjtaWY-8MaXRoypwJgmXj5m9LXNGsn-qZbP-7F1zb6NRD93HHLn_TZgPRg_X3hA2H8ca_iUM0Y4zNyuN9sq2nv6daA6bRYVUz2SXjVZvAZIBm4Bx9CFNNYAaD55PyP2NmyRtUKgEmGZAentmjQUinMXw8H20ZpeHJd7Pb4BpJT5zqVIlJQLiRWEeEE2copHakutpQo6a_pKMXSNlMZfXndqWo30sS97vXQHUiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/94329" target="_blank">📅 02:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcTnPFCAYBNd49MR-LgqMBHR8Z0XDQ8vvEwUaxOotu2XmNaAoFNXHhgpzdRL40CCbFd1cOkFn0Sz6Fr9gmlEAQKAvOg7tKJ8WLkYGyNv5ULdygBksUCDDLJRy5CDOSNgU7R8EBupYpM6VrQhDbvWW113Vrv7jkyA9U9ZQeNj78TrjExrS57WAqNeZ0k3G9xj4Yl8ZoVrXCL_sNVocfGVkXIYTEDTEd3t1KRb7VnWC5tBwV4bsidR5EHHxijxi3E-9WQzxfg6gh5FcCZaTaOJHEIRWBKqeRgsRzmcwzMPy9m6V8nruji3WlA61GfQKh7VkLWgbOJ3AuRuYY8k9G-gVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش قطری بازیکنو بگا داده زبونشم درازه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94328" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_PtveX8oPnrm679Di2vJ1KyKo1H8EvbE6TLebQ2yjZwJayaRem2BRJdbAQz1K7byUvtylZP2xFe_cDcC9a8arzEV29cZfsAOwOR23jxZoqJsCdt67LlQKHs1LQkGJhBgCelJqHDE6dOPAzornE_W5LckFQ55PKO9UoqfgLEJIqQxgso340mFLQEO4LVQSilrHbDeDAtBaD33O3cSuv8qFlzTj9TawWnvGZE0poFJ7b296Zhbrtjn2Ijnj0qz_KlXKl5mgnsChgj47Et91WhDvXXcSU6LPLUEZ4Mfap-IrxQT9sXX_TNKIzHkmgwPxfymevPRJ-sWlLS-retpiT-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ریدمممم حاجییییی شانسشوووووو
😐
😐</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/94327" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evm1lJvSKP1Fh2l_hPdxqmiN311m9arTYBn8lG4eqgOb4_w2MDatrGfvrxvuKLJbYsDaBV7uw78wNC-1z-cl2N_8fncGvMP4VhnAHnbxE6OlTkoOyd153XNO4ukOLB_0N8ZXUdxW860a7NZPbDZz66nkLsoIuy3jiEdgckYnu_GNtXG_H8-CTfkphI6TcydTRxFo-r13vQH78wtRvHQk11ZVmESkLKL1HwChRV2nlIR8B5FdKAPCGFkXeqcOehJ3X5-FUuf4sEA_03Pmhw2AcJff7DcdsKihawFXG_uu8RRDcSYC_3YipuYBJ1VT6_RprzVyL0r-kCyhdkmzONz0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شکستگی پای بازیکن کانادااااا
دلشووووو نداری نبیننننننننن
❌
❌
❌
❌
❌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94326" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بازیکنو با آمبولانس بردنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94325" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBdDV8rvzb6QxAWrR2csf0_IMARgkcytNmKJgs_5HiJReg77wbpGEwigfG5FsLKr23PfqkNE21tUQIsn4ck5DbsUYxvDpkQuiAJif0VKnOspS0NTNDXwF2_QTgplPA3P9QzciKTB5Gp7ucCFfr_-l6H8hPIA3vZ1WJbDpCcI-OsRucWCsMPReNZzQTe2jTdrBHCYbNGqNSB-tirLXcLvbidGWyLxCgycW0t6P5pZmw7usXPR9IIHpYbOUB_6oKI9wCKReEOcsTqsdC9yGTnBpDBLdguhBfXSjvCvJS4qgDGYCoBbL79Eur-ll4rm0g7oyEkuR1p5e4DeDUCm4_Uvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دور بازیکن کانادا حلقه زدنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94324" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🟥
بازیکن قطررررر اخراج شددددددد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94323" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
😐
بازیکن کانادا بگاااا رفتتتتتت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94322" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94321" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لحظاتی‌پیش نیمه دوم آغاز شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94320" target="_blank">📅 02:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه‌اول بازی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94319" target="_blank">📅 02:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvEpAHtgvTWZA-i1D2UVubnvVkWB-iqcyHkv__G_KvaZDdreirxfDGTKRP5kIiLwJCVEhuaKrAqtXsfKocTzfqzgvXKJXlsx0hGzsTkqjx6_0rjbt9JgO6_uo-lVVMQ6g-ZVBI4HMx-5luB6d0qziUPbHzYdKYzgWe_8HuwnzW8M3uH0Q3yY2lq3YJZ0wmVCynkFOz_T3ezYouJDvwnIVCIv5XaxXplomrKupxiLNSBnmwkMIRw5LIVwJnUbHh4qm0PIbOfpEA0fecboCvB2TjE6lpt46_kDAFs1z9ipVurXb1Vrh9XhhG8CPg-Upr9dWyLm-ThJXZNOjq12Bxh9y3wI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvEpAHtgvTWZA-i1D2UVubnvVkWB-iqcyHkv__G_KvaZDdreirxfDGTKRP5kIiLwJCVEhuaKrAqtXsfKocTzfqzgvXKJXlsx0hGzsTkqjx6_0rjbt9JgO6_uo-lVVMQ6g-ZVBI4HMx-5luB6d0qziUPbHzYdKYzgWe_8HuwnzW8M3uH0Q3yY2lq3YJZ0wmVCynkFOz_T3ezYouJDvwnIVCIv5XaxXplomrKupxiLNSBnmwkMIRw5LIVwJnUbHh4qm0PIbOfpEA0fecboCvB2TjE6lpt46_kDAFs1z9ipVurXb1Vrh9XhhG8CPg-Upr9dWyLm-ThJXZNOjq12Bxh9y3wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل سوم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94318" target="_blank">📅 02:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درحال تجاوزووووو به قطرررر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94317" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94316" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گل سوممممممم</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94315" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگلگگلگلگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94314" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قطر ده نفره باید نیمه دوم کون بده گل نخوره</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94313" target="_blank">📅 02:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94312" target="_blank">📅 02:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh79O5maPIX57m2p1CC32LdHYg_cEFmg4EgGsVBebbtrNoVK1B5JqVfu1uOLnQvFHgPX7pB5r5WON8RsEsVFJHRUi_ysyUmMrbXewLs-d-SasISdO6_WKPoLG2imUUaYa3yRkOMJTOap1unLZ_9ZuJ6LvPr2fn9hlFney5Srg_g8fanZLu0z83ZyKQPRbLBGoiVB_g65sZTt7OpFMnLa5SnmjrJhewrypWgYqnLs2I0ChDZBvZHiRDJAjjw8710ntTpdTHhpgqkOkB3V8fg19n2Je2VGQW3coblU6KdmxBPte1I_Ch0SbelSHEtdH62s98zC7tonWvQ828YB5nMXofM4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh79O5maPIX57m2p1CC32LdHYg_cEFmg4EgGsVBebbtrNoVK1B5JqVfu1uOLnQvFHgPX7pB5r5WON8RsEsVFJHRUi_ysyUmMrbXewLs-d-SasISdO6_WKPoLG2imUUaYa3yRkOMJTOap1unLZ_9ZuJ6LvPr2fn9hlFney5Srg_g8fanZLu0z83ZyKQPRbLBGoiVB_g65sZTt7OpFMnLa5SnmjrJhewrypWgYqnLs2I0ChDZBvZHiRDJAjjw8710ntTpdTHhpgqkOkB3V8fg19n2Je2VGQW3coblU6KdmxBPte1I_Ch0SbelSHEtdH62s98zC7tonWvQ828YB5nMXofM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌تماشایی جاناتان دیوید به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94311" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94310" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94309" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوووووممممم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94308" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94307" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=ar2sH7HYzpMnQegrI33gCAmAE0uxTJ1JkpyLzMg9pXtmeQxT4Uacgbl4tK0uAPAqaeG8b2Wzw5zgEGWPJtq3DBiz_4S5mbDzqvZNn_gMXk7CVPyoYHEP9p7lVAbJ26sVIZlH__Epi_uyfVb55QZMcyUfWr_URsPpcxiwbKduGpnv4Sd7Qr8IQ0fEL34fkI-NU2wFzJ2bs9uWaNVxg0fITNJQ9DhGaasKZMQklzWiSF42UqxgbfSgAKZMy6NgdrLj_sgMWkGKjxz8P0783HlaC_Zyypo8jjsmQy2mGpVBAFdHTZUN4ayJZTHddJF5GGJa9j8IFAowpmbdftCxu1A1lAn40XIf4GIddnT2kZbL7oIUwSyIeSJoD_IMTSt36eG-mXqwHdGYchlYenp_Lk4Sfc1E7dPi0LpcPj3iWsD0iH-EQlaWasjOgvZljUYlh8TYk7cz7_dFb4_ThjZ3YBCtKapUjOyg1jj7hrJqqHdIKwMuRdXww52T6R-th2p6axy6MH2Wh0ilTPIwlZZ-T6MkjEKiDqbigqJHf9lMB7VvSzZcr1Db4H2bpDWNm4kWWckShwaCTDVZeWJ0fDJoCzYiZnlin2zt2aYn6xb8qox8OmbUs1ZFLjtM7F7yvdPe3kR7sr24lW1UDE4rQg2v7_W2dihek1qwiviWQUeelVkljK4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=ar2sH7HYzpMnQegrI33gCAmAE0uxTJ1JkpyLzMg9pXtmeQxT4Uacgbl4tK0uAPAqaeG8b2Wzw5zgEGWPJtq3DBiz_4S5mbDzqvZNn_gMXk7CVPyoYHEP9p7lVAbJ26sVIZlH__Epi_uyfVb55QZMcyUfWr_URsPpcxiwbKduGpnv4Sd7Qr8IQ0fEL34fkI-NU2wFzJ2bs9uWaNVxg0fITNJQ9DhGaasKZMQklzWiSF42UqxgbfSgAKZMy6NgdrLj_sgMWkGKjxz8P0783HlaC_Zyypo8jjsmQy2mGpVBAFdHTZUN4ayJZTHddJF5GGJa9j8IFAowpmbdftCxu1A1lAn40XIf4GIddnT2kZbL7oIUwSyIeSJoD_IMTSt36eG-mXqwHdGYchlYenp_Lk4Sfc1E7dPi0LpcPj3iWsD0iH-EQlaWasjOgvZljUYlh8TYk7cz7_dFb4_ThjZ3YBCtKapUjOyg1jj7hrJqqHdIKwMuRdXww52T6R-th2p6axy6MH2Wh0ilTPIwlZZ-T6MkjEKiDqbigqJHf9lMB7VvSzZcr1Db4H2bpDWNm4kWWckShwaCTDVZeWJ0fDJoCzYiZnlin2zt2aYn6xb8qox8OmbUs1ZFLjtM7F7yvdPe3kR7sr24lW1UDE4rQg2v7_W2dihek1qwiviWQUeelVkljK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به قطر توسط لارین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94306" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94305" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گگگگلگگلگلگل</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94304" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
