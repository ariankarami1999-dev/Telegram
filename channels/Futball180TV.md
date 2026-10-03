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
<img src="https://cdn5.telesco.pe/file/s_4NxRMfBBVDCCKRNPKIRT2Jss9VcKfcbnKChn_DvLTOfega6QPjOA5tatf_y33h0kemTvJMQeACEoAXay5vMAK_N9fLHjC1BEpokfHb0E9uAy6MVOmaewUltSdWed2TrIVbs-Zamjgtw1WLIwMtGwUE6kDeYBkK7abf48CopMHwdUR-b8VCdsQAGNHrGaspOyd64i6PupnrgELPtystIAVdqLkOSWh4CtAhPDwWddduW7-SwCbXaB5-Nd8osSlC07mVsCG-NhmsbqNDCMO0zCGpFzn0Q6E5oi0fTMPjN5tlzIL9ObihCsCypsBfRaV3WJmoioG97Uk7SKWdSl0QAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 393K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isQPH-Id727fmrJcJyBQSxwg8ckipGb1uxk7QfLPaMd8ka8pBWfJ68OExDfFKUtZK7uv4Dxd3jlI_2aHG41Lah6cKsvYsfdcTiFwJagOWEAUoe66qDAkBerDex6Xvy1vsSf8VtveTUyaGs-7zAQajUBEG1EsIjD22bJMvEr9jsKb-wVqDSk1o2ClF5Bid2UqHApqEkINPtjEylc9uDQ1rFyAxAJcqwkVQOHPi_wa67m7IyZ7x_o4aZuZV7cMS62v49rnifZZTIB-vlxAw4kgS-lxu8MeWXIyZf2EXg8eXTT-Md6gJe4aezm7fXU7dupZHL6YTzsbLEcAxb-NdxG37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=Bmyp3IH6A7iUTY-Uw8qg1VOIJAtWZ3TlPYjsvBvn-E9RALLE6iV50ZZepJ_iCNHk73IVY7CvAp92H5btXfkPii-KVPhX9akF3HPE28kGuw1cRlpxNKD965lVrT61jSdXIqhreD4fM0mphuUGTN-vApjEKbPkZHbRwYMgoe0FO50Q3NpCM-NwpAsPXAUSlNEhxR3uZXH0_qRqyYfy21C1IHEurTd5X4WdUl8Y97iZi5CoFQLdd5qBaolMu4mOnQn5NKA58oN0UAwktj0thRBVstHqRC2tVH02I3YOvBboo3LCpPVWtxfHlg-1vbnaiyhPH1W_A_Mjr4j7vE-ItntsLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=Bmyp3IH6A7iUTY-Uw8qg1VOIJAtWZ3TlPYjsvBvn-E9RALLE6iV50ZZepJ_iCNHk73IVY7CvAp92H5btXfkPii-KVPhX9akF3HPE28kGuw1cRlpxNKD965lVrT61jSdXIqhreD4fM0mphuUGTN-vApjEKbPkZHbRwYMgoe0FO50Q3NpCM-NwpAsPXAUSlNEhxR3uZXH0_qRqyYfy21C1IHEurTd5X4WdUl8Y97iZi5CoFQLdd5qBaolMu4mOnQn5NKA58oN0UAwktj0thRBVstHqRC2tVH02I3YOvBboo3LCpPVWtxfHlg-1vbnaiyhPH1W_A_Mjr4j7vE-ItntsLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1I-D5yIZ0VYU3RZg8whvpipAkemamzrUCeSU04viw9iiywIkMXfDLPk8KQ7lw6NEoMwrhj5QolzJTVBbIEBfs_PspdDZV-jXlXUWZHYIKLapnuC8QQAKtUj9Yqu7YhQLk-1rv9TkKJpLH79yIQRGe17n5rE6nKeEyzca9UShiRoqCKbwM8huPoi85F92qepIGQv02sGEThwKYWu-WkUyZ3hcfybnuUqJF-kSaFAzqVStFgtyYB4TGrtP4kpwaG6NP1O2vkbRymGs0lI9LoF2TKkRaWkOgIpD2QGpS9sFccz2Ax4uHWl9wxAK-QWqxuzS0MIbHiDr0OhMlbijeLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc8cRPXD8vsV3f9-IrstFqcWlEWMiTCMUSpZuw-ToL7NfbTLx1lPHS3rNegw0AN2fPTwqWwjbZTsPrHmCpL_7tiFFrtcm9AtNSAp80D8CncJan5yjVTzGEbUD-ERQXfH3Bve26XDUqRJcqewk9VFbAR5Ll4iXOedy5st4F5m3RcI3oTcakW3fMY3-OiZpDkcuY5OjvNpCJrH0mjVbaAW-BVf8AWA2Sy0YTqh1wjD86EWoVGJWPLv4hPEs-dLowSKxMR8ZxjG-TfdG5MI8RUi4Yx0qZThpjKSh1JqaOViJiVzFj1bh12hJzDkBoEvYjraTBXs0ysI2v-Fv2EC3FiV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107734">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/107734" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107733">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6FLNldS-KgCaXRWgOxluArANTbFmBadjYmxRHU5ioCQkzjfvK8n2QmMWcvl0rKUHOElazl8bZJdx6pHkbhkA1PLchF7Oev6IIxNPNuWnr8LCBSwz5LSrgzHWF5jJGU6yLzWXB1HiJgnmEbaFpwd0cAbsyjx5BlNU7ELcvGVsHZnsEywKTV_TcWn48m4IfsAxEQeCZe0YTRe2rC50mWLkpgoUtKq7P4-oLyayyKPzFKQmCtSk5Uwfo42ikb8whFsr5wjPiPtxZRofKUPePmyeNjiWtE9NuI90DJ-XRIeBcBxjVqDK4PeyZW00RabjkKZKvfla6FezLlyVzKNHF8yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/107733" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=gpzp-AShVAvso6JbHfBE-avOY9_KHD0MsfXEYUvULkiN7ZBXVTxpKSkeDXGLltSPbNDWayVyauJKaSBOqDTP4EP9nHzeoagEpJbCQuoMGuM6ffshqhuyJtYorG674SlBAt9-n8BVIcumnq7OC_VgLsFIin_q1WYL2XsA1iPNtbnRANjpDybyRwH479vIvMFnIF6IR2zwSnmv7DrSiRqYy_Ains1NTaH3ZchSmmRB1Wrm6nSqg1ZmCamPLk5jWoaYwyu3H7naiByK43AKfx6uuIhKkMgx_qf_l5A7XmQSv0n2lz8debDZWlyGbF72b-ZYNYMZVWG0rPnYTJCdZYek5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=gpzp-AShVAvso6JbHfBE-avOY9_KHD0MsfXEYUvULkiN7ZBXVTxpKSkeDXGLltSPbNDWayVyauJKaSBOqDTP4EP9nHzeoagEpJbCQuoMGuM6ffshqhuyJtYorG674SlBAt9-n8BVIcumnq7OC_VgLsFIin_q1WYL2XsA1iPNtbnRANjpDybyRwH479vIvMFnIF6IR2zwSnmv7DrSiRqYy_Ains1NTaH3ZchSmmRB1Wrm6nSqg1ZmCamPLk5jWoaYwyu3H7naiByK43AKfx6uuIhKkMgx_qf_l5A7XmQSv0n2lz8debDZWlyGbF72b-ZYNYMZVWG0rPnYTJCdZYek5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc5xLGadiUK1uUL-6PDlYH4YBFurjXrBEt4vb4Bmbegj7a2SdDuWkg1Ziwqcu4id4Itk6dEi0d_Oq4miJh881xwekwYYO-shwEo_C4UQ8Y1nA-v6QtsfKH-uSgOdvg63J3JBsoCn4NUdPqWaE5-VmMVPY_0EuhtYRrBGg-w1aRIHdPB4fl9Pf933ZL05ECy2x6wZXKYAs0S6TkVzhh1gUI48RUSU2o0cRq6xLZcPx_n2BN7WLJnImtAsyM087j900Dn8w5YEQUAreLNzarJvOISmziJn1ryy24YfliIARHGwOxUAgpRTXptYTFOBojs2gxhu7lFQKcQBp2QngrqdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=Af9e2naN4SY2kx_h5bI-FjVTo62emdrOaN7Ikjtc8rLGYOogXejL3CzvTjh3qXNs3Zn-a8-yPecpcc-Dd2HHgD48ElwIZ7ANRfigs8N3zDpjY4fCT0s1HdYBl1pLx9cL9ZTQ--05J_Cg3zT8tyxUy7jMXcCCcA_dJhhKzFu5jHyTU_CF7bLaIO5FP5zliZRV63_YqKNxacSeIqdX4fqnYN53ZQXTCoTzD6sWZdWJUjxSYi4ksUb1GYjwF4VX8xmuSZb5kcaQGlPTXhDH3pDLkYQgBSQ9MiY8Yu0kF3hf99xF54hEN3Intq5Mg02y1LoWhKN3CHP1aShc0WxHRShkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=Af9e2naN4SY2kx_h5bI-FjVTo62emdrOaN7Ikjtc8rLGYOogXejL3CzvTjh3qXNs3Zn-a8-yPecpcc-Dd2HHgD48ElwIZ7ANRfigs8N3zDpjY4fCT0s1HdYBl1pLx9cL9ZTQ--05J_Cg3zT8tyxUy7jMXcCCcA_dJhhKzFu5jHyTU_CF7bLaIO5FP5zliZRV63_YqKNxacSeIqdX4fqnYN53ZQXTCoTzD6sWZdWJUjxSYi4ksUb1GYjwF4VX8xmuSZb5kcaQGlPTXhDH3pDLkYQgBSQ9MiY8Yu0kF3hf99xF54hEN3Intq5Mg02y1LoWhKN3CHP1aShc0WxHRShkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107724">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107724" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107724" target="_blank">📅 00:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107723">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPOjzmm7EUtb6ylYEXqHwKTGMuklSoPC1qVpxUwVcGxsSZZfxkAMJzSyrBgJMuIC3Sa5ypzSD68Vuoi1pJS0p56LYKEUriQjOY9H8fCHjUJvDXW6XANXnwO0tkthQNFWu9pOZF6mxmoE7DRzsmSSI_V3aDxmbjzlAoz1fgrDtbCdAa4GYB_7NtD1uOwz2JlPeljT9xMlH7H8zLLw5H4bggYMabKm1fdYfbQ6wUJMBhcXuUOioLMz5KT-dpY_DnVQMuTA1jLI1bTS9HE1atMNobC4-9MMUv6m1B164vbeg4yf_DPOLjdsuFk5vsBy7Rc1mdE0L3ASPBYfwnOycF0rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107723" target="_blank">📅 00:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107722">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنجره زمستانی انتقال حسین نژاد را نهایی کنند.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107722" target="_blank">📅 00:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvKBn_NQq1Q9-3z8bXNHJWRRDI12Ci1oTv1ZPMdLxKhbxbM2bZGAvB6edv5Al-WRLDz9fHCexX21_frUXU3fhQQltS-JyUq36SjCi8IwCMEgGsq8cf6dtyPsCKWISCmee_di7SiIzdESrom-RCSaq_ZzPcvZE0_fTRiYRtWAeR9EeivwhtCU9I5iou5hjfrlAYtD2yGOhHxq6UC_6-U-0peaaiMK3mMP89tXyLPx3TxczVf03UJS1LEguGir7MkJVr0Od_DTO2nOb9HMjRnh1xdDWnWJQFL6DNrC4PbCfnOwbcRRBBIck4oWPrx2KrN_w7ua2MEXJrfWqAhhZzGX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=k2zNmqP7KDOCslNFvoQor9joDZNXBchO5Rj_PE9O4jv14VdIkooVMvpu5ptCVkfwoiczYttv-bZG5wt4dY_3ElBGdKPE1Hv_J9u4vUqJyBmV4D3NtjkwUKkGi-sSFux2oRS02h8Oq5tumLfQcOzMWvqmFGYY8B-ymHdFS0pV-TPC12zSsJV0hQ-4fkWXs0Or0G3VvWQVAhrPXDi5PoES7S280Nk7mN7jU7TW7u_MMIEXs0ekThx8kYRLWjvmV8EGGV4zEKJmp-kePUYZNrdvy_IVjAVWa14PlxEOSve0Eu1bUpxlKu06FtQ7OphQGJKSs8O3SPP89uar38M4kzN4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=k2zNmqP7KDOCslNFvoQor9joDZNXBchO5Rj_PE9O4jv14VdIkooVMvpu5ptCVkfwoiczYttv-bZG5wt4dY_3ElBGdKPE1Hv_J9u4vUqJyBmV4D3NtjkwUKkGi-sSFux2oRS02h8Oq5tumLfQcOzMWvqmFGYY8B-ymHdFS0pV-TPC12zSsJV0hQ-4fkWXs0Or0G3VvWQVAhrPXDi5PoES7S280Nk7mN7jU7TW7u_MMIEXs0ekThx8kYRLWjvmV8EGGV4zEKJmp-kePUYZNrdvy_IVjAVWa14PlxEOSve0Eu1bUpxlKu06FtQ7OphQGJKSs8O3SPP89uar38M4kzN4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇧🇪
گل‌سوم بلژیک به ترکیه توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107717" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=riVFj6oSrkWh3v-8PSRcaY5P_7urF7RsP7IIBgfAM5Hw4tje8QCUQ9p40Pmf_drYZGVgEtvlCCKqkBAGfxhBfBMhHofh_d-XdxKJbBhwUu-XJP7lLrVN0cCddIbE_c5ddzBvoSVj5sF74xoblj-0zdvGnDBIpmyrwFXnyGPFHv2GAbiok5xOu1ypvPRfjTDgbnhbUzGQJEBdksNvrLfcGMCQ1Ltb4lH3BggBCoAcPMxAxjN-M1FC5TvGp18jQOWo3E1lq-GcO3EuJhcGqWzuAcoTmvZROOv9JwjFS9IhhsVVfMxgwLHqutJpSWqcuidPI6wPqX0HXSCJby8sKMhcTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=riVFj6oSrkWh3v-8PSRcaY5P_7urF7RsP7IIBgfAM5Hw4tje8QCUQ9p40Pmf_drYZGVgEtvlCCKqkBAGfxhBfBMhHofh_d-XdxKJbBhwUu-XJP7lLrVN0cCddIbE_c5ddzBvoSVj5sF74xoblj-0zdvGnDBIpmyrwFXnyGPFHv2GAbiok5xOu1ypvPRfjTDgbnhbUzGQJEBdksNvrLfcGMCQ1Ltb4lH3BggBCoAcPMxAxjN-M1FC5TvGp18jQOWo3E1lq-GcO3EuJhcGqWzuAcoTmvZROOv9JwjFS9IhhsVVfMxgwLHqutJpSWqcuidPI6wPqX0HXSCJby8sKMhcTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول ایتالیا به فرانسه توسط باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107716" target="_blank">📅 23:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=oyBsf8njn0nKzMVgLrx9T_M8UGUgicXhcc9vxgPlipDEg-eZPt-eivHpfKxPCCyYNm4oL6goxBt67WX7hY0pRnat0xWRjhxPvXQUpcxpk_LuPKjvqyd69RxJmbdREInFLScyR2GU1SNjcVrvnZtX-vowNRi1LM5z2s-qyPOUKz7h3smZyjNS-l77dqgjNSNAhQ0NV709ck5N438BIGVJ4pbGATy9eCe02Ra1vic4eAlzDuFi-zscq0Ohu2jPNh39zXygJtOc_xcLUQTsRS7YhtCs6le_TvQD5gA1EjtGJUff8EXmOz6UPyCUrU6hWo448vQFyUUpHsdy4UUfntpXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=oyBsf8njn0nKzMVgLrx9T_M8UGUgicXhcc9vxgPlipDEg-eZPt-eivHpfKxPCCyYNm4oL6goxBt67WX7hY0pRnat0xWRjhxPvXQUpcxpk_LuPKjvqyd69RxJmbdREInFLScyR2GU1SNjcVrvnZtX-vowNRi1LM5z2s-qyPOUKz7h3smZyjNS-l77dqgjNSNAhQ0NV709ck5N438BIGVJ4pbGATy9eCe02Ra1vic4eAlzDuFi-zscq0Ohu2jPNh39zXygJtOc_xcLUQTsRS7YhtCs6le_TvQD5gA1EjtGJUff8EXmOz6UPyCUrU6hWo448vQFyUUpHsdy4UUfntpXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
گل‌تماشایی کوین دیبروینه مقابل ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107715" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگلگلگلگلگلگ دوم بلژیک به ترکیهههههه دیبروینهههه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107714" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=rsUToci10qiHfj6Y5LUvK0zqTsrBQQCvU4NM8Zjlmrg6KV8VwtRUxHm9iNh3Ce53_DwenlOetpH_YW15en39aXKxULmgL-Eej1llzjRSJ_WNRLgcSdli9QnQXIRKIrveq-xUd0skwDjFa2CCSV7uCkAvSp_CGV5ZDcLxidil0rqDwVjxdw6bYZ7RYU1TW14zdS2Fb0Vg2ZZjjhdBsVQeL-G9tSXy3yh1Q2VqqVg5ca1MAZF91ov6hxdK7y44ZBiWYCBr6FcGQk4lsxIJuXI90ZEqEGWap8G0JZUt4hCFK1Hs3a_O1YkUuslMqXZjuesJPYI9H_BTXHnWI88Djm0XLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=rsUToci10qiHfj6Y5LUvK0zqTsrBQQCvU4NM8Zjlmrg6KV8VwtRUxHm9iNh3Ce53_DwenlOetpH_YW15en39aXKxULmgL-Eej1llzjRSJ_WNRLgcSdli9QnQXIRKIrveq-xUd0skwDjFa2CCSV7uCkAvSp_CGV5ZDcLxidil0rqDwVjxdw6bYZ7RYU1TW14zdS2Fb0Vg2ZZjjhdBsVQeL-G9tSXy3yh1Q2VqqVg5ca1MAZF91ov6hxdK7y44ZBiWYCBr6FcGQk4lsxIJuXI90ZEqEGWap8G0JZUt4hCFK1Hs3a_O1YkUuslMqXZjuesJPYI9H_BTXHnWI88Djm0XLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🤯
سوپرگل دیدنی اولیسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107713" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=CpaGgfe5HRbnIC0O-Q7Qn8W3rXQCDlcLljLNWyW6-prxVndrX_lZ7b-GHt1x70mnyVWpDTIYT5k-CBJlFH0D3J3IIMGfmY5x_uVDPrIDfTvXBM1Z9UN4EBX7zPmGWFczRubS4Y-vJFNvsL1CZFM1mrQCTn-HYQjBDDd99qx3EQuVlcT8fznNfUFP-hT_cG28FWp70ZbliTPVVhOHn9mDOkJrbCOXdTySBLKYht2keTzpZdqQasMvmx7EtJMZ2_0oAGhiI1l2-QhFkdUun61JZgod3IpGo6bzpIiD_6VhFLPGzVhPUNvsn5gsltXjRlQKVUWWrWe5Y20QLrNDWx5zIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=CpaGgfe5HRbnIC0O-Q7Qn8W3rXQCDlcLljLNWyW6-prxVndrX_lZ7b-GHt1x70mnyVWpDTIYT5k-CBJlFH0D3J3IIMGfmY5x_uVDPrIDfTvXBM1Z9UN4EBX7zPmGWFczRubS4Y-vJFNvsL1CZFM1mrQCTn-HYQjBDDd99qx3EQuVlcT8fznNfUFP-hT_cG28FWp70ZbliTPVVhOHn9mDOkJrbCOXdTySBLKYht2keTzpZdqQasMvmx7EtJMZ2_0oAGhiI1l2-QhFkdUun61JZgod3IpGo6bzpIiD_6VhFLPGzVhPUNvsn5gsltXjRlQKVUWWrWe5Y20QLrNDWx5zIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=EVRLc4pYg4QhRW4nzaIZ-Z0ncs5jP4-cyfc3AFum2_gmPc1nN117M6cL4EiIrnYNjymfM1aFT-x6krZydZ1cPREdjnVr7_PM2zGjcDr-b2G014LaV5H3FroUU6bfFnkrqr5mKCJiGT5ivtaI9K_L6iCAEBINHaGRw7sxYoRwd95hQ78jG91Nb-isLdszrQiIfaxs3dqkg2TC1kNreHQ2YgqCH-Gskp3zBGlCtgYSCOfO5iYeylFAkDujhdZiXv_7xPJqsdfCxykX5MdF5T4JK2-szBetXhgb1BVdOGFl1cmj4JEVTDwTMGsqq6aVkty6niPAESNOqJ96_DxkJK_0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=EVRLc4pYg4QhRW4nzaIZ-Z0ncs5jP4-cyfc3AFum2_gmPc1nN117M6cL4EiIrnYNjymfM1aFT-x6krZydZ1cPREdjnVr7_PM2zGjcDr-b2G014LaV5H3FroUU6bfFnkrqr5mKCJiGT5ivtaI9K_L6iCAEBINHaGRw7sxYoRwd95hQ78jG91Nb-isLdszrQiIfaxs3dqkg2TC1kNreHQ2YgqCH-Gskp3zBGlCtgYSCOfO5iYeylFAkDujhdZiXv_7xPJqsdfCxykX5MdF5T4JK2-szBetXhgb1BVdOGFl1cmj4JEVTDwTMGsqq6aVkty6niPAESNOqJ96_DxkJK_0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=p2MBKBWFtGJr4rKGgpIbDU3W00ux80D3mMGdvA-CRXoO68TSsv2IrLsTz941pYjEFs2sGsEllpNve8O8WlvgE93j3dAnzApFHy8bFz_0cuHv9isWN2W63BcT1a3e4PncBDs_rRL-m1AQOvY7znPEeLcYqxJy-a4Gp8OmrtfIsoXWJ3h_cLwi5-KM4RQyhkPujDEiJjGGkdyUMWmiafFUSI2OOn1bPZOxH2A8sizXU_qaOi5WXd4kX1O4m1AIj_BO7oF3M1KfbldW93Sk7ACUjq48UvRPpmnG-mC3GX5dvuc8cGZqqI29FkUug2OuPUHxHAtyMxO4jY3ptU3z1X0gPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=p2MBKBWFtGJr4rKGgpIbDU3W00ux80D3mMGdvA-CRXoO68TSsv2IrLsTz941pYjEFs2sGsEllpNve8O8WlvgE93j3dAnzApFHy8bFz_0cuHv9isWN2W63BcT1a3e4PncBDs_rRL-m1AQOvY7znPEeLcYqxJy-a4Gp8OmrtfIsoXWJ3h_cLwi5-KM4RQyhkPujDEiJjGGkdyUMWmiafFUSI2OOn1bPZOxH2A8sizXU_qaOi5WXd4kX1O4m1AIj_BO7oF3M1KfbldW93Sk7ACUjq48UvRPpmnG-mC3GX5dvuc8cGZqqI29FkUug2OuPUHxHAtyMxO4jY3ptU3z1X0gPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=miVeijKmFQ0QfVhGpiywx5SAbteSHXz2bJSpBsMAuAYOz1ToYxDOlJ1Eg0SFon5m1XuMEDAWojeyiO0Pb7uNZ1ROfL71cDCeZB5sNDEDTpBKOLwZln_Mj5hgf_8soR4eawC0eqQatV9vCIiC9NgExEBJcjzHCnzhvJX_sieiu1OQE9SO3C0joHbohN1pnzngqgvOEzz5VCuPcYjOcSSt5B__iuF_TlEZatShcb9i3zeTyt3OXlAQfYz2EBmDB_OJ9WhrlPNxZGIr7WLgiiT5fmA0nxFKD5WBljlTJteXZd0ZqJCJKmfPlx1Ax0kzFUnkaLpMzkMf8TuuYl2Fk87SbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=miVeijKmFQ0QfVhGpiywx5SAbteSHXz2bJSpBsMAuAYOz1ToYxDOlJ1Eg0SFon5m1XuMEDAWojeyiO0Pb7uNZ1ROfL71cDCeZB5sNDEDTpBKOLwZln_Mj5hgf_8soR4eawC0eqQatV9vCIiC9NgExEBJcjzHCnzhvJX_sieiu1OQE9SO3C0joHbohN1pnzngqgvOEzz5VCuPcYjOcSSt5B__iuF_TlEZatShcb9i3zeTyt3OXlAQfYz2EBmDB_OJ9WhrlPNxZGIr7WLgiiT5fmA0nxFKD5WBljlTJteXZd0ZqJCJKmfPlx1Ax0kzFUnkaLpMzkMf8TuuYl2Fk87SbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwZRG8zF1oniTox5YS6ddBv-dAxjtG2JWFJhYFxHPdc0wJrXvxAILEQ6CVmcgb5VSjGms3rZqCOCAZSdT-jtQh1pcbEGKyiE01ggMNy-bKJma69LJRpCen-DeScFF_VgzFvYCFE9ZqCkBPnUirZp-6VAgRxui6EHKrO5hVzEI8jqUC3to3CBpSJq_7SnykM2EEwcAdtZNUaUFG6G5Hw-7r3Lk7nm3tJz7V6l572jkcCiifgneiEKF1awYrl47ZON8CINMnFXtxBlqfPy9kPDdlPaU841C-1jba-MCAGhOxGepJXhCgdISxJahbRRtn1jTNGCO9-cym4sItbDwxXpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSC3npYH2gIxI4oo7kKkLPZZm1b4gRrDSjgRW2LW7_iyld9M9GAgXna3t0umfAG3WJUGX-OcNQC5s4Pha2lXh5iMaLEbKHiojasuIfd0iX5FylTbg89Y4cUej5j6-mNFFhXAwbcL9soNBDO6JPqa8m3uRJTR3gtPWfM1Azl-mC-Dp6iDQ3zdKQw93refL1bFu1GTXTsCJHUAXL2KPKghcf1VIPmL_IyNwlfWNvFDY6h2fTUraXnCo5V2O_wlVwSPK93Z3dWarL8oj5DyinS78jj9UYyMafquSr15AFkJpUVhLtY5vLyLRL3u9rn5S_NIO0fm-jitKAZ0J3EgSph77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g66l6F_BRTfV0kWeyGLkd_YGN29Tq0JxTBG-whT3fIDboOXJOPcsAM4APGV1N8EtnG8EqGh7EZ1BnjWplrQNwH3gRwZPsXtaYAPzjT7HWlhgLHETjvaFrJaklu6AMu3c0NxARt8w2x2g28ESDsTwfYCcHzFIN_fkuhdf-tDTwkNytTOesLM7bz-TLWHMh7QPxExmM5WExAlU4bCAlN0o7S86kB4Bx8Zmm3azD5RPcpoqnnAYYhihF1fxXuHUeGeImBpPvjOhWwGzRTnfuLw_U21d8sVAmlKexG6ujErpxFNqzXj_hhPkIsRxtJAJ8fA1reEAyLIwtxc3xLjkRTPQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107703" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIIkAOZPibSGolrJoYll06VE-5m5YC4N5CHT5rZ0VFjj0aPlFv1oIJ5Y9NvZGQBhrxye6U0Gk-sbFbjETK-AHvIiq3yYpZLnmIA8a0EsfvYIW2zJbvpT64mfkLDIwQ1MGVXOJkOxUWvdIX41MzxTQJMhSXyHQByyJscmezAlkckBsQzgQuxcdTcP2FISbCwErn5vQlaLYxGc3E97w_DEBvd748F8dLx3xPLyrmIDYc5efbmA5meVzyEI9DvdoHQp_bwWpUxbqM2YhJIZOH5IjwUJb6KLjmlzTIZiBuvNYd1T88oluIDh4n1ejEUPXuVOyoycxavwCOpfMld4hnFXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
نشریه The Athletic
در فصل 2017/18، گواردیولا اولین عنوان قهرمانی لیگ را با منچسترسیتی به دست آورد.
منچسترسیتی حدود 100 میلیون پوند قوانین مالی (PSR) را نقض کرده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107702" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af474384fb.mp4?token=MsABaXiz3p82d786M6rbiFa87cW4BpTj9Tr8nvlmecZAla2Nf2Oo9-0RKavsGn7X4_DpztVKxYDRdhxfpc1p1KnBhc-s-T5vXaHfiO6GFZI0NkIprPCmFBQaaUcUpKsxzEDaN229Nav3MAepwrrVfuzyBeY5zm7lSK_G3KJ8BZnA1V0WbC1gmRxtBZ4layhWc60Zzc_lpgsFz9mxwIsHakoAAoCF1SEeqdS-EyiqIQeMDfhhF-vmb_0QWrpHJbuqjg48141MFCn5jb4I0i-_JOuf7amXnIsKowxYoR-ZMgWl6Av5W0WBXZ2x67WnB8prx5vvULFT9HBKpxXSXWl35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af474384fb.mp4?token=MsABaXiz3p82d786M6rbiFa87cW4BpTj9Tr8nvlmecZAla2Nf2Oo9-0RKavsGn7X4_DpztVKxYDRdhxfpc1p1KnBhc-s-T5vXaHfiO6GFZI0NkIprPCmFBQaaUcUpKsxzEDaN229Nav3MAepwrrVfuzyBeY5zm7lSK_G3KJ8BZnA1V0WbC1gmRxtBZ4layhWc60Zzc_lpgsFz9mxwIsHakoAAoCF1SEeqdS-EyiqIQeMDfhhF-vmb_0QWrpHJbuqjg48141MFCn5jb4I0i-_JOuf7amXnIsKowxYoR-ZMgWl6Av5W0WBXZ2x67WnB8prx5vvULFT9HBKpxXSXWl35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رضا علیپور، نایب‌قهرمان سنگ‌نوردی بازی‌های آسیایی ۲۰۲۶ ناگویا، با انتشار ویدیویی در اینستاگرام، به پخش نشدن مسابقاتش از صدا و سیما اعتراض کرد: «همه مسابقات را صدا و سیما نشان می‌دهد؛ سکو، فینال، چه برده، چه بازنده، اما به ما که می‌رسد،‌ نشان نمی‌دهد. قضاوت با خودتان.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107701" target="_blank">📅 20:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=KRYByLjpjlQqBda6EAzQ0N1Vqj7PUQYx5OD4bDyyNdNgs10yiC_rD6mwg8iAW_fe6vOTqxyhSQa9wT60GX3xSYHy9Vrg_Yn8uTjnZcnGgCglK3zdNzNVx6cjvhDGTTfjRPCoM3F_LUIdNSF4p811nbvnixFRKFZpc39WE-aWoRvnlmU3AF7vo1rKtTQcr32swMkwdftyJYdoluMylf44ksxP50mVwsCw3TxCL12rIjMl-ySgk31idYh9iOmmT2QcgycA5w250rkAUGuqSz0h9-XzvqKxfc1ZHeWyaGBFqnb-Y4yYHQXrnIcrkNg08nSrF1nSSseQWColrqD-AHClaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=KRYByLjpjlQqBda6EAzQ0N1Vqj7PUQYx5OD4bDyyNdNgs10yiC_rD6mwg8iAW_fe6vOTqxyhSQa9wT60GX3xSYHy9Vrg_Yn8uTjnZcnGgCglK3zdNzNVx6cjvhDGTTfjRPCoM3F_LUIdNSF4p811nbvnixFRKFZpc39WE-aWoRvnlmU3AF7vo1rKtTQcr32swMkwdftyJYdoluMylf44ksxP50mVwsCw3TxCL12rIjMl-ySgk31idYh9iOmmT2QcgycA5w250rkAUGuqSz0h9-XzvqKxfc1ZHeWyaGBFqnb-Y4yYHQXrnIcrkNg08nSrF1nSSseQWColrqD-AHClaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
حاج‌صفی: در کار آقای قلعه‌نویی و کادر فنی تیم ملی اصلا دخالتی نمی کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107700" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=aY72Dav1RaRLw36dcegy17KCH6ADMiLj5K7xqJbAJn1uKdRRVylpydzb_xCIq9Lpf0Lyri5ImHROHLAecCB-VReLBaZ739IVP5HYzJH1qJgoxpePTc5u5RhUf6zftIA8pw_1RYcmp0l3l3jjxD1DDJLsuslWtFFBx7H1jJT--OqjAQ35bU9VHaBXLZmq23jGvFIkkLa1pCFle6-ysnMiIAKKskCls_jYtY-KnrIL_fFl2PRoo-s9A6fTfdfFzKsb3FaD8HbBuVexDTp7LTlvwkap_M_-t0XSWuYJ4yBhoU6HPOxP4t9ZpZhgy0VM82bmnnLe2ez7hs5tKReiHbcJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=aY72Dav1RaRLw36dcegy17KCH6ADMiLj5K7xqJbAJn1uKdRRVylpydzb_xCIq9Lpf0Lyri5ImHROHLAecCB-VReLBaZ739IVP5HYzJH1qJgoxpePTc5u5RhUf6zftIA8pw_1RYcmp0l3l3jjxD1DDJLsuslWtFFBx7H1jJT--OqjAQ35bU9VHaBXLZmq23jGvFIkkLa1pCFle6-ysnMiIAKKskCls_jYtY-KnrIL_fFl2PRoo-s9A6fTfdfFzKsb3FaD8HbBuVexDTp7LTlvwkap_M_-t0XSWuYJ4yBhoU6HPOxP4t9ZpZhgy0VM82bmnnLe2ez7hs5tKReiHbcJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درآمد ۲۰۰ میلیاردی مهدی شجاری مالک موبو نیوز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107699" target="_blank">📅 20:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8956163759.mp4?token=Lcl5BurxCXGgJC1eDzoXN6IZcr_qgHvtuxjfkk4FXnnFKe-1wPHYkR9oSw4o83wjGugvUtVQXyPoL-zBdSVh3iDpfzqaLhl_J7ZqOEoDWTQMiYsgL_H3QvYwlMlkmIIweRLWdVpmW4ZyVFUVoRC1X7TDvOFP0xzlC2l_OqPaAdh-__b1AlAlOZbNVXn3txAieTd_HZ9MG0s4na-feNKm1Y60DcGPek2oXZ-9Wr4L4oZPIiqdsqsJrq1tP2PHZvK8z20wWqdRsmgPcOXTLOfZ23dH0GhvxjHIEzC_sIsE_9-GhJIoU0r8InM0dfQBSLwO3-cq6vqC3q7KXFSEdm4wQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8956163759.mp4?token=Lcl5BurxCXGgJC1eDzoXN6IZcr_qgHvtuxjfkk4FXnnFKe-1wPHYkR9oSw4o83wjGugvUtVQXyPoL-zBdSVh3iDpfzqaLhl_J7ZqOEoDWTQMiYsgL_H3QvYwlMlkmIIweRLWdVpmW4ZyVFUVoRC1X7TDvOFP0xzlC2l_OqPaAdh-__b1AlAlOZbNVXn3txAieTd_HZ9MG0s4na-feNKm1Y60DcGPek2oXZ-9Wr4L4oZPIiqdsqsJrq1tP2PHZvK8z20wWqdRsmgPcOXTLOfZ23dH0GhvxjHIEzC_sIsE_9-GhJIoU0r8InM0dfQBSLwO3-cq6vqC3q7KXFSEdm4wQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
کیف کوک ژسوس بعد جدایی رونالدو از پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107698" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263935f09a.mp4?token=Glf7Ju4GgiI4yxhrQjkXcor3XzSm_bLDjHFBKGgnFsboj7kqjlKUamqSaZECI7kFJB4HxOKhC2ZV2Ine2PkHz7M229nOSpdH7KBmcp7maAnaFaGQVbdw3AZw64Lvs1JM7O9rUvVYxxtmiNjxREf-WIRZEyvPEMmmCrPz-lVkNkCFMt9s4MKf5BYUxnkE07yDyrl2ZjI7Hb1EE_fMm80SzGeEoW0cgPR-TrlfO1XIrGkTeuUCK75IVueE2gb1UEfJhUommOtVUhWAd7RFkZAsZukB6j9CFWbg0EzpwOnU3DT7kq9HKsS0vVanp3depDbKCa67yMf9JJci1Pq1PQCEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263935f09a.mp4?token=Glf7Ju4GgiI4yxhrQjkXcor3XzSm_bLDjHFBKGgnFsboj7kqjlKUamqSaZECI7kFJB4HxOKhC2ZV2Ine2PkHz7M229nOSpdH7KBmcp7maAnaFaGQVbdw3AZw64Lvs1JM7O9rUvVYxxtmiNjxREf-WIRZEyvPEMmmCrPz-lVkNkCFMt9s4MKf5BYUxnkE07yDyrl2ZjI7Hb1EE_fMm80SzGeEoW0cgPR-TrlfO1XIrGkTeuUCK75IVueE2gb1UEfJhUommOtVUhWAd7RFkZAsZukB6j9CFWbg0EzpwOnU3DT7kq9HKsS0vVanp3depDbKCa67yMf9JJci1Pq1PQCEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقادات از صحبت‌های عجیب احسان حدادی رئیس فدراسیون دوومیدانی جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107697" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=MbJGRKSnvbtGr-lSHv0z-ArPaje0XcXRWHF3HbDftE06ljQJjKxbxCEOl7HtsADH4dsGkSVYc0fzCogcVcqC5zy4N76sXRCWFXdXE_rGkpOezcPaUiTtwTrHuYCsZuKHT5BlXlExm_PH1YV9WvmvPZ-UicBIKPqrCZYD1SIQBBKFwjPeK8xDYwOvGISCDVKXZWHhV4jhEkOxOIFqnSxq1QCgFGhnWQhSVuUjV3Zx-b7IWLaezDZMY3ewkq3gCevPY502Te7iG57fSnRKOfugcb1Pt-BQrmBBysHP_Nc3kOtBWYzdVjUhjl_SA-bxIKfIb-cfXs3vuaK-7yqLWHQk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX-45bSnKkd9vgsgoyTNzegGHLPoz0OAs8qRd-WFSNVOErUJvciuPAAzc48z-y5IJQK8L4MnYemAuSm0-rU-ero5e26pT5QYJEG1aTQiI1i-PJLobV5l5UoVymN1-Obi9r1cz46fNvRV_vWqbN5VQFJsPiUDBAB5kSNa6GrARrCWLg2CutewfCVpE9xnNcLYES0986qJR8QwC1ZDi1lCJvKj0MBDNiZNmYoRCObsnx4pGw3SL1Lncbh8DyrSrsyQQycibG2ZEM79V5ySsDHbngvbcopVtjvk94JvGsRQ1Cr6ngrEgPgaFEhO_zSzMziJiFrZNLjmyXwQphtp_5W4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhA3ezB-uT2kQBqaLX5IrP_iXPv0C4HWK_vUGpPfnVaL4Ezf1GbJuYXoXU2q7aiJ4sun5Ne3TZJYLEmlONSFxcoxa-gNRpa3VH7gNB0XBtxaeCA8HbCF-0lH9yUUqIJvEpuwtstpyw-LkfdfW0fIVIWDDV51QIXMP8Fh1HFQuFYCgTZHq7z90yBJMgOOAnXrJXAMCFOlbzppsV-pd1S1g4pfLTxh7inyRT5f5iKXl12jF56j7OnDBJURGp55822fBlvx786lEDZXnLadkb5qWhRp76bIpc9h86w0saxua0bAlfWM6Mc-Xd-dyKzLDuApwejvicqthsDTGjQ0kt1NjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=kJ_SB-R-g7x3d8WG1z1Q-kK5DUe1JZOsD8VtyUtl56c9O52Gt0DeI0IokZLfluRM4YMVRs6ikfnvl-nk9OIvkhCq0cK39q8uiofMecT5PgqJDWo7xeqi_2fhGtUar1hqbeodfStUfCgIkN6NT9iJb3YR1WJWYixE8wZi0KrWI7W47GBjGAe3aBJbntd0r30JX8cZvi0XCAF9wixW9JtrbEgQok_04w21b0geBcXEychxQR8tYKu6igBdR9eBaw8TakqlrKGnbjK0h10VZvcRarnNdUWblUP43wqKc4ma18bnkdail5eBsOfmNcw51mke7ZnAUfrc9Rz0yOOhT_u3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107692" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107692" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp7JQR8-HXw3yRthlOu0sVZPr97nS7ndff9q3f9d7BZcMPnp4Uztn75bWGgHYnrqUii-KYTKQZ7wWmptwpQ3aC3YoiI_amtfS-MHK9hICr-VhHxeoiDOypIiWj1WtcphdOBOGM3ndC9q8jfHpTEWc0M7VJ_7ALkMI7YzGOg6mHHQnszA2jYQ4cvpkS37_mYo7Km8FJkaM3onVg7nQx5bEFtJARrOI4V9iDhBISgSUS4pZKD5dk0F5KxMigTg78dikTMnyoc-SD9AiqnxeRnkiX1Xo_LP37w6knhzYflj6PcO_9qTI4xL5zOUcV6XyOjqMTiAwHHgRdV4tvRuJF86gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107691" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=GRk0f3bIMRhEdZZUSJdVhhKXsvCEU8YqrGAPROm49_ux-2obLm7GK4WJAt4uqFUnkqT2IQw77TIsuhY4m-I5Dprw8926sWdPAfxI8_I55aTaCBv9ERqmNODmc1sV6kddnz2GCbSjEOMN4h87x4HHTMNuZKyKhm7h4CMaK9XrpuEpscbyNZyHV7zxv5pTaJOa51wiSgGfHikiDxwYXB7wa4-GUmnoRsphhXCc7GdTVYW8tv6cUSh4kfIu0_-e7Cb3mxAMAFbsW8qmycKnnG2_5A_I7fgYf42U-YdWSgwmshgd0nKCxoTxqBpgV_4iN-zvuDJ1ApkekpKZpvehI1P5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=l6DxHWHd-9_1y18ku6rpYjajbZ2SvxJJ0llte8UB2gRg7-RZeOUb1vb0FceMorf49QG7PgP44tm82im2dqH87zzZLYwbZq68Vson8cUwNiuQzir54AeHLeVnCrp6GGzXv1alfyHJtt4f4SP987NO5UDY6gvg5Er9Mnf0wj7Z3slw1zKwnxhDUz6qo1LlTMfiLBCuIkcXz96D2M-ysyex-RUCRp-ZDwZgX5vaxJTto2L7rmsUG8s8SBu24oNoFpevFU4n3lFb3VP6P9RVdzP-BqVcNSpgYNHsRNKLexDawAh0HY6z8DTzmH1ljb7h2_x0rJBDqZz8UGvHEOJ1BzrFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=s94qVjOOUXGjy97inFM_YUwXwuniL-Cr0I6Q6rcslvChQarolXW1FRIqKdQ-fjYdaEPvStITWerJ2w3Ku_Cb6ZYRUooEjwNjn5_Ulf_nPOIfcrPW1E_FAnFaYuZHQ340_uxsFb_Ua1nkgm0QeLT2g04FoEkngtRKcxreAmH0LNbUIG5o8p6gdl9vYh6fPEpLWhVeq67jsBGVMm9KPww4NsnG8tj3ahfBvHP8XiSb3pcz4n8OlgxssZsQxOTb1CGpX1U1bQQNNageqK0diMKDz8xS5PMnVJVcSweSjieU4FgrxxVRY4MKqGyMEMHYZkBPWWqHlIyE2k7u939mFXk2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=saKFKfShaoquLMk5pXeTNXuxMLbD3jJ7ASiD9NjBeFsNNRPiuqnJ6clcvUl2mf1oMDHp9RHhuXYWoG30bZbWPHVX6uIBJzu-Hal2o4fuB0uyFjmmPn3M3PoMF2b_Mj_sMLDtHC0rX1LM7FPQikMTcfBv0x0LbJZ__rcWCaOxizkfo2EtGcoxSpW_mrcmFAWwRfGw3BmYQJqcSsCFV8beFaV0kiGaq8IZh2qX8yPyz_mTPksuN0RlvBWHeEuZszq_qrEbvgoQ7qv44nfaycYOB2C5s3G2vEKoz2p0rZmJ8XdxEY3lGpFkT7jEOj-cp3wdGna-su9pGREZtqN3pnxrwYkt7b0BYBP2dTwx9gqppDQAB8T7ptLjGuUgI6ocuqgzZQB6GtYctnnnhUj_JvRZkidzGKCWRt-JIS3Gy8d_WbVfiaaJbBWcbZxZ5s7s-LrpLACJm4x1F2DPz5O3LM1m6seTeKpnQM7f-3BrLrtDGvZep02vbvkLNllxY7_9ERBDkFBVRa9UxzqGWbh3z60VQAudJCb2A0-7fAxCYN5ftXIf_QJSVRz6EEzeoIgykjWuX5xgMPL8907Y639ERVlsVW2FI5INDvej9YfMzCn6EAxZadLeFw7-R3V4m9V9BvWfhHZWcMIO3rXSaQD4t1NKD59RvnQflp3VKQIEm8JmiiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=Jx6Xg1rmF6PMFxM2yeix1-Y057nlaQbpRDSjzNxDK_hEZaZ2x-qNoGEsPkCN8jnqOt-cWI0w4penc6WY4MYbiVWLa9r8d_uupUMTkmDy1qjK47BzU3AYEF1XfRdT7ZoCQ6cHps3Pul-FFBfy9RkLcmk7UQLrWFgH9uAJBf97BaKC3t_TFf2sNAxMxr9ac03t9j6TT1v2UbTrUIHL15z3BHZiScZEuHZ8Ok2bk6w1lX9eJ9-ZgN5ZmFH0sjQJN0Cn9gby3DOVPTssxGImKMcKsW5-ghSQwDHx0RZMYE0kH3gKH0eR_zWi0Cf7mBX0ijRAUNsl-ARLyjrTSYKlcjQ01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=uqP2mNQ1cMPf7jt_vyEBlO6gzgx3hkN95Y8MnjfddzxENcu2XcSkiyS8aJJL4X634sv_cKhcvY4n0k07zs2lof4PU6ZhWUpeX66CYIUR8J1ibWwH1qE8dawh-SgyGeslSuPrPKjgLknmaVjNI_BCGOv_aRqQGa2UhUJjxM_zK0Q-2BUDZZYiHSjMk-RnxczAhA6MQZJGvrnORVlslzVsPS5p0GAiNYfat1eHuL8zmAV5sQ63fDOepxKRu_JggsSdvr_B3F0GD8dwsLJxhkCpWg9SIaroagHZ_jNzU7MwgeCVxtqZHQDu2Q_rRuKAyC3IhiHMUoxPq1GpUSowx4h1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXo_wKYEaxbxXfBaworgDwhpHCMDR-io0xWR9KDVeOerhc2VISsZLNuBQehY2pHzRIf0E7kSkL8NTJEHbt9ObJ2hFRnwXiQG1GkmehWRWBPuNIGHi_dIwd0Yv6n_AhocLnnDvk-k1c4n_XnqdFnaPyyNpedQ1GrGTVm6bSixvtDeu3FRlCD5b2VzDwfaODnD--ueFWg-FBj3q0mW8AQMFabdjvT-Gtak93nC92XeKuZACNRFU9qCf-aIvN5y_tMZnRkLuhZWskATuTBmBAhYs77fOppEbGUNuPRyO7QZ02DoUjF598FTCNOT4HX1dj3I_EIorhVXDKiof07Qt0_xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=W19ABO0rpDZAGCdBlw0gfvDCNV8PM_ZGMLJD0hMAIbRAx-4cN4thEamgDKjq0EEJvNLQuIz-cMMbsFAMAIzhSUpvxOvz-VHywO-v4DhN3zZj3HKR_Nc1-BE_vt7YZC-4QVgpK3PhjueYH5a7x9uM3XKymyLM0VwblY3jhj4eoF-OU5Hzu7rkloJMo8gliHjUB4Urj782Z1oSw3xHvhZR5XDrwoWhl7SdrPFfgXkMfX_zOa7vpdWL86Ggvpe1fwRct2Axp45WPbh-_BKFs3Ncu38QKx6wKa2DRRK0i42CyOF6K5LwvbWbhzUwH9u3yFWBTuuL6Ekvc_cucs1PcDDjZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=DqjBqkhpNjg6DWmgrBUrpZw7qGXVrlF-ncz1jT5xUYN-ErEjOoMApKfpMmKnbTTsRTYhHx3SzFqXO9frYYelM-aEpeagAD0djbRmTN-V-Vb1vAZ_RIxUL-bimWopFwMpiG5xa6qu8IO3GUOBwZNwUzzaw1EJIoh6R01JFA3elSQyOMmg8lW-bs1ZCKb9XP7jATWKFhw26op6U2b1vAViX6WDuTe1NkMZOXX6_E612K1el2k4Zc87nXYUj8MVHpoaJUkMDVnGoMK-MxTnFk4dvyBAcDJJcX1RX_N61wa-WAQolCbNyVvYryDgVZ1C84MZPaMKLrtaphdF-aL-vFxs7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAqh6JVaOxK6HKSFGf1so0WNuMv0K11dbajlujiYRBYZDlkIWZ-Fv92krIywyT1uNCQ6eZj78Iqd0ceqScAa6HAohvPrQiRZneY_utwrcBuvONt_f2qihjx8RAHD1hTNcNxbp-xXIRq_AjrED430TTTgG5RQNUQCU1w_W0wxbtsgaFa4ohhY-T6mVFptRKySPLfonH7oFIfQ7uagyFWQIOG7rgAWHKurYxOTy-WKcr93hrSZ3-GBtCR1fI_U-bTfWII2rQD8_xDH3UjKEIVyGqNnWNg74hK5jGykBRXyjh5IuLiQI4x7hRYrfqZy7PvueKdbsEHOFZhE-IMP1dEArF_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyKPLr6gY3DRjmNwaIUTmUKxXlm4gv2QSKVydsfDg9W9PopIAABm6IwE0GYMSAPv8mDFKOvGo6jHlNPzkk8bMmJqczDFN_hBITjFvVk-7ZEVKXuvSFH5R9mEk4gd9TcptgRlZ39g5HqtLFkw9bR2U9Ow0JyuMiAToNq_GOzhPuRIGLhyurPbpb8vU6ML7yQUG6SvjZuCXx31sMubwNpYPjtAFdWEhqTqIfwTrY4HaNafYZauHmUghvbof9naSKtk_P4Ov0ZLl3oT1H2CszslLyDK_teCUbvLalgUib-rc5w14JlKfe3cg4FNtKud6KqJQoR7ZsKrB57s-0tbHVNAZDU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyKPLr6gY3DRjmNwaIUTmUKxXlm4gv2QSKVydsfDg9W9PopIAABm6IwE0GYMSAPv8mDFKOvGo6jHlNPzkk8bMmJqczDFN_hBITjFvVk-7ZEVKXuvSFH5R9mEk4gd9TcptgRlZ39g5HqtLFkw9bR2U9Ow0JyuMiAToNq_GOzhPuRIGLhyurPbpb8vU6ML7yQUG6SvjZuCXx31sMubwNpYPjtAFdWEhqTqIfwTrY4HaNafYZauHmUghvbof9naSKtk_P4Ov0ZLl3oT1H2CszslLyDK_teCUbvLalgUib-rc5w14JlKfe3cg4FNtKud6KqJQoR7ZsKrB57s-0tbHVNAZDU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XojlIVHjCoL9stQdjSeY0emOD_LYm8qnDYrFU4wwvrF1RA2WHmv-AFfsuhQt00HDg6zpUaXRHWE4stgqftOQ2_j2k_BlGypo8ZCYJMzGDZXpqZc6oZLgHjXlpsN9GWkf6NdZgbcNN7lPFd1muKvvzMAYt0ya1Z2V654oSQbMbricxrY8r7-RWz5-dpG0I_4cYYNKzpbwMA7Z64WBua26m14P-jDMp8Oy-lVP72pq84-peYFD0giOe0Y0aCLuRmaSrqOFAeTITWzvme22uBPTN3FJNKSOTFAzsA735SXFxdQzaOaPis7sRslDptMZxHMr5nCjjvkZo5WFtL9xhqIpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=XpH9ac6dmWI3FGZKl1RSCnSzicNiIt943W_AUjYR6c6lfAaEBAUJcscsxdxjCIrYIykTMccCOfnmq4ZIpDtJx-G4xx_4e9r7_DpBE5jFwvhXQLpMzU8KHJ8GzO0u5d2vPaRPVQfLufeXGNFTKDxaFq0OhqmDujMc0ddItJti5lpyRRvVrAkd0PwxzkTyaLj4R5QQ5vBTBuoX5uQD3FiHaqS-1FiR-2A7xUUFrZeKoQfE1iiG9ZCmvVUNJgQHcdzfrvUbY9GD0We6qE_zeeMmPLp6uhB8BSGTNmen04Ql2MVy8MeTPoWhsNG5y4g6DTem_1LBmaHhE-hLYeKmQjzH8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eade000140.mp4?token=AqLbJXcrBShB2cH1_ELqn5lhYN8FJ7bPConT_08Glbe6VvD-_H__7FgYwV1B2oq9fkX610UE4Vj4E76gSO0TQaWFsHZ-I6oyIiEzXZfOb3_KGo9A4iOCK9X63iJ-GFxoB1B1U6vlTM6LE2oGyNEN7OwA0DxqvUuPkUqyatPSfSVZ95ow59hUqMuSDbbti-G37wet1ohlj-pbrQ3Yjrnl1Iut7aThGB-eodZASVc4tEjPFpwTg4rv4QDNt3JUsn38hl5vaFfI54REPaIRskuQhEN4ba3dc2jgBxVLpPpRCPrIVUlmA1o__50tY2wCylipRkooMdg2knM2FDgHGdQsYbaaxCTDFzU6ZPH14gKStZuMmzJgw8lTED0ErpsBeeM4iRWcTpovjtn7yuusPg7V7YuB49PdQptoPouEe1HWmV7zOMm6mqzRUVBPeueUi67kVZYcb9BvSeQt-EyctbrTVmLqAg8o8_kY9mT5scwJnA_ogcuBYSCAHVhDN7rUboUT_93EPn-pQhrFoFfUfWQxrehpnsR7Rq5C0ZalNVY9CV88PGZoclwYY2kHAzbZZrpzl8h7Ujzf7OrNv_HOCzyGwxs4Nck5elh7vRXjdX_zlzoQQCQhZ4u1TfejFBS5XQjW8uK0vRqw-FZN3yWtJ-woxA1fbM9OfWtmoaXOd0bBVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط محمد نخودی با شکست حریف ژاپنی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107676" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=I2TZg1YRoNF9hEAxbcTGjx1YYzBpo2LhXl8uFcafik0Ko28LrLrlIpnsZh1c6qRuZfjDJvHNQ8RQi6M-uO9Iwr3dgtgzokkIxhIHY16Fh0KjpxrWp83PA8Uc5Cqnf5vjqxF9V-jxKnnokK4pSO5w6Diu-kFHbOVROK2K6qsA-qyzCZzUXdYsqRWifR5x83mXSVUvc7BzJKbxmmTC4GnQlyqjsqkvLgF2AHxRp1-AahzNLs-MiCYFtPQpa7Gc2mPZ1c04I2EIRbDqxonoR_CtlpqIt8ctvlREj4GGsGi0B03VorrgPkZSa6kDADDNJKYSQvcrMWP_ecRC_uBXwvSebQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آخرین اردو تیم ملی قبل سربازی =))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107675" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moo1-bhGIfQdFpdJqg2BqZh1LmgfFzjJhNZwDoxpaXvdZhgxWN6BVxecil_da72PlhxhzoI2xY5yzdOhyrgXhqJueiUbEcr8UTd-SSUduqy_FniYkJbikqwGW_Xx9ZzBQ7DwYdy0DuGh3OxNQtHbaYSKxpoMZ_tR3Juy4bPnJ4fgwojz_9NTxjcQci_5AcYqjYjXXIvel0768YyI_b_T9nExTj0osX43O-IA1_UlVxE7x64hA86Hf-omR_hJEmp_KEv8RX1QcIlCs-_1l8wxwX3jBeLgmB78V_GYsDgJ_qO6MYrSZBw9ek4FAqGqmkLmiJeaJqQYXpSWM_7suC8qfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
هویلند بازیکن تیم‌ملی دانمارک: شادی دیشبم برای ادای احترام به رونالدو بود و هیچ قصدی برای توهین به بازیکنان و مربی پرتغال نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107674" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=PoNP1zKqVIn2tAdVfXl5d_nGkoA3ClhknuKW0__u6O7Rvxkyms_Crx9SvxlJ1_SfiWkuvessAiDpHGsP3C27AdrD9JCl3IbFEjGmkdqnQ4eSb2NkbiYJAZTEKAIa1EkSNYiCk1zXpXxCkWmXdOjWxUCE2sa98KjAzEH7VXBvG8qbko4I37CwnFPENy07u2CcuObuQ4gGtKZV2cQRaQeJITgYncMWrL9fAevmttaUIwJKy_3qubyBoH1fyLUdZ4nnybQEoQaf9eNPp9LUHnt99m_XuwCG_omU_-qO1DlLruAAQIqvlhZLk_z4EImSycIR5Jstt1AIzbLNJj2CH0OWNL5CyJErBDM328LwSlfm3o_cwPbGdc6trz9_T86lzFF_6TfjcvvTkeCgHi0LZtPTzv5BVRjUFX2cKeNtcUGvyjyyUpx_9XBIKQuvoirFvn5QFDb9rBk-Cy2iM7Uc8pnh1Q8AYaLUiuE1oAvhmHN-kpl7ZlxrPgzrf-vfqFz6eTr0EcGbvuTBeffNZ-sxxa3grymRo7CMyczleoVR_8E_jZHFWpyg38CW3uA-CnKBfOaKMnLS917DY8v_NIUnWCgETz3MonDle03Qj1lcyS3Q-fgyDCWe1EDGOpkfvFG_qraPFIVPW-kJbCmjuSCRegbcaARGxgLyD-wwOAUB3koZP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=PoNP1zKqVIn2tAdVfXl5d_nGkoA3ClhknuKW0__u6O7Rvxkyms_Crx9SvxlJ1_SfiWkuvessAiDpHGsP3C27AdrD9JCl3IbFEjGmkdqnQ4eSb2NkbiYJAZTEKAIa1EkSNYiCk1zXpXxCkWmXdOjWxUCE2sa98KjAzEH7VXBvG8qbko4I37CwnFPENy07u2CcuObuQ4gGtKZV2cQRaQeJITgYncMWrL9fAevmttaUIwJKy_3qubyBoH1fyLUdZ4nnybQEoQaf9eNPp9LUHnt99m_XuwCG_omU_-qO1DlLruAAQIqvlhZLk_z4EImSycIR5Jstt1AIzbLNJj2CH0OWNL5CyJErBDM328LwSlfm3o_cwPbGdc6trz9_T86lzFF_6TfjcvvTkeCgHi0LZtPTzv5BVRjUFX2cKeNtcUGvyjyyUpx_9XBIKQuvoirFvn5QFDb9rBk-Cy2iM7Uc8pnh1Q8AYaLUiuE1oAvhmHN-kpl7ZlxrPgzrf-vfqFz6eTr0EcGbvuTBeffNZ-sxxa3grymRo7CMyczleoVR_8E_jZHFWpyg38CW3uA-CnKBfOaKMnLS917DY8v_NIUnWCgETz3MonDle03Qj1lcyS3Q-fgyDCWe1EDGOpkfvFG_qraPFIVPW-kJbCmjuSCRegbcaARGxgLyD-wwOAUB3koZP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✔️
نکاتی‌که قبل از خرید آیفون دسته‌دو باید بهش توجه کرد؛ برای رفقاتون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107673" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQhl3BfUbilIXzA-VHBRoMOpCnnrpkDHEY1v-cTYXSe1pfMETm14mRB85yrzlG1iruGkQMcef39Ehn2JTY6Dzr8E8jPZ4MKMFijz_ccSe3rp2cvKLtWDGH702vOGW3Xzmjivy_--w2-u95JMkMRsvOJp4wtcv6YjodwWxixJaq7oVAo419ozyVmyySHe8TavTxQromID0IhaK-jOcdnI2sZynJ96Kw-45pZIWIT4Pc5jsaRzZ59dsubjm1Po_zrxApRkPJbbIuefzUbn8E5KtKNG_zcHdn7tkBgy7YG7x6B08ycDaJ85dodrujP_tEDV7sRZw-f3yzjlZKRrzaMDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
استوری همسر رافینیا ستاره بارسا!!!
فوت‌فتیش هستید دیگه چرا علنی میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107672" target="_blank">📅 12:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=W2Q5DkMLK0HTZLzfUOdP-mj_12FAT2ZF3LbMuT0RytXumpc71mGvZhIgeHRXELXdMpAA9twr_xjX5ZcpCisds_Gs8488uqSVLb8nHc6mkUgnBY5gFqH6ULyfogt-Uqy5OuRJsQcDiPr_d8gG34UMkUWFcUWLsrOP89IH2WSqyWvMDyclN_YBAHOEtJWRq_TG49P8eO7Ce1pinVgTI-mcbJskmE_icgPdggjV3-LCUt1Xru20Smp61O0RmjgK17x-vdkbgB34lNrqhzxCq7xVTSXgB7Jv1vZaKBRZdM-UyMs39vg5X4GryisEUGU_cvkxyQhrc2nZIhADfdFQqUyhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=W2Q5DkMLK0HTZLzfUOdP-mj_12FAT2ZF3LbMuT0RytXumpc71mGvZhIgeHRXELXdMpAA9twr_xjX5ZcpCisds_Gs8488uqSVLb8nHc6mkUgnBY5gFqH6ULyfogt-Uqy5OuRJsQcDiPr_d8gG34UMkUWFcUWLsrOP89IH2WSqyWvMDyclN_YBAHOEtJWRq_TG49P8eO7Ce1pinVgTI-mcbJskmE_icgPdggjV3-LCUt1Xru20Smp61O0RmjgK17x-vdkbgB34lNrqhzxCq7xVTSXgB7Jv1vZaKBRZdM-UyMs39vg5X4GryisEUGU_cvkxyQhrc2nZIhADfdFQqUyhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
🎙
واکنش متفاوت بازیکنان تیم‌ملی پرتغال به خروج ناگهانی رونالدو از اردوی تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107671" target="_blank">📅 12:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya_RflkY7RqcgTVhKI8DN8DOPPUGrNpCQQJH7jWsOCf5E31C7y5sEoIxLbMIIJwAINDq6nnw5FPL3htNpZxcJNqWqguNwEwF48uRj32-iRFP2-mekHS-Z-ThoE04beo9p204ARM477NkoLfzGkMRdM3chmPLpUpQ7GYmIHO3h3SFExJDM77E9WMgqWLT-4-2qkISaCPXMazT9ADWEicrP9fnb7gNraS_XjKIbnryqlqJ_IkpQP80JwjjnYnf2HksHaQEdvQSydCDwJyV_wD5fGSwASxdJL0bE6zo--qUQAHJj4y5rDjL-elWWS6fxgVWtumZdJ8JKhFGUJeIbirrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تایلر، د کریتور (Tyler, the Creator) هنرمندیه که تصویرش روی پیراهن بارسلونا در ال‌کلاسیکو رفت مقابل رئال مادرید قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107670" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWfvXSXVNHZYDFkpjZOboRHm5i9Ayv8mAwxRMuOgn89cHqXhB8RikfxqyHY7uTarZflbLxADZr1ceNSOKDiFpSP5CWnKeHF-gGoOHyVmraWdMZWUNYt4bHTFIQhkbV6XoRM_uUYU7EQvGg4dUwlEgtu3TM3yV3HHvCPIJrfphruYjVRVxvLqAxrBIZjXLUDs8n7nvmKeVd7mh4uCoQ2vmmKqAU4oUDb-1ghnV4eSZHBuqYcOQ5eerVVR3_VQrVKNVzNhQKz-fyZcRV8olqIPfF1PGi8sbxAMlBldtsQHZCsXbDsNTp9IJ44YcfmlQ3LqaHve78wnCIoX95yVJZZlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇵🇹
خط‌حمله پرتغال بدون حضور رونالدو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107669" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv5lV8rpuwoLYVgjy0nuZlM_UW1FgGVymdzZ-hrOp6H8e8qJFDiDaqttKn4FmjSDJXBNnb4luRkzESk34L2HL7OaKiLOZmRtGTb-zsVOPWq-BntXJCox0pozTrphBL2TtRKteT64YdYctNPAgaArOUC0YeMtBP1DjWRp8V_mlub9KE5QUMBxPQtEksz4fk-T_uLFZiEzwM4ZOsXfpkcgJfjHlwZEWLWS1OQve5_IcpL5ljKBWQqGtZgsLj6GlhS5TaSU7Mm3mtEGlFIVkhld--X857QahoCvHicirIfP1AH1kiwBLUAWdIwV1YPaY079SiBsa8Pyhdpqljyaw_tR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
📊
بر اساس انتخاب  بلچر ریپورت ، لئو مسی بهترین بازیکن تاریخ فوتبال است.
۱.
🇦🇷
لئو مسی
۲.
🇧🇷
پله
۳.
🇦🇷
مارادونا
۴.
🇵🇹
کریستیانو رونالدو
۵.
🇧🇷
رونالدو نازاریو
۶.
🇳🇱
یوهان کرایف
۷.
🇫🇷
زین‌الدین زیدان
۸.
🇧🇷
رونالدینیو
۹.
🇩🇪
فرانتس بکن‌باوئر
۱۰.
🇪🇸
آندرس اینیستا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107668" target="_blank">📅 12:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=RwiMZDrrqClqBsbf-35znM350tcatV9Rkgn2C8WoI8657R-GC8DBuBi58UbQshPitFRQvsO5yUCEqpgem9UPC9g7QmFKJP3Y1K8mCWNzRe8Prhcj7mBptPZJhCwfCre--_AEVbIL-eDZ6YPOKFavrSPU-6TMPew9CDL5-J7D5DDfL5wnrQGe4dnbakz7qf03xTVABGhiy-J-rfs8WsVwiHDWDtmfD8mOLD5XgU3T_St5XRAnFbTGvunwkwlC2J8FKkpKGfBVErmhIiqf8G7hgc33Mu_VqmsA2DrxC54pdDwZQa9FiL9KOIUod3C3VYQRgJOb9b18o7JjV0n-UOsOARx09dKRVERdqP2_wv7LkhB0ZjRBCkJjJdlBnnhiKOpznDrlD2iEex3phKORYHcT49-f3GTAUf5waMXtiWkYbRlwQeNqxCXE-yNU6VlkELiQuTud2eJEdTk2JTnrS-_Kb8CcF5yB0nNSo-ADo5z6-MKZcWcFVi8Fuuv1pe4eHravI-kzDtGbfTLSObez75vTJdRlOOdA3r8GnEx7L8TNlRCGgvwxh2c6jqh0NMI8a4SLMLVmDGv_VcfLJThDKbJw2kUVLEmZYR63lXJKQsXyqRX0Q6c7f07W9KFtndflZhvJ7Uzl2xIRWcfyTvjGwUwZgQyXWJ-S0LLZhF0Y6PESlsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=RwiMZDrrqClqBsbf-35znM350tcatV9Rkgn2C8WoI8657R-GC8DBuBi58UbQshPitFRQvsO5yUCEqpgem9UPC9g7QmFKJP3Y1K8mCWNzRe8Prhcj7mBptPZJhCwfCre--_AEVbIL-eDZ6YPOKFavrSPU-6TMPew9CDL5-J7D5DDfL5wnrQGe4dnbakz7qf03xTVABGhiy-J-rfs8WsVwiHDWDtmfD8mOLD5XgU3T_St5XRAnFbTGvunwkwlC2J8FKkpKGfBVErmhIiqf8G7hgc33Mu_VqmsA2DrxC54pdDwZQa9FiL9KOIUod3C3VYQRgJOb9b18o7JjV0n-UOsOARx09dKRVERdqP2_wv7LkhB0ZjRBCkJjJdlBnnhiKOpznDrlD2iEex3phKORYHcT49-f3GTAUf5waMXtiWkYbRlwQeNqxCXE-yNU6VlkELiQuTud2eJEdTk2JTnrS-_Kb8CcF5yB0nNSo-ADo5z6-MKZcWcFVi8Fuuv1pe4eHravI-kzDtGbfTLSObez75vTJdRlOOdA3r8GnEx7L8TNlRCGgvwxh2c6jqh0NMI8a4SLMLVmDGv_VcfLJThDKbJw2kUVLEmZYR63lXJKQsXyqRX0Q6c7f07W9KFtndflZhvJ7Uzl2xIRWcfyTvjGwUwZgQyXWJ-S0LLZhF0Y6PESlsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
📊
راز شروع بازی‌های پاری‌سن‌ژرمن چیه؟ این آنالیز بسیار دیدنی رو باهم ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107667" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emIz2oTAUBgld7tGr7BTmT8agDd8xoCeCydk-D4ogkEv7tN4gWABi3pPhUi6H7IUSQkjhe_EIVhAQ2Sg0BYDF5B3tNuF1TKPdvHWQA43e7cFz5mj16DVqf8-HHoS4FTn_bcyAA3CBbnSV3TDZJnrzZrDRedNRtK26FpeCcrHMyTvMBzh_1WIh4tOllohYG9nF7EXSwvhFXqFSbxOEafJrhdc51XqEArMhPeGVMeymHImPNcIA9bxpQH93lTyvYsIsAEsv7cweWoXOl6-Ifu29Jg4mdlmMvYec2nMWIoMc9a7jLahi2T1pToQvGFz0cPzLX0wsEp-stySWLMn52ZrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تیم‌ملی والیبال ایران با برتری مقابل پاکستان راهی فینال بازی‌های آسیایی ناگویا شد. برنده چین و ژاپن فردا به مصاف ایران میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107666" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezsGQ3aANHgWWRBGqoBj-3GWhzhZDH-5S_qrvdlbarja9FNC2Z7v8G5Hjd9N0uWjeQWZxqTMJURvR7kB_umHBGlGku22tn3zXLClxC02nVhi2Jrdlc9TkaYmtkfBoE3FguBpaRXb2pvpt9WsfRu_KOK-Hsk34wT6B7vAt-gZuyAHcxAaywhyFJrIOSvwX24DS-0Pb-axrndqmzaEKHKu9g5zvaOFjoOIe_cz44cgjFEF2ohD1qtkyr6-Ni7M1cIMNac-NT8QOchIl1VD10qogsQBK_dl_0hy7UawFsaGPA-YNOwq2qekt7sxwkDK8Bc7QBUSrXb267XPM4JNqGggzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال نباید فراموش کنه که رونالدو عامل کسب سه جام ملی مهم برای کشورشون شد:
🇪🇺
یورو
🏆
لیگ‌ملت‌های اروپا 2019
🏆
لیگ‌ملت‌های اروپا 2025
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107665" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107664" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbRS_PwdtfLVhJ6HlFxdtU-a39H7xVADEru_pfpvhcHEKLn2nj60mevp0kX-CL2oLrFI8wE6ZgBrHfObZwpjl53C1HnPJrkdE8f8_IPzPRj3bU-tCAw0x4iOo520xWhsRAlWoaXLrrPGdnZRbeBBDv82dGxSNSkdbqVKROkJIJj9v1tQXywV4y_uGR58z-J4_UICQmS79ZCZPYDBNhGFCLRuiQ16cltR6yUeFKfnAagFKdYd7FGWYUgosLiXtBJ7lguG3LTAT1U-54IQ5FcVpKbuevhuyzv8HYY4lVb-A7IQWR2dM3tw51-2UN1uxE6f6olYpMYLnCrg1c59A_wCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107663" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEMQI_6ob8IrtnVG0HUzt1ywH2JVaRyfGUmK5LnK-l2sVSszprvKrgB8apfrEHk7AFwQA-0AAEKLQaASsmcBvjNuz0bVA4hHBqKnlb_g-mBmhJ6N8j8c8vgO_Crp93ppGaSNSf8a-Rv-6yE-JvhkOGnNgtOR6OuaE0PJnAzJ_kQ1F63U6jcD1LGBOpW2u-oArrmzse_roVvwuKHUSrtcPJXeJ8HaxSI6YPc4141gn5W_dIFNAmCdMK1AvoNsH8tBvCXiYx4xQ6ln8j2wD4iqU8uCTsG72uTSMD_TVwHHe-QMWyjh7KQoHthfcdRIFPVBkzR1rDOohvlAzCk-e1xVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری یاسر آسانی در کنار وریا غفوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107662" target="_blank">📅 11:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312a800413.mp4?token=bpB9htWhKLXfelCeGgX-lg9-F78dB9U6SHJx78agcto8C2DmnqvD5pdp3jFBeoQy7SPVNiHpCcMqkhPS-03JCdi6-2wE1xQ6Mu9-OEtHPWG8LUZ0H1KdJqDb-eJ3FR7NNHtPvs7GAdHltXUWoqvvbBQNcA-tOSXDUAn7B_-R00CRwOVWTvzkszVAVk4dcFq-gftczuW3qk6IuaSq1mYXrsuQGg_dWH97dwemcqa8DS29WBrgWkBkC81LkJd6WSUEz4eWWs8XlWbaFryGrkesAYysAZG2mu1Mi8gUUbI72Hqq1XHxJhBApwAtP3vb_chkcVHA3nUd_ELHCOGh4DOD-wsZ8n7ECXdeQ3tc3tWl7K0uRnP8yIP5A0SbqjIsj5-s6drFWqjyXhHiFOIaXBFNvmKiBN6lVkNq2Kr8e1OzDuDEACUr0CpO4j1FXjXR_kEPqWlINhhye6pJJUL3TW8p2FtOjyKNCH4u2UEDNpXts5Ahf2xl74CHUniXvxO00NN5its2pWd0uVh9DCCUnWoCBVTy4eLemOuaPvd6Y4XMUNx26HtgMJwcS--9nVmdaWQSMncOW1xFgo3dQdV0DYpO9GtJGU-me0l0h-34DQ_cOfXCUZJmgxyKHMw77BxtPIhv2v0Zvltiq0z6ulu5kSA3hCli-0pYWjq9jQd-CMDDRlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312a800413.mp4?token=bpB9htWhKLXfelCeGgX-lg9-F78dB9U6SHJx78agcto8C2DmnqvD5pdp3jFBeoQy7SPVNiHpCcMqkhPS-03JCdi6-2wE1xQ6Mu9-OEtHPWG8LUZ0H1KdJqDb-eJ3FR7NNHtPvs7GAdHltXUWoqvvbBQNcA-tOSXDUAn7B_-R00CRwOVWTvzkszVAVk4dcFq-gftczuW3qk6IuaSq1mYXrsuQGg_dWH97dwemcqa8DS29WBrgWkBkC81LkJd6WSUEz4eWWs8XlWbaFryGrkesAYysAZG2mu1Mi8gUUbI72Hqq1XHxJhBApwAtP3vb_chkcVHA3nUd_ELHCOGh4DOD-wsZ8n7ECXdeQ3tc3tWl7K0uRnP8yIP5A0SbqjIsj5-s6drFWqjyXhHiFOIaXBFNvmKiBN6lVkNq2Kr8e1OzDuDEACUr0CpO4j1FXjXR_kEPqWlINhhye6pJJUL3TW8p2FtOjyKNCH4u2UEDNpXts5Ahf2xl74CHUniXvxO00NN5its2pWd0uVh9DCCUnWoCBVTy4eLemOuaPvd6Y4XMUNx26HtgMJwcS--9nVmdaWQSMncOW1xFgo3dQdV0DYpO9GtJGU-me0l0h-34DQ_cOfXCUZJmgxyKHMw77BxtPIhv2v0Zvltiq0z6ulu5kSA3hCli-0pYWjq9jQd-CMDDRlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
عشق به مارادونا، با توصیف آقای گزارشگر
🎙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107661" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=pm9_4_wGyDreJgkyxoGWhPYU7hotI_5eQ9EN1rRkeWuxk0zaBZris9UChShmGIjuhFjTj6qEKDPIKx92VuPKW7ZileJTrflLE6H7C4adUDZFF6yFS3SmxU68TitLf5GJGtyaEhB_mLZxAd1Km0EKaw8ZTrl-gRkUgY02YAOcBrU_srvlkvwHdZvRDgDE-lqnsu2aTpvLHt8qJa9A7cJ17kA_AcJ0zj04T99b1zfaRlXis6NyzBZDTYCqJPQwEVTUe8-2Y27Imbmn9hSPNSAZnciqMShBr9aRmDARa4Ex2YPl7W1VAPr7bU0E8fuk8eb65rUT-f1piziVYBmbuTnvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=pm9_4_wGyDreJgkyxoGWhPYU7hotI_5eQ9EN1rRkeWuxk0zaBZris9UChShmGIjuhFjTj6qEKDPIKx92VuPKW7ZileJTrflLE6H7C4adUDZFF6yFS3SmxU68TitLf5GJGtyaEhB_mLZxAd1Km0EKaw8ZTrl-gRkUgY02YAOcBrU_srvlkvwHdZvRDgDE-lqnsu2aTpvLHt8qJa9A7cJ17kA_AcJ0zj04T99b1zfaRlXis6NyzBZDTYCqJPQwEVTUe8-2Y27Imbmn9hSPNSAZnciqMShBr9aRmDARa4Ex2YPl7W1VAPr7bU0E8fuk8eb65rUT-f1piziVYBmbuTnvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اون بعضیایی که میگن از صفر شروع کردیم ولی خب ؛ صفرِ شما ها، صدِ خیلیاس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107660" target="_blank">📅 10:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwowfA9U4j1YN8ZcGHt30BTsWnbEkcwy5I9z7YzYCSfBM9dkynHei9mllS9Yzrs2I1JNeY_Q8exqJY2sKA0ByMfwG5wRudbrUlNY84SPr0xiZYkDCxvBtvusKKLzKPDg5VRjPNYkGrPqGSHWW1Pv3RjTPmasDIQr6FiX6iwpZkh3v1bZfUwDNdXI2-a7_EZ_vpzTa3rFOmTb3EOQsYnh7KRZmxj3Dad9LEpMdhIsVEfpviz9C0ePLNwlG6mvMt_JIOqv4JTu6pYb_WEbBOWw1C2_gIHsfkFaQ2vgX1BTTgmSEHwlqXi8i_B3uNwDcHHKi1nLCVhCVMtyPpsLUnfPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
بزرگترین ورزشگاه‌های تیم‌های ملی در جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107659" target="_blank">📅 09:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvasV6jD_F7qLHrvQyNLo5XKxIqz5gTDLPj3Zru4435NGJ8Rtt_JnOWHd1lDabABjUKK2Ceais0y4HGeG4VG7bcY3ssf_Hfs9V9opWxSWvbCPhAJTe_YeVm4H1-rSLAOsSNGpRRRosfGaUsIZpY1wCA_0RIDB9VahNymDUAx_UlCXA4zXt4SbXztdlls5pi5xdCreIHCwWjwgbi2m0WQikXrwF2As68LaIz-rK5XmULKSTeXCzboTyKLUukiIdOwh5hAzr9uONY8dK_HpwPYic5bsuTLLkbjmM7v4IfJQhSZYuMLEK6qZq72sHt1c539eFhM9sNAgOZjmcdA6LOt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🔥
آمار و عملکرد مسی در تاریخ کریر فوتبالش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107658" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85455aa172.mp4?token=OV5FxcVy76ocaTcwxNG0D4oVhsw24A2HLJZ7QA3WZgSp5CO7gcxtpENYAWMnFL5kiJ9o-L2e8n_GpVMM_QTbtk-nJ_qG59fourd1X7GE_y4j3BYiZbeZm88MK94Uue3wzIICRartShzqw9lHWYqux126FPrwXFtqSFQfPsVUyB-M4Ewrko4KZZUSF78EAs2rxlRaUQMQkmyoD9B_KMOYf3OETWNmWxzI4lZn8NAaOAQmpSoRo5jW3RpR6U4_DPhXW6XzvJFZdcb_p4kE9I5TXKXnO9qOiWrIDb71v8SIlvBekADe0iuX7FmAyXsiOjVozLNK6dT1XjPZix-_lqaolabwy1LbO42w-w_e63FfhI1Xi_HyAhrUlqmvXYEmOir5913Ves8T2sIC2KyFfpvQTkM0dIGNhjldSvmXc3cOx3rI5dlTIQcC0UrzVqMssK1jUH5PHDVz8s6DOPAGYvTPWQE8-7BWA56DsMLOrga6jfSYUgU8jsBccxcb3bj7gHPDK095syWuyi0mQREOF-GhYWSFzdw9TMgUGgGM-SI6gkbaPFGug9Q84I4NGYDWb0VSsyJWU5GUC2ukftPaGqtVcMbuiFxyH4xFsOBVBlSBeAmvLmulVke3c7Swgz7AcoqIQwW2L8_QcVoXy84Mih44EcUAW51Qww89k2mtkE0bYBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85455aa172.mp4?token=OV5FxcVy76ocaTcwxNG0D4oVhsw24A2HLJZ7QA3WZgSp5CO7gcxtpENYAWMnFL5kiJ9o-L2e8n_GpVMM_QTbtk-nJ_qG59fourd1X7GE_y4j3BYiZbeZm88MK94Uue3wzIICRartShzqw9lHWYqux126FPrwXFtqSFQfPsVUyB-M4Ewrko4KZZUSF78EAs2rxlRaUQMQkmyoD9B_KMOYf3OETWNmWxzI4lZn8NAaOAQmpSoRo5jW3RpR6U4_DPhXW6XzvJFZdcb_p4kE9I5TXKXnO9qOiWrIDb71v8SIlvBekADe0iuX7FmAyXsiOjVozLNK6dT1XjPZix-_lqaolabwy1LbO42w-w_e63FfhI1Xi_HyAhrUlqmvXYEmOir5913Ves8T2sIC2KyFfpvQTkM0dIGNhjldSvmXc3cOx3rI5dlTIQcC0UrzVqMssK1jUH5PHDVz8s6DOPAGYvTPWQE8-7BWA56DsMLOrga6jfSYUgU8jsBccxcb3bj7gHPDK095syWuyi0mQREOF-GhYWSFzdw9TMgUGgGM-SI6gkbaPFGug9Q84I4NGYDWb0VSsyJWU5GUC2ukftPaGqtVcMbuiFxyH4xFsOBVBlSBeAmvLmulVke3c7Swgz7AcoqIQwW2L8_QcVoXy84Mih44EcUAW51Qww89k2mtkE0bYBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ابوطالب آماده ورود به فساد فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107657" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107654" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKI08MivWTWx_meCgMpUSKE2hh05gWZ8b5VTSYgmwQMlX6Jm1OrSqrcqDsPc5uZJ9lsJqqsbXyCwgkQkSs70avMeYtrvPeeQD3PjhHNixv8n8bSfQW9cAFJzjdcO3wKPJ8Gta3lePypy_OxhqUu4qmxntMhcVLBbplkYBRP7byHc4A2Ja7y702GeHTzf_Yybn5JEpqGEinlbMBom_LdWWN944-IC_tbUBl7JQheHCTFCUWWffEnWlCmgh6kjzBQTI0V-81RvGyKNf5WEElJy31degI9vlrfCb-T4_IL7h7P-ygSYOWNyDRmkvrC-w95Aq2YD_pIPm3bXlpBQfK-UCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107653" target="_blank">📅 00:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOaFA7B1L9tP5emJ1B1jaZ2fBqrVmY-_JGbe75BwWWJydyaXq1ac9I4_JLmMi4622L1xAvOYWjIngsbi74p3wsc0vpd-XEf99xZH14vLyttyyitcYV3XESewjBGhQ0egy5m8YzlNeKXReIvZXUuZKm6eurYKumhkM5V7lWarr1BdgpzTKrdQTeHHSc9yUatl9T1rU_Lm4Z1O4Xg3fmZKmKKad7k30xLbjccAEpYA8_zf_3kXVMbzQUr0B9w9VSmL2wVvSyPN7FLdF4FHhT9gt0XG99Rp3w3EPK-yYQ4c1MENTPyG4I4pveAtZWTw6rSc1kJZTG6ckWM-ZdOEMYvnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه ژسوس به رونالدو: خوشحالم که گروهی از بازیکنان را دارم که به ایده‌هایم احترام می‌گذارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107652" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkAYE5VCIsKwunjD9TEi-8EwnX_EVtTD_lmE1cLLBkc_RXWBa8IqUx6zrjo7w4qv1CgYgcXNRZ-63qUzKxaCHbCwfccjkOtTl1uG7mjHIctQupC7kZ0KNrPEjgWRB_YzO0zf57HYB3RXzpHwqN65sEFVr2ux8GH-IwzaGgTrYp5rVeBPW04BTkgJoH9hXBlZMfFs2qP_Ht4ng3-NgR5BgZaNe_-NirA5FkhO2IYzzKs4wYVKEwPSOsITsCIJDEJUNNfr6VZV9ClNsahh54W40rZiNWDaJ2zJ1nRIApf_xO-amSo-COilszF01Bx3GIBCSz6zGqFl6Fcg9XJBDXIv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
عملکرد فِلیکس تحت رهبری خورخه ژسوس در تیم النصر و تیم ملی پرتغال:
🏟️
50 مسابقه.
⚽️
47 مشارکت.
⚽️
29 گل.
⚽️
18 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107651" target="_blank">📅 00:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=fuyNhpH_IVLbhXpUh6lyMHwpGsV8lZJhn5c4BIfZVTyuYDmzp3CgoSit4-_8nkG-gdq3Vt7kUEfOG_wGwOjMyEjVtp8ofr3sE9Tn_aAuZCV1yftXp16AzKWqNdwvsEU0oXlEPyDijM86XV3Cv5glh-txFRCPPDZGaFi41m_rrsawhtT1nieKn2BV_CAnzyviR6P6I2axnuLWmqKVaNoTd_SK1TXX2hSuareoCx1PTUmkV8tk6MfxhodiS9aPFmlVFXaDTMI8r-3vhvvuhyfRQ7QUqQXEmWByJ72223YjKjnZ36zh2jVyF5gM0rTlOiu6GZQ4l6jIOzXQye9Ga349Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b6b9a87b.mp4?token=fuyNhpH_IVLbhXpUh6lyMHwpGsV8lZJhn5c4BIfZVTyuYDmzp3CgoSit4-_8nkG-gdq3Vt7kUEfOG_wGwOjMyEjVtp8ofr3sE9Tn_aAuZCV1yftXp16AzKWqNdwvsEU0oXlEPyDijM86XV3Cv5glh-txFRCPPDZGaFi41m_rrsawhtT1nieKn2BV_CAnzyviR6P6I2axnuLWmqKVaNoTd_SK1TXX2hSuareoCx1PTUmkV8tk6MfxhodiS9aPFmlVFXaDTMI8r-3vhvvuhyfRQ7QUqQXEmWByJ72223YjKjnZ36zh2jVyF5gM0rTlOiu6GZQ4l6jIOzXQye9Ga349Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌چهارم پرتغال به دانمارک توسط ژائو فلیکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107650" target="_blank">📅 00:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107649">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگل چهارم پرتغال توسط ژائو فلیکس</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107649" target="_blank">📅 00:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=AJGN9Cs3UjgruTwudsR9giBTK5mFtRFccPkZo4vkCcME__hNH5dLD-rkDFjeMtZ2ss4rZBxTgBkwCR_NBmG0-loVJC3RCr2IM9UndV8wLoNwF__xZ2RQ2FmMIh7LqZmlOmYU12t51JQ-4dYLhbbUkAUbp9hspQCUlxH83JOdox3w8K3yjgXnGOCTsHHQsq1-d10uzvIgdCDgSD5OxrScwEWx01T7kd2nPQQu3nghj4a4srjzBQumNcArGYw2PmakTH3h5yJH5svmZ52yN3PZEf5Ybws7J_citWf5CXv8LcZPu-5uB5nRDGf9qZPblYmoWlMa4zacnIkVYaYuEbSplA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbdf1dbe2.mp4?token=AJGN9Cs3UjgruTwudsR9giBTK5mFtRFccPkZo4vkCcME__hNH5dLD-rkDFjeMtZ2ss4rZBxTgBkwCR_NBmG0-loVJC3RCr2IM9UndV8wLoNwF__xZ2RQ2FmMIh7LqZmlOmYU12t51JQ-4dYLhbbUkAUbp9hspQCUlxH83JOdox3w8K3yjgXnGOCTsHHQsq1-d10uzvIgdCDgSD5OxrScwEWx01T7kd2nPQQu3nghj4a4srjzBQumNcArGYw2PmakTH3h5yJH5svmZ52yN3PZEf5Ybws7J_citWf5CXv8LcZPu-5uB5nRDGf9qZPblYmoWlMa4zacnIkVYaYuEbSplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل‌سوم پرتغال به دانمارک توسط ویتینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107648" target="_blank">📅 23:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107647">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگل سوم پرتغال به دانمارک
ویتینیا زدددد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107647" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هلند گل مساویو به یونان زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107646" target="_blank">📅 23:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107645">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107645" target="_blank">📅 23:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107644">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=iJ1ZfJN_1waHBRtZgg4EJBTDhxaBqCKfyn-NYr22n6xg8zN8iiji7uGYJ6rM0p4Ny3BiBxZnP9r-xdTjd4L1Fsj9NdYyiz6875nG6X0fj2k7yZSXjxHQiXnkdis2O8ahHy4WBHL28iRDmeV-R4i0VRg60Kr9Jba3dZcTRsfm-q20Dg81vOIFK_U5-fM3quUezAKBGOSOWVoc9gTZ0O51uqmfJYkXLRS6QIHPP8lMYfi1Om5Sp9D8Twok7BmV8o8WXXNWrUyX3zAj_vCRkwqSeZYn9TgTThF3xi7eVXkOzwVKfV6UeCbjIEIyfVenGOc6K2KasTMOgmEKR-0ne17lxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b7e5010a.mp4?token=iJ1ZfJN_1waHBRtZgg4EJBTDhxaBqCKfyn-NYr22n6xg8zN8iiji7uGYJ6rM0p4Ny3BiBxZnP9r-xdTjd4L1Fsj9NdYyiz6875nG6X0fj2k7yZSXjxHQiXnkdis2O8ahHy4WBHL28iRDmeV-R4i0VRg60Kr9Jba3dZcTRsfm-q20Dg81vOIFK_U5-fM3quUezAKBGOSOWVoc9gTZ0O51uqmfJYkXLRS6QIHPP8lMYfi1Om5Sp9D8Twok7BmV8o8WXXNWrUyX3zAj_vCRkwqSeZYn9TgTThF3xi7eVXkOzwVKfV6UeCbjIEIyfVenGOc6K2KasTMOgmEKR-0ne17lxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
چیپ تماشایی هویلند مقابل پرتغال و به ثمر رسیدن گل دوم و تساوی دانمارک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107644" target="_blank">📅 23:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107643">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih6aQ7H8huNsbLG1JkhyJ3ti97jrgf9EtUit0Cj666GvJL1P-BKS0CrLtabvalHQONzdutHixri33WcycbNqTqdKRd65_sYlQEYGOQUSIprH40FS1JRBU02FKIT2_f3zk4wBgsvysJ3JAdZehIvHyG9htgKaMSi3jXooAHzUKgbP_Zk8qdj6V22mEH07jjQiQnmdhdEnT6rCLmxjQQcuoU9ArRkhOwlndEUoZUa4EB_dswEddx5kJP3WvFAOfC4Dj8C6gQjBqjmn4S4eAoddTzWqsc7aalyuteOqP8khrCXTess9p13jTXVFMZcHs2uai0eBRjNu9MNzh-2IxVjqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت هلند تحت هدایت ژاوی جلو یونان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107643" target="_blank">📅 23:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107642">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GatnUOo5IvC3BqwuKigV1oX1FQLEr0JUWA1DdSA4TDM6GuFxhHCJqVoRlbPlIuVGUiUUoXgcq7J_OHJpqVzOM5sC2mheiFVP5OWQS48Olp0tekABsA7DhTLB8P7Rl19le2rAO_SfxwKdhbtgy193LM-xWN6VbwBB4QlzX9h1vdL11m4NMZo3He0pKa9ZQJcbhMxqcOgjZZ-WJ3E4UtAIIvoTdGkn1jtcqb4WapR6kL4ql3QD93UqrfMAwRxsyO1280Bw3ZYfCBXekIcU6EDHrifvyN-mOPDO1rg-TjOnbw2dNpr51PhqFEZdJH-laGWwdR2zJDeV8K4ClgW7DqMobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🛍️
فوتی هدلاینز :
🔻
آدیداس قصد دارد در سال ۲۰۲۷ لیونل مسی و لامین یامال را در یک پروژه ویژه کنار هم قرار دهد؛ پروژه‌ای که نماد انتقال مشعل بین این دو خواهد بود.
♨️
همان سال ممکن است آخرین سالی باشد که مسی کفش‌های اختصاصی با نام خودش دریافت می‌کند؛ در حالی که آدیداس آماده می‌شود پس از بازنشستگی این ستاره آرژانتینی، لامین را به چهره اول جهانی این برند در فوتبال تبدیل کند.
✅
انتظار می‌رود مجموعه‌ای ویژه با نام «Messi x Yamal» عرضه شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107642" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=P3svB95jiOH9e4AzNtcKKHABAF6TYEo7z_vl5ziuwf0Uegjt3dupxZgYUiYj4QZsWlpHFVyhp1dV-weYi4EtiC1QiJENy7tBl6U5GO-BQhY89ioMfKYemBPhbBQ3wRmeAsPXdmrGvfTDQZmQugs4KDqz0tVHWd6nDvM37fvKE_9xH_ivDHCak-m78t4vzydde-IUNIh3Qm9U4wqbo6kIGogMzZMFNRRgYWMl7XuDF3cyPBOmzDpyhUp-9PEeXaIRceuNWBIs1FpagnEQ6qbrZu83IzNgIrKNqshO9MmBNSzDboMq70IorbnPm4gxfjR5QqvcNy4_2046Ikosh3qo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069b82ea6e.mp4?token=P3svB95jiOH9e4AzNtcKKHABAF6TYEo7z_vl5ziuwf0Uegjt3dupxZgYUiYj4QZsWlpHFVyhp1dV-weYi4EtiC1QiJENy7tBl6U5GO-BQhY89ioMfKYemBPhbBQ3wRmeAsPXdmrGvfTDQZmQugs4KDqz0tVHWd6nDvM37fvKE_9xH_ivDHCak-m78t4vzydde-IUNIh3Qm9U4wqbo6kIGogMzZMFNRRgYWMl7XuDF3cyPBOmzDpyhUp-9PEeXaIRceuNWBIs1FpagnEQ6qbrZu83IzNgIrKNqshO9MmBNSzDboMq70IorbnPm4gxfjR5QqvcNy4_2046Ikosh3qo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل دوم پرتغال به دانمارک توسط راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107641" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107640">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753494da36.mp4?token=Ro7qgBL8i4Ls5TypQKuUHyeJxHFJqHIGDajahjfTQV9PTd4KelRZkgrtSgWe9qM-TLSV7xmb4PEFw9CqqJoq6vSfdhAB_IyaVBU5EbkaFjCYxLxvJPDjMr9MTpAyQ8OpEJuxV4k4MOGZBhaTYkoUPNygJWuKzcEYHEW0DT7mYf2FbF2MdkQFutIARk2WCiWV_QgK4pFTGRqcaewctSBCsJuoyUYlqCpNOiRu7-L4gvEwdEVx5GkafBY_i2VFlNq_L8vYmPmhkRrvXvA949afIvIv7g_qlPoRtSHA0yx3dQArV47ZNR2LukzWfnoKA8SV2CyCGK5IP_6_nQCWeiXG6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753494da36.mp4?token=Ro7qgBL8i4Ls5TypQKuUHyeJxHFJqHIGDajahjfTQV9PTd4KelRZkgrtSgWe9qM-TLSV7xmb4PEFw9CqqJoq6vSfdhAB_IyaVBU5EbkaFjCYxLxvJPDjMr9MTpAyQ8OpEJuxV4k4MOGZBhaTYkoUPNygJWuKzcEYHEW0DT7mYf2FbF2MdkQFutIARk2WCiWV_QgK4pFTGRqcaewctSBCsJuoyUYlqCpNOiRu7-L4gvEwdEVx5GkafBY_i2VFlNq_L8vYmPmhkRrvXvA949afIvIv7g_qlPoRtSHA0yx3dQArV47ZNR2LukzWfnoKA8SV2CyCGK5IP_6_nQCWeiXG6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به دانمارک توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107640" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107639">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=ZpkKCwa453qFHQm_jE0Z774Z2o1XrLR-kZEE88D_yYEFFZmPco0PF1H9rvuBCRZMNm-IVzTcHA35l3FQpL5llFSHhUDyjzgx7YcYE_Rivw_rH4YBtg9KsOkR9aVmRfGfxSutv3Ud-wx2D8i8BqyMrbtcfCEPX_jN9COmK-S308QPkiiJSZtlPEPEoAebHDx8iCNdjfqokOODZrqiixteuq0zzFYL6NbqpSgA3bOHK9VccvSUYmdb62v3ZTMgFECbk6CYJQhfLJSdsMiEHwctQx5U6w6MHJnHTop4huycVmL2HRT1A7mCGWb7cryk9tNelNB62qBa3AZ8y1KEGlhg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95be3e3e74.mp4?token=ZpkKCwa453qFHQm_jE0Z774Z2o1XrLR-kZEE88D_yYEFFZmPco0PF1H9rvuBCRZMNm-IVzTcHA35l3FQpL5llFSHhUDyjzgx7YcYE_Rivw_rH4YBtg9KsOkR9aVmRfGfxSutv3Ud-wx2D8i8BqyMrbtcfCEPX_jN9COmK-S308QPkiiJSZtlPEPEoAebHDx8iCNdjfqokOODZrqiixteuq0zzFYL6NbqpSgA3bOHK9VccvSUYmdb62v3ZTMgFECbk6CYJQhfLJSdsMiEHwctQx5U6w6MHJnHTop4huycVmL2HRT1A7mCGWb7cryk9tNelNB62qBa3AZ8y1KEGlhg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برونو فرناندزی که خیالش از بابت کاپیتانی پرتغال راحت شد و به خیال خودش از شر رونالدو خلاص شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107639" target="_blank">📅 22:33 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
