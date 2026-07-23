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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 539K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 15:38:44</div>
<hr>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=DfKOWMRJcQVnfVqhYDDtFfE-fat9g_Zd3CKqNiC-WFPmKonhckqnfXG7vIBqFAdVbzKEukRkq-MYUVWdEvsVdqcuec-xHr6Pt_WjVWXIbVg8ZHoZE9Ix91PaCUO_sCX5Dyq5luXSNgflpDPPfCh1HlgAn3of2Gu8CwIUfDek9e8E24dgSscR80xcHQV5QvNJzPKWHK43w2OzeybnkBhc1jPJZf6GvJDsuYvSyBmeI0_lBZt6FOwIDzpTu8dyUybpciSpYP6EdPq97O-NwiY6qEcu_N3tFQeVS31IoPwiQYk4-ii2KPFrExwOZ0HeZ7zeI4NZkR_EE00XfKef5G0z7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEXta4jOvFS0jlo8G5qtenvAOSz1qbROLwkgaHVUi9u_Y5fnlOzhZt63E0x_MNUgxnaH1OI9HcYgS8k_rbYdQXapwCi1pPYzh0qqBnTxxanODtl6tl_Fc0GXuR97k4WOGF4MW_CHy2yT1ithKLnItzJLP5Nu5mpypUopM8E6NXoiB6-a6BKXJDphBwa1q1Q6qpua3zjEq0Jc22qeBSCVW3-bUyvtNAkDBwNj0VFHRluGR6OVoeBfKGxzT85zrfxhK-3BhRPQAotr2Cu80t0mc6-mvWiIQKq5z1TvP7ZZb23gAEytyUff0D8gs2NMBxmmOwav47yWZWPx6B3_8xqeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=mtxO93sMBvOhGgrxo0fbzTNaWK6XOr0RaS_iItNlzmUEu1B_8hzNWfBFb9lTAv_Xg8J-iFY4ZDBcy2z19hyHVcveYeNS4xHtxCNkR1_zqqCR2rc7EZox4m-u1uxta6yvj4G7_YaiIt7Hq9NMPWvS8rXxtT0cQQkGfjgo6w8FnrvGw0vzEBvLZt1QkUzjjGJItME_nbfCR7v5BVvJ8iRtSVL9vkgQoNPMvJtj2mb7DLYzjkLoqjCW3Knj5n4p4t8GX1UnPaS_gMMdeerp0YBS8h0oNvjQA3Xoz8JiAvorVE7xVyg4lDu9Rf_mqYwthVakZmH83oatO1YGCrZrf7FBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=SVCwjyTV6GoRnKf-DiNh9Q7KmbAOz6gqPN2mcBr4mTL4ajZRmHsAz-s2gT5DXwcGo0QLUQZCZUSjSYQEZQT4WGhmqY_lS7G_vI_kB-YQlYj9FXGAe_7xzl5vr3DCSrqShvMcZf5jqlNzL_WTagoM85-LQDu8w_7QG2ojS019HN7LUccfbdN6Rhz5hMnxzmBDRjJoLQWvGMHH3YBqYLWMSYT_J5Bj8QpieVL92lUBoMIBg6cal-aOmvkT_NJ3jQq_33dSYuEE9NxTpmztfuBwRKZYUyBSEQ69W8G20UavKE9zy-VPG3Sun0GWY3XTWhvu71S2n5pCnfwXmuHhdTp6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=SVCwjyTV6GoRnKf-DiNh9Q7KmbAOz6gqPN2mcBr4mTL4ajZRmHsAz-s2gT5DXwcGo0QLUQZCZUSjSYQEZQT4WGhmqY_lS7G_vI_kB-YQlYj9FXGAe_7xzl5vr3DCSrqShvMcZf5jqlNzL_WTagoM85-LQDu8w_7QG2ojS019HN7LUccfbdN6Rhz5hMnxzmBDRjJoLQWvGMHH3YBqYLWMSYT_J5Bj8QpieVL92lUBoMIBg6cal-aOmvkT_NJ3jQq_33dSYuEE9NxTpmztfuBwRKZYUyBSEQ69W8G20UavKE9zy-VPG3Sun0GWY3XTWhvu71S2n5pCnfwXmuHhdTp6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=llz5JqqhOVgmYOLCq2iNEjoS4I2hUF00HEotH3tJhWxvb6oE1KHWDmDhd7DzFzZXCnPPp7Appd7Ycn_WUf5kyhQMPeLN9G9SKRiYDCT4qZedqR_YqRVjuic5jmx5poOTrvi4SpPT3yscM5g7LxtSwY8TWSTBap8l6HFRqb4n1aRm58leADupqHYsPc9Ldd7PJFgcTEUzvBv7AL9BriwUXn5ZuzVUuXLRZOJqUsoheZHRtB4SgN-M_i2h4qL1ovHtDkb7IEB_ydPyfSjYXPaAIMEEOvNJNfRCZ1enadqEX_50eN6AX8oMnu8lBIMZPb7wmFuVx3D4jLv9VIx0HpYAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=llz5JqqhOVgmYOLCq2iNEjoS4I2hUF00HEotH3tJhWxvb6oE1KHWDmDhd7DzFzZXCnPPp7Appd7Ycn_WUf5kyhQMPeLN9G9SKRiYDCT4qZedqR_YqRVjuic5jmx5poOTrvi4SpPT3yscM5g7LxtSwY8TWSTBap8l6HFRqb4n1aRm58leADupqHYsPc9Ldd7PJFgcTEUzvBv7AL9BriwUXn5ZuzVUuXLRZOJqUsoheZHRtB4SgN-M_i2h4qL1ovHtDkb7IEB_ydPyfSjYXPaAIMEEOvNJNfRCZ1enadqEX_50eN6AX8oMnu8lBIMZPb7wmFuVx3D4jLv9VIx0HpYAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt7R2uoBeoROPW_AHJEW1FjeoWFO0I8Tllm18x3_mRoa7IOVOOugeqEu8V-0SkjdXJThq8-N2cXnuSxSOFy0d_UmZSCm2Bkyjppot1TiMcjbT6q9Xxx__iw573zoXrsjxx_o81nPDNrgijDATx1eieWOeKSRd42H69vaqo_T3GvtnCXD3f8Gxb3gdm2MUUUs_GdhRlMo8XVi1EnQwfc06QyoeofCuacrqMg1fBrdrHaAbPr1QCuloESx2CqXtTnv4E7GRN6fYYEH-LGIDvalFYFppAK9oGPdvYfm2gdPcqH8S4e0lSd_769BBCi9x4MaaP0Ag0QEC7hOOJzac4UMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=nyO6He8tqNkdYda7SndI5Gi8Qm6nijscaJp_YqIVPhlKEtVl8XnicakskM6cT53M0UEqSvCQ9uLbqWlA5KIzGV5jJN_PxO1iHhN1B-JhyCx2Dt-M8j5VmMToqqM2B3VRIXJqkUfdr4pRQaYHEG52KmMwvsvh8pLyefAdV_5U4qPXsEK3FemnS6ciFDHodH4RG2B6spxsxEDZ07nRe7xKvFAx-xnF9jJuamU1EjfZa76tCovx81pOH7v7DbuZh2OtOOQV3ZX_AVFDq3uRvqVWjtu6LrC69C8i2u7LSR7T3zpkcPRvL3dbaBRbMh6TT1BNr53EUJempeCHIJkIfV_vVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=nyO6He8tqNkdYda7SndI5Gi8Qm6nijscaJp_YqIVPhlKEtVl8XnicakskM6cT53M0UEqSvCQ9uLbqWlA5KIzGV5jJN_PxO1iHhN1B-JhyCx2Dt-M8j5VmMToqqM2B3VRIXJqkUfdr4pRQaYHEG52KmMwvsvh8pLyefAdV_5U4qPXsEK3FemnS6ciFDHodH4RG2B6spxsxEDZ07nRe7xKvFAx-xnF9jJuamU1EjfZa76tCovx81pOH7v7DbuZh2OtOOQV3ZX_AVFDq3uRvqVWjtu6LrC69C8i2u7LSR7T3zpkcPRvL3dbaBRbMh6TT1BNr53EUJempeCHIJkIfV_vVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNm20_BFAwrUPw3tRY6UKH1IvQWBQo-CbpVT6GeXhqs1bNv4irF6X3HeackwGlx6rEzkWi4ckJt8Hv9QjG1FXDTocet5nMQ21KNnfP6eoef8bx1kvGIDDpziZNBshUl4YbC-bcYbwYHZDeFSI3JVI-dE_Iwx88YSRvdSERUsRyyO9bS6BSnK_9YNEGycZEa3f8uUVvWkgPPs4Ogi-TTWO5e2ZsCN9vUdyRBT0ZA5ZX9sAtMYygDJN-hF4LqPb67yM-rkSZOiYo4tQd4mMz7SM86dlOC9SrEhNIP3Jz3pR_bjNROt0hiiUBBZvmpT6s1KLtN3d_DlAJNFBYSLfFu2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB-0gjFjI39iLKz523C12fUEA89C9firbZ7I3TJdx1h96MdjIQx80cDCH3LzuTZv1GMeu2AjppCEYxSxKyIZZgXM1M8q4AGASEGnxO5ojdJ1ZhBSI11DAqDlYRTsKMx14Qeb7H-mD8fcv0RRRv3sHh68Sw4AH8o0JCqfsi1UOiPstR-tB3XnGTk4SDIh-wwmsSFXRS3k9618L9fWEcBN-DawKtSbVacUWCaCq_7tTHt7m1bAGLho4axCgd_dgswLDJxzTTJe7PgEsejjT02I6XBcFrvv7TjkG6mfE8zYaq89eSBleAaqU_NsH7ji6KY3sp96fh9VepDD64pWdWRdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZzkipYEJdDbZu9DNq4hyDw0wR-fkemTVt0aZDbfll-6L7X4N2sCJtSAKRvVV3Mx2w81H2_6QDnGNzxjfxI15O5aXlHUGtfSU6shqD_YsjJvH91nq4nwDZpNoLF4smRCaVv3eGzpikV4lk3kfgRsbpfrMnY3KZO92m_BZQ4PJZT1JbamlxSzV2HPmBfT-QmdekRHdveJ6SVhbv4k9hWDBwfFEQqA6laP8aAJd28XBwAU38MOKKYCZed5ujrLecLsxk0tfulfSMgmrtxvQ4LZmh4RIz6uD8uitjmWfCX-lZT4IW5XCgRA1Jayf3T-0ESzxt7H-1gkJiLWcZ11OtCaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BluY_gfOjyfl102Gr26qBniqJa0rl7a-yns9Qt2Heqd_4ETewu6uDcP5RL4bvgtdN7gNlc_BrvYLOUq6bhdHMVUQGBMXY1MZd2OM0QbEZevMTyhvCIRto0ks8m4ybGwpE5f5Hri0m9JXIylqmqw-Hl-yQJhltzRonrIAZGXaEif5-eL29kRCInAMjuV8gEPbxIpNM1oNpF0Hy404YDqwfnyrnqHEcAhgcGNBGj2a7AiCgm8zY-TCZU9EKV_4x3bkWvGDOuGTuzxfNgQ-gNGa8QtXskOse_78RcHOoshRlE4y90H8odabjDLDlkWrmRZKDygmj8vyvEucy5u4KxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQTQDCu8aQ7zuakpbUfXhCdFY630mx3T3ZH65N2na0qIuah-jP822Sg92Cg1PB3ka3JrKp9YrO3c2ASwBNe8vm5ipDmG6nYvvbDe_9N9_SVieyivkjlGYJKtDRYVKKUzRV7BdVU2hgpqShYBFieiuMDM4meuIoqOL2-D84XLs-UMHd6SyF5Ko5jlG3CHkVTu1e1ZibFbZ-X1lugSQNST7beeuV8MMaq3gCmkorvfd8l7yOM6knAO_DHKvg0_9Qr4anGLpoj9NXs0_BgKaMxrwB567Bolo1O2kEaTCCq7ztot1aYMJJEzQhqdbPrIIjV_n774vuj0UZI92V-Ici7mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1YpMlAmcb2NTfC5Yj4ilbI8_iJx9dqH0osWatlmZoAw56x9ZEpNi-g0txXhyujO3PdIP0tgJGECG2YG2F_cxO2c2ChfZfSDpi9WrgU6I2IsU_qhGSgw1fa-q4uAXPIoTc7y2YA7OIxYhQI81s7lqMuRKTkxpdbTEPd06cYccn0cXutFa65leidiYMxyp-X12y__gt83Lb4mInda3_Q8ddEN7nOs9sF-tdTQ3mim3hyYS1_O5rEOfWFzcpW18s-KlRFw5FuD8l20x1iUcCATu9T4RA1YBs48E9m_NJoPhXI1I-QA7ybLE-jITcyNa5QFTT4LTj16LU7ZXbBA5K_9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoaHS77mjbLzAqc3yRMAKZs5MfxFh_Snb8vfUutjG7sapZ_JQ18JeLJlcbmYAKAcDQzzuFxmPCjP77hKiz8bwlTTiGMG2Pd-zCu03HdN-wyQdr0AgMLrMImLUcQbK4bYRRlmsI4_fJXJHWq_QpoQebEfig6MjfRat8lm0pfHXEWzcAuOsm9FMKPt1Qnn4fuuUUmpcHjEYOwmxGSiM62YdYieQq4UZkCW-yY336e_3cviaarXmgvQJV0j_K_uc-HMw4avZ597wJhn5xbtN9jqiM2o2JfV0FRAHUbZ6YiAnU3B6_ut0OrGI5A3i8oXK7fz-YPs_srln9Bn406GcciOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJMZCH7caBcKfXO54NeZIaUyGFNfJ1KRoyhvFldhH4-nhIJjTPkcQ-bChmwxoPuqPDIPXHBjVGUQt-mWnit3Mrp2RdUctotc7AZC_ceBuVfVXxVU4DKfm9Wtlwvy46YpDC-j8ziirow9Wm01tL2Feo4Pa1RrcKWQGEo7V5GNTUCnEuZXo28C7i_Wos1aTXRZHtt6YOPY1bWe6Xeml25YSAcQ1XNn32arg5FtKBcHqqyRCCrOoPq_wC41Em7kea84JltVk_z_tP1NOkHN0kitNnauM5crrpCcqc0IlIZyKB-cS-kAM2PFnv3aT--L3Sfcl2EJMft5zy24Yr8zysZRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3DTjE_NpgnrSWErLrDpTiOdVc5GeTcVSLGT3AT67c9Wag7VAi-KmskcA3bIRKMUufKPUQ4gkJ6yG3oUvWb_oTcQ-Rtd5Yqorf_gpp688yb4ZNdGj-n4HWInXJkNMrWeY_ZpS8vFyPXOStH1PnL7qWEg55CK7Ib6qRZYpW7m5Fewl7_iKKpfIi8pn0_WYvxNGeVd_WF-JPvrAO9_bMO0wNN8C3pOjkSdklWK9RpZQnVmoC7fXypL4CnNYJO2Yz0g4cxnr12VlsBR6C32N_luO4mH1-Kvc6pQ82c_gGFckZ8klct2dzUbnWs3HA_juorJgxD_ItUCCUiTMskDBw_llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHn5aOL8pXiX3xG5A6LP3N9F1p7n4ueCvHKHHHSdo_xFg1rpMlFYFswE3E0JskNbRrT-qUAJGtDNqVmfWUz6kcMz3ry1RYPldS0rGfO62_PIJlcxLTxc3m22O9hfS0PS7iJtHD4OVu633GsaKxgvYIAFwkqSM9wNncTpY2R4yNTaFGvBx1hTGPs4NknXO_e2w2D95dxvTYDs1djPozhmOxkbTH5FWHrMMzaX0lXLlImzhUiR4xbhS3Onix3iOOqjNtDxWOc5PXPAnvdP8pbSdrGAQikNtoM-WGFzNp7UX82dEsBD9p3lcflLK3vLU7wpagqN9vSXZ867uUwcSmJzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEyjgrm9o5IGmIyl5Uxa_2jdBd46HMvF419gztY5n1iiCWJfcKQgWSpVahnjNb7T-ur5kTWl-yA3RvktA56up_bLekV8yxerOli39fWOFDTm9BuC1A24C2uMeFYeEhXjJHGw67EkaGoCh3sN1oGeRTpWdMtXJNcYRJXOWkElqs1RefpnzQzcETo8zGpDOi6eD5hCR0Z7ByQGiNTwNSOtUsu-XJhx9PwKyd4JBx9iNQjCb-_m1HcZq-lJUnnNl17L0xsLDxSOC-QcXTeO5N9X1cJoZtNwD-frPALLAnQMjGQEu_p_SzT8dYvGydKghTFaE7LXEfG8zjh0hHWREnsrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3VNxD6xFHK9uGfoiFnJHXbCjn2KYaLh98bSbwLVAw-dPgzBD6eDGCT5pTvUi-w5iKpHD4ehTFWu7RT9zfrVhGIXmKoDvwQ109ga7YBr139ib2eKa57PATqbsmoy_qR9xWRgW7c97igun7FJF9k5L3WfFbTyRooglep4WuhE_AsYKRUPPgAPf36h_L7j6kQTW0e6_KiQ42pWg50KSTOwKMq91YKtzB95p_vichwChX3khQd_yF-5TbExW2uyuoglpGCWnQzNTAWWXQiX5VaF9ILkdVpVbKlcdi-oHJ_twOIUeCSsbHZT4YMiHWEu8hLvSJE8mpTpxyFZl1o6NJM4Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsKyoqlWRxZf6A6WsqKLY79ChaiDquHD39QOxmIxMOzktVHN-Uv6zCX339QjMLgf_lLdBokRhJDEHkM46z0e3pSnKxt6L1GxuzFwhXWyZdT8UO7G7yqyXSb2bsT6q15F6-YAsEEHWUyqJtQ0pHFdGkizpSNXVQ6U2MbZA5_Vztpw8XrR69GBNHjEDBIvqunYTAEsUASrlXFazlRhMeEQGEx24sS6in00sFO81ppwZNnHLKvOaKIQLntFRqJpMdetG3Cd5an0iDa3VnSCxkjwTYEFtjXWCKR5p5N1evmZMID-jxImp1ZqN1aw4NzskMwtcDVXU9kyQuHGyF5oBLwE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W66tuXdqWeUDlZg_bwj6uGKJG340pdvjqSvgnl1Wjv-StwTDM3hQTjcxBI4KE73IhAJYctr-O3EdfSfXQpiSKCHRV07ffoWlNkNlh9V0n65XrZdPVgadKHo53cFGv1RlEchk37P7fe50hk9KbmI3Tx0jG-u5quZT06g_WJlAnjYvikSkgb7k9jwxjUQIWkETMq06ypdUTlFIAezrXEZi69gtl85zxzhQylImcAHjiw8t7S4f2IoBLVmli9Jqtd6qqbfLWVm_NWB-cSS05KCdA7jDgYh0az0BJUvC5B0yi-w5d2sv_AWpo7bAkGVDry46qfWuhoX1AVTdMNXhwNgnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyt0d-_L6C-mapZoWnLjEv_zUdsE4R6ouxtKa0W-3z-gpwnTms6ct97d2UTvAwEK1tcO3enI1--dGLbcjfeECqvofps6Iy0mwOfaWpMLprigsZL0pEvylO7xXyBYTyfE4dAfme7OsGAezLT5BZ2BUHCcnPKpyuNTg5l2GmFXigdOaUGyfz-wQzBKQjIJRviXE-C-35QIt_0uXkrnh4W4xf6wy1j-19K676cHLeC8lvKrApnCTMj3woMdvkfTbFowoULd5QT-6Gqvmh23xXH62WamBvRmrrho5vdFN3jpHJfiCpvZfE7HglRybaJTKHJ5e1pzxEmVdzDgNsrFSC65nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT_eFdm72l0lDVzw7nqmggVL4Sd5uMCwchlMXu4znszUaqXhOO0huZkmO8gRzXoT_gRlCQdn_r40TJhWDKI94ZlqPtipvS7JvhOfWJ3LnKJSwts3Y9IkIglzdM2_pWmgeJ6gPhg_J99B7iys_Lz8vBGKAa-7md1dcHspP7mMasrxcnYZASbRebX0DufYrp00wiGSNCt5sgS6njF7v6UOEuQdGf6t_5J0HvZtFrbb4EU95GBnBtDTPUVwIFEAZsCoCaeUihYeMDuttUPRVySMA9K1_5YT8sRfGA3dpQlScfde7VXQ_ShopIMifHmRUQUEBs4WYmLDrrjyE-0Pe82gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBrI-Ze5fOWwFtY6qfxsWI9C-uFBchttRDRIr_C0g9lwbQtmzxAaKI0jIt_dZ3WVYJW68ZnkWpyf9e1yjiqKcsjNZfmF7piZqZc_BpX91wyoD75gS7-IYTWR_VjJgIS8UM8Bk33OJw0C4tR6VXFD5MlNbo3abIJF-h_QNsRIvMY0rnWEbn9f9Q7iPw0NBogRnRZsIj7gTASbj-cVJnB45NHkILLNCJeMDGKOf_8v7y8B1UT5e_r_6G2GSoH4A1MobA9iQ2QnC2ha24adDRY_833XCT7ogiS9YmhR5neMJo-1Y5u1K_3NlYXpSsCuZx7JcclzOxFpDd3LqWzI1rfQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWdiwMDrh7zpU6uCZTWJdexgp69So8RZjjUSGtsOkSs7zsRA8DiOhtmBeie4nUDNoF_z9Y97s1_qdFBHMd2WIMJd2can0C8XWMjTqAhTMowemqh17a2F0pFdWchZ5Ox_CJStQ5Vc_58qVN3Grde0EeXiE0AdhNQxnRmpemZGjyb5gMlyulGzNgvYYEjv-DqmPVbb1Y_dRw6k03yU5fFGE8M97HD2XTLJfsH3Urqn7p0zq0r04iTJ8f-oazlXyyVM1VNvWsz15NYhGUxeP7BqCkaFxO0157h8Muhhv6y297o4Ln6Aa08VAXc4if0l6Q8_dDpfGHeVMeimdBPv_qs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBnkEy5wgbBu1Yoz1HJbbH2BV0L6U6npaueS_9SLljXhol0vKx459pwVlnxReP_YtmYR1gMu_FuNW1P8IF6Rcp54qZVvmIagGKFFm1mThqLtPDv8uwzzXo5VwbIjj4iFalCVeYOiydhyKNWs_b48jAp7YgmxlLq6T7vpXhSzVrofIqVpb7mjHTQC8pvC1Lg4Jw1UKjZ5wqLgrG58XeKQOaiwHc06wPsyqFYxZUPJsh7_SFcLfWCKis8U0MktTBd036CL9kHFxzcygfHHUGyAseBWyMXkxxEM3-UY6-Gg5wevVX8nWNDrX4PqouapDNkW0d-8m_mP8qvWdXMXI4kvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRA1i6EiRCtohnJSDyV3DVwmFW-2R4B7bLnoZoWlvgSG8zeleTVghG0pIuRPO-DVFvNvjmWpIe4vJrcY6RrPR_eclVfuxbxvGh_GxQ5gyHWJ7x-Vh37YkYWZVOsyyxm8Tg9Xdv0ESzcO_dGVXWsRRAfmcUzliYroh-Ut_7e7iXMS5Qx0qtxhfHMgSUOyltScoRDkKWV-DCCD5OVHZneBsGC8pfqeqlfwRoaWYWD07lSXO1vmUWPWcxhhEOrkHpkar65GyGhV8I2wKVi2xBDJRWJ5l5SgYcZ-lxBemj6mLt2WU2ECSaTFWr--nIrs_Qg72mHgQ3RoWWoZwfT20FWwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAXcR-s_olgEOWnNWf-OKCBCqSG6U6YNWdRuueK0oLPslTLrQY3aQrY6R0dTv7poMG9zfaSd5R_Wsuzw4XanyPPq9L5E5Uvz5ba0PvUHgwGoGMljfwrHIsJ6HTapN1lbtjBdvbcCXXc8Ix9H26TFf5O9aioAWo6X66oHgWlhqyyTBRKPLIC0BidupI12VxiITKBJRnbFgXfmTdRbFsXs_RLetAmSJrX8RV81DoJoLdApYSjk_pQGHm2y3ntX1WjKiJz9vbGK3I2bT8lrwuJAEpr2kSRewOl-VjU_benDmUe2ls9rHDgsfkmBQtsioJPIAaFEXRk_bxLkeZvEofS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoNF5vC5FssHsx8amy8_BoR99Y-nb6i33RaDgCM-rpgNhVuFXzil3DIpojC7s0lFvTtUvFQ2YR8t5daLFuBy-nrCkNeKxfz2Q5j-KE96ExfrYANXG6HTOAl5Os3Nd4bvaySddZLs1XHobvrAA8n2p9edRzy6yTp4BP6GBj_kHw9CfN4D3I_4iISU6RyHEl5t6hHprF_R4k6dN_aeUPOvt0zWT5H4uhYYzzmq81CCG-sx2zOvS9H8mY82g_-5I93p6gnuZHp0M0grDSyKZ3gssdYzpYHjGow2SZZY89cUKaIdN-umyya9oM66cGNCw3s7rGcOpwmrPySKBCQBbXvQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouZ0YSsQLGOVbv2HTZ9i0n4a8au9mReLqvoB4dh3CM4qjGt27T5bOzpEtDbgDzS25aikl3T2Kxee9Wu4yqdOArKqgIth2Fg7PmwH10BlBQ6WQndrM0abgUt8WVGkX2vN4gOeXoz5OcAbBoKLVk_d-fQgwqOd6WtQS-mWvnqpbahYoJJVXs8ZHbdLVrE_IbmGw9eaooBWLRIPoY3Z04wO2kPvH-OUQuXppDUywcDs5CZwbDlXhvIP1HvZiJD6fV8U6EViWe27FsZ-I8E87zSrDpFjbzuGEHNgpQIGZ9joAiv0X8RXf7999JkLkKuXNizeEYRD9q6tnQvwhm8sV0JRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-Fy4RtiTaeAqrsrREQiwBmdohv9uesjICyVkMyoEA-rZ0eLuq1s027RsYqMdnlxlX9BSAEfHlXLB1UqDArpBteyJIsw0OexEJLM60x4qrLmTSuR0d9o_LNBtX-5k2wKXQPB9sIJSw5CyZ29A1nqPa11uorV0lo0AJ6yyex8psEYhLG1S4U23TocAJ7zk7aAYti0ATL3ceHrr-LPo_oOUAZmI8Q4qSuKrmY7xju-a2IiCJ91f6GP-wy-AHy5cGEJcU5JemsBhLTNeTUOWRgAo00-sSWfDV7We9RqFE-phRJT_n1uNNeKVjkZzKNuwldF6qsNwWZ03LlelWhKTJ8mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK0f2y_l-H4Jedv-TNh95OaJvLNk5ugsKkUnK1d2_Pl4JDsnPQTyDOZg1ki9nDv-uEu-LBfFXBjf2CaZPYyS5JSWuj0-UsSc_Bm51ri-sm36_57gYaBfrq7LKd3PQ3XfJ2fmdOzMk14-MlZO-UtCEf7LdvN7Ci0O0K61VFeK9btHW3KwfRNvq0QiY_pvfP3sgeFgbc9nIky9jUsUDy-441kavsIIpSV1R56lQVRdO64-LPPvdT7756dEJcGk6JCK7tNCembXCYEaPYJUfM2u5MNCYSmJ8IXJKRW8uS6gZp6uESrm-9tsBUtjve0UdgLdUEbhXDu-Gs0Abkx6GfDZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfHClRqUXn5ljKMEKvbdTa0G2fT2dgOb9nKfeo0T20qnSLXwHcLC2Apc8wiPXCG6QG5g9QG0HzEVdibI7kIWQ5TPPa0SIuB4tXeM_SUKolAKJBYKTjwHCz7ZKFkDl5SldBbVH9Jp3p_hTPmkDDmMrl34g_k0LqeypoYZv090T5xSmNxuJRsckSL508szl4Z_Br8KkfvcJP4fGCY-X6BoCbQCPAna2b1a8YVub_GyNhPSc0KslfyiyFfBl82sbEeVwpqubPZVm8SobLx7vbLvJXGGc-C4cnAHQQEmb6vKhvZUo2XT1NJdPy40vE_phtAib9XAZRhxLOuqm-taY7PBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaKeKoCb117tpwuVUqT38AKa3VX4E9bAlVMtqqfF2k0bFehLluDkdrL8LZN8GY3UmMJuBYk1zz7NDZxpYVuRCy5-A-rtILhkVcII1BUzrAdhfW_fJnSTf-zfo-0WlNe25yHyX-3SHaZ-VcOH7VpXyZeAnksq1EqZHiQEIloKzqf61s5pL5QU072Jx5X1U3nrsvLQG64TxRffEQlcdWWVVSep5mWMf9ayIC85gLH4d-PqvhwNHFPSJuadH9RG4glCoeHK5D0r26XdvQTUAHrTVjZVslIfB43oX00AOKh7m_-k_3jdZNs5xkPxNOXZDN-sga9CzQdB_o29IC3KOyEMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cadIxgmmiPdPbG7gdOf4KdwgrUYhbSi7iQlp7k643nVMs_mICsiSfnfceDTQp4lHIMs5BfGbiHUpY3uTK6jw8d0oZkJVFSXkA3u2v77vi_DiE2nPNJJqIg1EZxMfygOOkFWYaPMMXLamQLlRJgwQLCTYTQC0oq6lSU8A7szb0ZlInBrlr9fs6u_P17zczmEDDGm3CAehEkbBOlnqtvqUNPkUWakcHXWRdUbDhu1ZW-SaeZGwWf7QhcuJbO2i1u-OjExj0yGuIAd902SQ58iJGuF6OoD4fdZSgKjtWeez9uKc6HaYgUbKEU4k5Hmyn3zzw2PWyjgvbA19JOgc7N0Naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM8vmT5isICxyAh4Ph7vSoEQDz78ZMDmTOhcpg1LrBqy_gjv9hB4d9kZy_RzFdOs58jHpx4EtZ85r5aGQya9wLMPtUh_eyo4pIPgJW7A8RZb42fQgckeKVRu_Hi9TJCQdswiiKOB_BNnAS5u8ROKxi1cM4Lk--9QkhTlDkhbEee5oVsSR7qts_Q9u5TBk15oE4mxn01lUZrsAfmx_FzhbNO9GHafSygf5NZP_ZCJBislFvOpob1bjVgg3S09Nf6A5aLi8iBV2f8IUkYToIyhA3mMNX1CTACm3zW67DxlyhsQJSJQPVlT42y6E0WDqZnRT707E1DHXLG56jLdcP3pyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G1lFBwyscZoM73E05uxCOucL0FVmBBL4QiotkLBvwovBfSMZ-HqUoyzd0nvXln-JVI5hPu2R_Drqz3LoJSPHa_KrL0_2HplUvByBw-uqcuLdKkqzoI3ynJNAFAMMs6NgDfInmo1EMoh8gruNsFPgFFvk9PBCwqEoPddpOpntPtLEcAlQVP68eo1-YEmmjPgVLq4wI2M4a-cSgWrG9_lUffLFwcDXUHCZ3LILThdDwV9cdvYi93tq4rKVOj0OTGBMUMzsgZgG--shwTcUAIUJBnxATmsdru2i2KcIP28THZM7q0GEzifurrtevURCKky-gY6rCzviREWAf9ECxd-NbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSOg9EcwpNyFaY96X8C9E6SI9Cwt8nG82zOAtBYcWGw5BwxwfAB93ywPZSk4KvT7TeBjk_oDqmqRKqCvaAZ7KU8JZE1_5aNkhQOCgfRLTkx35zyWrRmyxVRbBVXPgvnky9oL6Tv7c3j_gbTTGZccTU3by97oOlmgXbV37JNFRO-vluXbjecnPCd5KR1m_1O7YLZTxoG332FEiMJ0NiRWcqYlslQEpjQm2P9KFxAi8iHvdaUtVj1ndAs8cIBeelX1GMBbi5KV3ed5hroCx-P9uuMotGPYMkthnVQzItT9wAh3cdlqggIx8dJ4hoZUsskffDmDtwWn18HN8Mfb-kRceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGAuIJ3M5B-JgrH_3CAICG8fFI04GDI7Zu_IEOEE7Q_nTkt7fG-42OhKlNcMw6fNFZ5kWcpoIWbu3RtV6QUlp4bx1LoQmg5Gug-DlW752fOWhjiLTOzR6-mO9Boi2PoAwKpIB9aZSW4SkMvLjca_sgiBxJLIhdXyLpE6nBoh7GI6TayRvIDv8mZZFft-GP_FFlriv7TLPYLmGXbpXMSW_oEITUaQ_PAWG-ROUzZtdpd10oKJznWJ21VKefDDlBJKdWMo0VzYAu4cKF0DjVWHuTkUn3ly2o0VI3c17XgfR44OSU_oiaiezJV3_4RhdyQxlZRkXQOtCKL4Xj4O4Rcmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJGmJnkSrXjoF0ooy4WpbdK3-INn5RqxXflRWEPqPIwBNMqHAQwBa_10zMPyg3rDG9gPWX9LIqSjDrk_rW_mpyo0bCPKwWZY4-wovCtnkMmBBrPmesA66SBRnZRIBgXuFeo27VJ_9UVE0X-cETfQGzlClv0g7d3oRdZ4pAl0Ew8_D4FDD91sDwcq6TKy6WLBjohduZDhEz09tdDyipOOOS--abu9cW9qq94e2MniUSPdZAAVM5V4KyGodgtle_gjDlOmKqrPHo93aP0_7p2grae1OXkJ_FSlWaevY9yHuTPunlu4sJwb-pemOLkEHwEHxJfCQCHPoRwtYielbqiziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK7nqyUjn4PsIfEB7dFwzvXw6ddvMVKXbc2TqWnu8_PGSwsneVRDfle87S6VQqKvdy7aLOM65x4xQIiFExSUCFGVzA-OOEBdUrGYC_55I_WnKAU9HQxr1yWh_mb4kb7w_LVk0hiDQR1XkVpcruLYO5eBfZRGIP5-G4BdTW17qRUuWsRKwrw5D_TuWD2syPJnjHRn_Oz4wmU_l7Zcjc_GnesawCJQ-eYcT4rDzogxOehhCByxrN6gsTy78BY4CvqJaHbakwKI4dSw4nxJenTdZuCqM9lZWUF2jbh3ousTDltEsjyAx9WkKztvqrAyvG9f71M5-s_Snrf8rPKNyJznDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmm6c4FRzsiOASYZR_6Ac9zIerwTHRf2CmJbOLTxyNVtHK_1pDS3PUnIXCEqk0dcIL7fjsHzlJoL0qPEg5_jb7lBsskldJhG1KHVjrvi-pi_szMb4aJCmVYxXBrkIQrIyL3VLpVz-cYpbq4UA9gUoJR7zIMtLxBHDqZFxlzdJcbuI2rmRF51g1w9nrPHXAgodPH1DLbpJhXdo3G2-oKQZKtgHpJINcjCTUZ997IjP7lbxnzKdioAw98xhqZCoUoRUrZCoiJMQEHcMt9J1PorqXT19wTxwPqck39kYl-lHqBswKA_spEcVgBKBuzyK7j2to5VANgG-_xlWLBQp1ibvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC3pgtRepW7_1EvYg2QrbjBWpzlwFvRjGJFyD7CktuPt9hPKcD5ZySYHcE1YunAHDYBmohmWZLZrL091sC3i6FRPEHd7dtudcdxwAIr5uum1TmqhlwEiqL1Lu8QsMD0e-2cAVmyoaD7oDPxU3YuHTUuZpZXGyZHR-IT3tS8ne0upZLDJFW2U7C8vSzg9iUIlbShqwEMB2H-MRm7tzA-7dWx8h0LGJpP3VpFGIq68MCwiGlAlwhYVWUtoldEJtC9hz85zwQOqCdB8RtNQOMmp7sHbu31T15GrFzmF7IE2y6HlAd_cU0U_FwYYNmbtfBHuBll6Ab1BJFcpZ9x_LTWXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACm3WWHiwsnOjkUKO21X4WMWbBCFD-liUevJv0bL6tdGlsesiw3pnFcD6_vLbs5YgJrk39sPTtR99h5b79nwfV4liyEkCxyxTKHqX5Lxfd3DTQOh2jNze49mfg0qZYzSQwmb_x-7Uf3rNAGNdqZOucxVxfkiYtm8NTtcK5Wbcxu2GpED5Q3iWiFPHZUlAgi5I4UpnippPf27z9F9nK5Zw5xr4WTUtVhBt-gaFgjOa-C1S67GXM5Vfrm8kFueRvv1vlswcoal32Oh8CFr-6abaD6S11ti57tC_QdMmVD65STd38xuUtnXHoHp8zlXhAWeiuznYffzvVDZ4Hlo18COsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0oFsXSdMMJRj1MWwuHADrv4mGHmwvLvhosQnL3ErOycux-_U6UJGxCQsrEKtZo6B7SHvjCATzrsgPOA4J8PIJyQyhrMfMG6gMEmza_Yc6TN3c0Y2L5rV_lvev2aDxuonXLs1Aqm1czNbxHMyvv6DBY0hV97blNny_M7ZumJacX1n1dXGyIPClbFTu658GyXLfOseK8Ii8Wz9XLwgNOh-MsL_8wDu_qEuIbRdukb_d3a4p7b6Zm6uWUMbVr1IB4mHIMp0Zm6DPtQV7kNLg3_wDWTPupfE8WdgV8u6rqgJ7QMhlJ3gGHv7HRfsVTOC5JHRDKR03bbMfTyRifyIc0aIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K65LTZrYOUTRBtD6bGqZZBWS3OmZ1ur7kpEj3kj9JHV8BXbPQq7ZvQoKrlkzJRUi5GZPaVd9Qk-dIHdZ8y-rHlIP3nZl5dVGOifX6aIxzTfQqkon6KF4dphNBdTpaWc4Cb7Tmp3UQaYTlBgynj2Cu2YfcYu_Np2tr1kJcXgMQ1Bo7BXuAM7C-VhccMr2jj5MAiZRnqQPXGWrd9s94rC75SqLumXyeYzjnlDtItJlXddDY3pclSA9k9WtLza88EBNcn0icIAN283OIPBLXn97VnRt51f8WfEe_0ZYISUObq2N_TBh0Gh_sGlw4HRoH9mJSgiDGNE8nU9VOc1VV8oAzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ سال بعد، او انجامش داد!
✅
📊
کیلیان امباپه حالا:
⚽️
🥇
آقای گل جام جهانی ۲۰۲۶
⚽️
🥇
آقای گل لیگ قهرمانان اروپا ۲۰۲۵/۲۶
⚽️
🥇
آقای گل لیگ داخلی در فصل ۲۰۲۵/۲۶
تنها اوزه‌بیو
🇵🇹
پیش از این موفق شده بود در یک فصل، آقای گل هر سه رقابت باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=BL28kb-ry9O6Sz-ikIx_WMel0enb3Qp3q4yd0_u2SK90A5SKh63fZiybLQEbMD5_4xf13p1-xlI-KH6BJfXh1ia9YXIXxH-AclAY8R1ij5Dlx-n0qu121jl5-hbUWqJzoFqsUm16kZP0AHpOYVNnq5T6hnjoxtqMfhOcl9u4rAe_RZdF0EuzG7mw6ymk5R-LbQV7asCjs5f9caUMh4zwoAu7kzf8BePrX1J_3jZPSO-sdXUYYUJ0qpfJ1Alu74p9fEVc0l3K9OzxlBuWv7GDka8utuaqhFLS1iMzUnTD7vy2bLBq8YhmyJG4aK_TUhc5qbPF93J70pU1tyAF2ks7yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=BL28kb-ry9O6Sz-ikIx_WMel0enb3Qp3q4yd0_u2SK90A5SKh63fZiybLQEbMD5_4xf13p1-xlI-KH6BJfXh1ia9YXIXxH-AclAY8R1ij5Dlx-n0qu121jl5-hbUWqJzoFqsUm16kZP0AHpOYVNnq5T6hnjoxtqMfhOcl9u4rAe_RZdF0EuzG7mw6ymk5R-LbQV7asCjs5f9caUMh4zwoAu7kzf8BePrX1J_3jZPSO-sdXUYYUJ0qpfJ1Alu74p9fEVc0l3K9OzxlBuWv7GDka8utuaqhFLS1iMzUnTD7vy2bLBq8YhmyJG4aK_TUhc5qbPF93J70pU1tyAF2ks7yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWXidWDN273NTD3_3TaZqfkMYeKzpNE2XRKQK5tejn4on6CX_1SSqzp03Okp2ohc0pD8Lmxo-KLTjjv2fYhqwcH1hnEwGX8QhbY1jMIFkcF-RMRgkaQHRR1xaqF3pHlbbK_B8C9VkBs-iMmywY_xxPr7lA8ufhr_yJq6s1skb7udpOCvIpVOukV5sxLF2kK6G516G8NCYfLm0cxbWPqh__ZmfRoJO5TgfVju6IluEVyju2KfeUnRMxzOeX2b3uAM5kbWOCVEibhjjViQSHAr1NGazbH5KVKIzZ-c5FXglp0JciEVLhMLpAsDvhvdncwIdO4o5ytjH7pHOQhdUn5Hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLh3JQ19NFZkN3WmoVjkxHUujQiuKRLPnvI7Vslg6xT_84UvSJAyx_0pFgIhMRLb0jv-DVCp7J0FFLFAfll0PF6SvvnkJMaQft808D3Px_wEL2vg9rf_XUEXQEnyIyFAYCUtFubMzojEaR7s_hw2xaIT2AEi5j5kFTYQN-1bhZY3AW8h6TowXISmiuItxWEPeaI-aRdC0CW7ssADn6T3VadFbwkwpCs8V-oOrK62iQSrrFwiVW0Nafqix2eKBbMwyoR-7zdbwF1IpmHJ_IXX0HXaTVmPTbkTxgnL3U4WdQ1iOj7ZIUxLNEnD6Y1JpcsUtOlM8F_2HYFX8rhHy-Y6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYNCsQoiwn2MUNlluP9V5ZorGsrsWlUjROPyKIt1t14I9IoGAU-5V8t0gioWzGN5Uai2-UpwhxYYVDcLSy16bUPlKvzvhahn1xy2zax2z6kSkvaIpm5NVkGE70uGlygRkkbHaGNvH3xk1tPtPYk-VgV-u9MZs85Ve2AVmVtG6wivHU3Npds9peP2LnVrf4AmATNUt6mUxTPPAUs5rLBe_UN-6KZeH-ModLJjwpV8pamOXWzNR_edXdCAtCewOocw73-Zu_Oe3pXggFebX8wplxUKJWDimo83d4Q1KNjCauzV9xDCjBEW6L6o7YQkU4aqepmMtf1_9y4mQ16YfeZtYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_fkt07F1OH5jyNXUjrtZtuACF0DcbdSEELWvYxA3UVxBIqQDo-LOPSBfxZtO7tRNtyXRzWI8jw88SmBmQbUH0CI6zWPO7DcaTl3GyGxMoLqrkPWdFYuuvXNHKIuJR1nGuu14nzv6gsOyZdrqYHZF1E2KjZ52b9q3F1Fjy0W91sJMOyYSzQ10g5KrzEA5p3ALSdPs2cqSDZ9hW1Lm0OomxQKBxy7da0yQwoYhn2P-QwcW6NwF5TPhE3VIHyMxHP6vqpJzCk7fhoIvYeyen1yr80bZ_v7dq0Gh_z0A6aKOOv9JHL6FaRIFDfzpnDTl0hWH9-M063_XYxZ5jYb7tRAHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueG1fg7Lla3bzF_bXqqwQ6ay8SiKEq5C0WXVcxSopWn-A0jsC9poGOoeh7ITzHWKdYuJRrukF8PBTE6j4YipAAVjnd51iMIFRWA-5UQBOnOGR1SPIR53XXYkgfW3kvroYd0ftbu9or5vFtdkAnVDHyW4tXbRp7eL_HQwkmM-1RsMz2WY7LPJABxHJ6DUnjAFBaubPO_5XSQnNZuayd-t3FGB0UEFCOU-eyWoCdq0fCBnZEGw2jgVlegjtItWKDmo3Mztz3TBQEF-u7TKbqc9RF8RkU_NK54m32MA90oiC7IU_jiPSRJLcBIKUf4QmWC2Bg8OEp1qWwp8hQl8qwL2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=IXUp4s6oOOcdHyiS8-QI0nTUaSDafcu9c6_JpD4hUZbcscn8JhG-Qb_I1Gnbepz_NCyp70Y3r6V4nnXgSmgglvAwIyvkrGG_i-8cOHIuw8oCGabYQ2XQ1o-T-ZBMzOXapGKCDiOxKpubmTtz0rAF_rysNt3aQ9Zd7ZrBIqh--vVUfwpmdmzLTpkHXH5C5akT1FlVKdUt_t7WAHDhxvJW8djuSvPbVbwQjI9XTcdWlYqaDmthk9t80v22AL2uCWipsrhA9_xRsDnehauGPBU7Y0vihAA2xSjoWHWife7h1mVQ7WCeRfdYqsIFSARmKpZtEbgpzIQyLgowmwNt92VW6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=IXUp4s6oOOcdHyiS8-QI0nTUaSDafcu9c6_JpD4hUZbcscn8JhG-Qb_I1Gnbepz_NCyp70Y3r6V4nnXgSmgglvAwIyvkrGG_i-8cOHIuw8oCGabYQ2XQ1o-T-ZBMzOXapGKCDiOxKpubmTtz0rAF_rysNt3aQ9Zd7ZrBIqh--vVUfwpmdmzLTpkHXH5C5akT1FlVKdUt_t7WAHDhxvJW8djuSvPbVbwQjI9XTcdWlYqaDmthk9t80v22AL2uCWipsrhA9_xRsDnehauGPBU7Y0vihAA2xSjoWHWife7h1mVQ7WCeRfdYqsIFSARmKpZtEbgpzIQyLgowmwNt92VW6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbFJUu0-8NR8WZiz6qdB1qaQBW9jQfpWr0ox3pgxPd90IHpXJSmPLlp-UKzXn6IM0_r87sy_sqrgevh0-6xPRyWPzGAL4Q_bxskyA-_ygWTogNGD1PYSAjak-5YxHpv4pYUeL1WVMRPFZP3AO0ei0ad2XExaasqpy-rBIbFQb71UmzTBFyh71gkfN5PmkLnbvWqW-DqqROAupW4U2tIuQkzIXmcdA1izWSmdQ_BmfdE30DO534c4bV-l35UtNKM7JyyW9RnI_nEnpEcZq1DUo1w7dgAsw7arDXlymk90aMqtcgc6RZUKsl9U8zJy1guhDezd_mTwo88tdkSiwAsLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-fFfAXEDZ9j-ADHbeaa8PstV1SukDI4cksNk1N6aj63vTl46LQ0f9z0_poYSRmtHZbqV881-QrWR8WWuUPUQpNmo0_22PmzHZnSiEWMWoRzaBFYiB0o2wKAApimccWXXzYxO-r5DHbDSiie0va09NBNvhDuFSu9WN7NbfXLPl-eaG3tbxqdx_P4NhlpAED74oICY1EMPfw71y7ub7O_06P5fcvBZkRfwONKM9GGPSO5XySC1_BFFLHqmU8lJLF7UqttTgEp0id3LF0W5_4gKyE5fLLZcZxWNBPFw-GCRgo_qK60hUJq_B4bP6STZn2JWHxFfK0PetDs5DcOoFRNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=qc9eqp1fA8_dUzvz99qpu-Df9IPqkirVjBUk-8_1TxBW5Fr0OpMuxg0q4mtHzIrmJCTlZRq-SpCEeGrynsWxbxTHTq3sAsmdknn55aBCR-1uIWG2w-XUFGg5BoyoDBHkBKRutlEBpBbW2n0AZECcTRzq2zmzLnB6AP_I4bVNEuI_9b-yTrw8XA8oXdpzTUHo-ymwmnrkpIs9m_kpUKWOtIfhpuxg6O6UTRS9YHcNRpUMir-vXAqJxi4D9cVGA36nQeQ_r5eFueLbgr_r2exBivXdslTV9UqVXWPqzUhDAuUDBLQ8U7hRe_f9hCpyF_GDRXqTJ92ybtsfSB-AkaJSPyefbbbG7xyWBf5jFJwfLFgfwJfvX20GNAaiysnRrDHCcD321EUgolCbf7OsAQ5dypyVjp-0G28VDQQQwfUfzYomZ3DuUGf8c2ELC4rPi-WKAFMmDiNd6TrasZ3hnC3G_a6_lUkSx2BDR8N1BlAwaPtk6duXXCOAtG-FmoWTPAZh1S3PAJbBGfDMKnYJz3X5712gLJF1jrAvJYKCFC7pntj0d02F5f0psDL2dM48HQiOrIFr6lbc2qD2YtkSVB4lEf2xMUS7jOeI7OVjx-5M-dyvNevX1x5LT5Pz_QR11jLNzIInFkpQ9KO-WOA4t6TddZOWTVvjfI6cng-syltErfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=qc9eqp1fA8_dUzvz99qpu-Df9IPqkirVjBUk-8_1TxBW5Fr0OpMuxg0q4mtHzIrmJCTlZRq-SpCEeGrynsWxbxTHTq3sAsmdknn55aBCR-1uIWG2w-XUFGg5BoyoDBHkBKRutlEBpBbW2n0AZECcTRzq2zmzLnB6AP_I4bVNEuI_9b-yTrw8XA8oXdpzTUHo-ymwmnrkpIs9m_kpUKWOtIfhpuxg6O6UTRS9YHcNRpUMir-vXAqJxi4D9cVGA36nQeQ_r5eFueLbgr_r2exBivXdslTV9UqVXWPqzUhDAuUDBLQ8U7hRe_f9hCpyF_GDRXqTJ92ybtsfSB-AkaJSPyefbbbG7xyWBf5jFJwfLFgfwJfvX20GNAaiysnRrDHCcD321EUgolCbf7OsAQ5dypyVjp-0G28VDQQQwfUfzYomZ3DuUGf8c2ELC4rPi-WKAFMmDiNd6TrasZ3hnC3G_a6_lUkSx2BDR8N1BlAwaPtk6duXXCOAtG-FmoWTPAZh1S3PAJbBGfDMKnYJz3X5712gLJF1jrAvJYKCFC7pntj0d02F5f0psDL2dM48HQiOrIFr6lbc2qD2YtkSVB4lEf2xMUS7jOeI7OVjx-5M-dyvNevX1x5LT5Pz_QR11jLNzIInFkpQ9KO-WOA4t6TddZOWTVvjfI6cng-syltErfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amiXe2N3ofd-D5S8FvZNfluJYvpFT7NzJngLVN6qqICGXYnJRUz0fTpzEb3BDcxcS5hw_xplLfT5pY81NgNIThMF8v48PvZrQqSIV7O0nSBDcerNld6j4YIloYffNgCcO0NOkPjn0h_1oT3vQdAhY2gduLnl1DKZI3JLcc48HTrz84ZPXx_KR0ydUjxXDNCwg49gzttu7nbJuQ_DvuD3YYpog6GlTJV2c-keW530-o9D5P8tsHaawcVwNbmniA9ISd3g5o1TZyG_DbVY1QYJqPbERNv_Dr96adWwDW1WpE_2rbijY3TNcR4oFiyt1E2vVNgVBDrwkJEGGDauNXarwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=MBy6MmQ2AvAvICYyxUtYMXyOAJ5MivqGBDPCDgTE-XI0A7KMPRbTB4p3W_YAuAEyDC3ALpw1pLkqCLVxo3Yp8TAfRq9FvmcikPH7pIxz0021POFQfUDcdneZMW1ic1obEshLNWRW3K-4of6dzwoz1PTwY3h_V2E_3epLPHBcnMlvrhw2-OGjFLtBqIuYH31KutgxoUQ41riz_oKdYn4gOG9bNwJ_xiPyqmgJgl8Srvj4imr90ugg1x4OuFBx4lvbJu2Bo7F5V2Ge5RNBEo-MUmF9kIQHXGKMZ5O0QvmET8Kl4efRXk1pI-IgHYRa723mV70Qn6Jlib8LhnQImreFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=MBy6MmQ2AvAvICYyxUtYMXyOAJ5MivqGBDPCDgTE-XI0A7KMPRbTB4p3W_YAuAEyDC3ALpw1pLkqCLVxo3Yp8TAfRq9FvmcikPH7pIxz0021POFQfUDcdneZMW1ic1obEshLNWRW3K-4of6dzwoz1PTwY3h_V2E_3epLPHBcnMlvrhw2-OGjFLtBqIuYH31KutgxoUQ41riz_oKdYn4gOG9bNwJ_xiPyqmgJgl8Srvj4imr90ugg1x4OuFBx4lvbJu2Bo7F5V2Ge5RNBEo-MUmF9kIQHXGKMZ5O0QvmET8Kl4efRXk1pI-IgHYRa723mV70Qn6Jlib8LhnQImreFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onoezyF4hLxnTILzrITtY6esAuIMIQM8oSNg7CUSdeV-QCXjjeUB4g7_v7hJvctNKyd0Nbi5-4lJWbjuukQYgCAqalWuR9SE0cy1Jmrd56vCzQvwGUPANyr5aPYz92TWMo8DLcSLflRthv1bmyh_M3ind5QHBKMn7ePqADS39HT6xwWUKDCKNbW79KHCtsAk02JT9jF_O_ZydSejCimRQHP913qqCf3-fpJ8pKLNP60KGJeJJidSGk0w_5BF3iaan2jjg99r_jNucoDEQTOSV9WfzvtwC5ZFWxNnAqkwt4A8PIl_fgne5uNUdwJ75kn4QYKSw91hpcq44qtEDNok9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVDO5Pe-qKRRzVDuvv6LdEhyANjkl9vdfmDMLSgTk3N6U3Wu7YHBvPNWEgP0J9WO6SAfmgWsDZoKi2PpR0_Z2UOX67pv468rW-VR-IPwaff9wg4IdzskiquMFFBRpzb2VYrF2kPjLIZ1LZcAvwjU3JV9HnZzoQkZVtfgFS43k9NrReR1HqVjZ1R5Uq9PFihzVq6XqHT7CGqguZ74UwUTivOR8HAX2AxRtSqvL-O9ur9AIhh5mHIdwuqWNkabhF8qLi4WOr1iIHpFys_MZm9sLFq7WsrTb8pBCcIAlBkBG94jUwZSgf-ZlT0zutlPp4GoeGU-9PnYyhlgC5yiZTJoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy4fWa7B9yQq3u_eQnkvtGgdviUuOX_MvOFlMdxuxCBDKWjTOuC56uti8p7nknZF-t_qqZIkgNVCqdB1PMrV1j_EvDwRC3u-3AhM36xoY5QMznptuSqvGh9Blevqa4Yp2ykBAXGGyoWM3qPfNDZ-2IEDbbv9SacMiIiODreaH5bpcqjTcEu8pxsk1jAxVlbyXL6VcFYMB6rCpiyzgGe1BZFzW10yOso0TTzutcGPrFe9vY89sfysMYgWQy70v-oQwVeAJ1F6KNsDFZVf93zP7oBNoMVNqO9qs6y5gvPbdI7DLvPEATHPLaU6gFPV8PurHoNResZtBLY-oWKtZhPCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=iEkVej3XidgelkLTq5kzs-Dr4L0XSnOoGJbXsU3l5EnG7Ep3SN5NhgmY-Ny-dGibNnjX_KtQgG6fgkW00ZkNnc3H9KyZJymna-FFQzTy-3gTmMZ2ho3tEsnkFayE3Hwm9_V0Wen6eKKy_WatMuHrZbiiEtEubUxt5OjKuPdTKsXEzcCLX7SpMwTqZ_DiZhexjUP82rAS_NFeLIrUF7t2JWAaRovZ87xXFx9MGY1ePwYFk1WmgQwBBSGhl2lLvCYCWrQkiB-ZddLCi5TnDWoCbZ4omzNJNiDrZpYZ0tyJACwCHYsHvtTxR1QeP93f0zeKwYpa8_-qMBvsfXhNXV24TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=iEkVej3XidgelkLTq5kzs-Dr4L0XSnOoGJbXsU3l5EnG7Ep3SN5NhgmY-Ny-dGibNnjX_KtQgG6fgkW00ZkNnc3H9KyZJymna-FFQzTy-3gTmMZ2ho3tEsnkFayE3Hwm9_V0Wen6eKKy_WatMuHrZbiiEtEubUxt5OjKuPdTKsXEzcCLX7SpMwTqZ_DiZhexjUP82rAS_NFeLIrUF7t2JWAaRovZ87xXFx9MGY1ePwYFk1WmgQwBBSGhl2lLvCYCWrQkiB-ZddLCi5TnDWoCbZ4omzNJNiDrZpYZ0tyJACwCHYsHvtTxR1QeP93f0zeKwYpa8_-qMBvsfXhNXV24TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=rLEOatoe-3KvOAsSkGRlulWFeVhX3DXwtkC8Nwyssk_QLgbRalGIuR_D5zq4HXTdN6L2wJOHplDedo20NHOkppgoQshXyoCnzHWqmj-PoAPkcH9Qmf4kHZyqyZdspM-Q7NewkHLqnr1srt59lhE2YLFoP2Hu1M614E5yJy3_bQb9fNjyUM1vXkJ95B-sC0W6aGMLXtLPIFHXqiFeTMeC_5kiZdVH_sGif5Nd5hc10kCbZh_D3jYzIR7ruMGqkkUSPyvoEvdvxnDmuibMM03OqFeVPZ6J0qV9DPMu0SNuGV1et6kXf5Hs_Cc83I3_m-t4Zq2magrpN2wsA2957k3053d7LA4ZyVg8x13OPYFq1OQ7g_taon0Xn8m5fPmq0XWE8DqY305Qgoxq-Ej5Cm6Ya_yzaCrAgLFWkexowkak-g51NkLcCF4Ba5rbCo2Ufr679iRtQ8xZ_5x6kWIS--ME5GLvy6lZUna-tFglvEze-CzVqdN_vUQaGxwg4rO7bMri-ViEGpIkYbJeVex6BwYhkdZvnsK9jP4xUBuVwmV9eTRS5yxBeOdDgzwcAs_DJ8QOpARRxFVnGkeWnOk_rFRdXYZrLZR5grflfoiea3ANFhbd0_ZMRxxIa6MFdY9XQxal6vXbFHUyoLAu_mhP3NqVNIddYFW0v7P-fQo8P2RehPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=rLEOatoe-3KvOAsSkGRlulWFeVhX3DXwtkC8Nwyssk_QLgbRalGIuR_D5zq4HXTdN6L2wJOHplDedo20NHOkppgoQshXyoCnzHWqmj-PoAPkcH9Qmf4kHZyqyZdspM-Q7NewkHLqnr1srt59lhE2YLFoP2Hu1M614E5yJy3_bQb9fNjyUM1vXkJ95B-sC0W6aGMLXtLPIFHXqiFeTMeC_5kiZdVH_sGif5Nd5hc10kCbZh_D3jYzIR7ruMGqkkUSPyvoEvdvxnDmuibMM03OqFeVPZ6J0qV9DPMu0SNuGV1et6kXf5Hs_Cc83I3_m-t4Zq2magrpN2wsA2957k3053d7LA4ZyVg8x13OPYFq1OQ7g_taon0Xn8m5fPmq0XWE8DqY305Qgoxq-Ej5Cm6Ya_yzaCrAgLFWkexowkak-g51NkLcCF4Ba5rbCo2Ufr679iRtQ8xZ_5x6kWIS--ME5GLvy6lZUna-tFglvEze-CzVqdN_vUQaGxwg4rO7bMri-ViEGpIkYbJeVex6BwYhkdZvnsK9jP4xUBuVwmV9eTRS5yxBeOdDgzwcAs_DJ8QOpARRxFVnGkeWnOk_rFRdXYZrLZR5grflfoiea3ANFhbd0_ZMRxxIa6MFdY9XQxal6vXbFHUyoLAu_mhP3NqVNIddYFW0v7P-fQo8P2RehPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=AnKBqwfPo6rcc1YxtuWVDmnzPcqOYduP9oXQIqZb7qOa7oYd8IGj8WSu8gFVirBQtziOjaHlDrGvGer_Xm2rzgoTJt0rHcvyeTR_UzKbgI6b13zi-w2WhtnC1STuihkn82_5fH7F_vQsrTb1F13HRcjdEz0JLkggbLGoj18rj3qBPNWCMiWkvwlWORPGmofy0OReM6FSe27aNXZSmM1ISidNfumRJR4zvq2atLcRihsNTJ4hE98HGkCTgX0mcVmAps5frZVNntUuwNNjbKrLenRADfiugTkNIDbvyv9K65HMxl8OviyNSkzgKINmU2FN72WttDeuMf_avGa1zVZlXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=AnKBqwfPo6rcc1YxtuWVDmnzPcqOYduP9oXQIqZb7qOa7oYd8IGj8WSu8gFVirBQtziOjaHlDrGvGer_Xm2rzgoTJt0rHcvyeTR_UzKbgI6b13zi-w2WhtnC1STuihkn82_5fH7F_vQsrTb1F13HRcjdEz0JLkggbLGoj18rj3qBPNWCMiWkvwlWORPGmofy0OReM6FSe27aNXZSmM1ISidNfumRJR4zvq2atLcRihsNTJ4hE98HGkCTgX0mcVmAps5frZVNntUuwNNjbKrLenRADfiugTkNIDbvyv9K65HMxl8OviyNSkzgKINmU2FN72WttDeuMf_avGa1zVZlXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=q5ovWX09GzIvwSDNtDk3HyDx21tY1C8VJadzW9z-b_DRXZS_pqayzF8mw0VeSpfxIV88m_k4qk6M5J7Jredz0NRz8ahpMtLeAucBb20TdwjH0gHjTqiytVzKsX2-WG2ddz9aoYz21nFqStYpIUZvfZTJNKZ6jaMEOzA6CsmRCFxN-J2I2JgqUjdOZ4a0DC9WhLvlKhsDUeGfkJCN8Sz_uwNujAxMeg_tsWJSap49GFRuKdXaCXDAyQhxcaHVSZvdaCPHN73W8gsZ-ABYSvUlJQKN4QULrMiPaCMV0WHe6ckdnKEmg2HA5rrgJHyQal_YHJ52sC8uezDAWTN9p-3wVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=q5ovWX09GzIvwSDNtDk3HyDx21tY1C8VJadzW9z-b_DRXZS_pqayzF8mw0VeSpfxIV88m_k4qk6M5J7Jredz0NRz8ahpMtLeAucBb20TdwjH0gHjTqiytVzKsX2-WG2ddz9aoYz21nFqStYpIUZvfZTJNKZ6jaMEOzA6CsmRCFxN-J2I2JgqUjdOZ4a0DC9WhLvlKhsDUeGfkJCN8Sz_uwNujAxMeg_tsWJSap49GFRuKdXaCXDAyQhxcaHVSZvdaCPHN73W8gsZ-ABYSvUlJQKN4QULrMiPaCMV0WHe6ckdnKEmg2HA5rrgJHyQal_YHJ52sC8uezDAWTN9p-3wVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-NeTSbEJb0AEyyWDIe8mfQgWxgmFDVeCc4UXNRHO233RwR774qSVs3pmBnkQzFr1kN5S5VX4-hpTRI8LYZA-bFLFHsEG2vWZKvy9gHI6ohSMbRKLSgTS_P-V_OGepqQbEvV52SBRD9Sp8-m0m3MjDzxDciR_dCjG_RgXRv56q-v99Mp_mQmp2vKQmwunqMnvnzVozPBr1X8Y5kFsuRfjXp3FtWb-CHXxP7PgdLjgX80SOlI_Wi58BjXt-NPLalNW7E57LaKq7ZnGm1MBo29Dm0h_TNHocMKtda8ec7f0tLnLGxQkvEhWtAHM4sGlMsCXFp6O-dwaiwq67OF1cSAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=vPBtZoUQ0RftdjbgoUamacfABv_UBu06C4mf3vORu1AvBqu6wbjk1Iyry843DO73cPvonjEfZcospTJyr_je_RynFDw9h2FZZZOD7d_Ow6xrKvIBOuoxVYQyID_YCTUJRnyO5EuTaQWWf6N1FKglir90Jk7bSV67dfKjnj2KR6rCoi47AlUvD-fcDK7I4FqbxHQhgg0noHAh6smMxQCKC9Lcisx1M9EirR82gSaRmuxuur-LJuvjUiiRbvn2ws67HZdwIzQLulVuLqWA3Ncxt552hAhUGwRFYxAWWFrzfB4vi7VtXVzZQyFU70jfCEIJu7-NEjqszn6N0TUWGJkN2C0X7XuBcxJITJGljnplI2TUGYtAvFzjRr2wQzCV2oW9f41MRPqOyKqXnCPyLiBCDosJUYRc7zJUDeN_k3VjeyeWp75H9wnlxAREyclQwRWkSPsXHnFfr_-JKILXW_GzWpqT-fpxBknvezX1Xvcuh5qcDlLIroavDa4J7La1oqdC67chyB_49gJDlvPdNH8_EQQvuh9gV4qk4dGzwqNDhx6zSzzQBqZ2qS7UNhmocj7DDDU_E0yQ7v7iHh8FP1Obrfucm2jC5u9Bc8WAlKKT0VctSE_KqGg3-FLvdFCpMAFfnKmJjHo4UsGQN-GMr1pl4z30tABnljgRd_QCx2zTctM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=vPBtZoUQ0RftdjbgoUamacfABv_UBu06C4mf3vORu1AvBqu6wbjk1Iyry843DO73cPvonjEfZcospTJyr_je_RynFDw9h2FZZZOD7d_Ow6xrKvIBOuoxVYQyID_YCTUJRnyO5EuTaQWWf6N1FKglir90Jk7bSV67dfKjnj2KR6rCoi47AlUvD-fcDK7I4FqbxHQhgg0noHAh6smMxQCKC9Lcisx1M9EirR82gSaRmuxuur-LJuvjUiiRbvn2ws67HZdwIzQLulVuLqWA3Ncxt552hAhUGwRFYxAWWFrzfB4vi7VtXVzZQyFU70jfCEIJu7-NEjqszn6N0TUWGJkN2C0X7XuBcxJITJGljnplI2TUGYtAvFzjRr2wQzCV2oW9f41MRPqOyKqXnCPyLiBCDosJUYRc7zJUDeN_k3VjeyeWp75H9wnlxAREyclQwRWkSPsXHnFfr_-JKILXW_GzWpqT-fpxBknvezX1Xvcuh5qcDlLIroavDa4J7La1oqdC67chyB_49gJDlvPdNH8_EQQvuh9gV4qk4dGzwqNDhx6zSzzQBqZ2qS7UNhmocj7DDDU_E0yQ7v7iHh8FP1Obrfucm2jC5u9Bc8WAlKKT0VctSE_KqGg3-FLvdFCpMAFfnKmJjHo4UsGQN-GMr1pl4z30tABnljgRd_QCx2zTctM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLIeKwkoZ17QiA3NTmvbyZCihgBD-cfQhj4B9NhERCVxRyn8TnhaLXvmwdCq8oPnPpPHidcb-9lgfmIrdcgjn7ZBsBwy2tz3r9DHg1etj7gkBCRBhIVcOZlTinJdZeSQP2ZMjW0FDixie4P2J9VADW8K1KZYoV2aZZnizh6ZYJptNrgncA5EP9h9C3ZzU_uRk_pLScFzahuNTPnHNkuAQ_2-aeLVg8_dEVzmMGzBc0ZY9I336cZcG5DU1MxI8hMzdiL5Lbq3T08nWWwO7bL3zI9Y0hdj__PAFYU5RwbtHGNuWwTsFWyg0EYOE3au6cF1dYzxihhNAeFpw0ow8oNKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=ml0FCRJMBy_0C2OkFH7hkwczry8ibpG5W4J5LxBOUb3lGv2Am6KaS4I3GyBv92Afq1ZsKEIJmhI95Mt394VxI7BdL-bzD2oEfLN0xUJzLQYgSSQFyGlVEyVfXi9d_Onm_lRn7bDTRJKJT735Fb2C-Vo9TxQPaVSuEFFsm_qy_B2sHA94O9ud0eoVd8zRVTqQibK_4iK7U3jUdF0hlUBWfy8DkVCVqIyMN7jficHpQxU3v2GIaw9ggLBL-D_UcFDW47CFzCD6kHHF1tfqR3gHQhuNWJgWXKCIsCp87OKH0-PEdgMrvEBEtwBw8juiTZR-jnte7Ti2mz3LMHpaFR-mIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=ml0FCRJMBy_0C2OkFH7hkwczry8ibpG5W4J5LxBOUb3lGv2Am6KaS4I3GyBv92Afq1ZsKEIJmhI95Mt394VxI7BdL-bzD2oEfLN0xUJzLQYgSSQFyGlVEyVfXi9d_Onm_lRn7bDTRJKJT735Fb2C-Vo9TxQPaVSuEFFsm_qy_B2sHA94O9ud0eoVd8zRVTqQibK_4iK7U3jUdF0hlUBWfy8DkVCVqIyMN7jficHpQxU3v2GIaw9ggLBL-D_UcFDW47CFzCD6kHHF1tfqR3gHQhuNWJgWXKCIsCp87OKH0-PEdgMrvEBEtwBw8juiTZR-jnte7Ti2mz3LMHpaFR-mIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=OUn0tE_D1BY2PPWUVXl-nO_gmtqbH5PiA240QeL3t-0kMyY3QJv_CFtpOw5p5Uvsx19aZ69s0Hszl_QF_7Zegy03rMvG4Nt-INUZ4LkBSu-wvdRNMSHG8_OVvy0sf4G-MYmMgqtH8k-vqh60QB2q13g0TXQLb-Xl4Lyt_QkkoUozXWxdTQc7-OkshGgbooMQI9LAApgmBBlI9wk2AgebChyxbJGKWWMW4BkxsdldH5qAieJqKlKRWpA6mM7rTnV13Af1XiE5wrskSTbpN7xqEdJnWa3Z_3GAKnWrlDNTIXzBx7r773jSZLrTTxkOqR4TGvkVNFedUgq0NjF9fcghBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=OUn0tE_D1BY2PPWUVXl-nO_gmtqbH5PiA240QeL3t-0kMyY3QJv_CFtpOw5p5Uvsx19aZ69s0Hszl_QF_7Zegy03rMvG4Nt-INUZ4LkBSu-wvdRNMSHG8_OVvy0sf4G-MYmMgqtH8k-vqh60QB2q13g0TXQLb-Xl4Lyt_QkkoUozXWxdTQc7-OkshGgbooMQI9LAApgmBBlI9wk2AgebChyxbJGKWWMW4BkxsdldH5qAieJqKlKRWpA6mM7rTnV13Af1XiE5wrskSTbpN7xqEdJnWa3Z_3GAKnWrlDNTIXzBx7r773jSZLrTTxkOqR4TGvkVNFedUgq0NjF9fcghBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmjj6jXAaCfEqYB6rWOwmwSTqSL8ki7d4EBhTkKKeTWz3-1Bqd6xgx6A4c7xkwD3ZGQsan6jjSE5Q8xp3Cuni-6SV6VM7B0_D9m9ZrKMYCdjRSYPvbHEC0uYUhKnyakWJFrwYFA-C3WSpfcLoI3tQYnaeZ-hzwZ1J3RjEu3xferTFlf9ojPi-XQLLTwOSEzLTKr7X-yCslPlqnFdGwEuGgLgY5q9iyIKTTlamObkwkQf4BjQMewmcpCmVXI8L7HLGHrCAsf_J_ZU95mbrR23q-erPIZPlpO_e8eODzPy9IEODmHIamyQOVOEFr9T4pnBOtSWWx74YNyIVYSM-uT10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ao_8RzxHKF5T_p9S4zx8C4Guozo8Hv3KRTHsG-2CkeU9eWJKlJr6D6d7NZkSLego2-wprqKDrAYTotQ-oQGtg0t1jtQmjE52MKDOgOWUl2dh0MmlMUtTOmJr1otqU_wMFXgEOYksV4T9dlPRmk3SquqIMQ-goUzG4whw7F15lufQtzAr9W4R9bdyVUwlXncI9C8v4jhIdOU45fhF6_g97i9V2kHPeL3LaBgUoSy5ceYgQN4Gn61-tl7xByrYD1FTU1PWE1-LhgihLq8k0kIJKoHlPYLVVvXeUffbmBxKM3R-UCx68Zq60evCo3qczWmQ5oqyMu1p7aZJB4SpUCp5zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ao_8RzxHKF5T_p9S4zx8C4Guozo8Hv3KRTHsG-2CkeU9eWJKlJr6D6d7NZkSLego2-wprqKDrAYTotQ-oQGtg0t1jtQmjE52MKDOgOWUl2dh0MmlMUtTOmJr1otqU_wMFXgEOYksV4T9dlPRmk3SquqIMQ-goUzG4whw7F15lufQtzAr9W4R9bdyVUwlXncI9C8v4jhIdOU45fhF6_g97i9V2kHPeL3LaBgUoSy5ceYgQN4Gn61-tl7xByrYD1FTU1PWE1-LhgihLq8k0kIJKoHlPYLVVvXeUffbmBxKM3R-UCx68Zq60evCo3qczWmQ5oqyMu1p7aZJB4SpUCp5zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=q6su5bD24F412emBAsvihoqOpcUfDvlx9Muagvvo_oxcm-c5GL9EedU2aQ0p4QgUmccDB5g4lLInX9womdNP8sCAf9bTIRk0ES_GEMsMS1Cxj3L5s-KmOqOYzzCaCtVwWQIMNYZWXpHGJslr91wJgdrBSeyRhjE2_7WYubNxwz34Ua5n2WUzV25vOc2BT-bac8cjzOM5mA1EFTLoPhJdbajnO4uqk9m988SKIBOqlWLWAk_D8aygbZCSQqx0LHvx90V_ZDlkxn-oS_0H79Zfjq5ItZEivUTXeewgekmvf1BMClReICadYTyXLo1nsXE__cFh_lNBL8zYmC-iP41u0k_JdOB1qw548jsgjV79Mjfqf2MrosKPeUyH3CADt0uTxev1YDuqEwVRSUB_Nqy1k2KWGu1DZAgQEnp2KFGzQPFXGHQKIV_YW6QvGo-g7SBIHXB2e_Otk-S62HS_eZUFXPgr_WUsKlTqSQPHws78LPcvvOSaf_0-ZoaDPmSi84EZ9rlWkojHpGTosCzaure2gcqBThIVUo9ebasMYY-P4NyOHX7W21cbjZxIK1hmQoak2KPj6PBV0HT41vhRDej7i3O7fbiunHis2_LP942RztRng6J48fNbEADffy8-cmWJHNRc4PhjbJCINID24mRTlUtgyGIAgLvjiB144QY0VzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=q6su5bD24F412emBAsvihoqOpcUfDvlx9Muagvvo_oxcm-c5GL9EedU2aQ0p4QgUmccDB5g4lLInX9womdNP8sCAf9bTIRk0ES_GEMsMS1Cxj3L5s-KmOqOYzzCaCtVwWQIMNYZWXpHGJslr91wJgdrBSeyRhjE2_7WYubNxwz34Ua5n2WUzV25vOc2BT-bac8cjzOM5mA1EFTLoPhJdbajnO4uqk9m988SKIBOqlWLWAk_D8aygbZCSQqx0LHvx90V_ZDlkxn-oS_0H79Zfjq5ItZEivUTXeewgekmvf1BMClReICadYTyXLo1nsXE__cFh_lNBL8zYmC-iP41u0k_JdOB1qw548jsgjV79Mjfqf2MrosKPeUyH3CADt0uTxev1YDuqEwVRSUB_Nqy1k2KWGu1DZAgQEnp2KFGzQPFXGHQKIV_YW6QvGo-g7SBIHXB2e_Otk-S62HS_eZUFXPgr_WUsKlTqSQPHws78LPcvvOSaf_0-ZoaDPmSi84EZ9rlWkojHpGTosCzaure2gcqBThIVUo9ebasMYY-P4NyOHX7W21cbjZxIK1hmQoak2KPj6PBV0HT41vhRDej7i3O7fbiunHis2_LP942RztRng6J48fNbEADffy8-cmWJHNRc4PhjbJCINID24mRTlUtgyGIAgLvjiB144QY0VzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZT5xubAHZSZT9V9r_qwAZt4e4_zK3Q1VRm4icUi5OnfOHE8CwtievF4FXteHGX3r6RVHBX1UNfBHuFQr2GrnQVrJ2bXdvYuQG7-2BNktzI_7tG5e0p2ZVR3CRPbB0hDkbM44-7-KxvmDbUYsKc4z-zpHMXg-EW3fVaiehJTbWF0dIULPtZO4e8iyxdS7VS2Zl-7fOoxc7hbnmwx9of5d_m1zpcQS9JbSoEL_foDkFJSgZYKknrJU9yBxzQrE0X9w4tEPcB8_Lb-12-78bbA8o5BTKA31zHTmVGOEWtsbRqgXrhfEDVvb1kEC7mBoGbBZw-_459PPBEu3ATZxuIeAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=SDLm3W7e0h1BbLmFI-R6Zp6hhBqdRWvjCz7JopN-PaSevw-xpG2e343r-xxoT7Dc9xb54qi1anmC7H98uGsve5MM1DzVwjSknkJJ2xQ9t4aGoGWgJZFNGwtLwgocHO7liR32k5qX9b3W-N-TiesKJ-au3XhdUunoCDhgN579kL460OChthFmo-yfLFDc4bMJ6XYvKU1Vzv30X_5DhawcbO5jASgS_U0b1eXkmLC3nWwxMtUyIPxfVAp8a0WJDxTsrAN2j-hWVCp8nXNF7EsIytU_gaREi6QujWCl_8Xp5eKD7af08Ta-hNBUvq6n4E-qI3BmC4H6EPZywNYoiZ58qzD3kQXmqDdaIWSn5UdC4GiA6tjaX5A_Y__Lxk4XXjWdygtFwbKLN06vLHq54-0WeXaoHc8h5vysy-7yLExiZjtN3-zqqrKv6hlFUfhx-ayadpoprn7aEItgyPJGBLrIM4AO15BMKWm2PRn9ByAAzmR-WmdRyEHpx3pW1nOBhdKDa4ksFsuiHEyMkQK0G9_iwi-LSXX1dqenEcZiJLlQIP5Mo_D3YS6jgf7ZlOGHuFgrgvxFvz-MFruKIb1REzLjtEJzmtMDBdWpZgFBkfZyHa_TKpNMMknT0fOddXCqs_nNwWTvWgDsskg0Ce0o03NfrOHbFMJXhv2k8eHDvHkkPJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=SDLm3W7e0h1BbLmFI-R6Zp6hhBqdRWvjCz7JopN-PaSevw-xpG2e343r-xxoT7Dc9xb54qi1anmC7H98uGsve5MM1DzVwjSknkJJ2xQ9t4aGoGWgJZFNGwtLwgocHO7liR32k5qX9b3W-N-TiesKJ-au3XhdUunoCDhgN579kL460OChthFmo-yfLFDc4bMJ6XYvKU1Vzv30X_5DhawcbO5jASgS_U0b1eXkmLC3nWwxMtUyIPxfVAp8a0WJDxTsrAN2j-hWVCp8nXNF7EsIytU_gaREi6QujWCl_8Xp5eKD7af08Ta-hNBUvq6n4E-qI3BmC4H6EPZywNYoiZ58qzD3kQXmqDdaIWSn5UdC4GiA6tjaX5A_Y__Lxk4XXjWdygtFwbKLN06vLHq54-0WeXaoHc8h5vysy-7yLExiZjtN3-zqqrKv6hlFUfhx-ayadpoprn7aEItgyPJGBLrIM4AO15BMKWm2PRn9ByAAzmR-WmdRyEHpx3pW1nOBhdKDa4ksFsuiHEyMkQK0G9_iwi-LSXX1dqenEcZiJLlQIP5Mo_D3YS6jgf7ZlOGHuFgrgvxFvz-MFruKIb1REzLjtEJzmtMDBdWpZgFBkfZyHa_TKpNMMknT0fOddXCqs_nNwWTvWgDsskg0Ce0o03NfrOHbFMJXhv2k8eHDvHkkPJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6XRH5sTKVSxYVQ-1HBb36yQH_F2vuXM_Rz9lP88ut7OO_xTwlUpto56G1BB_jFsuheumNSu4mRVKkiHLGsfRBxaj37Ug2Vjhe9M7oWHpc2vBBnu6vAXEI7iMtvD7OsadZpeKKBFI03pKpWITezUv6zqJvqhMwoDhjrko68nZJi-wGiVsBNGEW_3JG23gYJ3DQbnHOq_-VXlMednLbtuSxZRPHOR91uRTmqjnYh55BgTHVcn6yO3VS4nZL_MkPGEHGBgx7-2kl2wnSS5rC3l4Zpjevy2-HMthvnkDe3tEvXK7cqXvSLX-XCqima1HZSSPOScz9gSCv1qz8kpCYQ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm5CObldfko8YGq4ji2C_P4PyR3UgyjGkWclH48aV-X_RhjUJ2hVfLuQZwTy0C5L9hH1EcpRkriTlnzl-OdTonrfs7OkHfygqw7kvx0Y_atUzcwmEiYQ648x4fbQFwV1Jnp_8SntB-5TB7JlRxkEnysd04EU0Jouf646JMSjPxtTz43oasUTfvZbl1KpgAQwUkGLwC9ENLriqFkkIBufkJTKbFl2TeXGE85-kwiE-V9QMy6wBe8tkKc0fIjz0QBI9leb89dgLgywAVDF1uhzpOKHVzFMQLe1Ar7jEw6CGDVDJQmBtALizfHtRs78MTxOKbTgZmYSgpCj5ka6Zoo1LqDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm5CObldfko8YGq4ji2C_P4PyR3UgyjGkWclH48aV-X_RhjUJ2hVfLuQZwTy0C5L9hH1EcpRkriTlnzl-OdTonrfs7OkHfygqw7kvx0Y_atUzcwmEiYQ648x4fbQFwV1Jnp_8SntB-5TB7JlRxkEnysd04EU0Jouf646JMSjPxtTz43oasUTfvZbl1KpgAQwUkGLwC9ENLriqFkkIBufkJTKbFl2TeXGE85-kwiE-V9QMy6wBe8tkKc0fIjz0QBI9leb89dgLgywAVDF1uhzpOKHVzFMQLe1Ar7jEw6CGDVDJQmBtALizfHtRs78MTxOKbTgZmYSgpCj5ka6Zoo1LqDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=WDVyCLN3PjwrGc8FjLwlLQ0DSogvItH1jySBBrhTtVtrRhQp3xyL_OgrrHXDvRWeFIY8rD61fA2xGfd2Xl9YsG38fMNmsXla00DmnjwwJc5_A3HectuAZHGX7G2N7EUlXYrnx1oqG_5G4C67azSFsp3yh54fKXFsvhIyHwdo6mbCN3f2skLEDE7khvmEnsqGTzZb1hJs63Gqf0r65ex2mFptdzPzZkQCoo0XPeC87UxhXOywDQ27k09GZ2Am-U0VDcA__fbWSyuNyDu48r9dabiId-WT7Sm10Hk_MdRjtgEST9eDBTWqLWbu1k9Fm7PfeFMI03rh5R7W8tedAcCT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=WDVyCLN3PjwrGc8FjLwlLQ0DSogvItH1jySBBrhTtVtrRhQp3xyL_OgrrHXDvRWeFIY8rD61fA2xGfd2Xl9YsG38fMNmsXla00DmnjwwJc5_A3HectuAZHGX7G2N7EUlXYrnx1oqG_5G4C67azSFsp3yh54fKXFsvhIyHwdo6mbCN3f2skLEDE7khvmEnsqGTzZb1hJs63Gqf0r65ex2mFptdzPzZkQCoo0XPeC87UxhXOywDQ27k09GZ2Am-U0VDcA__fbWSyuNyDu48r9dabiId-WT7Sm10Hk_MdRjtgEST9eDBTWqLWbu1k9Fm7PfeFMI03rh5R7W8tedAcCT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3wiZ8VMHXcHs11gDQFdeKsdJGezn7rdHs77StIjWO9svsELqmv-4HzswUHtW2TEgHYb5SJFPWPm7ARSRZLIynBGiP1eRf8YhNPpWT73Je0CUQ_f4Q9N4CLxiLu8-Fjtvr9EYsu5KZ459bHVlFhEy8VRyayRVb92H9rmochV1fzBW_XFGLCKueOa6fJ-vFcbmxwo7DMlaaonxBu6Tegtq7ji1nY02OCi2RysD78ZMbaDG0E509MdY4feZ3vBqWaV1zBgszEud1nIVDhVJbbiXHoDVDRkNgCUoXcNqhk9SUkUeoZm8PMXBcwsaBnxQamYw8jaxpWp1JRSs1nUhU_5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=oqD-V9gVaEn-6TjhxURbyywyCP9Hz5PdLxMZ9DCVhhENSHxiIRfZlRof4Z3KMPSCYbxFfuPR0oAJPjQPQPnpgevy_d0as1ZjR5o2WdZba_1thVQRsuflOQ37k7_nNwt266__YbN8VDg3DMrczTxNZkEjQttxJogNbzRdmAeJlFYI6vVvQvFwtJIoiMFbSR7i81AOAb21jTY1Ijxg5l61tfgBnCYUSWqrmCaxWjvuPadxJXCd6fQGu3Azs0m3RQXedm_4VmwPmkDCjSgG7gUijS8oCesf-W57JZWWFW0d6tl7fRGNj2eUoBZGyckL3C8IleoSu_L_8jNCsn_seaaong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=oqD-V9gVaEn-6TjhxURbyywyCP9Hz5PdLxMZ9DCVhhENSHxiIRfZlRof4Z3KMPSCYbxFfuPR0oAJPjQPQPnpgevy_d0as1ZjR5o2WdZba_1thVQRsuflOQ37k7_nNwt266__YbN8VDg3DMrczTxNZkEjQttxJogNbzRdmAeJlFYI6vVvQvFwtJIoiMFbSR7i81AOAb21jTY1Ijxg5l61tfgBnCYUSWqrmCaxWjvuPadxJXCd6fQGu3Azs0m3RQXedm_4VmwPmkDCjSgG7gUijS8oCesf-W57JZWWFW0d6tl7fRGNj2eUoBZGyckL3C8IleoSu_L_8jNCsn_seaaong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8tI5OJJeETSWwYnoqqtcrgY2KYnJPZX9DjE4JiwkZYaXXP0Oof9kNIdSTwEMt-PhldW3A8uL2p8i-g-5eTMosvLRo_EPxvVDnxLdMVs3jgEeuOrRyzgyKLlvI5WGs9ECw9tMHva5-p0vzA4W9_mCpkuwnE_VJLzTsT7zUDkwxrYZVi7PDybj7QjjhDb71ULTC52c6EqROta_IT5pXXedBbfObnY_8adptHtLIIK025k3g8HeOYWom2uWCezSXx-kH8gA_3BJiIXbIc-dHm86k7Pe1Ws4CwCun3mBISNKT0-duafQ7eAATZnSruR8jDBE7qkXwQugXNdHmY9Z1xigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJctgnTgBfCKpRMW2H3Q13_bWd6ynL3HpFhajn8wkN82-KagsvHZenWonoecXkcfpRjBJk1KSWWbSL5I5QnAazQA8AHk_-cJXhltzAe9Gtfsl2WkZDibtac-_Axoc9h49VFhSUkswSSND91kZaaKylP5OYouMkCFaPT70HafkXwDFa0ChZ5OXaUG_wkrjWz9_AKi1mf9UGE4VSCnOJVJkuxHMXKLZTS_EJXUNuFQVzcPfdtb3SUF0Hj5ZwkUYzmo-xET6cmDRDsi8GT0GT-obVjSaUvQAA9i-GgN4fielSskNXhuAB5AAXJeKNUKDdyOowQSIi5hvPNAxbv5zTIHqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwqXSdgXQEcEaGi6XCV5WS0DZIX_dMLE5OAM_6f9lbVvcOSLC7FiwlEZ5xepSQ597k2efn1e6uqQXZjY4USfTtpXvSK6J6iLMaHYs9Bj6IYAODJZ1aqrtMh7l_S3Zu0nFlb-pUnvZz48XernH7I8XKrmWHcaftWvUdKey1BKm3haOEoQDhxg_r0e3i1U0QdoXVcqQZ5nMZZM8R_lTldyHMdSF9sxFRjHOw9zzj0xEkhCN1JvH18-E25yz7OlyNPxYuiyxm85FmmJp7uRVwfgNtq_OSF7V7c3j_guUxgPogY_MTrwcNFXl3ItaGfMD5OkIuH4_K43Oo9-6B2HDGkSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5UFlsePIISRCh7eDiCOOi1KfD831jEC0KLeil0LMCsZFAOa5mGRRh_7LxDt38bOzvWRLT7wQ1DVRTLFYqNvbJZItRDTgNOw7Gta8VrOX8edJm91Ak_RA7Yy-fXm2RZ7Wb8k8NTHrM0u1sv-gTxBgFbWd5lPIu2gBs3WihllBRLiuwag0JAHj-gC16YrWt019dctsp8GADegrkpH3SRcQgVeQVDX5ARkyIGMx0MEA5x_ZxElcXfp1lbdO1RtCGPwds0LlWmaQxi62K2ELBsGoobMhZJ7kJgi7FvqOgYc8NBEDKzWE7oQ4e4R6BC0bKqU4JiNYN9EGJytv1GaUIaffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
