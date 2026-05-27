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
<img src="https://cdn4.telesco.pe/file/ZXgNxLRwGeFgrDEcxLYBwncoRleNzzsGzS8a6uz6ogWlj1d4lmtFsDXOqTiNH5_ohJqZIP6j5NfKEaU4s2RlIUy-F0rbA3C5_WR4OZ2oS-jMQLUXpXufhKVtdK9eR_M-9BlOIA419_nKHySppgwFZoe1kr7MDmGp_DP0LWTxAQe2sdBbD3lnrvfxLOwYXfLqWqY6q0PqcWLpn6hqwItlWNEqfa0NJNCHOs-9A4ZDvJmVasBlSKxv3LdpHawF-cwQsu9j_ErKIHRl4D87sPAIZ9_xrFOJjf_T6EUsyxX3l58GQUmy6gIfFmhuZ0vS1DOm6sjppqDJfOG83Y70s1OtbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 124K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coe5SXlJ3GBuYSYiHIlHmtS8FHeabG6JQn42kdqxBVHz8db5JstUmCVxF2CAaebbVki7w78-vEzKTLKRoBpW5X7DCBVjlcfovcOxVmP4IFBaYRfZx1TMbc25f9qViV6qElYvtE7uGqBjgddUXOtvr541DR7C-i6G7I6JtotoIRIqM87NSj337LwApTNX5uNiJLbyBlpKljAZ71y098lUWFkYpYgoV4oE5H4Jf6yGB0KT-hJsoRH0ubSsIb5V4y-sFEpGt8rwnGMLKYzYPpVdMK40yOSk2Bxpp_5chfNt51BOac0NZ3eV18bI7R-vfqz9VqKIWbhchK3jw2YvHqksIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzQW_o8F2W6gqwPid1kVl_qJF6SlrfJ6gmfjJRiR-ULDRwFvMS70YbwgPF4T5FhlTSY0YlrbTf3w6MFE15KkV5Z8e-l6xnBg5HZeu3-doF1Ir0KhXHf_nPiO20gw_D3hWuEYlBEgAsRWxgVWqGDD_nxgALi4zMetfDSwacnFppD7FvIq1cHs4keIwBnDhMZuqqM0Xsi5VbsUnFE3sUHOnZU3wuXnm_q6tsML3U08gQoSSXzv3TyqezOzTxSdZcQ6FJlyqHOMgeoOCQvDNLGPKqjedD3KRO1l3bxnvd0RqxtsC3g7ZcgZBLpWLuWtXg-qRt7Pw81G-ERHVCam1FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu729zj7E4x21Qjz9ZkvIK4XzNuvtPRNt6toX1q4hT4v3nJXQ8BmYt_JIw7cEeAC7wOqTuOMNEFjVPM7rPqHWfmjUP9dKqASVvQc5S9iJqAIkyOgvT9Wu0pelPdEpKrSiC_mxQNTOMFjlm-kOMT3vo-FdxwuIpsFcdtz3GIwsw9YVfKRNVpehKcdXm6DH5JvFzgmTft5YrJJJ2PyINjTY7SjZejKacRWaqkOmUDUKJGpc6BSkpGrn1CEHow27KNv7KxfAeIJ6CpScf9OBPym6eiM8dI0Qbd2ZouF6mYgn4xsF9m7P0YySXh8iUJVU51uwz3f8jBq1gqydx_m8YaXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZUBhClMlC2Pffqsey1BSCVonztJMGScNWDPvcguZDmO3pvHDOw5E9soAcI32tJP3RR4bTzFEvMdgrjFxnkNn3lcaJssnQ6SvrC1KBGb61oVanHiC4lIsdHhCO_U2qANWhoNI0-PyY_ZtTygkGSfT6PdIzqC1MIk5qShRDIMnkhgRMlCjoom2b2OHjjtB-GMYCSEv3z0j3QMzCg-wpx30-hLAFBTfflVz2foOQ0IOvqTpEiyhaoqHEUE-y0UxNAsvY4TlX8WTjV7SqDxfibiHi2035iYLDJEXF1Th8-MfaQoz2eVVivZ1joRfMdcXt5jcrrcoMIjQ_8CWeHHVmtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDAmxhI6I1VGqJBIMfP2JcSIIdO6Gr3YlkPzT4rxvVWBIEtVi5RZ8vbIiRhp-oxvlYUr335S1BXzSGkxCEDmxc6xSH_HdUbN0vpAJq7i7ziH-pPu0Sm2DENh_ohbc-T4SrfgJY_hHH9N6Z160ugx80MC2GCS5wYReB4ScNBDhv_s1QfWoaWJRv7_Hib-67MqWF0TL1rlyIomAAmkBuYKjb0nxwVWbuxYou7Y_WcMXQpd3xTGj-QvbTvl92gMTsCXDM3Mw75c5IIaoIyVyfGUo1_w2XoCPBpm78bippvdQHGAaj_pW0GYs5023RdnJUzMDqowLwX7Wq_eCbvGi9yFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZMVn6YWe3uDlsjKCPt1H469iSvqVsvHgWpYJS1rOt6-CtEvRWTftUVEYWvq49dbNtsnAu5sdwBpwyJyR8MhnE37pMmSCC6xaCPmHrJxX_2q3RViBaK4RBIks05r0N7HNpZ-j2DxTVydxdIL-VaK_5LkezCxv0LqMT0epYsAVvPBwHA08QJRFEq_0hs0pUXodNHyhAJSE2VVHyB3dvZJP9V9O2w3gnrlml4maY_ZP0vUxmF00umGQq2w1SVgOASR3CE4yDCv2_V9odvzDUtYinjDuQlD5DeWVA3GULK1EAEXhoignczJGvxUvbqXcUufZwMQk0xaMf6hzGF9il2GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7_BJmb0ABTb-aDUQFjvvcXEoEoZzQ_28-drbG7sjEN-PJOsNKAo-CGXDpP8UOZMCmBvTkOvdK4VkBbitMCo01zLiqlPKsvkUOVx83_H9q8iNv1s_us_N_jggmg7ymlpXL6nZ69iOsHO3UqGCwPaUnPVwiY-wfIZ3nivlr1vZn0WYxW77DNkADVHUBG67upnIw1DzjXQvbG2yphqFcmtKmFoHUK5byYBRvhFEL5qt8UJx0MnvKM0K8Db4drSbRXEBOQxBMkZTg-RfY2iUOiT6IcKkgkgeyThggiixefnomOZdDHqTmzU9pDpffZmT3BLGJmjfz6-kHbpIfk56G3-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkrgbjTwkYQEtBcqiAFVgbEFaWw7cUSmcXx5mkwCApxPaYIVXSvaIxHbkc7eq8FYac-hx7ylIFIyy_HhIXg7G8zWssaj8PD0UoaUpVH8aMA5tpHCViWSaScElCiYRnNcOjExQZ8xFunVJHd94M4hpxKA5r9HpDb3iCuR6LJxgBirHiOYZqRCX0-RLvqHbv72nQipQT4i1qcvFQ_wXOr9Fu-Z0rbDL5KLTeGfczElyZ2BXhNEh_RTgWcLi299ysYengs5gNZeWQc1sW3kT6UO23yXbumiim8r6cBdBj0H2yiN92I0N8d0Bi7DMXzvGSqFAvJjDE1XjEp7kBn6Ex94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMolkyy4GZIjfMPJIci9P6Q9LZ1tJiiLuknNWO4jIjL-GbXhe9OjvSD-jc9gXbE3wBWJJP-_MJJa_0FafozdAloCl79QQtpnKtRbA5VwQWPDaeeeYNV90jPQxohp-fWSFwKpC9qWliCwDWD8Fay6BEojOzNvoDCJOWDhNq4Wgf_F6lpwJqVta3P6q8bJEV7rtaVeV2GCvQx0OdWwnxLuBypzR0m2aqI_FyEofsgtSkuo-xBY0ga5oIN723ExHt6QkaMsTnbjGR404PovKm5ZCVFUOOr4ghVSMopETtc5-yrbxCdd2OLlx6iVGy8AWwhGpfmsNqWrMxlkgAi9o7e1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL2VHTcMfywk8L202XFA9ptpGQ9uPVhylLDsXgukp4HDV01_f6QztiR07l22KvWt6JoFrrGFHcFUVOtKB71NUw-shm0dEWVVzcKsc1rQRJjw4xsFwbe-lRghyJm1oI7x7g6FwZEPUv92eRCZw_LrHAGJycQtavPvS9hp8gB_Hnqjuwp1q-SJfEsNMYZZaT_4-JWy1_d36Ye4Xt1tafuXZzT2CPb258Pl-Moz95QGX-CK4csgOi_RhbTNIPsALyWWlznyYFkueUzfgX-nStWimnmeiKybWApClUcTlb2y4QfD36RZ58Dx83KEAzLo31ew4p8Qpt-RB2SzW00QNVUwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
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
Winro.io…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZt9fe6UkoXe0Kamvw7y8LJCXY4jwHTYZXiuJ_2yZP5I3IczxHObl-QKQS7OzlDnc-EgT2jVVZKjwkuOzFzvRzL1byAyNd76UV9BYJQJb0rAa4Uc5Y8rCqQYHlDwYbXoAQCMsCvMg2JXanfeCrDfpbmL7AZPXZ8lW35t_W5nt5hoyWsRBKcFvCuZGe-KArGBd9MZZoJRfSoUNNVgJ6-btYdDKVVSyKQr9wDD2GnDJRzF5o8URgpRKKu0qCUD4HShxtlSvkjlqh2rAUGT91R6GdGKJLeMnkJfWosHYm1eZzee2GYxwy-qeivX8uPeoKTEJWX50JOxl-69mX2E2WXOw.jpg" alt="photo" loading="lazy"/></div>
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
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDnq0wzrNdDzTYnBlLOoMvXLbMGTsUhKckiepBlnS5Ja_tiV22vy-xtKvxN_kd3MGwu2hgSgdmCCaA4jddlmWSdQw2Kj6IuFnPwwYU8m3drYZMRiyXDdSb2cC5ntsrIhMZ4TjqXpSpsXMBiLjxBKU-qZE-Q8mXpvsy1g3jL8yv0vOHCg2WL_8DiX9QFn1KWIus1230qFc8scyJ1d3UtP-7Nnp2y9dyRY0cB7lnSMx653yu7TdrrPLZ3af6H8RlZQ7FLSMSh64IIQ29GHvydhF-dFM5WwP9SIGhwQKJCZNkd1GB18UetuColLSw51QXX_mq1QHSWPrSUX5xaQpkAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWhhTmfl5omiq0MChMEiRKuSHvzGI9LLv7cRCbWNaYKmfnViRg3GoOYyhRJ4tx0Pnm5xfU_Psxfmq5Y41nBQoAWu4avgMYhew5x3HWZUhtcmWofkQ2flRnU-2StjoDQvAKmXcx_oT69Yv0N2cKlur6NVh4L8Rb5cdw0PU5mvIemxw058xmSbhzqQ8Au-uCr_ib9MM_VtbMA-mBt4cIte_iYC2ejpj3BqPFztKp9mBYt2TGM2mEmcbR_qRsQ6fU0Bobn0xP4eVl7TDQQzjELWhscJuI7pi_rbjRiIqrmsMIZin1aYFXjKqnDFhujgH5868TkoRWjjVcLNF9oRtrtCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otW_lbD7_zKRILGsNTJiDsO4xPkC9nMAGHL5kZTz8PX_j1potRSAp9r8zD950KViOYF0OCD_HXxYeLQX8gzuGEkDQbPCuSXeQwYBqYTOpcgaubvQKuBow37BGpsXlS5PVM7bRkwaZ5PSqkcQQBP2fInHgQ2opNf-YXTSvt47LjBIP5nHpDc14PNxa7cJyDDZnh09NqxB2-DSNYeGwu38JMz_jqkaIhrZGchK1Clc1KLQt22eMRLd1yBAWTE6IjBtuxkS0E_jerEqJGmgsJMzqRRR4XrdVT2j2os5cjECvBMasEcQXncUWY9f69PL8MIZTF_hdmPflCJwAchJ3VDAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjaYvtQcrNXuEXtUjP3r392s-b1I0c8pNv70lLZOQORh6soYezQXLs3GDtSRyW2amFxf7PkN6yOxlm0j8MnyaXa0-wlJNh0CxBdPuE332I9qVXKWYXxackOUfeiQmU9UwwFxDOm7MXH7j1Amm0VJoifIhZPjIfZEFMZ2zwLA816q_-Pio1VTq6wil3lgaSMVP8IIqmrY28d2iYLkxbijfRYm2N1v1-2xrCp--jbsvokOZhCNkmg9CIEqJVIDxVH37KNEKLTIOPoXwqookXPMZ26DmIS1lcIIgjtDy0zzFXPGMKb_7gi8xuDUq6zjVCGhepev0eBThFr72EmikXixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFHiFk-5QS-c0z-3t3otl7d6bVIPiWprqOgzenRHv72gIdxosxbiziDORJsKwdMdEGemTqPfUniTgw94CyNjY0kgX0PHdMHMWIt62WbHllPCvpVu41wTsDwk-fo08rem2xy4fN5SuhELaBgDPlooojwzVo13Qi8TH-mTuog0DN-QXFKmqcAwO-bIzjP6Pt6qAzcBVVMcDgTFkypV0z81eMpKrT7TxNG0IF-CBP-V5GksFi8Eg2ILL06hTSxbmcUGoBi2cBDYvjktL_UsU9Zuwt2RqAygBO5oCHhZ_DFl4211nScTy8uilkwG-QtJJU1xw70jfiTTa8GbqfcUacAQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvp_bRKf5rSoZnkPqyyb_SLKn8SMPgWB2FONvjUNRu4mtwOJ0g4uhF6Oojv6h1Gp21gcmBkTcTu_CiosdFmPAOCBf0XdBj_lt1IcoEnzQvNDhN452hrFmOFPsrbcPSAI8FLQ3XvxqwEWpuLpQ2ifoBd1P8uNtiyX22b5Agzto1K3SnwrmwVFJMk8tqGageM59IoYjjLBwfo8PUIY2jQQNoMopfnL_CY5JA2YpOunD4BldiHaCAVcHEUKztjhctMmwqpThac4igOavQnQBaDW_WRQchwTRuCEe9w-7sV6vouVdQQbPWwDR2P7UcfGBO_zRS4RB8PUrZmLWRrc9s9yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niWTgW7LtW2Q4b0unV5XEkhOTTwz36IEklDrlUGtBMWPztzYdybuFzd5eFqULS7KAiINklAXuhH2DMkuM-A5a10upxBZqhXc5bwV557N4j7OYpG4kLxHeAvC5OrFog8-m-8T-ZEwpSPKRgFgoZoemnStMLhWTGAJIsT_YM68_-REs-ZiZMJXIhZrHLhorMKtT1Wdml3HGc1ILmzW5aCLLxJJJBTg_bR2v-J3dElA9wx3WQSYfeoROG8aL2K7-kMuZieqaFWzntdC0PkW8cxOAkVHweJIW4XoHl5ZZDyuVTn_MNiNVD5kkyIqHpi6g4Avd76kgReoZybealISAembbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbyxTqmG7rkw-aB0CI_Y33FF93gYMV_URbGdBsGVs1i-Ewz-MdhzrmeZpObPjJkFJHbqvqLBxkT-sa0SwMKJESgc4T-xGShGEWYy8BnFFD1w1VNztuOTts3jZRfXpyoWV22VM6N6QGIQ6RxOCHJErjjElXTVNAk4nDHU_KTGqz7Ohn-cUtXAwao-1Otsh1CWQtVEhsXXoUXACQS5ztgdEG7LRrnRwslw4hUIGYHJnX51H0Rlaf3JdumeanCLUC47GvDmLhfOA9ctZXldE8BPt8TO6mpW2dOcpM9fgBjPB49d9q98ccxZjsUS08hTsHhNQ0KXvi5KcisgD2Tsr80CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN4VUFmiJWTfdREE0aR_kLSQiubXFF3dVmeIcE79krVbOujFXNwzMuq5OmIteQaGmgV2DXkUoflMLb4PLcjUJv14fvzHGRNckBx-qOzQLzFza6XgeBBiGmmMW-HULOFsXvcN9x-5slmH32tA3tjkB0aHcUt6-OhY7ubGwmp1cA_YBMIfoxs1fxbFXUFYYqIHg0PkKKPf76RdW86l4p3aa6J529UpcrqMO0f3C0bP1dpmzD7xvM4-ZU7_QA-TsIyykW6a8-4_dC1aYZpxYHefBszfRyFHo3NbLcD3oJ6XUm6F9v9Jtg6gZ-u0Le91Lf9XzcAqLczo7Z3_QUbViVO-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ob8S3L2qE4Cdw906iMX7DQm4_HtxfhWjXpCnLiATYey7C376b1wy7LRaRvmq6x59ec1Ic3DuGk16Kc0wDO_z5wcefIRtcaX1CzLgtwZQi1Q-wGZxMJvnA4V-6b_l-hmh1jNJGCkO3r5tqKfQ5a7vrOn6OZ9_-SMnBpzlU0muR4ddAsofreizcQmRpQ6t1KfU-GSUMvg4fpsu6BTWjpdaRvoZwx4Rh4YkSTbScilFSRNkfmp9EgujdV1pFdKYqutUG3bNtdLj7iS-dnPbB14St2wv1cuBeNpY66OW7QRsp4uBFtc1Zz9vXHdd53WsRtLXQZQXiBWKDpW242PVhLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYlnRrSc7256Y_UqfU6uoBGrxcfkgXVkCYG9S9F3jp41LfO7l4_PY9LyCNBYF4fbeFvKuDKBW7jXEcZjRnLExwX2R4dxyv--6QpwUtvlILVbwU_o5AqDh1UACNRqUgpCREJ8d9DJ9w19zXMoAnGmRPteNzlVTQF_a1wzJ2Q-daaSOwmXRk3weIBVXDmshIB7t1JjwRPQzafPAOw4CHuzG21-2YXJzQld5pNPHX4kjCFvKmf70LdUCfbduPLepBCjcknQARDoqkdn9WHw8gff3NpvmO8qhoel6t_3PIEsGo2nk5Z6EdzAO0WEmqFh3M-xNIV_54T5zumhXVLSnh9sCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5H2EY7BjZEe-8IEmREywH48zhi9XquT0UO8KHE6YlK5ouA-sZiMm4DYIOfpwKCJyZxfRcBDwK4a7OO09vmvHoOKjccFctQCFYOHCVbq6cMZm8LaySauNx07b-myllaXxZ8UeYeGPUujKui_ifO9dL3K70NmU1eld2t97XZ6CJyVUTiOPd1Exwt_K591uez80J6ugf9pYc4yEy7nDBOts_uc2X4s6ZbLHgF3r6bkTl-Pb3nmFiIeik4VcKifqjbfyAfT05nMXJoywySxqQhhPyNGDSXP9xPGs_UIkFnTp7zMMdyIrPqCzgaqlpVHjvvTBCBWdz-aPaXWw2UKlDSVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq77jnUqGUq5Q3qKzvs08dhRzWdk_m_TEnHk0iM5ZyHx1V4lnkvp6IjUkHDDjKjvQA9aJCkqLt3zPtiW7k--7gb3q5xXBWGx6fM0kFo5MfmRbH8JD0ESHNIpxg9Qdk9Baq74t0OA1iMFxwGfeHTQdffW-hSPzUeBio2CBo2DHT9rU_IaAKiSVd2GHyiA2BRx1RUolBS6SQbGytIB82TJ7-nmwOyzP_EN7Ubtg9rPZVD96iipOmN0z8VDazZiRiT0QzaUFi89pZ3R5FxONZDEAiawVHcw8vWItEMbblL8PnT2jSTYQeyvuAbKZzkq-m0cZ_QN_BNl6Mex-fFIPd_2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQFtDntXf1u4goCc_G2dPKY_uiwYU6BGF7pyp13wZqECqSkhkNH5pJZhaEyRbrrg7gNNdWQmOLTz0m0L7oZl8J9abCstZP0Nk2rHrMhcHOkSWN9n3BSCrnA5Ux7lzXpVt1fev6N1s9D_FwVQr75Jv2GQjTxbMK-eC3cAM8DG8XfmGahk9cSFXXHB7DimshMSXrCCzexbs5gDq4riQuKzqM-FvzWFxeB7EMEtb43DFS-C2LT0VOSUJ16sAmzD7eKTKWteoqnQ6DomVUwVsZqH8zN7DOOiE7Rlba4fG7Qy8-nOHzEXVZC9lP6YvyvqbGfCb1f0CdD9iD17czmMSzShqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZaul7h3s3SON6Qs8eWTNCFgZFI5vR_1X9igovKqUOtUho65X32mSPI7Yyn7rswqhkNGiJIsAP9alznqm9mEGy7xVg4sBITPGRN496iIc7RmQWJK0vTAQYWvBt_osuO-dCNfvDXKW7_nwuavkaefeBQstuB_TaAzFseyffGOW7DnlwvAT6UbtdXuLc3sUQ74B5sIpNFgKoqr8C0gY5zISBGxuVANmgzaD2chRZa9nk6MLaKmrugrlEL84tQ2-8zaHtSZFLXfuUIeP3QYkVE4JaITu-EK3xH2hq4r-v5S0tHLbPlTBy7MKsBvO0MbkaopTmApYg2Cu_lvzACu1lPcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDoqHBi9WRzs985VHN81rrlp1XEq9tukswlahwky-r95YNpZHlylCMGPuhXURtu_UhZvjqUG-pnMH1-C9Pf0L7ol-Bn_NUz9qrnh5Jw658klFNSyrw67G10O-8b9uoNxozkczOvdWFCC2l6p3vimplnju4myHeTRjsZLtIO00-9kFQL2HAdn2io7wvODgCcVivjc-RVsK9i-5v7NtPjTRPZFQeDkZpiky-AT1PQHHb3MKZzBINFS-l0xsC-YFXmMYp3SLai05N5CcoqJtVHfC_xkJLIXV91cQVQmHD2vOaaxzOcvEXBfNOWOnHCysNi4PKTulgKqq3XxsOVmBa68oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=k41IUuCOhgQ6Xgc2POgUVWxPFA-yCPhWL4j362auNbP8oGfbff_AKEEQcEm4XxptuRAo4XPksxqSKZ0I8wdZ6q0HENTa1RhAqjzmozghDfX853QGM1Y3j4WOnZW2tUG3wTfTDfN5ib9p6BA3tHOA4zoBLFRaif0uSXcGCGv4U3e9TUopYXrCjKlxHun7OB08j0UhXc_6Wfa2BEX4axBixTF--hBQ9IwF6geGQrcM8XBEQOsqy07m6Nmbj3Gr9Xx2X739nJz9i_NDJVoeIFZ-7qp9lJn8x86zpFsqE_q_FHewU9HSg9dgxyZj5-AhujRnfbnS7fznH1Jkv_SdPcg-ahU8agpwnAKo6sUNfB8F_A3hLgP-dsCDvgX81vF_AkpM2iunpUNHlNUtQieUUaZGfqGTEkbqvl9rLPAqbj-Cq1rPw6UUO2m-SIzUcJ1rxtIHlS9AcMVXZbpSlOIj00ztLTCAZhiQiSHm-7NsjMdBeHV7K2ifSN6ObqwxkJaBHYG6rOjlxFDNefqM2iXalsR8sdCZLKL3-yl4DwzWBxgjOfL1C9FdvXG6Z4w_6OPya3TIHobHGpf0z93dPCmpw-4-f8nFn1VoJQVk8GJfQD5R-ELL_yvR94w2gIB0f8uTSpa5aobPkv4ETTY4E7TwW9ClUp__XsejqzF4bCpLLmwbKIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=k41IUuCOhgQ6Xgc2POgUVWxPFA-yCPhWL4j362auNbP8oGfbff_AKEEQcEm4XxptuRAo4XPksxqSKZ0I8wdZ6q0HENTa1RhAqjzmozghDfX853QGM1Y3j4WOnZW2tUG3wTfTDfN5ib9p6BA3tHOA4zoBLFRaif0uSXcGCGv4U3e9TUopYXrCjKlxHun7OB08j0UhXc_6Wfa2BEX4axBixTF--hBQ9IwF6geGQrcM8XBEQOsqy07m6Nmbj3Gr9Xx2X739nJz9i_NDJVoeIFZ-7qp9lJn8x86zpFsqE_q_FHewU9HSg9dgxyZj5-AhujRnfbnS7fznH1Jkv_SdPcg-ahU8agpwnAKo6sUNfB8F_A3hLgP-dsCDvgX81vF_AkpM2iunpUNHlNUtQieUUaZGfqGTEkbqvl9rLPAqbj-Cq1rPw6UUO2m-SIzUcJ1rxtIHlS9AcMVXZbpSlOIj00ztLTCAZhiQiSHm-7NsjMdBeHV7K2ifSN6ObqwxkJaBHYG6rOjlxFDNefqM2iXalsR8sdCZLKL3-yl4DwzWBxgjOfL1C9FdvXG6Z4w_6OPya3TIHobHGpf0z93dPCmpw-4-f8nFn1VoJQVk8GJfQD5R-ELL_yvR94w2gIB0f8uTSpa5aobPkv4ETTY4E7TwW9ClUp__XsejqzF4bCpLLmwbKIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doyZwLGTbSj_isy9BJwcWD1rrjFEYW0cJF9IGT1cWDBJAtMsbJSn1VVezsqAXs0gOyr5BpAomxJIjObf82Pk2H7uu3G-M6L3NdvAd16pMwJuJt0tzAZd_DO8n14GRnCUtPl1SYFVstBvLZyjHsvUfCTItItou2WXw3ef4gnUYgfV2NkrGdF8NCFmQnNdtM7oJWT80W4xNoRMgPO5WeNIWsA0lQoiTVqZ3Ws6amcc-kBnMeB0AZkyDem9uNNWB4rO-f0ikce-gw1VZOkv0eml3KJfetAxtD6KBg-AfR6ZbU-Y1eZ3V6auuX3e83uo9VFbaa_bkaJ-lfyDMHL9XfObEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=VGC3cwn-V_aHTGbrM1szQ18BwZat9C3WVX6rtVZ2BBqbA4gX-NSzTJCBh-ReEOwlPUEPDlAmBQQRvAuV70sSXjB1bP32jyYzN9MjlLwzLW7C_jXNoqRZqH3AtXJGkZfjjCBY13NcXjkbV-PQyB5Cf7EmNBPa5pV_FMNpbI7nH3X0OwcfzdJmxgkxI2l5XVLvIec87GPjMTC9ZB9wCMg9MNwPGyAEEi1XnaBcKJxc427wF2ZyjP7O-FHrHkPywqEfuyz0WmYqEL9Cwa0I7eWvnE1NW6KxrPR6inIkdwgiCa6WsyPDVlC23Szggr2IQzNasOdFmdEzqfOAodPpDg_H8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=VGC3cwn-V_aHTGbrM1szQ18BwZat9C3WVX6rtVZ2BBqbA4gX-NSzTJCBh-ReEOwlPUEPDlAmBQQRvAuV70sSXjB1bP32jyYzN9MjlLwzLW7C_jXNoqRZqH3AtXJGkZfjjCBY13NcXjkbV-PQyB5Cf7EmNBPa5pV_FMNpbI7nH3X0OwcfzdJmxgkxI2l5XVLvIec87GPjMTC9ZB9wCMg9MNwPGyAEEi1XnaBcKJxc427wF2ZyjP7O-FHrHkPywqEfuyz0WmYqEL9Cwa0I7eWvnE1NW6KxrPR6inIkdwgiCa6WsyPDVlC23Szggr2IQzNasOdFmdEzqfOAodPpDg_H8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Y6Fla1XMPborb0mnsH0Sl3ys9VZPO55TWXRLbpllpIp4sYCtEg5GMhmYd-c4IryZlDEf86n0vvWohx5CWV5hk8iDvVxawaTgKmzR4s45Nb8DZR8GjOPPydrCxGxCCvrEjnu5K1apa-_4LrbzflQkUsBk1vTUWCqF_h1Qdbg1lGMcYx9PT8_h6g5QD3_ojgW7MEWDF0NuiEACwaKi0ogzUtgtGnTcbs_bLslocw7yl4vj6Bx58aNsHMjvRZby3pSdYoP6_-thZvfkhV4LDbInW1Ztgqsm_XW3149__56IRPSl06fa7g2RjWGQ2vYulgPmjrqiTaBOPG9eDHuVssKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDcUNuu5X8nBkiuTEt_w8MWj_y2_Ark0BrOQYn1iLizCtRymq0QhYydgDN16GYOT648d4D417O85xVcoJl4uhH7qA4KwfCeqo7IUjALfR2_Kk-PKGjkxiMsbPfLB-Ba0oqJenysnlnhyvFIY8ljW6KWmOkQTJFfzuhLT51DQCCAAEYI_e9DYpvUfv7pigHQAMEACGap0F8lAuaoHUyx2KKj4CScO29HWM7R2LrS3lOrQl-eesgaobzkMBZ9iXFAKKg51BunsfyKTw4hpe7JbenOvZy_ddY5Bp7LKNqB0PE-cUhhiMeBqXMgIJccUGPl2EerNJHpMnM66v1sIWfJr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=C4lz-UmfADm01i25aVr_NPEfON77DUdkLNG7zUJtsWg5DgTr7X61LbHpkw30T8e7gS6RfuBz9piFjMPAnNFsBiZm512oHcG1dzy4IfFg2rFMU2eqJmk5UHOWPljlbPOQYqVbfBDe2xi5gsLdzItqgZMcrJmKOqGC1eizR8yTJMRpn59UPH5JZ9zLXVyfzvS9Cbit2ul7NyTlYXTa8yQSGXIFL8w1AYyczV6U7cVnQcHow-6u66aND5irusV0NDrHygc8rBpbB5-WPeHqJx0yDYldT8OUjjiHx6CVskBUSSKer0gZOIoMkbGYT5KjuToj-S8X425OELacWrPP-eCvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=C4lz-UmfADm01i25aVr_NPEfON77DUdkLNG7zUJtsWg5DgTr7X61LbHpkw30T8e7gS6RfuBz9piFjMPAnNFsBiZm512oHcG1dzy4IfFg2rFMU2eqJmk5UHOWPljlbPOQYqVbfBDe2xi5gsLdzItqgZMcrJmKOqGC1eizR8yTJMRpn59UPH5JZ9zLXVyfzvS9Cbit2ul7NyTlYXTa8yQSGXIFL8w1AYyczV6U7cVnQcHow-6u66aND5irusV0NDrHygc8rBpbB5-WPeHqJx0yDYldT8OUjjiHx6CVskBUSSKer0gZOIoMkbGYT5KjuToj-S8X425OELacWrPP-eCvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=baV14zF-TLhMtEA7BzjoQwYCCnFmM6xQ24igO7rjoCBdGM6ersNCakxIURGj3bEAsmB8J0qqCgdL1JY9UtMpaO0PIPuyJ0fi9q2YliJw-Bl55Kd8iWx0HWpleMaLBBLbnZZWJtAJ2-Pm13481yqcjfK3NfVqKcbDMmqEjl4sWgXpqoNAMdFor5pLuj4whzOJpJQce6-tBR7A_yeZFlRcATRNIdr1ygMDCH3E5h8Fziw4Rp13Dl5nNP5vCL07xv7vW9iEKqMPDC_LxhdTtTTFpHVWNG7lkHs3oQ6ygG7j_46jtotTIyy2hq3SZEaiYAq5C3YWRsJxT3-b8zym3yamLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=baV14zF-TLhMtEA7BzjoQwYCCnFmM6xQ24igO7rjoCBdGM6ersNCakxIURGj3bEAsmB8J0qqCgdL1JY9UtMpaO0PIPuyJ0fi9q2YliJw-Bl55Kd8iWx0HWpleMaLBBLbnZZWJtAJ2-Pm13481yqcjfK3NfVqKcbDMmqEjl4sWgXpqoNAMdFor5pLuj4whzOJpJQce6-tBR7A_yeZFlRcATRNIdr1ygMDCH3E5h8Fziw4Rp13Dl5nNP5vCL07xv7vW9iEKqMPDC_LxhdTtTTFpHVWNG7lkHs3oQ6ygG7j_46jtotTIyy2hq3SZEaiYAq5C3YWRsJxT3-b8zym3yamLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCismRO9qXhsTPEHubRJwo6Gpbr-8RkvecCAt6IrTGqimmtsMochdy3kaOd9wg9M562Y4hUJzZR2jw-AvSc4O0F4Uwid5RfJlhMLiG7B05SAJJhLdcwpteZsW10iP98696tvwqsZFHPrjinFTeg2-FUCw_aruvEiKXNJQvqG-ROF1qyPuz-ajwdxIsA1-Eb7nErpNmHWIq70x0b1UuGS8DIS-fCE3lr0ANz7_AowrzYQsk3WrVCXFYAs0mOmFJX6EpKX0Sr8VHo-A-ybSD_-auXRI3TCw7pSb7nI4onkNgbbwyQJ_78tpU2VgOKIEERtsMyxKFSSAGJIcSErlbq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuABEr23abHGi_iuO5ht7uTo4e0SvabaT_YdnAFzClsPlApnX_5GEbMMpJGwfupH8fDQKVW1ckg9T54uYPCF2QBMFlzT7FWiaaAuCJqQ0mnDQGQQMoEW7E2rhY3HBfrxl6gh5yfCNQ-T_-rsnFaSEIVxS2Wy0mYRiRIZ74t-KZJ0EPdmJa-JxeU1aKvVFhql1-UDq9wPIzncQnG71H7RpO0LrhDzJ6gWrQnqow9yPppvoR4rYUWMwHxIkhGcesxfJwjrtpEkwqTsJ2q3BBl3uPpcXlCGjWhLZgWBi_qXPI2sbMWjkpzLuP-qySpE5ijP-OfVkNCm7qeAte8SR17L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdh5mDyGkFs6R8YjbsiAJ9B-bjLcgvjMvWH_XRZuDMBOIIO3xs8Dtdy3z_ck3C5juK0qLNP2Hl0CraLz5kqvKodrkvmY_zzRc1MEh1ib2A5ZXeSSAF_ZuGcg-4XElHM3EChVsxARCrs7114wwMu6u2NjBjngd50HC3apHA3v3ywIW3FeH7Md8xjBvx5lf3pppeqRrlfHcneSjfEyIRFWL3jdOsAY5KXuk3IOKYVeIixd1-7a7yXi93i1D558hTJi4ZaO4Hcq9q-h9rzrpxKCqguL9tKX3U42mh0acKSPoTiUEEDp2E4wwRP7Z3TGgdXpLUMxbhi08le47ZqqX0n_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=vgZyvIUMz8mBw8nkfpT3KRIC5-nvYCkLUZI6P__h7sP1iFgsqaBEYdoG1yoZQc4ZsdLc8lArerEWRtr0caFa-UCKB9PhaPFURd4Xh2WWa7dw8BnHT2_n31cW7pcV8TMpRFMLtiwZPvj1Xb4i1vSFSmU2ssYuo-q2__7-ONq9IITIpeslvy1MJtehylCLEFoTIlgIUbA67yqcaKuW20Ae5Q05l7lTYESeAhlBTo8i9PYjMNnAx1bmsWp_fQaWi9t8KGU1AsH6hfuRcVCARDG4d-gR8qi3NZBwhibj3UKLo_fXPdFFxN58lY63EWNBGfBnrTMeHPpoJZuefI2gSbZRlF1KkIX-eCLAxmfn5wct0KaXiGF_OEk6F6mxKHsizxdIqGIoVg95oRpHoyIBYvHeVErEBGX06zYRPoKt9R9SQVH1uGHVl6PMnWOlA-JaNwIVxJ_EmPbdRlN4ZQTVJlqYSs44jX8JFwIJYPjB2iOBxTaA2ywyj3qvnuya-f8NkBbCYlRMcnLa8-Nx2OEYMtxVtrjLnTD408QMU3lO8SP_69JG0iOQyS4riiva3Sfi8hEtFkgUkvyaYC0FLmgBljgn0GCpCGa_OyxRB-uqBNu3e4vqcrg2RSR2M3NYd3lMaM_6qNpIC4DPyT5mRN27VEz68pbAWhnx59MMV2SjW4fzo34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=vgZyvIUMz8mBw8nkfpT3KRIC5-nvYCkLUZI6P__h7sP1iFgsqaBEYdoG1yoZQc4ZsdLc8lArerEWRtr0caFa-UCKB9PhaPFURd4Xh2WWa7dw8BnHT2_n31cW7pcV8TMpRFMLtiwZPvj1Xb4i1vSFSmU2ssYuo-q2__7-ONq9IITIpeslvy1MJtehylCLEFoTIlgIUbA67yqcaKuW20Ae5Q05l7lTYESeAhlBTo8i9PYjMNnAx1bmsWp_fQaWi9t8KGU1AsH6hfuRcVCARDG4d-gR8qi3NZBwhibj3UKLo_fXPdFFxN58lY63EWNBGfBnrTMeHPpoJZuefI2gSbZRlF1KkIX-eCLAxmfn5wct0KaXiGF_OEk6F6mxKHsizxdIqGIoVg95oRpHoyIBYvHeVErEBGX06zYRPoKt9R9SQVH1uGHVl6PMnWOlA-JaNwIVxJ_EmPbdRlN4ZQTVJlqYSs44jX8JFwIJYPjB2iOBxTaA2ywyj3qvnuya-f8NkBbCYlRMcnLa8-Nx2OEYMtxVtrjLnTD408QMU3lO8SP_69JG0iOQyS4riiva3Sfi8hEtFkgUkvyaYC0FLmgBljgn0GCpCGa_OyxRB-uqBNu3e4vqcrg2RSR2M3NYd3lMaM_6qNpIC4DPyT5mRN27VEz68pbAWhnx59MMV2SjW4fzo34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POcuLBtdo_ZB3o8K1EWHBYUfEc8H9RsGvCNxosGJbpAAXVdw779bPPjh9AVxEWqBmfM8voo23ykwfblSEImyM4o99p9Vsdj36jXqNUk_H_KQz4smijl1GYL67k3bFxentVgTqPKXBzHv3RPBgWYKuLQ_gpQFAIuHMI44zburk5TcOJCCpRAWYpQhr2buor2ZNfWjemyasbxdrW5FXoLQ6aGB1NEKxHQONZwq2dj6hwAUeP778FOT6gi_jKnqtoFv4V93B2TOb4tPFArpz187h7os4qzevasnp7BYQQWoqn4vKj2dtbmqwcdy2QuOCXHcUe7TdZSTHgOkb3Fu0iSONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHdR15plks81JZdTlR4A_f68p2w-kcI4tEJPW4FNToTE4aS0Yp2skPZ9AJooq6XADRtBoMob1Ti3e2BlI2pLScFjHJQXwOeB2jJD6Rs4jcoSCZFMQTi4lbvJ0o4frojlHrJSOXD6kwnYXMYRAhiWW-KySc_HP_TROUZCYFzNjLQ-NL71m6Knbpp0ApjJyGwEF4HaD5Nhqh1HDmCkcGdf01gp3d5i9WonSsbLmd2GxJ34JHCl4O7ndYGEgVuQ8jBnBhj-ImjxdB6tZFSVrD5iEYt3eCDeGflLx0DWRyrtXc81gmHR-2sIRl0RTOgafRPHupcrD5Zir340sT4KSPVIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_CUzeHQfX5mgtSGSCwy6nMDyoZMSmveTcTU8mX22OqCuqvlBeoXnCMnKmSCJFtVIUTYy-WYOyOw5sfguRH7FAY90Uq640ebcHmI3_pBCJrs5k2rX8ff0-_6pJ-FKxg74lB4T3qWTnRW9jFahkXkg8lOJzzS4bu43rWxiCtYTdvvt_qF3GYOJ_yUnTlH0NfLGVMH4WGKRsFzg3GHC_kW3Q4FptTKCiV2nr0t9cnm2Oe5tUe0Mb6q0fVWmXZP46dOAraXnR8LrXXwdomxoZPFgIFFcCWuxzh3F-fCpAQ_Sq7AhTdVJNDB_o1VfBkPWHRtD510oeApxq7Ve1iN4yfC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=YPaJD36KxIVV2eZaeJRfR2fg-lCK3MWpigUBD_uDiUbW2W1LZbwyjBV4K-7wzJUl9-N75HQMQ7Prxunt_AGEIchZlFO1GloSHPe7yB54Eb4KpKKHcdKFD8_qcxcAAHqNaX5q8vlbiWIOVCV0i4Td8dCC3vFUvW0J1TPidh13n2_dI8Hvw5imT0Rx3sQt95V0VKm4_pOTs6VJkXUZUwe95vu2ceg5MQUyYg4OWCg7oHWZaXvQZBLTr9f7eIac4TDPmdC99B4AiOyzhldYYHqYY85b_aeeLb4Db_qdCSO7eAPTvKtep5Kz_oVyCHbrg-R_rLYPqEv4SNFCwwJE4KYbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=YPaJD36KxIVV2eZaeJRfR2fg-lCK3MWpigUBD_uDiUbW2W1LZbwyjBV4K-7wzJUl9-N75HQMQ7Prxunt_AGEIchZlFO1GloSHPe7yB54Eb4KpKKHcdKFD8_qcxcAAHqNaX5q8vlbiWIOVCV0i4Td8dCC3vFUvW0J1TPidh13n2_dI8Hvw5imT0Rx3sQt95V0VKm4_pOTs6VJkXUZUwe95vu2ceg5MQUyYg4OWCg7oHWZaXvQZBLTr9f7eIac4TDPmdC99B4AiOyzhldYYHqYY85b_aeeLb4Db_qdCSO7eAPTvKtep5Kz_oVyCHbrg-R_rLYPqEv4SNFCwwJE4KYbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXolmes_2TNDShfNPWDJd3BLNg_xKYXgWnrkMUouPFNynIrhB1JS0y4NapIfAAekFHY-2qeckL66S5qYLl1tx9dIkPiDCsTmgkf2vCDQMexRr9K2oZK1LdUSWbA8cYWl_otyvVbl4XvA-Se-v3ITCUFpmXnIq7VbaWZJLIa_A8Elefpg55PVddMNd_urMPdcUfJcJEeHD7tQkHaiR0wQVvmk5GKHgmEXZyImCBiC7-5vcZWwWjDrEkKypv9RME7fw-3s360KgVzdbj_xMle-IVHPfKTLH47yD9mP4VrCaToBm0yQkDLSju1nd0MKTApkjINMayc7FcbLHg_IfHK7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
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
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=Ey4T_TPiM-85xMnJiCvPOWhbGc-aXJcZBWEAgtcEZjz5EzhyVXGhkNp3WCFG9RFlLjXkdFuL1rqlJF67vAwhdWeOLkR6CB7g8FpnRk7oakxZb6ZkFGyf4UYZZXrJdec7frsFsXSQgdhxBqeFn3ELvF9ZI0QmWtOCYOQqC9m94KLZcXGMY3AFdElDVS7DGkzS5iEy-mngcQLoZ86S_e8-KvKsIBkT8nQdDd0-WMBQ7J9Ht0i8HihKodFScZZMzJoR8jB_z7mTVWloo813HiARKnG1bXqgKo1K51VwZNENmW-HPqMM13DxlBqrasMVfMMbtAoRZmJ-WLp_3od_4aqAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=Ey4T_TPiM-85xMnJiCvPOWhbGc-aXJcZBWEAgtcEZjz5EzhyVXGhkNp3WCFG9RFlLjXkdFuL1rqlJF67vAwhdWeOLkR6CB7g8FpnRk7oakxZb6ZkFGyf4UYZZXrJdec7frsFsXSQgdhxBqeFn3ELvF9ZI0QmWtOCYOQqC9m94KLZcXGMY3AFdElDVS7DGkzS5iEy-mngcQLoZ86S_e8-KvKsIBkT8nQdDd0-WMBQ7J9Ht0i8HihKodFScZZMzJoR8jB_z7mTVWloo813HiARKnG1bXqgKo1K51VwZNENmW-HPqMM13DxlBqrasMVfMMbtAoRZmJ-WLp_3od_4aqAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=j7MjQZAHepuXpbV3EcA3Xh2aXwSjQNfhxHtrTsVsKx4mC_Kpk60L6qNFvW5txcxgmbLD7RdSc55SYbjJIYPaXsUUqOm9QS8ggo4rjCno50_VFGkNIe7fjFDBEHx8ZxIbrm5hGKEYbNDV_mY8tsJyGTkEflFgErZHdiI9ywgvfzCZ2hMmd4JDyjGPIVTf7NMBBRq_ClsFXz9zDDVCgQxKhroS7mJ_895jTbiGr8P-ILU8THQH5LDo0tKagwvRTt8ZqlyndthcxWCz4RmPxeQ-FUuiiAVPHUdtjWCqz4ECQ2YD_A6mrq0-wlf1uRfQMGmxs9aU1rYLfPLXtTDhgKu2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=j7MjQZAHepuXpbV3EcA3Xh2aXwSjQNfhxHtrTsVsKx4mC_Kpk60L6qNFvW5txcxgmbLD7RdSc55SYbjJIYPaXsUUqOm9QS8ggo4rjCno50_VFGkNIe7fjFDBEHx8ZxIbrm5hGKEYbNDV_mY8tsJyGTkEflFgErZHdiI9ywgvfzCZ2hMmd4JDyjGPIVTf7NMBBRq_ClsFXz9zDDVCgQxKhroS7mJ_895jTbiGr8P-ILU8THQH5LDo0tKagwvRTt8ZqlyndthcxWCz4RmPxeQ-FUuiiAVPHUdtjWCqz4ECQ2YD_A6mrq0-wlf1uRfQMGmxs9aU1rYLfPLXtTDhgKu2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=q8oLpYExVVcaHa8ajpijzBIqwtUkK9tHS_RWpS1Px2cLPAHu8c-YGJbmJ-eFMxF6vuDamQQ4cs46zqJtOU_47SXM0zMgaCGr19C4IzPC31sYVyUL_vNCecg01C8XxZkLeAVLwXs-IMW1nYOCV0QAB9uBHaQbJzrANePFJVwTGygvM1J8ffGJKswQhmQgKGUI-TpQwuQdZ8fW0zyhjCz1n5ytZUtKrtMPq67hrfYYUzj3X6LjJqFiDhiUOujFI_AS7wkbhGEvnzT4_WByV-kR3HiEus3Dx7T525bLWYQWXjSJbokJYj34xGQNpAatM9jnL4CJHcZvjm-pJwiGdB0C5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=q8oLpYExVVcaHa8ajpijzBIqwtUkK9tHS_RWpS1Px2cLPAHu8c-YGJbmJ-eFMxF6vuDamQQ4cs46zqJtOU_47SXM0zMgaCGr19C4IzPC31sYVyUL_vNCecg01C8XxZkLeAVLwXs-IMW1nYOCV0QAB9uBHaQbJzrANePFJVwTGygvM1J8ffGJKswQhmQgKGUI-TpQwuQdZ8fW0zyhjCz1n5ytZUtKrtMPq67hrfYYUzj3X6LjJqFiDhiUOujFI_AS7wkbhGEvnzT4_WByV-kR3HiEus3Dx7T525bLWYQWXjSJbokJYj34xGQNpAatM9jnL4CJHcZvjm-pJwiGdB0C5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxTFqGq3py3N8umYG31VP7pFPYKgKvJQunc2pluDiF_M_m7Wbsi-1dt6ADRmehCTXNnT3LxYYKFBr5jVJFb8wDGBjL4oxRXOStBQY9PHUCG73g9pu2monTapczjxMzposPqTbbBchfpM3tG4fbLnNG50uQcWaW12gHj8qlZUOVHieRNuFETOZZgXqDvtUSfvfvLcbAQOV4DgT5q-pkYUFu65OkYAM-Rbv0tSp-VmDYAXvCB09I72PxTgqllkKJddNhwLo4DYsQorCLfM8eYdvjWZ1TU11Pb4i6pcFjMlPuTdYuprpKwlCeLDL8sdBGS5b43fyY35vaSo1LhS5g7Z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=i52DOr6XFXKDT9CopVZeR9hQP6beLDmGnbzQ-0EzfWBtMGGUHlb139hX3n6wHlPDu7dWDBsgcp5IBv75N-GpyAuFyIFsQY70RJl5twoELvm8kIPSye_KAx6Exw_UcRxwR-Etxlbh9Pz6vsAtrrPnwuvdzRwv_f9xSt2p_HdlO9EoLOenrpukMWxeBPdXFzH9fbMv3XMFF8my8R197pOt33dvpWO98pGP0J4nUN_-kqR3O7_fKanKD2W5saLLbq48e-0erS4ROYpPKbD0hOYYGUYpk4W7Jbd2aDGmbmLrK--oV_5vJMiJpl4yKXkt-Zp7XPocBIqeB3i1qQj54_z0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=i52DOr6XFXKDT9CopVZeR9hQP6beLDmGnbzQ-0EzfWBtMGGUHlb139hX3n6wHlPDu7dWDBsgcp5IBv75N-GpyAuFyIFsQY70RJl5twoELvm8kIPSye_KAx6Exw_UcRxwR-Etxlbh9Pz6vsAtrrPnwuvdzRwv_f9xSt2p_HdlO9EoLOenrpukMWxeBPdXFzH9fbMv3XMFF8my8R197pOt33dvpWO98pGP0J4nUN_-kqR3O7_fKanKD2W5saLLbq48e-0erS4ROYpPKbD0hOYYGUYpk4W7Jbd2aDGmbmLrK--oV_5vJMiJpl4yKXkt-Zp7XPocBIqeB3i1qQj54_z0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=Kju7SaVoub6ddIc-qE2xSJ5w2KwI5bgQXfG26RZl7KnY8x3MWvXmSD8PRJTKhL4IL4ziPqum6XA-V7NDHNF5SJ7nvnHyjNjwN3x0_BAhp-0H_ZmxGB1dKvMpIt3yBXpmmvYeBOu-tJFFufA4dYx180DhL4m4LR1WD78Zb2aJ5GxPOGbUKv-fblHsmhT_trfC1FOLoAB8e7kdBHWIlvkOu2zqUCmLVrTicLTYmdrhG3Qbd3vbLbxPCbIyPN-JT0-ClGpvvE2LIu41VP12VKK-djuwpn2x-6qVujR8lV5SDaF0JiT_5QQxgfwJTqMyPO7XHaTBtvwugqFxlkLCjiuu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=Kju7SaVoub6ddIc-qE2xSJ5w2KwI5bgQXfG26RZl7KnY8x3MWvXmSD8PRJTKhL4IL4ziPqum6XA-V7NDHNF5SJ7nvnHyjNjwN3x0_BAhp-0H_ZmxGB1dKvMpIt3yBXpmmvYeBOu-tJFFufA4dYx180DhL4m4LR1WD78Zb2aJ5GxPOGbUKv-fblHsmhT_trfC1FOLoAB8e7kdBHWIlvkOu2zqUCmLVrTicLTYmdrhG3Qbd3vbLbxPCbIyPN-JT0-ClGpvvE2LIu41VP12VKK-djuwpn2x-6qVujR8lV5SDaF0JiT_5QQxgfwJTqMyPO7XHaTBtvwugqFxlkLCjiuu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=CyLUNVcm8L5qStMhSqa4ne-fvJpVfvf-Wp3YnyZcOOgUdGb-Zm24NeveWVLCDVvIzYLaH3AgcF_pKIQSYNkIzrOTkB2qjLXFV8TWuHcrs93KI9GKKhH7EqvKNkloN6qo18buFb-7HY4zN5Md66YfUtjtZhrGG8uJKD5ym1gJkU6ZgAoHbeeFSrsqoxcJcDy0feBtJMNsqby2Xlq_WF3GxLB7Z31SfSmSG4oCcVCbgKImjXxynsXYv3A9hnDefUHZ3FiptlL-3sd7Z8u-CbAz4e8bhHek2GPOhksaZIHsFWQPPwiviFUmvu_PSksKjh70MEXMyYTUDN-dlMpM5bcNRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=CyLUNVcm8L5qStMhSqa4ne-fvJpVfvf-Wp3YnyZcOOgUdGb-Zm24NeveWVLCDVvIzYLaH3AgcF_pKIQSYNkIzrOTkB2qjLXFV8TWuHcrs93KI9GKKhH7EqvKNkloN6qo18buFb-7HY4zN5Md66YfUtjtZhrGG8uJKD5ym1gJkU6ZgAoHbeeFSrsqoxcJcDy0feBtJMNsqby2Xlq_WF3GxLB7Z31SfSmSG4oCcVCbgKImjXxynsXYv3A9hnDefUHZ3FiptlL-3sd7Z8u-CbAz4e8bhHek2GPOhksaZIHsFWQPPwiviFUmvu_PSksKjh70MEXMyYTUDN-dlMpM5bcNRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1nI4Vgkk5WALlpWZnnvmIjuGCAtyTm_XikAzOkn1aPPBFeRSuc6ZyprsNdPggBXFm2Xjqn8WI2vWrdA-QhFeIVFxDneCQ1tcBpu3Geiamb6ni5QcO0u1Bcv-CExv_7F5X7P8j2Q-yxRqHehR0ir2B03PXxaSK32Shh_5vNzLXpMBvA5602GYxOkHdTccR7l7apFmJFqNjAQJ398JsL2_5IQhPqVz3OLTiRGUawtnFFpgNvwJUEldrEpsKZAjattCp1SyWOrvKDV-gB3jmtEEo4e4pJd5VDIzYcv9eGkkUJ9kQSnFw20KTnNNhdrLKaW-gLChOq1wLJj3q4Ll_efA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX-TwQkNW1w7jTNqCn_xFp8yfoO1ELiovbge7isdomFlRyNVf1LgbFBMvnaOowmIfug4Wd4FWm-HDf2lGpRhl5McNGyUgeKfgTAS63xu-f3xWmOcMMW2lPAzbmyXUS9D922nZwW9dVTLtQGyycuJfyLc-6_XGiuX5Ybg5JKjPEd7tZUkg0tVUyDUhvKKELlUkOsqUVy2gOTnpZMy86c6B6GmsQEqG91vQSWNMCl0NDUxCr5zM0RuX8uQtfQjTzl0bgrQ9sV8NivVi8pv5VKu4rzMOepEs9sMQCR_8okpz6p6WP1QGwX_hyfoHjXVlEbii6itL5xe4cE4dfGeMrimLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=QRLaPePH_Cl3dqCfMZ49ZmznyOyR7vTre_kmavtlF-3DaFaRf0WLOFBhNi-FcAfvn5A71zOyHZSgDa_HbfQgA00UuodOUsTli4dW4Ze3v-wbtM1cqbyTHYjRV826Xu2Y3Si5D_6yiICoAoeEgEauv_3Y_niLrWKxGgyLW19BCGeXewg8dhTlawOAbyKMEiCeVfhpFHbvfc8TODOFs2oCNNu6pFkpwXYFHJWA5krwsTg3bqzZtQkT7IvCOJZQxtq-rJVnosoT8flkYP0GpPb5zuw8tHJ-U9JofbCnNxZgle6Ae1J-H6ftIz77IF9k0vA9rEoEjAnKTal3aDSE5W3mCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=QRLaPePH_Cl3dqCfMZ49ZmznyOyR7vTre_kmavtlF-3DaFaRf0WLOFBhNi-FcAfvn5A71zOyHZSgDa_HbfQgA00UuodOUsTli4dW4Ze3v-wbtM1cqbyTHYjRV826Xu2Y3Si5D_6yiICoAoeEgEauv_3Y_niLrWKxGgyLW19BCGeXewg8dhTlawOAbyKMEiCeVfhpFHbvfc8TODOFs2oCNNu6pFkpwXYFHJWA5krwsTg3bqzZtQkT7IvCOJZQxtq-rJVnosoT8flkYP0GpPb5zuw8tHJ-U9JofbCnNxZgle6Ae1J-H6ftIz77IF9k0vA9rEoEjAnKTal3aDSE5W3mCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQGus-CtaH5LV8EYEtmF-34gY7gn4-JDsxMA-904WOIj14zbKwp0nDaKeW72bKkBCxd7YJwwJDLw7l82uXgfgk_iWHgojnbls3QV-6o3BCayRMGRSHaMYTAsoXE-S8n70ypZ-V_F3km6-xOGlrTCo_pz50OTrPRurk5_40l9tGRxliI7fSMJmat3pZy0v6SORzp5QqwVAALMvZYUfWJ-k2RFFjYuNEPbT_ya021uQ9ENIHqm7wcXnGt7UwG7zDhnxkqV4zn5OCbuhBSijwmAbTAnPIMQvXx31fyUJiiOyonVVrKJApdGn430WOWZWh2vKkR013qiEYvmTA6KgsrSFZ8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQGus-CtaH5LV8EYEtmF-34gY7gn4-JDsxMA-904WOIj14zbKwp0nDaKeW72bKkBCxd7YJwwJDLw7l82uXgfgk_iWHgojnbls3QV-6o3BCayRMGRSHaMYTAsoXE-S8n70ypZ-V_F3km6-xOGlrTCo_pz50OTrPRurk5_40l9tGRxliI7fSMJmat3pZy0v6SORzp5QqwVAALMvZYUfWJ-k2RFFjYuNEPbT_ya021uQ9ENIHqm7wcXnGt7UwG7zDhnxkqV4zn5OCbuhBSijwmAbTAnPIMQvXx31fyUJiiOyonVVrKJApdGn430WOWZWh2vKkR013qiEYvmTA6KgsrSFZ8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAX5kVlB19sgeFK-BiglvZlbNUBxY0maCh6jbNDkhvtbftHxUJ7_rWAjBu6Fm28WYBisCNCDyIUhPBV_OGmR-uyah4YFnJTXbxgXvd4BuXKWUjXPiAkwBM_mSpDidgg8nmJsNUW0qvI9Y2_x3qsN7O3kqVX3ie0qEH5LtQU-poleFFd5omv4H21VDskPM-mfKXVlK8WY75R-LAPnwiDZGZoO9S4iBY8J7MLb5k_DRKQoTtEuggBFIlBGw-CORQuoInm2KYB1N_mUA4Ite70rPwUHa6eWki7mLU_gmzg5iJsjB-jdgkM9tXy4-QHYKxq81yw2dNDK7aeMR5WyAPuzfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=hg76Q247NWy9-v2_INImnIVdLSf8DtTcnVCad7NZ1snHG3NG16DCu7-zfzJviGig2pskNXPnE3n-iGS4bmLciqk1ARiAPJuGfvrE9bWKn5UfGU_vVRWV0PP0Qxrh8YIfBxPvKmg_vjQw4BPpAdFy9volG0DspsiZqVnZBym7P5ItOXV3hqqelbOtJmYsEY31aVkdBVJfRYNWCJgAYA5Fo0QI1C9vLf71UVh0f16pqj7WG4yiCyY3Ll3vOg4kttGG_08uRhjXtaWH69GxFB5QPl26w80-G24KgsSNateLj6sIpJCwJ96wbnNg9apL4VlGVMnI77jAQAbRof1yKz6iVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=hg76Q247NWy9-v2_INImnIVdLSf8DtTcnVCad7NZ1snHG3NG16DCu7-zfzJviGig2pskNXPnE3n-iGS4bmLciqk1ARiAPJuGfvrE9bWKn5UfGU_vVRWV0PP0Qxrh8YIfBxPvKmg_vjQw4BPpAdFy9volG0DspsiZqVnZBym7P5ItOXV3hqqelbOtJmYsEY31aVkdBVJfRYNWCJgAYA5Fo0QI1C9vLf71UVh0f16pqj7WG4yiCyY3Ll3vOg4kttGG_08uRhjXtaWH69GxFB5QPl26w80-G24KgsSNateLj6sIpJCwJ96wbnNg9apL4VlGVMnI77jAQAbRof1yKz6iVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_FfRhDMPHdgbYYID0DGHbS5_6MvMiNiOoxfKBnXpSFWGSJnj7tTfHotaaEZJr2MGDU91ErFWUinDcY8ho82vA8kNaUk_YntY81boR2gPxkOTYRr9MXQayL2wgeak0cuaNWUCqtSlCIJNQ10oYJRsd2bcpWs8-ZEin5hDpiCcPqw6GNmtaWyva434UH3KAgkLET0dMuysI-v0Hh_u08i2kf9sG25JGZpum4rIwklJSvhAu--VjhfVxXqXLFuY4Ff8OGjUUiYaAKfd8Vpb9wLwVGsyOAh2HUWpFoEXZiRDuWfqC-tJni0taWoAHm7owzz-3m6trebuHGwcVFrk81NjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaQ_cqH-d3udKlHn_6zJJS3LIaF7buanKU-DgIHi1RCwnTGelEmPeqmeLZsx-3UGHV5OEppJhodMK-QNpFY0qJUbAkNm-MZ-uxC2ZUMcUbEd9ZzSDhwaWCRt-xE5NjZQ97u_JYL5J68GS01wrNYlmyxFtIRL1wF_2hFTp8jbncyTuLZFa8bCF7PR8iExEinUjuDeBSJ5Rv5Os1f1NrscD7o09KHZoN1WKKw7JN1SagShJED2uB8duf9n1z_tyDlCHFw7ReHoVSBOZuW38SlVsB8EDzAgGS38s6GQNEBw6RgFTvwSqxXUyz0hdDFkdnMBicVwfQvgjE97Jf8rxtgQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgEfCUE_SOrfnKtGmEazuYHcfULydKYG7C_aGqDYzl8BVSwCqPNXw3tPy4cTraqOMhqkQAM2qiLYvcvzSfDrJHMtBcNN1yfg8uJ2NFGGK2LtX8TAy7Is_L9K6WJcRObfFEJkaHlGcTSfPkGipbO0Z5k_Q0BbdLSLfTDAJ6arrAmxXj3gEi5qA6cImy1_u1j8tgtY7jkSb8nPNGTyU0-E2wpI_nsX7ezlaaPCkjk2dCtXWZuGJAL06yoej3ZVfySJeyMX5N1TOo-RJJOwuVuM4H3Vws3rqgB2VFIYd2KQJ5EUMBRhCP1aU7gyLLhkyZjyT-iP9NwgGWhc-9drR8uGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
