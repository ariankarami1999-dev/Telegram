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
<img src="https://cdn5.telesco.pe/file/YY4PXxtnkFfUcBm438lPy88QxJ3ZB-XJtLVlCG_lRKQSEBd2FqDRQcc-sUXUprEtIgE3MPjP0iwB9cN8eDkvkwCzqFeArgeuUOnYLwvzOi6YEDTSjuj4SPH50psm_53PwGglGnnpbSH8ohTwHkmMrMP02yMWvr_BLHtnjeoaqL9fptQo6W4XhdQBz_xVMYlEPODUDd4qYDYOyEZUm2_CSVAd8NkmRKga-_tnE7fcZ8BSOoDbd6nekoCjqABj7ziGRuUxQvizQvjK0BXixec0B73jzrED1j8WbdybKgOYetKlH04szBqXt_Z-x9EEeNQpBaHjKN5TKwAMw0tjzp2xZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 515K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=VXCX2hjLHqOO8HYnBAkn6AZtNlZdWPTPJrasqAa6LktS9KtH345IeSD6OSgQg10IRRcKI7TDeg-jSX7wgKyMO4QCxLRHfyZpr3CZy2NDxG-ztfaii6KY6MTLk7atNpH03Iv2aDhVScsQZ70rbNfs5_Urd0hKC0JsfOp_aNB5oQ_YorfMRYxmJLGDV6tdCJM6H5S9QzuPBECbhU6LS6pYCLgsxHHdUleS_zJlR81SfD27uIIl4yvgw4TL1oBkEC2khEeQUHfVG25L4kvwfqpZSGwBvnTmSLNNDjJCAPRQG-1v-DYqSuQaSDu6KxIJBU02J2uoegEYF4QB37L8Ttc-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGgEm16p8HTipBefpW6HiJH38wJnHVezuS2KLmo9B3tCzCgs0SaLThFoq8puCYgQrqn-kF-ttwucGD_GDJAhJYFifo-nxF1FtfPT_adVyNaQYVw8dwM7vcLa5uKMOcLjR_1YWRfVJWSul4gbtciwVZ7lqyvUHVIOaRsTYIIzSloXFhz5hnk25HXxBiyrJSsZLFheG5MRrhsaCkpvYCyt-iRWu9KVUj1yXdD7XO7iyXB3bCc1AX-h2gB7meHALgPhtBIiKTMpYqX5ZWUO1BIiLtJjbREz8OYkZah6037iBT_pN3WrPqXLOOeubgQvUJukRHBu1_hXWjOa743PEyS4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=aGoA2xS5RM3qAE1RgG0owqcp3KhmhWdAECJrYCOnLK_1SC67cuenNLFsT1Wgt0gm71fRUrDi9enj6NIhVqQWMiiZ1rwzB9D2hpb4eY7rtfdwAcIc-8-nWxxdsQ5sWuDJ_kDaHXESRlBNFXkaH8TAF-RMR2Cr4iZWFZRAX81638uHE_iv2YUSES6c9HcotTXXy4gFTA-4sos3bRLapalKgQdXk_wr1gVi8FvLfNO7BcAaTKt6D3nmyaK5inJXNWmNaWcKSrpyHo3VIZ8DZXDLQu02cg4bMhFnCWAfLFjAcWgqI1wDZSE239nW59d83dE85GMn9856sJHS-3SYQuqPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ZQQbj5arf2mgDpLVYGuCYEl6NUxDQzEPss92UUe-Ku6CFs-WI6V7R1-cY4nt3MTKSlos3z7IoBL43g8IhcLX8EXvUp8Gl0WbXbRL5BD8T_bi6VKkGydyn8Z8QGtAzSxuB-9LYG11I_JPBSgCRGNEJui7SVUtM-ZQKpjdWvaCubKcxpH-NekI5hMUEoxrNwVg0YQwL7m2r4uMNpqcYRPvDvMEH0dRMIodH9UXnp1wHSRBlgjkdjG3D95TfTthwuIhmOa87e4-M0OHoB0oozMtgVyc00nNGugT-Oo6_GLoQG7H_wuFXjMKSDLd1ojgvp8Te8ajmuI9R6r1-yRaaI39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=iRGfv_VjCL19MVjVKw9TdFZId1_7NjK_CvBRawgm-uxL5GnP37pltNmaXR5GJK0ZFXhJBInkDYdcf7tWWBBHXYbByx3KMAHPHg5H8ficZ9O065iIIZD2PQqA8OVAFEll4XmR09a1s_Rtm9VdNct1OZbl0Vf1zoSnsS5iTcvxmSXhev8K7p--Ls29nQbLjiZ-nsnMoYjyG9mPq-2z4q2__vZjeD7L7eTAMaCfvfrnHMI7oXcjkQNTjAWtsUhadJ0al1M_MY57IvJm9gWpXThMFYktIdjDxUd2GovHf0dFgfpCXh4YEQjDaomiy2gzg8m4gUeaIJVZyXu3SAq4e0jrdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=Q0rNQeB0vpheGkrHJCbJe0I553gOe080Hz1bDQd5cJwP45iexHDJEi1t1YRHIpgc8SOogW-3Aviowgdn6RxEq1RGoRW3j5_m9E8caGdVqwTr-BuxCAtthysoNAGfhcxukR_DiM4r6bixPFi-nzzWV6nWPsZ7OurGakCDjvygz0JltJ3XdIPZfwd6SGNfuzcsh3DfqU8le3MHfNar2Wxk-ufBeI9F0AXmwj_PiExwCWihWYYGNbTgoFjBS65gntRfeRH2TqEJnj6_ajg5yzutLs2D6zcb7ba-POCXIFZdxOGQPWKojT7KO6CJttpT8SCjoMe0lRF53c6H9mXAcxOUkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=LTQ2a4LMVDFqXkSVUdDqUxSI4M-6VWqVcrl9to2aKM3kFW8SgCi87364exmK8QR9V8z6PDZAA2L5HinR7W_mR_Yt9FIZzpluOcb6xmspf6hJvmvaEc8JkbOthvnBHjDYVravojPzNOyA5J0iiWsH9lB0TuvgXSq_xUX0BdKG4hOA_7wBPRPHwCG6jZsAMypl61jH8zev7eDT46oQdTAUWQFZae_D3THFhDl5KhZHJjZDPeeMYvyBLS7quRJpx-YzcRrPntTjlI1388J_8dugJBs_4k9Bp0X7PtuiSztZT3YwaZUs2D85QDUxYerb1rffT8WoQ2FwXeju_-XapMM1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-ROEaU9hJfHo6Mi39lkj0RsxtmxlsyX9TZhFXpqBsvIQj7jWiOilzJCL6rzkBmosTwwTsp9dxy9dV-IMpoOXYwjhZfIjtduLvEgVhHJrEnHR1AM4kYQOUyDcVkMucaKY-M0KgSfXeYwo7hFQVbfdceirUFyvRdfR3r4EvVrviTMfxAg4mqGRt60tWZErI1zoqnRxSAzbqQrzUmp2_aLXZfOmGIrqzm8lxJCUxC8Ah1FkpQbW2tgQ5jsjgGFukqIgfvvPW-6dR_Icvf5HQOpZOZcsYr0DUE7psCZ9o9RHg9q1zGX4n_LVvuKQKPRnCU1kKCjF_mHWImFpylFV1D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KxuOi-iRHNK2hYvec_yOxonjXvsFg9cQWCmGyMWgz7ZwNqZ_LvTndQfisDsCR_SZy4itFIL54z1hUxicRgUvEQqpdcHOBYjfcf6qun7O7MW8ArlN7A4EiVbqWvCQRhpV_O_2xa8QfzCay5qdY7XIaHzFI0tJ-GDV72jZKp9i0tNPQcDFEpj93KxfeGYwBfm3cfN1oz4UCgoKJYNzRjec4DcH7a4b78uV9FAOWylwG8uF-ilV6AZNTB4ULMj7Fsw-5HFCkEJwAr5jhz-I_INy_r3xf4y9dFpkd-2Y0kCjnPSkY1Rsgj5zjnpYFOP3VA_PyPKtYZIlzOvdah8QGlQCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWTP5x2PZ5MPm1QZ7W2xZoyrqAAaaczL1pqrkkxii4zqcDut56F2Qj1jZ4LsumQcaVLjXAEw92NwcukbrxkBE6PblLOnTfkn3xl8dYFIPu3yILyg3UCItBOPYTH068gQ7jJZd5CxKBv99CVNsvBGe9zuahRoB6vERHVra-ShwVaL4rA0f02TNQ24CBJOvM9JltBFgTDShOblCEdsnHNX8kr_6ODHizU6sU_zrD7Ez-1t01qpjlrGIi73Yr3tmLfbRJ6YnYbpMWq4fM3dMcJbEcYqVwYv80toc2WIOd5fE_9kdtWVU5oos7unMtcR-orQKCvDxBJBQTjkWF3-K6-nHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxZ50GBxrOAub7attGb8wiUBPIyDX91D1cZaqW_JolU1kzQmvN1mtIyDNExCkK2IA38Fb7uBJvxfObmtONIYMLKyW42S91m4lM28WYTOK3obeaCz1p9oZBfuCfF6ekdWElC9pIUomZcnxcRyRxmv62ViPYBaT7bFA83rxuQ2CzvNYiOOGJveY1Ad9SwFOyr4cWkp1XPYz9jZ-9lyeZgTtN2v15O5pXSR8LMM_zzPHdrdWZ1E8KKwo07THTfRGnTGwlMtYXxIVwwqae0-iNufTYJCShRYHdJFoKGd0iWdNur4HJ1ZPLbqbDM2UM_5DxWaSRs27_QfMsKNrDlIujXx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjW4lfxM42BZoaVZ_fhqfxEn1vI9wfgtoRxX_Z82xKiCQhXa8v6IK4ObG_FdWmeJroymw_WbMZ_o1lfWNyfNMV4QGDoZde2zwNPgJtJZEo_4rp6AkjeNb81jpTYityMiBT4YML3uhrcnBF3hYwLHYzgZjKKEIcAhjrviS678JmqvrvmY1LXloenVtTDJzT5SYIwGJhKJYxkBuU7lg4VKP3MRvVO_Mjma0n0iZGeYkAG74poCUoVZYWOM6hHvwL6jetBMsBi5KfxPIT7uqgJZprYIJn18te1M_c1w-4e3x6JDKuo5w-FK7da9PJ8asUwUS4b0T2Rb-lor0rJ0FoA_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjImJ9oNJ2K0_YnAnOBEP5Fgz2IL8RVE8OiQ2Ixox0VFxwy64i6XF7Ih1SxF1g4jVbcbnK-x1O1HdRazEE4dUvvwWRT-zEpjwgOVO9sj0DwnyQqEUh5VEcx3kJBYI9lx2rUJqFUGwhGJzJRdqGP60z8RpCgvbwMg55gmNB2RbkM2q5iSTH7hHXFm1zQL0qHaUAMnlzS5NjD2x10oT-hLCwF-JjP6VkUMbAcVkNIJMRFGoSFPeUiVEeVGYTWY_cLzKYAirke436rUuIA1MzTXwMaEz_nkOjXibpgi-YdraFgjvRrWZPs65P5lyoN9TvJvORluV839rPMLVVG_nGpvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=bBJrik2f2REihgWNZ-eYxaIk2VpmkUrnWjrLKxW8pQRaxNmtbj8C97k8-6HeLY0v6VNnfC-YK87v8SO8qd3dGN8yuiSQTQEI8uuG-6HVxrkDUq5xhay4Iy_oVnSQXkjfCVoUPL0pJjNaEDzR8Si4smM8hJa5hbi1KceB3MsE3v6P7SYkCqtYWhygIWfCITYuklsssQ16Elc5yW1rQXjePiqWtHN6JeKxYe1PQmCXXERmIAawRjBrzn7qmRUfgLMBNYONPDiTe9rQfrXgP0KjaHWzi3LPKIF75Ap4dj0bQ4U_mhezD7_gBbFBaRQ6iwlLeLEXRzd1SmuqzZYuSxLUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=bBJrik2f2REihgWNZ-eYxaIk2VpmkUrnWjrLKxW8pQRaxNmtbj8C97k8-6HeLY0v6VNnfC-YK87v8SO8qd3dGN8yuiSQTQEI8uuG-6HVxrkDUq5xhay4Iy_oVnSQXkjfCVoUPL0pJjNaEDzR8Si4smM8hJa5hbi1KceB3MsE3v6P7SYkCqtYWhygIWfCITYuklsssQ16Elc5yW1rQXjePiqWtHN6JeKxYe1PQmCXXERmIAawRjBrzn7qmRUfgLMBNYONPDiTe9rQfrXgP0KjaHWzi3LPKIF75Ap4dj0bQ4U_mhezD7_gBbFBaRQ6iwlLeLEXRzd1SmuqzZYuSxLUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=mG7bekTQdV1J8VVQJxfNDn9BvztFR-nUK51sME0TAYyOW2E5vnewdFMHJbXA_va173HgATcWJB4OQymV6tl4as0k5QFu1zTWKTbFDzAcShSWFPaXSMJcgJRPokl6VHm8g8zOK9LpKx6m635TdyHq7mUFOYjC9DmtaT6WoA_eTXVxp7JojW5rIii2oSCWybfjDCzEJTv8SssFaTlFYIptgGb_C9gCs-VqAp9qLzO3_aYVYXJoDf4xuKPYCqnxPGiULho7vcJb3hvJq5cub9fZ3FL56iuzPSPAGDDwqhdnDDch9UnL9G-el2m_tosch6v6e7l9Rz6s0tNH3j-jlo84eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=mG7bekTQdV1J8VVQJxfNDn9BvztFR-nUK51sME0TAYyOW2E5vnewdFMHJbXA_va173HgATcWJB4OQymV6tl4as0k5QFu1zTWKTbFDzAcShSWFPaXSMJcgJRPokl6VHm8g8zOK9LpKx6m635TdyHq7mUFOYjC9DmtaT6WoA_eTXVxp7JojW5rIii2oSCWybfjDCzEJTv8SssFaTlFYIptgGb_C9gCs-VqAp9qLzO3_aYVYXJoDf4xuKPYCqnxPGiULho7vcJb3hvJq5cub9fZ3FL56iuzPSPAGDDwqhdnDDch9UnL9G-el2m_tosch6v6e7l9Rz6s0tNH3j-jlo84eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=ehx72lYF1CagT_j_wpwEWhl0o3AWrZLqHGQnhMVk0sYOS0O4HYxMAl7n0QDhLkQBKP3Sy3QYQqUPhK0Z6Oql62O4nwYj2b3rC2y8KqUewyt5pme2YHxSBpL0ylUiGzez8XzbKsJqmu3A4Ag_7ns59UWEQfhsx56pPFN9IfrWksEZJdXZFmxKvdbZPSo1mrY31jSNd-ZdrseABIHvQvTbaW-73U367G_I58T3PSR3ro-66DNdnk37faGfXTJk9eHYu5B00wHnGl6Q-9JOmjjNhLduJMOsIh2CFo-uebYJFFEnWgWgNUpwzZVFq3--tH5jgnaOFl4XkMG3Ysz-W1_cgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=ehx72lYF1CagT_j_wpwEWhl0o3AWrZLqHGQnhMVk0sYOS0O4HYxMAl7n0QDhLkQBKP3Sy3QYQqUPhK0Z6Oql62O4nwYj2b3rC2y8KqUewyt5pme2YHxSBpL0ylUiGzez8XzbKsJqmu3A4Ag_7ns59UWEQfhsx56pPFN9IfrWksEZJdXZFmxKvdbZPSo1mrY31jSNd-ZdrseABIHvQvTbaW-73U367G_I58T3PSR3ro-66DNdnk37faGfXTJk9eHYu5B00wHnGl6Q-9JOmjjNhLduJMOsIh2CFo-uebYJFFEnWgWgNUpwzZVFq3--tH5jgnaOFl4XkMG3Ysz-W1_cgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B35z1mEqM5rIRtsJ9dPhEu_0ARAEAdZHYHJDgnTvFLZRvCvXVs90tNvqPGYr6GqVv-OWeFXOnIdGJrJNqHeNkzb25YVE4NOtBvVNpe1jBsVEQQAp5u6ZR27WcN94--wZO5I9cAqpiEvHyncrvUbn3gdeY3rUPGMcEskX0Lebi5AZQuDpDdlefB0-WtXh_Mu_d3IoI52HirTmo2g26fo3zd9lQ_try9B3ZXYevCevvAjbiBfqRqX5DgDkQt_bSOwj4mhpEA1sxGHRHUYkwU-AJC5wIWFUph_vXGQ9LZmPXpSsCs-4X2WCCCHg2P7eVOWF66U3DHjx3i9HWT3CBeW5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3hcuTbRMmsF6Q3gm2I2pg_ut_Raxm2L9yfmNWHVhTeWY4nixLmHjtVTep-rD0jfufyOtMfUMq0Pq2v_f-dPmhloNI_Zqyxz3j9NxWkBy3c5d-p_tZ1Z3cgizhp5qqlRdhodyOcxLejj8GMMpGy0X1NXN3aQsQXBS3fsAMtgkAy6uSnw-p1erXnFZPbzA0__XXRQbC1oKsXf_6ilSnLJTEnAHTCCgpYsK8fznCJmwg6oAUj4ODgBosH02aKBG8RKjgEHagFVbeQ-_NBSoG6YNwl0D-oFbwdKbCDlEuhtpj4-L8cMro72LjWinA5xGXx5XBbdpXMdEuknSDdrWcse8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rris8FS2PfTbKn94LxJOsTE4LL95mTaMfSkZn0fhvNe7wnArSJV5vC3PNaR4-NS-bCQim4fyFBCgWjEallKUjfEm5mIUoeRnbhNEB9re_aHXfyS-pgTxuMexHMX-dAGLOWb3-ck0DYEXdDWjNkBxHBVy9VvKZqZHoUFeVeqHE0fNo3GOw-QkmLapo-zZv6MBrBxXvuYJcy6SyWAqT8yU9KtUV2fqUBVNTccwRDY3uIxTbySpD5I1nosZmy79D1Nb4mClKn1Uvj3sVpXBjrp6WWLa8pZlqhdMRjbz2VXmty0f1f5S7ArZr8t7DJHNdR8Y-WoXwXgTU2vQurRD7sV4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6yojmItXhwqmN0m33gpVsbPPGc6P0oHOidUUikubgYUV03fqXzxIbfCogxJhUaxzWMG-1KDNvDLKSnTzVAbFVoxykKhaCrRFEHTm8o91-9AXhyxKqCChKSEuULFK4OWP7ma8cWatpZWcwisxjESzKVGcryXwtlB3Hp-0QULYkVQdm-QbCq5KZ81s15HgsH1Dg5Wl_TbHD-9xt9EUh55y5yNgql7iKe6vQyRG2h9MDlxe6DJHVajbgqmi9h6LHlrZNqxM8DMjGCoOZ9OvrxW5W33sCMEwsXzksQbtKTehz-K4k2SnCVdpvRxsqXGHWnXlOBqIZK0EZLpxaBHmwlP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if7OArxvbxdfyf09eq-zoCgCpPfQTtIlRlqHtesszyQxSKEDJZMxv6_muof-40UQmhAUUlC3rFu3y13hQPN8xqFSgh24h03jGpsMPRtd-auhtbKybQ_96n5hhzbmLPYJ214VB0l8e292xf5kY3x52qd6Y0UFQ9Yx8lRgmE1oOzwMS5HtpytpT6ph3qR-_d62vVM3rN6caevaEBAph4ALf6_kRgppCLv9_zfPsJOfSfcJPRaDWekxiFJs72EHjANj2_aOaWP4PPljBkIg7Et3bg7QHEvs05WKI5bzeB84w8bhJUrsDjX3V4Kqm8GhCY1YyF5aeDYhIre3UYsG_ozaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s24POu1p364Fld25Gkpv31nag6jbOf5mA3wAktmghrf-XZcbF0vtkFUP2WUMcZkKhgEN3oUVEbbkboWw1ivOwrgrGB3R0EAHTSRaFJ-EayIalkq5khW83XmWnRX9lb0pnLZ1rDwwy6SYQ5rR8pDpUieNi5EA9Tb--eaE0fvS2gr4UuBCNBLngPu0kRjiBHmnyRWmA1KFDGsTpF0oY8DGTB-pZF8ZIdpuaGeZmoysApjES-bLPtScsrC6WeArJNc9K5iggC_x1BUYilglDqkGLbHfT0cixxb27jR3K29Pa2u-j98uz0kavQBp00X26-aFMwHB8bTGZO_-E1vYcWriNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbgR0yK_UQq1pkMwkp2xltZUhOZ-3tY13-4gQbRWpfOxCDfnPVqFRXjr7Nb2hyqwCHJURT1QQDj0S5BRTa6Ue77lYKy6y-VNcWOtESgqmlI9gA6vjfLszc7oRn9mBGALKpQuPrnT1F_r18-aA93TJ1QtvK1d9FtopFcL5yCZAIZAIbVr8kwe9lhw6lRNqR2SF-n-gx33HwZ4OLBA0Vk2DofJVSnl0mOOKXiaENk0uSXobAc331mBzmz8K-8fiIMZ61_g7wMsgxV2hhPvxgp8epq51kkEl3cW42xLhriIjKKkGKZqGyiJ04yeXbaGmYbUFSy-NbbwQvoPtjX2MnjNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEdl9lTkuG0F0OMpka0GxT0O8KRRz_XvPoPb6pX84wy1ZzuQ3JaelnGC3MjDnZlcRV5mcATLAhhfGmBVVNsZzosv9XjTb1WRoglpTuJhRgp_-lhxR_QEe7Dqo3Ldlyiye3DLJ4IVRYJqp28529s9btZtFXQmIeXE6YbQ5ydUVsMa-6wBQf_rdpuZuhkSZWntwOmXrd-vQd99vifIa2mmC7R9k83CH70llXCJWON16EWelQushbEbxClQybyTBHNLZTikN7AsuzAGlS_xRzdfa2TWMkxTQ5FZQ8G_0Jwr67VMmDZ-EUGdBvKx7kZSgdUxpkcMLAR-IfcL2--HNJY2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrQmflOXsXYL7rORrqGkv435A4QCEhey6U2q08qIzrcAcis7tRHIBdEyiHXOy8F8ONVFhDVmoxKxtIXNdDhkHXwQt5Smj1PLuXLm6ko-4K4eUsbNBF_4xFtd6jfrKcXbVfQ-2O14VBd0oFEdGZf4EkjkDwn_nPx-y8tGqyVRVCXL44Fj7giQ6bMuk9n7qLKko2o8f7T8l8i6FPCNX9zAoHc2V16qN-uHH9s8dzGO5XaiJdRtSaCvI52umSg0kXAuC3i7dqoS2l3E2egtznQNmy0dZJBEWR5f-qgDmDDjlN6GYQsArocFK1fgeNH_NeEVtpLj7kHKIPbP4NCKWqCgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=qUvjwjW6rhviE7NQ_jGpYCFHD2CeFbVa-avLc2hgN9La-A5ZNV7y2WiMxppZ1LGcVDgLcPKzk2XgEOIbSjdIu9igvuWjk9cBn3Pbgy58Y1laTuOV7fFQtDXFB5V7vW2Wl-7gIOgbUkOu0NUW5T9KAs8V97niabiN33WkeRghqQzRZ3gBRgmN9ZpvtFAvtrSrP2UcDQi9Gll3KE-F2lB4pVX0snPbfpI5_9kFPeBCFsoFlSE1Uzu4-L8mDV7xlXZkSYKnkEiFUR9yJhKdAvam5R_C_aMUhZ-1NJc7pfEM0xsoYhW2XjHvV0HKlAWXmlIyqlHT-UpAQ5YbWuXQjp3oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=qUvjwjW6rhviE7NQ_jGpYCFHD2CeFbVa-avLc2hgN9La-A5ZNV7y2WiMxppZ1LGcVDgLcPKzk2XgEOIbSjdIu9igvuWjk9cBn3Pbgy58Y1laTuOV7fFQtDXFB5V7vW2Wl-7gIOgbUkOu0NUW5T9KAs8V97niabiN33WkeRghqQzRZ3gBRgmN9ZpvtFAvtrSrP2UcDQi9Gll3KE-F2lB4pVX0snPbfpI5_9kFPeBCFsoFlSE1Uzu4-L8mDV7xlXZkSYKnkEiFUR9yJhKdAvam5R_C_aMUhZ-1NJc7pfEM0xsoYhW2XjHvV0HKlAWXmlIyqlHT-UpAQ5YbWuXQjp3oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=a3iS1LQ-ASaZEiytHQB4G6o_LKjoMK7yqkPNIccJFSAGKf36rbWsf_zJVitEusNLpxXuXn1xwVMqgUTCd6Djuki4FwBXT8C44u_djAgf4p7g3TmIN748CzWeeA391RRQF4R4ywmbJ37zCE75zc82nJ86evm6m3cSpUWvyTZoSBYyIucoBjIjfr2iUTOCPVOiDU8NzmEneKi9o8A59uR2YKaBHZgxVAsA99Xb47lLE5jY3eSZAloZf2PV9Se_N4oSTiqXQxDN3H_pRr32O_bJhrC2msBZ_9exbPJzsavaylZUL47tfCmjBrNsyg17hMMedoPg8R5vcj6ufiycIBSyag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=a3iS1LQ-ASaZEiytHQB4G6o_LKjoMK7yqkPNIccJFSAGKf36rbWsf_zJVitEusNLpxXuXn1xwVMqgUTCd6Djuki4FwBXT8C44u_djAgf4p7g3TmIN748CzWeeA391RRQF4R4ywmbJ37zCE75zc82nJ86evm6m3cSpUWvyTZoSBYyIucoBjIjfr2iUTOCPVOiDU8NzmEneKi9o8A59uR2YKaBHZgxVAsA99Xb47lLE5jY3eSZAloZf2PV9Se_N4oSTiqXQxDN3H_pRr32O_bJhrC2msBZ_9exbPJzsavaylZUL47tfCmjBrNsyg17hMMedoPg8R5vcj6ufiycIBSyag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaW3RtUSN1vVrn-OXQkSxHYCRyGhw06O1cmjhc_4xID77rijl6j-SDOa5kW1Iqx7hBRrO3FxSUQO0jBwUkR1Mu-tV0xfgxpIGFDVTKfGQI4Q11GCKcxii_SAeYnFSZlY8dRmStTLXOrg7ge-5SzcPbSEfC8z9J7DrfU5JRu9Lb2-2Hj6CxCU3jmhGaZ9wnMfsvFG-BLF4PoAhAESxBJlc3bDZnQtZEKaYj_mnKmSwQ0mUQB3ALrb0IiF_inT0peFtsSvyFlU13Bc79GCoTT7isYcWG4jy2sm9zHf7WBjsBq4JqDGFgJpIFC1DCfsJPbJzzJ_gJyPXAdBnTh7oCJrMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=KAjZwB6Vp1mOhWHR-AxwLey0LSgM2AM5kW-SyqWGA8AI81o_9HIJ6soEwM8JFLFqgZCdl614VbM2Zy_ubo9BbklWAny0k1Dvw85YGzUtS_S9qCrkO1fSVvDjlr2VBDZy5_SrrfgURARLREboKdxNEhjCJ5Rs4Jr20CBVLLWy3BHmtCwvSSVEHqfIvLpIUHwcFGnD8EBViWq5a7P5X2Jhs84uHv-5hrfchWL6P1nqBmH5-kTHsYwaBEroIJxeycZJ15jLukXHVno9yVo0mQc47Ooh3IaoogXLy9rAU1A7k0iS1nrjJJ78bwH_5cNmYCw9KsJ1MTXgf-EnAY_rjFSx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=KAjZwB6Vp1mOhWHR-AxwLey0LSgM2AM5kW-SyqWGA8AI81o_9HIJ6soEwM8JFLFqgZCdl614VbM2Zy_ubo9BbklWAny0k1Dvw85YGzUtS_S9qCrkO1fSVvDjlr2VBDZy5_SrrfgURARLREboKdxNEhjCJ5Rs4Jr20CBVLLWy3BHmtCwvSSVEHqfIvLpIUHwcFGnD8EBViWq5a7P5X2Jhs84uHv-5hrfchWL6P1nqBmH5-kTHsYwaBEroIJxeycZJ15jLukXHVno9yVo0mQc47Ooh3IaoogXLy9rAU1A7k0iS1nrjJJ78bwH_5cNmYCw9KsJ1MTXgf-EnAY_rjFSx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA8qm_YBVhiJDYwwt6RnLaAFkZSkjyPlQq3A_OAxRCCEJAskILLRwxVrH_wPkVg1d6JMzdw7mY4-5iO3qZmIqpfgOcMco9LaZ7ZY6DURB-gE4nEXu-muNeOTO695uWoVsw04KGy4kb7f0CuPlLkbqQTlLIyeN80V-_Gq1uooNpamMcBDhU69nNEVoRa6zIDWyRByJb4NEywwIbsECu8K0NYCjQrwpB9ccszyTfahnY-X9xb_yFKd3SpP0yY0uYP758c75QWD_gx8f8UjMaJsnuJ5bvPqxO5lk7jTig5DhFmfk7EN9RaaM--Sdsqe5yUQWkGqlaHabSJPIoRmNa0n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=be4_0hKImKx8PahTfY47oeeBSoZ8C5CjIiL7AWEr7c5yKChpzgMXXQp8GNNMYmLPsU__AKw3rhSd8R4c2PChOGN75hReqGQM0WIbIowOdBsx0_jdGGRrmb5dFNBYWeIPec0hFzSfLOqLBPPEuW_1ePnTlEEaQeuoBpgFZBswXABV1R3DDoreCDVqRgLIDCWo351on0Mc3bGPh-Sqri-xUhkyHuQFolHwdmDx1tIK4L1RVrpCQNfBAzMxcGuDtrnP9z4D3M5vdSPfY2wvFy_D4EwfQrpsrXhn8INk_YUM1KHSixv40GeGBBklprGsT-bGov048V13tk3iaip74YX_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=be4_0hKImKx8PahTfY47oeeBSoZ8C5CjIiL7AWEr7c5yKChpzgMXXQp8GNNMYmLPsU__AKw3rhSd8R4c2PChOGN75hReqGQM0WIbIowOdBsx0_jdGGRrmb5dFNBYWeIPec0hFzSfLOqLBPPEuW_1ePnTlEEaQeuoBpgFZBswXABV1R3DDoreCDVqRgLIDCWo351on0Mc3bGPh-Sqri-xUhkyHuQFolHwdmDx1tIK4L1RVrpCQNfBAzMxcGuDtrnP9z4D3M5vdSPfY2wvFy_D4EwfQrpsrXhn8INk_YUM1KHSixv40GeGBBklprGsT-bGov048V13tk3iaip74YX_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=b9flY244_rHRnlspL_H-uuRCblrYLKT4Qjt3MRA8D-xQjXN0HXE1Y6YD5xO9e5tRvdtRiK7ZhFnXJe49GwdJK9ZsI_HyIU-wWsJJClUQHSFjHOgXUZ6YaGV8g689wjFosr8LOkLMaKjnW6KVmeD6Nw6-lI2PNeqnwOFnsDdGFb-XxseSCsaXnR-QMusKuZLxaoQFuK1W5ii1Ait-VJ56IgXn7YVnaxtSAITM738YLdHMuNOfOQR-X1EsiJ4jTOO58kG4XjRUq54lYxSqCyKjKQPCsWR2XMsx6XDir_04JleDkjCx-OW0veNTRTQ7l4uC-pXJBdDyTe_fwLwRz2NFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=b9flY244_rHRnlspL_H-uuRCblrYLKT4Qjt3MRA8D-xQjXN0HXE1Y6YD5xO9e5tRvdtRiK7ZhFnXJe49GwdJK9ZsI_HyIU-wWsJJClUQHSFjHOgXUZ6YaGV8g689wjFosr8LOkLMaKjnW6KVmeD6Nw6-lI2PNeqnwOFnsDdGFb-XxseSCsaXnR-QMusKuZLxaoQFuK1W5ii1Ait-VJ56IgXn7YVnaxtSAITM738YLdHMuNOfOQR-X1EsiJ4jTOO58kG4XjRUq54lYxSqCyKjKQPCsWR2XMsx6XDir_04JleDkjCx-OW0veNTRTQ7l4uC-pXJBdDyTe_fwLwRz2NFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ6cRKmXTlO-40eaYo3LnUu4SqHnuSG_4htMjmMM0jl5YOhEVDJ3Aq8C3PsKYELmMyCguPslhWudml4kUQU0Qfg13XnQJdU2u3xY-1paIvFQx9rEQBYr8l74LB32kfLxp8VY6ULYL0LPdy2HMkzAp-XYSV6PTAsIPJcf1cmtsvKl4swqEHHoliWaxq1djX0RIbNBUXNC3UhGK7GYXsd5JcSgcs8tOqJ9AGokdyKKhFGOEnQG-EL73Wt93UDP2JxsAmBtg4zT5G4wCspXSrZpZlbiSmJtUxZtGdcMTmFm_HF7EgDZSB3z7vDuUbXqzIg6UteHMAg3KIlcrfuw6N0fJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-Gaghc-axHIFpW-T5kw5p2grAlnafSPQ4BQRcRa3HWhEj7-eTCDRstHZPHVBSgE8FuivToSA1g_9VojXnoy8oezZOBwE0Xw6xv7JkC7OVNXfQlY2XUxUapt6-okYcBR5L96Nv9KCyplAI4Ifp2RUgaLQf041cjUYuCVz6uyNc4Y5C31DzXEu6a-IM_aXjsAYu52C6bsIeE6WF62f9BpTzvcZeYcefOFmyNeX47xMFtAWhAzw5b4cMtq2Mg0oBhhElMpJdFcWOVSlwt34UwX5OSakUDZFNZ7xlxz4MQKGY-lKE2lSIEh8zGoRQEpe9w-33bizjDs1tEEsGQ_TW5opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJZ7D4OwIeHmvyvkm8rLI6jgY0pn-q8Q8DST3rSHt-9CG-5yrW1C-UpSzB57cOYiG88olJbygA-Rhk3DZaVYScJOJXCHc22N4i8K3SNHXDmsMiC7q267v9FHMwZmkxo9lqOTZBiXLF2UcICyAXJkLRHFeLw3S_QQKnBdA86LxU5D4Ui35w36U4_zbVKEmUeRJr24adqGwEvfdP6MQYUhrSVBTAfIR3LM9xEcCzwNFEKIgJaXQ2K2k-D_yDdfsOKDMXHWSwntq5kD9pCmlRqyrZEctedUybUAoeWmihHNDooO5PqFqh7k0m1ruvytZIR54I1dCVgZKUMUSznk686Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oP1PRC8o6UzS-GWHGUE2t66YLCoU7lHA1Pi08TMl86cwVyg0L3BkakogBDLJo1OJ_9e1kZe1d-ksfLQdXsqhaITuBsi3ALlhVBj7zah-Xjn2fIjpR1GHLsN21YtG_R4MJcDBhBBTxPEAznU7g9W-95dbKyaL1k8pzEaxFJcGAdEo-hE_QLaZZwpgz8fGzQgib9FTv4m0s7YnREArkGBDq53BZBApWtsfA1dBOy5DkD0F2keX4-_gPFYhMTeF-8x6skOKbKGkaWx362j0i1OV89oibzHeExaH2Ct1n_pvOwQqGXBlC_iQWLpjNdULd5B1pXEevL_h8_HPqTY1dvrgng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPpWjYqlfN886R4_0zc4R6xWBzgATAlgQXBxi4p7d1KuUZQoqXTBQiULXfbSq_Jcklq4ZBJtN6tHlqibk60Gosow3ppiz5hOLhL71owc8xFREollN0DTsjbBF1yu3UWedTW7O3W8Vyi05ghncg-D2J-4Et7atBCrAw2CWoqOf154Gs23UtChRbLpkwino7XsXB1rHEXrV4Ba1Rl3NWk1EQ1KX3Y8bexRDuPJ6r4O4ESOXdV9nkjkJhy8x3104FevKATurtIADa_ygUR8EMK-GshENrR4hm4-7XAVi2b0yF26xKIGVBQd0IHfuPudPH7YHm041loKzqfDkrkxbo_CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb_woRtMxNeO8IzlC79lqc2nQBCTm5ugo-YaExyuy_sh6FrAeR3HfqOW1NbwmNng1JsqG74TsVojKai639_KNb8XMNtk67MoKM8GXeF9BsgCr9r2J_nFvTlpoplRAo7-ILpus5twfar1pqfvRua-ZDL463pT46SuayXPBk1fFQLeHxJC8Sig9NixfC3FJt2q_Pa36iqGu813XRIGhTPDmdT6ck4d98cTA6Nv8z1IdfxKlzvuqfKgkG-KX1idKpzMbxjSkd7lEuNLtz0qEEkiUuBqYEhY6Li3SQtFXgRCB4UZf3MpOwmmqsu8x1TTdbGG1QUHm9rEPge9yMKlIDbrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=gY8nydnIp8kRvbyovh3HdfcJ03R00e7OoYYATAMFTFThyRgn5iMojusH0QVViu99v1n6MASFft84zBM7ASkLIdxUTAIiLL6gPsol7AYoRi_LYWEje4LcAsScBVOxjHaB20cWPk791POi4HplEfhPTmfEYMDVoTcbV3pA4BAWSXvLpZ9wZ75aCYBZArVt3dVaMyxeyDoxrV5_GxfPglwtzCFwZcscT4u7MkGFGVhBkyOBQCfWkvgK1HTn2_Db-YSj78NuV2NhYSwU_08ohh9TjpC1PS5Swehw70sS9tHXNsZv7ifdLk5POEUP9FSUm6WPTFI6Opz_cvzzDeZWWNQg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=gY8nydnIp8kRvbyovh3HdfcJ03R00e7OoYYATAMFTFThyRgn5iMojusH0QVViu99v1n6MASFft84zBM7ASkLIdxUTAIiLL6gPsol7AYoRi_LYWEje4LcAsScBVOxjHaB20cWPk791POi4HplEfhPTmfEYMDVoTcbV3pA4BAWSXvLpZ9wZ75aCYBZArVt3dVaMyxeyDoxrV5_GxfPglwtzCFwZcscT4u7MkGFGVhBkyOBQCfWkvgK1HTn2_Db-YSj78NuV2NhYSwU_08ohh9TjpC1PS5Swehw70sS9tHXNsZv7ifdLk5POEUP9FSUm6WPTFI6Opz_cvzzDeZWWNQg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebFcqyT1HBpsUCPWPVxfaEYipPB_1jollD5myaXnWEj_CdWxS8YgCHjRXQO7C9Hiyn69fYpo4Wr8nme97rFBYikR2cw3unags0pJn84PBtge5vCoQ-OnWZsuyj17nmWxg5oB5YIz9QSudkCPTyz59koVU2RyVmtGjCMxy4Mx8qMifZ1RKeyaEvulI5zIw9kCdGZapFl8g6nsvTdPJMzzQnfldcIAPswNQ3x4Am_MabLihPR_DMrZX2qGAuHJQgw9Nob7gUbvp8yvxShmzW3Y_lFGEjBSFNI6xmTVsQtZBXpCM6l0DKEu02NOLZKyNdizmglc_k5P66xAVlEWnc4yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5pUb910quSxqLimYJ6-bDNSXnTHzTQK88gNJnY2vReXcs_3yTyxIMqzY1MM8MVe1YK8G782DyhZwvA_u313zaEwd0eBTmICHA59SZCqQvg6_zMuRNSo3VYU-__SLUg8WZfsPxsUcl04NwpjNGFcoQKx80gWkO37zn8cnmWyvQGpgu7N95uVstfg1luLWDytaRnhFnpLgsgHkQT6Z2TE9TrUymm-xPHGfrVXLOASbWgWyKgF8AofGwV6YqAvHGnksfDJiwlOYcz2-JMO-bilOZ6fJn7dEGb5WLITbaT9iMD_NSdFZhsp9Ace3raZsfH3K91ebQRHir6TrHWmvnPg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDub74Miu3GGnG7on7HID_xPCxEajIeq-nbWlYRY465S0mgpgf5rgFW6zZJhVEUaRxxz5D3inlY4tDTbpIrkrYzVtc1l36INhyydvQnhMwia9ZhlZeJ8hrMRvcykbQDnLzAGlFMivfP9BjNd7d-qJlUCLucyppra_VTqnp9ulQcAmhy9KeOgcrSxogta8DJdZnNZ8YHzKhpExAUhkkRQeuBvrRH1H30fQOJs6M7XJu7K3UexDwMz730T9kDRrIbqp9CO3OsOfs_e397tP_X4EiobvaN0VaxGpeNyhpK0YDWaT6WN15q7jc1KZWK5yMHKFUlrOpdwvonJPMelRH_QFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsL-b_CktLbfDSH7raj_E-DxZvWQchwTZZgM74xwxM8MF-NrheTburzUO4gLh2xa_APsjOZigI5kwhq6eq143M6S9b09QVT28bwfZbZ990yBUQFopmOhJxNJ8YhJ0uAnqsueCe3xN_Ws7IreJ_5zrEnZvD8yZjOUtUwEwxd8jUAWhAejbSSXLtbGa2pGsKbumsf6rmS_2UGd8WbQELoi3CpG4_mxpOPOEa1DeseSwkiyg60ine1RjdybCFgMlqJjN3JluV_PqmZD4ZsTPyWMRciGyEWkNzt8fOQYsFnKM5IOgXTDyvEV7ki4I3esKOftZVp32eP9KriH8emvyQlaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=s5gchbe6jbO1SoCiPbG1oPXPUICYR0FyWAmRH4VhRBFZHMFDJVyzOkBiSIyhv5afggLjbWMGOO-X8AzKRDO21TOtaAU4Ai9O4KN4puk19kWAJJbXyGJA4pezn2ysuxi3H-JPDoKgEtHEba5aZcPkniQgXzJnOUBUH6zWIj0CLo9bg6uC0p4YGoykDT3iVzJDYERRfg1ac2Bb30bY2_MD_mbEhHzafyO5Fv2KH6j18eLJiwH3SpurS8A2ts3iqqtv3CaxwJrSwCunP97axlmmyvc4KAZLUiNJuEoO-qUJ0QWBE3x3lJrjfnSPd30Djw8N6iwHJq7GK-9U02vC_xcu0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=s5gchbe6jbO1SoCiPbG1oPXPUICYR0FyWAmRH4VhRBFZHMFDJVyzOkBiSIyhv5afggLjbWMGOO-X8AzKRDO21TOtaAU4Ai9O4KN4puk19kWAJJbXyGJA4pezn2ysuxi3H-JPDoKgEtHEba5aZcPkniQgXzJnOUBUH6zWIj0CLo9bg6uC0p4YGoykDT3iVzJDYERRfg1ac2Bb30bY2_MD_mbEhHzafyO5Fv2KH6j18eLJiwH3SpurS8A2ts3iqqtv3CaxwJrSwCunP97axlmmyvc4KAZLUiNJuEoO-qUJ0QWBE3x3lJrjfnSPd30Djw8N6iwHJq7GK-9U02vC_xcu0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTzp9nfM6mB8mPVD3qdFNfj8WZL8bQRPqiaV8BSMXZIq30M35NadKawqo1f_af8VQ4OWBv1ZVJPg0VCzRueX6YIbdewzWY3YXz1Mr-ODTzs5jQjbXbrTlqFH7ZYAVMgC-rTTf_j54MeoPiiICDKlEO_-w9DIWNGG5SFcns_v0IKLOyasjrChhrFYXYFTCXUR7EBGpdEbbDhRMaIKzNDP9Cb6gMNuCkWaitdLG7krOi4bHahfnOpYzBihhmQVLM8xniq8sGvSDNjex8yiahBHvN7otz3979-Xjc8CkrExaou-sHxzVhCFa6RZtwsYRp6tryzTvAmOZXYGBpcA3jP8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcnwMyhcOHi9s5dr3ZTqWTnMhUcP0WM_IARQRDSodWiHwxAHQxT5QoZkVRb_AI5ls5q7vSU8engF1X6wS-4A1PI8IthgLpaGh9DABVpFGJm7auj3lT6cGTRvTTI1-mrpUbZ0vDwW5y_VVDodT657d3o0SdVP2oDz3Z4b7A_wWAbthXda_wB6DWIpCBraYwLGi5Vbb79fnD311ilYB01rlj-PEUTHdgJDtL5aErstYxzpeU-llE032bWNPTo2X1jQ-3fys2A-oW_hFCOkOey3Bje4BhUmmsAncbNuagS4c8IUxJzJgxRoziAfIV2sUaHc-imoxlRB6YtsrwbpQIkZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-VM08_tC3LGOZdG0m2RpQkrLUsFrEY0YG3rFp8oQKZLeGPuwms_YvqY7o_LvJjq5Q-ynn_q3il20pZFFCvfCYIfxEzh2LxgdL-UFL9U8L-8968rdHi7-e1keVj7EgDv2E9M39l84CD13RINmvfB2KgiB5EDUsFGXJbNKvNFGbnE23qqKfnedf3kBu6VR8kyps6ZvAvnO3qqwMoO5_SsMeavktFOfMDQhbYQs0WIT2aOGlyuSh-WdBmq4CYozPW1pQAQSfX-FK80rI9N0QecjYURNmZ1Ijp8VordfZxW4slWAXyzYupaCea6VmzyinFEtv19KaL2WmDHMlEAk_FmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiflBgguqH280kErkUOLuTILVSnaVfZr9kFbmpI9B1nWkeka3ujfQG0rFxoFHtJ7Tn1BG8oHhj7XujegMcbMXYeH624hl5Puq5eFWeFu0Sg5Xm0IUq6TH02H_eE0ilZXoXAUVzZBr4MCRSpNgAWOk5y2HEZ8bk0SbJUbaymltgLlXIsvHHqj-9hORr55lkKKiF0vY9cE_Vn9YhehPj3l5mv9npgm5bYBd7wNWLATxPlVJ9VxLL_tq0nvhNzIqplGyHlJ2JOIvOuKgxin8ovNcx7b01IBOCbJwJjjt5XfPDdjZSp6-BP7Wa4-OyL0igdiwz0eIeMBFCy5mM2xV_gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-zlu9TJEyFKbtRzEt9uuNxj4vTQwb4mpSfyv7TjbnCXN8VP4QEPFHxym4lb5NXAn6Bq0pK7WHPuPYpdVAT0gL0gAfl9RUYHXfdlCeIs4cWxpWvCjfj2jiMj9NBsv0AEqYkOCCD_Bf9vm3ELAysVOozQy8yNfsBTw6ne4efW9qOTI0zwRqzy_OHJY7xzZjIf9N7WWMJo-FsVtGDQd-2GeVxdmyr5Sr2j2ugW16-dfwqvUaB7WQqcIUkPLvIvDDyQv0rlvBtaU9WWmx-j1fhYjkM1g72w3N1QVOTZHsKgDm6yGYBiq-Z0wuAy2Tx7BkutZuR-AUWMhR9z3x442vC4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=QBVxQprEs3kI7GjyHT340MJs9BvCKvaQcBvaFq6Pmg6AcgZwik37LoM3fkOcJTcBFdkx8ijJVzWzgK755fkOZKXZP_vRxSPUhTNFqEO7Qqbwr4LYk0ZsWXmUqi0uykWeVIg5zEiQIJFNFVtHqdAxJ5J4mnzrderH8p8rXDQTx1btiP5ryO-eBtr6-SM8ToXkV4cF64x0zTO0jHV632o9IGLLjfSMadIUNH6-oQuTuibeoJIgVNnd_c027W4_WgPj2q6alMRdWNdXghpeN5uEI5O7UwEEjOOvYtr5auUKfmRoWGHv1ghAa95p70by5n1RiZqfXp60BlseZjwpLhmxqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=QBVxQprEs3kI7GjyHT340MJs9BvCKvaQcBvaFq6Pmg6AcgZwik37LoM3fkOcJTcBFdkx8ijJVzWzgK755fkOZKXZP_vRxSPUhTNFqEO7Qqbwr4LYk0ZsWXmUqi0uykWeVIg5zEiQIJFNFVtHqdAxJ5J4mnzrderH8p8rXDQTx1btiP5ryO-eBtr6-SM8ToXkV4cF64x0zTO0jHV632o9IGLLjfSMadIUNH6-oQuTuibeoJIgVNnd_c027W4_WgPj2q6alMRdWNdXghpeN5uEI5O7UwEEjOOvYtr5auUKfmRoWGHv1ghAa95p70by5n1RiZqfXp60BlseZjwpLhmxqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_kvVNA-2Es9suacYbY5zYhBG6hwciQvVeZyurHxEvlaSC8MBIHJnEnzZV-NhqVB7wFaJBZVPUe2WZU22rIYFzCT_2q2z9S78AnnHGAAwJKBUhyDvhs800LtVjaQEM2bNzYo9zRFDlDEqUfZEMQqrJQA8WqKdwOD1VRVREabeey3ojnVl4h2kVHCWQF-XcuHle7yRnVSb--1lbX3oGUqCSBXambc8Wvo9FyaETjCvC9FDtly_AdcLUiPwdHPM8W7Qeme6c5toAaRrk_N9d6SD-9G8FeL9Hdv0mKa94GJGKhowaK0ikvDpilyh-ssNwAomcfvtLqdvbcqgwU_PQmqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=IghZNgMgx6ylNfprLrpNaX5lr-_wmIRDp9SSfamAXVuMyCRn_MLdE6ud9xU2H7DfpeeGlFFKTmJKTrBk-RjSf2NtkXBSSLfv4CyVMHXpEun501QyM4w3umJj06LjJwsUqzCnHUJXlgrPr415xH-r7yMOFUmop_rdd51Giw21DHi5S1y9Xo4YS85tW4B8ekhl2TvrOovvFhjl4P5plb-1WasVoOlGirYLeVu9099LVNCbcLGpoT3Sh44UlhGe8l_s-PDkwtq2AuoTeDLFkAlyoFdquKxTKICX30_AXdiXsJP7PKjAWJQwD0dXrXW5wC4KLqMUGBFlsEW1os2SQ8W_Haakqv7CuDr5BxaZHMD3qU2sTAjyRyMbodgGxv1nxBSljUEFtDNK2Y5FZLH3ONZt6z9VPs7CsT5nNO3BGwM3kyav7x9iyDcoPKwzBDuepFCvUqY1jJ4z4ONM-OC9llCXT8GztSvt3zHXnaXynORIoz0q5hSuOwwzlL2gNh4VfEUMnpXEooHpMuDYlRvz300cE4NaeW2fKF5QmXHJq3yK1_zwSXNzIUwBdNYCbs5DMCWt0hpkUIGFoUjI3g5fS4MuWYHv1-fmryzy0gucKV11pzJeXQM_XPdnlgaOk0DkbrJZDxZbt9H-ikRJnyMKQcvumVMrLyTt0s11_-0tWKL6nGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=IghZNgMgx6ylNfprLrpNaX5lr-_wmIRDp9SSfamAXVuMyCRn_MLdE6ud9xU2H7DfpeeGlFFKTmJKTrBk-RjSf2NtkXBSSLfv4CyVMHXpEun501QyM4w3umJj06LjJwsUqzCnHUJXlgrPr415xH-r7yMOFUmop_rdd51Giw21DHi5S1y9Xo4YS85tW4B8ekhl2TvrOovvFhjl4P5plb-1WasVoOlGirYLeVu9099LVNCbcLGpoT3Sh44UlhGe8l_s-PDkwtq2AuoTeDLFkAlyoFdquKxTKICX30_AXdiXsJP7PKjAWJQwD0dXrXW5wC4KLqMUGBFlsEW1os2SQ8W_Haakqv7CuDr5BxaZHMD3qU2sTAjyRyMbodgGxv1nxBSljUEFtDNK2Y5FZLH3ONZt6z9VPs7CsT5nNO3BGwM3kyav7x9iyDcoPKwzBDuepFCvUqY1jJ4z4ONM-OC9llCXT8GztSvt3zHXnaXynORIoz0q5hSuOwwzlL2gNh4VfEUMnpXEooHpMuDYlRvz300cE4NaeW2fKF5QmXHJq3yK1_zwSXNzIUwBdNYCbs5DMCWt0hpkUIGFoUjI3g5fS4MuWYHv1-fmryzy0gucKV11pzJeXQM_XPdnlgaOk0DkbrJZDxZbt9H-ikRJnyMKQcvumVMrLyTt0s11_-0tWKL6nGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORiKnngQaWt9_cGg4oSxZEzfAzN3BT2HIT4s2QFmVn2QNA2Bf6vEhUi9UYrvNLuuy9L0o0yEmlvKpvIXn1NQ6AOyxurmA-cj43P6CNMQbkXgWgX92RYTVcl3M2dRzXRQ--1ZInpwQtoVuRSxGtDJIM56p4mS7R9sGKdjcvC2-vIFtNHXyrXdFnuHVJF8i2cvWx4vfTtHM71Penv9NnhHM-NzteIB49I6WrC-jtgKrvqaRGAvjelv9ZXiKo4TDC5YEirGw4B6Xf4jNpkG12deVwA8ExREKwgLhivETz_FUKinoL4T7dadrTp-mAITwdlf5414m2L6-fMG3AsPdjBjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K69Ka3ar15tZL4O2KLyPrNrdKu95aw6bg5k6ZNM9hN5Y7spvRUwrxgRSi6bz2rMwy9-jpLDcqhkkDqHkb3NaCzzbnRWVvY8BShDeos3zKypuJ1sWG06ssfNX2FoB3XLM9UJYmR5_W5B-obKkd1JGD_6GSn-nanBAaORs-4ldDAMluVyTus-Tg0mL_2xupdlwJ3ppuNnGpkO3-R_eC4wUP4C9_SOGtXj4LmT9hn7Dx73bXBx3YF877QlFZEvto2ZYHtJzmdD1_QCMEGfjXBDLRKrMFaamMjzxQ1YAkAqPML1XWevyvgWN7GzlsuBPb8NMQ_5xPNtiaQgTJJP6sHQ4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcPwvfKvNZZBtWCWZ9NbvTSWMBm-cUvKfo16tQBCF0wp3RZNDBLLCSayYvQnpzM3TJvPlIJzBpjKbxPYmrs5wf1oGqWXoGIZovmE4YmMVD6R1e8vwiIAqv0syvownV7wQswi3bX_4E02b9cpjaxjeNtXW4Oq21Qt-CBmTTVZCOj4r8toW2WQ82qRbUeqCBdoxOwYK3fiqvS5zY53rasBRu1UMYesa9LQXevhrwbU8UchWFk4G_gsZWmrkk3rj-X30k6Pc_pqznIwUQs8IYO4XCjRnRFsK0E4mzXK82kaCZhrf7ipm_mWt1qnUP70weYPmzQ6hCNjcrme8MJDmBlLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABfQRIu8vS3joiSkzARj-7w2TNb1SLpjRfAoa2qzWjBafcmN86WXs9t6oSEjpFL2jT_CnRL50vw2BHkycxYqP95GXmBGFhoEfBCrcU8zWmU1HI4T_cruh99OZqwtXk-vOegM5htbpoP5DOZ6WgWnzGOvhGAQa1ZxPpPr8VqHUMaLDIK_LAlj9G5__aepkBY1fBLnCLqAvY6-7AeLtYQfU702FQBGRqjn8hhp18qROO80ged6oV-6tSNHon4OEf-E1AgVl_fooq7rOondUXxy9XgdncC6lkDt-Jc-Nuad-0HXUGBzYIaI8ydAMup10wcb9UYLtryyZ2CyZ67YtJrGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBRW8NEN5vmLVjK95e04yezgFKPh-OThnXSFAwklG2Wcy1KNeTwTzQk0huZ_1lsLiGuoI5BqRUcv0sCgz5ZOBhRhxuOdq3M-lZjrnEnSVvhJ0ATO1Vv047D7B_OfLyECDcsYNcnb5VwMboZFkQXkWXvs9C8jVhm3kTL2AYkp6KUd0FWXXw2Li6z-SHJcIr-KXD9az74AcCV7nNCkOHuM3-SA9vxQ1vFDeBKtJDrrovc4ZTkwXbde7kRjD0yP0kPy8RTsJ8M-nB344I0DshT9by4ieTMq9a15i4VIZH2qF01CFBclKXr1bCTc8GElUjzZ1y3gZDhaKdYHMshPNCWTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NM5D9WYTQ3Aa6aRHS21P_DVLZtFTVW7_6wFRLdY0-GMft5i7RsUBP9LnbN8AlvIUPzjgE3WLi4iu4BT523eRREdm7GYH1cuJTahWzVFRn0Vrq_Bwl_zJS47yEkDALo8Gtym9F0cPHrHyUa9U6FxIrP2a944nE5TAnzyLhFydA-6O0lZ47QCNuTjE_MTgA9xH35ACFRA4RaGS01ALjnz0DI_gLjd7GlbhDIB_LsdGMVb66AcoT1y8qQTj9FoKaz27sR7EWS58M_axspHw2M4ChEKC0b81Cd_ubzx3vW6_fykxlHuxlV7b2gJUNhaFlq-xJWZvcF3qyu7PHIvlYAoZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML75xhPZlr0U5HDBNkT3cZS0opEJfUZxDQYEAqRxyxe_2i_-9SpuJYXfw0MxM8i-MGiuk68atu-d1fhg0wE9vAh6LpgTJqy9Ek1_0A1HHq2CKX5M1ER_CLR3C298ntv90E__xOAvdWHJjPa8ruBu8DoB4MIQyaigZl8gN0baJmyDM3XoJMklOPc9UlSFdSxZ2anQZc8vsnLjr1G3XyE1JDpMyoZGea1Os2GD4SAVhLJ2JbCRqkyq8YSduZxgUpZqahOEiHHjDujCtrnuyeyoggLZAnZYpjciVZAmblUMuKeh9Dpc198G_iyRV6c8MjKSdmbSx6Hm9MHBt70ew9E3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=IjO1xuYQKkMt1SClnvwnMD42pskXVWZiqfrjtKedAGzM70jdhDjUp6LY6oIwpK50ted3e3z2XSiBv5lQ0NygEnmgqcoaTGvRPRu85ioRbZwqA0wTwaiyFu7AAUflz1U0ygey04rSzDy5sUcDPczhp_gZWon2SO6DQpmtlTTOJWGeYC1z-lYW1_L3JSaoHZhYEzSuI7iEl2UvjHQU6g_MInmGm3lz5LPJv7tq9cGDax5Fr8OfEXhfgs2JuI-yd_xygnTxOrd_78Tn7t5HXrkEe4QKfKDs_XMdZigtPAE8ZKddqfkDiStCz7bu-qWkGgYl4i9itYp9kVThDA4iqigRHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=IjO1xuYQKkMt1SClnvwnMD42pskXVWZiqfrjtKedAGzM70jdhDjUp6LY6oIwpK50ted3e3z2XSiBv5lQ0NygEnmgqcoaTGvRPRu85ioRbZwqA0wTwaiyFu7AAUflz1U0ygey04rSzDy5sUcDPczhp_gZWon2SO6DQpmtlTTOJWGeYC1z-lYW1_L3JSaoHZhYEzSuI7iEl2UvjHQU6g_MInmGm3lz5LPJv7tq9cGDax5Fr8OfEXhfgs2JuI-yd_xygnTxOrd_78Tn7t5HXrkEe4QKfKDs_XMdZigtPAE8ZKddqfkDiStCz7bu-qWkGgYl4i9itYp9kVThDA4iqigRHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6LsBMroSRd-SsG7BMlG7AHR2lJFDRYZ6X8K_fFTYj1kOR48Q0sCgbT-Aoop07TN0hcJiKG0mbLRjwedeFKlH-kodOtpTxyF59PLDlXIySoTTO43raVgoKmNFijEUFI_CE9M48tB6cR4ZuebcmSvhznc_Hzb8DyVdEA7ZMGooAC7Vula8etMtYyFx-RYSkDoRVz4Js8uSIb_rOOimWHI5iKkLXo_mX-QSd2YIALCSZi_syfJzV9Ou7CM5X5eoND25jQIU3jtGX-Uecsx79KgQu52jT4LF6xBx3bdvEqz-ZJ7IgRwW7KSYQWpnSCArxCOmI6uG87nKE3-oVTz-CUQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=rL3xVCz1FcINorCm8j66d6CorTG3qttdK4YPqjoCdxmR_2McV9Ne0v3hrTk9LX2-GZvTGkQ40aGLDUEYmiivfayttrU9FwQTg4s18GmJUo1UeCbvEjABocokyClKkXk85LsXeZL11pVF1mZKg2Q8Djhdxp25jiSlPazLDgsfOMb8vdijzd93kPMnl0Q9xLdK8q2o-Wb6rFf9NY8_E1armzX9t_m_5EQLSxDgaqZMN2KjuoPnmjEyrHFFPapEmJLGlTMdH-mz25tRBNE6iovb6PcO6AaagGkH9Wnv-H7iE3fUWvrXdqeJav2ByxHpQHZdBOqzwketmyQnw61Peh91Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=rL3xVCz1FcINorCm8j66d6CorTG3qttdK4YPqjoCdxmR_2McV9Ne0v3hrTk9LX2-GZvTGkQ40aGLDUEYmiivfayttrU9FwQTg4s18GmJUo1UeCbvEjABocokyClKkXk85LsXeZL11pVF1mZKg2Q8Djhdxp25jiSlPazLDgsfOMb8vdijzd93kPMnl0Q9xLdK8q2o-Wb6rFf9NY8_E1armzX9t_m_5EQLSxDgaqZMN2KjuoPnmjEyrHFFPapEmJLGlTMdH-mz25tRBNE6iovb6PcO6AaagGkH9Wnv-H7iE3fUWvrXdqeJav2ByxHpQHZdBOqzwketmyQnw61Peh91Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=cc_EsWJ8tWd0EZQMtMtbEckYuFUsJ_aStWP1vEbPK05MsZC3etPVcWlcG0Z6OdZHVKKAgbEQ5-yFar_gCAIqK94J68OwMZcCTGrL7ti13llyl5rcwMrj0xVNDN5Hd3BBO0d-w-eYxnMl2Yh7thg-fX_dNXDpWHH9gEqWd0z26TNqFn_sh5hNrSL4QsRSmCQkXSwlp5xp-18M6jUjQ-4RTm1jxgBtI9-W1l5no_RMGHPvPJeNCSjfp5QYME2YdL48WCOPmItzlLo_pbWMdrouc-P-ktc0aE_qyS6ZT7jg2JvirdgG4ZlXyrtfPqlhHF0y6iU7qL_MeRZT6wWUs3FtOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=cc_EsWJ8tWd0EZQMtMtbEckYuFUsJ_aStWP1vEbPK05MsZC3etPVcWlcG0Z6OdZHVKKAgbEQ5-yFar_gCAIqK94J68OwMZcCTGrL7ti13llyl5rcwMrj0xVNDN5Hd3BBO0d-w-eYxnMl2Yh7thg-fX_dNXDpWHH9gEqWd0z26TNqFn_sh5hNrSL4QsRSmCQkXSwlp5xp-18M6jUjQ-4RTm1jxgBtI9-W1l5no_RMGHPvPJeNCSjfp5QYME2YdL48WCOPmItzlLo_pbWMdrouc-P-ktc0aE_qyS6ZT7jg2JvirdgG4ZlXyrtfPqlhHF0y6iU7qL_MeRZT6wWUs3FtOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr6IWEfRFwukbG__kiItoCRgnc_KlKW-bJ7V80ZT8RqRgPnsS323YWD9sAexTzxW4cceTAK5BMi5OfJok_AnW5D8m8SNEdTvKQeuHZfZLkMkA6LVzVBioyLmbWbiMbdzhF77s6UvKoH45uTlZuh_jd1p8W5c6JDSQmrAnuhPbYbOkKlBgPWB-KT0mh96rlpsA_taEJjIREYMvBQPssXiCbhf2HXR0_uVPduO9VAn3S9g2oeZUxs85agQfcFIlyC7xxinOodqSnLcjuf6YZQYpp8AMxV6M-ZCh1O3Cza3Gf6srNQoNQiBfHlVxULLYWydGkjb8XrG-UyUcPbXYPd0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUuka7nYJlTZ4MCpQg5jvNSDBYVNEyuh7NnTyRdZjwF14IQvvd87ZVp4HVcAIIcuDAg3wcKXu-e6zsMkKxfiecKeirHXN4iOPCcVEwNI6wN1S0eEbcZMZbFQPvAN05LpN6C0aKQqsHT5aa8qkzzuwVl7uCCCKG-o2swJSRKfvUPkX8rV1aUhac_eOft6u9BR6w2qlb2ENzikWvMJZHHwYPenBT8urFHllKUfrdhmR3GGuaf8qEyezXMmP0vc0g2A-0acRoKvvsbUliU7o_lKLQ_8YA4jT2qvZk-e4fWWKI2uJMyIUIKM3S_Rx8ITONQUOtnFBUDOsPou3GDVoOo5oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdg6JYA5lmURd_87UuXSlcZuSgyYHHfq7cNHTI8KyUcMxb5oPWJDFMsHb-Ijz77eDOrUiH8sOXJPU485kmhl0vMhCgVAz7xm2D56-kSLHPxq0vDf6KFCONGuJ2HDQVgb_CJs-Fm2ZZ6KowcsYarD-vERIlcm6Q1CSmFAOsP9X1K9m5BZHYC92wrZhE2mOYvCZuLDwjGzFHJ0WnZ22Xx-6jRIWG_tvpfiP9JE2isQIn0SN6baGZr9MIAUna6qk0ohsYhe6gTWhBtCOkprTjM7xpKfi8ngAPn765nh1RguNdnpBokdN7S2XrYAVzKJULz8eud_yKn5s_pin8N8eqfPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhgiiirrg58V70Oy18HShOubX1Dt3BgDu1RiXKAwm8R0yghSrm92lDYHSKHXzp4q0j5Oi88DLmlFVqjlAGrmseLy2cMglC4FjIBJAyVO3tAurrn9MT711V-R68M5T8oionlapLRTYOTmNSeHgrqwCCdeQAxVtTJiCNttojxFPy-vNY7WwWCBBKb-_rL48DbPKvT3iOcFMKMzRr6gvX7r0Ce3OUiVaSZgdYneqBsyLBcSd-NCAZvqRPWq1HkqgsT4MSglVXIQKlnJJfHfTnbUAtmFgdqhvbYfAEsnu1Ti3ERuJRuxNJw8bkd_C-L4CGchwgGdKdvR2A0Q-vGMgwVFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo7_1TDcdaFBD1JGxL3WlI3qClKnlKq4GnS5Zr3GFPlr872rzBiun_HSUQot3C-NKT7b2tcJL-y3luck7MrE-HCNm_oFYpszFNaZUEKvF66StjCm6nFBXZqjvDPES-X_lXpr2PNNXs0HSGmVYdq_Dn38DLVxULJenbJ0LX1Ftn0sH-CMyAfJWzXrqNSYCcT7D5dd5BmgThwUl1A72afaR92Dz2zlXjeJ_J9qkCTJk8hY3VRGHIK2Qca8WJvgP-M1Hq_tB1zxy0VYc15Os-_6GTYQGoM5UpmX_PI5y0aH7GkL0wcoA8SXv5rbN7v7t7o_NMigI5_21K7zDShyr5Egow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=PfOsY_rZhA6wmb8ADUjj_Yws9WPuBne-cEv1kdUf6F3lFqMaVYrTPrJriTghiPrLoMKNEoALJVSR0wj1ASO_an8Wyn_c5tvaGbebpCRsFnPeCmuSYqmGNHCl2UA82nvDzYsvNhtRcfNVETIaQIihD4de_p7LM-MamngFTi_JFgt9KgM1J5uTeWHfeN-XKPIXddBJ1Vfo6XleggGpKya3jFqON3DZILsFzHJZjJCRbwll26FwfbnJU5Ur_dIdstdWsP0ExwE3H0TcjaENB0Vz1zKE_K0ntK5cgi6pykHmGS4Ttzt7Qvh_dU6jsbVrId8z_YiMQrUQF8kwAqG5LwPnLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=PfOsY_rZhA6wmb8ADUjj_Yws9WPuBne-cEv1kdUf6F3lFqMaVYrTPrJriTghiPrLoMKNEoALJVSR0wj1ASO_an8Wyn_c5tvaGbebpCRsFnPeCmuSYqmGNHCl2UA82nvDzYsvNhtRcfNVETIaQIihD4de_p7LM-MamngFTi_JFgt9KgM1J5uTeWHfeN-XKPIXddBJ1Vfo6XleggGpKya3jFqON3DZILsFzHJZjJCRbwll26FwfbnJU5Ur_dIdstdWsP0ExwE3H0TcjaENB0Vz1zKE_K0ntK5cgi6pykHmGS4Ttzt7Qvh_dU6jsbVrId8z_YiMQrUQF8kwAqG5LwPnLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-xpq8ehUVRckRphjfW3xxu0FLeX62U7Vd86OrS4hFydMZ2rS1hRv95Du_tiCfdZKHzMZc8EmY-U6coyU4_fQbLbilOEaiME5ehJRVRHQBdLsblR0yMy0OxugzHqMI4Ecaso9901iECqmBYjzk-cocDgtg_QfHeEdqRSn6-1CbvnpmEjVd6k61EBBay7QjyiXDz4elith4aFEzqdoeNJowdzzGluzke5RWz1x7ZMXZGa-7inCtxO2H5S_Wqah8mVehsg8RXQG-MJh17yYzN_Zu1CAlJpl_f3QYQhQTMNP-Nz9sOq0i_NQGYaiJEZ6HwppDZpAWHAmaiIlCDBlVjx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkilULWim8czCLyebLy1TlDLYH-c8BYFB_yLijFZKTrjoiztCD6NBQ1IvPQthgZFrKDkkKQiOizV5l77opwtrCGh3hZoMZ43gca_2BSiGG_WM_ElkaoFHco8w8TUcy4Ry-JCT8Czpsb17Covc_Ri3rJIkpxK1vK-88EiDiHBY1b6wLB8pL48XVf0_JmsfVQUa7gPMDOK8ID3lSIl6ckqHlDfnuk2bYwrfKsiXraWvTUANoL5cANMfliwJ9R_PHWR-n34fcD7Jd1H5-KDCFqtsy-NPQ8nxSp1GpMM5jPmToqN_gTkqn-zLV7S5s7Olh4LMwZDfyO4vJxQIB8AaEWaUTGls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkilULWim8czCLyebLy1TlDLYH-c8BYFB_yLijFZKTrjoiztCD6NBQ1IvPQthgZFrKDkkKQiOizV5l77opwtrCGh3hZoMZ43gca_2BSiGG_WM_ElkaoFHco8w8TUcy4Ry-JCT8Czpsb17Covc_Ri3rJIkpxK1vK-88EiDiHBY1b6wLB8pL48XVf0_JmsfVQUa7gPMDOK8ID3lSIl6ckqHlDfnuk2bYwrfKsiXraWvTUANoL5cANMfliwJ9R_PHWR-n34fcD7Jd1H5-KDCFqtsy-NPQ8nxSp1GpMM5jPmToqN_gTkqn-zLV7S5s7Olh4LMwZDfyO4vJxQIB8AaEWaUTGls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKWyiDeC7M2VQuF6XXptp32pOChG1vShR4H7PsX2TXdjPpDSALHN79IDUqYoqZHUW73J0tF-QO-aQx2JSKmxUJM467CuvOhXEklq7-6jDfrcpk1BOVKT-ahZSwZQoaQ2GyXoiCnjvWV_yxFFP3UCVrtpMr8h_QnZiu0lbqNtfOauJZt586WArPOze8NDuQnWodWqHIEIXyBFlHfyBNeQUfDNaFiQkKvWkbTWm3p88s63ExUMpLEk-05CdZKuuRrvOwRbLwz5Whq8z7b7YjA-fcvVogLtS887zUAVVt0akKqeBWYO8v3njhGLUOrVeTNWvMd9kyrZVlJdjeivCypPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgRAzpNYr8RM6Fo3itXbwXS8w5wa6M3E9NlavrzgfRbPLOMQ6cudhpI2hBY3-1n8S9GYnFuWJg4A2Dv27Qj4Qz5cRFxBsSpBlbpuLDjMnQescXkJTLzEDdBgfC4Q4lWZBlRl9zLYaIXUAeDq03TFriq-S8VGUTn0otPte5Fl_q9_BPEY1zighAN2RndMVserEl-qD_-LHOAI8SKztJi4ba3ywFp4vTUKhOyVuw2HWKJ4neztzHZ7nsySuR78wxtNz2IRTqnxwQB0zBLrIwwknOnLvtBh0qAo_E3YYVi75n21Ho6Gj30jhQUadVzvuJsFmYpdw08wPefHHUjClxLe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBZQXb0w04z7Yg5RrIN1TPkXGZsFTqxPQ_WxBlBXz-R3mZXUIoTXXs2gycPg_g6_8c98WwtZORkM8M0XoYfvgI10NmxHhxcBZ9xJard3Cs4F5FdTLDUUSLF4F9KJJsuFwmt-7GcxiOBjOthwmQRSnlkmm1LcYD7RShp26HdIz82ysfGUd0BTWg2FgoaO-EVAPy0ij7XrnUH-S_4wBB6ff1ZIS53pM7nBxWWLTY01EBeQWmOs_-0lXyP-a4qcabvrlM5Kj-Vo7g4kN3q56x8Jnp2RatzkuYvYRc7wdQfUAAvD-Od0rpNH_NO8l1N2A8Wg2qPaAQVAw3wM7GHEL43P5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccAB8CMC1NVKcoSde5WAABZgfcEhcgSs97otoAsR08HhlrYFvgC8rxtqF7jZf88uc-W4GRSMfQlAX8vFIXlhl6DvdfhA1BMBdU7cJcxugI-QQLsu4FjdG52iw7lXRirEPU_RYcZrxmG74qFu4GlmN7g0hQmDAG7Jj57pt0lYBv8kxao6jURUEkBDK-BFw4_ghU_uKNg_2k_eLP32jyGT_JXtwm8Xc03T9EyaqaAGOWCzLsX52VmvG6Nh90o_laGQXXDlFdRodDLLuQBELDHJyiQvM4H-5DP405iOVw9tK1xPJBsuwJ_ePm-KdOyS8Dp2S7evdvUcEltzJ62b_ttf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLtBdg-F1VvIhCJBDiW6MVypbVlwFhJSz8d3FiwqQb8vUeg3mNvrak0OhnuLk8a_H8AvzzCIqsaREIZfSzfIHt7gv4e3Wsnm9s2iIinBmamNFLWQxlpmxB_hA7_iQRMOiJsjPFa6GqvuGxWQCYTuy0sqrdTbnLD3txPpPvnCycDHHq-qJKu2V9DCw0Kp1fbToYCmNtkSEQRkaC0vEHUFhvYsab_dyORS_TzdNLTc-l01-66stbF72XTwh-25a2jvCB-fgOtSdhIygGA0F0Oa8OgpHFs4qS_m1UQdHb6DVt3yzdJ-Yo902yM3QPjnJ-fFsNesK6_ymqELvIV5qW2F3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sLZWZtPP-wYdkxpJFCt_Vx0H66yZX9PoGXfeetY9Dc0DLuGageH4n9T2KMRkCG2MT3JCgC6KGTcqrnIyLzUtpBoOaKl18pCOje4OLxfvvDZlEmB_u7mh55jze-jaUr1Npq9H50EVsVdYanWakEa4RfwxuyW_3cayQ8LcpYm2Db_Ui6DFOpwQFhCzqkht4A6aYcHsr5y-qitwh2P-7wYzlMmeCmC_1a0YSTzmOZ-vAFTcwMe7G0sHfoPrfWSkZrZr4KV46Y4LYgjT7-Yf1m0mM9HPT-N32IzLNRcqIXXSN32SNKnjJeBkSIdrImuk2G1uNFhmtJLIafc95jCdsF6AoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKOiYU3Mi0ypbkT-wGULOP58NJAbqCCnsei8_mm6VcdEtDs05KjONs_JDzdG4zQ32_EmpINgjFj9gB9SFewn8IX4vU7AV3qpbtOmnc4fYmcMqI-8_gyM9hA1_RPRscPpuxEciH8i68snOtWRuqdtvUPA6ZQSzg0AfEUCMquMtK_Fi4T3_771qmhB7Y_eDACIScvHxILq1Ax-Hss37GoqN2uTwgUVSQxwlekodjr095jgNULzTSwAOFgPulutx7rMS5zeQpu07mQ-BuzVppbHUUFcWrR5gxNjgjTBl1zjQEtCSajA3wk5Xnbqlh1QylYQyiUXegjsODKG2k9Zg0xZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkByv7717Sx2EJ4bwhg1CP7MdwLDjl178IM9TM_vUq9x-BNNx8J4qlIEFUgb1v4aquCjYzBHlrREqBb7o2xsmLA5Pzcso055_6qZnfEWv19ihHCnlb0m73oYajdnY59500whDFwd-h-fDpgdGvuXuwkda5cJ1saylXIyqtTg_GITog5muuG6TkNye8iDPE-xQQGLNyAZ5Ee_raC1kXL1jzmmxgFukmU9JNje2YydUQsMT7W0t9Ajnu8zqtzt8wXosdOtb8TdU8bwoSh8mMZsC2RKzpXnJ7KtChHnuXhZoasVKLJOs__npwp9Ky8-pMHBJ3fYFI1iwxz35mGyIz9_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emyCwNWzw6HHnJGP28jW9VESEKnxFHiKKHwUT16JQ7k-iC7k_O5DyCKSILZzgJKAc0t4bKGW3tV14ykbFZxBqDNoAouO_hpShXPANlAkdnijjVubSpXNd7vzHVyvKb9fcvpIP-E3TKa35iVDFE2qJm6uD-4yXXnE3LR6Z1yf72m57orK5swAKP03Y87u_N1_ydCSPeqdaCqaMoFv1ZqSXMnpkxiNEImtL2YcmrUZHH4yCqM29oihba3ivwmyCrV25SK2kDEw6wm4tkvhhuJxh6F351nNJETD6dsX25EaZFn9hAmH5W9LZpt9cMPul9BDBLt_kG4k6srLAqt6ZjiY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVJs4JfoUvHotv5bxDLthUPdp-Y6vKrzDe2UzAU3OQ0et7UKRYw1d11i9agx1rhcquuM-rl2IAy_nU8BnFz4mw3EPecqhrDS5D_scYb0knDzf7-VfckmgPXdlKCw20xEAsc5FpBdJKf9MRzcx3dKOfPzZboyrZl9uLUbklE_dhbRehoDHNFDmNtp8CY21RiqNX3eekT5JTo5g3MkKzKMNfkYaCdDt3peb90_6Mzr54LX0nr4l-XbdrTOnhDTQLiPT6cADm3SlpQM7lWIK12fi3Zy957oo6JP3GJeyN_55hBuSz0m3aJvJMMDZzSquCLxpOmuS6IzWh2G1mOu1OXghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=JeZugDh8sH-eZZT83Sc5HyVSXCGrFZx3Zrv5SMnIR9ARQGaysmV5g2hk4ztV9PW5tyhxtWwqjhQNaHIpQqZUwziyX9t7WcQUfDFOOO2pd2-yyB4Hn1R_yH33SUMwW8rERLCZmvjjSt_mGI6wNCO-NK8kQHJ5PfglLLlGRavfOuEY0iIpPEgxSU19BFgZ9hzLZ9W7MS4-wHReolOhx4sEkvhnIdKnJFtXSZUBktWt2DcgFhtXYoG1gEqHue2JUaXggN4NllhMLVKPzTnbmaTelcAuTJqoiMF1V6_asSMcysnEGRue8m9K2C7W8bkAdg3ftbmCi9ghaQEsnW76UEHDXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=JeZugDh8sH-eZZT83Sc5HyVSXCGrFZx3Zrv5SMnIR9ARQGaysmV5g2hk4ztV9PW5tyhxtWwqjhQNaHIpQqZUwziyX9t7WcQUfDFOOO2pd2-yyB4Hn1R_yH33SUMwW8rERLCZmvjjSt_mGI6wNCO-NK8kQHJ5PfglLLlGRavfOuEY0iIpPEgxSU19BFgZ9hzLZ9W7MS4-wHReolOhx4sEkvhnIdKnJFtXSZUBktWt2DcgFhtXYoG1gEqHue2JUaXggN4NllhMLVKPzTnbmaTelcAuTJqoiMF1V6_asSMcysnEGRue8m9K2C7W8bkAdg3ftbmCi9ghaQEsnW76UEHDXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsfkyUpnTidbZWDPugsqdFes2yxKfrsjrsg-QMkQ9LFZ96KeXQid02cUx1CQEYpf-fWUjbADDRIrSHkdhmJmke220eYK5PxB-R_JjHRY5JHBEwAsJz8WtprPs5Vmp3Dev--QIXfhKC4lQj765n4I0mf6iiFTGG9TGvMtujYv4dWqpp43SAci2zUQY_GuzOGBOpgb4QyMBQSu-e81Osluqww-tWiST6LuLUHDNEUQuyYhqNbjlAaPBOxg5fXNbKdG5kmMZpbwbUtogi_8EMjMHtMwqDU-iNS_fNPjG6ASRZEgE8LmcQecM0qmClJAP933Fu0Jcu0MPPhErVX2omnOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyTgi8oEnOINm-aHQMMZTQGrnP0szDmrQjiav0n0TI-PJ6IfxgHIkSd_t4rAV9EvBeNhiYf748AAlMjUL5WfjmC98LH4H60S2JAm0dcoNTUi1DV1VxDrz3Ywt-Rmgaqa8rBfACdy0HPa3RAY39YSo13Zkvyfs79II38IGw6wpqxabOVDWTZpeWy9BYCEurMM7DLwvA9HYHi0la2NIK666m8u0ql4GQJEP9f_wTA28bKspe7HhJH5zv_6H5UEiq7l-lKACUVh2aHy1K5fB5Eo-igKeTtJS2tQUznMwHyLqSyruo2x4eNg7MV-VEsdqvA9VNBHCZSaKo_yYiGh6tGzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKa1oXV9UeV5ueSbJDLo0ji0JjJBSfOznrDnq_zgWyi3vvy0gpQ9YmCV6J6XLaJ05XAz2NHaxTIDypxE6-UPrw-LvGGpazufrFZAEQOcmfh_tDMp31slgIkqOpLXPzZ5hl9oSbUMPe-ce2AXpZHxzqmmvSCacN7ub0idn7NgWJgDjLpiR1ZcBbjnOUdqN0UTUjQp1uEDPB46ATvvNE47S7DNZdKg6iC94LkjRkQNkkzaQyHp4NX8WhnrYHMPUEZ-m3F11j3AH5NJw4b1x32vm6XdzkqP-aQty-vzqDDUSdmp3bLAWa1Lpp31WIu-ul24QnqnS9UE-conV8N5nnLOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7fEbj7rSeapFzgDNVhM-Mrsxh28j1xwTkbY4NRxoL4UQxw4QwAqyycyYlq8Wa-CTd-WwnUzgoCLkCRGuteZup7WIJDGqsV77ZS0D91JwK4SNEPMFINNVlErHHAzEWQVh3OY7PqxNKLYFSJcOwvgUYphpT2U3A31HM4i6EZXaUCRGApQeT0Ggm1e7fgq4s1sE-lDkKJxFc24qoPpxN2PFsRgl53qHJpwG_MT13y2Mcc7uzMuS9Midqz-5StmARu-M8eB3VJqV5Ou5qER2t0mtLfufnUAwKgxhZJyy2GVVnKlnyFxeLjD9G7QwXq5nas5QbKz2OVZ32YA5JVZhaLoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHudr3Fkqh2sq9HLc9-71-pRKI8Nv2B4Ma5T8iirc1Anr0p7x7SVwokou4pAHeGHUYMj6RKB9Zhq-qvad8_RjZivQhCalHUc3mIadFHPT2tk51wX1vJ4iDKTA2-h-oULpvC7UtR3XXl8iN55Ib4TjIcLFZa502mMar0lRllwjgVydnO0VZ7xD_5GjsO32kQ5LniqME56Ow5_T-Pwk_pmGZ9caZZTvXqJ0Nur2Yccj6ZMwq95QGH6N8qtfCdpdhVqoEneEHGDw-a8lRWGfblY-U9l9YkjBF2fCSj3rTKvfB2eAVvvrFqWEGYhi-yKY9lXI64EJ0cSgBev1VXjcxO8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=SYzmvVN3S_8XL0uZ--RFskCzTmuiX1kbRQv16yKQs8seHk8_pCSjYcVbZRu8D-PLPOM1vUWmBDun1tb8_w656Jyzs41BNBb9OuBn77_lHgAyBGjWWGCsNvRVj3MS8wJfzyFUsQGWiSkd6Dxrvj-koO5qlCiRJQthmLZ_hzRe69CsItBlJUxnF5T4alqYHwPA5TCkF7PcfsefZV3sQIG3_KMaOhJkceI2KIVcL3Um16Lvs_8fxsBKlqBncXTk5qlFX4KKWoSdR2wvFay6SyqyCaoyfF_2D8mQLHJ8Ltkpefxejov3bVolJeAOKRV8BqaEIO1U9qZu2O0UqbpLJDs9wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=SYzmvVN3S_8XL0uZ--RFskCzTmuiX1kbRQv16yKQs8seHk8_pCSjYcVbZRu8D-PLPOM1vUWmBDun1tb8_w656Jyzs41BNBb9OuBn77_lHgAyBGjWWGCsNvRVj3MS8wJfzyFUsQGWiSkd6Dxrvj-koO5qlCiRJQthmLZ_hzRe69CsItBlJUxnF5T4alqYHwPA5TCkF7PcfsefZV3sQIG3_KMaOhJkceI2KIVcL3Um16Lvs_8fxsBKlqBncXTk5qlFX4KKWoSdR2wvFay6SyqyCaoyfF_2D8mQLHJ8Ltkpefxejov3bVolJeAOKRV8BqaEIO1U9qZu2O0UqbpLJDs9wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Vg5EM_1QVAtLOp9MVvwT3Vv9MRPSx1E13GsMP3VAuhu4KPLZ9MWf-26pwT6Q4idWCZjX8CvBA2auNkkFeXyYQ7iJPiiT1yXovpuXNKDGdQzFCDeoR62xfFNQzJg0lUiIl-9R6jTCRew7BQLXvB1M4v2yZpsAF62wFTdEnbQXCwfNJwKd_JvzbLJq3zztFn6PrmOdEczhdzprOpsbnIoQKLUCoQESexrzYM2pKCFtW4KsAaOwHN1jdlJdgseZrgS5gQ52suBY79u4jpOg9MWl-phjIVLzydulGFvZy62zZfNs8LaSWDzb4G4GEBUuBEfj5oHKV68idZ3PS8FhbGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuhztytcPBDmM3EnZZFZMLvCoHuvbsFySI6ZPEj3S_LOvOhc_SH3Y-yA0MmhceiHBubAQ3R1OsApH3n6FeGxYOiPo7gameGigrGg-NyhEC6lSemfK2N4TfUK0pKq4dY0CYKuQ3YRxOcipUV_LiboseYQFxYMX3cUOuNVaq5yivUDg4ilS0-oL-J104B8JfZ2wt7sNVhhHfvQvNe9gDO7CnPe6uqtYvycPMfh2ovC03yZinsUiT0LgNfCzEfHLelt4j66-uotImgk1QCk2hzFBRDIlzg5bZ3xnmHO2Jb9txZ2Llr3BgEWCLgYATc-T-fykPUEgrrfIq4DaXJlh_22vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=Vv46lyeqrqEY4ZhUChEmvWHslyJ0pJpptds3tY5qH9qwLACzonwsRXQ0JpRoXZS1Vdw5GVBm2w21J3sa57lFZJ092g5ITVqDmxmRNFCXJZh072wUSwX-Xt3RM3AvcCM8WaqHW9SxC2bgM77L9imLJF-vgJ7YkL4pKvadSecp8cqoxqFtkuIk-vcxHbjXBRImRaqZt-WdGzYg2-qq4Jeb_G0-k5FP8g3BTN0TwTIRZzTWSFLF1KdbuvCn0zxOw_NLggsFv15gWMaXLwXtb91ld6VctckIgWslZ9WC5JuuFjY7LTojeSQAPt4lxccoUeFZps2FUR6O3arZFND2beLYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=Vv46lyeqrqEY4ZhUChEmvWHslyJ0pJpptds3tY5qH9qwLACzonwsRXQ0JpRoXZS1Vdw5GVBm2w21J3sa57lFZJ092g5ITVqDmxmRNFCXJZh072wUSwX-Xt3RM3AvcCM8WaqHW9SxC2bgM77L9imLJF-vgJ7YkL4pKvadSecp8cqoxqFtkuIk-vcxHbjXBRImRaqZt-WdGzYg2-qq4Jeb_G0-k5FP8g3BTN0TwTIRZzTWSFLF1KdbuvCn0zxOw_NLggsFv15gWMaXLwXtb91ld6VctckIgWslZ9WC5JuuFjY7LTojeSQAPt4lxccoUeFZps2FUR6O3arZFND2beLYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=toLlHe82vL798bIEVjiVQgD2vG21gXefKvCYlyaxlg0d-aU4mxCEA7ESw1HZRbug2NnC3-Zx6GJYEBSTeffEfnlgpPsnOhzZNzd1VKDQjdUnOXjbK3XYXUuhwQV60Sv8t1r4T6LTvlKyMBICEceBADlFAbsafUQV6ZxH-dn_6bih1o6Bndlqya2igZrdJct1xJSpnhO2jEFQ8Vwrm-89S51Byhq0K4XTystkm29Yo-4HgS4Cj7pPQd_a5MnUGCjOi3gV69PJfAblz0Tzb1BzDwxKUl4WAIa3SzrnEwmNv0Qy99vZMU9-OfuG1vCNga8Nh21k0UM-xi5rSHKa3jIj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=toLlHe82vL798bIEVjiVQgD2vG21gXefKvCYlyaxlg0d-aU4mxCEA7ESw1HZRbug2NnC3-Zx6GJYEBSTeffEfnlgpPsnOhzZNzd1VKDQjdUnOXjbK3XYXUuhwQV60Sv8t1r4T6LTvlKyMBICEceBADlFAbsafUQV6ZxH-dn_6bih1o6Bndlqya2igZrdJct1xJSpnhO2jEFQ8Vwrm-89S51Byhq0K4XTystkm29Yo-4HgS4Cj7pPQd_a5MnUGCjOi3gV69PJfAblz0Tzb1BzDwxKUl4WAIa3SzrnEwmNv0Qy99vZMU9-OfuG1vCNga8Nh21k0UM-xi5rSHKa3jIj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6eAY7dCa0HBiNVVo3FLkI132h476Iggr5YCumzerFHTmKhAigCtbitkoPIZYktM9XV61yjzO_nMqEOLAkzbq5UlHNaMwqxweQ3URg1NYp73jNl_TTtbobD3ep8Vdyqw6j5984kIrUgkPHN0s70XON1tvioOoWDuFOTSSzghbZuSsXycrqGFw77GtgkGDqNd7EayyjU9glzkE6fNS5xZYYryrXX21GvERV4IubIihNLGsPTNgonQhODAXWnYafu6LwTFQe9IwXWpENUWA-DTVN6L1YK_yBt9VUY4sxi-J4wEF4BboF3j-5_0UFV3HYKi18Q06AayUs7pSCqHZRC3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cv7zLzJTXtQ8RIsp-dBuPmDW2WCGjyC3cznQlnDuS4bEgxAvSlhGjdKxi7kZC1WhsD68pg8a6h1lHP_ypHrZFxfV1ZC9IGsISa1sniLQwhrD2S0udvwo1ieNMIkumVv4ClmPakF2psL7uBk7HVkMowfEkpvCpO-mss8564SuGZqMlodH316CWz2NDUwnjeKP13auuZFgOo1aDQUBVOC_uwtSGHPTk508u3J38J81wiK6x1vN6nOJbddzpnZZ_806U-DJ2badfP3CvKUmTiKb4kmk4GE1lpzEQJDWZvaYLPDu_8Pzbr3zqbRTHdxJj1cLOQbSFWYlLHKULcVFXsrwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QosPOhOcoGa0QVPf0XEBwAEWdpuQ_LTPtFtOVxV9J8AHAubitX4fDIdhvSNCfN4bQXkANVDf8nc0sfZ0cjNFA01YQ1ffT_VBsNa3KTEZm0bHcpHKFp1v0DN6ZY61zwTr4oHiO0NXvhx1-E2JCy6Z8wOhQNU6dEdBB_HVQq3drlyPYGXaM2i8_8DuUEwOGWOsaqjkxR0NkxyFmbmzLJIlpNNuq2eo1UwqrDf1z99waMHRHqWhCu3ZOd5WnHFMzN-rMbXSUkMntnSuX35FeWf8PH03kuo1HCbvG76CdtaEeQzapoJgj2_6lUS5f1eb0k7NZcbC9uFzRG6aWd9Rsp1-Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8iM3GIJXoGNUa-Rb4w_-kcLSinvY0I2aH4HcLeKVPRGqsYL12WQqrcGE_Nnq_OPCjHqgtX0RU5zZ2oiKAdJ-7ktGUSyO9BufkfYt-_baPesaSVCtHwtBwTucZRpQv5A_9uojnJCi4un8vPEiLtvoLhC9WsUsu9y0_BaxjT9i3YQgIT-f7mqBURuQMh19SfORnHX4B9cOzq4xdzFQhsX2laf0QYFr6GRKMZEUhyamC9w-hT1p6dbKvdV11Z8TXzp0E4EZlWmEDHxPSZA6fE58w2CFFHMVdoRwIHCMPevc5lCKdWMX4_1lk57MBdIDEUiE6ewli-C84hU1KVOKtqZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWMnMRIozzHMz9i8woUbFDltCUn1VHI9fzt7HfXv-G8XssKohuFnHzavmUzFurczJwiWfxAuNf0gLlHWX7Ho1eMNjFwHNopzp3KeWy2fsF4VYBA4tyf3_Evndq-uTqw1i_xpw8WAc-KEkhFtYmazg_cbgeL8s1RJrzWm2xySb1U5SDi_UnH0pW1SkJe--2XJ0YdSzRTU7bjlY6Cx3lwzorQJDvKllGSFz_OblDZ2DSsVVKBT8lOCmgLXqnjP5T6IiRdG6fm2sBDKuxqFFWnKjuhn7R8CSDYl7GE7A6SsK6g3uZZQlsYovCy8zoDvJJHyOPT0bP-7LOZe9gPUfPVVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=NFL8_fb0TK97fMueVH96Mc2FPXStQSi85jr8OKjFKyBl2abtDMbyooBmOreL8282JhPjZT853AmkWuLiU7NPSyaClStvzo7qryNyl8CDOt0aWMNHJuJGM1w10hO4UB0g_EyE8Zw55RiwS-sZJCmh9FainICYRo5DzE2m8JyM2yJYWvGSsJH-lXf_xsBVePfs4dO5z8AqgwtYHhWZZA4q4ek6-i1yG9f5HSD8j5uO9UvZ2tsOdiVZTub6pOtLSye8LZhSSZY1t0nbt7Q2pW98-oT6aGDbBFtqEMgtePQ5ty3yhSZ-JJsSkL4a0ZtbavBAsAJzBwy4CLgdaTEHuccfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=NFL8_fb0TK97fMueVH96Mc2FPXStQSi85jr8OKjFKyBl2abtDMbyooBmOreL8282JhPjZT853AmkWuLiU7NPSyaClStvzo7qryNyl8CDOt0aWMNHJuJGM1w10hO4UB0g_EyE8Zw55RiwS-sZJCmh9FainICYRo5DzE2m8JyM2yJYWvGSsJH-lXf_xsBVePfs4dO5z8AqgwtYHhWZZA4q4ek6-i1yG9f5HSD8j5uO9UvZ2tsOdiVZTub6pOtLSye8LZhSSZY1t0nbt7Q2pW98-oT6aGDbBFtqEMgtePQ5ty3yhSZ-JJsSkL4a0ZtbavBAsAJzBwy4CLgdaTEHuccfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
