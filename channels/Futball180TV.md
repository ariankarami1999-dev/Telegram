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
<img src="https://cdn5.telesco.pe/file/Yk_aN2BNTEALTKKu37m1Dux5Gr5Ra3gqdJEQykIzYOz144QoJ2mgzOpSz_fAWDYG83CgDl2FX4JoMlG04Em4uWZGS_Up70pBlqmgTDZzROhnSmqjQ4wRdxjA0C916tKckkdQNes02XAoDy_WmQ0PgDYX0DpoBsSxNc5TZZXdc1Cc4XEGNXZ6F2NpZ5W2BejUkGf1NRG1siFnrkq74Ecz7GYCtldYMqnWEcHC3ZsGLkomT234wkjo7OOarFvMVxb5R-yPoLtx4JNwHlOsUYhYJEj9pPq5Bo2c7R27up7sTzPVVpI2tQoAVm7lorlbGPe3qsHexM1QGe866DPeliOUJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 425K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-105684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=UviRSFVHG8wAVYFx3ag1_wA1k2lDJC3ckoovIfWLnAglvTC18C3F0F1ftxlaYrdsypdARQD9gD3Oi2txH7KM1jFzIee3jOPk1xLcyZ0IiytT_G2Y48cS96bsDE_1IV67y7XOS57AwkEUCFGTV_28v6wHQ59CIV6RsbHUT1BhZq6N4tj94r-95waJGJss-91Yg5O3lE_tsMdebqlQENV4xlxbOTHYvvJ5aPV6oQhY4a8jU7XfiWb5b2pjxoISPct9dLVDEul0dW0oTTVCowLmSMRzY77Q1LrxsGHDdb1arrSu3iM07AkdtnQuiKrmUFsphtmy_8b37uuTB9G0VgexUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=UviRSFVHG8wAVYFx3ag1_wA1k2lDJC3ckoovIfWLnAglvTC18C3F0F1ftxlaYrdsypdARQD9gD3Oi2txH7KM1jFzIee3jOPk1xLcyZ0IiytT_G2Y48cS96bsDE_1IV67y7XOS57AwkEUCFGTV_28v6wHQ59CIV6RsbHUT1BhZq6N4tj94r-95waJGJss-91Yg5O3lE_tsMdebqlQENV4xlxbOTHYvvJ5aPV6oQhY4a8jU7XfiWb5b2pjxoISPct9dLVDEul0dW0oTTVCowLmSMRzY77Q1LrxsGHDdb1arrSu3iM07AkdtnQuiKrmUFsphtmy_8b37uuTB9G0VgexUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
وضعیت دیشب امید عالیشاه هنگام ترک استادیوم یادگار امام تبریز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/105684" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105683">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=vJxMY_u3Vs5hWKxow-VALG3RzALQk1oMIVjE_e7DigHQ1kgnM6rUFy0GleoqHJl47lmyhKH-t-Z0BtgnNuliD-fIT_NSHFM2I6yFeIF5JkTTZBRMvlEpMf2uG-7OobQsoPNgTyQwPwAW8VQB4vZVCOAV3SHkhgQQGgPEchiktSCJ1ta6BeHJ8pw7lioM-946f-i3pNnF9S4iup6R7-EXMCyxiDaFp160QBaHjxUb-Ydw_z0HWEuOb90YWXCSg82C_LZoY2_AZE-2whQVQTNpOlwFQt5Y3I4tdl9Iq3iiRfBRKK3Lxv8MQb8qiQxSV5ry7a8gOnLnM8huY_vOryBnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=vJxMY_u3Vs5hWKxow-VALG3RzALQk1oMIVjE_e7DigHQ1kgnM6rUFy0GleoqHJl47lmyhKH-t-Z0BtgnNuliD-fIT_NSHFM2I6yFeIF5JkTTZBRMvlEpMf2uG-7OobQsoPNgTyQwPwAW8VQB4vZVCOAV3SHkhgQQGgPEchiktSCJ1ta6BeHJ8pw7lioM-946f-i3pNnF9S4iup6R7-EXMCyxiDaFp160QBaHjxUb-Ydw_z0HWEuOb90YWXCSg82C_LZoY2_AZE-2whQVQTNpOlwFQt5Y3I4tdl9Iq3iiRfBRKK3Lxv8MQb8qiQxSV5ry7a8gOnLnM8huY_vOryBnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇮🇹
شادی فوق‌العاده شب‌گذشته لائوتارو‌با هواداران تیم فوتبال‌اینتر از این زاویه خاص
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/105683" target="_blank">📅 16:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس: اینکه پنجره نقل‌وانتقالات تیم استقلال بسته شده به من ربطی نداره و مشکل از مدیریت خودشونه. اگه استقلال بازیکنانش رو به تیم‌ملی امید داد ماهم میدیم. اگر اونا ندادن ما هم نمیدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/105682" target="_blank">📅 15:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105681">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی تارتار، سرمربی پرسپولیس:
از فیروز کریمی(پدر زنم)من خیلی چیزها یاد گرفتم‌. الان چون ایشان استقلالی است زیاد نمی توانم مشورت بگیرم اما از او چیزهای زیادی یاد گرفته ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/105681" target="_blank">📅 15:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/105680" target="_blank">📅 15:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
واکنش تارتار به گل پیروزی‌بخش تراکتور مقابل گل‌گهر: نتیجه باید در زمین مشخص شود/ مطمئنم که مسئولین بررسی‌های لازم را انجام خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/105679" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=FAChvuDse1ZPhpX4xy_ZxRR014G0MsJYifTkMLt1dCGmfpkMg-IpOa_rQlQXf_pkXYYUt-w5b5O033BsUhnUE-b4hf6EzqNxEnGMan5gXHXhVFj6GYWzwUZHGpOhKzjtqaLQ6QirPAIUpQqU2dsJaop9Fud3eg6SUtENyPSAiYUoXCdJExNG7DCe4baayHaEBCK0iQnKpyxt6bCTisAzOW4ncUQoSyqBLuQuMmAChfpvkSRWvvlYY6iYCfsK0uLocUb2B_K08keGAot_rrD2sgvEK7zb5IkNEKrGySz82k8lkUlVQl1JuG1k_gzLUdRb7x483ZuWdD0fekwS-lecsIBHI3mhJRcECdHcmj9p334qcZV2a0Ds9jiaZgY9_yK6DfzLhjw3fG566mG-RKJPuOgAp9GlNaqKdXP-Is8zEhpgxY5fS5AN6rT3n_6Qpg94WBrHke0htT4ZajwT_q3rfVltldNmY1e-h8J-LgqCgO71nFqi_qef8QExslWWo4HMIl6yNKOKvOF9KHZjTYVzDwPM1vRGF1bhJqx_3TrQJO8qQjdTinj2-_CBLph5pkdOPhLm6vfIlvY9Ar0gHGiDgh6UEkV-waK9xUOJOjtyvKc4xdOGqWZ_30JopqNnBpO1yDyr4Iu700uUefbUycNCKhMbWCGA2NqXL7MbomohOX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=FAChvuDse1ZPhpX4xy_ZxRR014G0MsJYifTkMLt1dCGmfpkMg-IpOa_rQlQXf_pkXYYUt-w5b5O033BsUhnUE-b4hf6EzqNxEnGMan5gXHXhVFj6GYWzwUZHGpOhKzjtqaLQ6QirPAIUpQqU2dsJaop9Fud3eg6SUtENyPSAiYUoXCdJExNG7DCe4baayHaEBCK0iQnKpyxt6bCTisAzOW4ncUQoSyqBLuQuMmAChfpvkSRWvvlYY6iYCfsK0uLocUb2B_K08keGAot_rrD2sgvEK7zb5IkNEKrGySz82k8lkUlVQl1JuG1k_gzLUdRb7x483ZuWdD0fekwS-lecsIBHI3mhJRcECdHcmj9p334qcZV2a0Ds9jiaZgY9_yK6DfzLhjw3fG566mG-RKJPuOgAp9GlNaqKdXP-Is8zEhpgxY5fS5AN6rT3n_6Qpg94WBrHke0htT4ZajwT_q3rfVltldNmY1e-h8J-LgqCgO71nFqi_qef8QExslWWo4HMIl6yNKOKvOF9KHZjTYVzDwPM1vRGF1bhJqx_3TrQJO8qQjdTinj2-_CBLph5pkdOPhLm6vfIlvY9Ar0gHGiDgh6UEkV-waK9xUOJOjtyvKc4xdOGqWZ_30JopqNnBpO1yDyr4Iu700uUefbUycNCKhMbWCGA2NqXL7MbomohOX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/Futball180TV/105678" target="_blank">📅 15:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=jaXD9lbumtcLfolrmZ-WKXQAA48AjMVOafZg2oR1EKfP5AD7MLfryLAZ5a1QLZ4fBNamYq39bUAaxj4X_ZFvXZVgPZYjeJt-3L5Z6SeUQYEQ8I_msjPJk4uqi7TY2NZLzNVYgOnVpT_NWS9VV0j7zn50eDm5N18p7a2Dj330tfR7pstT1vB3ip7xFdxyURo_Fixw8_GU3krn5mcYZLxUhLARrJaQwO6hXtKR3Gxoi8qoEer1XnHWtRpTEcZYTqFgSpSl_JlFRjVRDKQ7plC5AhdtX52yv11vvZAqaYD3IBQnWh7wVL1v54xHnSXxvfQJP3DVPbw32nSLefIo5rAI0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=jaXD9lbumtcLfolrmZ-WKXQAA48AjMVOafZg2oR1EKfP5AD7MLfryLAZ5a1QLZ4fBNamYq39bUAaxj4X_ZFvXZVgPZYjeJt-3L5Z6SeUQYEQ8I_msjPJk4uqi7TY2NZLzNVYgOnVpT_NWS9VV0j7zn50eDm5N18p7a2Dj330tfR7pstT1vB3ip7xFdxyURo_Fixw8_GU3krn5mcYZLxUhLARrJaQwO6hXtKR3Gxoi8qoEer1XnHWtRpTEcZYTqFgSpSl_JlFRjVRDKQ7plC5AhdtX52yv11vvZAqaYD3IBQnWh7wVL1v54xHnSXxvfQJP3DVPbw32nSLefIo5rAI0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاطینِ پنالتی این فصل در رئال مادرید دور هم جمع شدن.
🤝
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/105677" target="_blank">📅 15:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=FGk12Xm6vmDLl2jKnWMS0lEHXqlLD2j3sR_vhaH7BTp44cYcmWleBcTb9PvYSjPvIzpTd4wcbatTdKJIMkhBRkk4EfnlH_Dt-zPoFVJi1RZIGAUJ1ov4SceAgXMKKmfiLhA956cy_kPMGSu6SIR2JmcwECK7q3VTsLTFGYWfQL1vFE6nLRo8aMVvz2MjlAVZi7rt8NJh5qPI1cCxi7p87knyj6QQj3aJd0sSLoOFNgh7YAHDwAB8mvUzhhLpL3RLe4xHjv6SbwGcn9psgeJIdi3g3W8ruEL31UstG_ezzIz0pvZYBZu3FM8uVvh0NNLPpYstHHapasL5fLwMog80MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=FGk12Xm6vmDLl2jKnWMS0lEHXqlLD2j3sR_vhaH7BTp44cYcmWleBcTb9PvYSjPvIzpTd4wcbatTdKJIMkhBRkk4EfnlH_Dt-zPoFVJi1RZIGAUJ1ov4SceAgXMKKmfiLhA956cy_kPMGSu6SIR2JmcwECK7q3VTsLTFGYWfQL1vFE6nLRo8aMVvz2MjlAVZi7rt8NJh5qPI1cCxi7p87knyj6QQj3aJd0sSLoOFNgh7YAHDwAB8mvUzhhLpL3RLe4xHjv6SbwGcn9psgeJIdi3g3W8ruEL31UstG_ezzIz0pvZYBZu3FM8uVvh0NNLPpYstHHapasL5fLwMog80MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎾
👀
واکنش خانم‌ها به تعویض لباس آلکاراز!
کارلوس آلکاراز پس از پیروزی مقابل وو یی‌بینگ در دور سوم US Open، مقابل جایگاه تماشاگران لباسش را عوض کرد؛ صحنه‌ای که با واکنش‌های جالب هواداران، به‌خصوص خانم‌های حاضر در ردیف‌های نزدیک، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/105676" target="_blank">📅 14:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Pljd0I-KKo4k4abXVspcj2w4cltEVyoulLKILLzJ8QneZOvvDCXt8_dH5MgPEIMbLWhiWpDwv-nAt2zHDc_Bbq7BaM1MCIFde8pTfaym5J3R_yvEIm8Bl0VJDvhcrx9OHiSm9qsPRuplTq-jjIopZQydMWr9124SaVs2jJOmoDv1oN-cqGOhx-Mnqy2yS-_0TxmBlcyhu7faRK6tVFnMuqHCZ6UpTQcZrYsX5CJn2_t5ufiN0zdeu_9hhyhzfXxhYV5WdsRQyBTKALDguSSrsc0gwBk8eH2fRq5bYU84x_xRqD7wprseZa4RqNtYDNgqFbM9Os2N0L5wuoz8tg4qaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Pljd0I-KKo4k4abXVspcj2w4cltEVyoulLKILLzJ8QneZOvvDCXt8_dH5MgPEIMbLWhiWpDwv-nAt2zHDc_Bbq7BaM1MCIFde8pTfaym5J3R_yvEIm8Bl0VJDvhcrx9OHiSm9qsPRuplTq-jjIopZQydMWr9124SaVs2jJOmoDv1oN-cqGOhx-Mnqy2yS-_0TxmBlcyhu7faRK6tVFnMuqHCZ6UpTQcZrYsX5CJn2_t5ufiN0zdeu_9hhyhzfXxhYV5WdsRQyBTKALDguSSrsc0gwBk8eH2fRq5bYU84x_xRqD7wprseZa4RqNtYDNgqFbM9Os2N0L5wuoz8tg4qaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بهی جدیدی، بازیگر نقش مهرو سبابه‌چی، نامزد مسعود شصت‌چی در سریال «مرد سه‌هزار چهره» به کارگردانی مهران مدیری است. وی سابقه فعالیت‌در تئاتر را در کارنامه‌اش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105675" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sH2_v-QtadBIN3Bk5wK_JZNH7qmfi__w9ePOvx-_j9aEhSE5_qvTAgKIj4lUVa6bUiyBGXc6QrDxAGP34OfUQcwIBzvZCvBRC7a7KxFlcXqGbAD0ydZrjIaYbl7XqTHljKmM1JTJMsufXp00K860Ss2Eetc3O2eu_y_YSS3g2PdqBFViDASUM8WJjl9Jtbg_ArRhf6KpeAnLJ-boi3jcLTYc4x7JdX2IRiaU2rGURenPSpMtWB4hZSLGsY8tdzm5S6HPTmhpEcvpbUXapr7z3QcIGyhLbcd58gsICzf18GDmhcamzrUIX_BYRQASj_Q7TFeTqL0_y1vtGUKxUllQink" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sH2_v-QtadBIN3Bk5wK_JZNH7qmfi__w9ePOvx-_j9aEhSE5_qvTAgKIj4lUVa6bUiyBGXc6QrDxAGP34OfUQcwIBzvZCvBRC7a7KxFlcXqGbAD0ydZrjIaYbl7XqTHljKmM1JTJMsufXp00K860Ss2Eetc3O2eu_y_YSS3g2PdqBFViDASUM8WJjl9Jtbg_ArRhf6KpeAnLJ-boi3jcLTYc4x7JdX2IRiaU2rGURenPSpMtWB4hZSLGsY8tdzm5S6HPTmhpEcvpbUXapr7z3QcIGyhLbcd58gsICzf18GDmhcamzrUIX_BYRQASj_Q7TFeTqL0_y1vtGUKxUllQink" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری وزیر کار دولت رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/105674" target="_blank">📅 14:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d1369def.mp4?token=DaHCsjTANwZPd8zZzasqv16SJZa5pu5tdV5zT1-NNaxh5A4xVeKSc4sCzb-dYzRefJnptPgEImuqDoQdRehi6MhcUdYZFZg1tKqLXrp8DL_SuUAVsn8jsSf6B60hZopMKQGDVOwh5e_LEYNz2ylrGCdpntxdkk7qdaO0hDRhDzgiPR6NjFipPMIeU6RTGC1gl2POu-lUmgSyMCeviZ_IuuVHu2X79ifBm9w34AR93dLiapzAJT6_dhKwtCDjJmwaiLHxRCBWtp1yxmzf-VwFmpDkAZGNq7oQXqOb5Y0jUTTtzwKb4SrerdPmdr0RbHBRm-1_ji-ndCxhN98bW57AZ4nRITDv3fptHGA_1kGvL777l3m8_JD1fnbPS3mvW6NRz5noBv1VckJRo3ccdkMGSaI8EzFX_Qh_u-ACbj2dZ_7k56C2S96HLbH5fm62Z99tgIJvEIaSAtasO6G5a-VTVevdItWJ6q-1vAYEblxxg4D8d-23IyZfCP_q1KHMdgUeKC651CaKY2S_jWEN46nHsG_0H3F7MrrJXaMXqUyRIE_aJbIlPLGQQUuFvyos-tCyBaOONq6J3zumpUvzxVO1u2t2NgZ5VTQoS_iGlzjksoLCqoolUWB4TC2PnquXXfnX9RGtqC1pqZ3Srsg8T81CWl0HLXNFuI4JoPMADMBcrzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d1369def.mp4?token=DaHCsjTANwZPd8zZzasqv16SJZa5pu5tdV5zT1-NNaxh5A4xVeKSc4sCzb-dYzRefJnptPgEImuqDoQdRehi6MhcUdYZFZg1tKqLXrp8DL_SuUAVsn8jsSf6B60hZopMKQGDVOwh5e_LEYNz2ylrGCdpntxdkk7qdaO0hDRhDzgiPR6NjFipPMIeU6RTGC1gl2POu-lUmgSyMCeviZ_IuuVHu2X79ifBm9w34AR93dLiapzAJT6_dhKwtCDjJmwaiLHxRCBWtp1yxmzf-VwFmpDkAZGNq7oQXqOb5Y0jUTTtzwKb4SrerdPmdr0RbHBRm-1_ji-ndCxhN98bW57AZ4nRITDv3fptHGA_1kGvL777l3m8_JD1fnbPS3mvW6NRz5noBv1VckJRo3ccdkMGSaI8EzFX_Qh_u-ACbj2dZ_7k56C2S96HLbH5fm62Z99tgIJvEIaSAtasO6G5a-VTVevdItWJ6q-1vAYEblxxg4D8d-23IyZfCP_q1KHMdgUeKC651CaKY2S_jWEN46nHsG_0H3F7MrrJXaMXqUyRIE_aJbIlPLGQQUuFvyos-tCyBaOONq6J3zumpUvzxVO1u2t2NgZ5VTQoS_iGlzjksoLCqoolUWB4TC2PnquXXfnX9RGtqC1pqZ3Srsg8T81CWl0HLXNFuI4JoPMADMBcrzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
جمله کنایه‌آمیز نکونام: چون یکسری قانون خوب داریم، تا نیم‌فصل نمی‌توانیم بازیکن بزرگسال بجای مهدی‌ترابی جذب کنیم. خودمان برای حضور در آسیا دست و پای خودمان را می‌بندیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105673" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105672" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105672" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeZTR4HSxy5Vg1P186ADbc7xAoizTpqahUX7OGNeEXEDz4LqcX72NnBbnDiXWdz2g25L2z2ZhPYSuz6ATPmMVntJMz3kvIqyFqQLHXU9z6ssbcmD-l0x0VZXiWpiKaLc8D-RDVifnuOud5m2_saCEyJKCUsEqpm-k_jDIvM1ODc3zFwDtXGS0QC3C0sYmWWYaBu7c5AJJq-ESRsd7zaLhE3Ly8oK5PtHliknghyGDiHTly9mK4dglvtty7IgiM7Ie4pdO46M4ipHrIwFo6fiNbPnPk4Wq0p0NTGOiiOXWA_7-Mh0UaBclv3TYydGMZX7KLldVahYaBethjzCLsuNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105671" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AltGx_nBK4ouUEM972RpCXZKOoZX2MFkubhjS2hs0LnQtLo6TD1PSg3bEhBHF9f7-PvbRBwk948_7Yuhi2MMxyQfwB6r6LhbWSnIs-Tbjw2I3MAxlwwO2mODpOHEHy1s4k3WPuhG033EuKLZARusWZdzXups8ncZhw8DlLe6N2bOjB62Ihw6Y02evSQlYWYP3PkQakeaeihYd8v9L0k6-DX45cOyY_JBqNKUljN_rKLqCpdAVFczOnC8r9UEhdG47WHYnbiyD1yFJMAaVBA93rOgpK2A_IkrseAounwiEIBPbbJWiE6IkovmuwiumYbAJaqNxxc6rXh-4pdvpbri_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🤩
🇮🇹
🇪🇸
مایکل‌اولیور انگلیسی داور بازی روز سه‌شنبه رئال‌مادرید و‌ اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105670" target="_blank">📅 13:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=MXKiklKrFSlrR5P28FWD6N3S3x9-qKsPqqrS566EFnHBM8NTUEJX8yCzbIUimF8_B45dwWkkVNHtmGa1vlRMK1HCEL-vDoYNWz30Bnd6oUnvI3Nybeun5j15KHeQAmVT9mgxmM-a9GAI5q3kxvi-ZBN4tY6AASAo9wD-gJ9ju5daYbtBY4CH9H32bZgVJ-keeMoVIfuItrqu7pZQzek8RojhxVu_rIv1MZMt6KcxVw6ixKFfpre6XGW4nOsa0S_DnTiokiqPrRSz8AwKsdsrGbxoitov6Jxk9ExZ0cNId1AU2yd0ITgWHyrUSpoa-T1RFMBfqK6MCIvanPvK_5pG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=MXKiklKrFSlrR5P28FWD6N3S3x9-qKsPqqrS566EFnHBM8NTUEJX8yCzbIUimF8_B45dwWkkVNHtmGa1vlRMK1HCEL-vDoYNWz30Bnd6oUnvI3Nybeun5j15KHeQAmVT9mgxmM-a9GAI5q3kxvi-ZBN4tY6AASAo9wD-gJ9ju5daYbtBY4CH9H32bZgVJ-keeMoVIfuItrqu7pZQzek8RojhxVu_rIv1MZMt6KcxVw6ixKFfpre6XGW4nOsa0S_DnTiokiqPrRSz8AwKsdsrGbxoitov6Jxk9ExZ0cNId1AU2yd0ITgWHyrUSpoa-T1RFMBfqK6MCIvanPvK_5pG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا در مراسم معارفه ایوب بوعدی به بازیکنان سیتی: فقط خودت باش، ما میدونیم تو چقدر خوبی، اینجا لازم نیست چیزی رو به کسی اثبات کنی. کار کن، یاد بگیر، لذت ببر و خودت باش.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105669" target="_blank">📅 13:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=torDMykcFBIMAOcbU2NW02ucmSYozrRtPAC-yj14pRpmclxDUWK0ic6GrAuIqN7j0dwVXA2jeDMLpPSyHZlwPPE8-Ojr9lr7KzDvwDMEUY_qhRSb58U-tBHhmMGsBrdAgcYY7HZ3HN8CuvIGBk3DdPmCDLKLoZvun3z2gUAjODxLcb8H5hN5KoCZEJZd0Zz4-Lxex8mOuUc6ufIl5iIol8rP4cZiCYMYM4v_IbwgrOBiNyw5D5vX3DLY9uABuYLxRFy8h0afPOGaVCpE6TA3--PHjvADWlY7LoncK95TvvBJb5ZUN1kKHe0xpjjBTSO3fioNkfPJqnKEoUSCxs79vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=torDMykcFBIMAOcbU2NW02ucmSYozrRtPAC-yj14pRpmclxDUWK0ic6GrAuIqN7j0dwVXA2jeDMLpPSyHZlwPPE8-Ojr9lr7KzDvwDMEUY_qhRSb58U-tBHhmMGsBrdAgcYY7HZ3HN8CuvIGBk3DdPmCDLKLoZvun3z2gUAjODxLcb8H5hN5KoCZEJZd0Zz4-Lxex8mOuUc6ufIl5iIol8rP4cZiCYMYM4v_IbwgrOBiNyw5D5vX3DLY9uABuYLxRFy8h0afPOGaVCpE6TA3--PHjvADWlY7LoncK95TvvBJb5ZUN1kKHe0xpjjBTSO3fioNkfPJqnKEoUSCxs79vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
روایت تاریخی رویانیان از هزینه مراسم وداع با اسطوره مهدی مهدوی‌کیا در‌ پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105668" target="_blank">📅 12:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82f6d2ba8.mp4?token=GiCZQJ4R5ATForN0WqzDGl7BsIvR6uL3wayDQPIR7_QbvkI8mQt9xJ1oiwCpTZme69gwGEtkMEFYETmLVYZLfmTqLNNHoIJ66hUiYsvK5tZ_YM2TTkTZ3Rxa4JpKk-8ewr0ANYoiSiZevXRB1_I37e306YjvckBCOX4Vn4CG_BOAkl1Gz3mgWTtdu8gN0Z9O-W-2gzKpYacbf7V1tHvPIgM7S7TlGm3oibF_NL3h5Qf1ecjlGFIPWGmxABl5Fs6bW6ePt1obCikq77q5RTtRamD47I8T9IV7H93WmastRs7x3xivJhjnduJfSo_UBaWQEsNsovPKd-hJqq88pQQzNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82f6d2ba8.mp4?token=GiCZQJ4R5ATForN0WqzDGl7BsIvR6uL3wayDQPIR7_QbvkI8mQt9xJ1oiwCpTZme69gwGEtkMEFYETmLVYZLfmTqLNNHoIJ66hUiYsvK5tZ_YM2TTkTZ3Rxa4JpKk-8ewr0ANYoiSiZevXRB1_I37e306YjvckBCOX4Vn4CG_BOAkl1Gz3mgWTtdu8gN0Z9O-W-2gzKpYacbf7V1tHvPIgM7S7TlGm3oibF_NL3h5Qf1ecjlGFIPWGmxABl5Fs6bW6ePt1obCikq77q5RTtRamD47I8T9IV7H93WmastRs7x3xivJhjnduJfSo_UBaWQEsNsovPKd-hJqq88pQQzNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇶🇦
شادی‌گل فوق‌العاده سمی اکرم‌عفیف در بازی دیشب السد در لیگ‌قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105667" target="_blank">📅 12:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdb42b18f.mp4?token=IYyEs_0DefON2BYtGvmbDU69lm2S7p_4r7qvymhDgpMB_f2H5wtiySnX4xQBIA28DFaN5GeAkhrcVZ1ICDmx3jrbVsofbU5DSba-s7IeYHLE9t5YwCTf_79n8iQzDTgotNeUDGqMSARU1hVIPsdDSd6XvFITQ_vN_MGH6cutb2n0QFlpxKKF1EEEu2__CI3yY0SmHkO3SExdz-8-vGL0OSjEQhuaLxh09z3MOF4FjWAlFS7UsUFj7-G-wRnyWjRnieHb4CPg80HxWVVjUcodm4fiw5dMlD0D53eaMKytPA3FwY8J5kFKfcB5gubhlsej-7-dAOdb4LdwUFMYLezW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdb42b18f.mp4?token=IYyEs_0DefON2BYtGvmbDU69lm2S7p_4r7qvymhDgpMB_f2H5wtiySnX4xQBIA28DFaN5GeAkhrcVZ1ICDmx3jrbVsofbU5DSba-s7IeYHLE9t5YwCTf_79n8iQzDTgotNeUDGqMSARU1hVIPsdDSd6XvFITQ_vN_MGH6cutb2n0QFlpxKKF1EEEu2__CI3yY0SmHkO3SExdz-8-vGL0OSjEQhuaLxh09z3MOF4FjWAlFS7UsUFj7-G-wRnyWjRnieHb4CPg80HxWVVjUcodm4fiw5dMlD0D53eaMKytPA3FwY8J5kFKfcB5gubhlsej-7-dAOdb4LdwUFMYLezW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل لیونل‌مسی برای کاسمیرو در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105666" target="_blank">📅 11:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a3702d1a.mp4?token=iUGOjCp5FpT3abBIH7iS2PwS91kFoGe-dJkegn_YVoSI6JKGHyk42s-YIXG7qUGyM3bRRiJM5xzJpgkMDFjgGpNqpH1dU9Q642su-osHEcLyJ5c8xI288ZxXXN_VZuWt0HrI6kkcHqp0LCnL7bmp6tX8vBmOM56qNxdHHjUf6p_l2bSWvsKKLsUJNOV6k-Y6Q10ruyyL8JArz2HheySBF5eoRqH-rc8WGyY8_-u4RIFCkwWNJR5m_UqfEuLWPxZxGV_ECAMr8i-I9x6ZP6nUodyOePzJWAcftx9wgjqPPHhEVwsO7jxPTXHCuEBR3_9uRfHnWHBviIkEdqpqVvjm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a3702d1a.mp4?token=iUGOjCp5FpT3abBIH7iS2PwS91kFoGe-dJkegn_YVoSI6JKGHyk42s-YIXG7qUGyM3bRRiJM5xzJpgkMDFjgGpNqpH1dU9Q642su-osHEcLyJ5c8xI288ZxXXN_VZuWt0HrI6kkcHqp0LCnL7bmp6tX8vBmOM56qNxdHHjUf6p_l2bSWvsKKLsUJNOV6k-Y6Q10ruyyL8JArz2HheySBF5eoRqH-rc8WGyY8_-u4RIFCkwWNJR5m_UqfEuLWPxZxGV_ECAMr8i-I9x6ZP6nUodyOePzJWAcftx9wgjqPPHhEVwsO7jxPTXHCuEBR3_9uRfHnWHBviIkEdqpqVvjm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😁
🇮🇷
🇮🇷
ویدیو سمی آلومینیوم اراک برای بازی امشب با استقلال در هفته‌ششم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105665" target="_blank">📅 11:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA1Y6xbvWl05rbWjcResxzpO3sbgy9odCIDzeLq-K8JUTixFvMbbRq02bmY8lN_i5yhoN621xqQpyFJXqbJI-bchvipCJ6W9gi091x0YCwEGlSSxtgwTVBO9cLYIO8FqS5AGGQcZDrXG8PvZDws4_XnKObxnkgnXkQoNLQvUC4xvOwhUF5SnIJMnRckSEOUi6ly-ELjfW8YYYf-UVOcfQKnrqoE5gAGQOMQzePP7us7hZK3TasmJjiMgWLvtyAS1qVnH2bjgRZsKI40Urh3mTeCyG8PzuJeESTdR-w2bIHeanD6h7jNmvVSBLI3M5zck-rxC3dEOzvoICVd_2B9Y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
بیانیه جنجالی باشگاه تراکتور در مورد امید عالیشاه
‼️
رفتارهای عالیشاه دیگر حاشیه نیست؛ یک رویه تکراری است
🔴
این بازیکن دقیقاً چه مصونیتی دارد؟
🔴
چند بار توهین و خطای خشن دیگر لازم است تا قانون اجرا شود؟
🔴
چرا داور مقابل چشمش توهین‌های عالیشاه را می‌دید اما جسارت اخراج او را نداشت؟
🔴
عالیشاه پس از سوت پایان هم به مدیر تراکتور هم توهین کرد
🔴
سال‌هاست در تبریز از خطوط قرمز عبور می‌کند؛ اما خبری از برخورد جدی نیست
🔴
اگر اهانت به داور مستحق اخراج نیست، پس کارت قرمز برای چه زمانی است؟
🔴
این‌بار نگاه رنگی نداشته باشید؛ قانون را اجرا کنید
🔴
اگر برخی بازیکنان فراتر از قانون باشند، دیگر حرفی از عدالت باقی نمی‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105664" target="_blank">📅 11:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105663">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d77d3348d.mp4?token=P-K9BK5RVIkWrlbwvk_NxRrU60Znj6dtSKa6-V6Yw3Kjg_Na3DMAnK2MvxwFaFI0vTtImcj2hYMBYotb3sb7dtpDf1vdoGc_kLJVmYEsv7QJwsWorKC7loIBdt5CUC4AqexUSpHjbl4lCpY3BInEE_R7EHqhqC5isOYU3X9JnG80d6l1VLm1rcG7HDakUDhPHQMbCQlRweR77ce_ph3bEOZVaFYl_u6Tr08V7L2Eh3O_jfNG0MgI8Jf6V3MheVUe8cCxUt2jzdcI69MdMK_ForsdsQ9rwop1sqDn0rJC0aEvmhhmGV-eoAcj5hnjge8WDsgjQOJf7odhOYbYxOmCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d77d3348d.mp4?token=P-K9BK5RVIkWrlbwvk_NxRrU60Znj6dtSKa6-V6Yw3Kjg_Na3DMAnK2MvxwFaFI0vTtImcj2hYMBYotb3sb7dtpDf1vdoGc_kLJVmYEsv7QJwsWorKC7loIBdt5CUC4AqexUSpHjbl4lCpY3BInEE_R7EHqhqC5isOYU3X9JnG80d6l1VLm1rcG7HDakUDhPHQMbCQlRweR77ce_ph3bEOZVaFYl_u6Tr08V7L2Eh3O_jfNG0MgI8Jf6V3MheVUe8cCxUt2jzdcI69MdMK_ForsdsQ9rwop1sqDn0rJC0aEvmhhmGV-eoAcj5hnjge8WDsgjQOJf7odhOYbYxOmCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
گل‌بخودی فوق‌العاده سمی و البته زیبا آداما ترائوره بازیکن دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105663" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105662">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goYShbd0i63-boUiLoRnZ8pZWYpYcHDr73p4VIx5gjvebq3PJoRmne7pjyRqhBuSql3FGsdDWJ4f5sfCiDg4TseVBXsf6CjiTj-MsSAdNSqWtVvGlpRhpKNj8xelriRUaf-GGyT0iqZ5jx-bF7dK8rIkb_edcaB1dy2NaUT7Fh9th0Oi7jZ96bC-N_xaslfb1zpNxv6osey-gkpgq1FCJTfu80feiWEUlaUZc_wf0Ve8O0xuXf76uBB-50Z_aqKci6kagUDjFkLtvmWyOmOgx3tqlIh7t3a3ZlWdH9Muy0EOnC1a1IW8icCR_6iVUAuQ-iVgcYzrx6eRQyc4gmE6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
فرشته کریمی، ستاره سابق تیم فوتسال ایران، به تیم فوتبال زنان پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105662" target="_blank">📅 10:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105661">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff10f908a.mp4?token=n-WLCp6RtchKvLGfwSDKMaJ60dSZVnGxBCZFxSjee2H8oRlrd3kjaAre36jPRDeJpN9kSh8uc8z-4szFLvvERh4KChAM_a5B-k4cw1P2NA_wcH_2gfedsZHZJjHWVSI6LDKg8sISFf91WnwiTD1DN_QPzUiScLYw6leY_lCF2gvrIhLjCqwnsOTl4mCoFN05v79ixWrqynU7Dnwo2YDTSJLNwKi4qwQ6cgpZyTDOQjExuXriNWJMs27JZmnKHDDlp2EDONTkStelR1VeFMaXlpqqO36rMIGzPGy1pzNjNlPGEKYhN68SIBMrQw1ozQH8X09ljm4a8cFg2mi8WhFbHYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff10f908a.mp4?token=n-WLCp6RtchKvLGfwSDKMaJ60dSZVnGxBCZFxSjee2H8oRlrd3kjaAre36jPRDeJpN9kSh8uc8z-4szFLvvERh4KChAM_a5B-k4cw1P2NA_wcH_2gfedsZHZJjHWVSI6LDKg8sISFf91WnwiTD1DN_QPzUiScLYw6leY_lCF2gvrIhLjCqwnsOTl4mCoFN05v79ixWrqynU7Dnwo2YDTSJLNwKi4qwQ6cgpZyTDOQjExuXriNWJMs27JZmnKHDDlp2EDONTkStelR1VeFMaXlpqqO36rMIGzPGy1pzNjNlPGEKYhN68SIBMrQw1ozQH8X09ljm4a8cFg2mi8WhFbHYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی گلر‌ها وسط بازی حواس‌پرت میشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105661" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105660">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cec5d5803.mp4?token=FeZzGvU8i47siTJhkvTRRgroyNwNU5Kb3n9sbSai_Zs9MiPYQH1LgmiLjO3hUKtBMGVsrD-XetEYNQ65kFCyrs-RtNkh6Zyhzozf7WjfSwrE8puP4S2COptvSOewGzhtCGzWP7RSF5ZysRcPQwmDQ4CqETo71qXtXtJsRVVhLvGWWcG-s5XY7pNA2t1znkAvN3S3lmO7H05xpg2sgHhh4atfv7zPvq6gx04Q33T4Kd-usp8e6Z4d2FH5DP54L-JXYKjVEJSDEz9lxvvmf7WX8H-kEiziYb6MseRzTNyNBU_UbSV7Z0yIhOrJ7rqbB7AZbOBRYURV8nBmzE07FA9hhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cec5d5803.mp4?token=FeZzGvU8i47siTJhkvTRRgroyNwNU5Kb3n9sbSai_Zs9MiPYQH1LgmiLjO3hUKtBMGVsrD-XetEYNQ65kFCyrs-RtNkh6Zyhzozf7WjfSwrE8puP4S2COptvSOewGzhtCGzWP7RSF5ZysRcPQwmDQ4CqETo71qXtXtJsRVVhLvGWWcG-s5XY7pNA2t1znkAvN3S3lmO7H05xpg2sgHhh4atfv7zPvq6gx04Q33T4Kd-usp8e6Z4d2FH5DP54L-JXYKjVEJSDEz9lxvvmf7WX8H-kEiziYb6MseRzTNyNBU_UbSV7Z0yIhOrJ7rqbB7AZbOBRYURV8nBmzE07FA9hhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رفقای باسکی، رقبای لندنی⁣؛ دیدار غیردوستانه‌ی آرسنال - چلسی، امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105660" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjgriy3Pc_lpynklE6uTbCEca6UuDs4sFk6V873WeqT7sDQEjM3ue3ftbH_3bo6Es_jhw269nFHXvrVY1Po2bqUgJ_-EeE06ZHTEXdW2JyYv8a1ncV-6FFLkEFkGSAHovOZF2x-yccEdIa9hA-t0teQ_iMHKkCAQQ6K1CLrZU8ah0j0vqTAYiqCueZVN74hqsaOfYwZwcu1gyUy62oGrCyue6cQdMRKldE89tsZQr5ly77wb-fi0hu5qdEmiv3iNqNcQAhI69DlVBDt1JfcAkUbiBg5NaxfyjVMDUgxRZ-yYzxzSRMf2bEDPp_RVoAMZbFVcwTXG3f1bbChxEbX8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚑
تصویر دلخراش؛ مصدومیت فوق‌العاده شدید ایوب‌الکعبی بازیکن المپیاکوس یونان در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105659" target="_blank">📅 09:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3abb5b4d2.mp4?token=r7SMBz7XtvmRMG--2xgqXXPWJsJ0Bj1dXOQJ3DSNFVKrEOlGP9WUQzJHBBZD2vRXQGJilqcVB014fesaAUoCeutNIbRtfMWHjiXL0Rf5PkcF2Xd9I6isJ6BWPYFUD3YfVzPAlstRAfZwdeXDmF6-iySV9uyVwjLAmIMq_GKDUN89RtN1mJQWBhwiqrrw1IBef-aI5ffBch7xEzuKQTz4KJOcoYhrd7Zhafk-_xf-m6e8f8QI6YvruFHAG4OJBfMhYsDjnfCTA4bvMsIB2ysF1r_PINkNVBu7JZhFqbpCfRgZuG7xePLi-2CwlA64E8mU1KVWh9pH58Gs1-cKVJwNDyQP8SK4zc-KgwkzBUVQZzV_1id3sgWZQ3vda3hsOigQVTrE6ESObQPOzBcR2Mn-gWBCmbN6Cj3X9Sojc9B5gDCPj1_tvGRnVfMG3fu3jt-FQiTcKdUv8M21aBfU2twSfc4xJ95XaclzAuP3ddObWvQuwPrAFDpBV1ELjWuTiVl0yMEnD1W_rM6QBDlYF8pBA916ay7hGe0LrD_cGWlyrLJP8OJPMKgdFGJ9OCz4KLQIS2_04WFOlRBNQwFnEbVd2mwTNB4f_gOoyt3iGxDbiQpwdQN-1CmaD7MH_hWaG00i4176auui7So0nUJrGd9aGfgjcxmQOgjbnI9GKtS7q9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3abb5b4d2.mp4?token=r7SMBz7XtvmRMG--2xgqXXPWJsJ0Bj1dXOQJ3DSNFVKrEOlGP9WUQzJHBBZD2vRXQGJilqcVB014fesaAUoCeutNIbRtfMWHjiXL0Rf5PkcF2Xd9I6isJ6BWPYFUD3YfVzPAlstRAfZwdeXDmF6-iySV9uyVwjLAmIMq_GKDUN89RtN1mJQWBhwiqrrw1IBef-aI5ffBch7xEzuKQTz4KJOcoYhrd7Zhafk-_xf-m6e8f8QI6YvruFHAG4OJBfMhYsDjnfCTA4bvMsIB2ysF1r_PINkNVBu7JZhFqbpCfRgZuG7xePLi-2CwlA64E8mU1KVWh9pH58Gs1-cKVJwNDyQP8SK4zc-KgwkzBUVQZzV_1id3sgWZQ3vda3hsOigQVTrE6ESObQPOzBcR2Mn-gWBCmbN6Cj3X9Sojc9B5gDCPj1_tvGRnVfMG3fu3jt-FQiTcKdUv8M21aBfU2twSfc4xJ95XaclzAuP3ddObWvQuwPrAFDpBV1ELjWuTiVl0yMEnD1W_rM6QBDlYF8pBA916ay7hGe0LrD_cGWlyrLJP8OJPMKgdFGJ9OCz4KLQIS2_04WFOlRBNQwFnEbVd2mwTNB4f_gOoyt3iGxDbiQpwdQN-1CmaD7MH_hWaG00i4176auui7So0nUJrGd9aGfgjcxmQOgjbnI9GKtS7q9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی رحمتی پس از سومین شکست
:
🔴
برای گرفتن سه امتیاز تنها تیم بستن، بازیکن داشتن و تمرین کردن کافی نیست و باید کارهای دیگری هم انجام بدهید که از توان و اختیار من خارج است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105658" target="_blank">📅 09:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/Futball180TV/105657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🚫
خداداد عزیزی:
اره عالیشاه بهم فحش داد منم جوابش با فحش دادم
با شجاعت میگم بله من فحش دادم و کار خوبی کردم
قبل بازی رفتم لیدر هارو جمع کردم به بازیکن های حریف فحش ندن اما کار اشتباهی کردم
باید میگفتم به بازیکنا هرچی دلشون میخواد بگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105657" target="_blank">📅 08:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41325b7826.mp4?token=urArk6yVAqzUbw9TanR-fUjQQcUs_NejU2G2TwTL4I0kazmituAYMovUu6UNr6yv-iFb98L8wU6aRL_nScWa6fJjxDsTCLIkbwLcPgAs8TOL3vvq30nbsDwbfqX9khTtsKVHI72psVrLqlzzS8oyBZJt6jWbhCBHTMpDG2rPagU8FlhKvaa_BoKuqDTCEjEUxwwfwBTMPXl06OBNAh-ssfrCBLvn7v2UpPxu9YFDZBkaTqJzM8SeiwovI7A3jY9glO8hJWIFPppfa9cW1aa72x5gh71SbrP6HmU0X7wtpr0Tsw-asyf-H9QiQhjbEcWpzyJDp7BHkZcg0fCC10bt5wajHqYWs-azONy2o3Epuf1IL-qbSYEC990ugTIUSRI11yoyz0vejj0zdpRET7QON_1nMBjdFxmrP1FNObGqVY6c3OOimDDRUN5DahOmBlGFBxpMkAf75vFoX7VaUtK6Zx2-jzZvtjDKxBwSYcV5RbJcGGz9k8owBcfeBFNG9bG29Mc634yLCCrMpisu6fYHyWfJSZLto3h-j6ElkLjMOig961GoJWw2Fohmco1IjM_uFQL_8KBvPgSCG-KOACJPeEfaLudfxgSu5STKNcwT6EhA8Fw2xdO9UAwHwzgfJSCv3fUD8aHfI2kW--t18oYH30AjMTNd84GPKh0GQfmi8ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41325b7826.mp4?token=urArk6yVAqzUbw9TanR-fUjQQcUs_NejU2G2TwTL4I0kazmituAYMovUu6UNr6yv-iFb98L8wU6aRL_nScWa6fJjxDsTCLIkbwLcPgAs8TOL3vvq30nbsDwbfqX9khTtsKVHI72psVrLqlzzS8oyBZJt6jWbhCBHTMpDG2rPagU8FlhKvaa_BoKuqDTCEjEUxwwfwBTMPXl06OBNAh-ssfrCBLvn7v2UpPxu9YFDZBkaTqJzM8SeiwovI7A3jY9glO8hJWIFPppfa9cW1aa72x5gh71SbrP6HmU0X7wtpr0Tsw-asyf-H9QiQhjbEcWpzyJDp7BHkZcg0fCC10bt5wajHqYWs-azONy2o3Epuf1IL-qbSYEC990ugTIUSRI11yoyz0vejj0zdpRET7QON_1nMBjdFxmrP1FNObGqVY6c3OOimDDRUN5DahOmBlGFBxpMkAf75vFoX7VaUtK6Zx2-jzZvtjDKxBwSYcV5RbJcGGz9k8owBcfeBFNG9bG29Mc634yLCCrMpisu6fYHyWfJSZLto3h-j6ElkLjMOig961GoJWw2Fohmco1IjM_uFQL_8KBvPgSCG-KOACJPeEfaLudfxgSu5STKNcwT6EhA8Fw2xdO9UAwHwzgfJSCv3fUD8aHfI2kW--t18oYH30AjMTNd84GPKh0GQfmi8ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⛔️
‼️
خداداد-عالیشاه؛ جدیدترین دیس‌ و دیس‌بک ایران؛ رجزخوانی بر سر کارنامه و سابقه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105656" target="_blank">📅 08:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105655" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105655" target="_blank">📅 01:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aetgjCKioELIT5HUX-_tVa0nJe78bJdErJL70U2acV3-F03GZttP9xFAqIW-WL4kIodLwBwttB0vSHsiZudJJx0BwqTLS2hTTl_-ZfogkNSj7XlTcg4ZD35DvfEeVFeIxF-SOv2niA2TN3kNYYT1N_lfoLZli5MBM3453bu5FxGFp1BnggXVnTKrLkgvOHkLP5QB79mRtaULwIK1fqU7HIk0olU_Ce-tyJv4ssyIHM-3LpJ7ziA66cuRsI6wxNKLgr3Ch-NgvRvyqd4DKP_t0Vmm5wnXUWzBrW0oTKu12irM7gMz-2rEiQ_dJdr03m323KICSpBp058iyaAquU39DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105654" target="_blank">📅 01:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105653" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚫
اوه‌اوه لحظه‌ای که خداداد عزیزی به داور بازی میگه کصکش
😕
😕
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105652" target="_blank">📅 01:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
🇮🇷
واکنش محمدرضا تقیون، مدیر روابط‌عمومی هیأت فوتبال تبریز، به ادعای گل‌گهری‌ها: فحاشی صورت نگرفت، مدرک دارید رو کنید
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105651" target="_blank">📅 00:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105649">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/105649" target="_blank">📅 00:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArWr--WdKHkE2sD2RVrrWjDYgR-FTt_YQRVRno6wMDDEJuzHuuT3uOUAJFkuu5L4PX0DOo1FBYQDCBq99urZPD3cODju5hkA2EVXXJfQMNj-UVhPu2RAu3TOfrDHI7ttLPS4zSZEx5zU5gSm8CtbeRTKu4GCU__Y5WaN74YEsicHkzphYcqVL_0m-0g0tE2zo-xTOO04mbgclrMX_byKXzXIONcdrooB3H_rDWB82FmUBB8EY6iRcw5WtQX-izATPMCBAE7Y53EWZnrUoViTk21gsGitv4wQOlP9BP_Fi3PXNhF54cRmTf0KopYSkHEXdr669Yq__Z5o1dofU-9GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
💥
اوبامیانگ در این فصل از لالیگا:
📊
👀
4 بازی
؛
4 گل و 2 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105648" target="_blank">📅 00:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0972e47983.mp4?token=ut6ZAj-47c5LHUZ4fw9RLIpeVmwRT9HoNtehvwNh_FQb5buO0BG5n3y3qks_Mzp7TVpMcQbuuCzgXKD6-lAp_BYDDxcXs1xdUoptmISLIaGuFMF0-0htOt2g83Fj0l_SVWYjg9T5SYxYdFA0WOcow-0EemCXOSIGThFhsyi7kKN2PjKt1eEoZbO1f35aKcvMzxy9Ec6zRuFWJVE9N7N6qgi-zJJXZ8FVq5bCkz0t2lQjfEZMmzOJaKlkD6nGzj-GK9N7uhYNaRkCV125gJDLmm8ajcealObaswAf0S-Dt6Z4jhGwtoc16hkgGedJCcIjVPGuV3j92wdulkytT1ZQX6V9I5Ykg4p6FLLQcUPVeGYqFgEr_kL7qSQwf9JUe31W5m5IQi27qT3ITM48VlaK9bGdhn_75lECaPoMBMnkrzu2jgkLskTi2etEnbtQJz9btR3hEPOE0qf_71pPnw9MReghDTtgVu5U0xb_bes83DHe-24WdXdCJ48dLgL6t4h4MFys834tP1DNf1ID2LPQS5Ukw6KB0ikL7pXt97eie_4JsVgQLt8rbQ1DmaXZL7omEC2uH5XE4huY7GhQ4jv1A9PRwM232Z3tzEAhLy8DnVMJ0s0qRn2WzubS1eBqeV0UQV8NBUwInruxQI1TgHqjY-MDlkXZdZq1VUFi-6Bpghg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0972e47983.mp4?token=ut6ZAj-47c5LHUZ4fw9RLIpeVmwRT9HoNtehvwNh_FQb5buO0BG5n3y3qks_Mzp7TVpMcQbuuCzgXKD6-lAp_BYDDxcXs1xdUoptmISLIaGuFMF0-0htOt2g83Fj0l_SVWYjg9T5SYxYdFA0WOcow-0EemCXOSIGThFhsyi7kKN2PjKt1eEoZbO1f35aKcvMzxy9Ec6zRuFWJVE9N7N6qgi-zJJXZ8FVq5bCkz0t2lQjfEZMmzOJaKlkD6nGzj-GK9N7uhYNaRkCV125gJDLmm8ajcealObaswAf0S-Dt6Z4jhGwtoc16hkgGedJCcIjVPGuV3j92wdulkytT1ZQX6V9I5Ykg4p6FLLQcUPVeGYqFgEr_kL7qSQwf9JUe31W5m5IQi27qT3ITM48VlaK9bGdhn_75lECaPoMBMnkrzu2jgkLskTi2etEnbtQJz9btR3hEPOE0qf_71pPnw9MReghDTtgVu5U0xb_bes83DHe-24WdXdCJ48dLgL6t4h4MFys834tP1DNf1ID2LPQS5Ukw6KB0ikL7pXt97eie_4JsVgQLt8rbQ1DmaXZL7omEC2uH5XE4huY7GhQ4jv1A9PRwM232Z3tzEAhLy8DnVMJ0s0qRn2WzubS1eBqeV0UQV8NBUwInruxQI1TgHqjY-MDlkXZdZq1VUFi-6Bpghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
🇮🇹
کامبک جنون‌آمیز رم مقابل آتالانتا
🇮🇹
آاس‌رم
😀
-
😃
آتالانتا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105647" target="_blank">📅 00:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو از پشت چسبیده به دفاع حریف تا تاکتیکی که مربیشون داده رو ببینه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105646" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه گل گهر با انتشار‌ این ویدیو نوشت: دو صحنه مشابه با دو برخورد متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105645" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با انتشار این ویدیو نوشت:
خطای شدید امید عالیشاه روی پای امیرحسین حسین‌زاده در شرایطی رخ داد که بازیکن گل‌گهر پیش از این یک کارت زرد دریافت کرده بود و با توجه به شدت خطا، می‌بایست با دریافت کارت زرد دوم از زمین مسابقه اخراج می‌شد؛ اما متأسفانه داور از این صحنه نیز به‌سادگی عبور کرد.
در ادامه، خداداد عزیزی، مدیر تیم تراکتور، که نسبت به این تصمیم داوری معترض بود، با تصمیم داور از کنار زمین اخراج شد؛ اتفاقی که در نوع خود قابل تأمل است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105644" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
مهار شوت سنگین رونالدو توسط رایکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105643" target="_blank">📅 22:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🐐
به پرواز درآمدن کریستیانو رونالدو برای انجام حرکت آکروباتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105642" target="_blank">📅 22:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حمله شدید امید عالیشاه به خداداد عزیزی: خدا را شکر سابقه ملی ندارم. من نون بازومو می‌خورم
🔵
بزرگتر از شما هم نمی‌تونه اونجوری صحبت کنه. داور سر تیم را برید، گل تراکتور قطعا خطا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105641" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fes7krtB-XoqFR7HVJaeSGqYmgqumnHDDLqfrsGDcBFVXApxOQlxtmqjk9Emg09VyJCrfr-aly4_tqvm7ntpLA0wQ9P787grF3OhFTRt0a9qKpuEwyGB6zyvyufmA6WnVpLfCXL_jsEkcByjCiB-xPS60pJRWEzgQNFBq09_6hGqmrjlX5TE16TTKtLN4KvUinjr_yPY5-pxtjwxltVzAkLUUsa1yh8eBwh9BA4-tARr846TKFxlkgmTEmPC0gn3C-C0T_4Nk8ZUbO5G89IjpJ0GlNyQIHm8aTGw9A3V6M7aBMeASEriCmgXPYk2BmnUCDuR3Tl3ifDsUJxDY5T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
محمد عمری بازیکن پرسپولیس بدلیل کشیدگی رباط زانو حداقل یکماه غایب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105640" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت‌کریمی، مدیر عامل تراکتور: از آقای تاج درخواست داریم ستادی که علیه داوری بازی‌های تراکتور تشکیل شده است را پیگیری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105639" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWFOPnxA2EC4r2PupsxxqySXxLLJsWYC-2kY0YEKxzih3c4yeAocwKsOFCAbmSjd04vGLZBA_MXRx-EN5Lz_zUVLae3NpNo5DXWKaURIz27mTeBBHqitfWzUIsGiCVPCDdL-Y38vnE_nD2zt98v8VF8fkXnbIwil7Dpm8YOY-b16AU8-osoGfYgeToyav82f8IE1OzYBtg9QIkuPjaOs0rWVd90AUDVGNsyg1ZJnKLM3udcCc75ZDoyYBtjm3JjrByuQ_u_yJ95NWswZQMBAEhgZ-OCyx5fSX0ZMlSVyT_trqmtSWK9LhIFvk3l00uRK5r2iWTLU942zUMHsmMyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105638" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105637" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ffHm8eDwE6KH3blBsKX6sXDpea1fdp3EaTVLyxvXWso2n3O26mZC6LzpxwJRuxhsiYAfPC_fpOYC4rgL_pfa8QPz6RNu4D3oUQeB8XfrEm7aqhUDnGJy5DoJNaKXtJES2BVu89nK6oEFusCOKTCB9kJA8yOzgmh1AHqOy6ahUn5mSZubyywKJaXLfT3tp2ryFqrYOkgtJkh8MYi7m_WEfuj5dgNHe3AiR30BwvWxLshg8qljsG4gCybD0s2km1LgIKqpJyJOKIomYz_O9rJ6ToTaEOmQwmlfNyCF4deewDv7rtVvE1Nnqx5fNCkRaf8PkYVe9_OZdjlicGn_vSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105636" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
گل‌تساوی اینتر به ناپولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105635" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105634" target="_blank">📅 21:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
صحبت‌های جنجالی علیه عالیشاه؛
خداداد عزیزی: او اصلا در حد من نیست
🔴
بیاید بگوید کجا بازی کرده است؟!
🔴
اگر یک بازی ملی داشت بیاد صحبت کنیم
🔴
این همه مربی آمدند رفتند هیچکس تو را نخواست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105633" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول اینتر به میلان توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105632" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌دوم ناپولی به اینتر توسط هویلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105631" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول ناپولی به اینتر توسط متئو پولیتانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105630" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbX4gQce3Ygf9gSnZkOcQfrmQF3Pb_n9EywhZYDfcPcM96zf2-TFdVFYHvAPHc4HlLacal-kOhNEnILR5sWi3UEKFXaodHCmoZyYxII54kY_DpI2MZsjVZGlJZlv3_gsDOci_VtiqSZSwciKhjfjpApCosi54IBxH6O9Hyax4YgDAouY3tYf3JEpKR__eXjnCBejkOjX4zi05XHDvRCH8r8qFCJaN-szMfz2EjSCpBPjCLWH8PZXxKU6GoRju9-Q3EXXQ-LUhDctzR6ddclhGe8vNwko_EVWgkJBPU7n8bhdOj75yVQCGdXN-S-EPxN77InFoJkMILdI8rnWFvg-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105629" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
🇮🇷
سهراب
بختیاری‌زاده با کنایه به صالح حردانی: کاپیتان دوم ما باید یادش باشد که زمانی ناصر حجازی، پورحیدری، شاهین بیانی و زرینچه کاپیتان استقلال بوده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105628" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105627" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105626" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEfWKDZtZfw3ZlDM9zwIAOr51YNLDYvyD1b4WBvCoD_m4pA5_R_05XNJ4RcLh6pQoRIbvraOifzWZjw6oRtH8zhCJBwchMg8EHEWcXLEQBD76dD8RCUxEMBpRjQyyG8_VijR7SfqAfwilI4CNQWCDmurc5R4E6_pABWL9Fjmy7cLmcjuU3Kracuf0Qj89yw1hQukWk5aBedpXso_9WtMVyOLRT3fz0S3t8xiRYyD0SpTje-hEgxbjwwUYm5spcVYyWd-3BhpIUA3OyhVky1o2Q965mIzuO9FZ70r7pvXt7KS5t9ezkp5gSVnGqV1PJPSDkL63oQpCvM5v6a1UzrrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
ترکیب النصر مقابل الاتحاد با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105625" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoW86EBi1OjI2oq8P3Gi5aHU7zaBiCeNhn5-2Ks0A79JVidnz0O-dFEhLihHg2mv09-trur3FG6eGIKx_jjnLI5b-g-lfKhDdiY3X8yQ1XuSCj-ciZVKWwkPGzZSGj3oeWpD4WKyWgllDLAm2ahI-aXnBP-RRoNDQiHdg4msgDRlPc5rwFyfO_fTwqUx0G0IcII4wJKotv8EGMwCkMhd3qMFRDE9AUw7DeFCtS3EWX8eMJSVJOAOONWYoHB_tYBwry-S1h9f1QTTTFTVf438G2DSplQNf75_UiAm-djNaCJaez4UBO129HkKqvvLnbQvTmTh8zVABB4QVqrGd1l_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم لیگ‌برتر؛ پنجمین برد نکونام اینبار مقابل همبازی سابقش رحمتی؛ تراکتور با تک‌گل جنجالی امیرحسین حسین‌زاده در اوج باقی‌ماند!
🇮🇷
تراکتور
😃
-
😏
گل‌گهر سیرجان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105624" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYet1nlpnfQDAPZHM5ciMCFs0crLSqnpSS31lozMjIrw9O7Bl5UL5ekTiRK7ZGLz5U7soquM8xR4US5hyvJiBavZdUj5BAfBLwQbnBA0k8j_Tr8pAciRlgFCTarxtAVaf4Jy5oqrwFfU6c9MUJWo0ir22b3WqY7z-Y3STRQeMnouADuaz86dK7A8WkIEbf8zO2cwUdALPWmkOrEp18p9aq92qLplnybP7ECNEQ0hu3BEXb4DQwdeIKlJYvyrltDxzJUG9wM71_m9xFgQ_teSLfFHX8JZvPGHuE3XLQNkQM_sW4S515O8KE9CnZm7R6cuNV6lupPyf955iXit9Z44ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105623" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgECjQm_s5crvmw2WJwTITd4cuCv0DzKrXRxihGYbr81zI8Nu5P6V-hrwlzF9cHHA0c7lKAYeey94zBWkpBX6OAMDWyeSeTTZ9TymArD6deCB_7Xj-5VXjPNZQE2YhwBK_CflOfS-D5xtaZgWPTw3yt0ce2xrA_G8NMWNIiIyWBJzmSrNNm50rAMh6eelq5gPNa6dVKaKMcuAfdG4ZMSD7IbZzGFCgnTlb6-qmYQNw1d-2_ce2RUsIRy_f7t-llo59bJzVa3HeKH4smqe6jGEaHeR7eCiUvxVTofmUnNxnJCJTH02tZWxchB71hM9iVGRv1yowPcvjYm-DrH8GxOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKZfJVbEcBtnjtDoWQhlbPv0Gn1KjDXkt1zFZ8aHBixia9fmf1VZYfVHAD4iH0f1DxWTM7Yjbk0DBXBvlSVq0qtIRTRWwPQeAQHTl1kYhqztRi9i1BfCyxT9wJmskz6HDbw8LoED4RDUKDVPwhkeyoLLeBg4h9AVv4EsiOp21MpBkGAb8lqqDX3dUiW9fkAmIQUsCiJakJ_9XKfROcWenU3-ifrnbYUtlwbvPz9VubK8FcpD3XrYJouO3aTiIH5soMTksnAZfkfgxhPk_nM37aRvO9KRoZRDcZBxAWCS5xXa5Bd8u60_2HC15yS2pbLxqa0D9dW97L-9vksgHZADnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105620" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراضات شدید خداداد عزیزی به داور بازی؛ واقعا بعضی وقتا کسخل میشه الکی کارت میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105619" target="_blank">📅 19:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🟥
خبر کوتاه بود و تکراری؛ خداداد عزیزی در بازی امشب تراکتور هم کارت قرمز گرفت و اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105618" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1cbGwt-UjBKiD4qFyO7uTYRgIyfHoPkfbYZxCOlR3A8GA62iJJQpVG4GXdtLK1nNiV3LrJbh5wvfKF4x3Ro5Vfcy_p17wmtdBV-U3L2jiCAbaxdf_vyv1HN49_ZNhcY7IF-qwK0QpwQu5pBtQA-VDO1MyX-JnFawFk8qh0UoL3t9bE0KHdnTBz_HkRfTMZqlLy4K7QVoNKOBSUSPzId7nntTklkkT_TDWQWVaTIo7O7JJqWvvy3lo7MxMgMswEkaN26q0HU5i6spPV2QQJ-oif-0J2eHIH_FIdp9i9lNh1hcDlD-OGAHS_Rxb5M1k4dr3eDyprLvubjZbOYAYuVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاتنهام برای سومین هفته متوالی در لیگ برتر، بدون پیروزی و بدون گل باقی ماند!
😵‍💫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 3-0 مقابل برنتفورد.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 2-0 مقابل نیوکاسل.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تساوی 0-0 مقابل ناتینگهام.
💸
باشگاه بیش از 300 میلیون پوند هزینه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105617" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🇮🇷
🎙
صالح‌حردانی: مشکل خاصی میان من و آقا سهراب وجود نداره و‌ بزودی شرایط به روال قبل برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105616" target="_blank">📅 19:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105615" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPIF6Exub6AQWFQbZn-46uajuVf24sdEheuei33ayHMSM5-4kwB0NisUBEU-WeeDpQxFnCdtPsAvNC7lodUScsSBhr5WXoXGlrrXOksijk4Gs3_pL87ye1rdEmSnTH7SFA1RjOwvUf3l07p5XzZ-IwyswGqsl3BM1mmg8sr0TZvw82nLrzsPM2Y8tzlENxtfajvoOiw8I1i6-aSUN6UCXYuBMy6K9uk7NbDN2y2os33f5byRhrpLz5Euq8aUyyGK6Oi1friwqfGbX8jfb13SJpcyiZcVROxXjR1Y_ctnzLQeO-bt_Aoz_z23yaMv3sLuFk7qZahVLh-EBI6OPndSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105614" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=HflA_sHvZHYi7yWqBmYVPYTiQIRxqSgSq98CNnlWTTiVhGP3NHPFZvCLRKuYViR_uNLgjqZkuSSKw6jxb_ZjMaeyU6X-Fo-j8Esj-OQnp4Er31lmt1YdjCmmOZ7qXe_20EPpEdJxrep3TLhisrppGmJ3osewOj7gKVdI2uRT_ysF0kANf65AQVl6NuQ0qog2RKb_aKwqYYUSkHhSuJidafdRksI-fA2Q_mzaadZq8LshVAy9GQiTMgBImSPuFwaHOEGN0JzeYXKw1SgUxDsQt6g8-rcPlPnQHpJCUasVpuqT_njSwKRwH0GUSACBU6P2nrUSfa57_uOb-XeadoSDUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=HflA_sHvZHYi7yWqBmYVPYTiQIRxqSgSq98CNnlWTTiVhGP3NHPFZvCLRKuYViR_uNLgjqZkuSSKw6jxb_ZjMaeyU6X-Fo-j8Esj-OQnp4Er31lmt1YdjCmmOZ7qXe_20EPpEdJxrep3TLhisrppGmJ3osewOj7gKVdI2uRT_ysF0kANf65AQVl6NuQ0qog2RKb_aKwqYYUSkHhSuJidafdRksI-fA2Q_mzaadZq8LshVAy9GQiTMgBImSPuFwaHOEGN0JzeYXKw1SgUxDsQt6g8-rcPlPnQHpJCUasVpuqT_njSwKRwH0GUSACBU6P2nrUSfa57_uOb-XeadoSDUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
عصبانیت فوق‌العاده شدید مهدی‌رحمتی از داوری بازی تیمش مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105613" target="_blank">📅 19:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpK6egRw2EMS6D38L0H2Vsf6ZCAVMXyoNaJiU_h5yak8ctK2jSdHsvRIagEGc2u8RiuDwc0WFCjwz2t1x_l6tBoh-oohKMW1wQzmOogJBWbC-9Tj8EpwE4FJnpcdomBhCRCCyBEiF3SGpYEt9isnYak8seqjbjrYUd2CO9zgG8xT9B14a8FQ2b-Ei5LMC0MSgoe5h5UKljG0owsuYGdcPyfLM2A35KSIwcn-VvbdyyzgtD3vjV8x4w51OT20WduGGDcae3yGiQ2wgVegu1fCgfgMywHk4er5RNtKFCmaKwUhIe59Codh5YpGI-c1i_wUVCc3GhF46vT7wMpIIRKGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌مونیخ مقابل شالکه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105612" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=JcwHJbBeZ1vUDu4YQA4aweU8SkA5SuaiXWIZFimhmFzdzJENQn70I622Ji5zaUl12PW5haX9AmBISMq8zeA5vmM8dnj_dun_Xck3VULXAa9g8y7ne7sXOJ63VrcckJ30DonC9BgRvIdxyOUYxZlWaRe4WgsgUCJI0-bAa4W4gqRSeMtDspi62X51yYP_2sJ8FuH6_d3BimIU9gpHWpNjN23pwN33YE0agA7J6sPWXlwBo6uju0ysQWgaGapO6zZCRXeTcxUhHq1kkpBf11WFdmvRnpCCDz2Z2EZZ5EvOWgTN4hoEaMDNJmBmoBUUupU-ivhmnxkSgD7Mx-dcNglkCyKgChIffOHifV47D5rmuxAnY9hinXVQmFHx9VmKqRbu7MXJ5PseY3nusZAYOZ1GhaQU8HTfSbY1Z7GMFqKaLyhjiDRUNkyzCN7m0dmo_X02dXwym9kZ8GH8UXHZjQBl7-gUTJ04CG5Ht30KdLMg7owZUKJW7N1uODRbbXoeRKqVpLSdqqyVtnvwzho2PTI4lFXkotY9SZq1yUeX5XCxEsyyoe5X9KOm0IVLQSlp_CUd_LNd47U8DFyPtgllUZGHFZ0VYS9wF325tbhrPChHKNpfeYS8vIM2o2VEBoXj5YobJ1bS63Ndw_8LT2eVdchk2ANT0z5T95XnNnHarcMDhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=JcwHJbBeZ1vUDu4YQA4aweU8SkA5SuaiXWIZFimhmFzdzJENQn70I622Ji5zaUl12PW5haX9AmBISMq8zeA5vmM8dnj_dun_Xck3VULXAa9g8y7ne7sXOJ63VrcckJ30DonC9BgRvIdxyOUYxZlWaRe4WgsgUCJI0-bAa4W4gqRSeMtDspi62X51yYP_2sJ8FuH6_d3BimIU9gpHWpNjN23pwN33YE0agA7J6sPWXlwBo6uju0ysQWgaGapO6zZCRXeTcxUhHq1kkpBf11WFdmvRnpCCDz2Z2EZZ5EvOWgTN4hoEaMDNJmBmoBUUupU-ivhmnxkSgD7Mx-dcNglkCyKgChIffOHifV47D5rmuxAnY9hinXVQmFHx9VmKqRbu7MXJ5PseY3nusZAYOZ1GhaQU8HTfSbY1Z7GMFqKaLyhjiDRUNkyzCN7m0dmo_X02dXwym9kZ8GH8UXHZjQBl7-gUTJ04CG5Ht30KdLMg7owZUKJW7N1uODRbbXoeRKqVpLSdqqyVtnvwzho2PTI4lFXkotY9SZq1yUeX5XCxEsyyoe5X9KOm0IVLQSlp_CUd_LNd47U8DFyPtgllUZGHFZ0VYS9wF325tbhrPChHKNpfeYS8vIM2o2VEBoXj5YobJ1bS63Ndw_8LT2eVdchk2ANT0z5T95XnNnHarcMDhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بیلبائو به اتلتیکومادرید توسط ناوارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105611" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=rRPZqbJXMEbb7pp_bZqa4tHfMmBPCKCEmcS8-fvJVBBEb6bhjujZjb7sgdiVAis1TG78FHOo92BRHa0nnrZ71Rkawb3ZXHsnFYJeRk-c-RWRxQAlL7afMW8MHuCycctC9QYDj3fQ2RXq7oUt6tpDEqJb6BWuRx1Hoqc9W-MYHzBiJNHnGzpAHi2sSJF85_QuvydJiVCdxYsiUs0mCkDayujUBXSfedJGQqJi46Q2wTmN-iYP3loVHhfCLRxc6gIkVmfxWGCQJnA4U3diVJ1KyHT3dTfhdRT91evWOy18kO8atYbicsJ4npi2K9v53MWFGtLi6e3zAsPOAfLzUxJ7_XWMudYmP9AtA-XHSCw6ow66xqK-6crW2oWL99jwwN7tsd5BFGbhREinL540UySFJjfw2v5WyZuumJWeOQMwukD8ePl_WZhU0_NhVPkU5q7FSEyqIxZWKMOEb31Di4Hg7ko_i6Bwp_pL50nhTHL0WNMjcMwnaejTe7PkbV2_gx1aMA53UhPlYK7YKr7EigaRRhPNP27sOsA_BGdahzt_PxHu1_SereQa3irQjTiqJjvxoro_ld0Z--058u2AD3RwHQ5ibiwy5-_0p-OB0ua4eDlnDTrc5wYRs69AdR4pFsvB9h0iGuCpHEQcWEMaw7scliTqJOHT6fTnr_c8nieYZBs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=rRPZqbJXMEbb7pp_bZqa4tHfMmBPCKCEmcS8-fvJVBBEb6bhjujZjb7sgdiVAis1TG78FHOo92BRHa0nnrZ71Rkawb3ZXHsnFYJeRk-c-RWRxQAlL7afMW8MHuCycctC9QYDj3fQ2RXq7oUt6tpDEqJb6BWuRx1Hoqc9W-MYHzBiJNHnGzpAHi2sSJF85_QuvydJiVCdxYsiUs0mCkDayujUBXSfedJGQqJi46Q2wTmN-iYP3loVHhfCLRxc6gIkVmfxWGCQJnA4U3diVJ1KyHT3dTfhdRT91evWOy18kO8atYbicsJ4npi2K9v53MWFGtLi6e3zAsPOAfLzUxJ7_XWMudYmP9AtA-XHSCw6ow66xqK-6crW2oWL99jwwN7tsd5BFGbhREinL540UySFJjfw2v5WyZuumJWeOQMwukD8ePl_WZhU0_NhVPkU5q7FSEyqIxZWKMOEb31Di4Hg7ko_i6Bwp_pL50nhTHL0WNMjcMwnaejTe7PkbV2_gx1aMA53UhPlYK7YKr7EigaRRhPNP27sOsA_BGdahzt_PxHu1_SereQa3irQjTiqJjvxoro_ld0Z--058u2AD3RwHQ5ibiwy5-_0p-OB0ua4eDlnDTrc5wYRs69AdR4pFsvB9h0iGuCpHEQcWEMaw7scliTqJOHT6fTnr_c8nieYZBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بیلبائو به اتلتیکومادرید توسط ویلیامز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105610" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105609" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=NkBIKRV0-t0C9-kvFuNRYrfXaG_SINyMa14d-7qcIHrEvFiQstz3mHLR_v-1V44hYNweXGHXFUPrOFrIlu567UuhxVDmSwDfZWtJ4Q5PaVRzx_Xhlxgtm9z3WIJCpmDY3CBcuzb8HY6ccpK6xQSUTOvYAV1mksmwTz64AQ0RR9-rFUM-fJ1FlRfdLtZn-DT4EHO12V6dMFZxPH0IpO4b5LNYokZ90M1Cr_RG60FoOrmHdf2OB3LCaN_zPHOXmpbqSXzG-ggBSduljSndPpAceqUsMk2gBXP_O4KZQ2MG77KuY1PuS4DZuRPdx--_vUKL6Q-vQTQK9IFcTaaqztcyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=NkBIKRV0-t0C9-kvFuNRYrfXaG_SINyMa14d-7qcIHrEvFiQstz3mHLR_v-1V44hYNweXGHXFUPrOFrIlu567UuhxVDmSwDfZWtJ4Q5PaVRzx_Xhlxgtm9z3WIJCpmDY3CBcuzb8HY6ccpK6xQSUTOvYAV1mksmwTz64AQ0RR9-rFUM-fJ1FlRfdLtZn-DT4EHO12V6dMFZxPH0IpO4b5LNYokZ90M1Cr_RG60FoOrmHdf2OB3LCaN_zPHOXmpbqSXzG-ggBSduljSndPpAceqUsMk2gBXP_O4KZQ2MG77KuY1PuS4DZuRPdx--_vUKL6Q-vQTQK9IFcTaaqztcyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده
روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105608" target="_blank">📅 19:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تراکتور زدددددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105607" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105606" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105605" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=qq-w9qNk2qp6gjvOnWSCBdYZkyPTaSol2X_l4ofqQBbur12HEwJhU74b0sewmVv-BBNddzznTOgfJR4h1-b19-EM0IH7HQ2FVZJ2xeK7Ra8w4KNtXJUB8bD9D5nnk4J9S4I0Bx3q1DQFTPOmEMkdITqLv-UsJ_vVLV_fBLM3lcIZn0jMxa4XFKy0sXYflKRYQ2QoGzL9U0dKxu7yGQ9s7wd8VHnNx_6gLZbmpPwSjwNE5SIbJ556edWYruWCUDu4LmUA4IetVfiqenI7keuCPXWoTeT44vQfEOt8IsN4MgIONXnmpNpu57ZY9dswBf7ffRE0bHE0H2iAJ3e7rV3-dVgLjlj_--E3UGIiIHs1eiLO0WhtZRAzAZwHvA6Ajzsch0yrsn6n5G5eimT5bVuc3ddb3QcGgStXiz5oSAAAZ-GvN2ioEZaPL4REPeb9q7kXBsFBMEJvZ15oyms4FlbWX_IFpNr8a7RwzbhkCWwTdM-3y-aaD-PkycU1e91iVWy0dMe7NY8AF-BZthTyK62VgfkmQ0RakJK-S_29VNuDiTdxTKnfyS3gRyjGR8S-GUdlFbEpRq9EHSkMxWrUW05ekCfC70JqyjNQO-XiYTZwXuGYFX0oeJRKmeSfJbh960rzCzz8UZ8LkzIEHY3hz5NAktuBYlIQZtr-l2PQoc_AIPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=qq-w9qNk2qp6gjvOnWSCBdYZkyPTaSol2X_l4ofqQBbur12HEwJhU74b0sewmVv-BBNddzznTOgfJR4h1-b19-EM0IH7HQ2FVZJ2xeK7Ra8w4KNtXJUB8bD9D5nnk4J9S4I0Bx3q1DQFTPOmEMkdITqLv-UsJ_vVLV_fBLM3lcIZn0jMxa4XFKy0sXYflKRYQ2QoGzL9U0dKxu7yGQ9s7wd8VHnNx_6gLZbmpPwSjwNE5SIbJ556edWYruWCUDu4LmUA4IetVfiqenI7keuCPXWoTeT44vQfEOt8IsN4MgIONXnmpNpu57ZY9dswBf7ffRE0bHE0H2iAJ3e7rV3-dVgLjlj_--E3UGIiIHs1eiLO0WhtZRAzAZwHvA6Ajzsch0yrsn6n5G5eimT5bVuc3ddb3QcGgStXiz5oSAAAZ-GvN2ioEZaPL4REPeb9q7kXBsFBMEJvZ15oyms4FlbWX_IFpNr8a7RwzbhkCWwTdM-3y-aaD-PkycU1e91iVWy0dMe7NY8AF-BZthTyK62VgfkmQ0RakJK-S_29VNuDiTdxTKnfyS3gRyjGR8S-GUdlFbEpRq9EHSkMxWrUW05ekCfC70JqyjNQO-XiYTZwXuGYFX0oeJRKmeSfJbh960rzCzz8UZ8LkzIEHY3hz5NAktuBYlIQZtr-l2PQoc_AIPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
تمجید لوکا مودریچ از کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105604" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105603" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgEijuhJyXyCPJomQ52fVjRWoqajNoWvdYE-q2qauPquFJ_D5w8R5gpEFBI1PWVZiJNVD4Bb8FDycPa5lh0lyRWbyer6ph2dCJUVjVmzif09S4FN6etnMbU2Sk7ulZEJX9LcFidKLRWXploDx49OjYKuStxXnpqiMVLJjRMet9EYl7Rmn7Er0T6oMVHVof0V51IJPDoy1asWhz6JS0t64CbKpwmC7I1YABn7K2qlCnQtz8PZPC_RO9H_F_l0-eRDcAW_BQSmPmg9r_4xO4kUGx2wUzI1koI6xLaW8Vbr3XfdknEa6RaJNnLiUOUcL7PX71ptC79tkUsohQyx765fGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105602" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=ir_kRuw3gWbupbA_DcO4hxjph-TCktsnQEe7KSbI9EX4QcZrvdOt_hFN9npw_ipbOo9rXVPmf3dZWBv295haTF1PYK-uqgWJki5mvW1aK6OyANoXQBumfgmhlNlwJBFuNjmi66XuE-SY30_Tfp0W1ICA_hOh6wGyGrvE8CjMuFiLovqWM-JqjT989MsNb4DN0YpsfZOr8BrisaSeOJT5WJet6NwSXHE923Nez47PrZKHrVb3Y77GKJOliyEw3udAJUhkyaZJQBkb4mRoxb5AD7kPEJ4qoElxAovso93QWMR0wCDGMqd8UF6VMDCypnLOsG3O6OBXz4Qebeg29W88SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=ir_kRuw3gWbupbA_DcO4hxjph-TCktsnQEe7KSbI9EX4QcZrvdOt_hFN9npw_ipbOo9rXVPmf3dZWBv295haTF1PYK-uqgWJki5mvW1aK6OyANoXQBumfgmhlNlwJBFuNjmi66XuE-SY30_Tfp0W1ICA_hOh6wGyGrvE8CjMuFiLovqWM-JqjT989MsNb4DN0YpsfZOr8BrisaSeOJT5WJet6NwSXHE923Nez47PrZKHrVb3Y77GKJOliyEw3udAJUhkyaZJQBkb4mRoxb5AD7kPEJ4qoElxAovso93QWMR0wCDGMqd8UF6VMDCypnLOsG3O6OBXz4Qebeg29W88SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فحاشی هواداران تراکتور به امید عالیشاه در بازی مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105601" target="_blank">📅 18:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMY7Wp3S1attse0YGtioZhmJq8Sey1VVfRAD1jhwrZ0wRJ7VltZICAP5FIof4tgrk7TMUkptVItZaBbElgIBhz07r1VtWC9JJO1vjHH25CMmJpMYIWZ0Kf43w7sv2f77b6nL2TH5Chq7LajIOBjALdda1_HRCCWpml_NXMgVMrzaO2FwmQB6A9I6x1j0vtwMDYZs3k969vY38U8_dwV4zSv4U4Tat6JoPYVDLs-ArVM5Jt1AjRfCQaWMGLEQWm29BfRd-3hsr3ErRdGIz8ArIyoj85WMziKcX2w0TNl1RjicI1qtW2XPUnnur3B0J98Rce4DaSalaTTUaFhSOAne0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
🔵
هالند مقابل تمام تیم‌هایی که در لیگ انگلیس با آن‌ها بازی کرده، گلزنی کرده است، به جز یک تیم، یعنی ساندرلند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105600" target="_blank">📅 18:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQqGjEHnsfWQ0O7h1BbLEqQcbBexiQdr4kI8IbVfClRWqLthXq3G4iBPbkvwuC-Rj57etnWqJYtVhSYJOYEsms_SGm4bSFr-_kr9VpHkGxrm94-iDVNlooFm2oC3CpDOPnJjsHf6-PmrAcmGNBLSrdZ6gjD2ibaiNzLt7dx2SF5ZZLQb6jMDAu__K3DKmt2WxPVG-6H8Oop4hNBQqvT2bAArrB8bBdOfUIOHPz4yehSD0jf6aVWuK_UAXgblgV4uBezMJuUTy4VzFfkE_pLRzyPS2cJU-tDlEygXAFoL9WhEJvK-pOh9KyKuSxMc7ahQzdlihNEpRZDcSUv-fDLCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اصلی اینتر مقابل ناپولی؛ ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105599" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FennrDGOnijwtiQi5FX2Mm2BuQCKpCZQVcTG4f_u6Kz8XhprKiTUbtnn9hVv8QkY4D2UHs6oxMyXER3ads_OwvSYjDSHUxUBPvf6eRJoWvM0r4ldLYdS_MVEmjl1tqC7zh3rQGodxe0Dx7MNJUEJYaNdLBbVtimtDZSWccWrDRY_zYy93msZGe4oBOOPtjCG2WcASl8kvoOS5K8Km7AsOW_jHK6bG4zH_mKlaTumCL-F7VSNm5Gk1lX5vUf7r4LbmnWZFPCcyKhk6BlZmabYrioS42wF7DjzQVj7YjzWLCNkMwg2MHfB6macb-xDx3nlb-SFzJfclJZhBplJaYr7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خولیان آلوارز امروز هم نیمکت‌نشین اتلتیکو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105598" target="_blank">📅 18:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=TM4TS-3467dG1myS6tGUVXPye9Z4EQF71n9x7MAFUooEKE0566UP4GGMaiSnzOmz7PhfQX671cjQoKY_1H5llZL9vJuogPtxK42uSdrFC5cKOpwNBJ_JS7Jp-uUeVcx5oOMyNcVcSrT3_1kz2b46FhFWzXsAr1iaz7IZpjxafNjs0zYqB4KjFaLhWl4hLzq_2QfYDE7Fz0n1UdmqGpZhQgy23Yl_P0hDxACe_AdNMD4CSMrjgNPsOJS97X9fmjPlCXJBCp-EONTkdjxwL1nKFClvj2JeJVn_vNALpt0tdSY0nLwUCTMrQOFEBRUxySBKZ-L1SYhn7tcLOtNH38lRzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=TM4TS-3467dG1myS6tGUVXPye9Z4EQF71n9x7MAFUooEKE0566UP4GGMaiSnzOmz7PhfQX671cjQoKY_1H5llZL9vJuogPtxK42uSdrFC5cKOpwNBJ_JS7Jp-uUeVcx5oOMyNcVcSrT3_1kz2b46FhFWzXsAr1iaz7IZpjxafNjs0zYqB4KjFaLhWl4hLzq_2QfYDE7Fz0n1UdmqGpZhQgy23Yl_P0hDxACe_AdNMD4CSMrjgNPsOJS97X9fmjPlCXJBCp-EONTkdjxwL1nKFClvj2JeJVn_vNALpt0tdSY0nLwUCTMrQOFEBRUxySBKZ-L1SYhn7tcLOtNH38lRzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105597" target="_blank">📅 18:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
🎙
🇮🇷
حمله رسول‌خطیبی به هواداران شیرازی: لابد پارسال فجرسپاسی قهرمان شده و من بی‌خبرم‌. یا من فوتبال نمی‌فهمم یا این چند نفر هوادار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105596" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
سنتکام این ویدیو رو‌ منتشر کرد و گفت امروز سه نفتکش ایرانی رو با موشک‌‌ هدف قرار دادیم
نفتکش "دانی" را در نزدیکی جزیره خارک و نفتکش "استارک 1" را در نزدیکی جاسک به طور دائم از کار انداخت و نفتکش "کایلو" را در خلیج عمان به طور کامل نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105595" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry6-335Ro5oVxvGszRJRJ4LGWFdDxliXgkf6aYdHBzBOdQLIu285OwolQ4r3bICAxl0TMPTqKcH02f-IdOwlaFptxHq8b1W2TMz_F5Fa2-qbcyQcSOp2aoAPnJit32q7h187bOtTREZTGy0oWbUF5kxswWnux8KkooAGMhZCT-jaZlHBSye39Mx3mxBO3g2EG_6_ydt8kPtCXBIuHC8S2CCzUvUFTc9FWjfSt5KxlcVqAnF8bcxNdsuj43Ap9f-LluLqQoW07XJ446axcrqkBrGdah0tsWsI3gri09IPkXcCaszitv8lMmTd7-PS8oX8kYv5f7hfthh8rsukYhn0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=fuDu4z2IiauN7hcn5r0o3fpTjBn3L520e_xE0ad0-sp27YFvIsQoBeYkgUKZRE2JssHJNYzhrXkYwrbGPXY0BqsTfsyyKhXBXKJkttFWbU8KZQLhu5eSPtBcCGnun1RO5C0y-wk-ksYrDbKvL8OVU6x-qgshA9-pFrrmOHs68-_ehxwdL1oEB_MBReCLmb4qViMCk1DjIz5Ux4PW6Do5fSod5gsaAwzNOeHw4_9G3UGcSr6LAKsU9-waIYkOmXJV453kMt4He80AXGug5yZgazVF13D2UpB6rFNEbdxITKlvG6EZir2zCwDcKAu3nTdaIr2s6voxg91m657aE7ihTQ5bsGMUSOw8DXQUZOlt3gCL_Zp2KigiPaguzZzkfGkTxKGbcsqpJd7KIsCBZNOAc27TqoQvR97O70FwIvw8bzhGoB_SG16j-wZ_f_cszQetStaOSVi38qrJjny2WUMriE95TORzUKGlesVQt6czdIg7PdUOghO6Y1T7Zv9EFm3kTY8B1PnFcAmKaVFYEVF_XPGz6zs-7YWQZwfIcm65gcrM_Jw3sERV_CWOxe12fqwvt_DvHmWPnnc1rFW68N4d-iGrkukyekoN9gk6A8w6fr8XbB3UFcNxQSndqrl75cR1s5Z7W8E4AsI1zoAQSMa1NlTUnOU1RFMTBKaTAzaIuS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=fuDu4z2IiauN7hcn5r0o3fpTjBn3L520e_xE0ad0-sp27YFvIsQoBeYkgUKZRE2JssHJNYzhrXkYwrbGPXY0BqsTfsyyKhXBXKJkttFWbU8KZQLhu5eSPtBcCGnun1RO5C0y-wk-ksYrDbKvL8OVU6x-qgshA9-pFrrmOHs68-_ehxwdL1oEB_MBReCLmb4qViMCk1DjIz5Ux4PW6Do5fSod5gsaAwzNOeHw4_9G3UGcSr6LAKsU9-waIYkOmXJV453kMt4He80AXGug5yZgazVF13D2UpB6rFNEbdxITKlvG6EZir2zCwDcKAu3nTdaIr2s6voxg91m657aE7ihTQ5bsGMUSOw8DXQUZOlt3gCL_Zp2KigiPaguzZzkfGkTxKGbcsqpJd7KIsCBZNOAc27TqoQvR97O70FwIvw8bzhGoB_SG16j-wZ_f_cszQetStaOSVi38qrJjny2WUMriE95TORzUKGlesVQt6czdIg7PdUOghO6Y1T7Zv9EFm3kTY8B1PnFcAmKaVFYEVF_XPGz6zs-7YWQZwfIcm65gcrM_Jw3sERV_CWOxe12fqwvt_DvHmWPnnc1rFW68N4d-iGrkukyekoN9gk6A8w6fr8XbB3UFcNxQSndqrl75cR1s5Z7W8E4AsI1zoAQSMa1NlTUnOU1RFMTBKaTAzaIuS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=o-2WVSbIqm8R1e886IZ8M-Kf4jOQIOP97n4EP4S3RKBFd3135NqT9m8oLv8H33u6ekKw0vQ11rkdvdZLpr1DjxlSLinr4gRTCyNn_QogUWRY7Gb1Kjq3adb_2aTHyPEdPKo_Udpmyy3pHV1HNytWHR2EWRzNQ9anvAkOtb-IVq-MuZLJZ9xO3xq4TIRj8whQinfVbUG5MrVsnQmw68cgpggL9kheXNAoh_tryLFYT6YqtVJAybuGduBBrwKYc2FeLIYVKlyN0UV4x3IZpv_aBpe3fMdvcmhJLDzUqiM-foavRe5H76LLMo2Qr5Ilj6qJdmb55TY99NSAZJmCJvvnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=o-2WVSbIqm8R1e886IZ8M-Kf4jOQIOP97n4EP4S3RKBFd3135NqT9m8oLv8H33u6ekKw0vQ11rkdvdZLpr1DjxlSLinr4gRTCyNn_QogUWRY7Gb1Kjq3adb_2aTHyPEdPKo_Udpmyy3pHV1HNytWHR2EWRzNQ9anvAkOtb-IVq-MuZLJZ9xO3xq4TIRj8whQinfVbUG5MrVsnQmw68cgpggL9kheXNAoh_tryLFYT6YqtVJAybuGduBBrwKYc2FeLIYVKlyN0UV4x3IZpv_aBpe3fMdvcmhJLDzUqiM-foavRe5H76LLMo2Qr5Ilj6qJdmb55TY99NSAZJmCJvvnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQXXBnQsecAJAyN3lwTfFDb-5npRSBa1SAskojqlckUlORagN7zkXUYCjxSKR4LyCGAU12n0FL9Io6t_2etqnejPyuUiXjCXRXJ-j7jKH8RLOZIUmJAiZC_G-LO0bSMOT-QqoL_z2OzCHT0gPaRMBnuxp9U38oFIMmQpkEpNNDf_FaNGTlNa0D4MZCkFROod-Cy0hDrW9kvkc-gKJVlQ-hHigUZsf979SoA4KhP5WBA7065nfdosOm736dCN84FtxJGPwpTpZf4Cvm7J8uf9S2arXlRCvF6Qp8ZWvbfq9nuXLrxvi8HoC5hiiL5DB_0pDyBMivdYMgAle9Epr76tlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkXLRnuAS0Ip5wmSPjmxSRoAPoHB0uh-Cl4ktfeKhymfDr3IV4uiNKQEc2PXg2Qu9V2BWpKjUfQXbsKQkiSqvFye9XdrlDWMDK-9fioEuumvkhONuFvyBD6Oq_cHUr_W9_1XYPdH4c2CFIiQ6WwDjaziXvzS5TbBpFlOJlQe0NfNIl2izbebr0mCNTNWwguz5cx9QW_6zaOAaB6S2nQyrDrQgGouNtJ1JCwu1Iff7jaMgakm_O_O00pog4W0i0o6dF81B9vbkWpeF9iYsBhd_vo2J0hVeIDKey59T9Z8FfcUEIubGQnsUIIikq2PbTAhWANYaWVi8MsbXgdhd0LAbsWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkXLRnuAS0Ip5wmSPjmxSRoAPoHB0uh-Cl4ktfeKhymfDr3IV4uiNKQEc2PXg2Qu9V2BWpKjUfQXbsKQkiSqvFye9XdrlDWMDK-9fioEuumvkhONuFvyBD6Oq_cHUr_W9_1XYPdH4c2CFIiQ6WwDjaziXvzS5TbBpFlOJlQe0NfNIl2izbebr0mCNTNWwguz5cx9QW_6zaOAaB6S2nQyrDrQgGouNtJ1JCwu1Iff7jaMgakm_O_O00pog4W0i0o6dF81B9vbkWpeF9iYsBhd_vo2J0hVeIDKey59T9Z8FfcUEIubGQnsUIIikq2PbTAhWANYaWVi8MsbXgdhd0LAbsWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=GIRnpH5Wa4taOpvSQb12-dYgsAhNekIKZ5ZvoVLAHpiiBzzOzIAI06AQHS6qZKXdqx6vdtvk7CUB-xIMSAA8M_Fuia8pUKdLDXKgvawxYH-7SO65-OBw6t91559_BIOPz2RUvVscTAKgilZE2ySJkx0qniIcVyqb6TugTTL3SH8bOLvxXxnlv-aLK0VS26OMMM3kM4WeR9ANXYvhXaIYQt3TIPaAemrPT8AS_aG8pGgOS6lNKF8Dh45hOxRbrb-MpejqqRVRakW6RsAzU9u7a8ZjOwF1INDJXr1Vif3IVhwuMEXvgG4B70PgyyFTJjdPWJxcM3_90QJs5gplSVBjEVbc5jYY38Mbjk-O9yTGZJcDgJ-0Rz4d_8tr4uqatEy64BQZzLsWiEGDnHRPM-mjPy7ivCJ9-wJCoIdi7KfJFdxyypGYlTLkuDO_ZznJEoDQAEdDlAq5vA5C5i9WtCt4i0PR0YPurFXIdCJO4A4GjWP3bPz9GnJe503P6ewUn5KoS0bQwqMAHbwBy8HVUQ0WwGudXXDhArMQOCCQ8Cb2rjgjRa-K3EkE_WZq1-zjQWNDcXdnv2jfO8qZeLTFKHKOaOgnsbttIOwKAi456417cxdeuqPctihwwdd4z8fQ6ekPzuyLxHNudFgml0ZEV7OhbmTYxCasLvsV_TAEdUGdj4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=GIRnpH5Wa4taOpvSQb12-dYgsAhNekIKZ5ZvoVLAHpiiBzzOzIAI06AQHS6qZKXdqx6vdtvk7CUB-xIMSAA8M_Fuia8pUKdLDXKgvawxYH-7SO65-OBw6t91559_BIOPz2RUvVscTAKgilZE2ySJkx0qniIcVyqb6TugTTL3SH8bOLvxXxnlv-aLK0VS26OMMM3kM4WeR9ANXYvhXaIYQt3TIPaAemrPT8AS_aG8pGgOS6lNKF8Dh45hOxRbrb-MpejqqRVRakW6RsAzU9u7a8ZjOwF1INDJXr1Vif3IVhwuMEXvgG4B70PgyyFTJjdPWJxcM3_90QJs5gplSVBjEVbc5jYY38Mbjk-O9yTGZJcDgJ-0Rz4d_8tr4uqatEy64BQZzLsWiEGDnHRPM-mjPy7ivCJ9-wJCoIdi7KfJFdxyypGYlTLkuDO_ZznJEoDQAEdDlAq5vA5C5i9WtCt4i0PR0YPurFXIdCJO4A4GjWP3bPz9GnJe503P6ewUn5KoS0bQwqMAHbwBy8HVUQ0WwGudXXDhArMQOCCQ8Cb2rjgjRa-K3EkE_WZq1-zjQWNDcXdnv2jfO8qZeLTFKHKOaOgnsbttIOwKAi456417cxdeuqPctihwwdd4z8fQ6ekPzuyLxHNudFgml0ZEV7OhbmTYxCasLvsV_TAEdUGdj4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=ZQjuDoRmbD5zTIG4MC3M9NjVj0xsZnN7G7_l8DWAIz1bs2SKjtHNIfKqNrXWaEA5pK4fgPItx4wcQB3iZWzX3xxFGU8h6vcuBkpOPMonnECSe2ZoC8XU8oL7Ejv8FwDBihhny0ZJ7MiaomZSfwlMzkDgda-bTSyPlk7IiDN6qXN51Y5PUceHHQHb7M5S09jWFJw4TWozrHKBwvTc2JUMWbvHInbBHw_MpxCvV-BAs2zixWiy_SYqMhmoSWTd8FdRyY3ZpVP2ZptvaOFFkH3jjeZXxQF180jEj1JIjGbHTrcrPWxI5Jfja4Kd1VEAEH7TH8GPeJeQ2zLQGZdA_CyhgT15j3kVKjLbYW3nso-J4IP7iPenoQSJ6XqU1rZ9dqAUc8Fl7ZotjbRbKbPYHwX89IbHXlEU7EgtH022QrMABn8tHtucCYHFqNCFPI-P4Jp9aOKOjxBkqzuPJJZqQuU_dewd_0cs3b750LGrTFYcezh_ENItx-AmkuAnAZai8Dl-vZfOYS8dq5JziXopSrC7ag4HJkU__DeMrnBKzbkbhKZx0QVT6d-UUQsCYzdbUDpkXVf2ms_66eaxUiOs6dhQs4D9-bU1JcKD86K-Vlfp_iuqC-6cN_km8NzB1QoykE3x1CngF-VrU-m7GQyyLnqa1g4ExUAyCg2NrXEmbHY2Spo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=ZQjuDoRmbD5zTIG4MC3M9NjVj0xsZnN7G7_l8DWAIz1bs2SKjtHNIfKqNrXWaEA5pK4fgPItx4wcQB3iZWzX3xxFGU8h6vcuBkpOPMonnECSe2ZoC8XU8oL7Ejv8FwDBihhny0ZJ7MiaomZSfwlMzkDgda-bTSyPlk7IiDN6qXN51Y5PUceHHQHb7M5S09jWFJw4TWozrHKBwvTc2JUMWbvHInbBHw_MpxCvV-BAs2zixWiy_SYqMhmoSWTd8FdRyY3ZpVP2ZptvaOFFkH3jjeZXxQF180jEj1JIjGbHTrcrPWxI5Jfja4Kd1VEAEH7TH8GPeJeQ2zLQGZdA_CyhgT15j3kVKjLbYW3nso-J4IP7iPenoQSJ6XqU1rZ9dqAUc8Fl7ZotjbRbKbPYHwX89IbHXlEU7EgtH022QrMABn8tHtucCYHFqNCFPI-P4Jp9aOKOjxBkqzuPJJZqQuU_dewd_0cs3b750LGrTFYcezh_ENItx-AmkuAnAZai8Dl-vZfOYS8dq5JziXopSrC7ag4HJkU__DeMrnBKzbkbhKZx0QVT6d-UUQsCYzdbUDpkXVf2ms_66eaxUiOs6dhQs4D9-bU1JcKD86K-Vlfp_iuqC-6cN_km8NzB1QoykE3x1CngF-VrU-m7GQyyLnqa1g4ExUAyCg2NrXEmbHY2Spo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpUeJV0Ar2d7CLrtlA0fgVT72q0GdAnPoH1DZQqR0hkZ7OzdWwcrnRJFIzCNBFY7il6rJ_OEJDtSQyrctAMmJHr7FQTK4emfIQGRj9TjU68xoJlkWw7vT5Kq_Za_B69KNT9puRWgd7HdlvoN_UPzznFm83oEX_WLT5KMnhmATRU0ypdJZoFqdlYjwXHoI66hWZBiHxj7oNlRJSxVg_L5LJnJav3leAiDT_KN8FErP1ABf_06ol4556lpRWS4sZ8eSDvbhDRQ3z0AZTKXk9ZYGtuRjvThlBaIQpYGcBk5x8DovIZosR4_5pmoZfslpOvsXkwHGNJQWnJXa2lGsPC_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
