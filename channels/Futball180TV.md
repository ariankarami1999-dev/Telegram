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
<img src="https://cdn5.telesco.pe/file/c1-UUzRPDMFrpp37Aitenah-07p7dfFkpTx1A6kUPIDn7JMtW6-bjggYRcZZXi85beImwQcNEQ1e8q76v7bf-662xcH5Q_IH2fEDp781lsSLpw6F9EUrPTj8H7xVj9fHtCE1v1S5LZCQD8Im712MoA2JZyjhRWq88mpcxG5qRY8Qf1zoQxUy1bsfbMzNkWRQG0Y-TzN4rDYsp8d0eZJS2ZBSfLY32FudILw2B4VqOrEVnHvH4J5AI7w46ENNiP63GhiN8VLUKCQ-x2xg1LUsWAL7zo4au_PF2GVaeh3sV4taxUZpFpJRrHQWC7U1Dk496tLjxxhSJUQMNPOM_EJ8sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 549K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 11:14:42</div>
<hr>

<div class="tg-post" id="msg-101416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd52d97f.mp4?token=Ud-TiYhLHiobie1hpxl_fEAWQMqNZhxGtnCyMzrO_P0H-mudGK2eiM9apc2A7pjt5lSB0tLYyRLTl6NPIyAa1v52Xc5uj5twZ-9Ebwvx0hJ8GYlRXTmhJpOmARZ2mv9xp8rmhC1TtC_2KC6T9aD7VSRndwKco3AqZlha4azSlE71kaBVvp4aPTfiwEpVPl8SQJzieuPaFcl42xfdxUQm32XCP98nD_SuTctrfew7Fh77Zi1LUxs6GU7IVXZmtA10XYw8F65SqWFqdJSjlc22Ampiga0nNiHvNDIdWPLkqhTfNxZeWcfDb12IdxX0wtaHL1Lo0N0dsih5YSDr0UdI8038khtf4MTisMnQHiJByY8F5MY_VOcVRZM5t-AeP10LH2a2XhvUbDcsvdWDlrSwRkFSx7Dv_pEyrDP6LMj1rDKeC5OCffolNbVHGLt6hNV2g8FHOGc48LK0b_BHZ3zOPinwf3eWLCdhg2TJpn9EW9gUfTkv_amcnTDNzROdBGgzIAGSd6_38SRNpqZSl8N_vYgJHHgIQyQjbYB5LbJ5aMbyXTAi12Vq_sNuqybRk5u7QykbpPENssv8JyQwp82NLa8d73KUUeRv438E4jd12UNpQGCtR3SrJRRNzo9mEQp6AfdvfCvPtRlKiipmslLXbla18nVG_zVZdr8-LVpe8GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
پشمام بنگلادشی‌ها بعد باخت لیونل‌مسی اینجوری حالشون کیری شده و غش کردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/101416" target="_blank">📅 11:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhE8OSHk4Nb6XbG5v5u-gwLAxIYPCFQ7TbCZ-k_3d--VGa88efE-bf0PAm665Xd8LTxnEsmZ-JjEkIw20oH9yIPIIhU1zMWoPQDbDJhizvtcQnLs5RRs_rSMAqk4v7ucN_FKZI6z-fpoDXUzgB86iqQOnRAhQyNr1C5YbPhEVvlrm4s4Hv2BkfEOQgTUfs_ZCoENnuSdLRHl8MNT78lZSDiX5wevGCSNB8kMZcB3TtNknahQNoGV7SAaIZozhB8rXNM4y2ekqE7FjLsx2YM4BFsBB-uH4XzEgfKUr6m0Kocr21nxeRx5nCG_qDYLVI3xQDKPSUs6kb1YfHvVG-EXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استقلال در فصل‌آینده لیگ‌نخبگان آسیا در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/101415" target="_blank">📅 10:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a52a115e8.mp4?token=FH5Mhq38mwbifoxDN9cbIpZJb-YG9rHwL7ULHEUJLGMBGsnMZ9SvxxKzfgSWvSx4LBFVjOf_ZKsWuD_EVIQtyxc7Acbm_9rnfFWqyJb4aPxhoXVqXBsRLzZZnQvK_1tkcFZU1p6_KkM8LpLwP7TI1gQ0jpxptMvHjLn1b15WHqS7PkKVsN7av8kqbzQyAdpEXYy0mqOm_BshX2bDISbeQ-31SyAGFBPa9UwPlw86cojoUxWBLly_tkZfpCIp8X3PJ_cRF1chp8iWQVNxrJ3Hsy4xH33xdl-2n08Cb8y8NYCGuDneeZRTxYoD3XGNE0arQf5u9ewCeRgDcZOb3ZYxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مراسم ختم مردم ایران برای لیونل‌مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/101414" target="_blank">📅 10:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBklY2l9aDpAREKz1pamfdEdc6X_BfVt-iPiKiY6z0cxIZ4ndreKyWepBZMG2_IbiCULFBorWIdeA80uYYeh-MLsWoxQ2Q5vcOmU1-zjI_gBLR70QJyX5W8moTi_jutX1ruhspVwJX5JcRZCnE5A_E254pi_537usW4SDv4sxVC2c8wkGgs8p9G7NQd0YWkogATGIQxeHEOWSlIKFIxZvxq_XgZDUOlyiKDxpN2MTlASB_AVHcnXQd2e83s1NnSU-dtLYsOD7ppi1Qgq3IImbAZmgZEUmdEO4FJafAdD2SBqmohQgx82I_Q40SZ8dA5litF3FnoGblnFn36eFGzYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لوکا مودریچ در ماه اکتبر از فوتبال ملی خداحافظی خواهد کرد
بازی اسپانیا مقابل کرواسی آخرین بازی او خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/101413" target="_blank">📅 10:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342ba6a359.mp4?token=so-Yr_imqOG0cXiVvapEc2cyA5f0iTuZBEGrhJF71OBPguoiSc1gJs0Qo5vKbq859gYt4sKnNZdQ0PissccmkwFn0J6QzmB_Y8kM_lducnh9my2472oNXUA_pTAplNFVvkrZeMxnTtPXFfJ1BNKhH2ueMhdgSsdHPOlHIJrl1Sf6pZe2zUodvBeOFz8sD_wZh_te0p1z_zSol0PkuVYPvmcynHSgaGDVlunCHXzQOSVTSeRDN46CrOwEcEKAkCO5l1DrJ7DtlFFehM-G4-gzGa_o8Q5nlhe0PVuO4nJtZR7cBA22NKK1ZPuy6b1IjY_GOQSguCfcP6c6xmgAkKdASg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
همزمانی شگفت‌انگیز عصر مسی و رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/101412" target="_blank">📅 10:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061bd5d306.mp4?token=aeS9Lyv_L6ZS23rARYzaZqDOJQRJodYVeOftWctu6B9vfvcHEe4aeqTzqJIkekbvKaeZn2fqbQiuDZmZEYniPv0pq4ROE87D-hLY95kgrtzAcqJFDwDhGhlT-itlmKsCUwXd86Ouly1zOdiY50WIvzUmXlqDkWv36Urm8GkfHQRr4lldqrhwcEwGz2dFtkQUiSDAa6n1cwGpDAbJH2axwX3wcXTozrsaOiYZp_A49o0aMvXUhw--LikC1JqyZMm11vklnYlxY_0I5ey-T-R_g-h0bl1fsTllDPeHe-hxUqOTNfFzCz33dDWzMF2EmkzcX0g_OQqp07vTbqAiNIQwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
استقبال مقامات دولتی آرژانتین از تیم فوتبال این کشور در بدو ورود به بوئنس‌آیرس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/101411" target="_blank">📅 10:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔥
▶️
اجرای زیبای شکیرا از این نمای دیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101410" target="_blank">📅 09:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
❌
⭕️
سروش‌رفیعی با انتشار ویدیویی رسما از تیم‌پرسپولیس جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/101409" target="_blank">📅 09:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_C1YjHMJrHKhAGOrGJsKfkVa98VjBF1YqgGTMIp9jFNV-CGfLARK6PrTXEtR6X3HWPqlqZpvrxSSICWshj0pa6aT-VvGIScI2MIBem4pt3aM0fy0OVSviU_Aaw9a7pHbAHtvvuIyCFq-DSFjk_DjnC8Ng2ryLOq1MDeR8xv2EwPWq4gPTHhSFjDw7SPofj3Xprxm4J2-a50FTRXf5Dd9FKEFxeJomB1rzWBjH20ZR07WPdk6LFM-SdnO3DjFQFggVslq-f4St_SVx79vs27rH_4MdMXZbBpeaNvvkR3oMS-kP5mPB67s7N34IE9Da6oHhZoq_CVS1msflUEe5B0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برندگان جایزه توپ‌طلا جام‌جهانی از سال ۲۰۰۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/101408" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18768f80f3.mp4?token=fAHad0-HUOVOwegMn6YCKg9jPeTQ-uojQaCggqlxqZ6Fjok1JRKn1VfPdN_rIIuK-HCvcbTUsRxuMHPfS8ehtBxpc1_vUbrJ4V5BGrqJVIjmiyOK8EM6gl3giBPdJknkn1n6tZVIKfwgfAI2TpMWcfUpNxAj_JyTj3pMvYWDF2W9VYkTGkcTaS5pDgEVGHok_vsRgFhskwqH_6W2QfprNcuo4i1dNI3fPNsxrleN5DYw4mKz8FKrahRJnVcK5LKSqkSye-5xn7DJgqx4fbrA2RB4Q6JkDv7RuU2XthP88NWDKUDEx_1ttqLMBH8jpoCnKNqQ9Zar9_8y00I7_EQjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
بسیجی‌ها گله‌ای ضد مسی شدن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101407" target="_blank">📅 09:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33df2c440b.mp4?token=lhkDlNjeyAgOO4pWvo835QyEno9etR7weAzSBm92nQZ4AagxhElqgkxGlinM2o8nMoFW5fgXuqXT2MGimVi7CLLZxSX_9aRNHN3XI8CqPLunbdF7rUnqGl0Uyw9Q1eDVxTaofyAjoY-StTzSXTjFpmFOez6itV5qLgfTUHxT0LdxQlpZubI3zyBwTh6AOBuB5Ur5q8VUe9IYxsVtOJeSggF8_VTYjX3kqxHhTW_S411H50MyQS2eZjl4SNXcye4qPeBa8c6ZCc3PtK8XOiln_U1AFk6T02Nc0rmFP8SZ6d6corLtfk1OBR-QwAHWy1A-Ex4HkC6nAHwboJ5Y3jCJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال وسط این همه آدم تو جشن قهرمانی اسپانیا شرتشو کشیده پایین و میرقصه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101406" target="_blank">📅 07:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30588621a9.mp4?token=taGnY-Gl3Rxtx4Ta07ojiVPV7JLeCu_udcguzVQ9jBkq1T-DNli951Q5Sr9wNiJO4AAaAL5hC-T68njsHxhh9X1wY35vy5PTKsrzC9XPC_Zz50XSA94dLN8NCmGtnMrNJXbHamVfVpvNHBbX67ssHO3eBEtjIM4gBPS7c8hs5hia-uN0e27sHfJe6_c2FFN4SQMDuFWICBq3JF2xboT4uMfxE_rRVItjwYpcCa_CMJnLGD97Xeni7Xc4tL7OymQWBOLwQYzJ1_igQRj6WGpOATL9UDs6bFZQg5Vpz3tBYnQIPhIgC0JEIV9QCJZJcxglvVb5Wvw1sjgUDLCFB1h5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤣
ناراحتی امیر قلعه‌نویی؛ برای اسکالونی کلیپ ساختید اما برای من نه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101405" target="_blank">📅 07:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0EXmPwpD3G_Ue1tPHM5nKKlGPj2ZrRkZsU_kZYuHh60Eun0k6UgnNykpeOYQrhVFlPyFbk8FWdny2xWyao9_YxsE9nfV4-_u6Ha6xAdStMXwKKAsTQshvNubJZlneyTH3GMGzOyPRvVaOpjWG-10J9Xr5R20uzayvoJVrzYVp2qshNapvvYw57fJ9iJWR6F8OEXDhpuFcOVZxsjlF_JftxifQF5BgrYp54KaeRlNUqe7imDxoNt1PCuvylT2AAmIFFhaVu8yWrR4-vNRSaR3qyqDdglhkxYIgdpDXFnhBXmlc8axWKXu6U8aIhi5pEWqqaqw8BQk8nvBrWZ79eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
فوری از هرنان کاستیو، خبرنگار آرژانتینی:
لیونل مسی به هم‌تیمی‌هایش گفته که فینال جام جهانی، آخرین بازی او با پیراهن تیم ملی آرژانتین بوده.
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101404" target="_blank">📅 03:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvyewI5ixQmqRX7NKfZv90GAp7pIVabUdetDf99rP9HmA5jZohN3lBuUI0lGlGxd_QZCXl0P1v2nNJl2h1J0COt38etQrpJqb591HkPpwrtnl55soPyBv87SSFRtfYxgQH5GsD-WjjQG9dfg8pVqQK_YATEMjFwfLgDAKILOekB8lV8c78QV6iLo59B5lSq78kTlRJgswEslUc_yLqeVujz5OTufK9q7FO-4RZnF2hqDyTpog9iYDArryrVIeDgw8929IeSZYaXDB0SP_-pr3IMasEMHMnoN35_lpcaWfM_bxP2Tf_kicyNlYBdr4OAGcHNOp6mLmOZbvnqxgiwVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
||
آمار و دستاوردهای ارلینگ هالند در دوران فوتبالش به مناسبت تولد 26 سالگی‌ غول نروژی:
🏟️
[419] بازی
⚽️
[359] گل
🔴
[66] پاس گل
🏆
لیگ برتر انگلیس [2 بار]
🏆
لیگ قهرمانان اروپا [1 بار]
🏆
جام باشگاه‌های جهان [1 بار]
🏆
جام حذفی انگلیس [2 بار]
🎖
کارابائو کاپ [1 بار]
🏆
سوپر کاپ اروپا [1 بار]
🏆
جام حذفی آلمان [1 بار]
🎖
جام خیریه [1 بار]
🏆
لیگ اتریش [1 بار]
🏆
جام اتریش [1 بار]
🏆
جام اطلس [1 بار]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101403" target="_blank">📅 02:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeXIoV6UxCPplFkxZ1hde8Zsh-2ka7TfHTBYjb8LZVYtX0ShV86n5c7bL55yAdNHCKSlbgEJAlGATrLeoQdkMaU1qNwXLrekbXMaqD6Cd1Rb8r0u8Zh70z_4_KdvIkeJflNBfT_UM3tMMdo4fmFxmVsiKEQhglCq3gOASNHC4qYe7jAucnK3yF_INvBOxSPDPJWQztmI-vxJYRM004kbvJp65IsAtni-S811Kvd881pPFrwBbsnHI5jrErMAiGqeMso_W95l1bjJwA6EKr4er5tn4j1uYWtvPEcsaNq1Mv3Dy4OfirFpHnh6KWsd8zIp7Eh0Dlr1a2sbXZV9CvlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
گلوبو برزیل: ترکیب بدترین بازیکنای مطرح جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101402" target="_blank">📅 02:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور:
افتخار می‌کنم دایی و باقری با یک تماس آمدند؛ یک ریال به هیچ میهمانی پول ندادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101401" target="_blank">📅 02:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoJINYBMS4dm5CKx9MnrnR8BPL7sfVjIkjm63_gWapR4nIFBKLNFgd4pbhIY0lHEboRHmTEszj5DG1vn92IO3ilozJ87lzWrcP7QsJlE0gnneWszEqX0q1Ozm6ECLiAR6eOzlFyKY_UwGVWcIwn9KALnPxb8H7n7u2colGvFqfjEhMm_j6COlqFowCecd5KzG3k2ZGHz3O4rNYH0rMsyaZ_afB-aTSRmzGmXIvn9S_FEprsiPhvWFzwn-wFR6wjf7u6OwwEwM3ZfHjiYRxTGVvsN3hA3E3ULm9lKbkpVnxtNhhb6As0_Y7ThHjCrdtDByHySjV8VLy6tkY_E3pVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
اسطوره وینیسیوس بعد عمل زیبایی در برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101400" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101399" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB63G7uwgaIwLENKyzAs0RxNEbww2GgeFci45S7OYN3mwM4_P1CJoIJ1nIsgM2EmisXi4iS7r2v1k0ecG61i9lIkmD6em09kwaObLDO5z-UcDsKmK-6CH0_-HEVQlAYnCDSHc-TnWrNlKBCykHRFRLvFqnC71KHLEQ4ewLT3UzrnQqGlZGUfjNVtCVBfxX3NqnV7y7qb4mY_ozzx2gh7c7nD--qccXYPdrS1FsJSNqIDfec2eNfWZUVA1dXkoRxa6HnFT5Qlczd9ZOzlafjVOQkrNqzcP5AHuqwUGzM-7pk8L9yj2N7fkOOJ2SjjBV2yA_L1bOqtpKb6OdVxffg4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101398" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e202619a75.mp4?token=ESnzJg99IThEJ3xn_lisVFnyi8cMRj8ca93cPYWaMewnGk-v_1naB7qgb56NKvcPiI6a4G2BDHstDlUKzz-d_Vt-9e_6rGoZGgHEtQr8fIF9jV37l-ijnJ4JyndXqolotwqskNFEUCB2nl5YkS3UUt30mdgWhIGUoH9zNzxxM7yCzZ808hli5zrtWol7eYrgd0mrrRpoIn4-PfEG1wltSTu5z17tv0sb5Usk3ClxuB9i-1mTNG7iD9b2pZNY7ACQelyJV5ivfDZ6n76gULN_gm-hu8MnMOlZx2D0mg6DpKGMqD9G5XpIfhidip2cwj2P6grPWyRZy91K-bJ0PV_jOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
عادل فردوسی‌پور در ادامه: من بله قربان گو نبودم، نخواهم بود و نخواهم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101397" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piLJNNk7Zbu9fZg8OQj5X9_c8DuXIjBMx8SMWhZ_Xs7IuzjJ9U-F3XpS2ax-AVFPklcrsukDp4W9uC1OZVi0rFx810TA5nM-88U2jjA25_mjruCfXfg1keXrY_7OvSsBJREnRyciRh6idZNjHbDLeseKyP5BzZPLbzdeMzwuDw4kLBDarF8GC941hKoq1TOQ9AvvH86xcZGCy4DjiU_R-59RJyN00ztopddEeuE9KfdAF6euXT1O4TSIOXdAuB0QPylDxMfCPjmstMFlw26IOHMH8WqsXtnddwglqqa-Afo4jqPZlRLWEUVJiNMVVGa6W0frOdXL6NczjcFov71RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر قهرمانی اسپانیا
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101396" target="_blank">📅 01:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a7fe008.mp4?token=k134COIgGO5zKkB5W9VmCZgpVA-i__PmKqsJcopaPMD724Ocf7o2SjGdpWn75_X8kJFlDGVqkeEZIkmqbimKGhrik_Mt4_tsNP-ayB9xmxv4gKnQCR1D-ja7uV63pqZLI2EIR8GrKM7au9nrBF19cd-R-c3RS6SEozaRk4SVaHGPnUcUYn0Sbpj-TQxDhF9THNm2nFmKomlZFc4YRs6sDC1fE0pSoPpeWtliotc1CGfP9OZYKpiqDtYjWK_tqh8gGvAdNZ145NlnNvLsY9YUqwE6CFwfk8cMpjov9DJHxot2-tA8GTrIHQHAv-gzsbVlBwK4DhyFVaXz8OIZ5rY3og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101395" target="_blank">📅 01:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
👍
بغض عادل از صحبت‌های حاج‌رضایی: جایگاه اجتماعی با پول خریدنی نیست. در آخر، تن شریف باقی می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101394" target="_blank">📅 01:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101393">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_yGSMGE3yDwYxQXCiTmPTVFSWUnsyucEy342YJONZvM0bziSBAscGd1Y_pBSornjiCGAa3olgBLWi_0psoxZa_kiodYSsBrknPtuays_R4JvuW_goUeOw0TSD0w4TrwBZgJk1zrG6FQ3Pezpm1C96E8fOrNo_uVV2vjlN8Jm0H4k2CN2LRwk5SxnxOe3O0wGsrwND4ZejVr4QdKk6u6ZikTDiG7EV-wz8F3M502dBpBhih7yfUkN5kPrDTeWEuHhhmgfNstuDLobJ2X6ChjQPK9vPbq5FnF8GkiHJK78APJmDbCpk2czKFhce0rmsA_kssY615FCyOoDjWbtoTwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101393" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ4Uw6cKs7zoqB7R-s12UzxUNeHFUbWDBfpUqwmE7UonsgrD3uRx6i7HuYC-croQneOAVGQXysWKIA0jNZ1L5_4hw0Qijy9QF8VPbE6yjYfSuY7y3QIUeD0Y5XmPB2dtPFt3TBqbsUAqur28mRbjJT3zbnBY1WfUoF8_t6z8rcqTOZjLEoEJTfnKf71y96pXzz8abGjqohsBvPLVXB-urmHRgsQCYVNiFpd8acDd-o2fZu9apZjfhwBm4CclcM-4QnMQG1-bRrof8cP0SXBnZ6OpzYN_MsLvHJKii_ttZ_bsEPb1NbtjvXKxHFHLZnhlu22x8NT4UK2vjbHSzq_q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دی مارتزیو: لوکا مودریچ و میلان در مراحل پایانی تمدید قرارداد هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101392" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gen3bXcTbluuLUVuVIR0CguPv3Cj5XQlLCE0MuoR5zO7R5HK_fHlhinle7gj-QCzkzNmSuvBSnRzzo9RA5Uj5Oy-D9eY4NvJ8aKC3QQoC1Fm_FIACQd4_3ptnYMI7p-KrWEfW4IFozLwuIU8W73DzfnHQB-_cr9TfKhiVN5sayqTkvjCSUuQmG-4yTDfgruWkoVph66PtdqldalcpuNivuHL__VMqDPWpElL7fgAo27x04dxLQYyZKRTN2WiPN3LlgR8HzRMrWrY5oq8cXugfWWzJFdij-76UQI-LaUIVbtVBLj_zyf7CFYSiqV9_AgQTqYj3FACxvWW15dMup5PYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کیت جدید اسپانیا با دو ستاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101391" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1fa4b0ee.mp4?token=njJEW6_s1cZDYgRFca1QPZj85ZwJcEbvCGR-bMn41R2DDT123L6clH3OxXuypPsGZxnYgxu5TnaFWKblBbU-embztgtniwEHqSFyNZporGB8-7p5HA6nFLRFbz32EHRXQZmwRaY8qamHIablMkrRpN_rb170Lv4Xf-pocUUFRpdWENPjHLgE6Hyjcy9TRHUztuTOhxRJcQvb7a9tPgLEtM8ruRQBiCXkJ35G0l_ayFjkoXFZl_HnjCVOawnhCgsOPxGmYcYyqz3gLM76Dx8YoYBTcOxqvq3iyJQiBYPFgtnhonr1XzOfxN42g4s4K2OFKxSrdnBb8znGR9ZJ0_Wc6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با صدای معروفش در جشن قهرمانی
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101390" target="_blank">📅 01:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار در شیراز و اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101389" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101388" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IQTrKTjkF0JVSGs1PIr1fEOSvaqwO8H6yF8jWbdt72fTBX967FeEKzzIMHK1zmVFJE1J2e5ynlKkEc9UIpAe5IKPQ8SYZbtGFbKhKCoXdngr5mbNya4l-3UBpZYXdNY_sQ8L1jzmIcm8L1SglpnzHcI5NNdGwvXKf5Spt-FG8I4N3YR0esc7pPLPymvvJ0wfkt76M_2jiQsoh5M-Egie0Ysbnf84hN0RZIEialFmAj2IpVWbxoN5e-5VCRRcgRBw4ViG2QZvYm_VKnCWcjqJCBZphNI8a7eSaF9zbe_F6Z9u7S_ACys_tVGWG9CoqYNxjjoZP9_8Q4Ep57VMG1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تی‌ان‌تی اسپورت: فینالیسیما بین اسپانیا و آرژانتین در ماه نوامبر برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101387" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr5JdO_Ax3qMF-XBQqtT-ViCprHSS5hCsXzhmJ-ls5aF1co5ug31G_wSUhUxhrFby67TlKuIpu_4tKZ3p-pDdUtqTBgDcu3EQsfUEF_BBEo0OMTTyROyTHpGOP2AeTUwQ7UQfbTJt_tIsYSGfzAtwTnsQTp54KtO8f4xexy8mC89duCUwnCxmxgHdKNIlJA70mWPIIoxjq-g3UtrIe5yS-ZlKZwqNdeAJy8m8EYOhF_HvOqku7v5ivJHGK_Q8sEtQ7Rqh-PhGLTQMHuHuSaJf6xpjM2ipLekQPfumbjgZu3JV4b7DoCkjzxcAwYL1vsVmXk_ywDPJMSv8fyS5fq92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ پشماتون از معجزه خط دفاعی اسپانیا بریزه که اونای سیمون در کل جام‌جهانی 10 تا سیو داشته و کلا هم یه گل خورده درحالیکه مارتینز فقط در فینال مقابل اسپانیا 11 تا سیو داشته
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101386" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrq8i3UpOD4hbP0PwWEVdHFGLOsS8pzw6hD1-6nJOsac3eTXwBF3ob0vw-pn-Zu9fuK5fIXuGCPA_pSZGhOwpuHljbXs6sL6Li_gI8291YgTdr-TSEVQSJ3LFUX7yKQADJ0JxbZWV8UbevpIzkz7BaFCBpf6OjxHW5pfmuk8IaKALbvs6CM-KoExpzwjG5seyxLTh2GqGP2q5EUX9Uhfj3yMLVwkPxLwMSeRIXFKlp0oqo3bJSWg9Ohls19Lxep2-X69vbCWzgOU4iH86p9VrCSqiQfHOOazRSTT3PrLv8UaLbL_wM3DKLorWfocEsGhCFFZ_gkc60K1djdlB5xa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تو جشن قهرمانی اسپانیا
😂
😂
😂
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101385" target="_blank">📅 00:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8C7kCDP22LRSm2PnSlW7Qot7qqx4GL9R21yMndq6zl39ctsdvQQ_rF3kklL-xwFjqopha6sdXxtNdINeCvSMBGJJFNLrkZc7ss7BbNDO3EKv-ckuP_Hha2HHRYvHaputKIDomqHtKGwYaPUh0_g8VTfMxi0eCV2JUcluLN5ZXMXRx6YSjPYBk-vnWBHAewwUnmUckMOR1I7oCW9nN1NiOCRnnWpkPC65w0-NMH0ghHcroxV1zdFUuwr4CoonKL1OAIAIkMDH64XMurkYA2xn8K7Ecp0Xymw2kLS_WIoCb2sGC5X4qdAmmxvcbBNSPsUqqpE-BzY1p93Fb9py7g-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا با کیت اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101384" target="_blank">📅 00:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2968949297.mp4?token=bZirzDcv7uGSczfx-5Q_dw3ci11_y76_ZcwZSB8EReGH_w6eXoCPVmqeLXnyzfxJcfAmJO8cduy_i07lU3NdqYm1MjQwvwrxAhUK40CStUQtXOqXPYKuYgpz0oUfHEln_ZCzYZ07xC3mU4QryB7YfGKqpE7tkjSmLDofJRqoQtjrTBPbVOCJ_9wKfYOwQeLKLOe6dbxXKA4Vk9dsk9HtytY7MA7zg6oilGBg7scW6ASwa_kXqt3_75vM_Eemnr3dtxvhqW04dCAODf5nvvr3CzNaAn3jFopbYRHtJYuBDOI2qY88I3-AjONXsiAD2lB_CRKR98CqM0fo81dg3SNBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
توضیحات عادل فردوسی‌پور در لایوش در ارتباط با فیلتر شدن 360: بدترین راه رو برای ساکت‌ کردن گروه من انتخاب کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101383" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0990cab9b2.mp4?token=eusWOCBBqCFw_yvngF-mBlTRrVK3Dji6A10fJf8tbtr5Mt28fcHDfkDaDdl_ZYHB_ADr1xWR8B5AX4ahjHqUzJf8VxIGEz--iyA7gSj1r90MwE4AUwln_TM9jfZdlnWHUfAVq4LiLJk5ljOWDw28hJNd3LKRobg7GyzKnawZW2ry9cv0wn7iMoPF7WuGHAkdPF3GeVk6xohphhoc8Q7g_RL1wIOTu3_JBTbP5NHCThvuDagT_1BkE7RnmX5-yONXMgGWVguQcuS81xRKbvfzQisX9wG0cBNxmjft3PfMahpstwny4lcT1u_Zng2QIckV9W_R0cVFqSRyYuyn8p3U0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال با آهنگ معروفش رفت بالای استیج
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101382" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارشات از حملات ارتش آمریکا به بندرعباس، قشم، سیریک و چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101381" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdecc8438.mp4?token=lCRmxPv9L9Jk-oPx6YbXZavKAaJGT4qX8GfMp5mtv_U4AEJGNCVkcMoiN41frOBjNPKbhJefTCZjjFMV7Prg3fA77NdgpsDwO8pst7W9jw32WSYwy9iiwx2-FEB_JAFdDW6MUc8cdklrk0TdEQnJMyUIwr5pULFCQU1wsuvziFuE_-HWTlhAfU4y0v8cgHIXY4TKCgJGlR6CRVBeEvhMwHjRDXvcjmU4vRpBwHYJOFTvqGRKvsHJO2ska7r69g-QxTsT080MLuGDyFbd2lhNez-ekOTkns0g3y9mnoWRSTiqyN8TDmD_GL0w0rY8ZR7pTCKlH35G8NO7WP5z-8_Jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
قلعه نویی: آمده ام بگویم شرمنده مردم ایران هستم می توانستیم مردم را بیشتر خوشحال کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101380" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpD9DB4_v0MEWLjZbLwYG9K0F0sOZeLSVsVdrmi39BrG7pQ3XxAhl4hfG-MTAXa9IVg7uWHVyLZ4XWQdjnX2D2-gqf4gkWg_-6T37QrHdHMvIPVPNM1mxVHn3njSwdulm2e3k5oLc8ZXa21lnEkfWiPEhVZB7B4kI2jxPhXktqWBqmMEgCOPvsEGyFaR0iloFvTUY9uhOJvDnG2m5RInrMPDER3QP939RcrQa8D3G9ZkXgHNYI8aO9wzlSjF9ns_ukQ-T1KB_mESjO909k5DZ59Verj0bLG6hbrrec8A14otlhn33yWDn22Hu3F09NcDmGEofcE3EqFTDJv3RfLq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به گفته آاس نزدیک به 1.8 میلیون نفر در جشن قهرمانی اسپانیا حاضر بودن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101379" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1bf2a3334.mp4?token=iCbc1gUAEb-5HBmerjrCMumwLr1yAWKvD8Hom4X5VBP-trjWZyUu4xd46L-yyZi3tlE2qeslhDIqP71hB3UgC9y5bqorcQ9_CYMGYDcdZGsAuIv0tJYUNw6q7GF0YTdEZ-wjcfwZuiemqWmvk-2yQkVEg0sGMEtYEl-8n8KO9ojee6SFYX4ER5e5TA2AroObwCJowhmelLV7IWtt24HKz7DPFW2IA0R2BFhH5bq50AJ7de4C2nqv_EA8MY3ZMGDJTYr8Jg-idJew2fYIyfBwWA4-nCRsBrJJ-isnyi4swbvTN-Mr7QSc4tWSxNtenDPNhlD2DAxxYU79oaCQ6ZSCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قلعه نویی: در همه جای دنیا انتقاد از سرمربی تیم ملی وجود دارد اما آنجا حسادت و عقده گشایی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101378" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUzALSS1B2nkYkPqQ2xegD1QqyNF8KcOModCcHJJkZuRVX1fnaUtBmly0VINPAhUzhka1MCwZOBHqfAmSYougfqZkn4aYIBXGrvDgWtb9BS1U53Tz3CFK3twbTksiBMtiKocqxjOcxdnlaiU7PW2thnf1_dm9or4TiHfBgrNXFPIUS5557gJuksz-ccB3_H7v1JZ9V4eYjyQtyNu2gl7km8Iw_n2upPtGSJvM9PgZNgNz7qTP3osx6bxn4_pZ85u0aBijTTpX0IlA9kCpFtAiLJObDQwRir8nYWzaxtUwGRsm3pyVrBeXR4Sb-wTTUFTgltnSSpSVzeIxAiykwjoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان دوران به صورت قرضی از النصر راهی بنفیکا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101377" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QswE5Y1_rlsrCTn2bgk8Ci6WsXGwCGwBNVYevzuJ0AR0LrD7ANcmbEi-T3S5AVKYKfZmZqDoGTLspwm98aB58nvA06SvOsDJ43HH1GkwCOOtyIpQnfWtgads3Zs-EO8T8Mrh6MUwPtl89FXl7c7Wbv9EUoE-tv-BkEYul3bQutQezUCN0MmhR-SE_0mxDUAbL6-WTFjUPnMI7a2N2B6fCkjv4XzLSBHBCvxy5w6sgDhqPIR0T7TzZqSBfQhjmNbgb1v72fUCSQDFJL9xvmagQQqZim3Ju5Ip2NSWQvmWvkU1zAH_2ZzJskqKmsLoIQzCinWcBBnoFXHDdRbXedNYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNL9PVZ81WihKbtOxMyhF7XCAVjdjtV1zqzQV5Z2kYlhTuGuO2QaKS2YSF97aV-pfy_usVAFyow-R9_mZkyfaLd0uy-GVm3OxhicdHZAws5j8WRYxUruTbuaZrNurd_h4Qj7BeTqyBPAr7TXiosL2KGZT1yXL0GUnIEnhN4_BKO20kX9nei0IfhWFpOGJsUru9wiUpPI_DRrTR383qVR3z7KDOuR90fkaPUG2KB5iXgVxWgku-aPy7cOuYcTLxFVtYQLSoEytAXtTL_GAfR3Fd8L7CWzdbJoypXRRuZffncJKyTSf4KaNA_0mJXbvH9kw_tfs4YscMIy2CCG0vm51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQqeVOeE_2AQEVCT4ncPdwUvo6TxUAs1hGzs5YDqsUvR7WgJIoeEMYJLp0ylM4UUAuqK8Muj4l24n9BJhVRvYGrLcgh4FfSWJvFbGBREHa0Zw5EgxiLcJRD5S1a4qN-EOd024b9QCdq4eQMDWf_QIlrBQs-Un4SS8jCl1fqcT5IAjkArwpbLQfQO-N_5_8EauC44DhDZ9FoqoTxLPDPiBLw_tFq0sZiAp40V6zIJW0T_8Jfkowb99ossZT0DhKGjEZWnXhhupZyUqUu35HdMN1sQH9qfJB8qPn97vd9KlyzfsSA1rj0QusD1v3JA7yMBf405_nwf9oU4jwhjGRVlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ka4TvXcK4KdygJaopuc8TjdKuo_1c9pv6dIkdxCdWm5pwmAfjf5XBbOCqL2rj_WyqO5mosVmY_mAR3Cy1NeF9zbYh7Ku0yCPb1aFy3KTDcbcue0V1KUrwyuUxegQ2HahHTbjKt62YphMmjcAzxC4eOmtCt2uKg1QsapR8dHJRUZVd81Mi7cpF6gsWg3k9ioz7BjpoWGhNebG_4pHbK5KlyGiL2tcyyGTY0fqKe61RpZwchVMMXVd4F9Xm7FVqirlC-wX37uiXy6AyJmeo8U8jQaUNSQ0CDL8YOhfBhM5mTSODy08noDaNoCJQJRldGec_luMdckwv34P8dX92u7mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
| اولین تمرین منچستر سیتی تحت هدایت انزو مارسکای ایتالیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/101373" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtfqNpnD8G2mS1rkV9-vCU2u1efj9LrmkGxG8yddPWwQDpX3u3czvKa8ULB4AWs_wpsMgT1oDhCfWxoFF996qsnR8PTwjbgt6q-VsWxFDcN3fdkLWs-W1Xh78MDwd70cxtcXfQkbU5AE8w90bu1tkBNW5wKItEWg_RMtseFm-5fwpv050slPBgyEXJhNOENQKhIPtWTt3ex1owHIrHPOW3Jid--fzdCdU1y0uWpfXMIgOEkHyo5N2DD-9CUv73M1zZ3zF01zbZc0vpgEatmcx1tX3zK2-dLe6V8XcEH9up1XVNtn9L0R0cM4YBhGDcu4WdXxufYHP1zIgkxh9LHFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:  رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101372" target="_blank">📅 23:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9632195436.mp4?token=JUDGRyO-vBC2HSsoCtVoNkoLeJyKgqIUyfyoiVsBs1XaSgUNca4ZI0wO6p6CELpDpvN0tqurlHBOiCw8nUynZ76dT0vEw5z24se2CL_UgTJCUkL5pmxn5AkxtSEWDRyw3lTvGIgXoItAQ2nXdzBYYNV07FSgku8Ih1Y-0CpbXyIAVsjRCys2RA9DuBgV2FiBmO_L07Eivu6ANYatPUDPkgyX9Sa90nXeWdzd3PwrVr55gzyEneN6Lr0StD5jBULDGqPUNAPtKrpBomirhISYpp79MK7qXS-5rKg6S-zMKsT4-CQC2hoAJjRWhJDX50e7GoKBv2k7JEN4RoPgViv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
تاجگذاری لامین‌یامال در شهر مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101371" target="_blank">📅 22:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iONPs1BNy2UgAXBbnb3Sy5-rjzXLppeQZIF0sfsD_XRaqwSRgRbZAnE0LHkpbl28G0WUC5mdX8mzjNPpWJJrGbpzUagSUpbp2VwsJl7xKnu3p6-7FjF1NMECGucZLfjN4XhQEVFCwBuywgg0JWouzJZC5mI4O-H5NsRMVd4daBhdoj_CaN77m7Cn2RdSRQ14i7xp8FZRWM_gACKBbd1CrCgXX4dpuu5BqvdCokHyUFNyXqTXI8KuVz1HyDNvvuYkhTp2e09AYNtscfY-NJcF3rUKxFszuoFg2_-90dWuEyq_2Z_LFafZsfP1wo1NJlGo6WonZF_lAzgZqPSFPGBUmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال این بنرو از یه هوادار تو جشن قهرمانی امروز اسپانیا گرفته که روش نوشته شده:«هفتمین دورهٔ مسابقات ولادا دل آنیو (یه تورنومنت بوکس بین آدمای معروف)، بین پاردس و گاوی.»
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101370" target="_blank">📅 22:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKjgyi2NKSoWHmq6YyNDzXpQnunLtV8CuK9tyjACdIFvPpDx37Q2rMPgFDGTX6nSS-6DP4wPzRyOiXX3gqAk2qDulF9XhrXSXCwKSVHSuz0_GlfaTR_sBH5bbCIQJr4OXzv5Jnp1q0yml_ExN7ou1OIvSe6daPyqUoEy6FSCMotoFmq1arL-57PnzV08eAO9IQ0jrXb1-ZzJiTymaPzOJccpGSFPLRBIdueY7g8baw7NozBI1z46b6AALLwURuAxNIIqvzW_18zowF-LbykL0LGmHJsG7-07X1O_js-65lR2Zqq6QR-sgSiudprig_IC_b_jTQfrAN_kyfhpQlsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgdJtRapxOvi5RlcqUHKRxJCSsfXzczx9BLz69JYDUTzkznY3flwszVecSrUQFYaulVlCfeUe6i1LcIZjbrP0Tlz8FnQOF0Nbs3w_6_evFzEP2YE8ppgF0jS1GMjX8A8u6BGVLaVcFybmJVW_4qFC4qhHe2OCb5NaGjPKtZyBz467AV_i712Na_uFqX0JJDkPDyNqHcMEfAIPp-tKU7WQHnVHW94cOU37lT4nFnFXd7rCXVix4CRM-SqfgLCeCV8bGZHZdM6xlSPTNeF-7njTnLTBW2Ia0T8y_NJQrC_p6FbDPlgVPNjhCGB45GRwbqOoZCiqoOoBzbrfpw1GBhdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgOKUuMaKvgGp8HSXCEMpvS24yJ-xzMKrPoMe6AFdlUtiwiddbb5BwdKeggK8lOvk3MPVTQlKsCNEGyutGBORQQifhP1T6xDkYhoP1BKGdP65yHR1yuXj78tZP6Hc6qmH-Dppc78bcgi_KZSSKSPRCm7kbWVQfliU3tq8NkxeoFTfENIPXfo6r7OYYUBqKOmYsznx3pl_kWJI5sCV12bCy4d428mnVi3Mj6woDTrQY1YQC2w1tRRDM0gChyxi6u5xeWbRUJksE1Xna8LQKrfLqtrjIe5RINa-JGAh49GnouIgD7YPsuWx0tYz8KKiR6ZVwMWRf0w6HM7lFCr9VHfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnTFWPMMD5cYvzye2l3O39VSfLEk_d_iJjZl8_GWrDQUuX9DQ1FoSZ4qq7X50j46BtSKIgQ5Wj8w--MbL6Gja_SUQeRN8polKNmh389gTip7gLQ-RVEbgmtbl4YgGHc5YKYhb54EKBYxnASrP14gi9qOWiyeqZaXF7oSYpJYLvdTmB5Qz4yD6Vt3cKYDIGal2we2mZR22U7PD_ckZTxeMCoxljiDCCGTRr9cx-wlc1k_3BdpODlb6d8DwW86EEOWfhid3xYo6kSFaEvPLcnfKYoIWQ8DlLkoL8Z-ZrRUJ3Axebh4vByLo1fuucJk4GXDvYWZcKd0maBsyI_q8cSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA3iDGDYvQbFLS7xvoAPntReAKEFCGCVVYjY3Q_SOnbRS_GdcdIIFeG9iGdtHjKVXoTGINEDjLjpNtFRJQE1yAuah9TF9f1Zzeht9QCHillw2OTEuqtFYLmpvFCLs_M5_-U-HC3FgKMt3vs5g5foBgD3uJEObCUC_bdMCjje-RQQROwqVcwffzv-nIR8ssm-ndP2lWQowCdk_rSBbprt8x-MwJllEWz4q69hLByBdlQLkHHA2awIM9tgubuAIhhqo_0JYrmCbyPsEQXA6PNtGyl0dakuXhoTgSAU8VGW0WxqUH8727bguAdq8u-eHUMjEZJWemmJv9PGNdZUPE7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erWEaal7dLZ4wpBv_P1V-7yL3B9fEizht00EJmcN9Qf-6ebRUu6qeRzcGl3n4bh6fPBg5z3QgonftIZOeXvYROhDMJpuS6bY3gLcY4Tv3dj3LvqZYlKhgGterYN4OFvtpjYOBQXXPdiWdtdAzItW6y61XVoQPpeJD7QEjhsbUOTgmM8t94QxtRkLb5Hk3-TaE0hnLwr9qAPjzlwBNJ1KsZZwTyWU7N_jzAmw__mH0TxYIT8lt9dhFYsUY3Obpgwdn7BylhimMW8NRjj-caj-yN6ENjvn1Z2ldaQEfp_vfhGqUBSgsT3YXFexH7ZoRuJFVOzO0xEbHoMmnEeSBZln6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZy9_CW90W9Juie4sBfKEFGdjH-OAYZmF5l1-4n7PLNYOnNp3T65D8aN2Kb-u_YdPj1RoinsxsTdSz3Pqk1Choxk__gyspYDa1b7KrhgOrxaZN66ssdA3Bky7y2m3SRm37jUdDP3ZYpsuBi7cj6Fwcpr6rtRc_UGt2Mpf1dOK0y_hAFhjnvFXUB_LTlrLWAfwjQ3DPtpiTYH4hU5UpXnryYREV30AbZ-H2Qvqo1fsCwRs5d7kPVbq3ii2ytsG4cfVgAM0dtIJkiLQbtu1fJ-6MEuVBdk7V-jx7Orsop9nxj-YDfzSo1brnp_KVxllXXH-utmKAqvY3avncuZl0PPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgwqYn9GxntkU1Qts5-hQoKtxcwk2ynn09mdbmTY8na_VwN9fvhtxv2u8Rc4_3dUcfQ_BBgJvcbHPFVErtpT9WZl6vETqnnaqyBRcjnzZutT8HVEDXUI0lqq9Gq45nt5idGjteao9_RhgOjzni28MRYWJlh1w-x_ZEOhnS9oiKwfC6jKHEJNyIc7zRWSXbyDzqkrTtrc7YBHzOr-mnYopwlKWwC8KhAtzazO6wYtRAl24qLzqYPr4lkgCuk327z8dScZlVJdv_uKPPzs3OWil_Mm1y9vKmCdm5BAStLM8LuKZMKb6qGVlayIJaX2T-TU9GYTQmcnKtOF2QQnmRJwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTNWKxXfavKiZwB2KzZnAz_RmiqQHyt2e6J0mrp9B27b0-ZkFxquros-cChCDiVABj-DGH8h7goaVaGz9gQg0hxZ9w95MyJwRxm5lCj6_Kvn5pUVLis7L2SVoobzz87Jupe1mSdcZkP4-DwTwudtAl0hopwxNL7kQy2f0NTZgr4KkZGZc72V1GWCAYeEB6HPRP688R8paRSnuTIO20zOcJ43ttyY7PJ92wL3YupSNDvAaL7bQN1RevsmAmwNBQRMjz9ceQEVzYscvW1hVwyaLG06v9ClPMFg8an1GIGZGpUQxlXXqyx9UDZXhTejJacFncRWfeYM7NHuv2uAorxnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjW_LbEK_80xS4A8T_-y0KrzxMR1o44sUmb1Rq7Lv8VlSaTysvI1bQm29f1KPfBrLDI7d8C3jHPPi4EoFEtNf6K2fFdjRi5ZHY8efkNBMc5EsDrm_HrFctqldiS2t1Layl7qmzEQAGSC2muiBRzTMGKyKn16QB3Xo9E4nE-jFd3DPP04zETJnKPum9k2XR2f4KMxbqrndzRGnoNSTFGsYndF30CgF1AHhKRSz0wDZGzxCWMIGhk550bRbA1dFts8xwcnsH5f1CS1bQbAcLVUBiHX5tR8pEHNXaW4q1RSYz3TF9hEi2QlnU7WnrYO1XlS7jtxBwo1HyC9Pji57zLYAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
اسپید، یوتیوبر معروف دیشب حین اجرا در اختتامیه جام جهانی مقابل چشم میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101351" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihd9VAeymAVA3M7ayDa72fImv1qC_B49ozgsR5LJ_IW_jxq9wbSanntTxQiye3u_GrZ-prxJ3ftzi1Zlh9gT5V9eYPpSJZR-MOmR4W_6k5ocUzrKmj-W9qcPnuzbNACBVJ9vQAbCVR7v8TVV_wpfJHgREFrGUVcAy6IFv7_oR43o6FmWvlLZ0kj6JnSCcki9YPgCXfX-48SVHA60ssiQBUfSjK28_afbVXcIrZUkJW3zwjv8YS1i8nyatprzvC9Uxas6U859yVzQHvk5HdnKVhuqrQKk0GvwTy_cAJgFg5fLHWmUqIkzLxmmR2RhrJs9jRkOl2tHZ4OBtxGjBPoIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین میزان حضور تماشاگر در یک دوره از تاریخ مسابقات جام جهانی
✔️
جام جهانی 2026: بیش از 6 میلیون تماشاگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101350" target="_blank">📅 19:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
هوادار تیم‌ملی اسپانیا بعد قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101349" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن باشکوه دیشب مردم مظلوم لبنان در بیروت برای قهرمانی اسپانیا
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101348" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=YHmZ9S_rZ1B8Qmyalcp0D-MlMD7QWF1g2vo6-Fm93_cNfIaFiZoWrGfILKeiGg9wjuqEEguZPEH5XmC7VzZNg7QJigHSvNsrCl1kLJoy7dlYeDIgANcv3tlo5_1gAv5GJy3y8zqcPjlxSyPcrgRMboi7jdRTfpfLK3tGG3YyxwYyd2sK8T-b3-R2cKG5ovboijK5R2yDUmtAj3fIncUWG2Gsm9fK6Ma8AEy7vYR0PxentQ3Oc_yd1zAEuu49x_k7AUcIoiUQLwJkbbYXaxa3lBrthRtFGix2cHbJYeF0e2VtcS6U_aubGqSc5nAXgBScFcqtUMP1iBS3gXhEUTydkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
بخور بخور پرزیدنت در جایگاه ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101346" target="_blank">📅 19:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpxY5W0MGfUGw-iKiVHTBGjm3job1Urk7-Vbf-nB-F09YbuaRg4fO8jt00Ml-sKyYnTHMdw4w1HJyxHun0OSRVMY_0NGI86X9UFYeEWdan5qd08mX1_RvULvqFGe954OUOEblTX_PB-nlwaHpiUkxQdPeEXbS2yTOwmoiLvBsN-W5VSuwjTtdrefkuLPTIkJC12Qo71XK7vj_3aGKOs4FwCnFSMbwlFRZbKWUK-ceKgiokfiZG66865DKf3ll-IQup8iRAfcyqpS_vL7YyXBJkcaAlpAxQnWWXzqZWvnmKBVsT8pjpkfDlrUBqFz5PbqiK1Ohrca7-aWyyZA71csgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با ۱۰ گل اقای گل این دوره جام جهانی هم شد. برای اولین بار دو جام پیاپی یک بازیکن اقای گل جام شد.
و برای اولین بار یک بازیکن در یک فصل آقای گل لیگ داخلیش، چمپیونزلیگ و جام جهانی شد.
عملکرد فردی: کم‌نظیر
عملکرد تیمی: فاجعه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101345" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7RzI2d1ZKcvYhA35ifSYjsccFOzDsEQlTi61qROIjtI0_vpfCX2S5O-fMf01WaMAfctC0Qy_j5gClSPSR4M3B3BfkLEGrXrI8kAuUhxzM898Sa7-fQ3zPgI9eUT7BO3CrBRNUmjTEQg4BqTopdAj80z3CFfMKSSd962yPKf4x5ROTwNhpGZ3s2wkiN1fHGo1zJstSauFo-BI_bW9mOizkmOF0YDWM7iwJSDWsjDCbA1wuuk8YdErMt38IBbyHiXGKK4AvO0-P-DzOvZXWp_qT3VFMm3sto-r-p-Ib1whtZyIEdyaGN-i0BDhmlGf_LKCSHAU5iDacrnBhryfx9_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بایرن مونیخ از تمدید قرارداد لایمر تا سال 2029 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101344" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773a69b961.mp4?token=pS-yKK_SIgk6bWaUwSmHovz681g1I7-QVKE9--n3oQCcQqpQaZ19IJEejDlSF1yUfdnZiC_aJAd_8uUu0Y_cEKnrDyaBWSbUnibnEYAgYNwNisvOmXyJwNEi2afTtdadvb_r2w1R14okUzOm9oJzNPp80XqXejCxJKvY_hkw2frxbXPJz9yMWmKgwbTwfGRnqBL1zsowAmqZBCJbgMLmGXpSGAU07aYHTiXtfL1s45j70dwEDEyQT8Lv1wjyhC4LlxiUjQE-2jxvAv0DJhbx0ByaeANINXyrHr3U1nfYTBCCobMZPjqgwPFvXmKFtdQJagXZGfVF3ZTZw8_OuXyzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773a69b961.mp4?token=pS-yKK_SIgk6bWaUwSmHovz681g1I7-QVKE9--n3oQCcQqpQaZ19IJEejDlSF1yUfdnZiC_aJAd_8uUu0Y_cEKnrDyaBWSbUnibnEYAgYNwNisvOmXyJwNEi2afTtdadvb_r2w1R14okUzOm9oJzNPp80XqXejCxJKvY_hkw2frxbXPJz9yMWmKgwbTwfGRnqBL1zsowAmqZBCJbgMLmGXpSGAU07aYHTiXtfL1s45j70dwEDEyQT8Lv1wjyhC4LlxiUjQE-2jxvAv0DJhbx0ByaeANINXyrHr3U1nfYTBCCobMZPjqgwPFvXmKFtdQJagXZGfVF3ZTZw8_OuXyzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای دلافوئنته درباره اسکالونی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101343" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G68M3RIw9KD3AXb1Lc8gmsZQ639SMUQM390gUkfRmFwHDxnCx5NRar34sOemTZ7jJwAZKrSEHCLNWP08GTDzemAc0wCROR4DTLHQs9VkTbIXyMlAytzf0iFRx2iQdsjVFpcf4lEIy3i5ne_E2m4pgbgZXjSBrzCertK5dbFmrzStli5Z7fUI-8YF_fQm_KoeICMSEYqMrcy2xW3e1aYCdHvDJtq8sK8yF35-sBPStADnnii21_t_ibUTp3AbtB7Lwr7_QKuOtZlaGEGmGafMPl-_CvTI9OQVafRswRpA2A43KBcwouwFXw5GFz9DBLLqt-WO_F0_lG9IYF30pBAuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=BfIUuLNLA92Kh1NJ7PKRPwp3KocPmtmV9-sagmW1SuFPwLfnwGlUP7D_rlX1znIK6SsrgBkBU-MT0QpZHBAN819Z2wai7tkAGyPIEvJfwLbvkM1slvQJWdzjgjalpl2WD-3sqTjhLT9HVzW94zfbGkb0lym0QTeUwg5K07D54bGJTOTOoKn8A8bjZBfJ_5MTuHsGBwp9SWMZ4HLp8gfezdPkQ3egRU0QTF6tm9biooz0iTKDolEjcIQMHEgCNdFNsGcpx9iXBbbhH9UCoFwjysFKeqomEUE_5WZHJBFdCGsXWwSRDdv8B3X-593OKZ2TyMWAdNSN-lTe4Isn-wS8npVOf0uwWH6MgCLD3RMG1IBuKqRz13s6TQrNOk3NjhR8j1KedFFnJjd9ldwNae0pES0UKnrTe3C7uko0aGUTp-ODOXsxd3V7-X_WmpQd5r6TV5pI91Gxxu-5IX6uxn3VkrTb2s5FSb7bnBA2qWjsF6h-VkPmR6RaZG4t9C7veAao1n8P-2sRn_tyVCkr_ZEwUL7bu7kTbUyvcgJUGhDzfbRBd3bhVy_PuHE4ycYKns23sENntT1XA7lu2AxXzNtVtxe6rhq47JEgEu0MQqgitNMmiTMwSvQ1AO7GmXqv3lVdlJ4LEQjvXujPd7Jn-N5IY7mlUczqmU3uQqlTtOmNYrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqAeqpakEXfXZyi8hDVpzBVcPeoITC3QJfEISaV1ez5czhwI-z1GpKp4kDQRYm4F3ge-jJosgNtSFuLFAzN2FdCucZa3I5QLRQfw5uQ7fSSv6LLeLlVP2QEKd-MxqoCvvCEItKli1m5pp6Hx_5Az2LuxpoZp3fUsRRz465IRub9JzHviHyldY3iEmjPZoQqGD-IfFFRLFF31CZc0_E1v0BB_yOa4QFB7yMcZC8zhjLydlpgk5YMkEOkaggEsQb_thwOTdOtXf3kSpKijXk2QxWr-NX-smSiJ3m7CNrynf_LE8smvrsEn5Fm0sLQMpCNBBorOh_NZS8rAFxDhxg47aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVYJ3MUDGMYPrAKBsC63S86dHjFhcPg6HSkvgfutWG7FMi0ldTDnqXebeHT29YnaDKmqhmAPzFXAEdVXQ2NWNtBPtIoS3hMrAlflulgxsVDl5p8N0bsWABan6UMJ8lAgIaEv34i6yK8Ks9wgkz8o8w1R1Kma215KkgLG-PGGfaDatVN1h2OXK2TlW1M9OsAFZF-puI0mhGpT_ykyXTGxecvIG1I8zo2c30ldh_Klt1zzgvZNDYobtRaLRzjK1dxf3gHFalbrvx95iNH_OaWx_l_2wX3RaLXXwoTPBclcL6gMhI5R6dVDtGmwQSfE-kj3RbzFQFEDhicj01AAUgDogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3dJeErSzrmhYCJ1MMkBrIQNqUsNRusw0CuR5Itpx6x61ETCZS0nwQv39YWSHuZ8fAZPCY8q6oOTTXRdbBZi8gzNKLyrmdi_XQjL1rnpLvSiSx5s8mXMa0KjNSYEZpWxxxOLyTi0hxebxZtyzm4hdsdfuUSwnejj8Zw-m4QSgplVofNkC3dl6_HD29HnHCtoNxUbMbabmIoA9rFlAYlGHtheJ-rgMbOsq0KvCPNYPfBD12uF-5h7kYdw-zphpLSFl7klPFkV53Enwg6cccnvP_Qkh-23oHpTiX7JUKi-OJVGiusv4UNDeY3ij6HciC0eHH4fvtwa9Xe3tO3SeJ4bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMFgh2MDo_6SvHFX9nJ6rThM4QNAsJYeFgObKgB-Dd-p27Z2d2Q37mD-wa_kGubdL_mKTJItmDfUxbwJYsh8Z9ejUXPCau2WpZbKOgUj117qc1EK_lZTSAPTyXneggfhiLea_tEW-vxjUmN1W9yMKtahBheyjVRANSsp-PzeumJHFrEmsEBq7g0KdOxzHLzI1MNOSex4CQAoElylXDnMVOCqnyJhoq474u7jFnKIGc-m-8AaQU0XYcpOs6jB8DBW_SaYb73xRchBlZ9iWI51BVSQPoV2Gy1BBdt0t2CwiMX5b7jA1Tu8g-oZwA5U1R8sjzYy7oOWWiXUGD52jA-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست لیورپول برای تور پیش‌فصل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101336" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=H1x4r2JIZ83tjmMYaSOq2labiYNcbl9F-fJHEim1J31O5JyIL2h8beD16DVU5yYm3WOvVUNACiF_7t6TFa3ps_ZVwMqv3yMDwLRmwhLhn3Pwe1PXq-6KPeipPf95Fe6UlhUK3oAgP42dabzvbsOjpZoEfaMiTjLcb2pFPCZq_wqYK0cJaf0tR1Uxy6hfcBpL4iCN50Trgea3VcCJei5BDRAhZ2Y0aeWC8TgWPRVG_Q99-ugrbqg1Qb2TYfPdOhqgc_m7fVhDdWJ7v1DJW0mKSxqq-gxYz3tXKBJeCiLiTPR3q2Or_MS1P2WFLp1cjq089Funz54LWBj-kEZenU-FvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=H1x4r2JIZ83tjmMYaSOq2labiYNcbl9F-fJHEim1J31O5JyIL2h8beD16DVU5yYm3WOvVUNACiF_7t6TFa3ps_ZVwMqv3yMDwLRmwhLhn3Pwe1PXq-6KPeipPf95Fe6UlhUK3oAgP42dabzvbsOjpZoEfaMiTjLcb2pFPCZq_wqYK0cJaf0tR1Uxy6hfcBpL4iCN50Trgea3VcCJei5BDRAhZ2Y0aeWC8TgWPRVG_Q99-ugrbqg1Qb2TYfPdOhqgc_m7fVhDdWJ7v1DJW0mKSxqq-gxYz3tXKBJeCiLiTPR3q2Or_MS1P2WFLp1cjq089Funz54LWBj-kEZenU-FvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ اسطوره های بچگیمون
❤️
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101335" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=F9xS7wkaDQcYjU4fE4jAT-eRi92-dxvSTC7TM6eOGG4wRzz1AU80eyTgb46Eo0tqsvwjccgN5mk8Efuu2B0xjrA8HLiBynXn077DuIIPf2vaqMAtoEEmP1gSgFtBPUnOwW3g5_VP-vkJGJCyztSjNkVfFMytSyiW_A5Fd8kIrvXiLAqsClfw7Uj4ajjK9uDmfVNgaI_DQSw1586pG9KwapCmmGKez9-U0PFKRZvG3KsXIuQuinEAmB1Gy13b23NVxG6XI4RURn8KwD7TqU3-Tdr9ukbBXWoWMhFQf6yneXMNH8TKIYYNJGiIwjfvbocW70SQ1zFNJ_1ChoKjcgLjkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=F9xS7wkaDQcYjU4fE4jAT-eRi92-dxvSTC7TM6eOGG4wRzz1AU80eyTgb46Eo0tqsvwjccgN5mk8Efuu2B0xjrA8HLiBynXn077DuIIPf2vaqMAtoEEmP1gSgFtBPUnOwW3g5_VP-vkJGJCyztSjNkVfFMytSyiW_A5Fd8kIrvXiLAqsClfw7Uj4ajjK9uDmfVNgaI_DQSw1586pG9KwapCmmGKez9-U0PFKRZvG3KsXIuQuinEAmB1Gy13b23NVxG6XI4RURn8KwD7TqU3-Tdr9ukbBXWoWMhFQf6yneXMNH8TKIYYNJGiIwjfvbocW70SQ1zFNJ_1ChoKjcgLjkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇪🇸
نیکو ویلیامز هم تصمیم گرفت که مدال قهرمانی جام‌جهانی رو به مادرش اهدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101334" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=KAOzuAY_BwfkX2vdtHx9p4rw-GyMhbveG2-RzmEJgOdNZD4IdM19ivyHACoaZSnb1woGvAT5bQsxyoP8m9vzeTQzi1RDcFPIz2ZwD-_DGF5CdvzaTY6Vzd1eHTSFlKGVmp9uuMJTi_TOuMUcGLCrERlRV7jVhKhtSVNJlRSmXU6_OXo_KgQ03J9fvZv9nKC8WwMTzgUrYJYOVBNagGU-brgO9kkOrtS3OEczZ9F_WJVeUKMneuf2d201V2CAaDEUstISyJaaTnYgs1AN2cXY7IHjsA5lrznEEThuRfMDl2isUb7w2Rqudw0ysDW98PtmS47-CAuFJgWLvWuinJzEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=KAOzuAY_BwfkX2vdtHx9p4rw-GyMhbveG2-RzmEJgOdNZD4IdM19ivyHACoaZSnb1woGvAT5bQsxyoP8m9vzeTQzi1RDcFPIz2ZwD-_DGF5CdvzaTY6Vzd1eHTSFlKGVmp9uuMJTi_TOuMUcGLCrERlRV7jVhKhtSVNJlRSmXU6_OXo_KgQ03J9fvZv9nKC8WwMTzgUrYJYOVBNagGU-brgO9kkOrtS3OEczZ9F_WJVeUKMneuf2d201V2CAaDEUstISyJaaTnYgs1AN2cXY7IHjsA5lrznEEThuRfMDl2isUb7w2Rqudw0ysDW98PtmS47-CAuFJgWLvWuinJzEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های لیونل‌مسی در حین تشویق تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101333" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=CduYGCxlPKTYet1DHP4BMM-R52m027jgfacfOV-s_hNy0OeUzlxM7651WkQaaN4DBcJI59GtnhOeqmfy_GFOujlaAbHpA14AQPiA0ZjSxhvvuVE32RNKhpjWSEq7_ARiElBEdQoTVxnroq1n5Ce4ORZI4D9hxPWBthoeP_cpeG-9H7Z_BOak4jBhXHEeIOK3ix0EOdDwdn_3z16GmYa8W3cUmaART2goDZha7hYoRiCRhvEhq1qcKBqCacN03U7FyETyK1ucg7iLeoC3_4xY1vBrpuqR_bvwC0adx0tt03nUgi-zm8zJpo_f9txxWLiqplQWYE7ch3i8CF53McGntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=CduYGCxlPKTYet1DHP4BMM-R52m027jgfacfOV-s_hNy0OeUzlxM7651WkQaaN4DBcJI59GtnhOeqmfy_GFOujlaAbHpA14AQPiA0ZjSxhvvuVE32RNKhpjWSEq7_ARiElBEdQoTVxnroq1n5Ce4ORZI4D9hxPWBthoeP_cpeG-9H7Z_BOak4jBhXHEeIOK3ix0EOdDwdn_3z16GmYa8W3cUmaART2goDZha7hYoRiCRhvEhq1qcKBqCacN03U7FyETyK1ucg7iLeoC3_4xY1vBrpuqR_bvwC0adx0tt03nUgi-zm8zJpo_f9txxWLiqplQWYE7ch3i8CF53McGntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: کوکوریا و بعضی بازیکنا قول داده بودن بعد از قهرمانی تصویر صورت تو رو روی بدنشون تتو کنن⁣. نظرت در این باره چیه
🎙
دلافوئنته: کار اشتباهی کردن که قول دادن اما اونا به قولشون عمل میکنن چون آدمای متعهدین
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101332" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs6GxJAlxQ__4X9BwN52ip5fChw7-b2B4iPCLX8uQ632SJM3wfuOa1zfEDlC0B_XLkAYiW6oizippsGSPmxmr09j7ApdIOduYwSL7P4NlpvxAKQC8fZDOxp6sUpJnGYq6vblvPIs9AG2_me1EeWQMdhyWVcyoicRovnbFBZomjPnAMDWlUFpxqaBJ84p8VECJZrhenIj_80bUu-Nf2F71LxffQna8J3__gAflPNE-STRzVpKHe_NrIpzQPtqLV7UrPg09bHa0gLX9Rz8_zYVLMzXM_yAn_-surKMe50S97SERPgHE97cM_Gkq9Cekr3A7sil62G65D84ZdJFKVzPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسکای اسپورت:
فیفا تحقیقاتی را درباره رفتار بازیکنان آرژانتین پس از پایان مسابقه نهایی جام جهانی آغاز خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101331" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=VD6mly4Fjl-3xIWByfM9cATpvuIMslmRLNOCeVgTt6Zma84U55GrRpp_L6pdWpXd_v-FjAj884iZR6M7190XpTBynXOdSiJT_jsBrAGa5TrYd7c3aObZU2BhAb7cf1LVTtG-LlIRVOnYyFPwVAMiwzgJ1Riz1OekkzqidUm7afJy_oeDirojaOnL4lYO1E2xwdMAFTHM_a8oxw5FYwY4-N92j9BB6Yx8jq1D1B72zcn_d2bafNgwxyr3DMU88pP3IC4eh1hcdzD7k2VM_v1HAkq91iUPz_YDIMUqXmxhReB2uxuaLjpyWKMSrtGTIxyMLg5bKtfNVm2AB79C56HtIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=VD6mly4Fjl-3xIWByfM9cATpvuIMslmRLNOCeVgTt6Zma84U55GrRpp_L6pdWpXd_v-FjAj884iZR6M7190XpTBynXOdSiJT_jsBrAGa5TrYd7c3aObZU2BhAb7cf1LVTtG-LlIRVOnYyFPwVAMiwzgJ1Riz1OekkzqidUm7afJy_oeDirojaOnL4lYO1E2xwdMAFTHM_a8oxw5FYwY4-N92j9BB6Yx8jq1D1B72zcn_d2bafNgwxyr3DMU88pP3IC4eh1hcdzD7k2VM_v1HAkq91iUPz_YDIMUqXmxhReB2uxuaLjpyWKMSrtGTIxyMLg5bKtfNVm2AB79C56HtIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت داداش یامال در بین ماموران امنیتی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101330" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M37n4aJtP0Ljj8Mk1q76H_8xc43GQpMRwkONM1L27GYyVl41t0edDKafDuBTDAbVNVmZEpibPvqtJV36QqP4qe2lNohHY6wrlRiyx_Jto3vMfm1Y9jrF_AXcW6Qm4hnMoxFsIEESMmYgHh-EaEPlVublhMBOIrcRqN4cb1lYeNXg0MT5Souooz8T50Sw2BipXnKXYhCofjOPlXKBg4GjMfaemftIwTSh1O-FUKwg7Qam18AF2Y15KVTTq760Rvoj75fCT4BMRP_tIwPgWqhUfXkDdQ04940cYXzHCwdN4G570Y2HYMGxgFX9I1DLsctrdVQzd7DIEUTP2-NaYiu5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
قهرمان جام‌جهانی به کشورش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101329" target="_blank">📅 16:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC8hjnE66DBJADguy9D_vdzy1nKJFGG1NQxJeBM2P9HfnyDYvSkcSvm2xUdpUhQEFqwGKd2DZcourgJa8cqxgAq2D-Qt6Egc4-TU4Ry6Z-T71F25K4hmLscl-1Ekf_ZAoKbiST5BDNGCAfKOdVY1S9yS58Vz6fJczui-_0Za2GfjnCCNWqchW9e3K9f1rF8dIm5sqvoD_rcEOfbO0K7R-NafGTNTwAP36hWxbjoYBWx3SI5BqVMyDFS9iKGZ39wJoBan1txjGEF2XFQw1hjWwIyiv4dYFYu54JqNZpGy3sQDKzo-I8p0ITxw8eR_KGuQVaBOb0_CAhuvj0QvqZN6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
گاوی و بانو در مراسم دیشب فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101328" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqCrqmtPOpBFc2iRmccMV2_W1Icdukw-Dhfv-TJYQ2qRPsH3xMm9lmHNUKRUyYRH1Urx32K5EM4Af8mp-sKJJKdUrxb9X6e84akiRUOaeyx8uK3rAVC_q3qmP2nvnaLIastVQz5-03WUp0IZ6cn6wG1eJzD0w189EAzOetWBdq5oJFqqRql0Al8nInOU3KyTYqsW6pLoXv3SAUYeciqfC7TOrqGnAWU3X5bchIYSk8AtS52fyJomXq6Lrc9Uk31C9tHwGWceW-_cb3F0Sv6YjUWfYzC6LEaqlDrwXL4lgioC2CCE9SCiED9OdincaAK66kWk8APtyDkCh3smuEn33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رودی گارسیا از سرمربیگری تیم ملی بلژیک برکنار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101327" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=STuqmMdkR1793E4iQgZnXsR31Gr_Lb-QhKgY6D9sMm4IIkBa081SBIk-Yb9q9L-M4wYvyD4-yxgbrKcB_Yt3Kqxi7cHiUr2MrWSCeF2N3zH9wGT3WaCxNjv3oV85iPMp6dS87QMHo8u3oMJbLlHxPV2mOjIyUx6LBHPZAx3Am_oPHJ3lKsHk8qH8gze0TnRU2ktXmcu8d9UL4DHZM--jsuwnQMF0sfWQ4NVwmL36MuKMf-tlCeyXbI5vyqCHLXi6a86N5LANBbw8jsTVJ3QC6yAjCmcu71B38vnsCec0lk_qvJ1MNTW-etU93NRPua4ga3gZMXr2nEOyBStclIHI-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=STuqmMdkR1793E4iQgZnXsR31Gr_Lb-QhKgY6D9sMm4IIkBa081SBIk-Yb9q9L-M4wYvyD4-yxgbrKcB_Yt3Kqxi7cHiUr2MrWSCeF2N3zH9wGT3WaCxNjv3oV85iPMp6dS87QMHo8u3oMJbLlHxPV2mOjIyUx6LBHPZAx3Am_oPHJ3lKsHk8qH8gze0TnRU2ktXmcu8d9UL4DHZM--jsuwnQMF0sfWQ4NVwmL36MuKMf-tlCeyXbI5vyqCHLXi6a86N5LANBbw8jsTVJ3QC6yAjCmcu71B38vnsCec0lk_qvJ1MNTW-etU93NRPua4ga3gZMXr2nEOyBStclIHI-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خشن و اخراج انزو فرناندز از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101326" target="_blank">📅 16:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936d28a634.mp4?token=vFMfDyDW8QyP-9vbBrE1lnvYh8itPZeftYOtN-_gK6VYdarv5bofx3DPsqYCM0tP92CxQAKXIqj-GhH-xSN6M7ZgMd2e6YhISevAMHlomLXuPqJF1jcGlhmmIH9PZ9Wxfxk4FBEfJmaBObDI0G_B3H0lYgaqj4rRoiSgcttZO3Ev9YJ6IJbNlENGYp1Agh7yrvU0mIOnSUcKLPw_J-kidJmBuMAoBiLdY-Y-FZbdtNpqDgIa03RDqMKuPLUOOhgHRm5cn6pGPCPJ1f-MyKkivE2g1RuU6GG5dQDE5M_sTyM85sJkQIrURGrOAT5P1dOXnr_ZGy-9O-jGIMNniFn7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936d28a634.mp4?token=vFMfDyDW8QyP-9vbBrE1lnvYh8itPZeftYOtN-_gK6VYdarv5bofx3DPsqYCM0tP92CxQAKXIqj-GhH-xSN6M7ZgMd2e6YhISevAMHlomLXuPqJF1jcGlhmmIH9PZ9Wxfxk4FBEfJmaBObDI0G_B3H0lYgaqj4rRoiSgcttZO3Ev9YJ6IJbNlENGYp1Agh7yrvU0mIOnSUcKLPw_J-kidJmBuMAoBiLdY-Y-FZbdtNpqDgIa03RDqMKuPLUOOhgHRm5cn6pGPCPJ1f-MyKkivE2g1RuU6GG5dQDE5M_sTyM85sJkQIrURGrOAT5P1dOXnr_ZGy-9O-jGIMNniFn7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این ویدیو از تفاوت رفتار مسی و رونالدو از دیشب وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101325" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ick8fwmmZSCV5HxfJXvOUPYV0t0YiOj2nnWoCzYmbfIUW4jpXEV_1QiSkPv_P3vfKCIcPfxmBbPtsuApt-JJ0f5pwNI4ZX4uvDLcj3HhZ_aUyEL2JxEaJah2vWH0KQGi4rPqfcc6UfPLyTTGHVEEYN6ZKoLsCc6ZGcepzWaauP6g0k12jesruMjlfxviclfk8xQxmvSeS2y95GZ4bjc0eN0Y8uOHbg2KHtWRiQJ6rl7Udt54hZZ08C7La55SOfRXsGdCScZ6omIa0s0ds9ZEGiVRogGGpecskUGEHitzd-vXiy2FPMH2XbMmULaGLczYXLsBA6i08j7nhEliMoWe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
قهرمانی جام جهانی و انتقال به رئال مادرید؟ این یک تابستان بی‌نظیر است و من آن را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101324" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46470a010c.mp4?token=iYdVKXvYCxkPtTaj8QVGB3L048bmYGycfj_1Ecgk2GoF5tSN5cJFq0WBE5IiCih7ZO3sGGRSJw0Lrlq9Pi0e-cLN_KWUfW8MwsVw2LGqfcdDrnNyWFVMvJhHepuKeimSvSDcntVJF3QgQbiOycNsvVUoXNBoLpc9QR09K0Qyxuj-dYrN8IK8qylGqMjvKdJ7KQThZ9GvYfZu6R6t-mxArVpXX3uKarWBlElBEWcZakNF9qWPsZa8X25PqSWSQRs-N9MYoViK_Fh4OKqTSmmY7zmQIrenKvSxuqkc0omT8jrEQW7Ty2qyd4vCfef8OEtLCCrEG2Mmn4ss_WfPX2Yrjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46470a010c.mp4?token=iYdVKXvYCxkPtTaj8QVGB3L048bmYGycfj_1Ecgk2GoF5tSN5cJFq0WBE5IiCih7ZO3sGGRSJw0Lrlq9Pi0e-cLN_KWUfW8MwsVw2LGqfcdDrnNyWFVMvJhHepuKeimSvSDcntVJF3QgQbiOycNsvVUoXNBoLpc9QR09K0Qyxuj-dYrN8IK8qylGqMjvKdJ7KQThZ9GvYfZu6R6t-mxArVpXX3uKarWBlElBEWcZakNF9qWPsZa8X25PqSWSQRs-N9MYoViK_Fh4OKqTSmmY7zmQIrenKvSxuqkc0omT8jrEQW7Ty2qyd4vCfef8OEtLCCrEG2Mmn4ss_WfPX2Yrjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان یورو در ۱۷ سالگی
قهرمان جام‌جهانی در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101323" target="_blank">📅 15:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=bvBpLUObkklPnFuQq7oJ6p-pcm1w8Fc1bfQhZtaq6LzLozXMD4bAKxv-7MGPWiWpH9kYXibNnlEa5BjLZG77R5S9YOl5SbrU6enkMJ05ziuf2-vzxLvzOKaHzksREa5uiMxzHfdFV0gxLGxlwFU7nN11ARP9g2ziMGkl5eliYKhW0UP5MRstdv-e-STtJtzMdzl0N6elUv3BnFbHoyW9iEPesab2JqoeRigeh84mFWuoZn9zNKSI8pVVkgK9EQOrtCJSwpKxeNLsLg-V1h8fQiPw3NSLy5DrTMC1z_BbLR7j_jNEkQyJ1j7J4AxtLAaUJZQHBGWcvnwehZ_f_5aSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=bvBpLUObkklPnFuQq7oJ6p-pcm1w8Fc1bfQhZtaq6LzLozXMD4bAKxv-7MGPWiWpH9kYXibNnlEa5BjLZG77R5S9YOl5SbrU6enkMJ05ziuf2-vzxLvzOKaHzksREa5uiMxzHfdFV0gxLGxlwFU7nN11ARP9g2ziMGkl5eliYKhW0UP5MRstdv-e-STtJtzMdzl0N6elUv3BnFbHoyW9iEPesab2JqoeRigeh84mFWuoZn9zNKSI8pVVkgK9EQOrtCJSwpKxeNLsLg-V1h8fQiPw3NSLy5DrTMC1z_BbLR7j_jNEkQyJ1j7J4AxtLAaUJZQHBGWcvnwehZ_f_5aSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
چه ابهتی داره سرخیو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101322" target="_blank">📅 15:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP6q4CAxp7qxnAVT4J3r9ja4xBB4IYB6XjeNqzvPEIcaEdlcGbMLLc3HrB9YkWlg8utJhoiZwO-myGC96VcvHqIOk5bCo9kA90tjmuOfX6ScDTDe25FDQ4sRcrfRkI-xVHPF_KllHFT76bB499LMkiMtQpVXobEFFrKL66ToeWxnvvZqFPUV9AzgcZrzX4ZgGKo67cbuDOzDzQQby4EQS3GAjNrjKshOR12eT1U4VdqqX6po5UQ0bfcl5HBPtmbEyRSOIAGok2sfKHNZx_z1xJ2PaIegL3-ulCF8F7Pk5KK1mupy-59CxckMiATuRZXtFemCopGJc4k1_dnlRKbNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی اولین فینال خود را با تیم ملی آرژانتین در غیاب دوستش، آنخل دی ماریا، باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101321" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJi0Dexnuh3nCADch1CiePxt4VxOQtnAfZtx126EgdHcF-j8KPjvwTF8N4U_igRut_FGk0zqfsrt3HcTr9ndMrMG6Mnd9udD9jrb1jkm_-HKQPSyd1cWzZK44I0BLreT2c2mQ6gWxho9zPeJVTOqx79zE7jnF2O_HdpY3sFJlavsN7PWqO-F65WUwIl-bF6-jhulKVRYiMEussvtvW7j3MCnmXCT556S8SsFdRTfBNQvDXErp-TdYZFeECV5MZwjPi4XbqHuox4WdNGuvFrtptyn-E3TfZ_6uLL8vrhBiuqik9vv5k9qnQBPDbYDi5wD7lK95XRfOs_zmuVl8MYh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
پائولو مالدینی و لئوناردو با پپ گواردیولا ملاقات کردند و ایده سرمربیگری تیم ملی ایتالیا را به او ارائه کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101320" target="_blank">📅 15:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=rVMju_sLfES_SLcdOfO9ImoxQNtip1lzAa_ZnWxWrjRexuMKxHKzgz9uk7hao5IfkgrrOZxYKgLVmro0NR26oVsPP5HmoPXp7YSzs25O2yMRkV-8oFJ3PJYztoM5JAv-F0l_EFUlrXR0hYM_tjN-DcakUYqwvnIM-cqBN3HOasMUjfau2lDkP-TNBJ1VKq7IFw8gf3t42m6svwlbwEYqJEEpK2Mwkg0dt-Bvq5Z73mQy2PCYVmskp6W3TOA1_B8AshW-AILvURQTQpHAHBzbmHyACtgCKvd8gVMNn2HzXAFDdljH2fhImIxivRahuMgFi4yqoWGfKtFkDKhS0LPMmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=rVMju_sLfES_SLcdOfO9ImoxQNtip1lzAa_ZnWxWrjRexuMKxHKzgz9uk7hao5IfkgrrOZxYKgLVmro0NR26oVsPP5HmoPXp7YSzs25O2yMRkV-8oFJ3PJYztoM5JAv-F0l_EFUlrXR0hYM_tjN-DcakUYqwvnIM-cqBN3HOasMUjfau2lDkP-TNBJ1VKq7IFw8gf3t42m6svwlbwEYqJEEpK2Mwkg0dt-Bvq5Z73mQy2PCYVmskp6W3TOA1_B8AshW-AILvURQTQpHAHBzbmHyACtgCKvd8gVMNn2HzXAFDdljH2fhImIxivRahuMgFi4yqoWGfKtFkDKhS0LPMmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نمای هوایی دونالد ترامپ از استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101319" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9sp3iO69nYMw34pNklVeWhuB5hnlX74iQbM9xcyphrHxACZrX6_yFexIX_kAFm_yhzb2ZWJn7vEEdoUy9uL78NYkyalWeHQ1xbwiYZBe7jEgjcjPqBsw0sYOJt8gb23dqtdcbLL6pr_6W055JA7mCS-emuRBKlLB7a6o8wS-UuRS1qSIscuxIuxbQ58yj8JsnGSUwBr0sgSkly5oAc39OFu6DyAXMcbBTyVAEoVeCFCpoeNCBu7VRJ6dsMwZnP39QxZxd3UhLSIrLZPsydeW3Z7p3mL_dlQ7xkxiZK2MG8uJx0s34w5NOAoeTQ_Lkz9wQ_JsKwac6MbjkbYyu16hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgtFEN6tlSgHmu65sJctK_5eNOclOnI8VaGsPo7kaKXuilF_S62SV933ZXqHX16CqrDTHwwQmaoPq9s36gMOAIFkglb1Svn28ZxiwgX_sQ3EF--mj-uMV2PMvccOq521JBUa5_oNiOjHF83HEhtrfQKkX-ALEc4SLRHaduxSKpz3gS8Q8OFVLtyupDXE5wj97b4Bqn2Q3F2cWDuRDpkn4B3L_NUSrZ3y468Ns4jrmP6a8B_qhKyCsLb3lExMSWFzov3lsYjkVmjYTy9cvbvBlvI-ibXg46GyH-o3PR8EqhIbe3zBig2f-LZNlYXZ_NaKKj3NXFPcL-ZTNR8ad10X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=pRgCkLsH4ewsmGkDxvzF7iw4CtjSbO63OV1P7fS6RmJHzzfmrFLmDYh5tVeRMkMW3V5MOAPjlO6JeSA8WmppDXe3tm4epY8tCBTT88CMbwp8Bbb8wLnzkbXOBuYe147WDqXWgwGeGBnizbsZXKuLubA701EoV8rqHjPgiezMyYg33E6v7bzUK5-fcleudfnuGITuVl2NFFPBHQGj0-VDqh7LNMZI3wbF1RfMq6IVG5Sm2UxmRD8PNaml93I8_vP1N9i1TZU1VUbEXZ-GZzsTgDut7PV-TcONBlHB1m_ufCSjniqcgaT65KVKqfbDK96fTD6Ku2LhQ7tJ6DWR0rufTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=pRgCkLsH4ewsmGkDxvzF7iw4CtjSbO63OV1P7fS6RmJHzzfmrFLmDYh5tVeRMkMW3V5MOAPjlO6JeSA8WmppDXe3tm4epY8tCBTT88CMbwp8Bbb8wLnzkbXOBuYe147WDqXWgwGeGBnizbsZXKuLubA701EoV8rqHjPgiezMyYg33E6v7bzUK5-fcleudfnuGITuVl2NFFPBHQGj0-VDqh7LNMZI3wbF1RfMq6IVG5Sm2UxmRD8PNaml93I8_vP1N9i1TZU1VUbEXZ-GZzsTgDut7PV-TcONBlHB1m_ufCSjniqcgaT65KVKqfbDK96fTD6Ku2LhQ7tJ6DWR0rufTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=V6eij_4ArQQ9z9i8PUb0Y-osEuuQWHbrJTfpC5jgY9nyeumR1aBDFCyj7wxprd3B-Cm8h981egWREcL-Z5U09FZU2q3ysI8L2IQKyK8QbI_OGGfAFHhNM7vrydlXWXi0uvRo9lWETpry5AAwO7nB4fhmd95d5Xlt7wz7Yu8YpX-_07a55_ilchbUPqIAxuDzfxglS6WHQ3sxOBmiHwSoUmrA1t_aX-YG6oMq3_xoWkZ2fbwC4CnEY_dN8Zux1i6FW7Hjyl4Ek0tBhil8fuLxfvRuLXKFGQikqNKt-Rs_LlS7seaBySL5M7DDig2bnBBylN1TNGxrDCOZI-n4FeIKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=V6eij_4ArQQ9z9i8PUb0Y-osEuuQWHbrJTfpC5jgY9nyeumR1aBDFCyj7wxprd3B-Cm8h981egWREcL-Z5U09FZU2q3ysI8L2IQKyK8QbI_OGGfAFHhNM7vrydlXWXi0uvRo9lWETpry5AAwO7nB4fhmd95d5Xlt7wz7Yu8YpX-_07a55_ilchbUPqIAxuDzfxglS6WHQ3sxOBmiHwSoUmrA1t_aX-YG6oMq3_xoWkZ2fbwC4CnEY_dN8Zux1i6FW7Hjyl4Ek0tBhil8fuLxfvRuLXKFGQikqNKt-Rs_LlS7seaBySL5M7DDig2bnBBylN1TNGxrDCOZI-n4FeIKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=OwKa3RQ-2U-x_YW8jKRTIAmfvdQagSouVbJPWiZzzLmLzl0NLzwfE9E-lclZNDDrBNJicktaLhTkVClQwVQf_BurIxWOGTGqol4G_3on4xEdAHeBH2o_rnussmNW1BuHTJwXsgR_0K1R40Km_H6vj7UGMd2ZMrub4PHoasjF8vFln3weddpnd84ZtA5h6fCVKLQqrZy49umLuSMio0BsR9gXZcZ2D6MFcDBjPNkiF2q6Z-anMJxjyfa3bqkCYWGb3YTTWZLrgNjw2JwNc8UAqH3cGvvoawLmTqDoJ9MGenj6gjSY9nMUAVvUpAzd1HFP3hs2DvOVrTpE3o12y89E-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=OwKa3RQ-2U-x_YW8jKRTIAmfvdQagSouVbJPWiZzzLmLzl0NLzwfE9E-lclZNDDrBNJicktaLhTkVClQwVQf_BurIxWOGTGqol4G_3on4xEdAHeBH2o_rnussmNW1BuHTJwXsgR_0K1R40Km_H6vj7UGMd2ZMrub4PHoasjF8vFln3weddpnd84ZtA5h6fCVKLQqrZy49umLuSMio0BsR9gXZcZ2D6MFcDBjPNkiF2q6Z-anMJxjyfa3bqkCYWGb3YTTWZLrgNjw2JwNc8UAqH3cGvvoawLmTqDoJ9MGenj6gjSY9nMUAVvUpAzd1HFP3hs2DvOVrTpE3o12y89E-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oulh3jby8T4xIlzbQodTG8nB71H4oCuM0ZKpW0PiYzqb030nZRUxU0_9yiHTBPG9POLsFKXkNvEpXytOtZ-wy-mpGdrO6gm7U1pNqmU8ggNjwsze5Wkm7sC7_RA1PN0XUxqbCLj0U1304KSyulERTjiwIHKOy6PSeB3U1rbXsky1GSdVZU4jY361Rxsc-m8HIubA9Nv3N2PNLx7ECiF38p1AocFNHj8B69ti-SQj8ImJhaZf52Z-W29vqTutNyeyMSxOM0w6DwOtUNufvvDCDv23vIwyceq5GNYQLaOaZxnM3l2Fm04HPG0XraDkydYGVsZMj-mpne3wctLoqO4edQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQT_nqv2BcPTPO8iZo5VubArJP7pDPY3FY7nrP7e4nhomAfZ_xd30PhuSWVbdeohzbNWiio-K-jGsGFYgVbrt0gWiLVCgr5WOkTJ_CfyOFC1T7gmoBngnEaRFDrqko7XjQCeGQlrJqRQCCIfU5zumwHh0nB89AdC5VGah3KFKx-D0-vx7UakGHnXya7iFIDWLcIDR1G1JOdeGOhCRTnJG2PjhT30U6dkUWFn57QBMF2LyLjDMOozQWpszwqt1ge0h_TuBizQjhF8PwipWlDCUJ-tc3cZGdS-iJTNmrfxrM_VatfCrsLHNr27CyLl_7CrywgkJNBwrW-G_kwRsUHBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz0am282lNGgvTkLc-gsCpsvojCDuRHty34TedIFYy3NZ0Gv7SvgmyYTyJHZ_GrIZv0Oa-pLvWlop-_cXMZPEaGL7Lxms2wTgLMbhoc0R6gfQE_HY81CrmxPlb4PNXWFWX6oorYbyiwbmdNfwznjZir3JON9zSIMnkPFT4Vx2FVo18fVlUyCc2SvtKNRVUVHXsJRn4A-Fuv9JFDcDVJivHcHB0YTpFXa6zlpqxC_0Eb4NKBNCL6vR6x-5bz0Jj6xCT3E3TzJHOz1WT4AoAseg_o84u1klGmYxdwdw6ZWLF8BDORWNDf2jRoz26SC0XIL2usrPPi0wzQX9Aq0WwhDeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
