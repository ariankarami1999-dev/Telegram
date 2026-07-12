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
<img src="https://cdn5.telesco.pe/file/ATROMVnxPMC5NtpmvHo4fvTSBY27R_jgdJyJxdRwHbjyGUIcdzJTyQS2d8yfyU5wdgM-ur0Ny5X4w9Oa_xzB79xZTE1umRa3Mezmo5wJo-9q-cLWkXr9pG8RtAAWtUVrnSDwye1D7tTFz0qS2LxQ6Q49d2AqYCNS0Lgn6vDGhje3vY6AsbnWTrMTvquWbMwCn5_XDQgleoZy1P04-3YTsFZZnJQkybScxHjrRLTju098meOPOQo7clwLBU5j9p-g5u7MLpr22ltQfydPUUcwvzjVWdgNMfOJOK9KCJE2DL2vii1G_dvBZ_WZHnV7Nf1jny7uP3lDrkokqL5QPMG0RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 587K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 00:41:58</div>
<hr>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwI6DbPu07jb9oq7-Mk-m6oBC1UNROu7NiF-s_CIvhbGVPpI_qFnwxI81kjwarrRlfTvtOGmVRN8DJVmSzhylgtEG9sr0QgBgaMo40F97KK5kgEYvVF7T-WhLIWvxM14GyZVU7bHuMcbw4Zjt0R3oPQ3s5bJVcdzPUzXEmvTRQuedGtakv2ornkk9QRtA6-EmjexH0XP_L3jlQrMg8wJJ8GgFN_OSzq7OjtlAvIeQa6iygDPpnge9yg6hRLi3uMB7JKk6KkajV9CdsIb2x27gjh0Yv2cYajG9BgiX8pX6sNWX_ImgQE2tW8-cx8u1AIJy0CYGGkzRrIbRISoXUl3bWRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwI6DbPu07jb9oq7-Mk-m6oBC1UNROu7NiF-s_CIvhbGVPpI_qFnwxI81kjwarrRlfTvtOGmVRN8DJVmSzhylgtEG9sr0QgBgaMo40F97KK5kgEYvVF7T-WhLIWvxM14GyZVU7bHuMcbw4Zjt0R3oPQ3s5bJVcdzPUzXEmvTRQuedGtakv2ornkk9QRtA6-EmjexH0XP_L3jlQrMg8wJJ8GgFN_OSzq7OjtlAvIeQa6iygDPpnge9yg6hRLi3uMB7JKk6KkajV9CdsIb2x27gjh0Yv2cYajG9BgiX8pX6sNWX_ImgQE2tW8-cx8u1AIJy0CYGGkzRrIbRISoXUl3bWRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
بیرانوند: آخرین بازی دوستانه ما پیش از دیدار با نیوزیلند، با کارمندان کمپ تیخوانا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=Q_HnyMIsceIyRt8ReVy45RVugEidj_wZv8FAUTqK6WNQ5g7DSuRm4dtQPIQMX2-F0UvYXLyj0zHYBu6N1YeiYfZ0ze16FsONw8pZAV0s3T63n9oT7OZblItHg8GBZge7hC0Je02sdZtmPKtMqWPSVbDz6dMPYI9YT-YozjvbJKRZFBj6YWnu-fM3FwaJRjIzSYMz4ZtAToCasNn3amzRNHeprbXGBkyT3k6Rst9MI60QAaZfpQQNnvgLFpAZl5c1BcqVISjhv0FhddDLCjG9RNy7uRmhB5aWEu3A4eH2JazoA6zJFBk9KA1GC9yGZ8YQhf-ADChlIw8ZHYDi0Fhi1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=Q_HnyMIsceIyRt8ReVy45RVugEidj_wZv8FAUTqK6WNQ5g7DSuRm4dtQPIQMX2-F0UvYXLyj0zHYBu6N1YeiYfZ0ze16FsONw8pZAV0s3T63n9oT7OZblItHg8GBZge7hC0Je02sdZtmPKtMqWPSVbDz6dMPYI9YT-YozjvbJKRZFBj6YWnu-fM3FwaJRjIzSYMz4ZtAToCasNn3amzRNHeprbXGBkyT3k6Rst9MI60QAaZfpQQNnvgLFpAZl5c1BcqVISjhv0FhddDLCjG9RNy7uRmhB5aWEu3A4eH2JazoA6zJFBk9KA1GC9yGZ8YQhf-ADChlIw8ZHYDi0Fhi1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه سه خطاب به بیرانوند و اعضای تیم‌منتخب فوتبال‌ایران:
از ته قلبم بهتون خسته نباشید میگم
در ادامه رو به دوربین:
به زحمت این بچه ها باید احترام بگذاریم
😐
😐
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=QuAKVx7rDWeAI2o_cz_q2ZURtb_VQ2LwmC5zfJ31ZYxDgkGciv_D7VwDF2zYs0miWxneOuVy1vBCVEwNqNr6cU0v_v9S2iLcj2F5VPorNZ1BO53m1fMfpR9s6hkMh_5j2efxGzbMIgoMwUg9fYHhiLQwGTrA7B1wzticacTt6y5MRwzs6iVbSKEd4RZjbNRtsyD5S97hFUpuLUDca9tLfr8QNTIy6XhH6DRvW9JAY8WHwrRUONLqTigpL6dbzhmUptje0wa5USewcVOL3senH1_oeTFoMkIKLBpg3JN9cG_If6P0pVWAc6yDU23CW8gnbYSRvla2rfX7-w6qNVbovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=QuAKVx7rDWeAI2o_cz_q2ZURtb_VQ2LwmC5zfJ31ZYxDgkGciv_D7VwDF2zYs0miWxneOuVy1vBCVEwNqNr6cU0v_v9S2iLcj2F5VPorNZ1BO53m1fMfpR9s6hkMh_5j2efxGzbMIgoMwUg9fYHhiLQwGTrA7B1wzticacTt6y5MRwzs6iVbSKEd4RZjbNRtsyD5S97hFUpuLUDca9tLfr8QNTIy6XhH6DRvW9JAY8WHwrRUONLqTigpL6dbzhmUptje0wa5USewcVOL3senH1_oeTFoMkIKLBpg3JN9cG_If6P0pVWAc6yDU23CW8gnbYSRvla2rfX7-w6qNVbovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDdcxVkKDx7tnOzFVeY3Lal6wTbgAr-NBGzjmaMPfD7IjSs9Wk0xwdPMkl4aUs2bJzgICtBAUBUCvRAQCyzcXzR3c8epjtMwTqk-xnk5zzZeUHc_mPhXqdM2qcCsUQETgLCV-_U49X4w0dpeCbDAT4UsUNQR99nbprV6Iyjo71UkXGuA67wjw99IegtULk11Nlx0NJRbxfyINp9AZvrk2zJsorpzApOtSXbN9jXal9Nrf4qtOInq8sXKqs8NkdenRcOQr3i5DBTUcJlRu9YV5_MPzUE0dIKN_ALsBA_LYz4cuzNze-8tF3qm1J_YesBHZGPt0AqNc61qLKzvGvC0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElQ5A83nJs-w9_-LtjYNOLsdPSLkASqjsTDbFujmirAmGN74LIdE7ePSRFK3mL_-YOWaWMBHB8TmwZEu6dcmCBiaW8RADsHleGB93ZFxu_I1H1yoaqtOdQSIN6DhUFIsDRNt7f5AWBzOsvb44hZFGdZ_-kVXulimDDGasN9mBwD9IGXAnEa2U4bWMpL77-1__2BIN-CNfNMUBhYR8lq2EeDWpBqlf_d96djMCXhYWVJmp4fH0YKlnvkMJza0Gh4_nptRTV20CQjajB7jKF74fLiUZvHddYzqUfqDJAKK-byRMgNCXj-ruSvmLXYThQHNgwixrGqTpWR-DOpFhMYw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: ما بدون باخت به ایران برگشتیم و این برای مردم ما یک افتخار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99872" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99871">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99871" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99871" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99870">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usZYnv9uNBk8SrgLo859nE2t8Qtl-ZwLLzhIZ3vnlpt_OFrcaQm4njDNSS6NL-DAPnMpdzMlZlfDON5WpMmrYUrwLB7XoU-eoxemadxCTBO0auUVgVGb1O8-xwaHIbCecqMtuqwCOcejnmlWyvvMpawb54DuUpW_hPgNll19djQpSCg_2-wHTbAMaSohu51mf2k1M0wOTKuLVBG13BAuXt6aazn1uOUOSgkqv2lprc9wcXLEAYWuDx6MDZvo8foBCzLUVueDyCFj3JXhrzZBUB-dgvNBqWNXIPvURU3ZfcuFsRNgTzRaS6OQY5jmI3i82slFFM29sF_hKa5L2_69pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99870" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4_0MGUZB0HOddHEC7tH2cQ3d0VDdpImdo_Hh1-5R7fSyO_AKkQKpGGA8vnM_3MzdagFznkdUUi-30G9H19oJmLhZ1onYaIeiodIxpwvJNThXehsjE2ibKH8cl3hRVDVHmsZc6Pvf9Pk5VB7V6Nd7aKa0yBcb4haUjToFXOdQOPK9n2JLgZ95Nbnzo0Ri3lqO9VFBw3xOLzBjNQFvJQWKLAUK1NP7nIOdGEPy7DHUphQgWP7lG-cEg28m5Jl8eKvJtGOVpmAnHmvob-H6Z4g7SHo9TTc45FvdCCgg4ANg4l8z22UPaDs65iy13PpF3zsMd-z4DEHUoulzPLrnF7p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فوووووری
؛ باشگاه لاشخور اینتر درحال مذاکره با جان‌استونز برای جذب رایگان این مدافع مستحکم تیم‌ملی انگلیس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99868" target="_blank">📅 00:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
⭕️
🤩
باشگاه نساجی مازندران موفق به هایجک کسری‌طاهری از پرسپولیس شد تا حضور این ستاره جوان در جمع شاگردان مهدی تارتار منتفی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99867" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gw-ajKB_VjParP1T2kthzOWp1UO1g7_Ao_GgUNdWNOmKTywKQmWSsuecD3afuDcFC1NTt4o646nCSUMg5J_vSpxxGB-yhyDenFhIXu5Z4iMs8i5uYoB8LK4dlvwTTgVYMdpqlgQmLp1nNHGoQgcoCgKZSL3zgnwEJBTywKTrCmiZFayzqdasuYHwhGDzc_62Dhl2jPCRQPwJVjXijAiiyjwJc933thKjoqv2EqTpVQPS1riySeujotfkxTTjg2734QqFuNdNEoJbMZl2S9e_uCVCRPG5uJHC9za4q31UWG-Z4minbOctK2CtNR_gIFJUlCTrdpbjayhwUMin_-ZrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
از فلوریان پلتنبرگ: یوهان مانزامبی ستاره ۲۰ ساله فرایبورگ پس از درخشش در جام‌جهانی با تیم‌ملی سوئیس به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99866" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmhx-M1m0MeOkD-872bC55lG6SHdk0VHToG7NY1-f8hPZOV2hj5WtA5Kx22U72sgHPtz-XMzeDBe7y5rFnlldMsr6AXQEZbCG34JbSWJq4qrsmNJkvR-eb_w-tkmg1xs_QH-STm8eQxCjh8q-cZu0HBxAhOi1UbHrDNhwFLpHnhMGdRl7L37Z74lVASjES4nt9qTDkOwU8rQlYRlgG3uNIMeiqBbg4SMxbr5mRNfYe4qZaCXTP_7bwvxH_BbkabVzuVgzLE-hNqt9sTvEFPOjkxGihvZ7mgO6atNwXeHbud_14_p3ALpCE76TPQ9DN68ONDdFtxxn6DDJbpVmeBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری
از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99865" target="_blank">📅 23:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUOuE7476kx5iUywdVAS8yz1rlfqJNpxg_ihw1cegi1DOuMzomljxaCXuLuGz2RuNg-cPomgacYtXdxmh8qHoYZ0scwh_3jeMulS5KAw15JUjhN-o4mTJtitxPxJ5jhmClNyvD0aQ2Pyfx965l-fJn9C44nrQzYIvxaL5xNM3P6N0jNgu38AeAHBCBG1QyPSBBlJHLv637q5PyCZrHkJn1my97DDvZyrztYZA5TOSfvpJfPyz8TIolMmP-QmyNcZR95OUPWBMr7mzxQ1xyI7gMZlolgsz8TSzkl7IiyziEFbsosJy49pbKh1hjPjb4g4pMSPQ4kvPNRFcuo2uSW0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZGV7sLR0FQ_SPQmGCtaUJZ0xR5dT38I-dKRm8_Ch6PZjiG1j2JTSGlBDGWLNj78ZnY6z1VvP1v6Bt9kg2QXqcxF1_MZKNz2D5f3x7u1tQQ4OTYWO_JXiyH0RIi4quacsZeAvEqpq2S8In0UupZIcylToRm5RdvGckO5hMd8OxTOdZR-Y6TuaPvsjG6_p79VGV-6F0sCDLOXx9yCQrCkJUV3iC8i0QCxUdQVUAEKBCraeeABJS4azO2gj6B-C7JWCgyYefUl3-lMTvVi-_Wy3pUdc8eTXlpAPJ9xEXb9yV-8cxnOe0y2KfXdOOguVkwwxYU2vWwTQHl2KbYgIHw3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFNbMsVbgRJMKG_Yei0rq_dc3IdeKYkR4EbPd5opsSKyQkriH5dSxkVQJIiasE1VFdgHFrbCNbA9OTgsdGnQ8mFmUjFDSxfvcNHyuOTh8ZvtQ1BBfd-1DwVBRSk-ascj5-g50Iiy1Nl5UwGA3v7a5-mmokV_Pn0ItPKUcD4MbjjeOjoSpZV2CSBuCCv0-jFoF3j06dv6EfjEMSc_-cW8xXApsmECEpHajxiOxsTPiijz1g4nzXzhvS7Vplq5Ki9e-O6g2X9d3cs74fdJrrLn2rINvLABxJ8mSBtx30CRtSZvWcF9OQB53YWWNTxZado0UVzPOJCTXOHTli_PO5vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCW3SwoacmvGhdWUf8ujg3zvCq1ZuB4ATgzHm6XW71ILKNEkJj92oYeloPzWZ8zSo_hJ3yIRfteYQcfdZmd_eYvdhKnRWvQLsXh23GTTeBGXccmntz0S00xvaacq-LubiRSwWJ7MxU0LOQxKEElgdl02rbs9N51_bZfYSVxfQwmT2-dezcMeMkMhCqBFzhT_n2VVewB48-swSqyt-P78jiGOdD6cqDeFKx30T3r-iA_S6Wdtgl8Eg5ne4g5T69HVOxxzi38eBCC4twSdlXE41rme53S7ulUoyboIFIJ2a2Os7yga5Jbbq3a8Agi4nwEOzHGjCZjb8aQud8NGAG178g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INaOaXen6rzDBx4u5sycL3sTbu0JGyQvoEBZRt9PjrA44RqNcadAAdA4NJxvoR2lxrEPgla8DsRS_e0yOtOgamlONvOzC7LuMPcdBgQprOC7gRmN4D1v-kk3fL8VArzbsVmnz8Zt5iP3dyKW_6YG8IdarqNDHcxB_6LvifVTBd2GniUCigYJTyaY_wqRFXm8L-2Deo4U9vJtdQEZbaAPmH_tKJDuKDzZHB5eW3ApMqznBlnfChndtpaeWKGkqpJ40AF6a9WydSbhdF27IjsxwKS6zT7pQ_fx_akVLIxsikx5RyzYWImYLgQTfEreNIoPt4MnYzRatiyukbjyklve9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRAbLmT4ICBZT4Fj8dve-AyDkEJJ_jrtwqDiX0szsXnXArMhmramo6ImUUj_pHolSWUDmUW06VQuAAq6FEns_stejx3IF8I4XKYGsW3CtgSQbXlrg4V5n-SS7Ftt0fIOeuZEfQja4zb1-mK7nxLB0DnJXK924BHhbGtML45T81gNhCrCyRbFrD3NQVoadOthvFMxytWP8PAQ-_u3wWRfK_usx-ytg-IVgZZQphCFlveOBQNpYeBN0tSuP26Oo2e_Gms5BOlz2TZmV0hjhcVpNmK3dkIsxm02rBuQX_-aJr-EVwj968AOuLNLcN_qhViBJMSHr9nkNMrInY6ncqpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1daixLyqf8gB16zaj5R8bcpDDiN1_i6SQgQAmD1alzN44DkxUoe9JIWxgA7HL3w5hGQPvqjsUjO6-C7vwWs9V5Z0TNe_l7ZS9JIlenef2fl5s9VJKnQmK8Ygh_8lF5DDyrvMKwZGizxj3jAmKogzI0d5IO8pjXBvGCwsBfIy_VxajCJ6WqljYu6it1ZqH-YalOP24Lp-by6qcGLMxdRr3GPUbODywTd6yJak5NOuCb5nq-4OEIcdLyctVCEVbOAIxg3Bbd8RS3oesIUqJI0gfUvZYujlVUzJbbOTaXKF6CVObwdGVyjPHx9A2173jCZr6zUeRGoBkgvu8SB9oOclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MouxN2bbdCHnAeTpTHZQPKSKNERHWyoWb7jjv8Df4Z4Gd1q2XcROIi_8FRMzza_ADXnwdoDDSs2h29SV89_p4q69EW3I-IsqWinCFRvuXrO3cbhezv0jw1Yin86MdgExX1aSSwqTKFYboEwX3JmEggzUFQgMePuiWqQFxSzgtd9-70wgIMVcbPHC7aP5gi1ScMeO5obRNlBaX_mOhRRrD-057kI_xwX1zIoWbskKr1NmFknVlhxzxC7ciQm8qngjdeDQowYiA3LHxqs9N38wFUgvNHg3a0PMSYYofNSgvhY1FkpWSrBPxj1mQTFHOFBSoyRgXVai3uH1BaT4uZR-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
#فوووووری
رومانو: فران‌تورس علاقه‌ای به تمدید قرارداد با بارسلونا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99855" target="_blank">📅 21:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99854">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwIUcETHtMaoc7paj7reqbRmzboUMdJDenBrKrpj9ihmQgGTRS44nRoIdf_3UOdFt3eQNVraJS3HXKsUXs4YBNr5yNCJir6z4eGvsGeY6BWJUvd43IL_-NCp8k5Ecj0qrGNm7S8ZimjD5Hdv91BoqKXWF-tFMmvv1mmVNtW-njyD-up8F9iXeTZmptjrsaew2CWknXRLM7JDCU5JoxLO2K3LG66T02VRp8QVN3xXPLMf3MlLp45fmXQuIKEIJLyE_MJ1HtVuTlaRDNHYhjEcPj0YJAxlqbFY72zpr6yPQKSjTMabIGe34bJjYuJU3CzRtODDw7wjf0SpzHdc9tPmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#
فوری
؛ رومانو: میسون گرینوود در آستانه عقد قرارداد با فنرباغچه ترکیه قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99854" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMmrLamz2PKKDv8mE2pa7A5jpPGPh3tm90Bs6-k97q4lTEtdfBkvvlB4pFlNKe5nyncvf2Df4ewf9x1BGSFXYvavtoPHYEiP7cxV54ysR54h3_P-Ve1YZnUnwTUvqo8VAzDLGD-Gg7UpbgPWvRVdKR-YHTcXBeSjyFXh9pEyaffLJ142iK1YzFX_5-bT4jsw8fCB3VGK2Eh2_-T4nPeBONKIuklblStLpUTzhEUJERD6QY5Vp1tg9BQY4mrofrqQPeGwhsOAlYa-jDX9efB3tKKI_S70amZE0LPTksyDsrsXJW-eBUgQkMjps2t4cewT3X24Ar3pgTfhRj6ndv56JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWVoXIpD-fGti9Z96FWqtCeMaSEQiQP_4SKqgY_aOnQiYqfjgXKS9vWvA2oNKa19KOe7WxRYuUG1xkl2go_0NlD1cwIPk3OigstvMfgjGQpjdGOhv5o9Jc0XAAJ6ifSZPXbLPOJnwBCg1VCBdIJw-oq8N5XzVLevA_Iy08iFdyhqYO2JuYUS1-0nCjuoS-iNyOBaHsgtwEcNCnPI0MQe-5vrjydc3dIKrlu9b7d6ZyL3P_81MI8CjbZucyTt9R4SDnCqQLc8oTOIHL6e2nG6_OlOEBiErrgh_H4BrXDTB3L6XFmCUmmXoA8ClbQPwdcVZ0qKKf9Jn4zzmPGKGHipMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSXcpr0bSEMt2DeWHMQJpHB7PbpuuKUnw4OeCGeOHg7do7qLCxu5bLuxX9u4joipo6pHgA4JDTQ0sD_jFDP6dykU_3kalky97zKRLZp_fKlMKGcnACeZ5lVyTMyKxDb7DzXprEQ3TrIHvTSEjArrrmTGWSEPIacYhHv1lPQDAXXktyslz0B0o9SF7Gdh7ijDTsD1NAe1LP8YMdkz9KOYC7f5PQ88_Md0C25KQSSYULvb6Ur27HM7-QvF-NyLi1nFRnfMEaXM4lxjMfZHCZLjOgoXYxTGOWsHJPqFq9nspeBvioKxFkCV6K57F2tE74IYdyQn1DrerCfVkSek70p-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین تعداد پیروزی کسب شده توسط بازیکنان در تاریخ جام جهانی:
1- اسطوره مسی، 22 پیروزی
🇦🇷
🤯
2- کلوزه، 17 پیروزی
🇩🇪
2- امباپه، 17 پیروزی
🇫🇷
3- کافو، 16 پیروزی
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99850" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qmMMW-BIAzvYKoEbJIM6RLJ6fZhgVPuDspHJHAjStKyoP5-s6VccQpOX-9LF_YOCjIUuD9L6lsociVY0H9sGOnJHPM8624BK3sQEm0KzdAt0Ov4Uw2ZQpkzVsyok8_qxTh6aabG0qQa4_WKUUXb5FQAbSP0bHuT5JUeaAps6rAm6NvyrA2NmyVxVkJrR6IBdrfdUK_5HvCApkk1SwPvOeiCQGYqG8OryWdf6m2sWupRnK6ZXqMgejwxlE3NUOLHpcsqQbVgA5W_397iSjlSZH_97_1gxKJAclpdIMIL42ntUZTspM2gP-5EAhBmd1HXry3f_4wd9Ns5AQ6qkm7Alhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi7tO_g9jJD9HoA8FX0Wlfi74BgtZV3Az_sEU2GmJJVDHuwrKLOmfG7W0oDfIi1HrDxS7CqJUag0Eff5Ptk3gvN1eUgeYRzkfm0iWlgA7hI8YrI_DisSScJg20i-wUaetdAyYDy6sL_yCF_nXTlwBHsUyrbjtcYm3OGUl1jSx3elj8SyvCREb_o5upatXlbrFkT-RtptJ6hsjSrp_5hsypPQtjOYtFiPp_dXK9gC_GXqQK8EqRZVbIr-r_fBEWkxyrqMin3aosYGAEVP3KRN6MIDd77rHX045w2IoQlbYw6ffYgCPne2ttMciDLHQXRrHEQe-ngNqDMN84zZkWy-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMG87x2zPW-od7fdtCCX6p7DDocWCL-ciPj0wv6F-4adI5E1Af8-W14MJN1FlPh849khu1svCCLu_updmHLwhSxgOrUurtBEN1gY5L9_xNt6WnIQu9Onwdx8LshlN1JXtLWAJOlvItFoSaDnzS-M1Rkdpi7ypi-ddJgu-F-4JTGXHQU60qqyvw15yY9Ox9OH_7c-sIWXDn9ok8gIqDcTIBqxoY5LBH0Pc3QpKlOJuwNm6AUTE0gkEUzYHvywZuhcnJATOI_ixkqmijvyFbd3yD0QwP4UXb5HpNYvBwOZtpK921CEFCGRlv86bhsEFrhvD-1MdgHABBSmWhOWoZICTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
یک تیر و سه نشان، فرصتی متفاوت برای سپرده گذاران؛
از اعتبار یک میلیارد ریالی تا قرعه کشی هزاران جایزه در جشنواره حساب های قرض الحسنه بانک کشاورزی
🔻
جشنواره بزرگ قرعه کشی حساب های قرض الحسنه پس انداز بانک کشاورزی با هزاران جایزه ارزنده و امکان دریافت اعتبار خرید کالا تا سقف یک میلیارد ریال، تا پایان تیرماه ادامه دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdXX5KNZBxHDQeaAUHCthstJbwtFC3CNB-ODvHm_T3tZzNMWr6Xlu5OngQYnvl_rrz8YdZnMn8Ni-00ma9xOcg3dweJuzDK317zHQG5wAgFVeUwBXUcfVGS0C93Xae32QniCr5OxApgBTGuHaNbmI6CqJ4AfmW3mpZZo9SPM_3Fib6MbkHM8HHKbhtQtjYVtZh4FZl45_rE3dNLAzz7q6-_IJuP6Dpbby05mDIKG1-yeRME8ZA7FeUOh9eg0BLABllm_OOHsX3UK0Aj9ibbco2CuhmY_651t3_reA6BvK14PuFPWKLx3yKDL1iJjYUnrB9F0eaOfaHhdDb66lD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXP0esg629P5skPBRwATsFyZZc31NcQ79bP6opgWO4AdJ9SipAt9DrgI-JtMTsEMP8v2GeL3M_TYEnepnag3zm0QivX98FJq2vWF06Pl0UlZH4Ig54aIbSIemHBL2HDMPTMnzFjzCkgs_YgjU44cTClpt90vqOCLD40HUK77LUc7DULn8Js3DXZW-AjZ3kLGYSw1tce2g4uwG4jS0bTNKhLEEg9hCR558RLnoi_UzsHaJuPa-otrWVvMDEZ2V0lZfYhve_ayt4Xeyqd1siLLOMoTYBMuq4g6zJIvUVVWeCEm2znzghzEO_Q5ftLG5X8y_FhvOnH3bph_rOG3fW2RXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaC_VxJUZj8NPvXgSA1-Q_6TKQ0GXP70Lq409_3Y4eOKpNzQJ7teZxDoN1qsL7IInNjBixyNY9CX3cZR6pUR4ciVYDDNFgPQElCnFV1IaksCaZkmWelnvk88uYaO_8KfYh2_eD1QYrlFTMTVl2eVC87SDRG7i65TOqgU_2B4JsmdXJWiQ3KXqOS_BKt5a17Nq6Wf6EhuGxd34XVsjgRttb_zmlTPZZ1ogLQvWTHSt8mt8cUlSne30E7vPKSnM0ok-NpsYtnuubHUdI3qUUHwbFE0pwHwBZi9l3OUApRpc5D34HK0Epx8pOJzam1UoU4jg8J-9TqyCddjUVO9671G1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-1EeXNMIqYJhfYmSh9yRSRXbadFfvxPoAXX1cbAqci9bxjRUBV9alufNWkthmSieEq4OdnDxTmYKJ7WKrhycVpr-IrFWvBKgnyICNOH8uIPexkRcu8B3c5T836gWfFV0qBXq2KU_5haxxZCkuDpehT0TJBkGEbr94AXrz9maddq1GtXQzURhZWnuIaRVFlbRmuxnNwqS3FcUnXVNkLUIQw-foOjq3B6y1z47Ngb1ET2Haj5d5RKCoLrB8f2zb32pFSnqwmYucBtgTJs3CnYHFDqVyYENp6FdgzsLw1fIoALjMSeaVrC1VnEOPVdR6SiCk2Zs_l14mVuLkDI_7m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
بارسلونا و اتلتیکو به زودی مذاکرات جدیدی در رابطه با آلوارز انجام خواهند داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99836" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0FP1JLC7WsJIvSzE4MAac12A_TGN7FhtmGRmlPbk0VCIOO85O5BSPhLYrO0-ZUiM7XrArT32b1aCZJRdsobs6mmE8KidTHnghvyokadWkKbRsPgSGiSnOjfN3hAz1r2XY5o1SnR3jUTjjStRrqr_CjQMD5qIEH1y_lFms5fP8ld4P5h-8lmLtvGzc9uDFPaDRzgggGgiR_acRW7g8QA-WhYgP7B4l3PKtkTLy9PBwGEJa5yQJGv2PWKBFVFu1ThAExHawLUUtBH3mbZBgSQUO9xVDh-78sE_o4BHPghrHnA5hV_kHCF8bWpKLCofS2rgVcbMfy2fIYUWesy9pC8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99835" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRFisJXaNfgwLtFO2S_0pCDcnzZBagdMk1M08ho6aicXQddeSMcjIbGLPReAZ0r5TNvLiU3iuqRosn5Ft8G_rIxWidhujd3xYXEfaP-puxSonCerHoDVf-Qz_aNyh4Ndi7jhjZIOw1PNziWf2i7py8I55ZsHw30VmEzZMqTnUh1sXBuIqVpDqOjNvk2Q7KV7IrbIwYUgekW06DakxDdCpiFRX4KAXaOKZjrW-w5HLxZGyCcVosIPLjNcTepZ8JupfPTaJfWhrGDJ4-L04hkE34-0Bp91yxovcibertjoh90D2QbK-HknSs0ACGa_VV0nuvsfqgZVg_RlRltk4Lv-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فوق العاده رودری:
لمس توپ: 712 بار
مجموع پاس ها: 638
پاس های صحیح: 597
پاس های موفق در یک سوم حمله: 170‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99834" target="_blank">📅 18:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04227938e0.mp4?token=qeoGY5yXuqowutzWoHf_wRYpDC1f9FNSbZdG84KHvYE92GcY4-AK8yGIhGLM3xEQBj59-zAUB0dxM37-MJsMFooDgj-CCsS5cS0hCcvd1pnXr7Q94SsTIm286WdZJ1vREIt2vASEKUg5mi6hgwmvMl-hY6GZrTupePFzsOaqumjBq-kU5irXl3nBJvrqHlVdN65vqr46T0gaFR7syB4AS-QVxMcks2prgeIPII_ofUf511P_tctIwPlm9IXl_jDB0yUxhFvM4S_QsUEV5WRS4SBBK0ESuN82rfEQxRvOw_BcRwQAwjR-skUC4zBlrv0Pcy9iuGG_aG7fPAq3EX17ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04227938e0.mp4?token=qeoGY5yXuqowutzWoHf_wRYpDC1f9FNSbZdG84KHvYE92GcY4-AK8yGIhGLM3xEQBj59-zAUB0dxM37-MJsMFooDgj-CCsS5cS0hCcvd1pnXr7Q94SsTIm286WdZJ1vREIt2vASEKUg5mi6hgwmvMl-hY6GZrTupePFzsOaqumjBq-kU5irXl3nBJvrqHlVdN65vqr46T0gaFR7syB4AS-QVxMcks2prgeIPII_ofUf511P_tctIwPlm9IXl_jDB0yUxhFvM4S_QsUEV5WRS4SBBK0ESuN82rfEQxRvOw_BcRwQAwjR-skUC4zBlrv0Pcy9iuGG_aG7fPAq3EX17ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
ژاپن این‌شکلی داره فوتسال خودش رو گسترش میده؛ واقعا همه‌جوره باید حسرت بخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99833" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=gNqsQKIaQkKkQJFoENbQrF1HMwo5SgN6T8JyIadvh3sPFmn0ZHCfTpNZWbGdHdLektw_vmWuYfwwVLxexxzUCb7N6uD6g3GApIFJ5vcuwy3MwBwBlXsYCQxBcXH3pcKAzuHJ1IUz9i_-_Q_gQBiHdSRYgOzQKj8yOL-Y0MEiuOHi9aUTMahgmSu-LveWR3bWKdYgNsR0lThlJ809SIOu8px4YnK4l69Rgge_u0PQZgjSxWJGNIm4DEmNxmy0ZP3OWgfKswfd3HIEqgGFctBxNHrSQ-sqNRsoYPJv-ftdb9z5WHOEo59IR400M4Kbxmp115OeYAhUCmSzyWKkHp8irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=gNqsQKIaQkKkQJFoENbQrF1HMwo5SgN6T8JyIadvh3sPFmn0ZHCfTpNZWbGdHdLektw_vmWuYfwwVLxexxzUCb7N6uD6g3GApIFJ5vcuwy3MwBwBlXsYCQxBcXH3pcKAzuHJ1IUz9i_-_Q_gQBiHdSRYgOzQKj8yOL-Y0MEiuOHi9aUTMahgmSu-LveWR3bWKdYgNsR0lThlJ809SIOu8px4YnK4l69Rgge_u0PQZgjSxWJGNIm4DEmNxmy0ZP3OWgfKswfd3HIEqgGFctBxNHrSQ-sqNRsoYPJv-ftdb9z5WHOEo59IR400M4Kbxmp115OeYAhUCmSzyWKkHp8irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ماجرای تل سر یامال و عبارت EGO YAMAL
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99832" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIgoZAwsYew4NqP1GKW85-TarUzbO0nAkx_oNoGVSY_RmUgvrmEymQCfC-hlnEFs42K5Wy2W0XNoLvFNjhx-EKahuBmwMOMUkztCcZ2jLOw1NE8Xmmd-JzkLfCyBbR7sl60vfMJ-Aa5VHCwmlVYJyWc4pj_GOlqJ6rCHVSVdFAlKLui4jGsB8_Laa9Ae8gPS3TQzVm4dD9ITWWgKl6SENV3ec6j68isRE0JppBHs33J0AoDA5Wwf1ti60fz8G6unbQ-iiB7GUyCXHGqhFXvNJ4wuYrYmTbkjW0d-7Ys364CXr7z2CbiBse-NzD6snHqpSNcL5V3y0ppLKicFidv64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
اسپورت: الهلال عربستان اعلام کرده که هیچ قصدی برای جذب رافینیا نداره و این بازیکن جزو گزینه‌های تیمش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99831" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=X4Fm36L01H2qtA_LynqXycL5PWjlMzm-c6JR9TZ4o3X0x9D7I-dgykj-BDGPQLiD3cWdhuePZO-mFUKzgReNbL5ZWdypAWmiAlxid4BSjbYOEuqRZ619nix1cvxVNb0biweNtMe5zx2U1zglfSdNi36ReDMCLpTAE7rLnZxWX42dwSs6mDyyxUTLIKCPWEjjWmwFDiXe83X0jbCown_0j0KFktHfsKDFXIj-2oh2NhXmCJHlaRx2JDBGbreg-AgoF9fFCcAj5IgIk71_j1_L1QIcGdwEtC6dEUKhg9063KxNzjwcYudZ7SyKCGlizv6lbbNFJNuIqEIVYhdB5fSPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=X4Fm36L01H2qtA_LynqXycL5PWjlMzm-c6JR9TZ4o3X0x9D7I-dgykj-BDGPQLiD3cWdhuePZO-mFUKzgReNbL5ZWdypAWmiAlxid4BSjbYOEuqRZ619nix1cvxVNb0biweNtMe5zx2U1zglfSdNi36ReDMCLpTAE7rLnZxWX42dwSs6mDyyxUTLIKCPWEjjWmwFDiXe83X0jbCown_0j0KFktHfsKDFXIj-2oh2NhXmCJHlaRx2JDBGbreg-AgoF9fFCcAj5IgIk71_j1_L1QIcGdwEtC6dEUKhg9063KxNzjwcYudZ7SyKCGlizv6lbbNFJNuIqEIVYhdB5fSPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇳🇴
هالند تو این صحنه خودشو خیلی کنترل کرد که کون سورلوث نذاره. احمق اگه پاس میداد شاید گل میزدن شاید صعود میکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99830" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=aB17fgPOjDAi0T5QhdKR9p5O5Be3X66QZT36r9oPIWyVWzXvVsKvde8g0uvpkFbzdGt4eneQtU6OakZezo58fh9nu3rEjTdn2QWX8TzrOzl4E3bCjX9VpMw25KX3jexPT3RA88pUFOvzNBAXf3Ku3qeoFME4JHtv_1Z8-nePQcg36IH6OVmIIsbTFEL2IWfyBvp4COmS69z679mdzKgUZKFt6NZ2N2VzB_KRHhJJ3wxfBcUS_NgIkAGuluiVHPKbNypJUU2rmGks9S1k2erYgqybSb_Xmcvoxks5WMbahMlVQbfuTwcszQBKm5EZLSNWBOuNXmn_Yx1w8Lzu3Ii_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=aB17fgPOjDAi0T5QhdKR9p5O5Be3X66QZT36r9oPIWyVWzXvVsKvde8g0uvpkFbzdGt4eneQtU6OakZezo58fh9nu3rEjTdn2QWX8TzrOzl4E3bCjX9VpMw25KX3jexPT3RA88pUFOvzNBAXf3Ku3qeoFME4JHtv_1Z8-nePQcg36IH6OVmIIsbTFEL2IWfyBvp4COmS69z679mdzKgUZKFt6NZ2N2VzB_KRHhJJ3wxfBcUS_NgIkAGuluiVHPKbNypJUU2rmGks9S1k2erYgqybSb_Xmcvoxks5WMbahMlVQbfuTwcszQBKm5EZLSNWBOuNXmn_Yx1w8Lzu3Ii_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
نیمار بعد حذف از جام‌جهانی دوباره رفت سراغ عشق و حال و کار همیشگی خودش ینی پوکر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99829" target="_blank">📅 17:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99828">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=OZ1dycQl23f2Zomp6keRxs5P0TY1C1eASfT1rpEUrx2e5RXBnhrOYAnbD3dTZPArAo-7kOWKxamnzFIkIL25XXhFDKYYArg1G-02ytdM6aAEqTfZO4cVn2TSszILvss9QiRPaoSKWb0s7gcFmLujSlqViOK-fT4RUCab9HzDFGCqvLj30jurnDJ7JUOfXmVZi5I94XLsQP-qZ8F2MdFvu4YZfNTUk8o1P1lsJ9nu2quzbjOWFR1o82P_GyYSZ8DQtGl8LjtFaBmaqe_R_G7kIMqh46hoOleMN0A5d6qvFtMF1BjFo3a4ro1RnzRGWEWUTj0vCYSZVOi6Q0rocaPxZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=OZ1dycQl23f2Zomp6keRxs5P0TY1C1eASfT1rpEUrx2e5RXBnhrOYAnbD3dTZPArAo-7kOWKxamnzFIkIL25XXhFDKYYArg1G-02ytdM6aAEqTfZO4cVn2TSszILvss9QiRPaoSKWb0s7gcFmLujSlqViOK-fT4RUCab9HzDFGCqvLj30jurnDJ7JUOfXmVZi5I94XLsQP-qZ8F2MdFvu4YZfNTUk8o1P1lsJ9nu2quzbjOWFR1o82P_GyYSZ8DQtGl8LjtFaBmaqe_R_G7kIMqh46hoOleMN0A5d6qvFtMF1BjFo3a4ro1RnzRGWEWUTj0vCYSZVOi6Q0rocaPxZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید آوردن تو ویژه برنامه جام‌جهانی غافل از اینکه دوباره برامون حماسه آفرید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99828" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99827">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=vgXnzr8oJD7oNC1GxqnhUikoDtbmNKyGBXbO7QN31Pe3HtqUB14drBotKbeODodmU0vw8KltbDAUXWiHPVqQJxRFz3cRcjQ8iw7iqSKE72QlH8yjTbohy5rmAXateqc5cOAJMszKPxMc33bHY7GHY4-PApCg8N3v2904vP4oaiUhRe2gQSM79uIEtoVHyYk00CzGGzd4hK6DnRzLuSNvfhnZTLn9OPDAUS986rGkfHBQSDIZLBzDN6M5TRmLq94LjT7KFzaIuS68nAAfdBPE7wKUph8XIrO2VZefDEONAtJ11kBcGD7SdY7qi4Dy9pTBJS0ZgsDlPq2yjRitxVXAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=vgXnzr8oJD7oNC1GxqnhUikoDtbmNKyGBXbO7QN31Pe3HtqUB14drBotKbeODodmU0vw8KltbDAUXWiHPVqQJxRFz3cRcjQ8iw7iqSKE72QlH8yjTbohy5rmAXateqc5cOAJMszKPxMc33bHY7GHY4-PApCg8N3v2904vP4oaiUhRe2gQSM79uIEtoVHyYk00CzGGzd4hK6DnRzLuSNvfhnZTLn9OPDAUS986rGkfHBQSDIZLBzDN6M5TRmLq94LjT7KFzaIuS68nAAfdBPE7wKUph8XIrO2VZefDEONAtJ11kBcGD7SdY7qi4Dy9pTBJS0ZgsDlPq2yjRitxVXAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
صحبت‌های جالب سیروس میمنت بازیگر سینما نسبت به اتفاقات تیم‌قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99827" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99826">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuY89_talK-cVUUrFS0fZomEezTLMwbbWqvZzjkRwfiaRx17BiUccXuxzk8nnjZEDd4JpcWI1GHl6Uord0FyYqAmcyK8MYSsgXUSLJskrWOgKaX3ukbE2OJVh3GDzAEHTtnyBNfDW8cjkPT4KejHhmCCO_4W_EJfpWVpT6bTJ2wYIjjFMSRcIEwGVNU8uyoXQsn5_dz9jtPmxEOncpEFlyYOFAzugsOArHOYvKmIDPALakhzGT-niEeLq6TtvHJX4iCZMRGfV0ymaUlelfxVUL7A-x-StAl_enoALuNUsYIj6tnrhtL07emzDf4SZX7uFkmOeHMjhlXq82yoXsllFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
ترکیب منتخب مرحله یک چهارم نهایی جام جهانی براساس نمرات سایت هواسکورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99826" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
ویدیو فیفا و انتشار تصاویر ثبت‌شده از دوربین علیرضا فغانی در حین‌بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99825" target="_blank">📅 16:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=iNNmK8ikGy5sHP6460G5hsnDCvvxMUrJXIHqQ9KQXufY1ePsul5eRF7yeP1TLRYNLjzRgfRuTtJzYgNF8KoRbiK4EQeYqeSBdAe-yj9WCHlR6IV_QxNT4POVRzn9V0NUlNJ-3IjJRLZP8GyoBzziUNNyefXTYyoV4m_yicUMQ6W6lXeum2uUsjMRLJHJabstRdO0qTrWYRvrGiSaa-k35mEYqOQNykQ_sf2ncUNkPh3Y306XmfvDnExezZ_ThCqbdKXYVewCs4BFPUuB3GjBLUFeXK7xyXDCM4udrFpS6-_TR19qrBHMvPircIxgXRcnntUuwm726Ce2kpxtPmcgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=iNNmK8ikGy5sHP6460G5hsnDCvvxMUrJXIHqQ9KQXufY1ePsul5eRF7yeP1TLRYNLjzRgfRuTtJzYgNF8KoRbiK4EQeYqeSBdAe-yj9WCHlR6IV_QxNT4POVRzn9V0NUlNJ-3IjJRLZP8GyoBzziUNNyefXTYyoV4m_yicUMQ6W6lXeum2uUsjMRLJHJabstRdO0qTrWYRvrGiSaa-k35mEYqOQNykQ_sf2ncUNkPh3Y306XmfvDnExezZ_ThCqbdKXYVewCs4BFPUuB3GjBLUFeXK7xyXDCM4udrFpS6-_TR19qrBHMvPircIxgXRcnntUuwm726Ce2kpxtPmcgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👀
عاشقانه‌های حسین‌ماهینی و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99824" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99823">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=J_vOLx0XEwr-SCHnCUUcLMOcIwNBnRJYIQurRUptp4emkZbHA5o_FSW-bOkB7GPtrp4IfnDRb0q-sk6mVHDCWcSwzbanKHVcjTj_JzujUdXzXCXmtGDzLE_k1-fb3I8cHJ6yeSYqmwn8wkcY2qUsN_qSGXoUYn4MU4JA1Fep-oFXyl-qH9Y2zrK8TJCRwP0xS-mLRqWyMiTsvgfzi3SnCHLls-VvzyH7SyQZIuvFHPlQGT3w9rkmfRvmKENF9lMn2Wmtrr9QFrb07VJ2gIdP6siHQEvcXeAggsyxViPi1tjffkxQXM0kLFtFO7SAMiqwxmcZ6jdxHDyY9QX0ulk14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=J_vOLx0XEwr-SCHnCUUcLMOcIwNBnRJYIQurRUptp4emkZbHA5o_FSW-bOkB7GPtrp4IfnDRb0q-sk6mVHDCWcSwzbanKHVcjTj_JzujUdXzXCXmtGDzLE_k1-fb3I8cHJ6yeSYqmwn8wkcY2qUsN_qSGXoUYn4MU4JA1Fep-oFXyl-qH9Y2zrK8TJCRwP0xS-mLRqWyMiTsvgfzi3SnCHLls-VvzyH7SyQZIuvFHPlQGT3w9rkmfRvmKENF9lMn2Wmtrr9QFrb07VJ2gIdP6siHQEvcXeAggsyxViPi1tjffkxQXM0kLFtFO7SAMiqwxmcZ6jdxHDyY9QX0ulk14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
واکنش دیوید بکهام به گل دیدنی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99823" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=eRbFx-crSbnyHhm--SR2YYsxQp11QPiltJerosEVVjg0_R4Jt_EXpb7gvV3_mRPwhlOrLJh2m3jPujLMRKgocgNgiHR2EXaMENiAcogKdxDvwtVitLyp7FiMddFhVJsOW_FTe7LoANywsXqnKNuVku-tlNTt23fdUYm9vsOkMnDfZGVwds7SU00GmAjXJU3EhrrSSpyS_n8SgXCHlRiDRW6rbfmMMCwtsHXcjMI4oLttkgTGMJlFDFGZXgwIPm6l4AVb0Sjs5544o8iBhTxBAecFWz7Wt7MC40EH-f3GJMHukq_gKmI8LbRH-dXAXfUdIOg7BOSI6N9dRvrEeLi1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=eRbFx-crSbnyHhm--SR2YYsxQp11QPiltJerosEVVjg0_R4Jt_EXpb7gvV3_mRPwhlOrLJh2m3jPujLMRKgocgNgiHR2EXaMENiAcogKdxDvwtVitLyp7FiMddFhVJsOW_FTe7LoANywsXqnKNuVku-tlNTt23fdUYm9vsOkMnDfZGVwds7SU00GmAjXJU3EhrrSSpyS_n8SgXCHlRiDRW6rbfmMMCwtsHXcjMI4oLttkgTGMJlFDFGZXgwIPm6l4AVb0Sjs5544o8iBhTxBAecFWz7Wt7MC40EH-f3GJMHukq_gKmI8LbRH-dXAXfUdIOg7BOSI6N9dRvrEeLi1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1K0BJfPgHl15gr90XlgNMvFFR_wBiwzH2LL_h9H0mEVd6yA188sc2gpkt-cKnoW5toBvsTEEqSaJwVHlA6rmEDT1iO3iXpk-KnS0VApVWnvoDt2C4ErFe5dDTLbBwwMuzReIbskuvTw-ryUO4ywOg9-09rzILbpNuuJQ_p1kTBE6nXLNL7bUzg1iB2qM5HN9AwYFnTiptzyD2zwiawE9uFet1RKvDBL_EJQDO9OziMAud3HEAMMQi58xeSwR9jEcqMHuRnwC9m50kgbNgBw42Qgc8mnVDbL-1ssFi5YJ1oPuM5CDc4Fvro8VYlUFNVcNnvagXRQuXU3sU_CmVDlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3RpseACGvVdXBIAn6iE2icDwerbR8Nlop-42SkblLo0TTeQ-T-apYBRtfkzYqypjErmGvh0CajErWRkRLBfbirU604qpKs6_0IEJf3DpjoR57xfto-lzMvMF53jF8zCJ-XNyQ4bQJob3KxhFrknQwLx6HUxUnQqvWU4vqf11v1O2GvIt4spkKJtodcgUIkQTnv79XPfkuPquXT-C6Nufi9l8xof354E3DkOclWHrQyp76qloo4EcIUyhrG3oDp1CTZP5qiVz4eF8XuA9RmJLkg8ALcka93HudWAPyMrm51kpdbEAIpkNDs4UPzIt31HJmRT9gAYHvZHjcybkbLMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3N9ZyLrw-wMu8kM7i6ceSx418K6CBMO1TJopARV8CeDs_0cnoncUR8FQnEFyHQl-kJXjrEAPApECKYg5BoRcN-eB1QgDVncYCHKUeXmTzcs7E0uoZODrxy00Jh5aZpQ3_1EnBKI6iWRPE7ZsPxq718wXiHRkUrZoquAbiHTxtWySkipaCce4OB5tmcWbGxebjWgZs4FsAVZDfLNpc0gehtofyC8HAxrXHDk5_KkmZyP9Uf7q2VkVjDYf9Qq97V2qPnMEsHFTcfy7Lysy6tMiVbjyv5cAyzBSn6tgyyoB7zcEU3-qFfxkyQnxLl6_fQkd5v0tbCUVAxUUuhAOjrVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMDAKpCO2mPOBuP_vwBDrO6AFQu5gYhyH7jiT44etRu7LQQi_K_cwhpX3WIv8p3SOBylTh6Lp-x8iZzpnvFWbDZ9487JiAEDuE8o2KDmww0gjJxXtZAz7qHQnOzr9SY9a9QW9DMHlqq6OMJ6eUxbn5bdjBfzQ_7I1ljWMevG_9dcuExBSfO51gdD0n_TfWVivLH_NqZw4MyEJXnWmFSFYVd-ehdyuMOtcG49XJJsD1-Cw6XxXBJSJpWE0txEH628p6mnJF1qvxkLf6EENOIxqqyH5Ywi7Mw8SdU8Bl1MvTM1ZoNzSgMg26Z--PBJqUnclQFjIiW_-PtTL42fkw0C1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdp1WCcB-R8Zf96869JTXZ27X6ZOCGSyqvnzJtBlIGWNYffSufbG40dPJhidZdr8b8ylZBs_bljbXtUVKD7XHMvhcRZ0Hu88F5-MpN4IW3V8IDmHRFjmgiRpA1kqm7yrCVEtX7SOV0dsxQHM0rF4M41NKhlLir8zXDP9wox5V3Q2ofPWQKxmAQzRO2VDcvr2nXpvRfrehRadDBneamvWJ7d0pjbDEfVVYa3P9QeofGwJFy0ImGON_1M0JVNsRgGZHVXoI4gtJKi6RJmh4Avecrbt1bxaxiJCq-QCS7n0Cz4pz0wa-aliNmNnZIOsD3hIHsINXVrloFe3Qq91bED93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=FZV-t4axjm-mZlu4Tm7PQfYhYI5WqWBWcDLMUwgXuzbm8ylCg4EHYWKpeISWEDxKHuAG0wYvOme8dUPhDJZ3w_v6yEjKypselUkFlWCCOiHppwTHrNzFawZMEk9GWvo7rM0KxCrDRzlOMf5BQZKo013vL8DwEqH683cw2HkCLqOSii9thmsEu4z6RjqxH2P9ePvzqx2-OaFV_kuw23r9B-AtDUt0JQIdkhbXsIbbtMNjrmKBMjAgn9M4eaPvNbrAEUq2W4cX-UiCSHBc45s6kSWPHvSC0v3LXtCPNuRlv71Ccr_QVUT9oujIdRR6PmJy3mRP38qSnBhO98xJOH4BXXy8lN_9Pa3VKOSnFV1G6KciRmi_Wa9BlauP6O6anC8HiQpmjkSaqfL5t5jHq-eobvHAxJQhfY4F_Dl39gm5LnDsknv1nN5D6qJeOfN64uswSAavi8dr6i9abnhvFrNDGYLvmSooeCXOajWJvIVQLaAbGrMt0QUZKqKf9RVX8N-3g47LdmCOQKwg6l9tZdrnyRUrQ4cN9bOInLdpCdhZTRVlr5Ueq8qSUHjCVeP7Rw_K1nHDa9ajGAy5c2mspcHVa0Ek2IGv4ZbUFFz7IOr0FT1N2ReKlfN-1aB27pHzYlzbUT6ZCQKJesRBfVR143UYgHR7YdbrVC_d15P-X2Y6OJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=FZV-t4axjm-mZlu4Tm7PQfYhYI5WqWBWcDLMUwgXuzbm8ylCg4EHYWKpeISWEDxKHuAG0wYvOme8dUPhDJZ3w_v6yEjKypselUkFlWCCOiHppwTHrNzFawZMEk9GWvo7rM0KxCrDRzlOMf5BQZKo013vL8DwEqH683cw2HkCLqOSii9thmsEu4z6RjqxH2P9ePvzqx2-OaFV_kuw23r9B-AtDUt0JQIdkhbXsIbbtMNjrmKBMjAgn9M4eaPvNbrAEUq2W4cX-UiCSHBc45s6kSWPHvSC0v3LXtCPNuRlv71Ccr_QVUT9oujIdRR6PmJy3mRP38qSnBhO98xJOH4BXXy8lN_9Pa3VKOSnFV1G6KciRmi_Wa9BlauP6O6anC8HiQpmjkSaqfL5t5jHq-eobvHAxJQhfY4F_Dl39gm5LnDsknv1nN5D6qJeOfN64uswSAavi8dr6i9abnhvFrNDGYLvmSooeCXOajWJvIVQLaAbGrMt0QUZKqKf9RVX8N-3g47LdmCOQKwg6l9tZdrnyRUrQ4cN9bOInLdpCdhZTRVlr5Ueq8qSUHjCVeP7Rw_K1nHDa9ajGAy5c2mspcHVa0Ek2IGv4ZbUFFz7IOr0FT1N2ReKlfN-1aB27pHzYlzbUT6ZCQKJesRBfVR143UYgHR7YdbrVC_d15P-X2Y6OJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوش‌شانسی یک‌آرایشگر در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99816" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=Sn4MvKg4PreeXXoZhaJOaCK9FXZ2Khj1YGi_tcZ1YxBedgrkgG0B9HPGlwv8b6SSHzN1OZnhTCZfVK4kOdSW4SAswE1IalVNBa0NonThMWR9m3S3VGcmvQiB8aAB6pFr1vQDO9TsiJBpuSFziqzOq7VIqrKiZNfOFM6tA63nS9hspiPEUiBqY-aKMT5gtGcY1qelR_tHukY2-_BLWr142wYHIWWp_DM8VY4e0IUPm3hObGJeCo562r9Oiwkkgqlft0Q5xc9bWOfZC1M9dxFSE_0YokzLpl97MxVubSvysDorVft5p7J43c2t7n-Ygd8LZm31DEEq_9VCRwF8CiiyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=Sn4MvKg4PreeXXoZhaJOaCK9FXZ2Khj1YGi_tcZ1YxBedgrkgG0B9HPGlwv8b6SSHzN1OZnhTCZfVK4kOdSW4SAswE1IalVNBa0NonThMWR9m3S3VGcmvQiB8aAB6pFr1vQDO9TsiJBpuSFziqzOq7VIqrKiZNfOFM6tA63nS9hspiPEUiBqY-aKMT5gtGcY1qelR_tHukY2-_BLWr142wYHIWWp_DM8VY4e0IUPm3hObGJeCo562r9Oiwkkgqlft0Q5xc9bWOfZC1M9dxFSE_0YokzLpl97MxVubSvysDorVft5p7J43c2t7n-Ygd8LZm31DEEq_9VCRwF8CiiyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف نروژ از جام جهانی به دستِ جود بلینگام.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🦁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99815" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEvHR2CxqI2MFPXTu9rbGcFcIvFGZrTLzXsXHPiMhdP3o0boPHwH1728T-N0XIH3yFw8Qc4SFAQ0oc_MxF7yM7PJ9oYV86yKekuzhC9ZWOdFw96KDuXmzVlmChGAFMqwtgpHbsBAiBda_IfHC0IP-rsDXGU515ZLjftHMq0runVNvIhVvpYSrdNC4QRTRbFUJUgARbnoYjl5ETDAYGgFvRRUDod973uA2trLcu9n6ndCOsQr2EA5kdjfUEVfWQE9eItRpUFEP75IAUC302jMBgnQ-xR7_fGkgjBrx73VVc7ecsdUUDLqaTLB6I_krBs55QsjTLiESJ8DpKeb39LwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از حواشی زیبای بازی انگلیس و نروژ
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99814" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=ElFsMP-glCRXhSpJ3J28vXMjreRUGgY-PzySDmowaAhzcx3qowQwgsA8b74_n7mAjMd9O_i-41V3gEuuFxZH6OaMmfjdzOdxLs6ZbqWeyvzf8S2WCKqGJ9MREG6lON8K6TuvKhszxOP-58XaIFpxynG8BX7KBdkOAjUITIsIAnOfF6lN878ezV0-LNiRY8JVkKmGp_iT-hd8MPTGofKzZ24kuLhqwNpYSpb-DBINRfHfCjYAOQTsmflodB2L0r-JSfHavsYKDLRFZKIweHzawmzXDT9UJNrxmOCeSZxPFrIaJNQKAgHacmFw4JMqS4HhWr_2fONt0YAG-j3PBEkYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=ElFsMP-glCRXhSpJ3J28vXMjreRUGgY-PzySDmowaAhzcx3qowQwgsA8b74_n7mAjMd9O_i-41V3gEuuFxZH6OaMmfjdzOdxLs6ZbqWeyvzf8S2WCKqGJ9MREG6lON8K6TuvKhszxOP-58XaIFpxynG8BX7KBdkOAjUITIsIAnOfF6lN878ezV0-LNiRY8JVkKmGp_iT-hd8MPTGofKzZ24kuLhqwNpYSpb-DBINRfHfCjYAOQTsmflodB2L0r-JSfHavsYKDLRFZKIweHzawmzXDT9UJNrxmOCeSZxPFrIaJNQKAgHacmFw4JMqS4HhWr_2fONt0YAG-j3PBEkYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
کنایه عادل فردوسی‌پور به عادی جلوه دادن شهید شدن مردم هرمزگان توسط صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99813" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🙂
اگه جام جهانی توی ایران برگزار میشد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99812" target="_blank">📅 14:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99811">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=ZG2hL1ro6PSqsLeBtaYew5ljPIKAscUZ45XcLuYlOjamF4wiaVTVq72w-rWCFG_Nkwgvfrv_4nN-f3a8Q_6ALKOV71LPO1AF6owZn29Cu5GDkn087sLSujEYJHf9u_zdNrhfgoZVmL6dJfx9oswwbGJwwwOsoaEArluNeNVCOad2tl0MCfvSCYAymgOQInb4kYNDedIuZI4LNNC8KiwAcx0nlAUen-E6uWjWZ_zJW6KRMG7_S_8FiPloUZNAdSnMZomtStJlZxtZe8p6NLX-h8ObkkSt-2ecXVPpZQZB_3-xO0NLfSyqxsYwFEEN70WtTKkCwMeoXKBh4GGFIQC1jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=ZG2hL1ro6PSqsLeBtaYew5ljPIKAscUZ45XcLuYlOjamF4wiaVTVq72w-rWCFG_Nkwgvfrv_4nN-f3a8Q_6ALKOV71LPO1AF6owZn29Cu5GDkn087sLSujEYJHf9u_zdNrhfgoZVmL6dJfx9oswwbGJwwwOsoaEArluNeNVCOad2tl0MCfvSCYAymgOQInb4kYNDedIuZI4LNNC8KiwAcx0nlAUen-E6uWjWZ_zJW6KRMG7_S_8FiPloUZNAdSnMZomtStJlZxtZe8p6NLX-h8ObkkSt-2ecXVPpZQZB_3-xO0NLfSyqxsYwFEEN70WtTKkCwMeoXKBh4GGFIQC1jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇫🇷
حمید محمدی: اینکه کادرفنی فرانسه بعد از این نتایج درخشان و رسیدن به نیمه نهایی جام جهانی بگویند بس است و این سکان را به افرادی دیگر بدهیم بسیار آموزنده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99811" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99810">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=BdYwhKmeFXk_2mMzW5YxXj8TUsHds70ZuupvSw7w0ICuqnHl2nTlU_pXo-zcDXmE94qFAvFwXhTNxzsst9XGZmw3RXHMfE2jHToot42SXljpBgei526TiCEfwni7mC8lh8Y_Yc3YwsgSLFzlz48Esf-9JwrznFplrHkCUcGHlo4DqbQxAwE5MqN7ip9jU7XEor4AmtMWiuXOmYbkG1uCgPViWbPUqncRQrssMVvJ3cL-KYE_8ZcpjYXfoNpmbapYCPtsod8R-nrVgV7IaZFtfZBqmrnU8djuY8LjL85gd7tcAqp5NxZKgQtXIuSeYCN-bZJ3m7hqWHLJfyOiSQbyWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=BdYwhKmeFXk_2mMzW5YxXj8TUsHds70ZuupvSw7w0ICuqnHl2nTlU_pXo-zcDXmE94qFAvFwXhTNxzsst9XGZmw3RXHMfE2jHToot42SXljpBgei526TiCEfwni7mC8lh8Y_Yc3YwsgSLFzlz48Esf-9JwrznFplrHkCUcGHlo4DqbQxAwE5MqN7ip9jU7XEor4AmtMWiuXOmYbkG1uCgPViWbPUqncRQrssMVvJ3cL-KYE_8ZcpjYXfoNpmbapYCPtsod8R-nrVgV7IaZFtfZBqmrnU8djuY8LjL85gd7tcAqp5NxZKgQtXIuSeYCN-bZJ3m7hqWHLJfyOiSQbyWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکثیر ارلینگ‌هالند در سطح بین‌المللی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99810" target="_blank">📅 13:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99809">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
راز جلیقه‌های هوشمند بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99809" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6ym-nmg_4wFVCIfW3kI_-SZTQom5WGHqtwuLUaYihk-EFGjcOlX9xkbxYTNx2L6-mri_yWmsb7esuPR0MgyjB380NyXVKfhuLapqelIufrlHoNySJbqgoRMoEoNko6M2a1TVb0O6KoQ96OqiXxiVIQOPaX57W9rW8VBQjioayJIevMbcTziHtbk4wETvS7DyvmypzapFrqIl98iZ7DQqPZbyVdhNnXBJHHefpzWPTAzIvnlC2cHEVUrat6HRJFBX2tJERx6FJtVbDZFahKwUyIBV5i6CKmng1MkX9sUcO_CkFxscaO_9HmOx_PoCvxNOP_-iDFvEfSXOrjBxGGlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
• درصد احتمال صعود تیم‌های راه یافته به فینال جام جهانی (بر اساس مدل‌های پیش‌بینی):
🇫🇷
فرانسه
- 58%
🇪🇸
اسپانیا
- 42%
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
- 51%
🇦🇷
آرژانتین
- 49%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99808" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99807" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99807" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5h1pJtE6YqM4aon-hMehU23uILwmDLWQDqNAUEo76AtCpKUv9E2CAY9eylSMmaBA_8iNLUsEamJlYgPDVN5TEU1lE85U5t7KSf9unPSRb6lhcpbkR2M50RU3TKrqkxTjrXH_2RLQAsULXozkRVCwkva9LMsrrhN8ba1TZIEA8fpX8kI8GSOpzraTxZ4QNC4q741KKk_k_ekYUPmfVtDJ_9CaiRvzHeWZhiL4DK5ElogwT2pVGXCexo8dQfwI8w_IKuvV7T9lTxF0APcGWxOMpt_wfRGCMZiH0G30hthpaZxzgYublbrm_HY4wIGcBm0Qc1ctH-2CZTl25LYoqHcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99806" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22252f139a.mp4?token=oi3ZRl3jx7-lgPawkZtyBLTC81PP0KMuqW-VpLzhwlsDYJ8PWM6bcZj-ORSzBlB58VZ8S9hfKkN6rMChy5FJ4RK3AaqKpJXoIe6kl0tUd_Z9fu3idgHlHjgHNqSsd9SOU7ZmAyj_juEKqeyKeK7nV3pFQeEufSjSoWBF0OivoP2eLL8HHjB1sOrsxNMaZ3nKN6me7lkMW8Oh21-BBTryDgBxrG94UnuYnvBFyRDMxLQZXIu1y3Ij5V0AHN-zKoUf7nWsIAdJCFOcBJ7Krblvr050SfMLhpLnnOp-Fk7mCH2fQAySaeGX5SnSJYe3d2uMv4JparUnNVIgRxyeJyAkMTIxuQ6psXMJYf3BIa4Olc3nZo3LBY-nvwrUZPjsCrHW5Qw6hDQSxQS59x3dkFczngXbrkhG_50mz9J4SI_59HlxJuuC5AZfzsjK8g_BCdoqyYAkKPo5r0Liq0nrU3GlDj_40pBCu1v5rHUuNzUWBJTmJ4Wzs_XJOGgr7aJ-h6ASXpNcdlcZ5-Udeq1-4WY8_XXoZbkWqYYhMQTiZXwvCd9SFLV-GvRuO0SMsvZwEZlSij7tIPr7BHsg7HjmCXs8YifUESDnQvL0qTpx5MKKYzGHj3lPhC2VP-EQ7nXk9gWN5HeIkV1-Rd4qNep6HkayMlv8nF6pEdLfvEmEWXmQtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22252f139a.mp4?token=oi3ZRl3jx7-lgPawkZtyBLTC81PP0KMuqW-VpLzhwlsDYJ8PWM6bcZj-ORSzBlB58VZ8S9hfKkN6rMChy5FJ4RK3AaqKpJXoIe6kl0tUd_Z9fu3idgHlHjgHNqSsd9SOU7ZmAyj_juEKqeyKeK7nV3pFQeEufSjSoWBF0OivoP2eLL8HHjB1sOrsxNMaZ3nKN6me7lkMW8Oh21-BBTryDgBxrG94UnuYnvBFyRDMxLQZXIu1y3Ij5V0AHN-zKoUf7nWsIAdJCFOcBJ7Krblvr050SfMLhpLnnOp-Fk7mCH2fQAySaeGX5SnSJYe3d2uMv4JparUnNVIgRxyeJyAkMTIxuQ6psXMJYf3BIa4Olc3nZo3LBY-nvwrUZPjsCrHW5Qw6hDQSxQS59x3dkFczngXbrkhG_50mz9J4SI_59HlxJuuC5AZfzsjK8g_BCdoqyYAkKPo5r0Liq0nrU3GlDj_40pBCu1v5rHUuNzUWBJTmJ4Wzs_XJOGgr7aJ-h6ASXpNcdlcZ5-Udeq1-4WY8_XXoZbkWqYYhMQTiZXwvCd9SFLV-GvRuO0SMsvZwEZlSij7tIPr7BHsg7HjmCXs8YifUESDnQvL0qTpx5MKKYzGHj3lPhC2VP-EQ7nXk9gWN5HeIkV1-Rd4qNep6HkayMlv8nF6pEdLfvEmEWXmQtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انشالله برادر عزیز آقای عباس‌قانع با اون صدای گوشخراش خودش گزارشگر فینال جام‌جهانی نباشه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99805" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=NiftzdQrcvGnUa07GxAqzG6FFzipq-zMMszUFsV9HlihVztYBp6NCnp1JvkJO_pCsUmqIcwvbWTHrXJ9wsizQNu-8lO7HZaDi8ZxoOr2FGTQFHNAU-mWEe7I5kNL3Y4XyYLFlMwq8NYJJFEYjssbl5uiPnKa0TL2CsulB6yoCSOWfkE4abfnGbmhPyGkllwdn-vP1E5i9OLPAeFvbd5nFUQs0nb9S947Mk9jkBNKmz03eq1q1rFVJl8mhUksNsIv60Y0HEoomZBTUemkXMIi3jPeWiymc82wIkcChXwWzWuh8uIAVTHpF8QTirq4cqtlQRVjGiAZOBIhE6VVkHpCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=NiftzdQrcvGnUa07GxAqzG6FFzipq-zMMszUFsV9HlihVztYBp6NCnp1JvkJO_pCsUmqIcwvbWTHrXJ9wsizQNu-8lO7HZaDi8ZxoOr2FGTQFHNAU-mWEe7I5kNL3Y4XyYLFlMwq8NYJJFEYjssbl5uiPnKa0TL2CsulB6yoCSOWfkE4abfnGbmhPyGkllwdn-vP1E5i9OLPAeFvbd5nFUQs0nb9S947Mk9jkBNKmz03eq1q1rFVJl8mhUksNsIv60Y0HEoomZBTUemkXMIi3jPeWiymc82wIkcChXwWzWuh8uIAVTHpF8QTirq4cqtlQRVjGiAZOBIhE6VVkHpCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
جوری که پیمان حدادی مدیرعامل پرسپولیس دیشب از حقوق ۲۰۰ میلیونی صحبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99804" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsAmQR-eSLdjivIUZx1XGPHrVc7AG8rarAO2KJKvYbwDkGGZ9jXcBfr0pbXKtm9CoGetWZ9WALS7zibmyHvXvA0VkCBkdOS9n7RyfXdgiclPbShaBcg54zLQoNWNVooSlKcICyEeEmLPK_kWDoEfNjXZYXj4lKXtcNgtIoR3exuQpGSabCQvJXlxz6E60lSezgbX4l1_bwb2fJQQvzIwpI0yJbvj5rrCqnAQsStKraY1Wwj8R84fJxWea7xiTLz2n1JLdrN47wSgfTdZT3-F8CSmgPiGFBJTWnJ0u0Vzk7ts9PNC9RK6POHxPLnt3eQHAWR2h8OBJhIJjJ1APli2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQB0JAm1AUBWYXStK-GBblqEroVyzTvZQqshW3Z7o7ea8iXQ9C8z3KqOWiftYBBUt1eVQW6KeQT-1dhF2KQi1Vo7-1Q5TkeU1oOIgOuvHobgi6XPpkInsXH9lypAKOfAZ6vBBc4VWwdUrVEr2nQPGZD10KTeLcmh88zobaZ_idX2UHVk_lzQompfpKKqptnaTY8LxbBsQhslktpyzIzLZUQZQvDfK07SHdQNQh2dzvi_xx1wgKy3xx71rT54ZN8o3UVQ3vJjpRR8DF-7D5jcewF7IE_02u-4v2UEHx0gZapRL3LEdD8Mtm_89D2JBxlgRtr0wMLwx8X-nkkGFeKL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRdH3jO6WQ7CA144IA3P7RTKJNhL7za8W2NzCeHs4RIi-muMkdIDMG5Txoyrb_W9RCuKr0HjCBOkR9mPn3HW_0A5atFOwsABiJ6NpG8bLzVIm8UFpDWanOnIM6aXFaHf97zUE5cgAwiu3945JjqSLu1BtRvba5-yLfWHyG5E25FmSdgNbtFfpL_2kS8ka1cvZJKGyZCV7mv6ORLIDeXRDJkLMjG5dRcjv7_Sih7o1DLzFIna32i8GI0tfV-GguPOgIJ-8Wd824nzN7LIKWvni3RsULN4VscDO1pBIZoaQjKU9l3OIiypZpEsm-2HyJGJK0B_6uE4XuKAS4MiQAc88g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوس‌دختر بلینگهام در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99801" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007eae865e.mp4?token=NVnkMK6GWsbzeiaqQCu7h52Nk892DMV_-f9kvRbRTHjazM6FqU0WSTiW9gfwgXfWPptmDBUDARXhlxV9rv24kDmrK2cjXR9FRIsSSPVRNlYBbMBwcwZqLPNk8N06UL8TlbdhIuRDkymnmTJy_A-f8jRUNg3eIiOcIqKhYjPAmNtlHyeVpfIbIuJ79BmcFrRlZRgTZluBM_6gQ7b_H-zSVS74tQogkWQLYO6ds0VTDY9rJUONyoiOqnu5ojYlbk4UpssFBEVUVHl-PrJD1BVJewcim4-zXx_s8J_2lxIJGAsY5PSH_glEJIMDIVmFrJPRGB0_bV7M6J7gEJBPB3qmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007eae865e.mp4?token=NVnkMK6GWsbzeiaqQCu7h52Nk892DMV_-f9kvRbRTHjazM6FqU0WSTiW9gfwgXfWPptmDBUDARXhlxV9rv24kDmrK2cjXR9FRIsSSPVRNlYBbMBwcwZqLPNk8N06UL8TlbdhIuRDkymnmTJy_A-f8jRUNg3eIiOcIqKhYjPAmNtlHyeVpfIbIuJ79BmcFrRlZRgTZluBM_6gQ7b_H-zSVS74tQogkWQLYO6ds0VTDY9rJUONyoiOqnu5ojYlbk4UpssFBEVUVHl-PrJD1BVJewcim4-zXx_s8J_2lxIJGAsY5PSH_glEJIMDIVmFrJPRGB0_bV7M6J7gEJBPB3qmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
مود طرفداران آرژانتین در روزهای اخیر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99800" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAXPLwjpzYkHVGGgPpwT94OrtUzkP6fShDPbV3lRH0c3f9yC-M_e92UAOlmYx-hsvvHA1gWrN84ZUYhiZdS0Ubk-wFv5qSqbeKIZ0AXOJwzeIsb8JmgMlevRw7ffYBZqBWzEuFhgDXACeboyDowZociWWGvqQMu9Mclkq0Ha_eeAIPOY9OyPS9mlAKJMOCwCGzE8YLd-AasRutVWOtWDdjSGaC-WixX2gsyIB9zs-lRFRmJYDLPbqUh7SIqmPtTdQ7aADPjIQznO6rL395wOAb_SM-fMNNeOIJ0vsP6JwNhjyrgegzGwdLs-npW1C-sbxPmkWkDyfMitf02g_ae5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5dLqCO-DaJ6a4CrLf4n_3LMFEuSVkZ5EbIZ_8jVCiU-y2pMwVNcFVduFExwY2I2cj31VmUf2lqqb-759g3xy3Fi6d78DOlu59FeSsoKYN7uLlJFSynMu3H8dWUbBTqVeogeXAl9W4rexIO38SXgbB0xMPp9rPhSeuIHTPKqyORQC4jeamv2HNpLRliL2KieSLW1O9RXDJtlMrQrdA0aDAysQCkQwcdB265RrX6vQNNTMuW3ZJPWeSGxfZo4IJAbz9jV2EL-Y0Ea-ZnDCnjVdBC2k9uPZyOHdSxPvgLxFwYbpSFYRQJMNjmCDuKORNDK7YVwKqW37X1FIgiKkegZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k63UjpEXrzwm01jo1HJdJvVsW6y3sF2jyUdoo7bt6_oY-3yGizIu7pUwW5_y5CSZYul22_Dvaux8fof26eqIKShaUlTr-f3LWhQdlgj2cqbjMBv_WDtlJu9bgYax1rTFWDSVgk2HyGGSlR07DBTGwdXABncgs_ug5bG8Q3hmHqo_To38ZKBJnHqETO6OVsuUUX_ndH10HexxPkxuZ9M4eGhFwKBa1KWUm-7u962zTwXwpP_W5xxv1lQRw4ZAv47_YRgrYEZv3559LsJyg9KSz7OXPhk2Jo4opZqDFMqDbp_pD5teSTs2iHPJ8YUKnpe_10GXFv1Yqld0aj2IwQVSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAjP55pk5UBvgkVPvo-nglroi6vA66ywolagc8QrfxmZFCxNrAtR3pXO65acHSfBGGwtrO1dRU66bUwz9B_L_chi-HSvUyta7LfMpi_jV4j2pWlqc9yTQBEkTkp0jtYxpHL4uC7xMgTx4Hx7dlD8U7g_rdHM4xHoel_qc0td8FznNzknCt1awVy_CDqfpetX2yh7DF2JMChcBZeHHi-Z20hu2mI-6sqO_fdHCs1LyShPeW0De4EfU1xBO94rUJ-ccAgOdqST5_233BG2LMeUGD6Ps4iEfMXhx7OeSOqpyTJX22eYq0vnKlVGXJraDfpFA_VRfbkOV6Cojb2rQFFQuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇦🇷
خانواده لیونل‌مسی در بازی با سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99796" target="_blank">📅 11:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=QGo6pFq6vGCjGF5qndZXBSn3_OWge0belQCtG_VcfsvtIPwXzQrv907CqPH3e80q3QEZIiNpHzh97j5wQbOI95LgfogE4yMZuo-_QN-4Fb6CW5kDlfvmFQGhIoTu26KQWHCMSHDk9xxLF990VrNf_pV1FHabSvCtjFwAgSihvE39VviVobjGkfmv8Gmp4nno31epFc8llHOj4JJDKQJkwSM2QKSnyR9rzXkTQGP3z26ziEtxV-ybMWrSruGH0fa8OcM9VHf8SjIPUCeNuN-lbW52EyYMXbBJaGgNlrC_H8pVuhFLuA-AXPH-bxJPWAU2TydHsujXonkHd1suGpK9PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=QGo6pFq6vGCjGF5qndZXBSn3_OWge0belQCtG_VcfsvtIPwXzQrv907CqPH3e80q3QEZIiNpHzh97j5wQbOI95LgfogE4yMZuo-_QN-4Fb6CW5kDlfvmFQGhIoTu26KQWHCMSHDk9xxLF990VrNf_pV1FHabSvCtjFwAgSihvE39VviVobjGkfmv8Gmp4nno31epFc8llHOj4JJDKQJkwSM2QKSnyR9rzXkTQGP3z26ziEtxV-ybMWrSruGH0fa8OcM9VHf8SjIPUCeNuN-lbW52EyYMXbBJaGgNlrC_H8pVuhFLuA-AXPH-bxJPWAU2TydHsujXonkHd1suGpK9PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
روایت حمید مطهری سرمربی فولاد از بازی در آوردن علی‌نعمتی تازه به دوران رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99795" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8IfPjNmmSB3lT3zjwZ1fWqLsNIsL8taWBsieGlhz57aLaHBdGsunt6mAOjqNKyzureKsAZbRvxx5AyCSKM5VhqPEX_CXyAXgIC7nOfldjpQE5mBAFtx6_1ohZ4LGsIGN5lyhOr1iKyVR2OgvvBWhSo44L37AW_ElqIvqsAvFA0KAYRQgmw1dUPNticEZJPMbUWTP4LawTdO8kFzMxDNJmjObZDAXKet3Dnygc1W0ceX6TBfRMbSemGgC6x4MLmQfCNyBGiSUfsYo5OlVtqb2p3pe6lOiCp9o7oLc1Mst-yVq8HMePuMg90dMmjnxLYPOzc9ODdkWZXzNFyv7jD16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti7pHQcucXbbLXxEuvUJ8jZ2dEVVD3jVPV3V0q8xoZKbjwhhYXUZE90thRDKbKQv89ZXXBxBoTAYY7eRdQjfVv0gCy0EsaY13-1Q7YVTBuxAk8VWbzmzcE6Ka914X3EAjbsxAjlMeHTi_eRcKwAAEp0_NNynTRHsYMroEDq0As6Vu4QqOcym3GOFldvIaMWOnC2wcR-_qtKmnMDpmNvOR9mU-z881ylnYmlTGfdeQHkoKjNdFRKdr89tp-n0x9i5xj51YeN2AXTNeIHyVGMk5WfbqCX0JLm0xChSkJmKMnorFhwm5LNej3azkezlYz6P6l0qjmrq1dB8-Gm5fu5mKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
فیفا شروع کرده به فروش چمن های جام جهانی 2026 با قیمت 450 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99791" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPxu9cAJF2c2ZVwZlm9CIaQ4Lq-p5PHC4AuOysErv2vfZFdvg7whGMKxlYMO5WH8BTkpGtFRFQn8NSRTTvE3taRXmJQQiaZwJX0kCoXMRilMhh_yA99PO5YQlh0e2NQqmqDG4XR8YdQ8Rzl7ZjFOTBX-L9QOQgteD-7zfMZqiWkGW_f-bg1kaLWRPrc3HF0WvA-4LvWKGovIN-mXLN0D7JheOwd7VG3zW6Tj3ul_XBsQs3MY9d1DbIb_m5ZPr7CaDwJ6dsanzKLXMk1JZXJsbNJw84mbMfoCwkOGCzuPJJcUft7ImSQE71u8A4pWGURjNCoNw9tALsdZiyOMfKs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">� بعضی‌ها فقط پیش‌بینی می‌کنن…
بعضی‌ها از همون پیش‌بینی‌ها درآمد هم کسب می‌کنن!
داخل
@betegram_bot
می‌تونی شرط‌های برنده رو ببینی، از بقیه ایده بگیری، شرط خودت رو بفروشی، امتیاز جمع کنی و جایزه‌هایی مثل VPN، گیفت‌کارت، Steam، PlayStation و کارت‌های مجازی Visa و MasterCard بگیری.
⏳
هر مسابقه‌ای که از دست بدی، شاید فرصت بعدی درآمدت باشه.
👇
@betegram_bot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99790" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=vd1yzriQvynKss7DZI3QCpVIOsRC0i2gftsbiQmADZMnAokyv3UhP0RQVEojN_3DgmSPrnA9_iUl7gMcC1mVWv6iynUm16x9bwV4kgU2RVwCGltiEU99sFQjkt-63zY_eSFSVyizC_a8-5cDjyTWeD_sGLJ2o6MZEElzPK3cSh8uy32jA73V5vymYDqN_X9flEosBoXm5i54O9IVaWwh6t13EOaLriAFhaLqAB1AFOKyebZ0SzO2UID8MdpZ06ZyH7VbKhI_qQE9bnuFO6YgKXwjnxTuWg77r84bVy5Ez5Sk8R7w0GOw4DBTZqhEfRwkvS74v7xU7HELWAlH4KOhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=vd1yzriQvynKss7DZI3QCpVIOsRC0i2gftsbiQmADZMnAokyv3UhP0RQVEojN_3DgmSPrnA9_iUl7gMcC1mVWv6iynUm16x9bwV4kgU2RVwCGltiEU99sFQjkt-63zY_eSFSVyizC_a8-5cDjyTWeD_sGLJ2o6MZEElzPK3cSh8uy32jA73V5vymYDqN_X9flEosBoXm5i54O9IVaWwh6t13EOaLriAFhaLqAB1AFOKyebZ0SzO2UID8MdpZ06ZyH7VbKhI_qQE9bnuFO6YgKXwjnxTuWg77r84bVy5Ez5Sk8R7w0GOw4DBTZqhEfRwkvS74v7xU7HELWAlH4KOhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
لحظه اعلام خبر درگذشت گراهام توسط صداوسیما و تیتر: به درک واصل شدن گراهام رو به ملت ایران شادباش اعلام می‌کنیم
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99789" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=tp8v5XHunJd1wl-6pHKcbPhhWOmL2jmYHev0oWxlQTqdOHuzlHwzNQWFfm7Qrm7D-6tG2hLEbU3AVsnwwcgbRslQgx0OyTcwpL2n3tadeS99kzZgL-KftxmYYpiDGT2MBfnHKHM908PPaayNYwBwrnAPaeHFvUD-xgy2l_ZN5SCxRg3-4T5cJDcCh-zHREtGnrihFA-TD9gLfe9aOj4NX9lA_X5jGQE4cPcMY6uCcQwseFd8yQTIKgX5aKngwnAtSvzFjOJqqMSQ-qwUAU8ukwCXQxJJVg5O4BFk4GvwzsyaS3f-pWJzCGvpJ9l5Kr3io2J8TVBm0ZKMgrxyRv2uww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=tp8v5XHunJd1wl-6pHKcbPhhWOmL2jmYHev0oWxlQTqdOHuzlHwzNQWFfm7Qrm7D-6tG2hLEbU3AVsnwwcgbRslQgx0OyTcwpL2n3tadeS99kzZgL-KftxmYYpiDGT2MBfnHKHM908PPaayNYwBwrnAPaeHFvUD-xgy2l_ZN5SCxRg3-4T5cJDcCh-zHREtGnrihFA-TD9gLfe9aOj4NX9lA_X5jGQE4cPcMY6uCcQwseFd8yQTIKgX5aKngwnAtSvzFjOJqqMSQ-qwUAU8ukwCXQxJJVg5O4BFk4GvwzsyaS3f-pWJzCGvpJ9l5Kr3io2J8TVBm0ZKMgrxyRv2uww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: به پژمان جمشیدی با تاکید خیلی زیاد گفتم به تیم پاس نرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99788" target="_blank">📅 11:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=UOX6YfBVpSTouPkQu2MgNtYNBqAzQGp188NzyaF8_nNk5UUqeU9cgptwbRS3AD9d39gPCbpwNG06wpfIJ3X85yZ8W4hbfCe_QClraS1u8mJqd_2on7WGV83xCswUUKX4xbjKjyi7B3Ex3puhPm90YUWRmzeVuhAm2VOIkt7p8gAaIQapo_8-VBnKoGD02O4NuoFMWjqo9hTWmZNKY-jtYBwM8cs1wpD1CvV32FK-Hz0CG67C4ZfBTVOdzjgOc_42lgExy9yv4x31nRLL7H86hGLj7ipyNBtFX_G6J_zF_aY4Gert_nGmyQC4Z4FDRmAZ60gnphyR6m_eBkJXowxhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=UOX6YfBVpSTouPkQu2MgNtYNBqAzQGp188NzyaF8_nNk5UUqeU9cgptwbRS3AD9d39gPCbpwNG06wpfIJ3X85yZ8W4hbfCe_QClraS1u8mJqd_2on7WGV83xCswUUKX4xbjKjyi7B3Ex3puhPm90YUWRmzeVuhAm2VOIkt7p8gAaIQapo_8-VBnKoGD02O4NuoFMWjqo9hTWmZNKY-jtYBwM8cs1wpD1CvV32FK-Hz0CG67C4ZfBTVOdzjgOc_42lgExy9yv4x31nRLL7H86hGLj7ipyNBtFX_G6J_zF_aY4Gert_nGmyQC4Z4FDRmAZ60gnphyR6m_eBkJXowxhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
میکل‌مرینو فرشته نجات تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99787" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=iOeAGkKb_ZNntv3kyVRVDPdkfcYB7z-SdSwriDEKcu5dV7U6Kx8Pz737T7aBQNJJtacWMsgcZDPsmuwwnOJ4I7HPuKR1NyddlWpEX2MNjVaOnZ2WHfYti1S6wS87-db4gh2go_OhkqSvCVL7Kn7fAnphZBGJrrpujupJarxUatsDRHd5aMMXDzSg8HGvitEP3eEOw6pCfoIxZEOwCs3P6NghJdG9ZbnFCeY8Hnhsx6S9MeQCm1Yq-g3SNw46FJa_52J1i44zEcf8EsgtO1wClo9k0incYzf6yz_7JspEbaZM5LMEwDbuEleq-1Ejp2ngjqo_eI7zQl1SlMNdxz3JeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=iOeAGkKb_ZNntv3kyVRVDPdkfcYB7z-SdSwriDEKcu5dV7U6Kx8Pz737T7aBQNJJtacWMsgcZDPsmuwwnOJ4I7HPuKR1NyddlWpEX2MNjVaOnZ2WHfYti1S6wS87-db4gh2go_OhkqSvCVL7Kn7fAnphZBGJrrpujupJarxUatsDRHd5aMMXDzSg8HGvitEP3eEOw6pCfoIxZEOwCs3P6NghJdG9ZbnFCeY8Hnhsx6S9MeQCm1Yq-g3SNw46FJa_52J1i44zEcf8EsgtO1wClo9k0incYzf6yz_7JspEbaZM5LMEwDbuEleq-1Ejp2ngjqo_eI7zQl1SlMNdxz3JeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
جوری که جام‌جهانی قراره به پایان برسه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99786" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mYgBwbxzxNzTttpLEc_z8mZ88CzWUYCoJBJZsxmjH5EDTnvtUQInUXpUfqubp3uDSVmGLMhn3flo0Y0--koXBwhngzaU2weVMIVPJQ3j53rp9Y6X2VVw-3Aym2QaNXBgUKNYimeKRUsRlEi9Dveg3grw3fQZVhKI_zneBWYp8oYdtvvxTRIEASTXNVsKUVL201Ovm1X8979GRg5PExBWmrJzHK8WoNIz4VuxVTiFzV5-I87SM0b_8JBqx5e3uVHlEcp80tCt3Ec8grg9BK1mE4suHpY3msCFssnNG5x0HzO_udytHtcaf_LzP72p8tT3kWDweYTit7FEeLcK8C3oNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJsPSdzbENlX2VmIZxYIqkpnllBH314lefBuUVzZ-TyhOlatMIQp8bPz5AEyyev6jsiqLcvCC1hi2ulmCOjrurqg7Pt2B7xMlHlMqJe17XRO1kLnGMQS7Iei8tVdO7dbsejjTaIzlaGgp3FAo6xMXcHF9TbB3NdwRpfpz9soTIn_L6_5YVIr1Ray7mNhFKUZVH2zB5clthMgfgfYyciLHPyhtnJccD6h85HvmAAHVtnUNODCvGuAp_IYrS5YvOpQoWyura12roenORzZBI60uMXy2MIMidhAPTlvkAdpglD-cSH4oelRu22xsMAvtXfEAm6gfMRgwyEwm1s1nq4hdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چقدر به دروازه نزدیک‌تر بازی میکنه مهارنشدنی‌تر میشه. انگار بیشتر یه مهاجمه با قابلیت‌های یه هافبک نه برعکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99784" target="_blank">📅 10:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=AYM-NdpiQOWUrMpooUUF0DTvi_dc29BNkkwuJh5GLyjAAmU1wQBMRYUYCdcoP4LbJY32qiX0s0AbO6YAbJaUDOYz961c4kvMtG7DSbtxO6SpBH5Ej3zwBQbJFtSvFeUuO7Zmc1qvJf9WojhbCa-DNG3XkjkH-XA_zRBYXGWc2FdOdaGyAwIJ0SZCuKK_NPzemY3_IqzQOfaJRQBsxipnxKDDlTIeha_GQWNnGx5shXwzE6pcnVfL9FvY98MedIK2zLsvslfn7ed6KC_Xfd9DzSXH2nccf7XWYN7uNsCq073YHpcfAJdjPiO6iAMUFMyxq1_NpGjRWOoYQbyr0A-Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=AYM-NdpiQOWUrMpooUUF0DTvi_dc29BNkkwuJh5GLyjAAmU1wQBMRYUYCdcoP4LbJY32qiX0s0AbO6YAbJaUDOYz961c4kvMtG7DSbtxO6SpBH5Ej3zwBQbJFtSvFeUuO7Zmc1qvJf9WojhbCa-DNG3XkjkH-XA_zRBYXGWc2FdOdaGyAwIJ0SZCuKK_NPzemY3_IqzQOfaJRQBsxipnxKDDlTIeha_GQWNnGx5shXwzE6pcnVfL9FvY98MedIK2zLsvslfn7ed6KC_Xfd9DzSXH2nccf7XWYN7uNsCq073YHpcfAJdjPiO6iAMUFMyxq1_NpGjRWOoYQbyr0A-Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند اینقدر حوصله‌شون سر میره دست به همچین کارای کسشر و احمقانه‌ای میزنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99783" target="_blank">📅 10:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4x69B7Q4qFGzqMyqAn7MIsCAerOiDHP2769dt79KbL9tjV2OJ7QPuL87UHpxFHnylJsFuBX4GiUe83j6g_wHIhS58tbUOT_-0gEuhq7FkeECKQ2sWyAIcMA3XrzAdpHg1fn_s2roSuqB2FWCtyYBIk_BKtqdTfDJoOLA_HA29cAd2NOGKu224eXCoKsIyb-rqq1eL1SbSvuItp90DQ0jraD289ZJmhvWLBDGqRXcsiQjjZuVneseJSrrfB-DoMuK7mMiDdICdv0DbnkVtJQqaQpiJCJBwybTWvJ3oJWkrY7CZ7jSMq7__g_mXHYlS5J2JKhMhk9pbixcpnny0-dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام سناتور جمهوری خواه و از حامیان ترامپ بر اثر بیماری درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99782" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=Bbw8xMbKWkKbPbpeGp__r2jmAs1Ec_vgZXdy2CGv76q7zKZ_6dQ5cEovKKRvcwbM8pDNoRrWeF1fv2mdIgRiHKMhy5JmiDdnMyEbxGSm01yV4nB1aAalaD25rfhlsFh3eB46JLplFpRGlsORetlxb458mhdNDUau_hVxPeMnqhZlNfooKSFQ-3gIgmIjAgtJaFeyUB25-0Q3K1WS_2YmE4HYPrfRaYAxthWvgacmbseG2A6b3XxnAzAVR1HeFOsijbrL6lwRuLIq4CrC6L_bTCOfym1zqO66WFyEOy7JAnlJeKtxl24ketlH518L-O57eL1OAr9S2CBh_RSqUpQuKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=Bbw8xMbKWkKbPbpeGp__r2jmAs1Ec_vgZXdy2CGv76q7zKZ_6dQ5cEovKKRvcwbM8pDNoRrWeF1fv2mdIgRiHKMhy5JmiDdnMyEbxGSm01yV4nB1aAalaD25rfhlsFh3eB46JLplFpRGlsORetlxb458mhdNDUau_hVxPeMnqhZlNfooKSFQ-3gIgmIjAgtJaFeyUB25-0Q3K1WS_2YmE4HYPrfRaYAxthWvgacmbseG2A6b3XxnAzAVR1HeFOsijbrL6lwRuLIq4CrC6L_bTCOfym1zqO66WFyEOy7JAnlJeKtxl24ketlH518L-O57eL1OAr9S2CBh_RSqUpQuKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
صحنه زیبا در حاشیه بازی نروژ و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99781" target="_blank">📅 09:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iGUgyoLBmMZLwvL58wQCDrnC_4CFd7UtBwbq4gUrfpYlSkpckJEYJXJ3qyiVqKInVLa5t6mQoO2FaALk7BROydW3R80TYe550LRawtPBAoHZpFdxjan4L00g0KfTT8q5wmQlSAo_2g1PCZHj1_BiomALWsisGUCrMtAubEhRwUKLcOxyEysXb6eS2JjW7Rox9Eq9OkddYdxGboxCn5wYiwWqqOXM2G0-4ex-9SJN9sysisp4fMM0QxAZNOymzMhr3hJnkbNd0fmq_Xidfu3C1dI4DMSdtKQe_7D_hPY1pJibkbLf1UiBT-l1P2ghl3v4l5KbAMf8ls0fV8afFWxjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iGUgyoLBmMZLwvL58wQCDrnC_4CFd7UtBwbq4gUrfpYlSkpckJEYJXJ3qyiVqKInVLa5t6mQoO2FaALk7BROydW3R80TYe550LRawtPBAoHZpFdxjan4L00g0KfTT8q5wmQlSAo_2g1PCZHj1_BiomALWsisGUCrMtAubEhRwUKLcOxyEysXb6eS2JjW7Rox9Eq9OkddYdxGboxCn5wYiwWqqOXM2G0-4ex-9SJN9sysisp4fMM0QxAZNOymzMhr3hJnkbNd0fmq_Xidfu3C1dI4DMSdtKQe_7D_hPY1pJibkbLf1UiBT-l1P2ghl3v4l5KbAMf8ls0fV8afFWxjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
واکنش تند فیروز کریمی به عملکرد بازیکنان نروژ!
فیروز کریمی با انتقاد از تصمیم عجیب این بازیکن گفت:
«اگر دسته سه تهران هم بود، پاس می‌داد!»
😅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99780" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99779">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eROSM29RFf_LK-RGlWmqBDIj0_2N0WBGKvEtV9PQc6ruIZ5yBHdaNkgu72evs_qNc0BrpijDskfW4lZjOrYdElR2tRJRx8oRsacbIzlOuiHfjix8dsrzZgf5dC2mVswEaXbBmhxn8fb-3NmPeatIveo5qVAAl0mq3EBgZxFphFGX1mzC7CKbNEYSKyGH3eMSXpGtEk3c25KPCE4sLaW9X8BGbJ2x8Oo5yDeeOd0LuSPxA1ptvFbCJQNojVRIsYhYjXDw86G6qI3fV_kv-jyrxyemHyFTGYGaH5aQR_wBtpbgJCsJenEN-oiTkkgsAvL9PAeDhAAsbwekGq0Oyk1oAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک امروز 1 میلیون دلار رو کانر بت زده بود، که تو 30 ثانیه اول باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99779" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99778">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=vDp5Nk4wG2l82k1EAUlxnp35DaCwgEzftXyubOR5nXlB3SOVXY2ZhiASGCJypI3oixy72HalBej-0iohD6OyI1OarS0EEUmWwP7YLtavtKTESJHdt2RPPThCbwQMO8kLxvGUOzi_0yeTnDOoIWDvd1OxyMhYk9i6WFBo985UdTDhIqqujlfEuax_PwI3rN7aMgwskWzPw12I6ugQsHF_iNUTkS4ZFXFOJdROy_fNJhwNwTfXM_Dx8kM6ef3xr0s4BhTPdup1MSBh9pO0XL8QWbWxgCdG2s_rLHHUhCzHga_BFcTPbJ7h2wn0iQQVorvMEEvSkgHJKY3H4zRCGOoV8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=vDp5Nk4wG2l82k1EAUlxnp35DaCwgEzftXyubOR5nXlB3SOVXY2ZhiASGCJypI3oixy72HalBej-0iohD6OyI1OarS0EEUmWwP7YLtavtKTESJHdt2RPPThCbwQMO8kLxvGUOzi_0yeTnDOoIWDvd1OxyMhYk9i6WFBo985UdTDhIqqujlfEuax_PwI3rN7aMgwskWzPw12I6ugQsHF_iNUTkS4ZFXFOJdROy_fNJhwNwTfXM_Dx8kM6ef3xr0s4BhTPdup1MSBh9pO0XL8QWbWxgCdG2s_rLHHUhCzHga_BFcTPbJ7h2wn0iQQVorvMEEvSkgHJKY3H4zRCGOoV8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در نیمه نهایی به آرژانتین رسید!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99778" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99777">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=BwAq-tUiOLgJfSIz2lwe9dJbA04ugv_ie3IaYC1nBJAR1SFIdWwIIBV0nS4g0yLcYpKY2_cGvIISgJ0VQyQ8CbV6tEKmITROx4F2TVXwne7ylWdnS8oIPcelTIB29iEzjp9yBVQzjlIvAId0_kgEwfG13U9EvNdaxswGBHQK4dZHK9ffYXifhL4dHvHBGy4rFDdtDw3xtw2WekajIsoaj6pju3SMs3xPxxys3L93mvEkGc80XSdWBkKkI4ydiMmxbAL88eFN-IdSrM7xz1STXnT6_MkkggPdC1SYcpGB90Y5aRIjgWETIcE5_tA2hyLgsRLOuxNVIyDzetcUrMyg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=BwAq-tUiOLgJfSIz2lwe9dJbA04ugv_ie3IaYC1nBJAR1SFIdWwIIBV0nS4g0yLcYpKY2_cGvIISgJ0VQyQ8CbV6tEKmITROx4F2TVXwne7ylWdnS8oIPcelTIB29iEzjp9yBVQzjlIvAId0_kgEwfG13U9EvNdaxswGBHQK4dZHK9ffYXifhL4dHvHBGy4rFDdtDw3xtw2WekajIsoaj6pju3SMs3xPxxys3L93mvEkGc80XSdWBkKkI4ydiMmxbAL88eFN-IdSrM7xz1STXnT6_MkkggPdC1SYcpGB90Y5aRIjgWETIcE5_tA2hyLgsRLOuxNVIyDzetcUrMyg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😆
😆
😆
مکالمه پاره‌کننده دیشب هومن افاضلی و خداداد عزیزی. کپشن اصل داستانه⁩
من از شجاع پرسیدم!⁩ شجاع بهم گفت! گفت که بدنامون خسته بوده! خواب بوده
😂
⁩⁩ ولی هومن
💀
⁩⁩⁩ بعد همون شجاع
😂
😂
⁩ گفت غضلاتم همه گرفته، عضله رو ولشن!!!⁩پاهاش اینجوریه دیدی که
👐🏽
😂
، اگه پاش اینطوری بود
🦵🏻
آفساید نمیشد ما الان بالا بودیم
😂
😂
⁩⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99777" target="_blank">📅 08:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99776">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn0LWv-O5fpQ9R6U4oSDzM1WmUVVHE54kO6IkviGw23ThnuNRHNoSWS-5RhL1rUXtqWQSv1wLt4cvVHgjZEmsHsh4c4yKMU9E0srR8gIB8gvzCxdCaLwJ8j1tSotopr9TQL_3rs2Qiz3JIFT3hhvbJikHH9XgBYb3ZyP47WoKefGlBEPu_TjAqYyMN64A8iOw-c-eKtYV-yherrHchQqrAQpPQ-5Ma7RzekFFG-q79ls8RsGAAPqbKCkC4mBvm_iTyaPk9mYp_0Fs-4xhRDp7NdRXvEXaLwSpnDuQRRDW8jwh5QPuUWDc1oCm5K4OtgCXQ8ElPqMs-y4I3B7BkKSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی اولین بازیکن تاریخ شد که 15 بازی در دور حذفی جام جهانی انجام داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99776" target="_blank">📅 08:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99775">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elHoKhCD2LYI8sMtTlM8xFIpLtYllWHK6GBqlHRrK0kVWQgeIIuWFujHL-WhSsVe3fq_aU1TVNU4DKMPLg26PsdaajNs_45_9XjdIzyOutZoXpVwTB5mrzL1z74o97GFMVX3lGoAO2DLuHTV8807ojdnkAKsEmtttT8cgV5y-ep81fFNMkd6sYsC5TQhHvEP24LeBh0QK1rBKnvPgVhzkqAsG_4tQDuHWMVu_GebNaVY0bIO_UQvqXEkGZM9_mVP01-MZz225D-VGcN5jqoM4XLrG0-s8msWzEQmgehEfyuJfczY3QnAjDDsCVkxkfDbaGogGuL5wsfCANG5GhDkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇦🇷
خولیان آلوارز: مثل یک ارتش پشت‌سر رهبر خود لیونل‌مسی هستیم و هرکاری برای قهرمان شدن مجدد وی در جام‌جهانی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99775" target="_blank">📅 07:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq4jgQRoxTklOz9eVnh9_LYCvBbKVeApW9gnuJMHOwZo1Utxs61nJeW7PjGwtR1U5funxiLWAtp-yo5NzEFS_aIIV-3AWdqWQUmnMLhDKVAoZlasyCxPcfD6mW2YTgxoYgLUjHNoY7oEEfaF3rR9fS7KiIoLzLPm8c-apKno_ty-QPaZrP7PUbZICA3oIj7ykQFKOkc_-lZ28SX8GkYFdf-PLym7rAyF9nH9G55eB-Us309jpt4WleCWNeQqdBWVQXNq1u4zqLOoIj0cu-9qnY6s-Gmxg9yW3vEqA-RZE1O7HbScPtR0gJyb7MA3AA4AyJNrl0UJLNoKEpEEl1lgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تیم‌هایی که در طول تاریخ بیشترین تعداد به نیمه‌نهایی جام جهانی رسیده‌اند:
‏12 بار —
🇩🇪
آلمان
‏8 بار —
🇧🇷
برزیل
‏8 بار —
🇫🇷
فرانسه
‏7 بار —
🇮🇹
ایتالیا
‏6 بار —
🇦🇷
آرژانتین
‏4 بار —
🇺🇾
اروگوئه
‏4 بار —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99774" target="_blank">📅 07:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyVuO8u2yUTTx0H19XIJJqX7bRfNNGkiX5ibQmxGQE3dcxcTIEsTEDdKj9f0aFfgoR1584csAQSilUBzghjFjvAObCXmuMJy1qU7cpFUtXk8IfvoclHMkAWBRyHaM8cI8zYLRgYQ89vt1UswHbib-40ItxzZjVkOPoKj6f-S8XyeYe6dPjQPAsNYzi_YZqAxrxcgakkcmq_vjboPn9d6qGyBSaWypYWEoMPTGPZtWdYsQakK_NB4NW803t1M4r_rtdZ_UKVaz5MLyVf7JeOpHVxxO8tD5eIICxvcijCevuslDZNcqDf8_jqD8arOt8K17hWj8jFU-hN39Y8-N8Olww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
خولیان آلوارز رکورد مارادونا با ۵ گل در مراحل حذفی جام‌جهانی رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99773" target="_blank">📅 07:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoOml1PXfs60i7ZoY6p27i5S6kAMJUmPaYQiuYVKcVji72cjMJ1HtXLnbFCZmHte_UDWrBTNtF_kmmqyx1BuI853DhovCllxQKDzgizFnpnGpS-UEctRYPjmzxzGF6adJXYGh6UR9yT_aaC_cWVD-jQMLWqVZqC-YnqHag-_WJl-IUFqrsLyiejn2oQZ7yL4AKFJLtxdYtrfN5T0EPFkii8OjZCvQyaV5Ph8cMORpGlwevs8PRvZpzJ3Oh7AbWmGtKPVluAJwSo1PtioCfZdVQpqdOz2pqkZ2GaeUkh30kBiU69MQR1n26fGLqU5bCKePa0h0nsa9Bs84Qo5eD5EAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آرژانتین نخستین تیمی در تاریخ جام جهانی شد که بدون مصاف با ده تیم برتر رنکینگ فیفا به نیمه‌نهایی صعود کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99772" target="_blank">📅 07:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMPxmqRb6BjypwLxiBTIklJcazS2ySdGflVvrF5Tsl69HP9eDLgHkAIKC3d_XePIaNB4V7xAS9KdGRQy9GuPZzHQrywBsb0v_BDDNn-s6s2J3fuK7Ps74kzLJWZpgyeqHk1KGU8Sz0LwkCky-zL9lKnFc4nNUo84SggVfgDI70jtnOigu09FMIScaDekNqD_EM-JccHwH-Fczo7ABKMZQ9fHKhPKcdurLUjCzyikj2oBo7bFUIrAB6ptQAhiKrMg7-631x3KvteatmGLr8_gHbkjo2eNl34vvCnQxna50-XGbMy6GnJ4p-kV2wOwxUtnsVaITuxkGaT56woUatoJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
| برای اولین بار در تاریخ جام جهانی، چهار تیم برتر رنکینگ فیفا در مرحله نیمه‌نهایی با یکدیگر رقابت خواهند کرد:
🇫🇷
- فرانسه (رتبه ۱).
🇦🇷
- آرژانتین (رتبه ۲).
🇪🇸
- اسپانیا (رتبه ۳).
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس (رتبه ۴).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99771" target="_blank">📅 07:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99770">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=mCB7U9BAj-84Leaf9osAvafYNLQqQxC30dZu0f9uAgzHBislmzDvmmD2e1d_p1Cdi9ScFGnsPdvh6Nku45UocrLVuwq13-uNTRq8fk7tiwDLhoDsB97Okgv1A5hP73-02TbdUMSx0nfhEg0aAZnxHJvufKE0G3OPRQ6QcXiHSaYbW1dQ7FO4Wy3MlKXUJ5sSR2_F7DRQchkQVvsEb1kCr7Sfl-jvVIc5Sm4loh34JaN50iKEihNrwlG7ROT1biAkAFFGEJhOll2aRnrtVzkaDYVZhFKONtBsusSgtT7ffBRR-8mEfj7JqYZ3LmbwNXNDXQVkjA72rPruR0nB3hxTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=mCB7U9BAj-84Leaf9osAvafYNLQqQxC30dZu0f9uAgzHBislmzDvmmD2e1d_p1Cdi9ScFGnsPdvh6Nku45UocrLVuwq13-uNTRq8fk7tiwDLhoDsB97Okgv1A5hP73-02TbdUMSx0nfhEg0aAZnxHJvufKE0G3OPRQ6QcXiHSaYbW1dQ7FO4Wy3MlKXUJ5sSR2_F7DRQchkQVvsEb1kCr7Sfl-jvVIc5Sm4loh34JaN50iKEihNrwlG7ROT1biAkAFFGEJhOll2aRnrtVzkaDYVZhFKONtBsusSgtT7ffBRR-8mEfj7JqYZ3LmbwNXNDXQVkjA72rPruR0nB3hxTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی عجب کیری خورد تو این جام جهانی اسپید طفلک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99770" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99769">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrquMayT0T8W4jRnE8-CW3F05a7KEVwJ9F3IpqKuhj4R9M_rrM74VqzzCNsp2DbO1vTFgHhTqHfahIxNFnZsombD5lDbdZlOXLnu2pxQhM-RgNwryqknyYxYrq0fqdHwxiZEVt-pkImExU33MIvZzTnbDz_K08fL3J3AP_fk6_O2OCFaoeBME9ruYeJJXu-BYUl3YLVmLouMN0I9QbeW-eSlc7OgS6AgTi_27l1dMtebnTh8DuebIyNghJp15nc9ls6zyDJ_k3H_1i8Jl4pg4aZWTKKXjdIM_L1QT2jOGPL-A4U4vSmNyoBMopo8yjgK7YGxzSXN3a4LEuMwgy7wbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🥶
🥶
قهرمان رو با ریکشن نشون بدید
🔥
فرانسه
❤️
آرژانتین
👍
اسپانیا
🤯
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99769" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99768" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnNj_KGSrbo_Fh71AodfnjDCX8QNZoaf7SbnfN9V_7daPyQFn1tkCEvfDhAgwJC1ZNojI0aARBRZ_eYLh6nrZrTMjNNWb_GoBrZgAXDnZfgXHkhuMjXflIzi8G0qmWVFh-JG5n9z6fwEHuzbsgJ1gvx6RxYDuGzYNKABtN4Plas-o9nkOs0HSr8iRriL_UwsF6VHimTLpZKW6Vx1nGU_mjrzFvnVr-z_5FWyxUUclM1dKARrRYf5OcAuKqIZ0YAWUxVgz06utCSr4pVnpYizKQ0DVSzfyxMsxkEnYYlOlazAzcNH-gjPhQGV5Zxy0WZ53cUAtplgd3cSN8XhXkU2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
برای سومین‌بار پس از دوره ۱۹۷۰ و ۱۹۹۰، هر چهار تیم حاضر در مرحله نیمه‌نهایی جام‌جهانی سابقه قهرمانی در این مسابقات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99767" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiqGr4WCDCn7hCZOEo-Z3luvFM31Zc-cI492ZNwnXM_K60joh_Zsfs8ESdbpJd2nT-xItxr3MGpvfecM_ciUkyvq2lWqxyCj6oFQR-E3uGMERiSGaGuWuGZo6KcdvUvgJ5X1KpVKpbKy3WN8FDzAcDCZiZZYOXY7rMM0neekg18JXTboUhVJOSOCv0nsb5urF9pFAUfbpeFRJGvNFAEDS9Ny8nkbKvdAg_ltPRArPCdZN2Dmpko36ovSy29yhpPghJrY_fCJ2o2WBjQDDWMvQpID7a4nEo1Z2pohekxulrf5ln-9DXRiOyULAP6K3AUmcMZU__vVQZrtLsfuEmNUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسو ببین یا خداااا
🥶
🥶
🥶
🐍
🐍
🐍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99766" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2athkYKPwWD3v9lmAGQAeevDpMEnPEDXr4eUAUlxRebuDUxlCus_C4jmQ4JCo_uoQAvxCAnfH0lB82lrrnSZzhWBquu31qScXNVL5h8FIVndiJUvpQZeqxUWEqMiejqKx7bUH9qNUr2jGoMsILZGi-CfQTStu2XnHMB2yNUqiugnl-4GYzOxX5uf2tCrPujSohiKFaoMGyfP3KXbXzu2QVQgYJP_Ylt4D-Cki9icGHFKTWyOGKpDeOfiUKeIswOtBOrdNFg2Kef-b1ZvnlWLf4VNtHglaIXU_dmb8E67gm-LMLvC8LZs-F41FI2vNfQ1bwK358ynNVS59DOPkk6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی برای اولین بار در دوران فوتبالش، مقابل تیم ملی انگلیس قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99765" target="_blank">📅 07:19 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
