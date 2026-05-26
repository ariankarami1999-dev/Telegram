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
<img src="https://cdn4.telesco.pe/file/gcL8uBIkVC5EW2UwA7Z2gXl78py9aeVF-OuunAhkpTkwyKUHdJ4cu3JdhOemP6nC9bwfg8BggkXiE5KB8WXZ3AtAfL4TnkyLeDdLddqVT3WwHI1juIjcmJFat0Vb8dc2L7_42lf2ArFPiMmfCFRI6B2jOYKnDgBF7pE968zcuLvjzr7EVc70dmf5WYJcSbs2UCrx_BYnK0lmiR_EfoCiXsF9qZLr8PwZ440bkhFIJZv9Y_hojEuY_LVTmO6G4galYStAYfWLTVRLL-9EKNMRbfT-GG71QOGp3zIpTWBt3gZU-klJiqEE7ONd17XkBXAjMMwfZL-dvTVVfPNDt4wt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 190K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZvDeKRq1HYJH3WmTIqrQGFyEEmmpajclCGbD6H44ZQ8M81D5RhwNRkiCP1v3k-tNjjbFnVuYQGIXaN2CZSkB9hNsgKDyuTCbAsYS_EF_dUpca42llWmUDOQVJu0bTTPQz2jHi7SAXmWymYwZgIW7sZiIbibpBKMhMNnApcanbv5ZcEj5CftQib4fHQpMF6jeyLdr9995Mrqb2ZH25Gr4K-rPfhnVhrAg2D4RO0iIorrkRbMB1VMFbvG2kzNb45_V0nQ7zX3kydOBuzqA3qHZfwtJBcoKy1FgcSIpxYWL3DYwwJQPXRgZLBMPVNDCoqzBIg0igsOBUXKI8cVTdH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_aT9-NHlli2deICAp1dseGPytwby--7gPHWk1Mi6-45i_UNMdhO_Xl_vfLIiFlBOaHCTToAyadGnCDJrFJ5tFkN9zof0zyt6IiA6sZjHhtru0xlDTZL0k4VHMDlMKmN50a1x7KC6XkGh5VP68g-4CDXU4oHmsWW-c6cNQeJhw7Oz-tNp9aEBYotWUDvyCVUF_Cbv0UZb4Fhy2UFIJIDxNZdzAn3rYVTeUaAzk1iijsJFvqBxqiQZE0aIgGhSCV1dx5Wd8HVB4OMvt756UI6p3RQGlpstZzcr9bXeP1bnBSHCPTGnAuozO4g5TSAsOIb-BS_S-NXPWfz_4FJZ0mUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etHIygBC-8fBnduXAfDmC0bV5xuVqhLQwCmhUS4zgdCo4l0HYIIDg1VEmkX4etLOLI0UFyHOqrzT_LLGptjWS0yjMxuEfFAbVCulR96nudTcTiy6QOYPY28Ay7c2rVXo2D4p-l8OTgDvpdTEppsvBSLOlkQm9XDaMBU2AEQYiV_LAlzSLy6tPxJX2IXu1djeA8dhJ2MHBIxo4uWohvoC6fQxqFgeDIntffTrQlOEov4rz7qAhXCvxYzvI9mMlvSn1Tg90M8SOVUjgSS57ZzaK9aSNw7AKwpUeHzQa1TZ3gE9pUzhi2Hp0iDXRXsaeDJtcgf6XBGxD5Nxx5TnfuztOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3cqlhWMclppfjY4-H_u3N5m5Jml00bfb4YkxWc6O4mRxuncfP7ni3Z401bb9aMmjCcJxm33P1gJipY9VBm9fy0fEa2PpF2cWFVB105azUWurSTfpplOpdv_auoQAvNZq7VkQJU7205ztOk6ghihFPO0q1zRrl8xAD2Ybexldk-vEHCa0PerVdBNB_-kb1whH8YQlWC1Km_0wCOP8fBcMgdqf2WbW_awjQyWPzsZ__OdiwScdcE94ogvdX28BMeDOtjQL9YXN5IyOpp0VN_FpRBVPHKM2Y60HU72YfmVtx9IC9rvNIjJS6DAcXJf_yQIOxvNxwovcGMcHEfy6k4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQspzWRWoNuwZgBBzOtBNL8LX9wXXuxWASyUBou5QhGC1sz6_i99sCXHp92dZXlDChFEKo7aSLlXMd8eUixXc2AZ8aEDpRpnGVRKqF06KWDuLCf6cXSN0c7Wsyji5lGXJtt2X7yxDNacq0qEizqahqvpraS92NejsLlLyeJK8JBX1clkIroIz4kgBDjVZfAsnXTbZEf1Bl80qzfBdpwEpz04cqWv8W9n1x8ersVojL3yv4ZM02kVWgoLKRqjp9skPBKyYn6Kqq-8G2HS97XG0fU_nwDHjyGeUnuYYf7tLnlSOF3h4T7Cs_BXcF7-l-VBpBqgLuWG2FBlp7z90Tc9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKyvVkJFwJaozxOOlArXXJRDQLuY8bVB96frqJ4UoBUW41tMk2Wu3SQ8I10fPDvcInVPwOo4gt8z2sjtqZZv_csKpYz7VZiO6sSY9v2S57HOBn01lB5Er8AMQ41dFad8eI7LiNzUUOVpDshpZNXh55FKwEmYQPKMCPsxM7k5LjSbA2RFCfpMK_baWoMk1qkf29_f7YaAdh0x59gSCqFoalM8f7mt1w0sXKvVd4CwzAgJglv0QeFWq9Cu5FdaF7tS6CelZX4ELBfyZawplMlKfSR4fjguLdPT0hu52fDYZqcS7BpIgquo4kRuVjhdHK_eJUBs3RZUSzW8RlJK1UmatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6_Tk9DEABSwSZfPFiqgeN4TQvqglwTRQDcy2hpTWPhuVPnNS5sJ7BS2gh0ZQRLU4hFyZ8DyqofF4JiJcsouJ67yoxxSZGijJjz5Dhj9veWHFdA10d1w6RRnTokvuQl1zl-GiCBDb3HAeLHqy-k__LCwN-BgbSbv6aH9BVVlG_HPHENLDexe9TDvNLSfkdnhHzcnkLFPC0xdlX5IWHMBlypJEMTLxY9OZ8b7VU7IPCiIqTmiIPZK2mCOWj4F8_pUREX_jHCnnEtGOVc2Gyzlh5-LkCYmBPiPiwRDpFy_1RUUTvkHrYO-zbMIcDlZAZB-AZvuXMg8x7F5-CmeOWy2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-Qq8-FDSPucly6toQUZgL_yVE0X_Y3kvoVN-1kXa9wnb6bsQXQhj70T5ouWAA8SZSXyrA-1eP1OqkxAdnKulCR6rkd1A2kO19BQCmjBSXjUTTiC8YfPNJoItuJspShRnPdGF5EOpelTmG0imfW0adcAGxd9c8NwqXF3dHKiRAzzBZ-J3Sg6Sfraj3krdujFusD3mYU96AMcacVRI-gIcAzPCA0zJeoNZi4QlpRlPlQvSBzQyLJT1JL0y59qaNWfoVNwbNyjQZtbRfGD-nTLl_Jfzdh1KnnmMEqeYaUPKmfuxRfZN0OMj51KvanqnpM2PfNFZu-uyThTYGZdCvkEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKXlD_yFVnXpDRemOMdZ6Ws9n5DCBMuI_rXPinjdb_b6doV-KfKR1sXf1Ck7qo8mp2faU32LL9Pz1zVlAn_KL9FzkDUFgxBOsSas2pIdCrX6q464BwDH484vNUt9_epXDTUkpU0xaPJPoxi_LQLCSWFondvomYutzwurrm-FwLOo6hV1Vo_xs7suSvIpta2W5i4pDkLAxQMg5IwFShg6dc5u9BYDyDoCixtCDNmf5t7gZHuQUZw7fbGiBNNeb0a37elbEmD48RCgZl4546NOsRwEeaH0uUw2l2MARYAMtZMNCtu9572Eg3jx3wCfrvRK8erTI3_W1Q0sHm7Jy6_SOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a80nVh57H5wBzUMzRCUhUA18sWvotGfLvIQHPc00fcB2kbM5dRl-0LexLla7hP1yIJ80IbxXURdY9CSpVDyUEtrhR4u_PTSk84iMwYVcvxKnBOA9f2j3xb6KpBOGG6Bkn54ygEa1V6yRP9gA_bA-s8T62MHhluDgpqCTgCJ0YrdArZLjEtYjQFt2wQmWkCN9zkx6kRxkhVjm3_6_OSYF0tMs3gTIkgK5qU1jeyOdfgRiaX0rQnDm0H3CvfNLKCH8owU4reFvCNWhNW90Y0Aw2AlLi9g-Sgp8x_GwAUmFK5DEodm2qsiGQBNQP8XfOeczJWC_-4XjpNcaQnq7nmZa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H963Vu3NoDkrgnC7_mQl63LctZLuiTWtifOxILpasidQPZZwt9srxygykNOZLOLwx_lvJSVWz0xnY9b1LeJDN57id4bANUuy0rbtw_Pe7RqKSgeBcXSUSsPU67LNY6PTayr6_yCRv0ti2Qa7ta8e9toqzyRluxNpezXIMHO4fKm20pHmyTfYAF5rsnyeCV0hkFAZupoA3ygHlgjIhAOS7dyWigWl25gCVoDNtcEbwWvSEeTx9QcZcE-wmF41efY2Eg_Ah8u3xh1gTWiPr5OnAy9N-q4VQWF-hs_nPBNK6RCbi3e8tqJGXq9EoIvsnoqdcKDp3dfPw28o_KyqfCoFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7AN6bsQdxJwysr9W0dJLBJrzttwop8O3J0KdHYG0LVsjHGcUscrY1R6tt3nzNEAlqfzxT_wKcqL0FfRONelw8lLNqlytcMCKtbaDaagdkbTKpx2QlhZhP8mS3xdg0Rx4uoGoPUkviEqm5xGJIYcpBX28Wl02myG6VsxnKTpafeiQ2jQU5W45Ly6fw2ERuD6BnK-dM70fsjbWUGlGOUQp3lgmz_oQaA9F77hv4dv7bMvO_KDPd5aNLDfrnfEYgkccLUISeH3DhyEuFbS8AkvWFRpsMSC7ZlBGKcFPCJb5SpAdudiTDVjGwG-bRbh61vTe3wtujo8pIrolQgW__8A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbE4zznem_fH5RwVVGp-oPTx2YWjcYeKldYsSj8yFoY9fM65KuKA4s6Q7x3R_L6-gTcM_FeqBC3Hs2En42gNJsKfB3-Hi1X48GCyWuibjE76VEcTsh7ThvA5j9ZudyAeIJm1sdBvrGcT_uQn1D4cpMNJauUfwPfIqm8GkXj_2rAXnfhIGQhbii27TcAB5vV3MZkZlp92GfVu68d_AX-xG6v1QLiGR6Cq5G0c9cZJnf83gKwFD63cZ73mzh_HOysXFpRWDbwSpeLcz3XUprPWZbWc60mGmSCHyL4sk_v2jUmuj9pUkGj7cNrJRuqA0iBUgUKyjhX3WRImVXfGdsMfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CbO2dsaWuXVZhivMfaYEGRe6OpWAjcbD2FQGTafrObIor0Cg94odVg_ssYDhwP5lWZ1nFOnBfSsNU4n0cUdRFngD-Q-OvdGcuif1BPR1PZPJK_vvQi7KUpBKpUwS0kBVHFgplhnYFCBNQ86elGAVP7zIcjnFD_px6lj1TzmFpoxeZl_eWPbDhFDI_WrWw639btDF5dBqhHg-kqkgZ7BNT7Re54HTp6vehNFO33knbnWj-74iHS77cbU201LL5IMauZ0JofMd7N3nPY9JMuPxLRE2PtDZT2NoOkCuZBd8T68_cDNq0gJwmfj1tqyOXeGOfQpTaQeob7L3cY1XeFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi2YQi4itn-FllnQfH5IvNYEzGzaGUVg0-u9f-Hvow9e_8qbRvktZID8dI4GDTloOHwrec-2VsbNaN4Fgi9_p9GubeOASV2151gYUbsLvWdDtoxCucXz-i4HfQMlkcvlGUUAmQX6rYnf8br4XJmJbs7_eYH8axIKefCmhgrvZqpp4ldvHByQvwzTYZ9u2ozyXeHyogJeeM0TFNlGZUnUssqZBQVE1Vv7YeJ9M_6FS8RGQAy3nDMfg3-8u25F0xTQFIxwKZ9gsyezWzoIh2IkV52r8qWUwW17XmQN02IBcIJ176pk-O9qJbYwlZvcB3aZP0g6OI4uqhkCxG-PKXp4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5x7e49rfT_SnSRz9-vILzKHDfmomYQBSc7g1PL-MM4Sa4hSTtVriEd47jg0xW4YH3OmBlUi8v44fm7CznYkh8MGWBFN7IDXW90EnNXQA58QTHtLq2nCEMn2zn_q2WfEWyHvosRiNrQ-aEzvt-BYM4b3Cby2R5VyFeASbMikwTZqKtvfyWbNTW91Cg3-xMxu3W6jivyBrtzR0IU09Vhjy7vV-zfvVGxZg5dDFySEUYfGTh7RmciKyIyH6Nm83It5ftRkbvUOjt_P2-ZiT6yGwiKZxppLIr2bJa9VCim5HuxQuO7X8IU0dtv2ADo-cUNs0GRdgCyl1BEVrzZcHDCQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezPb2Rdx0_fjpHfkNubeTjt11m6CJWZg7XQayGfJRHdU7VtxKDBnWikj9dBm_YuQjihC1OBeoeW5moEpdF1nF2hy-8vwUspohEei_OQ37brpGu6mz2cUkmjrS1ADu0OwxcDdTRs7A6rni8MhzYfRs82UWR5LOhYBZIHP9nHEzPGUKUlYUFKxS7z8drUBkkzgptUvyC4sGoWVjgkRNwseNpXgpSx-Fu6j4gX51QOXk7EXuVZk4lNUYpwnoWBrJTF4nB8QLbyteCqLor9ihYBGwykcCZETZgJT8QOMB0j91y2cUwJi0sm48KCEV3E2zXSALuneQfd1WSk3go0w4N5bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVaayHzAqDFVtNyaLQTis1TN4YlpiLA5pvTPS83sJw-GhOdRkNaKVGxLQAoGTpru0Jlxj0TaSZpOOiPGrIDh73RzF8Mcm9xyga_sx2TGdYg8_hUgfy8mNys8UCX_sZs4t4v_PtkK8G35oNTzxEdpIYcFU0LTqLzGIadiaVYl61aT4QTI6RuLpf5AfE92P-61QiQC-qAA49MCq6WVt1sqDsEJngoOCyMBAvWW3JnYPvXzuNIss9BX5VvQwbAEkAio6K_9j0QxLIBVa4249952r2nnRH3Ie_d91MT0IxmPyV5YmdkLLglkONTl5wt4ErDNY2Ofwu0_-yJlpxqWqwN-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb3XVmvW3D-m63EgD6KtT4G2DqS5cGH8Sezo1nt9cYcIANUKD4sl2jor8ZfZcO0baXETvlmA-lXCc63RsOn7k0ym__gtYhnYJEict7DtQgT5m89r5U4FXEk927nkDTsWk3LsTeWYxSJtHdPRIxR-yJ4iKqB9YgsFAHSMAx3P7pU3A0ftgTBILJbXFJz9fhSaqW1iLMse6eEoSL-KwfGE5v7wkpyUNth60f_6WhV3P5R6em5ZT3VaCdbTn3g6dTckYxoP_qlYy04yrVxU44J4oen1hDRH7e9XR9sdNumywJ1c160tdnoNWOQYhVPZaQxl4f5rH4_yNSypGLNKzLafNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhxrU5QTG612atCm_ShCpV7MO3cVnJ-14moVokUjbdz_6F7I7vyQWTPA0zSXWIS7iESb-sCVwGpJCh1G0KGHZuvyg8om-FyPP3bcnpvDOCVupX-n3KOeAdbh38n5u_0kug9SJR3ZIqsz1Uwe55uHUseUiNSZWMSIEozM6503zFE5ff9ImVm6LmsQje_WatVz_nbdtx0nSEP_K1bbyt_TVheIPA0E7GHyM7ebg-ltztR5S-M2e979KlWIaIaml2zRKmZSHt9x1ibXEpGXsJXxvg_gP3gR8fjpRJ9JgSlSMw7aSamcMJzm0EZpPq7ZpQjIzxHFfNHbbWIXPrKCJgLpiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngUhi2lvlXvvX67VIfABfpe9qaN4QgYGjAi941NDO-cPOfiU567_-2FyYggnNrJfpty7hA3a1aIGto5s7vMICyDxZe4XCZlU-Fpx1WbbRJGnAUMYfrp94-P6RR5YwcIuomNbqqebNc4322FF8AgXuYM3u-ZqoGW5VpjSQshG0Iu1yGhg7CgAxBjeUvrNAG5p-0jIwBCJqTu0L_OKxBj6ZWseuPP5H6M8dZKHKOGeqz7Wkne13ZC-VN1a2aURf3FPWfoESRC44sEGrjlhJFU9b-0pVMRHSTioTZCbJ7Lz5WzkOeaQwJ4Vu2GTa-TwfBivIRFn_HpQVWLkYLA9CbIBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K65vnVO0lFjWgq9-DtFKMocXa5GM8gpMi-5fi5rAZFIX-0O51vC1xkC9nO6ru2rrFDbovmER5NmYp0v7cPLmKx7ZHQNXTglJOY-Uk6RmT38urfm3Mm27opU7J9EqMyi6Y4ttkulzt-M8iTvpBKV5zEwbX4yZu0E4UwtcmOyTaPpXYEObOnkRV0CG0XwbHIkWmyG427ZxQYE-wh1gP1LbRhIN5d4fqPtZp2RUnHJc92i6ZE2SLUTJzhOg6GmwaWKppSoxjMAoKu5Is6Ehy1hSKpLsP7EJdCEhyy1w3tabzbg5ReQEICoFePYTmaiyp1tYoDJWsphqzO8AvUKNLs8s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1d2f3jirUrt-olHhwm6HMPYUR_9TgaadTAj2gZxaPcG-r3PsTsyAbJE85zhuGs8o2JzJPYtu2W6oHitVFan54PJdd4o6ArCg5GL_2ZPYrMhlwv9uA41Nucp4h6WJ1L4HahXIFg_2pLvBoD3HzeM7vNlB3x35xQ6_oc9dV6-mVuqtB6yyheGw6NIxHA-uwIXIabwLeniN-O8VOuM_WkN9Yw4x2kCQylOjRMzaux2cqb5xvw-krEYcR1AObrjvQ3fSGPEaZVLrEfv_FjvhAhMF7jsYY_u4CNt9I1HYJ4cKOyDiNaQ8TWEZTYkRiIWgzp1-PZrF8GfPGY7PnS4cyULfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdRkhaHiZXjhJSrl7PTtMv0o3v39tKU9tpzfMnIj1DcDuaO1fvZqhkk-T1YBT76HYEUeD-e3XC8Ma7M6fLyhybRXp58pUBfrMkmm9aC10ghOWzYQ5-HiCTn-qqV5QrBsW4oXUCVozgVHBUaPKj8JbNQmHQAkS0XAWOfwGXxDr68VQGl8bIbE9DildBpqmICcY2CjrisNS9flD3PmFLbZPhbQl1_Mu9tPaLXyNm-2sDHYVzhxiPrW8k8fXdNSEPDaniJWPzIISjeLoYDjGp8x2O42K_qg_N0ZoZv3mqd6KlOzd9d5_R22zwChrq1wQDKV7jf-e8ODTxYUHVfjcS7Q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHjcN2152Agdkq3Yx0mxX8AHrbp-wdQuBpqkn8b3IXVBNk4_wzS5BJlMjZlYQUAQ0RvCjNhzLt0wY_eoJ4V78aeMNsyYqq9uIjUCrwUmX7QW4w6Ss-oY5HsYx3X_3ppoYrk12Lr2DU5sOPjCCOqgKp0To77cesakW3VocleLAPkmngr1SZEdfPjRQvcBlBiB7i9Ns21BLRYeFO0Nj6FDuEwjFFgKw1-uT2Y3WRjv8DjjIzORkldEkuemvGXnAlYWFCOX79n2z9nuocRfo-Jx5HxDBNLztL3dghy5v8MfwLq5l7nfpjVRg70-rJN-X_5ZYhjKe1U8058wiZ952073gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWWc5GewzJ-z8iilU-dOPJg5RI9QQJ6Jbr6PIIWTaNt0jWxPqurSr3Mdh3RAKOm2Ihi0BpM1SWSdxLMW1rGcRz3IIefHp9F08rZG758pb7FO-CAki7UaDB2F0zo-rikG6x69fl8CirQlURXTThm-XCgBfNa0j7KMl4pfBrXYc7pa6GZLlGOlr03yHt1ZDJ6-4Pl6G9m6JXRm-HfHWOdruT5Kezq35iCNqJ5FwF-pcZPNY5XgsfR8TMWxoivm8jD2frdy3NpfWhlJwKZ3su-FtbaXAZr7gkOpDCpSvXMnKlngvilUJp98yhHQEoAE-rau0K8IUTL7Fxge2lAVG0pHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dumVBbAvgRToD7mKCClr1A2jloJ0K__SCZI9PQ7w8AyiShoFNv1EM-FN97AYGhlWlvRpKyY3sZoFHgWXosCNiu04QqjCjEfL5JE53ZoGu-MzRCLDZhzAeZVAX-vZPJj5qDSKJkgiKQTmR-2ElQqMeFEaPv7eLo7JRpRA2bhJ3oA8S-QE1h_FYEiR6SzE746ABLp43GoD7L8-1VSfNvfitlEPxkypAnb2coMNmPpS5NeqoZ_XpRUpQ-cEbXkq6xd7uUdkAixAMwF3U-V98sEuFLoeANwRPP8o1KfXqLRQGmCPhzI73TDOpGywGGo88lP2ia8IKs-2GdGwHd7HpaWE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKbDd7vTPn5sGMd2J4xF0VtqznpmGXyUZeYpEd8tf7KM_WYJtIoe8nKwdFxCE703jf7eNjLnYWil5yLJSwhoak28kN0u1fqPqhaTb_qmngAMqwMtRqAXvjls9fXmfaWFgSlcdq8YnzrLmTtcb6BSGkI_ILWX4cUjv3qTOsO0zrTf5htHRFznAlEZnsRtAsqug4KI4EhAhdQok_XjfyUl1F4tlwwcugJ1bv1MXHSYrdnfkADI-q7zo9Qp-Kjx1KCsTo9GIdLDMbdOskgcOgOwH1nJMqcf1LIt9LK14tqYBoThgXvIIJ7dULuGbXqc2SYT5-bnZYrnql88mQ0zqpavDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPPzEUqEX0nm4bzKrMaJmH1CJ2sAyADWa0qTK8Qo89hYXYikcm_uuTl6RubR7Hohgy-5kzyAAtoQ-ej3hjq5AG6vgRR__sMaDypjgmWI8I7DUDO_X7jTt7Ri7hTe9BN-xdjDvnqyoG1dWXMbdGzqNPnsJ5NZpgF6ObNh1h1b6TKypFoxoLc01-SqgwIOCGZgqP-pdzi7DvdqMnEMoi4bZEG46btYSXKQJb6TNK-Uo_XkA9N6OCShZGUdrw5Qz9A6NcUQqcOHB5M07BOkV4PlLhInb0ga9YU54n7WC5wo2YWrgctTzj1LTB51vlUIyoejFTUovRSdjBCIunI1iK6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNjjVU2AHyTSXYblKzSAt-Rt__genpOKONOyaVswIzIUNbdu9ejIGxgHzfCIZn6fpABZ0Bcrut4xGOzjycpqnXcxBe8XJD-RJSHQQIjBwhLEx32gcJfvvb2I5FfE0IMeRHv0qbSeB7KwG5bzqvMkGNebqNwEoymZEAM22euAAG-bg-Hv-pp4yagb57QeEcjX9ZNnggy6CNe9CFelZIxGqVnKRPx946DIJ6DFlsxAVeK_LW-pGDuL8ZWg_AqLQilOLnGYUPv7iPZreCT-j3FXlN1ubpGuFGwnmO11dAtNQA5bTVojn-VTE6RGYT5sHIe7HfcgYxsdeXxk5MoujOECBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eboCrn8fSJAiyeTt8FU3WnEIi9OEBOkE0M2Bbw8CihlRg8ul3gUjlhtIF-5fwdb7zyENhTbb_1mcJXgp_cbMWMI629q3LaB49IpoZWjnOPvsdKCtdSXoAFXijZoLNjpdgrc733KELacu2BpcljO77uz7Y7pWaE0tFRj_RT_tNkk9iO1aadbmvdRmYvS_xGsCS-Wj_fyVAFfzFXf33og500XLRbpouO6ETOxempj7aeC86eMgubzxjr8c_xRKx559gh8nxZMN5bKoFe2U7CYXBi0RnL2-VpI0myKAbDY86juAgpEJs1phUcz56m11F2bklE2Aile0VzlweHp7kLEcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVUxeM-B5Ru0XIVJWQJ8dWKTEo2PBlTAl2sPRdKpNY-pjTHku_1Y6Gr318fHj-ZSqnoBhIwazK5R-r-zQmTTgcrWsdGg0SEFI9AgoIrPtaHGbGpnobhlWCQCVFHMvHntAZ3FRxjq5yCXqFln5UyDQmyuDffgttHPkDDr78RQeK4_16nOUap-MIrxvzPOT9K-VUMOa51jg9rry784ARIB4VHZb4yAFdGiqRPWPD5bHpUyWhV5xxyWNxSpdhDPwBWKDruTw9-0-oBkWL6vTJCQyoBBKiHhn_MbzbGtkneANnpw7kM42Xdd-M9uW0aqJ-qZVG3Bc6uNU2bKCNpQrSnyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4UEPGUm2UPK_JS_cRRSpZcih7WOWKQzHDGfWC4zWCFdSMmK8APRv_ES-fRT0nytETaPIjqTMa4wjKnzAJ1EW1cksRR0iFuw1IbnpI_T1U8I1U8uBBFznzehmkTgry6xNxALz8VVmOiZvlP80Oj6J6hV-Wn66OL9vwuObDh8Yg-AKj2pisEw0qbBB81y1E_aCJjGJThjEo9Ez8fxGiJ0p0kMnT_GTerid6yMsNwrSamPtf-xx1MRtsIrt5Jqhws4o6Mb8wdWSoGAR8k9O7_XQimMFhGrmygqENaC9bbzj4ygUaJWSNQeMGqV2c6qwUq0TAuv9dsdGqQt_TrF4_69Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcH34wb_ySQNkWpJj5DYHug_tkWjhv-_1YZacLsKx1_-ar-kIfNjinT8tNT77Uy9GT_Y-asDDs_Ral3AeQ7tpXDLJajKAHMBbqNFasPUlRBALNgf4iw9qF0wnXdc-uKWj3tD5C0289NgBa6lPU3XZYVYqjcWr4Lcpd5K8U9cryEveg5dmx-q_ZfMx_NEwzdPA5iyGYUaC4Wyy7yfQpUamn8EKkFdHn0OFbk-WVtIXolAcVaLbwNK2LrIyTavfpwNkJMXl3LbEw67XItaCBAWICX1YLou4mE_hwhjMMPRh74KkL9jZqjV9njCzu_KZacN432mrsPMfbLxKWouzufBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_JZRYzz5dZkTqF3kcbiy6o3wCiQ4G4DoarSodsj3ZNQ_Ms9QZeNHX_b3GdbsyNmxsw0hzeETlp4dJnif-Lv6USu07lCHtrn3qcA7OBfi3GUQk2PX4-ZHcZZm9mkMtbiIgT6BIMv0mCWG6t6rgokfh4sSqjiOUd721ob7kEIJl4CapuJS12Uix8PTy9ZM2j5sqvgcG9psJBrsTZW2almDgHQrlPQmOPvIzxa51y4rq0SqwsHwvzupUfRPH8NNUGBf5BMvj2Tr95FxNXTjsDmtTTfuj73uiqqyp5rVbqSaUE2wAXT9jROy_YzrNaxZBa6Bo5RUg_0sfJPYZG-zfXY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxduazOzeU621A30s9_hXF1lkRc5-_NsLMFi9omTMRQ7dvc35HQqR9tWUf4gtssmQo8jYPRFgnaGDZAy9FBkgkkefzlQDQLXATBbjNw3McUsGvb8BDAL7Kv8YA5MJEmKHiw_rkJfeFhT2C8IxczYWUvNLtzzLBkka5Q19wCrjXBISp-VsQJWMpIwDQd-KY1CnKWtIk0nKWsQmTAXInU3guk3bFJbLUJBOiS-5BjM99gHrjLSMC1n1F0jABq0TZZjk6czYjSHqQWYtEwBW7ZX9sQbfTYJ3Vr_JfxtzScHZLRLfi2yaflQTITTeZAyHEG3Cl0HdSG37ZIGBtjuXlEg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwDPnBxdMQCTT52-i-sGpAYX3PSEu1IjuUnkzpa-wn1LM2uavDkY-Ovrg5D5Qu7NMrBC7TFNzkDoI4c2fynhwlIlHTuK5MC6RCABrjgwNiRV7Kw3jhxae6-G8iHxTYf1ZHWiAjLkha1uiS7p5i04a9a7dNRz39wruVvoHPgI9lkDZWqrF9IZJ8YfgukRpJg3HH_cODRB3rgleqzb_mqeXvtH1BQotYP-aPdBJDmi8Xx-sDAkFugwjT9GXyeqm5oKB4Q8udgR3QHY-rOChc2oCZkyjLuc4tGhRPyogcMKe56ejjflHA5gl995ClVEozE7vyMFtHb0DbKioHJx_mySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjPXMtUwTnCEkDUweS-__5PrY_ypKoa658BYFxtkK_wAhsFcQwYpImFPuMtVrf5-A1yRpwuzwqeA7cfC_Sfh62x4WqhVx7X9eUNnR0G2R8-290_Jfkju2ATYjcRW37fAJg9z-J5gPxnyiOPZTe_naDaB2q7LmJF1l_-RetUy-dkvpbuEbE-8zS04e8X_WQ4FB_FmRkcYBeD4jGUs5YWPTTaHdKEPrrPz32LJS26jy4asyjZv3Ase0yFrKwkbSZ0nQsuxLLS3Gte2P5fdv__Js4uUJcM6IjYFK5sXUpzzmAOtle_pJuE6DbpBkNYUnP-EhqKFgo7bL0iTyTGENTY_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY1I9x7Fcifr6IIPRKUSXU9TwGRHLeA6-Za_7wnpHINVJIUgauqg6eQnu8JiJpBIP6jB2xeXXlv2WQkRi4JHMb-Ut6zD2-MRoKlWfwDzHSvLvyj95Rd926rikNK4JsCmNtSxDH8hDemxdQjFPfrDUKkX4PlQhWqQPdVlqE9z5zoWsmQGLPqiwcbdWyRTXwvnN6O-7qjqUMUVX9r8CM_J5HKrvouIBKkg8je_9-uMvC7iANp6Hj07ZA2k7OPbUhLXL98EA8MApZH0t1VcFGU1v7b_EIiqLnpn6lScJmwy5aVj6Tr5qZ9JKqMkUDZpxirGybCuGe74_7DXSEMYLmnjSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCF4oAk800zbsl41e0xuxeKV9mbOQsTOemA6-IkFmcBors6sB2EVW7WDzYf4S2rOkkXjW2k9OLT3cTFK7_STFpaanTMkpKXG28SLrWjEslK05PS7824FqZHN9IfXEAdQYNfADW9U_QSpPEDPXgDeZcODXI5uTtQ2h-MFx6X889IzNm5LQpSMKkJtN_boOB2dEl50u3SSyRtctSJ0FL717wAiHdnnlctfD5dCpQNihkBi_4hhSfLGf0kmHy4iNcT4ZdYX-DsGPsWQzQpbgB_STioBlclSBkg6IFpEVKfynZDDGpdgeGa55_uplQcoNqD0zhEt6ZkH8vzHeYKKgpMFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng09xiyUhnvVnw1SYnK5HvNLR0FR4ZH6KhxYIwM_g3U7t__yQfcSajp4QQGdqztMjNVH_EvIUtQK-yFsRe4nNK4MdpPkkg3HHtRfGkVcJo45yEr43sBZWJxtPhGSxPnt4Q-Q9Sq9sEuDQfmMzgdH3FkZTOOU1E_WMW62-Nf5SgtaTksdwrff6AyZlZgFamJmWCksSLu9Zn9_mwDrm0_M8JUn-hsKzpX2MnfY1LcC4sfEDm89-KH_uLlAqgp0H_kPB79t8KDDdpbO-N0kRXSonHFKNvuX26JAB30OpJJF_ZgaNQY5I0rVf3tmBJH5i7Xf03wLO135eZsP1PjIOyG0Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCwkuLbJZ8Gjr0b-V4U9QMQxPXG4DsZDtY7T75Qo9mwAnQHP180mlTJ6rBgHvahXFGSyM4gIhRVRSoxtGM1QVqBQ4jN9i22nfS7WuJjcUr2fHAdT649rUTyxkzJUB1QcAt13OqGngcMn0nn4J6EkAW24UsZRyju6HFVuU4M5jGPBQ7uixD-5WRv5RlYkliBetQS7ce5N_DQi7aZBvot2a8X95Wg54Yad3AqihRS00U1FxDtQ3FTBsO0xejJV9ZynLmPF8ucZq2HbRoR2Lp2MH5hZ1sV2fpg0eHEICV9veJa1vIk4mynNUM6spwgUZ6CE3sMqRHODVKNIK7-DqbiXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgsmR9h6hKlbWypmxvD0Jq1lbKfCK9ok_y9kftrvpGRBJ5Le-IbNcZ5mVOvLA_rYsbtVj1c5C9AE9VjYdNCFNQrnTcDUP3E3wFL4P6rtFEF0AnWA9qNpUMhe38nRpvbB6FNbiWYA0a7Ch872MwOGdyOU97-vO088gauPQKD8giedK0C6MkTrP4YVr_aNBqOkuzXZQFbXLwN9J4EwjygKqzwg38y69lg0NNHvPKXmcCoPyBzXdst8N8gssVTmNNztkE30xmUk-b44vL3fkESx0-lAv3_msKQPwp_kIxA8V7CFy6xauVZkLd-XiAYg07RJ0BB7Ey74sYZz1NNZuakOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK0Y51_Tcy9vHZA1EcHZ5BbkAZ5KPu1YJvdhAjeiAGpxcd5jNG72NFUww0KCd_JTndF6gULLqkICm-8FvrROZidbsA16lr1DLo9zMvnJ8_CYZKaXOufhVdYbOP0r0-fIueLnb6poVjrekDAJyemIgIbqaBylpRBhDY8OAWC_uu3XS7zF8-w0P_kVMLwbd5SCr0hEHMO8jQyzuds4vjE7RYzDNyyT5B0ZxASJbEag2WwH2FurD4oJbqgap_Z58t6PGipOlpGjIcG8aeN6R230d11qEcQhiaUtSPMB53FZs8k2IvRZofBPkO0NyvB0TD6QVUAcRSjlD2e51fkzIpim0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxnY-2BVcp5wCSme3Bo5bDCLxMGVbIA_fgMqTr5PiObct2hH_scY6xaOBpzCspf7vv4vD874ESPbFNTXY5Uj4X4fB3ARDT8uI0mYzKThWkRVYq_VJXcfdBOOQlhKLVMY8VuB2L3gZZXgi8uiD3UOxq2J2-tn53IZfuEDjDjkY4dhPjNGpxYdsOKO06_hT0XPxHIhuPgkqmlHF8cgNTR9scAB6uWfsW1NeR9uWvwxfkYShjGSyS_WJAVJhI4KKIj_OuJydg2rXLy96KsNJAQXjUvDDr5XDig1g1Ct9xwIWM597KbW8cysXDWyd4hi6P8PcJxMvWUOkrMQNwEtbEHkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1XSbCIHAxW1D5Q7cfKgK8rT1znmRMtkyRH6HUj9q7u-on660S0OXkY7RWJJJhVRKpp3-cN_zTi1OojSrbqQ3lMy7YpyDWQHLKpqkw2h2gv8wDCeqiqgnamP8i1Iu8Qgd5Y_NG0dlC9XkRKvUytJJvZb05pShowr5PLiPgoe3IEJB0s8r3H-q_HO-EgH3O6XAVW27PlJGRPPRy-7KP1awssMtbGYT1d6I3FL3pWvHM4VbDpTvQf61Na83lKa5qfaDKy_Va9SXNlm05no8MikFzoAd2XyaxIAQMxdrW8rWXlNXm_xwf5LOxAuERT6Y2lkdizU8mJJ_EfLLJpZvJYXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDwUy12IktqiT1UPP47dU4T4A8q7xbrrRI8nAlgwnh7qfaTm9xc2b12VfCZDj5a7WXeNF2dQaYrvesoSYs1kKb0KBWq9ahlD5j17VeDpi4AW1-6i2qV1VC_OjnALPe1Fqz9yVY6Eh_FbaHcja3PzSnUiDClgAMsekygutuly2kPZqVEQIG4X5JwnTUbUDKKl-J-Rn4N8Xm5PQYtiHqVyvaTAMdS7FTOf996dZhnj9ZrcGxJ4swhWFBmPUJUOmaL-PiPjk3hnJ4lDM92fWS0L4ol-AZkMhJ32TQY7UstzjLSsfNf5hHYrLnFFcjXp5BN905cqJmTPCJXdpx_Xps3LvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vo9K93QfawfoCtuU0jaLf0vBDT6vCgyR3Ul_aWydMk1ZIuD9t9I8Po0yQKH4qVGAqyo-ywJZAHhuyOXiosfEtI-sbrrNi6Wzn91E6Dm3MUB8Bnkf3jG9fHCR_u81ibaSeFNznz_hNm79psRJrbMskQQFQdbWG-ySM_g2zPf7HmjBAFGxXYPdptkL4KAd-K2K5e-FJnFBlncSqexyuYa9jYuVBsONsa6CBzvjeRUz4_R0nENHLvmc3sQc5Q0bnGaKp5P_N47cXZac7-QNzictPwMyOnr1Yql-XUqjWxPON-VfYAPXjwB0g8rRyO1UoOhROF8dR9QVBuILv5vJYvVtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8OsFfzjycOO4YehhCM5nhwD6FqiSj5qYHJwguug1gBGVJ7RZs1PvTDfFWx-hyCdoD99CjwbVIK_4eZ7jhyvvd_q52nZR9HVnJrhfIXEew9pKOPe6u8ft8idHngSVFvZ4_LlSWYt59nVhhL4_OocRtR_NiA_dDr7EZj4Lki9_mdO0OSzeMFt-h6Jd7eQx6GtLrrAy3E9jrBjugCrpp3KS9Yrzm8l8XzfEafG4wwK4a93tTkim5HTJPjrqWPrh50_HRVQpHwWrnC-w3HfFoEVWLyUREOwMRpD6bbVvXjvkEbxh0R6AvUW2EW2fsDJFMjXEkfiR8JAN5CRJQxkK6_0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOB_2RKZk1ceRxsRheXyEA4aBZQuuOoYxtV7HSM9iie0dHwAFHrfe1vque5fRnLyqBXkfLcLjZcTGZ___jXPzNMBvxZCfPapf87eXSmQKJ27lIZ1_fTN_MyisK9Tu3fTBCuPoeFVz9tktmoHvfZZ17W8wLjCFhxsc-0i9PiY8-5FrfLmvgq_m93tUc8SrVVSobWmqBP1fsQ4zacyOQBwrIIK1LiOFKGASnMW2Hvrwv6VAHRh18Owzcz8HMofB-PTtRvF6HJtn8DA8JfhtixS_LOSG2L4LPY2lfUXcO9hjhOiQsRCTktrCWLaldSdQ_fVItosRp-hHqs5z0iJ9KIjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=J2wYEJsw1TUX4_0npmGI9tQqbi_2F9kPGiqoXB0_DXcpoce8zRSNPv93yojVKU1rivajWjJvV06Gt2pd12x10Kn3yEzx9C5jH2WUmRItU-Q3jWqPz-2a4Jgrh115jTbN8dEpk0uASip-TN4dN8mEDC2IedhAKDW_iAoVVUkfAZ-jm1TNcMgxj9qafF-3b_I-oQaA_Oq0mJ9-oZvKrcQJMJV31LrP7wbjCj7T_wGrh2YsN5KpWMSOao89kI4AGHznvfaSjSQdYfp_hXBIp0Y7DVI6fxms9gfdnWB7c5dpFXfPJJxsIjtJiYybts7CFQInYiwyL-iC3r0O69kvFKbKDi0vqIcP1T-TPYg3oaI6Ssoe8N7bbVAcB46koRR-R8Jx8CyvTPFmzCIv5wf-c07N7SFy2-gZY75mhvafL8gQq_tTtfKB8Tx8nHiWXK-YgeDAWZ4cRrWuXcVWORdzI-YRvN8LHz4NvGMHEUpylj4RVX_7O-fbdHh_bLLN3ufDy2shVFXoGx7tO6UUbiECfVkaRm7cMVUa9fMKkjarrYGAOSZ2GxIsiOsSiJOXrTz2BPFU3bU3dJew5cyFB9-6JjEW2Vg-_YDFeYjrFN7J5tp9Sn5UDyH-qAQWpkRG3c_Ws6PoM20tGKmhNP391sO2n5i1RC8B6qVLKGtRdhuHvTlVZJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=J2wYEJsw1TUX4_0npmGI9tQqbi_2F9kPGiqoXB0_DXcpoce8zRSNPv93yojVKU1rivajWjJvV06Gt2pd12x10Kn3yEzx9C5jH2WUmRItU-Q3jWqPz-2a4Jgrh115jTbN8dEpk0uASip-TN4dN8mEDC2IedhAKDW_iAoVVUkfAZ-jm1TNcMgxj9qafF-3b_I-oQaA_Oq0mJ9-oZvKrcQJMJV31LrP7wbjCj7T_wGrh2YsN5KpWMSOao89kI4AGHznvfaSjSQdYfp_hXBIp0Y7DVI6fxms9gfdnWB7c5dpFXfPJJxsIjtJiYybts7CFQInYiwyL-iC3r0O69kvFKbKDi0vqIcP1T-TPYg3oaI6Ssoe8N7bbVAcB46koRR-R8Jx8CyvTPFmzCIv5wf-c07N7SFy2-gZY75mhvafL8gQq_tTtfKB8Tx8nHiWXK-YgeDAWZ4cRrWuXcVWORdzI-YRvN8LHz4NvGMHEUpylj4RVX_7O-fbdHh_bLLN3ufDy2shVFXoGx7tO6UUbiECfVkaRm7cMVUa9fMKkjarrYGAOSZ2GxIsiOsSiJOXrTz2BPFU3bU3dJew5cyFB9-6JjEW2Vg-_YDFeYjrFN7J5tp9Sn5UDyH-qAQWpkRG3c_Ws6PoM20tGKmhNP391sO2n5i1RC8B6qVLKGtRdhuHvTlVZJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIvbNxkVNmH8piLvyWLDPVJkOAVeMruiZDHXJxmsYizBg00lytbOV_Whu3Osf4uwkjhcnFhumgAeP7mwZnRvOfzmERmI68VfOk0RpmBw9EFSaBDBT68Ep4Ax5BxRev3wLm2Z72vinQ0DXidIg2UJZN7mXNvs0ey5suwr8BSRR81J3Eb6F4RhYPlPzYvAEbvTncE7_aPRp0qgsXu0ESDSt9O9cWWhie5TDL2r2gxhx21qmfHwDzQfBOqCXot-zx0qoxr7yY7cmC4xua9xm6oPYBp7KXwS-gN9VdhdhlQvkV1wejt4UHpHdtKvK8b4JoAewg7tPPQv-RXiqrEK3waVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=Y0qthJqPaoJpXtO5Q2HwC9GvGHO_zGf_OSV7WbULEy1NeBooh7Il4A_XJ1lwSJQd_Mw4O3FiZrGvu7BGgdBbqXurAwfut7DFX0oewpQk48Dtp3wwbvwI1HqP5bMK66pHFmX3FcYCnvGfzgaRsZdkS48R21an2U6qgsyODN608Goh5VLhhzikZJd0ZfHelagMvY54XkJCFMCJ7SRN1FagaPKyIxkxRmmKIQuo8w9ZpjR-CndbRCvczKnoAWyqba7jRvvvhQzYkoMHXFROhYrxzsFj0shdwP495sr3m1A9upoSNeAqArHVtd4SxMRYeNTGtoZ-JpBzPdh2byoIxsrIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=Y0qthJqPaoJpXtO5Q2HwC9GvGHO_zGf_OSV7WbULEy1NeBooh7Il4A_XJ1lwSJQd_Mw4O3FiZrGvu7BGgdBbqXurAwfut7DFX0oewpQk48Dtp3wwbvwI1HqP5bMK66pHFmX3FcYCnvGfzgaRsZdkS48R21an2U6qgsyODN608Goh5VLhhzikZJd0ZfHelagMvY54XkJCFMCJ7SRN1FagaPKyIxkxRmmKIQuo8w9ZpjR-CndbRCvczKnoAWyqba7jRvvvhQzYkoMHXFROhYrxzsFj0shdwP495sr3m1A9upoSNeAqArHVtd4SxMRYeNTGtoZ-JpBzPdh2byoIxsrIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_3DEZV4xOgacv2lGaARDxKpUy_2-75z8CxB5Qr7Kbc4CDoFBilwBftxswjbe_ZrRlbnnGh8uZgiXAKs5Az3X8SfaavBVHjIQj9F3wHDhNowr48MofihW_0G7LcJ4rS_uXdMP6t5zGr0N3p59hILj3mV10irSVrqnE4YAZe6UciUzJkh0f476UV-BF7sAApfVFC6k_-us1mMph-ShqQOIaYg8mUGZRAPH58g0iLY_mVbutmfP_i19WPfO3vQwqXPLtFO9cnMQ5x26-xa3AgIJM-XzLtVFzKkBW3mB6XoxPj0s0g9ijU137jlC7LqyoaCc_17Pk5zcJkpTjY3wiJawhVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_3DEZV4xOgacv2lGaARDxKpUy_2-75z8CxB5Qr7Kbc4CDoFBilwBftxswjbe_ZrRlbnnGh8uZgiXAKs5Az3X8SfaavBVHjIQj9F3wHDhNowr48MofihW_0G7LcJ4rS_uXdMP6t5zGr0N3p59hILj3mV10irSVrqnE4YAZe6UciUzJkh0f476UV-BF7sAApfVFC6k_-us1mMph-ShqQOIaYg8mUGZRAPH58g0iLY_mVbutmfP_i19WPfO3vQwqXPLtFO9cnMQ5x26-xa3AgIJM-XzLtVFzKkBW3mB6XoxPj0s0g9ijU137jlC7LqyoaCc_17Pk5zcJkpTjY3wiJawhVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFZalO0khM6fRUtDWPGG47hbNXPF7JamX2kOTfd8vqJEIgMlGvt4qA7Qgt8pIVJJQAHQC_mUHwOrt2OMYhIP0-2QkVJ-3SJO9-M7dOiQ0PgBbfphQWOd8Q3fTjcWXNjZf4XtUOqynK9saCmvd1QV_VhJFZBdqvIAKr8MVFNqP9RNyXCbDeguO2unuQ20rusOrf6Q4c3AQGZLHAtk3Oojd10sYSUE6oOUv5Y8BAhiffQSFz3kOKxhhJ5d3pwCjjKZ2BVRdTuWmnBNnC0pnnNmPVHACeVoSCxSib_8D1qbGTSju6SoeKGVYGWeWWCiFUYK27z-pn5WVAwpM7ZHavH8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUqOl-_brxtRsB_1UVx8SJec3FC89G00QEryp1VcRkFQcZeN4S2bo4QJZ135PvXNn3vvO7Y0thibwL4HQu6Z7SeAEmUId044mm5cMhUxkSb6dfruYgZs78DBSHHP4R-0x8STdFu_IqVzswOYaR0wMYVSjpMfnZHdjEqdJSuXROqGaz4Eqt-90c9He6f4Q0McWWgCvIp91Mv1W705SeHiqkm2RofZ9UJH91qsuNlVPx8ThpJ-JvjqSwZhGngsqLPs17dzpFshv9Uf-ACq6vLsuxGn92z0fChs0ksjSUT9KrZKhsUtvb3O0idBW66tOUwvPacaHAV5IrdrXL9lt9FDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhGh5SmmH9aorazo5iFjujGciNOBrt21sEZxGU8YohJWMG2KfT8iAq-h9violvsqQjdL8IeuF0qFd9jQNmMzIQrdDzlv2GA39P7qv9bmxownuoJ_8Lp_MSyKVDXWZIMRA8g3GxP0I9Cjnw5zCTGGtxFTnHB1RbxBsKVwQB-DrGsYHN4guPPONFrWEDJn8usMtjG_RA99vOrvblNMiKW0XHi5969agNfuMJIAosulpFlhfbMxyckEnoFhjxI0r4Jh-IscpVKXLkjp9kLBfBh-SFc8XHWWaO2_J42XBDN_LrnRhzSFIUqlcE4MofTB3y06GC2sAraqKVt8f92ZKuX04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSWlNxfS0MuY8JyeRto4rPTwT_J_933r9xCTMpniInhDOc4QrMSUYI4APTjf7RHF0_zDKIGmQHnI-uF1qdqvzwdesRR5ZKYh38F5nukTZ8Q0fHJ3aF6p5BFA8WiBrPU0kW4Xz-0UAmrFWtZezhHQMkwVPV4yJSxSrrj13RBZaBVxuey6k1TUTZcKjZ9jQzkAyB616OKFq9Xvw9ytrR2u9VQ7K1VEWK7PcYmVhyofKqlHa912326HvZ5Q5ZjnBU3nqvkTOpIj70k_wJhXirHVKDqHchwsdT5jc3UFo7RAd2C86XJHt98OosVtY-WUGwIp2TcUGJNe6VB5SpRBB6ZUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH5d7knCnoQ_m4g1ftxRH1I-6cDnnJUjkYAi4tPnB_E-FZRASZaeL80VGPH40ZaLl2n0oNNc32u0sZ352noar9DTZf6ety8I2roVxWyAtZpdFQxg6etqk-PRK99uMSGASbkHedzAf3YBQXSX1TBQMjfqS32SqxYWjHKAtd0ZCYcIvCOfEmZdUJCZf1t7BQLW_lAZ_SZG8nRuxfuTsfjHPrvVQKtZEbtbk9jq89ruRjtPvkakrEz3FmXLCA41Y4qfsZg9hgNjljesJOKi1nyPNM1ZOcE2u5U8udyUS1XOjhDUBy3y_gBHt5-qqtc1VvdBEZfT3TOa9PyD6JVlUdsBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz370u0rOv9i3F3mVJW1rxLtDvNxp6hsVaQ4UR2q0S-Wl2stTjKkvl85eN5SqwA4rugIOu-Xz8qt06F9iESEOIpTvIOY1IlJJdRStH6VoQCVio2oiIPQLxVxHoV5rah_BYXhg3Y5CSStGoBEBGVWg5-Wy2RRN-v4Z-vAATRG1fX5TG7e0blU3UAcvQmAu8P3Jh4ujRx1JyqqgZkQ8DjG4h8eJk00HPlSa6oPOclHrXhNiuQMuBhQvQeaDaeJvvkxkYhf42MQjgH7mXm5RkRt5zCegShIGJAN7_r8AfYXcTsNeJyJWFKOgqsKaLEhKwrFeeLP95Zyim7RyU7kWyqfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzzLw3ISDR_K-0EMIAGu3q5bsExN-blYkK29J8P3XFZR6vHktF8K0a5WsdhSwPUrkXMP4FjYXMsIwIr8VD_VPihUtT22LUzs49I7nWLdMzNbTdto1tAl4YYF0obklLZr6VmqKoxMIyMFsWect21hHJF0lPbLrk_NfRc6Jvxe4ZD6iWbNdWZe6pSn4YUggfSzxXNFth-Slkox8vaL1lfDweqktk0ZgxLTTWxHFqCh2Ku_nnUih5uVXnhHSkCluoNjjciDqYZY9T2Hr1YOJTmjdH--BvkVDOTZnUNrEqc-d8Ui2rS9QdXFAQhr89c8130uE78lKDWLDgDHK7XII5gRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgflQF3yEAAwpP858ljp6scvUouJ-hln1Yq0oA46ZFRlpt9JoFpvfVCUQWVbi36ljRk1-j0r8c4v4pEFEzQPZaVA_IJGGHvK3OgIFAjDAbsZREO4B7v9MvorZCxwFiy1nx1mcE7--p9bciEOJOMb0NJloUoVOlXRT5qTxSRs6zTPsChc1oMenXA36uIjGz5RR6aFYkmckLh_7Q-r5ero6BhtLFiXUanA01-soz0i_ofzWDQnvE4S56bhfylawe-RyOdUZUcJdq1_2VozUsEyothsnB2xOxoNLts1t2lPTBvyipqiKcJFvbzzGKksTqQI1TxU0-L1o06CC1YVz-xisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4sBYkt4UqVC7x4FH0qoJWotULR0VAFxpF-nySbedBZeNuq26gjpIU5EFnzb5t1ah8b1huPOC0RsjGTVzOw_N39O4V9HNlR7mR0Du10aDAfoj-Mj5dRZ497hTZMJaovAVw3BEB3JZPVegTgoTCpacO8Q6LaT3ssi7fmwprcImTcwfX-WGnB-IsSeR-Yvq8wq4wvnWkd8ZnQTMRUitpOAHI17CZrnFAj18cULJx3biHRUlRWOHz2SUpUgmGv1cf9ZSpJcQH5IZsCH2iZt_SQtHtBPpbwqNoMcLi3cbOdJJi2806lj8_FQKk6kk_Iaof44Hao-pa6059THoP3AUbyqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAGtOWXiXWSRhLviNMnll5wfJiVduBuLzS5e_4eDLIA3J8LPmpLR1m4cR1qbhZBHnXQMvcoheb1yBVMm_Y3G9p-L8Ki5eIRlF6oHgKwuQqRvBuHquyuuuM3vq7qwokNm5_GqN_gW8Jmzp4zwWjfRI3A6XKaP2Lftb4Wg2VlRbJCd8txWeVzOMerE5R2EY38boBvXeNilDQ1jKrFfPncHW33HFuCA4aNwZW5B8cTstsD-j56SRjniJ9fx7EFyEq7U9npE149Gnt89BCHrRai0hJYcmyNU0XHysYPPEy0G3Zx6Z6mbkr733mYvt28FpxUD3EvU8-miCek5wB9VMGfmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLzXl6wca_xRF5UR5P6q7KOfUAkQ98KKgknYgNIRG53lH5PzH062ito7hT5AsRcFweN8ygN25VXDqI0yoSD-2WNDonE0lXMt7vwfe9So-GS57Zm6mgK8gDl34VH26IFSpjtUgcmYs4bYJS6GRK0hGLm66nziJsTXDSwmtyK2fiFR9Km-PCpzEm2J5VCy6D_2xyEcMdHwmD4lCHAdaXxf7dAdScdzkdKgXT5j3iannzap73DBCF3bHeTvAugmc7FYZQDeLGKQInsMyfga8XYWQ9COqet9Vx6l0IB3dcE5JCOH-fiZsTh0CdSwbWQuDLMOTXIRUd4om2cZ5N_ZqKdBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3uAPwrxD_AHv0LCoW4wm2CGeYVeFRsy-y_V-J7fZKtqAV0YIDdoe_Yr3XvGiLbBGl_AQ4pBvEw3HFm7-l-udB4jxAfQtauvU_PwQf2e40XJdEA2mi9TscD3l3rz3wZLxKpnyC1dObwSsPLb4XrH6uG89SbQf8pKZNTYaPdWgiXw0EVXkYQoIGoxpUvL6Qz69YH-Ue1-dqWaevFZMIxRTvZ5X7OIAdSem4rycVCRCNY7qvqeqNmEY-xfLUSMJl1O3Fs111SDGbZqmcKDdmllDuDG9x8wPMyQ5wPcHW7X3E-9XQiscWnmRzKevfDsZ9pIM3c-PK5rC5cDRb_9SciNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxrp3mpSJbdJB06-Cv1nQ_sW-WtdgRHbHGPWSJrY0XJDBZviNFDt8nJXmWyXtDA1-zh5PfNExHeBZ3LDxP5WERvDPgOZ0rggKbYMavnMaVXrnspU-iQZYPn4-mh5x54Qk1H9Im3Ri9zigfk8lynmaHeEnFQ7u3_u_zm7aCHJdFIjd_JwQ21TJmvly1aLlMOV-2d6CdCMtxPukXEmxAhw52_ifzTfHcKpgM5FSg_ccGTCwHp0Kw98vht8T1HlhGRpbkcuwJMULLG11PrNkgIow-dhDO5zqBA0c5wzr5eXQIEHisSvxcIK5cR1YEzZmQUxfMXrS6kjGL3eo-bHilfYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-SjycOn7O-xLqrUHktQ7HAOOJYty_ZRc0PefJ-jY8VEAV8CNWtX0yTQIW7d3rAB6rVuEKTtQhpCghCzP8Ws9fyRB6Ahc-HZU2nBLR8yo-8sC8x5VZUrHAPqbVc8v3arcdDW193rcTOmUlKlWCL2dFqMz0SLZmZgUbJaGfb5BXftssSLOsyEq7IygrIJeJX-miuiIvU4leoww_3FyKQ4wm9NfzqtU-KVZ5CZb4NVoCPGEWaVf_F6WprmPs67Tv5rbUKNx1wUNBJvWQGLQevZl-08zSTYEUwj5Crs6UvSlrzXQHrrQoez0p7dW-V_hitaTNiTUi_TP5oCfInWtGqBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d63k5-AdTO8GlAVQhj8mBb8VbDYU2miWf-KJfzCLibrECKXfohkYykKlIkilMrnDnY0q1mENvjszcXANVJeFmcte-AmtZoOCRw38WaAGqOotVGs-wACfLfOnUWcsujqVAD76OVF76XbXZCZPBiUgFrWldus4turZiHnBxvBXmNLXeO-ri2EgCcC2gtHEXAzfP10VWXCw448rs2wmm_x9OFP7b6ap4ChAb_LM3dqdRnY_Jz9GvjUxvOay4jNwbCXAitqXP3pJlwif1US6fqPHFElVtGFIVOP88zzlwf8Qh_1iA0U6dFzkCVSzjMwYiTj2dabO3rTyiX69EI_G6BOVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImqY_cO_xjxoR7Tl0LuL0-gIGZz_gWXlYWg_kfFe9rkLWy5l_J6g4bCSCSfLVxBPUe1Vm6SxCiHJaWBvdqWkUVnRwk2-30HY8rCu7ITBd4Kp8frs5w3KeYlPXZ0pwsh2WPSTkvWvT9XT-Xh3EiJglhdAhqnIcsxi1SZKWTHBpKZ90dEYRCCIgXmbl-mepwfq7DoSfV7bml_-KvSaib5LFeV2pKv0RtK3_FO9MgRC3aMq3Rcx5pvgdsNAj5YQ5q_Iu597oSbsZXIpK6geKoNn7hrIo1qWpW0FckJNeHhfEadfesSaYeMq9B5pkGXiiAMledhw_gJQfuDR3j0UVDILgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArY4S1Whv2QMzfzXb1JkZg4vtOO6dp0Uwrx7oD5icDsAgLiBWNhRizL3MAVba44Df3wB_WVB6zSZwkLASv7qCi78IzKnxeHvC-eXwJ2O-gtTfYOIHGqdSVC5D0rxKEZydYJlcHrnOwfwQo3gHQhqzQ__DwIFvW2fKNCYkYnXDAj9kgzlE8LgXuZvPJ5XQK8BACqINaqOLnmrhzMfcQ23RbkV9iUIwg_wtVFNUuOc96dqaXR7fnWdEPG9erJ06i7GWnvVdJzY_FeRSdhPrYCd_3eJpUfFl_j_KdrsrpaqooOxl--Ou5n0cqX_MMT_dvZ05mw-8GSvuq0j1Yh5YX976g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsFAYAHPgLJtz_bDHEvEDpvMkrXT_R1ClZ1OZKNMDoTDFytUPKGQY0JkAJY_WwNcgDSjXlspAPqdqiqnxyLHLb62dGkOtmyclJC61lQuMxPrpcIzJyC7bthDaVDixIdDae_bVC1H5piarFkkjgSSeUx5Feni55kiR4qxchWr2m3fnLt6CyDiAvHMi7FYcNRXAqSXgW4R33AMnf5l6xf5_tPCNZQBvIRdoE-EH5n0woy1_BDseaFa6zYmus2F6s135aALMlRixmU8s6ZZBrp_NMli3BY_FZFbv0ID9joKEgzWVm15jqkspTXmr3kX_kd4TDp1vHMk1eSkzcijy0s_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUrIaiBXzu-j2lA0V1-1ldL50bs0L2VOe7MIU49PJETldMcI770xBRqSDPvXgIJTfo6m9zeD6fWiuJfoHOPPL28iaf8nwZUbsOTOmujtdVYXobrt3ppSw6Hc9QLrEGkLh6-UvAZPhEpeGMkAbnq611PsiSSX8-TaVMQ97mKV-Zn35kfkyZ2BRQ8axbCvtq_Zj15gVJ505SYyUBuxiRpPQgUXPwxPX7MhI7Hms4PxCR11VS7_4WMAM4uX4DcSF-mgH2XZcAyGtXQ6uX8-LmxdYwDjCUhuRI-hfa4vHXqVXKV79EuWTZo1QQyI68AwWbyrGQ81HQeW-ISPmLVnahD7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaPs--wRRN-Zdi5tP4L1bOb43_OfSV__Jf6zjMS5BrTNFtim-qowSGIPJ6gStcMpl3j09lwqEe0RfQEy20cch5eIK1w-xHmhnT3Ej_Xk26xiOPPf7Q1oq-2_YJYgJTWuDmSfhR4k6GuDv7McU4TjF0GJCgnVltZe3jZdyvFxzpTrnPS_IL7SmOKugefDz3aouLAIS6N8EaFGps9FTQDgOZ6nyD59z9eNXTC6D2PJV224Il0jP6hXgSCXsDhyMoaySSn2NF8HWCuXPhTjyi8FJicqkkyeDviTmx_HFC5mnXSHPZjYo99ooxmNcxhhQZtKqU8CYgYmLASozeUuP5vQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=CyucNvnbStxM7aYq8_4rfIdA-80iS4jGS2qdOreaJ9HYHXZikGdloa64LmhnM3mul9ogotPvCpqGNxRLfPArc3hqR9phbFFg2Cwo4tkzIuu3i5rcv-S5C30uDMxNLAVoU0YAF4NXuvF1Ul-qGx0BuuQEPXAimuaDCi0iLvvdRpLnAxaCnzAhjhgVCY1193rUXzwD1GH-zx9RB2q79DFSm8EA3NxxY0SrGrwqolsydYwV1h5MZlOYhXRw_tqJfBJ2Qt6OmRbXuytftTjxYkVJ6heGpcuw0OLr77MztcF0lT_V-z2VsPwK8ueENK7SmWwn7pNL_em4qtW7xFIL3slX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=CyucNvnbStxM7aYq8_4rfIdA-80iS4jGS2qdOreaJ9HYHXZikGdloa64LmhnM3mul9ogotPvCpqGNxRLfPArc3hqR9phbFFg2Cwo4tkzIuu3i5rcv-S5C30uDMxNLAVoU0YAF4NXuvF1Ul-qGx0BuuQEPXAimuaDCi0iLvvdRpLnAxaCnzAhjhgVCY1193rUXzwD1GH-zx9RB2q79DFSm8EA3NxxY0SrGrwqolsydYwV1h5MZlOYhXRw_tqJfBJ2Qt6OmRbXuytftTjxYkVJ6heGpcuw0OLr77MztcF0lT_V-z2VsPwK8ueENK7SmWwn7pNL_em4qtW7xFIL3slX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMRvU1O2A_0noY0ID3dTpmnflhLqpS7otbPl7_Qu12U-rZSCO2oFLZKblKGRMF1ir_OFeclyqCadb3f45381KIuQetSnYZ2YIfoXCyQuUV2TlhsT0ZmXq_zfIdnW864E6ow5p-t5eqHUZerd65nSVCzS1qOIcjjYxOCv47zSW8G0rqgpQxNc_BvQs2WD3k5qbFnMvoD98gZdiD6yAD673h3Ov9OX2b05sjmLFYQ3tienASu6BOatGg35DmDtibkG8HSSuFQevnXLR-KfFOBeV_RE2Sq-AVJHd5yDVJvZYnpYXS1eHwI8k11TaygqpSo2utGN94A9TE_MXVLVRYo6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzwltDgG3zVNoD6zdMmg0LCP463B6kk5Tgx-uJ-XhYwD9-VxIREL0oBVd_yTerb6AAgFl6-I7VeSGsJZPSumLeh08cK096HnPxE-c0UB3fimxgUMYDsrgWi5FyIH9ylbP-b2KO9qUjJXXY_O85qU11J12MyuBKBTXMe9HigSDziBaZPpGg1hk5a-yi0DTi5QPTsiqudGwO2aWRBHjPBb399iyyPnokudgZxyg0MRVtK3tLvJuli99BjeIsp_ohHZYt3Bc3MgspyCNtVjCZhUd2_M_k8Ebt6RzxnFtENtmXoB4cM8_5SHkv6f1hOB5Q5UYVoQRrq5WxZSrUWYrdBYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5E8LU1E7Bcj5wSypaZfhKUKCdXuVSscTpDrMPXmO3zLtFrUr4MGav8r6qJZtiOpntjFUZSrNGsEr0unTW2asglu8r7MnFtfa41k7G2V_KfKFRvxxYpVdbUu2TfhcNaqkRakaMdSHmOjlhBvLrNDroe6Tp_wm2Zum1afIZ5NfRM2hA7J3b7mYvFV-LJ88nAISaqmEg_4debMEfVhb9frYCzGdahTcfc2QCD713vePj17wNErw19IMdV20n8o1-NVEaTwpArjfVB0g6-T0-2hB3bAjrAUc6iKNiuNJ-7QB-VCQ1zB5HChlgK7yRHJb-Yke8sQVMmf_zcwXMrwRPRVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur_TImiz0A8CPyExKxrd2HEr9N6FATAiVaA5x3Rsbxd45XdsAZVkdCLSJWoxdsF7sjUuX07rCLts6G-zM02qRmdfT_3gG_nZtMl-8aZcToFJEOF1ILfSWmIRNXcRbW4jdSYRg5Uaqeh-L-u57Mq99ZLWHGFH-IJZd2B_QQYUsHuE1oNdVDvdphJB0YUkUe18RPTRxTl-t0_SfIa-Fs-XAUv9ICtuP7L1pTDALORgVk9-Y1JeKHtEfiTdU6_-xGgRlhzcEyZcIzJQT9G-Dph538kVaCmif0SQNuFjRqTsmCM5UBO5NNAHaOeCKwx3kn4OGGUL72AJ55LfM9EdBByldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7e1ytElbPidYIi2tEj25EClnkyD8V18neNY18JpMKC0I_k1lUrnV_L8tCogTRBnooWqWtvub0l2ZYkAdMDtZ21vPyvm0CmUGYuBP6kx9Oh6fjhuhk2KjfDTl6eogFRL_kruEgjDWbsJgbFGIhHTHorMYLUj_U97zXa6qYG3tVUk7Y0el8G3wpQx9ZIYBuy7sGWkDyK0nZuXtZHYyquqmM4oQUSNxrznqnkE4A25gvLdv1HrD5-u124GufOnlKnpHR-JTKrkX1E53biNJ7i93orue--mApa0b7tpymEmc6stFT-95eGSOitgh1-kSFmelQHDa0DKuZVnSGGjQ2yvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnAipwvKFmnRryDGHUhbtFa2J9Oi05O6TpoK8pwJZOO1fMTM3HrVt_mI3O7x7r4OXv5lgwhVcoh2NwwpJ5jhj6KUnoiuE23EWZLUvrbX9ukNsKvzWLORAibKuWaGZhpgkzMdHP4zbBKFoRJqDC6sTWoJCxebdBg9HSe4dFh5ipTKFLvrUyZDoqxltDxAjmIxQKHqyTW5VCMTcpneVTRTEIf8DEnrlPcoZybvm2xB3BTcmxRgDQljOadDHbzV7eUK0A7YZA_tW-rbDNxTCvioSBCBWKU2ZnWQzo4H2HL-UePmipqhqLJ-uNUXdn9OcJYcXvqWttH15myPNdsGqZT3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAUOPkgCFc4ot6ovyomH_BQBtLa67FYsL9QqpSjHekbGyiL8h8oesL8_zuWeOJVGE7rfPLcjpC9HfBz2ica4T1xaMS1HqHRdUbSvp1t5A3hB_XenQ9gwMVf1NZn9vaqtQpGVhdHAlRNwu_YPnPclzIGGfMo2UTP0XtemOwpwAZH2_8av9SQNdGbDfHaDRHjrnQ22G9UnQ-bjGeLMCsl8PiX0vogBMOPWPll25IwefG2c7kctD1e0GUgzsMKO92jVDs12nTmH4fe9z9LnP44S1d-Isd5mjfp_1VN-5yrd7zrdj8_Ab3n5CWDACl865VmNPOhESJNM1QhN0tuGYwgKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er4sG6DHigmBbiLCVjB0y8nfT0JUu_b5SmxogrmIaJ2057TanAzjnBsgdFxSTamx8Tnhlvd_-KRaNBxqRPfJB0ot_KAucZeQiwrz6nS4gB5uxsozPcPU0UeVKlSZN1kg9wg9nmKpI1kapboVzckD4fGILDR8qq-Ss0GESZgyXy2Jf4OeNu-GN4LLI0WzSjU_X6hiOpeKzxEDDHEWf_a2fsA8sDKv70m6gYGvZz29Q5-Nf2XqWjm_6y-NwFdkKgcZJ0t-SsZZkMoUbqElF3M1bHTyo4H_i1HD6zBB68UJ-SwmAQ8QserukWt0_v9CaqKUj3O7sI_lwQEGMyQmzhc4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGHSTGOMg5vnYFRhc6gJa1LtSFPfcgbDXLBCtLotynbPWnVBDrkDuNUBwix2B3zsrR2bK0Uw_IWAvMY-jSdcD8lmOiDnT8IZOTHeAg2k6eATwQ7F4S9DeK6Hqx0hCbNz4gPG5vRJ3b1H3Z2w3uE1Qq1xsnd6NKEjF5Zzgny10B6wHglLM0k2HW6_JvYSZIYsc7JkWMDtmZFchyVWR2855VgrjfVIURua8w_sKP86qo38FlotYkJZwujz9_6Fn7u8XI7np4IYfrMUCydkGZQ05qyOkG1ytFu6sWwPLpTkRUk3uH2jbjWtbzqWsh0bGgxDDNC__-qhKgOJGyiQyUUlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdCQG-RW3UAqrO50ymnrY7QCqbBGRh37QD2kIgqcmiMYN8JljNvYiU78QK9Ss-GJHbbGZtYSJWaqlMtFCXydvkhr3geH0vIbH2dI7kCkDAaSmCsHjVCLu_Wb6ks2MmhKF2JPrejAHQGygTi5FhQsHfSkgFSaG1tqoosSl-WWCQzLim1JvmeVvvesE7USkbl3d-Ijk9ICtnsx08bwjV23xTqTOGjc5rk_ZnyVMycG9OSYxQeJMaN-mJi586P7EYkMziL1yq3wE95Xks8gzSOMxkVrfSWDiEtMOZvgvacGMI4TWNPzDdhp20YLzKYYJX_kNYTUVdWDlBvYUESC_Wj6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdB90R9AoAjW3rN199BlPpVNhXW9m1bifpHx1xKDlZeLEpfkCVHzu5BoBsnRwKdwLhhnwJt20YfTJQcGEDhE43KbkipssRVy3vrCTXq1Ug58XoW-2xhiWzL9gDSqO-LrbeVqp3NqVwQYYgSCSq6iZskD8JL5B8YsSiibgfOJR6qjVpz64NDBmcdzxcld5HNWKOKngTcRx4rdYw4-oIybayguAhoXg1-kIpws-3rDrIXLU2_0CVd9Q5DpmCQEKa7flUkUV3VHkvh7JzwSo2vXFQiBF_-7paLAl2AOrN9mspkR4iZzHo_fshBmdiZbgF24OCqu-YzYVtxwS6TcUlgvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4sMg-j-X-V5qwhu4SLEXGdhu7rewhbuPShA-1mQrpoXcLbQOPrMp4nPVyiHRdc2WY4f6aqD7fV-vLy6A1j4J0DoHvA7jVk3csuFrSVomgxi58n5kdCZHzoI8cOFJRLgPm0ZaMI2FxDfp4XL359kOf1ln1hpq08uoqjQt0xtJDpz4jHQwGlVb4I47ngRH-pl6LpG5rVm3tWs2JCP01Tlu6BL7SAnJc6dGQge7y0zUCqqZ6Uh1Bq_I3EGM8xSCjr9-v2_bF5dOWXbYWKfW3baDZ8uRJZ27ihjbrxhM7I8Vvn_pA6nYoxER2SiHqMWSq85BVRpUFjGbk_xYLSZPSuI4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsMXPgshF_-ar4edsrCIBWRuHrAxXS6DHIiGEQevTURa56dlQRvhvOGy_Ucx9aea-fDPmk4u_LPWTh6f62-H8e5JQmqvU2w0IO5iYYS7383qMVldKHr7X67Yf1JZ22F7Fmqv1eOqNiMz97iiR_Be4Jy9VLZ5rn_P2CjDvhDtQ_oc2Cb8uftBSsQsiucS7FkCYSFFvKBBL0MT-LfhKu6J5M7BsWa9mpyA1dJhqN6WsKcmhAtXsEVQhf75u5lRAZsJZpccLx7T4_ptMWPYISqWk6YVbho2Z1ZFigbN3aXcf19-SM3avREQuLR1Pp9jqc5i9H3gVL6v4nBQLfyhCLgpsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rui7AZY_af5q-6w3kGLsAhSE4uNTP4Ivrh_hSx6w1YfzBMdILv7w-7xjK93yPNwAYBY_73LdwocuxXEabe9VmZVayPsCgozOLisxNl3s322mK8zA12rSfuoNY0VIfCLL3GdGkKorjN8w74a-kSHjdvsK4i1u5-FVYwtR_15YVLAroueYV9cuU9_MqadloMRi-Ul_vD_CyW_4u1brivgevpxSzeuPPVErG2sG9cNAelaHlfUQ1xbt_psomOApfZ44ANbx04G2zTZG3fF1RNOjuzj24eA_DRvdOenohhvOgkiFz5amHG1pnpPCtvKV0QRp_pycL_4yMtZwu8G8Va3LMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nh_gmFTK33YUC6OimrWHLnu6MMaXYFfcx1XMZ_lwNTjrFwWX64vFZe_vNNyvgs8afYfX6NXvwgzB7bjF0UwXKXx-DKt73Qd-wF1PTtR5VuBr5iUOpdt_a9-W4aED3wT0yJdH9G65UA1Gx5dX4YxlNBOUUEhJO1GKabknOuT9uw1ehWbmyQoP9dYN2PNSJgY9lS8PU3Qe1NjKUu6V0ndrs1SyYUk0BPFTS4P33kkila3SS_EAYuTu9iAfVoRG-MRuMUfQTxsN2bagr5tsWLTsaTkpUYMoeBWJr69-QafXjeeeSvI1bbOjXYUPUeKKJ3ofX-eVT_0awFpBq9F69OulRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3u6zgGCraj8jIxYO--Vjp8Zf3Ua9_q2CYrJ6L2sh1iyNTGOCkDX0CtZKWqC99g8GLVT5SkaiTNdZcvdQUNsfU63NRHaWNsLSkW0GXyoI700TBvhIAlxOGn8haLFtPfgXdC8bKUBt-WR5oicc9Aga5pRFzfbxA-zHe40xmV0KZ0ERK8My4wjRMJ7yIisbvwDqleqE6XXAN-qoZtbHoiRXW7aCznwNsg6lBezzrH2CvHakBG4tH2ac9K4zrwmnhKnFoQSFsTvoWCimKItKYj_yrwoo_h0QKOv3BUBkNErbj04LdQ2C2TSLjCcHnffs_VlQw_Q5Q2faKfRmVFeNHdakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3_rnt3LPzlW9gUNLz-NGjAxwJEcGO20IfqXLeDqRryHaNtvlzyUg79ngDKGvE5i2ZiOGbrr2t1jkGb5_wrza4__4ZXKV0NTdLE1ojB6veLphexXGNihk6SqypEcEr0nOMt7gkCh02iZxuSg0Z9t0xjXjQC3RmRksC4San0ebwS0t9xtKdATDc79k9VXESVcExEyZfB0iSukkpcMIrQu8iu0IMc6VUH6hNIHniaKEhFKrfCajlzLrhslppO_-JAFFYPw5DPSpddD0qDIZGJMAD0RvgMQE60ZaH87rUSUz_UKAfFiMFkLTnHlOp-f7CzKiIQFY3FChlqnAui1xqd78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f23W3x8oVuOsP3yRYwJ8x8l97RFCat_cfJlOY2qXQK6e4fMFemraGUbPLsNeh3T-0j5ucOYYllU8wGA06Jh816i1AI6GP5KVj2jHOTrLBrv9kHUi8_VdBOoOjnE0eaTPTfD0dIEGWd_sVl1psy3V2Q82nPfXt7W6hgWiaXys-hYYpDsx_R2bMt1nT6feTM0tLDh9bOHhkVBXfkPHgn-uy9Xbrf8e6Z_bTyE65FixZH74wvAd_MOI6SZuetz7DsSXeLFdAU4aRogkY5JNdC5FKQh2eyFbdXOneU2RRDNXo2cKGuLfFIFyei9U6ROOpRwVc0sfaYbZSx5UsZAqU99qIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=kL4NqkRlEgBXUavrJZ7kZsPZoz-cgZ4JFqn4nwx3H4WRSFjxiEgYomeWNg5Em6nuAvgJsGFSyIb7VH73AHa7QZhyWMel49smwu7k2icjEjxHLUaxfxIgFuAf9mmvGcV5bQl9JrevMTLVJZdDlVl91BQnmGsi5zYW9gLzxo4uBdCGmonCZnHQ5lhqBUsP72JUZ299cRd0tm2Pc_6k5lM9PsJQwJAZzBoJ2HuK_Xrk7m6y4a7QUKE_LvRUZ4FcZNc41oME-Y78yb20vp563thhqpuSfTkwCwPzgH9VphyhjooKdroFgDOAzEUjAEhxv9expqw7sRWtIKnkSnGVdPPXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=kL4NqkRlEgBXUavrJZ7kZsPZoz-cgZ4JFqn4nwx3H4WRSFjxiEgYomeWNg5Em6nuAvgJsGFSyIb7VH73AHa7QZhyWMel49smwu7k2icjEjxHLUaxfxIgFuAf9mmvGcV5bQl9JrevMTLVJZdDlVl91BQnmGsi5zYW9gLzxo4uBdCGmonCZnHQ5lhqBUsP72JUZ299cRd0tm2Pc_6k5lM9PsJQwJAZzBoJ2HuK_Xrk7m6y4a7QUKE_LvRUZ4FcZNc41oME-Y78yb20vp563thhqpuSfTkwCwPzgH9VphyhjooKdroFgDOAzEUjAEhxv9expqw7sRWtIKnkSnGVdPPXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=pwoK-6MKnSdcgnJ_9WE6zldA9ztrcs6VP-n5cGTHOoaN-bwKJcMowTVdwawI3mgnZm6A5zT95xk_olA2QVk-tLVJnzvVAdXvIAJS7_K5db7GacznZNs0nMoJA52lif2ldliq-JyIprrd7NPeRddVtWmGuyD3l3_VRWVUtJepSmpMm_-fIf9h4bMwVqbT09qOn220HOHOjhoh5KxbFb7Vmkv-HcstnVgzYrZ4Uhhnee3gVX69gKfOWnoYtLpRmxlOfI4S36iVggA0HE-HaeC7ek6PSUJMyyQmpdSToWxw8hsLcdZLLaQUw6Ks8HJBMMNy3Feg1xHflxwWayvhW243ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=pwoK-6MKnSdcgnJ_9WE6zldA9ztrcs6VP-n5cGTHOoaN-bwKJcMowTVdwawI3mgnZm6A5zT95xk_olA2QVk-tLVJnzvVAdXvIAJS7_K5db7GacznZNs0nMoJA52lif2ldliq-JyIprrd7NPeRddVtWmGuyD3l3_VRWVUtJepSmpMm_-fIf9h4bMwVqbT09qOn220HOHOjhoh5KxbFb7Vmkv-HcstnVgzYrZ4Uhhnee3gVX69gKfOWnoYtLpRmxlOfI4S36iVggA0HE-HaeC7ek6PSUJMyyQmpdSToWxw8hsLcdZLLaQUw6Ks8HJBMMNy3Feg1xHflxwWayvhW243ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMqb9o6PNVOJHVSqugXyrOkYKhQHAk5LYpL5e5UFusM5a61E0ChWSYc4T8y0UErQtfJAuCDYArAGT_2UJOHRxeiNbWr0xu17aKpmJzE1iLB6KScrn_9ierWLfN7z8IJtUgPf7YV0Wtmh0XwS-x784vOZgCczQx6n7YptB9lw5Roqx0e5ZZa9SzBVtJpFYFKWrkEwEWIEu_m3CHglJEEijyPLsy5TaSGlts312Jj14oYCLGyE6Yd9jeWlGn6Vr5F3e12caQJux0_I1MAnwgjaYPfXu1pk8hZIyYWz-XBIkZwbv0DHujCMBUKwkEAFZ4fJGUEnl88H3MtUFZC6gc_J2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grkqGIGIvgk6Ge50DsQ_PeZEkT6STv9TlfwXsErj_ObHKxdZTCQaX5TpsMv1X-pSCCjVmqlC1Hjo6dSAmQtKTSGVeYM8cMBiwc0UfuZrLmKrO6aMov4AXPofwYcQqmCSIfcbOpl35k1bhVz0gY9ixTREA45EablxlfD4oXkRNN3KPSE6Z8GasD8dymo815_jT62B5ZvkPM7ZblfgVYaLDWy7o61-t2cvffemGeG5iNHm17wFP_FKG_c2WnNMSntqNmHmaRIKc2nqhhewuxWzkbuB8vJ9HC0Tmgmg_jpJbQIu0HtwggB2X4cFQ7ik9F661aFS1NfcOSkKoLL105x3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXdrhQ2cu-7gzT_McjJ3JuwXUNXr5KFvAl-uUP1BIM1ZL99Txz7GWB44ze-WEjwk64ubz2hr5RhtzCm28Fla6Ijs-aWnWvhaA1mxrBK_ZbjinbSVsiAeeO0aku_BaOphITCvdHwKy_5wPLAdgYz9KDbsZFRjg4DkZtsAK4zWtvqRpBaQbxas5VDmdKnAagFS2F6gLh_86MC4QHmbTpG9g8FUFBc6q8eCQFTu5sXeO4FD_njfkT2zhJn7T32G3lBOiy89KFzdb4jQn4vkr3QIbauTuJumhhOoqp9CENcgoEGS0U9wJqIsPPrzLqDkFRKRiFlKlJZ8HicFTJg1KjBKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLfeIebQyJX74xyj7CRpwESiytGGfFHk6Ovw1ZLA0p53wuJGIDlXej9nLGSmaQuWNi8V0Bcg4HzTNUIlrvE84Rr_KXYXe3uwtPhB3OJd7CbpMpXZHxVO2cq8p-dqwJOq5LQmjVm0cffK-D1nteZZ5J7ZepgduDwPQVebbOGESzFGCc64bPOixm3GIGgSJDToF7hKLOCSZJ0rm1t7oVJPu3UsdiYQROQNQ3xfWjcAtMHjgjbHQZG3yfo1Gz0TvvRGFZqj8_5D-Lkv2BFmwlp0795AxGcxYB7imxm8bwXII2okvJ0bgK5XF-VHwIkboWTjBVXXF3l0bm5dzYNAwgs-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd_mb5ogpaFbMcqYRenu6A4k_IHGbpsYEVfAKo_s3085YBquBDuu3LUNV2rRbA7lU4T3H9WyBNqjuDs3po9T3v2cisUxtmnOXV0vdhdKVo1DDQVEd305tFJKNHy8WTKky0_I91fHosJfWXEI9LimhVkVFOiIGfq_kOGJLKFq9VnbvokfDxa2e6ATASE2onxTHgj9aVhW7fV3NMCqq-DDDelHLZ02ABA1MBn9CVo5DpW3Evo-qox0xls4U5snvmaX4nGAPdORhVgk2tcv_f0fUczXfVaqRDrNo_tHJ6U0SeHWVay6ctyt4GTc5E8GdqGgB44UiZmNyg7yS0jkYpk1pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmqE1U0l2dOYSQkfsl5-GnbA0bB1QBVfxX_mY8ZJDbFygQwCYCtgBBDxoiEJet05uScA36K9QQGMmE06HhhjVa7LbY_3I8vv01QUhn1frBRvgmFSzoWM9xODRb08MuYaBbK3qAhoQgnmcBv29tYDvcmiRame6HBL1cgL3Z16XAjF3MCw9FA54JRL_NLOOl1h38qbru7mrhAa7d_fMsdtxlJFuOTUJQ-1BnJJTcarhbcTOXoOPoEeerrC-fqWuTvJYFKrxeGnMEfCYodK9N5JDxsfgtfTOJhBJZY2WTmIm0XTNsdJnHagowOXJk9cYJEMHXDvueLK2HMQy9hq3vkx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoIqKIryeCKfj-nI4fMBZIsmPb4BwAfVqcZMCbQRlJrFZd4gou4pFETELPxfPLwLGM1sfISsPq6c0g4C0IyKxHmlusL5rwRDwdyoPl77pvBxwHvN-NbkwulQe9HmIzqZ_lK33Sw4ZhidUFHyngcE1f2QTC9gpN0HRrOEXe8nP1oZA_auulb1gbUCwXZMrtEsO42jCezx6Y5QcWBfsyLAMz9_gLYeKxSBHlmWbXuKhGmLq2V47Cxv4t35s1DfAPGjM0o5ipfk-hySLtPs8pppYcCKGFdbqT9xgYXCi0HXSym4raDKAH-jk4RufxnA0sP_1jhLhYgofUf-To1sq-Ctmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQnGHZDSKw2D7BgPYAUleM61S3m5w7diZ3mVOR0fTmSFaDSwBqur2YpQY4-FeBdFKQFpKf-RDB1JAiK4zlGLBezXwBJnG4rCuYd_ACgTnR-tN_ZZHf12S7B0sDmyuwQGhelDfpSVeXh97vDM_i6gk9ZxAzIXtgg2Vtd9MZdNXkDc8bgvAqp-ZBDe9M3SiOBa-q5imSB0lSAG-TJDERdddDBlwCciy1sAYP9GUh0DrL_wcBvuv8cOuDW3jIeUxuinqe0j7x6sf26h-Y2ntzINEtuGXljo7d4DK2Fmxxd6MHyddYH1i6_XBT1_hhqCFlr77EUHzZvUmtU37G7F4BQgsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
