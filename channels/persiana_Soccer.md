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
<img src="https://cdn4.telesco.pe/file/l_SxlZhQW5Zv5CfqmtTi2t4b3xD8gL47YZUt966zj-76ClbP1TNTtIrWBVgNY2ySMgo8Dq4H6nSFsbg4b3qBfSLP7DVbU-L6fwHBuZu5Izl_sZPEw5OcJVT16DXM6CEWhkgwGfhzWEzP8Ns_Fi48SDD_zm9U0W0cE7Qj5k3hcCLzkofiSdDHAGXL4IvEdZaW0w4FKXpfiRxmnrDauzVGC7HABOrmNoiz3xmhKl0CYWywU39dJXiIVi1hRA3TkyJ2HFVzvATfSnUbGW82SgOqwMr5ICwc6-CIXl8UkAqdyYgxH96nH_aG2hNxqZ4tBtl-h6-Sf9Rcd3VFE_Q2jtMPOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 13:46:11</div>
<hr>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WlBGEynB7rL0INyzIjXm_PKl8I2iUBgeIKUUlo4XgtLgX_yu5YscRiWRkZ6CFGyBoqCPKF4TJqNJ2Wq5EQFzi36tzolCEMgaOyk7vB7OU6R5cV_3pu10_fGUuWNFz-MQ-6tkh7BsMLzTdoY0xxcndLLYqEJIHclVOI28xY7BjlbAtsGAR6RyofEsiMAjbHm3dn88uwFioiYRn4mYtP0TVlV9l-qoo6B_rhVG3BiW5ihap9DMM9IM4bkHMoQ8jIvQ0FmM3aFhpt1x8BTto_EwXCvbeKhRSQMPABNO6VrXHE6-GlJN9oPRpWWOSqCj6uWwmThKH4q6p4bS1Bg5rAw8dGlPkpWwQnh7bcVFfngZZB4MlC4N_qAsR0ql3MuXvS8YPEoWEjPbGTBIvEyO8sjmi0UxnZvBiBVqqaGHAs9dlSkAy_Z6M73SSjlCO-1bMZdT6-gIpHPGF1xhloWNPBFxh23mRT9a36WTRBQZ3mPuThU_ShP1U-rRE2TwBeARHvO0g0Zds2b_gz49Z8NcYxtFx_XAXwm7tLkqHHMpbBPdlCZXV5M3qXp3lWbvoc1EPdkp2dk1d7HGdURehP-X_TXrBtJ7zMVcnG6nx8TiPHz1ByW5C94B-g6LXy_dV_fd_o5ebKSdQeoWDzD0fhNJ4RdYGjOEYyIZXX8OHSku_G0WQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WlBGEynB7rL0INyzIjXm_PKl8I2iUBgeIKUUlo4XgtLgX_yu5YscRiWRkZ6CFGyBoqCPKF4TJqNJ2Wq5EQFzi36tzolCEMgaOyk7vB7OU6R5cV_3pu10_fGUuWNFz-MQ-6tkh7BsMLzTdoY0xxcndLLYqEJIHclVOI28xY7BjlbAtsGAR6RyofEsiMAjbHm3dn88uwFioiYRn4mYtP0TVlV9l-qoo6B_rhVG3BiW5ihap9DMM9IM4bkHMoQ8jIvQ0FmM3aFhpt1x8BTto_EwXCvbeKhRSQMPABNO6VrXHE6-GlJN9oPRpWWOSqCj6uWwmThKH4q6p4bS1Bg5rAw8dGlPkpWwQnh7bcVFfngZZB4MlC4N_qAsR0ql3MuXvS8YPEoWEjPbGTBIvEyO8sjmi0UxnZvBiBVqqaGHAs9dlSkAy_Z6M73SSjlCO-1bMZdT6-gIpHPGF1xhloWNPBFxh23mRT9a36WTRBQZ3mPuThU_ShP1U-rRE2TwBeARHvO0g0Zds2b_gz49Z8NcYxtFx_XAXwm7tLkqHHMpbBPdlCZXV5M3qXp3lWbvoc1EPdkp2dk1d7HGdURehP-X_TXrBtJ7zMVcnG6nx8TiPHz1ByW5C94B-g6LXy_dV_fd_o5ebKSdQeoWDzD0fhNJ4RdYGjOEYyIZXX8OHSku_G0WQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3L9q5zTE1ys4pizdjjKYKg1JRM0SBIfX5j9CpaDn9MyNly_bpv_R2Hc1v0foTUdgOGW7lhxGrARTaloBRawxnGIR1s9ELsw821aiQdLrxyCjyyflW7TQTEk0UXConeHAHID0wwt05ibmEsSqILRqS8Vxq4GRsEvSPgrc55IWXhyUEF7TWF29R92NwDb8a5bfJVzMhxWL45G_JEMHdUf6pRTPl7hEgVCGngED5T41lnHMDq2Y3Iz2nt05z-oKuS3X8venaebFgrMMXMK2EWzq7910CY_ExoVYo_YOjx6-4JrrKCQDbxNMnCfrL39d9NXJYmsaeSw320NhEmmaHjBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XItYQMvmR7mHMSyPBONvPwE-1Wh2u5TaRgkuC7NpUTK2Xnjg2SCZ5IxQJBOX2NR86kkJsXtHrdby26ESdB-8_zq3Y6ktvGdHckMHZF0Xr0y25a61MCs-0qhwjxFg8GaJ-vn_yZpHXmGXitjsxUmoa66sutrwQMi34CH9ivNiEa_uMWy5FfAURH4fC6GROyg_4_JyayAjmGq-TkXrAlp1eqvbbm472yXlQBdX32lnEP8WwqMGuPHC8Ng082wEfCGr_qRTbjuM5srfu_VWmeR64Zy6BU-RmUHKItTxE0Q1UXdluwZwD2h6QLkgjNZesTnokJX56L_LckNNUuyCs237pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XItYQMvmR7mHMSyPBONvPwE-1Wh2u5TaRgkuC7NpUTK2Xnjg2SCZ5IxQJBOX2NR86kkJsXtHrdby26ESdB-8_zq3Y6ktvGdHckMHZF0Xr0y25a61MCs-0qhwjxFg8GaJ-vn_yZpHXmGXitjsxUmoa66sutrwQMi34CH9ivNiEa_uMWy5FfAURH4fC6GROyg_4_JyayAjmGq-TkXrAlp1eqvbbm472yXlQBdX32lnEP8WwqMGuPHC8Ng082wEfCGr_qRTbjuM5srfu_VWmeR64Zy6BU-RmUHKItTxE0Q1UXdluwZwD2h6QLkgjNZesTnokJX56L_LckNNUuyCs237pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yblpYOkq_IEIn1XUS6BKIznuWJJ4uD5Ssnpd9-q-mbaf_-wNRicr1fIhMRQenZZeQASMtTS1A-pdhf-W-f1_-O4g1ve3HFdf7BXCWkxNs7-2UUemh8DF3t2jLHkS5wpyyrWZohPc-13F6wJv3MWaowZIQplOatAdp3SbD64yHzok3k_gjJr12wIXh0G3PJLzIG1BjA5MJ27zPIGSU1oHSV5doTB-umux8nv0g1Fjxs2S5satkkfStHYhbGRjWp66muxVzOYvWLdfOiF7CgMfe5qo-WRwfFcjZwjyfIFXcV2nMfa-bz9wsebB7aUdwEkl3_ptwzFNdYwgSAahsiM0k4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yblpYOkq_IEIn1XUS6BKIznuWJJ4uD5Ssnpd9-q-mbaf_-wNRicr1fIhMRQenZZeQASMtTS1A-pdhf-W-f1_-O4g1ve3HFdf7BXCWkxNs7-2UUemh8DF3t2jLHkS5wpyyrWZohPc-13F6wJv3MWaowZIQplOatAdp3SbD64yHzok3k_gjJr12wIXh0G3PJLzIG1BjA5MJ27zPIGSU1oHSV5doTB-umux8nv0g1Fjxs2S5satkkfStHYhbGRjWp66muxVzOYvWLdfOiF7CgMfe5qo-WRwfFcjZwjyfIFXcV2nMfa-bz9wsebB7aUdwEkl3_ptwzFNdYwgSAahsiM0k4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JtciebQDAcflZT77cx0ZPXSkI2jYXQxoCZ0vktUb19IEEggy9CPzCO_C-whJu5z-WiH5mKMl0U897JP_kOSdmSYkpkw3r4LRpyxepo8ZKWDGeKtFpvbzFgwYBiF491bibgnG1ZckARygc7p5zbxxax_PjGN0E7nbeYi396cxQTs7Yr0yZjOhaANeFqtGQH63fHbbImALvH53fm7gN18x60vBEflwxAq0AyjnFay8nbNPBJEXog3n6XSh0Kd6Qzr6nnTK244t5aduFQLrESBneIA16wLJNOonAbhXNXpy1lc-B5uWzYuZWR7mVQ8Ob2IZqAdHeNz5mWKzo_dn-Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWV7gK4uw4GQelQixnU59-uDAelamBUSx3a0-R_EBL52mzrTHzaTmR4r78O4cJ8FhGXcdO34yuCzy0NgG8H5ML9UEt3Bk6xQqkR52KseJjP79JlhpCqbQXGFHDKIo77EG8DQyscY-FSiBBm2VpEdqgN0mmpJa16Rr_8VUse9Vsph84j6o-ONDn4st-3CC3WfXC4Qz9NOVHnx4HYHogLJI0PYld4B8sqfEM1pIt8qCXeOyvzAkwyqf9x9-9KXHCSu7zG9S0FSJnJ4d7DVLqfUvQ5bJ8KUlk1dDxXMGWlA-YQXzzpVRzWOqq_km7OdN9xDuhCiNies5TWFTveuBnnuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6AwpDDM5vapclrSAvl_19m36lrh3wMRtXid6Qa5iW-xu4UrxegwvUpIUT8U4vYmAjdc41OWwwuPTwDynfQ5wKyRqjKtz0lHTgUCIFrsxKmxsHsTFwB2BCt1Cy02bFYn2ubwV2Q6VchWnounZZMfzhumsxVw7g0TxVWSkK_geooSgUOmVWbOHCjlhmANxLuHxe5YPMLbnsBwR729KoGf0XQTiQlJ3SdljfkstLZqdLI1q18iteM_OsRfTDELFyCtnnHfVWZOl39f8o_zFkMx6ykZVgFI1jHXJUJt3LFeodgjK9kNAR5pfUTXRKQuGN4fkRs9UPd6PSYE_qggl7MYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIgiRjVxEvFYNt6S_9Eupk2KcwpIxBcGdMCQrwXJC_OOZ4XxJxD-6vLSZw-XNmcFCI6hZd70QPOLo84UexmHuNntiVZsSb8SB8qwNXtVddR_EikKrT2EShbazj1uvikKkT1KS8tXGjqHbA-CLpKjM1ZFa__7TQC7-aAeJkQF-TdCfQdMMOKCPjcV1aKeCSJbnmV7Y6J8D5B52nnSCdP8gSG5MFhkYu6Ka5o0h9taaZ8jFriFPTNvw-g3R-wFZo3gNCDn0XoOHAh6Y4ip-RaaYqzwdkOy7DPzwQ7jtNBypXqykNvf6J28FJRoWRNpPNH5vgwNullc4FHhsTONbW9ATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh0MdKHP0uX0C6uguRE343NElmQUNQBXfl0Ad6pbApvTCgcA6rT1s9tWgZwR_Pk62ynojnLplmeheUSD6Q7S1TcoddxcAhqgPMU2Ra3yF8c1WPeGznc5qGBprPFgRSolSj3MjpupmCRvXgAxGlSP4k8Ql4vuYfi4og0mkBhsoo3YduC_ct_lAQ7dxc9VcgaJaL8MyhEaDbNvU5yT-1dK0EpR0C8dvWpSKQY3-u7n4gN_KPnmdKTcceN2k6FyOChDZzU8YXWAorDHz30D1gk-F9sJhpz5puv8TfCBu7Cs8ZGipLmk8tm9KvZOkAsYFEV5qoZm2umeeXTslQdUAX5rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZSyHeT6_j7AcqvYkT0S4lVquxDZ2ycHtApkfnXNdStz3q_82VtSIYsdIiudistky8wtY-Foc7VgOxGz0xl9tsrsIh0u5X2tdVeXZHE8cTw8ZKDvVDtzAwI1lWY-STehVD_PyhTAU0a0bpgI5HXo0uV0a16aDDbsOzs_dz7Ke-wpjN_jIf8H7zvq5X7hl1DcU-6bRenu0VhxyFBR9rxDneJfqatWSjGU7LYwNyAggMCYfDXC9e4Eg7OIAMJMhW45rLKaa9UAV4g6iwDNQurDYGRRLSqmPFlmjrevzp-NyHb4wjZUC_ESLZGNpDLaJO0JEVPEJkSj0TEcDmna00CpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlCNfBOpYHuGjk0agwsvawlhZ50XB5h9nmTzItUUSw89gETJ0d3KUT0yerqX5ue0Z93YL5Su2oBJw0MuOmb57LoX7XE4bXzlMHay025m4hnO_PwbNmi3Q2bf-iiGc-cQj2CsoZNu_K51jn4UdD5S2XQG7KzSD2J9fjeWLDTR32CIOoQSSP9z5qEPLhUYOm5qJp-DchW1y2cxnDUwp81Fpfd_8Hc4nWuYSMfBxsDKwntF8xvmiUWIz7sdKnBmOYmI90cVOz0fQ6VkXIvIE5147Hng8sdbIoI1ui8WAGL5OfUphgqgFWQojZoQLBPGvTZMC3xQEBPR6HFu8DRi5vXW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyG5n-iWYWHz2J3e_Hc7c_XskWjZ66m6ziiRvkzyA0YwmKWI7PfRJFjPeNE2U5XxPSfbfWiPwfsgotN3w62nfjoe5mSauGwvrYBjpE8TW-Yj5xXo14yN3a8zXU0AD_cM95HJll5IUObzxh8kQIaNCVCAe3C4trFUzpOhJp9i1HdgbBL1YuH2CC1UeGfQ2BDQ6tM_jGXN7zLSp9JCF6zTrX8RBFkvPkNAplHyzBNFhK8wRFeRt4FfLA4nM1FpyH9DADwO2vIlauZy1ZMhm0FjnMN-65u_u4u0tMLf4JF-4y5jpF6zavkQn8ceifMIrpK67JE5EDYlCmUDev2RNC9-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIuowQo0E7yKwMBABs8Ttz-5N3u4SwbJpacyAsSEBGJLn3nEifiMdar_IUlf7_3J2uxZSvjygNmZXQUOe5Uk1q_hzJWzKVIzCd3xtMpYODxZqUF_eK2sorpEgkaNpCDSkgNyWspv9JTVxkmS3bzp3a3xd3275n_-CsCQFeLmj0uN_r7GIjEE0JSAynIqTj9YHsS5c_jSLIyCASChZEnn9icgoTCPGXw1QItFP6DqH0cvngU6c8tIpmkaqfzy2AjkwZZVwh02iA-HSeiDnozeBHiIMxbV_U232fPt0V34w9IwnRp4Da8IPbjpzfoLvEpnnd5bQ3unX71yQs8cI-WeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEcvXovOPStvS4oZn47A9l7ECIjAAE9JpaR-cXaAdJDEQvZceyki-E6OoamJp4pQowNvRn05Ko1bj5XITwlfC4DG73GhvhtyKLJ_fM2FbaD6BTVeoWieiMudod5zdeVnV8RFncz817XViEehLJ6t59YdWBVwuHHG2KsoetNYKR750UdL_5iCQFLCX170Mx9oS281srAVNCYwBX2j_rTgCaWWyWeMzqnsYdf_p7F_wHK-mq8C6jEsxlEsoHotOeu55_AchWlMM2KCg05O5e_1GZgsln7vpfb7bi89h_cZJbElgpW5JPtEld0H5fuH0pPJHVd1jqtAKaBiL9HVTpiZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-tBcV26H7HC1VImJ3N54_YUBMPUyzMATNf8If_UGSrx_PXoObxr6LUjhVQgTvYcAUkm0nJlNqKlo8xLuNO2-HtV23sPBA2VE6H75UC_EI0PPsj3Dd4cQPvdPq8HaHCl3UP7NXOWrqNQuTO4TS_ek0NyzM5WM9p5RB0pO6HT9YmxkVl_tVmQ4d9-47NRwJ8zzD1wlQ9Si_CxWOU0WutBAi2hjmcQRt3-5wkquAwh8S9Wa7kGujs8CogDG-erO6KFd7W-_b6WuTyN_Lx-i63jY7ZMgsNCMGxOxwQfKCPrszkufNi2nmC-lZ8Okl_ELeH_OhiMz6LxW41zDUFckJzylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwHV0SrEvKPVba04IrnbZZ8jCH6SobdfN3kbCQDievmRdADhJwtzpNOxRIk0QGxG6eUC6X92nwFQUDDUzdmpLAkRsznAZNcIDg7IqqPWjzggMg5hvWHktefz2zWe0b1rEFie4o6z8Acfw3yEjnLkKj50mds6_pHnI2AWqDlZ5APmU3WX2fBidsbaHWk7__r8xQtLmr-BSput1DT74YNgccu1bFq-x-ht0fe0lvthGU7pdhCAhJToXGTSYx8D6kDW43SZeBC5_a3t4FRk46nrZsGcugBobdJtDIvEzbhlTIS1OX_I-5RTobaWNq0xffQt63YGuTr6nsryJ0lcsZ6pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcflKlZ50HXdeZVQdVVo-giaQKOIxX4GLTU8ekBGO7421L4DtUzQsm_QWGw2qm0PBbOh9rw6zOF5D9gHS98ZnPDLOy14Rub6m7kZPnouDYTo32qNW-a_r0suy37ZKpOVh29FMRHewP5DS1pSdDuWdOy-nnBfAz_kSBdWbjx9LcOQE2rNVpYCwD0sruOK9CUguJ4qu_F9HJ_SxKV_DXPAMH9_4ZFcysN6A8-Lp7tHrmfb-6gjT8sGfb7N6MOkDWmz19HM3sq6PwclBqxDZupU7t0Z6A0FLl1d9alz4KAw9w09g0kkAkYDes-3Zl3mZBseT6TIZSgGsOx37SXKAUgtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhYMtKnes3hbESQT69S8peuQms4u1FCCWTgZ__fZqXcUrMuhBzyHKLY8CZJ3lqwPxMK37h3xysNG8P_tf3td20c88tz1mnJan-9vhy8hyeqwqXMHIqv65KXfFQWg1N8OPZ1-OSieAQOl2HvWXwM2VyOBR7uGfNb-_N-fUvC4vFjKRpLrxTtYzybaLDRKUNts8jhm2ELedk3EwakFwa68maCdD-t9u0sOAaF5JQd4NidudUMubpHoM80c1Jw3xPFWz_HPaRGxMT7QtWIooA6rDCH5GnFlN3jLHeSQHPznN0-Ccwk99ky93-ydaGSTrOjH8SfAraiovDA5_iWcKeOuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHs2QwbGmNCJLKLiQ28IVxH1S-Xbe3e7_gg2ySgmkzfEXBFrLJiWIqUQ_9t-V_Tplp4qf96NJF1NpV9_pqgRdZFG_AvwZkvK_M6BHKjN4zaGxoTw7Qd50IUHTl3mvCb26n_jvBnh3MOt7P25YSbU4TTw8SVfDt-v3peJN7V4OZChRY4S63HeMjkD7yl4d2jTuQU-PvgoRLNs8p_YkPT8aq4tJpJpdYU5tyVLSr-xdmfEs92huz0yqz8mHJkDBtwniabxFzpeQ7FnrG9eG4y2E_4vLyJfbnn8yhi0uFGx88WQqxoMPyTIlhN2PRZpKo8C6dphTJmiD2MdosX4rLPNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZmtiS8l_wkep91QgFY92or3vZm-YtOyjWquCq09KQZU650ZdMY7qU-NHfeAR2cCUM0iosP_egi7LQ95L4nldCPuEOMIhh18B_-Gc_r7moZHbbF3pJWd7F_M655PkQdP0wJhygLLdoMTepAIa6JXjot_0KMt_m_TG1qqHpPc8wnlORv1ifpfHDFvSpd2ZucpMighQJrqJekrpBZJSN6AxtL2v6T-CtfOLxPIUBVaUOS2rcb-NJAu5M9--IB5X7srTxgddSr5ISCm9T4ogDS5ORbydniagbrRVITU0CYS5QD1JAahC4cQI7TG7KbDPv407eQSJnEEeg4cxRgc4DgJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr3TMGq6TyY8rnkNwRQByrrI0SgVf3Z0DBtU00_m6BhWqgXkAseDdZWaO3jgxABuKEV9HS1H1pEPpFEGZwSTisZ8NinifvF1e_x4aRQWVJD3yLa9sFATTw4DDNJyk90iXuVhHPol-LQbFiAbYlFlL6IondIkZN10U93k0wn-5aIwSS5PgkSinJEbQEFkrPrBRKrq1iwCm8yXNXIPgr7778dh7sfKRVGMQM9bT6VMM-8JjHkPJ2Wv07NaeoU6mOdgoECRKaijHg5U-tWJD-u0haKFJVtJz0yLZ7IaHsvW5yQAwvR6KTeDc0QIY8wqWcQMYyouu2-pgWrPZxcxlA5bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARs8lVkMuJ7YhRk5h0S3UxuMWFDnFLQt8eW14apEr-4gHPFXKK7YF0vxHS1k7-C-kCMNkbednLL27h7-0mzeSZsqIqlIMvUQLoqMi7qmm3PTyzsZqHdqm8vW6dtRMh4cTQhcLm718ccINEcnV1htvIQIKpX-oMpBsp5RpjaZafhylJ9l39CU1DQCq-3U9QUJBGGWSvIp3p6PZ5qFeqZNoJE8WLhLIJ0mgo4T7_ifRSG2sRV2p1kQt73zeHskWI6KAf1MVak5A88dcsAa03M8z7GZ3bcpqa8jZG9SiWw3xLuOSHnvAFz9cUMB1rPhwu_ZZtYNDyuEh_QRmhcGvy1HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfbb4u4tgg1fCbnAxp6pgeT91K474LV18oXdmNK3Q4Mm4mFvgicbquuDgKDbG7yY0QASE9XWKiNaC_V0N972m3s-JjPMl37tyR5q4KbaHCPdT0TQFN2QhOg6an9OgTVESbmyfLrF1lhcR7N3shSCO2_tJvENEhFwa0yfxHD9knzMGgp9lmyfB3xhGTsSAwPJTuPIPp4kyM182OcX5wp2ffBbalAmNOxJbNgKDL9gIeAqQi2ozpd-y75k1VDWVpdP1HRilDJ2ItGFma1oAAA0JvCxLwGXal3rPoWTEpHoKSjNA1zSYymKPOFbwUfTIOF8k2gfI9-qE6TuRKhBCx8uBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkVYqOwlmRK94IXeaXDgvEavrO_AKIWwdXFPDrupq7Gqx84RQfKL6WRD1wGSqXarUZJTLKDhoGpvgT3cm6pMO8WE6EpySvTkDSjdz4PUl-uk-yO2b0mEwzwfOp5xoniexzwtSwRnptFbHQKpecNWcsgPmP5mHPDMj4FlnjqDvxyZDl5eQP0BITxx0qCLezeuOC-H6PXIEN2wdUkM8MnnCpaG1LAo5f5uIVdRq_W9hnH5iVk46-HuLS1Skn25aesHYipEbJcS6vkCsS1PdTRvanWk0tJhTiDFHYvBMKri6l8VKfrR0yVfV6nRVpZmL72_c7C-UCtQajyPFyb2uBGJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=nFZYw68L3LvRlBN4FDqQquRmJjmTuVPZxtDLJD6XRJVbHQKwYg0qDlwbv1AhlDLgHa5pL-o6FdStr79NI0aIfBLxgNQ6sh0T1iamundFnz8oFcddr-zGLUc4RBEtThpF4ADAQdEHS8PykIudRJyp36rIBEhSMHsOvwtY2ofoBK1sZikDLapVALuWAn0N79_oE8wRAN-gHpHLXaxCE-qQ_r6tMZ1dt5zD5lr-m3qhhpFFf6hExFx59juPSzGcpS7oNOGZq2gfEu-G0nGZmFfrBY4GbOsfKnloSjGZJg2zvsDH1jixM-l6FPL5qY3iDIbetwGcJk6wA8l1lJtp7JMm_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=nFZYw68L3LvRlBN4FDqQquRmJjmTuVPZxtDLJD6XRJVbHQKwYg0qDlwbv1AhlDLgHa5pL-o6FdStr79NI0aIfBLxgNQ6sh0T1iamundFnz8oFcddr-zGLUc4RBEtThpF4ADAQdEHS8PykIudRJyp36rIBEhSMHsOvwtY2ofoBK1sZikDLapVALuWAn0N79_oE8wRAN-gHpHLXaxCE-qQ_r6tMZ1dt5zD5lr-m3qhhpFFf6hExFx59juPSzGcpS7oNOGZq2gfEu-G0nGZmFfrBY4GbOsfKnloSjGZJg2zvsDH1jixM-l6FPL5qY3iDIbetwGcJk6wA8l1lJtp7JMm_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hftd_GEkYap1whJ3Vsk5b2gkeKCy9u0MewlbkcfcsB4og7KewrgWAV9pqx2iRgt84uLzQtKsCAFLkPFiGJ3LFdhgMgCYg7ZmaKG8OmKSFWkldxrD7S3ZqY1cklXZJ3yhv_-AS8qpUL8GjLqHCTg3jsp2drir5d8s6R_-ZU-2Nk-dP-3C83L3I9_KCmq02OmGFNfSfSQGSVZFWlo6JLhFYbZ5s-g46_8w8DmkA_olbPribjfQPit8ekxDA6W1a-UxcnpG9b2batRB-Qw1uugPSHN-o6b2sdCH9ga6PtcWvo1Enewn25uRwD9p5JWTzV0I_TBVcOyRU4F2BcmOc5fedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNl22DaIrKwxr8DIAT5wpem9fk4lq-CtYyFvu69O_wlaog1PqxkrjviMo8HmmgFLHfwkfki1H54Z2QIUJqs0OzCX4B6DbYi0v140O57UxYQApywX4L0-L8S9KRS13hrjW__469OzrsPJj7ebH8OuU99OkRp1xUaiV7OYaSWFa1huhtKPuC0ylRHS3TV4JPxMK0PlgBCNZbynGdXdHqxK0QMaGZxxVOL0bLydBjxkVtatmXdfav7e2VfJ_GnFQJBCtIhxcEjF_WPC9bSSmw09DeJGg71_X8A2mfihUABu346C7g4oTN_vFrISPVPpBjxSZmjgO57KXEsupX8ZQwQoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTR9zByjpfz7NQBnCUeYYVkTU2j229qJ4nc8wYFVZbCH-g0PrJaD8-EFfLbIorp83dRVmqWHBd3Joz09tUv244W2dpxTTwltXu3Z7IRolB87V84Aj5oEDrsggGUQKZibTLdVn3TQA5-bkTEesTSVRsXPV1v6LH-tGU6TELiw5U-KtotVhPO6gNpf8N9wuqiywGH7BvLjji9dbyDvonr-C7KPw53Zwkz3cTeagCXedxf3A1-SdwZo16KpwlqxOSGyl7d9sg9_T7oCAjJggp8U2Bwl63b8A--X0jgGxwKyOKGXlTqlZE4KU7gVYbzG2-V-uEjustvGitdthCXGu32uAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDGI-H1CSoMuDCl1wGvrbdcd6Mao5AkH4UkaPdPLjUOlLkm980I3IiFrxSA3OI__y_8vYV3jG4_fAnlwLwEZVEqoRca97gi0XSn8wm7l73kTvY-1YA6e4wWNi75_EiI_vEeB9MEIWm2vRbprsUFcjiT_j6Cy7j1o743cC4mGsw-QEv51G_sDzqF7qsoJH5jaGuQGiZva684ue9fgonBfB6Ll2FYGqQY2R9Axw17RtrfNR4I-gCVSAkpHc0cg_3mo01xmLM6SgeXxwRougTXTXHc2NiFOts0ZqtNHbprDV0uy6gEPbB2RdyLujwSAK7rZlmYz4sAPePBPo5AkAYpOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v60yYL-0O-dOu0WUNU-o_0yN3ZzaUiyHZHUbbpO5OgA4jPFsdCxCw-_slGRo4yPPAGqXOdljGx8JRsA5jKKr9DfqDEHPwFK_OSz6sfjNNM-OMMtQ6U0lU_0LSFxWsAfoJS9uGKF6YdTYSX1ipnIaxHk3orEfkSzPStO3Jen5Mvgfd3ZOG10Dn7yBZqHMkf_um6JF3_cOVYRHkGeTsFNDA81vsg3RCRwR5qR0ukR5GapJGkcan5wlz1ro9tEneNL_KcHz-NY-SIlXjMGKVc4cJVdHtzapb7A5eALW0LKHdRWuodEk4jUv8636DigP28CQ1NaXHEewiJHJoh2H1gkxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXhHHqtsidUGDDJh_MB2OrZ66nD7M5ZXoySBfQtS_w0K6uxQB7x7XZ-N2rljImG4x5mAXL45jEHraGdKBEWbkR1ziU48LNxkzpyPtjxNozjzk8Ay5faMxOPdrbSbUlEaHgC_iRtf4PD-mV-dUFTHRFC6LZ56Tsx3Wtz4bQpUwaXMI4JDegWuSZjdHKB_7qQvb_3utY4ibWmarhxXWDQCLecjmzEvSfrktRcpceV3OVS5UQ6fOrLem75wL5L2yF0rt21Ir3MBy3PJPYvV0_Cyi5dpiJ5RLVkl7K3UCm_ps6_A_RCFy87JNPWjJoVKKag8HLs0TBAgIZ0QeBHlQk_zhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkVqOPMT-zzAOpx7rvQd-t-PeUY4KHXoVXFKbGN_HuhGoAL2Ao0LjEkujTYEHDjxSAWHA-gUcFIasGMg8vwGD1lHLnbuKID9kK4ny3b9GK8Vx1BxyBSidJ4KdZTfqeD8EqP-IkrrqIjWmhqZZpYYf8eA1hketaEYk-ZMD7EstpEgAeHkdRquiXWH53pDen5AJLlIuAYaOjIlYXSVbsNAKG8ubFyT_wQh85LVC2T1OsGU2tc8bOCqA-zEJMzvp_jopBm2xY1lCKCg0ORleLyOhL2d82ZKHr7xXEdvEwL8jBfeEoe2TxA6iNVYTrBRo6bTp3F1L3g1rScyDNp4vgbweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1ExSEdO5ec9vFF3DSIE6XheZrnL3EvSR0RS_Ii5pkLgH_OadbTOKppJoWHKGKwUppXnMAZiQTh8nG3WWiqfTYcriSFrrTfWOenl9gCKA2TxCbdcvQR1lhs52NGlXjNYOfIgTL5N9OeeQZRUNSY-3oTjTWBiG_qcP-LProLvKyIEFlegrMTY8F_lXy6TtxBqXnzOP6jLdqm5xd_N8cUYee6zktLcDsGQ-Wxe1HHF6iWw8yrqcQQZbSgBUCraK6nXyw_eGkp5ARxyKrUTgNBqBp-uow3qC-VGG2b7ufr9r27yipjMXr7BMcjcC8UZLoq_tOdWILBvLg8FLFDYA905jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDHOM4o_YXWWveHDJe-J8ucQZP6VXP_d4_dCMOfCQKiamUbWM6_5snoRyGP5ln_SUgf0EIw4Qa02XFvNC8nyLH5V_Sbv4TEEPev2fEul0cxJAiu3YOHQVNX7lbC8wq9_ZgWCGc3Y-eenHD2D7738ued4Kpsx0Zb_dz5rpEZQUgooS1s0kjywRSQvmMRKYBMPpeydfMzikepos-P90jaeOmj60y_a4IzsGa7sU7N_unVheqdLjRcYFj_0Cd77INsCClh5Lhsq95FVlWCxx93-CkyMuI5lKn8TbIreMkGfcSxS_NL6Zu6sqLxGkOlMfo623ITyr95nWb5MTkZkT7kVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asr9JBxlNaI5a3A5CZkyF8xIOysDrXGBRL6vo9xERjuahIWZzeK4v2lQarapWVU4zHR0EEgkZx3m0NNaE2EPjSPqumVvMWRc-vE9s6TvZiZ-YQd4QdlvRZ85Yiny8-9lLnucLXD-uxsM931kmt50jgv4HMcZAVWoj_G-bCOOcHPxTW_XaYTZpBmYbmztR-qTNX9e3Yl2BTgT3o3BXJVQE03OiCdx1gnM_7zK_4TV0ef_Wm2vQa79210XsgXt5tDjWDu54omhYVI9MLJESsQd_-EKyrUkPGx0YywDvDurgHsBEPD_Mtqz1bytTrqaJcscvB0BOO7zfoz9yF-Z9Hm7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_gJNrn7YeKKwvKwI8sOAjJ2-R3ruly1wv6zEF6h2x6tSbMOWHd631tkn4G3pI-W0oHqeb8syzFyXgYHFBjEEVISGabauM87hz-8vokjW_qpxCffcRy46TJiXp77c-G1rXdHuuTzG2_cVf1xa7JXYNvqzyeDq6l46qxuMg-8SDGFJvncV_2rWy0Hsy1VkQt9QlsDh1lA6L7TBydZ9L41exaaObBjLSClHvgmki9tCysIQbt9OF7Jo28pOK5sFzTpiV-Vi2ap10h2m2exJEGIyanSR3G2b23giAPEd9xaSATagymziuC0BmkWwHSz5tL6HUVh3AABZuWRIoYR9KVjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VumIbzQcgGt7AFZnIu6SPx3DtIgLrvccThWAy3943e2i4kgWZkvmclgZvUMeLmtOO6MahQjNjskStn3kZFiPvFsaqKNxSiSZ0nyd9ZiP2uEv528Jw7VTk3ipUtncuoVTMSzOJ2IdcpBXfFhBOPJH5kq24EiCKWUaWC7vYkpo1eG12m0KeJ1769aKdfC2-Z7nLYHlTedfz9uYIRpRkKZ77oW1s4_ovQTGpwpz5eoqCVlBdFdPCyi0VhNnBwUI5-Vw5o_cBmk1cQfH8Yrtp96JKHjQXfTJj-hsKas3QmRvF8AYqRSI3q7ZgWoeJZJzZKnexvw5JFBlg5_W86wpVoHD9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7jYThcybv9LZRK_EdLOGF9cKgAG4PziQ4kMRBhsMUpGTFxsMCuqyEWYaCq9beYMlnv0tyNKx9FIss2XssgfA8F31-nHILN1vDG5zMyJCtaNihjBJkExkDLVNPkZ0n72AsD-i2fM293EHIodRwQhkEkLn0LOebhnnkTDKaQAByXIskFSSQ9CM6X_iAiTClodfjyfNu--xlgWF5vGxnDohOe6kR85FqEuMiKrlpP3JhZuUNOb4hhKsnPywS3WCxWLysTcuJv1SqIJw5nzDBWOOLlMjrWqHr_-mNlLkjZW_DK0cRMbnN1I9mkuipotBCVLVvROMipcWn9Us5FdnyEFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG08D3c1pi4dWs7qzgXIm_ByhnQQsMYE00YfA-xXojj5OIszcyqsGeT3UEqDnLBKTReFisxt5w7UjpTyuXgZDUi-WcE-BlW5SmRso38n27ePns3Z3HCpMFPrvSnmmAPQAtbgUAOlS2T_ynb1WOcnLzBexIolUJ3gPokB2CPi3YATUrniIdNPFqRVlPcl_G4v7gu4wVjSyYkgllGiv9QCuPoF6prhWrQdbMF9TD58fnkIo9aWmjO0ptZsg2WU-6O9DcUyE_LaMs1uVzcQ7ao3S2eqB1JFNyR5UVWHXz3YKlrHPXa5saT-2Dsy3zFcwGg8qKSan1Wmp-hVMS8QcKcxBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azH4f0VoL3yuzaG0xFrPEO2WFfqllLHRe6FuYVW0gXi6MgRj6WlIzPfi-Hp-8RHj7XLqg0V61k9C_o7-E4JBAD1KAS7C7YDmGmZ6bqW26I2yFOZ5Hmfm9bUrzwJ1nT88tRVOSrxFZGjWmR_qHNlCmUpv4qePo1WnTUiGEGRFFCP2lqLJIaowkOCWglwtTyfmtPpZePD-UAO2flpCeWzxzXtpsfutHeutzob8QY0yI51Y4tS6Tb5be3liDuBkg0u9ZYQUUrLsWsA2mevlLi9DwtfW_iwTETD3kXMfa914m3ho_Bw7CWWg8NAntN8eoPKddMVyJWR-FOiXNmKuqtpkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITbI-NWWomM_lxf_0fr2rzI_JS-UHl2Bd0juBuIjSFXcfmTbiXcI7o-XsCIBQTK8eh5GgXzQaLCi0qy686rtFmColyHuHM486ZZU1bwIayZ2LHk1rT2vS7CwaClbZGeDqsLLYLKXAz-X5O6u5La_rMrfrtRLZD1abPEJJF7EPkZLgJh7csS5qiEBul6xq2CoodWhogZ89gFmfmhJJXOpHsedvGwdmz8dZSh58RSEl2dYtBGE2R95CyOEuf999y6k-YHbsV6ERj1nfdcvnZ0UqT4mHC4AY2R6dfdk8kFmZEnrRwt-4fdH-VrTlSKHHRVqEUZbS6P2zshJ8OnDIKhQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRbh_2waNbXhihuRPR-Bn3FBCWKTrejPa2YkRZLPwDPV6DaSk3QLb4JYcbZp8GAHPv9_AHPLPXaL7e2Aks1FufzAUThS90_ZoFsIBJwXOZ5vMXUK3qLRR6QIMKS9XXpV0K0Q31Dp6K-HpTR9yyG7Y56dAry4EDLkorcN_df_Ci11dc4td1LbHg_sLHlhniaYkmQKYPsapvgcQ9IRtq4-b7MrHLIPb9mcjn6iBKoXjczr4sSwjpZT7ebgz9qhT3kG8s6h-8WL5Ok0FA910xuJ32buYzqDBL2Iw6vY22nM8w3j7seYE9QBohSs3LXxHRE0ABakRdjSo9uURawpT_DpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4ytVpEEJAvdSF03Y6tqVEWie2m78nqx2EzKNtY0dImk21CGdErJi_Jvs8fBnQ2GE6EOnBpVtOFTxBUhfFUQayHUPohb8Up_CL3IyXdXjVMl-lgI6DrDpP1zMGBl06NkdvB9LazamWbUx_KRy10CD0kqjpCJXLesFRC-Cu5lYk1veJARz7wf-NjdIbWWnwzVH7A7cA0Wi_wjI5-CrLh8Vs6smQzWhDlVpksaBydTk3dmaL_NF0fUoh5mdJ38pyDHvvSfVLMtptwrZ2vtCrAer_zQKZF7Sjlk9PC2Z-Kzgg5wkVfsgs4xsUb77FJyfcCZ6eDbJvsgjatfFm3Rm42nBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=uA289H7Qp4yFOn1oz5DE8MjD4N8TyomR3NXArOluuSIgzrY_2VPBV_2FfI4nB_uHqDJBoMxvirSy3Eln_R-xDWOFYMKPpbjhjpgwpcVDDT-58PSgNhNnMlFQvfNr6Tk9xDvd4JxH7THR2XgesXJnMGHuThanL3QAhcLUCIwStqwkfPi0GnURPMin15n-yuHqLeGQIbi8TtVrhFpXYHMKWMrrX61DClr0CN3izT5RNqjWaRpdba2ny1KIDfvRk32eNgL8C4gq7zyqFZ997h7A4AKzj83PvGNPn0YDFwuLrO5T3mF6Y0CaGewD87MYMRwlsbKQXS-R8mMTDgQid5k4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=uA289H7Qp4yFOn1oz5DE8MjD4N8TyomR3NXArOluuSIgzrY_2VPBV_2FfI4nB_uHqDJBoMxvirSy3Eln_R-xDWOFYMKPpbjhjpgwpcVDDT-58PSgNhNnMlFQvfNr6Tk9xDvd4JxH7THR2XgesXJnMGHuThanL3QAhcLUCIwStqwkfPi0GnURPMin15n-yuHqLeGQIbi8TtVrhFpXYHMKWMrrX61DClr0CN3izT5RNqjWaRpdba2ny1KIDfvRk32eNgL8C4gq7zyqFZ997h7A4AKzj83PvGNPn0YDFwuLrO5T3mF6Y0CaGewD87MYMRwlsbKQXS-R8mMTDgQid5k4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=frtKO-OppmmRf9mFeFoY9h8PnHf5dUfdSImRseg-pGiODu1MbucrpWTnQ5m3J0LfhS3_GYJZjWpcY9DDAgMS5cikXtUGPvxGYY2ukMP8fY7nesTWA5G9cgt6Mdw09Z3dm0ZB_QJJYnz8483eH2vxiKgYXlYf9TDIV7hFzttuwAQ2akbOyEHuUvzZbB8OqL6J7LiuxloAYvBQ2eZquofant9rdvyAHxLiIgh6sHywEGipSBF5N8Ax12lOLDBfY9Q6fbAMZgVH4xke-B-pOD1Y6kEZUdbr_WzGQu5S9NjnU41OBDaiZ1amfpdah0KRmNWu4vKx1igpd-iFb-aIjOg2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=frtKO-OppmmRf9mFeFoY9h8PnHf5dUfdSImRseg-pGiODu1MbucrpWTnQ5m3J0LfhS3_GYJZjWpcY9DDAgMS5cikXtUGPvxGYY2ukMP8fY7nesTWA5G9cgt6Mdw09Z3dm0ZB_QJJYnz8483eH2vxiKgYXlYf9TDIV7hFzttuwAQ2akbOyEHuUvzZbB8OqL6J7LiuxloAYvBQ2eZquofant9rdvyAHxLiIgh6sHywEGipSBF5N8Ax12lOLDBfY9Q6fbAMZgVH4xke-B-pOD1Y6kEZUdbr_WzGQu5S9NjnU41OBDaiZ1amfpdah0KRmNWu4vKx1igpd-iFb-aIjOg2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dphq9mUGA8ZLHZ9yR30yCt8VOvCiOvFlST4jpP6A0aBEfrRiICNzyAdPENALrzfKJb1vx6fD_9tsowXhBmHW4vkMbiUKM2GhUvnXE9y-BtBMEYv_Zz8kjliC8WgWBRgsV9qgTRP96_5UvptloyGMm6Slh6GCYRch6-JaJyNZ1WruFvFBL6ac09nnGollK0sMz2LUZP7mrztOdQpKUME6V4yFggq1TDYHiL2qeXOWPdHEaH4gS39fWumH081ViZUgpyQ2Eqi4X3XkGiWFpL8sKe6E57YtXlwS-EfIleyAFF8IbLltqVWo6Zz320LBLqrN2xELkhaWTkA0Qpm7PNe4fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSP_OL6egK6cVVYWy39xM6jIoVFipP__f4-IugkXbt-E5Wtvot7w9MB2MsyQEM27n6LQbqjeuijU0M2YZI5vihZpYpJel_vl-eK6Mj-O-R4BHAgRAZf32Ks9u9kaCf8t-GkLijhzxT55csDkonDB7DAyhnj711fvWU5_s1PjOn3Ek8P6lQ1ZcQY1SeIJhRMGKvKR20xZCsJup3Y3wZjhnkX9ddqmM3giCWBp3U2FT6hL_TpnHsb2HKpw69feU9QZMkh5gzyZx63K8FQYCh3nCNcLVjLWFu2IHJh3Xpkzp-DQyd0wfFNfA1N9zsUjwIQPDOFfXiyOO3rB4SE2W8dSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plW2AiIxXGgdbZbIemA6AtTcu3DjOu8pcmrGOqwwvb3QLNtIBy61E8nD3Ou9ttKxiLzU2yh96cR-GNC08otbM5xH7Ffe6kgeTjhQ6s9Bb1pjV8gUB3hKM1ZKDLihrapQUiIlEsC6FK9lchtSK5P5KJXiwNUvOFECY5slWFatIMpEdC2BLOfRh8sYBaDtMMxCTKXrKIUtCqVgsySz6d__uOHfSmqsry1wIJ8IKYbCwE-2i37C9HssKonygZ656wMGDQqyfCCj7UcbDE-VM4V1TQzYKf2l7sBdtxADlY0WvMAma9YD_zc2rD1U-MzqS05SPklNygDTNZ09WfS9ZoAkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvFXX_DLD4dwR2y_IPNNfViZbH7i_bSRRnJ8fXS5pOAdE8NLZGmz7uwPf35Xdn-U0pFjgJWLlv7GsKwrnu1X5aH838w-G_heZFMU0RRV5M4HxCsA9AJLLrW4tmVpRV1NAEWGn8XGCUdQgB9D2_co9Ix2UQTG-EwwZvtO3BsTNcAjN6JHk2mru8rRDuUn4mPMh5jvI5689Iqnbz-MaanWrncDmwxV8tWHZ97cYIQtCGaFM9Sx_T_P9PmDhiPxAjCQ_fy0Lkcepxgkp-T1uUDVeM5isngHll_iHlCrcqU1CQY57Ok9nbu8PGgv_POoWKVHKk6hK39CbITRE4rcdaxfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6jFFxN1wbRLARP-oH4ulVXVfBE4baAQpbzVa7SemC4I77f6B-YNpIAh7s1nb_fbhZdCgd-_zgZbZoZhO9Q700s6nshCon0l_uSaDA5gwnwf3Vbi0hk7KaGSpwOL-8sTyWnA-GI6VnXgLZsC9Uyd_Yi7Ci4_35xMDI7FfN0zMJkNhDb-bF7_96M_kE2L8Hy6opPrN62ENf6n25DXG_74CVC2Z5qP2-2DsXApnKFh-F1hVBrxE_wUXYuPVkpu8r3yBQEJEB5ICRgiXnFRaIWCnEHiWYNLAkMeSkjt7RDr73V8hnMQjxwW_xZvr1D-ImfWRRtno-yX5zMwZA1OojBRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQa5S-MpkW4vpR6_N6E4gp7EvwKbd91L-TunAByCB_UTagG96GVvdGCOn_3t1ejTDSU1TWu4_A1M4zY6MHZPgBcsNCD1dY5r_ncU2TLnt7MnkfQSdLqIKSuUxeYBSLHda63gxKpXiOr9KoBKZWgjVOWLhzoeksr6fu4PeM96nG-p4vKfE9eCXr2mefayLC6x4ANTwcfgxOdaR-unSIYE4X0nu4MlrmQ02tSQhd5eXUlncWJOT_ngnewdqyUYe3p4dNQsp96Psy1NYZJhtO9QnVKVe-4rTDzuv5381_JGmVzB4tQc_fD_hSFIhLGPeVps98KAjMiSB_MNvbuZ257bRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/um4SgtEUcrafMfxQVC1eieLcKSmvDyS-7M-SI4LzaHtrPMrtRL3GX1D9PBdIBemSqCFF9SjkXaoSkWtcUw2_fiTQnC5ZBx1MmA9CZSdL6w4dFQ-jR9OyFfgjrPtyKVf-Tpo2UwqP44O2gV5hb137CbxfHg0zzJVQZ-9hLJVLNuscQkEj6L1fsq6KmBM3IQHndzPX3nnEoJ1RxU_MI662sosXDk_50ILYjOg9ZYxMQZLBhWiwi0DJwiBZo8e7wCc2Il8B7UNaxlsb-MsDEuNLO2FR4UEPXr5bB0W5Hyp3ImBKCBgi7AL9FkXTMWMe5JRVXazcOPhEDGmZjQfvz4g3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFDmmc0zI_qUDMDib0MIudQ_3uGaDEdIOeQwzRSAQErkB2bJniQcsytKWxsC1scIgaA2YPWOrxl2oOrKC_fqTnS26p3HzxzPS2_Wa7vk8bB1x-WjYrURr-CfWwOp2OKG2Ep4MWQq0Gb3A_tkavf44NJWgs1xQtkxoGb35tErtCR5Tr638Fns0XMloVUizwulS4NIJSj9aIT7qAKnHnPVRfyiVpUXbQPuA9fRopG0DCAz_X67eRJLz_wJYWZPfAuii-o1sQ37GRf7Nc3P3g9fNCcALSCnE1F91JOo8mGo4Tyd4FxQ5GIJ92ByFsnL4e2NOAdWcSPCMdsqgpSYw_-DoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJdjvigxDHDIPdUlhwRiv8qBN4sq8j-H1tnwnbLgcsuVKpKmhn_qbACdVt1ILsDaHI1Wl9y6voZYUuP-h0sSs3tW1pyLuRKZoYdB55SPxIQUJ2698AR-l-KtmGMHGDVmjeFnNEi5GUae5LNFWTRrpq7YrTb-twTetKkgUqLl7zlcR_kNwMeyrgaWbCqlkNUedxh3frfq1fVRLpECJX-gun0eUUaelkDbDdYU_HwMWANyyk6cPL7W0QfpamvbWGAsOAb4D574hY-mLJSlHyJ7t6UxsyWSzGB0PO_2tP1t1NnVY6I8iDLD3bXG1MQpUeSF8IxsW5G7vpftN6SN4QWdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-Qq_vqmEhDrypt35rjJFW-zBNwwpYXc6uaImze8ZXXGiZQTLYTjgcWNARGjKi9nlA_vCWDMy9fe-ZWMLTKQI__utJ8JvmiCW385E462s_Voe0-HqnPUT0chKuyi0NJYvlJ0pei-aIrLhz_igEw3U8UjL176j7ZURujwl2sM8OWoEDSIxpJCneTpLpMChM-3zUhsgxCuHG__whwCHkiZwSaKHgxcP-haSBEM1eUpFlO8WlDgS9MlJ8aFcG6lEtJlZ3Uoh95DUSzVPpzUwn8P8D0VpLcH8m3fbfBcygAf_PP4AMltajq-sZ6Q_G4h9r81sn_TzuOGAnVJWnvDWKvwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix_jVusNgT3tLvEARXN0sBEA2sS1JsMXeRuioKgExCI8BMn9xIcgMfDoqHhqwpJ1DJA9bDnSMUEgR2wPewGkq8WuJWpnn6G6XmmShTrkhMaBob03MfzEHv63f7quNiE65fzAEPpd6kSup97CV8nYsL_R1lHpTPD6adGwLwLMXhjDMdWAk7Wy-IdBp_2zb7k6clVJKQ98-q8kjqDY4C5Jq28q5MaMr6cLzG-CQJ6HYJ6YoadCCeWuuYmKpTyudDa1vugCbK_HYCJCeYS9UAAvnRjlXJ3-tirB00mcWhkyWP_k-lOjo0jrrjR-v4HZ_pU9mOjUT0-AbzTiDQP-xnqdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnbP2roMCNXuNaRRL6pDNpm6MVP4HyJFM6Efqxhn42-qJLkMLG7qgvRn2M6e5JinrYgJNBHOgRCWiOmZznYnaaBW_aPxUkzB3Dfy7w9w6H_JdE1N9289XI7oD0eriH9vV1MWELuLx0AmV_w-s-NgRxtDLOYSYrlwuCnDGIr1MevmX_A5PguR_qiQl9G3W1UiDnVSMMWlRfkyoJTqwYFyDVQVBHAdIzfpj8cBR8fYkzOQWrflmtX2gylriQpgxPkW9aUEZAXeIscK8JuzsCnqceBOPl3PiyorZMj2J3f4cgolwyuIntfAUumM544FRPhUi1bxGAp-yUIcb7Kcux1UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhyg2I53uQYUNEHxqHndqM6vlGOslQMSCHwfxC2MA7PRgiB3mB-W0ojQ1_okZFRhTDq_3DxNCM6O8Dz8C6-I3sZukHTGSYN7NCD59Og2ZfQPJbCWy4zmms5VxYrfeJLKnWy-4zcHzSNn5WAiAGM_gSiAgycECFkphcfItK_-h8vJP9P-51wrQpLD_Fv12PEgU77kwX7SF8V-3A6ppk30PcsnKApHdyiegpaap-ekyTAALJeUP2z7R3qiNXw6g-OE0BreGry2XR4cki1g8QpAT9X_2-olvFSDgJ29GclCYqDW8K8a2Goxp4Kkvs09WOQZwrS0-2pPxbJKid5zOYO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFpQG3nYiXo6ALmdbhnqxAZZ0kJNhB-PYB4NYHZpnKNUXjs5IO9kmpJChRFXk30uZB4j6u3fgfrAm5mr1aqyy54uPUOfBh3CtCr2GkH4BAVr-zKcsPwmPALbaVz1Xsq1qsz-NnshQANpHp2Yx_XpG4f9naRLuTMTWqoZydnwMXyNkMJh0qucLp4NFNv4LG8TwEXfVZD5Qxr2hIcR3tWtscIGm5dRiDBWgHylX5xqZwjtdtF5D2LHQFy4IWuYym_ekAF11bLnwZ7BcHU2e3nE_RXb-9oQDDi4AF79wi1kUFw24NizeIkjM4T-ma0VXdJfkhSmkXXxO3u6J7pgwAQhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cER-XT0tx7Uc1J3sW0GNaVVVJsP-gkDDe05hkbAoqCzG6DtH-AcZXRqSNaH1fV4Aq7LgHy5WVxNotXyOhkwC__G9hNPBzQIQHbB3Z_gfHiR04e8CJMQ7XeUD-vNcC_oly3cvSrW_FWaTI5m-19hAF6YeEs3a_nXJa56zwYVGOjpP0Qgi-aEPbO-jK7buBcn4qY4C6yGswvC6QTu7wgUcCbR_K7lGoP-wTBAB9IVCzqWW9nmzjaFz5lopaO_rRT4kLgusriNJABTTT3UlKMI4_DNVMCXh_OIODuoRMJ2vfTdP8ylmDiz5I6ioe5jW9Tv_0j24591snlLn1sYHg1bSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOa7b8TS6LP23gRY1onwaqZ3YsxqhIVyvj-Dausd97L7-tWCy6UK1G0_HdMPbahY2IFzhylv1H279OJnBFA3pOJK9sAQbtH0jpVN462t9aOuNifjzbm6nm0oZBDioArpA-eh_BopdB7HZ_qwLXjLs1xwYrE2DiM3IXXqCVbRsBzr6KMpH3-etjY29MiYub40ZEpDKhTeE2qmsFoe3rE3qHgez6sEpscnCnvLz4z7pLBShSbieTZRiFJVlEkovV0uUKJsXSr5pV0J7rd-DoR7LsXao-csWNv6xUs8zRNnIhvzIKMbMVGbb0FK3cFg4CWu__QXZ77WFZM5I06QaNcG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy5PtIHfB4eCPQguAFmUapjnDBfo79eCZT26tLlXaFe2mlRhkDgrGVe9EOJbFtbBaAC9rSnCVQbfQwZ9qwMU8jWAiRuS5OGDYem0sbHfphlCieQK_4js24OGPw46MCXpbVq0mrDCCYJHC3Ke4bPr705Srw7mSCxALwGXkl8-_x8PGN79EhIFu3RqzcEcPJwMoudC1XnucaJtYiWTy9GcB4eLBm9i2dp_SsZMoU4zWMEgVQkiGv3VSr9EewgRIngM93NTsiFpbPBwf3ywTRc-esuhDtYHdeNccZrOY2rYuKCjedosXAyvBDWvLl04SvHfg6ZXNYZ1MUjFJjAf8J4WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLJhvLP0zKHYUFuESfKaiVf1j2ckSAw6p-Hobywh9xGn1EGlU7GBlOOTcnXELJ2QRG__56YtVKZ86mOkOBoMoN-TZRzGh0J_ECInnctTL_jIhMQfK6XbeDsIpDp0SwZxOE9RV1FJPvenDiH6VOUHliy8X396E5kpGZXLw-3xZWmpuV_9fq1BXDtMWFHWAnzE4BN-FfwnlJ3CtKAbKNI7JWfn5Lvw1yX9wndTKquZNrfYY6eoIb6vLcK5c0c3CvlBZYhGGF31wYQf3pgehmOt4c9xQpo4jgc1toHyGKT5JDJNtFSv9YGtw5EZgeHWThgsry-ypDK-cO5EcF3UaZXRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRxE9M3GhurS9EmiRhFnQivUXPFBErrDHSzLUB6v1MskGz7nmkFrxPKMdcglMDQph5lTHvmmPHhkmjCONJniwyQENLITuvcWIMDhQRTygnfOCIvn_KAWrsxZ60BIEkVaZgUsdaj_vuqK6A4KhlsIl-qUW78Qp40JLGIDLjcOdlqjc9KDVze9vH0N5cR4ui-GlfmeVzP0EJ0LnLqksqVO3v2VEjl4_Efzr1v0tMSmKgURd2zs9xby7bWmkVWnJsfUKF1_yKxGyGyHLQ7YT9Dpqub4K67qZ79WkQosVFctZ-l5q0NgJckMIe1ATVWCgED2DR5Sjt8oZyX3IowTyLONog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQLIpKQIzxDqG4GV9ovYXLKeTssUXmdwl16MKE_mb0h-B8VS1AInGZqP3C255Orgo0PV5FSauFpu_fqo7oFvXOmFsmcPdbpoR6oKW7Ef3YaiXvHCOnagaPkegocOwe2S0aepYFug01p-VfIDi3EMhmHRlzB-mVvin5t8_1nMzpQ4FaIp6JeJm80Ttl4TI7qeAXYFQGh4Gjf9jzYuc7RPu2fLX_ezwXSOjLkYi7PQ2S7xLRIjeBt_XaeQEedEWv6pnHo3eVAUGMJjbLFpRYpeV4-bhQGFs7bz02xdA99fO4vK5oNnRPOCdphrCz1szuHoO_LnB1Xmcd74FgRct1MsEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=tXlAYTL6Gt4kiC5AWlNOl8xuLY31e1f6jwnrLB7Hj6Q_H6J7NUmSwLhvIOut0LH5l4Mh0iVkKBeouy4PZ3zBOqcJoQ3QzTjDLS91Wx8mNo6NT5YWYK2g5DM59g2eiDdwEscf2VpemZj5CSCRV8sJuolKz4WVDzakedXYW8uTDED1DyzJooLzu1h1SW5A9Pfy0tSRyb1CbX2hXVYe86U9T3HYMRyc14vk9T19xCwjJGDTbbuPsqdLcDgonlNOgFgywUpQUbmSL-c-1xXFCeVdhruji1-8tB0JkDLxInea_zfbcWGS6eIJsvlvj1TayuP6lsVE4B_4WcMbRao1kkFVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=tXlAYTL6Gt4kiC5AWlNOl8xuLY31e1f6jwnrLB7Hj6Q_H6J7NUmSwLhvIOut0LH5l4Mh0iVkKBeouy4PZ3zBOqcJoQ3QzTjDLS91Wx8mNo6NT5YWYK2g5DM59g2eiDdwEscf2VpemZj5CSCRV8sJuolKz4WVDzakedXYW8uTDED1DyzJooLzu1h1SW5A9Pfy0tSRyb1CbX2hXVYe86U9T3HYMRyc14vk9T19xCwjJGDTbbuPsqdLcDgonlNOgFgywUpQUbmSL-c-1xXFCeVdhruji1-8tB0JkDLxInea_zfbcWGS6eIJsvlvj1TayuP6lsVE4B_4WcMbRao1kkFVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXE8SlQa_hChmA9XVOu1-kwUl0NiVOEXhziba4OD04mciWYb29CbOUrfguo2FCTZSgPYEJUvkUPMwJX3OayCmVzrGBqv4X8tLGwZfoCOSil4rpJ8mIk20ZblS3j1M5mupEYlHByRgGeYvwOYLDGUNUVEqtlN-6iknYqM2JNt4EVJ-dFuh65LrMpT4C1NveTLEMkQsTHvSZdj06ZM9jJNZ_Er8rGbEPQ1QO0mbuir1FTUPjZANlvimQXYwkq04-oSS4es21T7ebHv2QgZQMY3nyRysg5mOlPuS8Rb5dgzDvUysh8UHwPgL7vPgahqwfDY6h3-6vvzEXNsuDHQZvQLOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_Ug7AUkWALJCx7YJGoPEy6FrBIEVlXdjG3prvTc5oO2uBlESokN8WIzuW2keT6xex02f0SDOYStMp_OwgroFQdHVme-LcKueerwGND8k5gRx7KVgzxArW2FUXO-c2cDDnIiXplqrvNwKEFP35VCg4tfFJENYo4lonJ37giFJu6gYtnKBVpfAjMueFKjX1pilGfWKDe0fP0gKSAYsRUiUrdrR8r1XYSZ9TjG6EomJd6Xn0kIdq37r7QBh8F6v5FGayoI_GpoJmJy9NTobTVt0Pupu-ldQnaHK5TdqXUMs29WLclOtnctLZbz52RVpqm2dWISgHW03TIFoeGT0CsYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riBSanU2wo5mN9BloCMSigVZ6g1ojwUgc4T8Y3gw4UdieTxbFfEqhd8XT7StzXakUQ9riDbL-9xpTKG01q5fIvZ1dWPJlaPIbDnYwq_KNYLzeEmhm4v_1No3ZACP2DIcQbwE-jf3q8nF4qDSlPH3QpyhLz4oN7t5qmtc3SpFr73MSnUe3QcpXm4BSnCfHwjIx5ysFTgKdiiX7n9o1beLt-xciZBAoGE5HiBUt70EDHPLXXGzD3ZpL-rQU78I_vhRmNpuqixcwgbqTz1a4co7Dlp9kLMGtcWaFgxCz-HQEUpou2Ey4KadVrNKtpnCRj9HwcdrvHcRiizVq7ZI-_rs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8o688K941IfjY5i72ooXlhwtz6ZPvppdoKTAWsqleySn9JV4NJYqkXvvB7DwSynqRucr4jhCVixRwMdq7gw8m7gOlRr2Cv7KwdGkzs8QUH48m5im09D7925h-k2uNEkLk0-aZQYc8pB-ivnDL6MG_eoNVaMZ97boWx71nEYx_765FuUj92ccsyojyOLJtFE6DGWuwymHXo3OqiQgVsAdM_qdwRN5zGTz4ANjQzcYCBHDk0MZ9tE_TpqvCm_ege_ld56rDotYnZvbTSszXBPqdMSiNKVIDgncuVk1QSrG4hBLugDzQhm6O-EsSuq8dWJrDcPN_z1gOXTY7elO9v_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9BAL2RB-1Wc9bC1oQZCKJSOnQsBnQmrOKXWkmYPHuak9xqlTQ6xSni982GrOSoF8TGMQk4CKpec_WsTQ6ySKIEfZZqdbsuY7zwGII8sK2_I_MWDS-39ZHCRzpQUk8jsQ7X2o9SbvwU9rCaNMv_aSJ6gYy4zDFtjVFRpMHGDKd6beSkpClT59XJEG3XZMK7XCSMXxgXuIIbaKIdci7ZbzoEfy3i2CyZIOM4Yp0b64NYDj8NowC0tuEYZYFOmTiqtyrOyueMhUlE-BS2V_1ZcfsQlUFinb-bRnvyQPcvDxImCWInjI_Wj3RgixWJ_WUo5zcv6TNzqxSxH8chGZvB7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLesUFHADxGpzOseMIRhOwbpzQCPUWkDeXOXVsXVeFOO6Wjsyrf6hLViPMbtGyvLxGuxAiVGzVeXjb8kwECv-jWfWLpxtDgkbwQnxkzlO6jZc4FwdEukyWJJj4O22qSiw6I7fRLn5MSTMRF2Y1Y6yzSRDoVbCjo91gQD19NORAJ-L2PmPeAGldoQiP34D-NLsIPs5PwuLtyoZieBy4SzsHrmQTADNpBcie9irl00imMo3z33MJkE5_1TxJsS1DAZZ4LjtuMqNd1o9zHgDxu8oHZaKn5qyCIC-EU4XJpRRLmtbe6LQ14rEsBiDk3RB0uBUCJput4pSn5yXbl7iFh7OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiCHcA3xMqJeXlhkJiziT_WBR4Nxf-YKoS0txTHRkK6jG_tX86AGiqPU64oaueP0cHyTTXvV_Qtfkshg_0UwexSTCraxQ2Dk6ImsTmKgVKnSn8oL1Xq8pMqw0ZbpZ9BMdAw-SBTNYGrzpD8Xl_HDZjAAmkcNiL8vLPoWoVJXPs91ZdoJEXvV3mTp0oMoWp1YbeWfbAuN5bVUAM5d3Fb1hXSswgm29bGhpMCEjCqkzP9prueT9dz2TW0tiDx7_wTXTv5_5pgS7UZp6tQqgjp5ZQjtSvoK2F0ooaiew6XbbO6osEmylefL4UgsvD8oeAr1QfpqLrfNR2w6MQLfvAi8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeIGj3YL0oA3eY-HiF-M3BE1wN1RpsBAZ9NgeCXWd5Yz1KxXHARdpNeZm2APofGg4cGReCaS9AQ_CRuy2bf31N6xyX4uRRP4N0icEagpPHQTYeIEMvWW_7fH991OSrDeFyiVmE6EPPl6EqdDpPQv299kCKYYruG8smCMCse5DzUlfShkdP3XdbETIyqzuW6B0mWe02ULbab4GD7BhD11_FeCerNXG9ZXyC4jrWwM6gSAiG3ejS5P3vpHzRLYZRCKexqx0xzC7_-ZSuHBv3HDZflJhxaVc33wb_rypdPWt_ja7XzoE4HGUNuWniabPao2zFZ6zRnBiHzF44go1SG_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPsTOjUZtp4OWyB6ftqVdcOjMlf4_4AHehKCaLA3XOjxqt8jkfi6xBnfXL5ccfBAuvOVmiG2UPMFmbDtOUJG6k91on_VZHTKa9QKYGBGxLWgvKKG-MOzQWHdfdTIA1NeHUIZJXzGwCscoiDCFKNDShEbOQmP2_DNoMa6xW6IahcWD1lFLXnPLI_fM6xRdHK-9M8mkA0uedxy5_YXvrc97M26WxN2fy8C1v47jMPpi5twewtOcrTIbSQb-JySReD_hb-JlpuyOdH51W_7nW-2M3-gkmh8_K0YF8vaaOwHngNlD7U2rW6aWUAHv07XjfEfsCNbTzFOetGtM6BRmljL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzoS_kT698Q4pUMSkyoeNqwAsckck-fUZItALevIVIeoR43o8qlsV7nbnMZe6LZGjdCrkwEIqvkwyFNJ-NSabnQOFysGkocak2n3hlROfQkwpWBACF5bWjSDJ6vPnsLccqyLQA0ieD6yGwLJ9ZgVECeQQdW8qPsfuYIEzpd0kH0LmW0gQsPc6Me2umDCbbD-uYJUVYPsoSfmeWQ8MoqxH9OOj-FWgbx3zZNnijC0AsAGrB_tf0r7_85BmlY55KIZKtOCeI9YyOWKictkFF5v3_GX7fG533CQgHJrgAf0nBJs97eigcnE_KkxHAjwU2_gACg8yPoy0s0lCpXN4udBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThcKsVohAx9ipN3Q05PYs8yUYXh4qVM7X2KRlAUJ6mgJfnpg0FmGLu2xKm8NkigvLGFRaczyUXkzRF4F8Jm8NQMsRObsJM02-WRniqhi9II8-xmj0hrXPICWbzFX7WS7kQEYAPKVHBcsJ3y_dZ0J-XE8gqVTg14cWRoyjy2XQOsNLF_sohoGd258lTSlPuLENdn82czGHlr0zJKDBLzAEFcEoVlWHy_kasJEHyqAoFcAL7pbzU7KB1NSQB_vvwxuxf1fpNvPi2tt4pCEcbx5-or6Cnyn0JEo1oJ2iHYD6Z__5NQNv6K9VjC67dHT0ehvi8sfUxQ5W4qGST6lanFQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=gTPrN26ie5hS6oTfmh76qM274Y6m6nI4Q2rSQs1CXn19-87ACfSrzlsXl0B-TMX_Ia5uwFG99780LzH94ZMfqfIgHQ6204r6Wr12jPg_uuutzqxriWvTMpafF0kMlfjGI4EOzZZfSmvkMaVKXvt6CfEre8IQ88nqr5zPrk7JySJUV-B7rSDTpXV0KCeJA9r6RerNLl4jG6647883xQrCKbctQOKSOMrcgmqACoQkDPIeFHPGV5D4qXC6JsO6qU4A0E3BAJkg4AYdrT-pCE40mr_k_sIpUh_PVXQ_yIiH2XwLJXc7ynm0BFLZ6WYLao9w9wEDlv_d95LeuhSDPjfE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=gTPrN26ie5hS6oTfmh76qM274Y6m6nI4Q2rSQs1CXn19-87ACfSrzlsXl0B-TMX_Ia5uwFG99780LzH94ZMfqfIgHQ6204r6Wr12jPg_uuutzqxriWvTMpafF0kMlfjGI4EOzZZfSmvkMaVKXvt6CfEre8IQ88nqr5zPrk7JySJUV-B7rSDTpXV0KCeJA9r6RerNLl4jG6647883xQrCKbctQOKSOMrcgmqACoQkDPIeFHPGV5D4qXC6JsO6qU4A0E3BAJkg4AYdrT-pCE40mr_k_sIpUh_PVXQ_yIiH2XwLJXc7ynm0BFLZ6WYLao9w9wEDlv_d95LeuhSDPjfE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSAwMJogJWqFSZqYBaG8TUf4lGmT_Z0A-iDvq_-HScUy3Zc7kTdlqGvccjkZMArdp3zPxikrP-Vjg9K5hLojWMPvu-uu0Ue6CWHy_cb6svGmrKURo2B5idLwRO5E8Qv1fxJyfQQ0Wu1gCZWQGBgCsv8rAxkwjJ9qJQ0VFB14X0SdaTiysoiz5qTW64Vr7O5v4qy1SBSy6WGStAXfb8O4KfNLM5O_GrM6KxVzvoACDLHMYniVlrXUZx1UpPf9b9ZbnHw5aJlUvLIMZ_ebyqmJpH-BuS5VwVHe40p7n-_eaT3tdQSV5erc50nqcD857-_Q7k9ZxdRPITdMP8qrDNTkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVlMgvj-EQFQdEM29Jg9yo7gDMYh6BApdqJOqMGF4varyMJR5PmlNBsyFV_djz5MyVCR7GLMZYDdHchSlycY5qG7Z3-5oEEAf4EhMY1LuEf8lbbFdp9lYDnXyYtXFHxgjTuThQ6OUzd6zG6gCi5sHxz5GkwfYbN9JhcD4XVcTbZ-HL3nuQIQdiZvos-91m5dfK4ak_Uh52MIq22UscgW6ztvjK69PZ6JgIrbo3w-a8R0rAifARH3mtJTFABre7EnybLaGnomDjQwvokoyI7ZoDuYMYPBZaDY2W3dIMXzmCNVW66qt5dctkrRu152L42xeEbmdeR7LzLibyTT2hdtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdboWvEYyntEGcPPLLlVnChN4sa7nWwGADJCEo5eex9Jp1cFGTpIVvfUcKsA34nrn0VqTMrw9rkSLrxNdCGaXe92ZpQkRUewX5SWzn23MTtgLaboSO0imANngCtqX_ukVVlNGtEzP8MjBZ39iy-d-5i-WrLcxa5lZZpwJz_WAP7czsR8wSIsHD1eNgA2ogoOiCWxrTky8H78gheRbavmr8DIhNrB14BS6XNB-P4HzzvgF4JqOgZ9P2W7YFhvqQdaDSNiutHqEQz-vpsPLIH1gB-cn9h-PvfuQfpgm5SahRlfSPoQYrVw2b5QcWON9dr4PDwGVyxtmBP60dxnyAZKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3NARWRv44XIY0-YwF3UYrcJ4_DzfEo4waZ_OKz2AAsP6HN0RI28EecvUyhte__ROViCizXXCn3Rw-sxmSv817wzInEMPCWytpUurBnQ1I7tBlCrMhe2I9f4rKUgXR3ZcTNHHnQrncRymWLdNgRWvVx3mOpupENUV1MUOCG1A0hCW6N31VZxrFWXjr0xHV3bqI2Q7RVa8UlX845kmd3TQ_eM6DdfIfggjvFVqWBsMb2jBVNcoGACSqPotYInHhHgm3J-_v89OGg5tLCeMUgRx6M_qVRt4CzcccNHCR2jnLXRX1UV2o2e51F_e-nFWQw22M3uPnv27O7xsobxF_BQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYt4juoyfCLWs3zAxckP50sJ0A12AnZCw1X8ZNRHHWr_xj3JUcwyAToU1JtadSHPQi8Kmwdf9UbCE2ElOC3sg_cBSNMEMXtJMUWorev0c30atkvKddhCkckktXdzF4cyFAsyF55PeKkWsuZ7dFl6YLsLQn-HhKSS3qnWqHSq57qU3QTaDvi02ybBOPXIDy8t2m2oUSEywVjWvjD7zaam8K_2Zlc2UjXPeabnk2P46d6kCp90NhR86za4NxhshoYcnk-w7iAl5_uy31xQ-e83wvL9m7kKym48tbiTxbbEozNVnbM9ytk8p22Af7sRN7yLItesdsyQ9e4vBo520H5Bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKdesVcPOgn3DYQxFzV0OGD54opODirlJ_DqbH1eUUMYxA2tkbwcQRJob8qpksYhpbbhH4NhV3ZRLCyND_ImbmAv4S_ERxKQmA7HfJV0LYoWDI0E7sspfiD0DC-EXfQpBuN65Gt3QqDHdWNysY3qk1QVpTJ1lWMN8_xBLmVpzZdQylG_GjWsyRLJHMb7v8BSoBLZryGlnV18UANwafXObhZPeif8RNe_BPStAwftV2qKL9Z9dT9T6poTFC_zk9oM0u4SEmqLXXY5-E75jG6QnRE3JlDGOotL_b38uB0JfrTtZBkd134Sfd5cwRJTPQiA12kARyzozs5Lp50m-1smlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qiavl1B3Rk9q_B0c5JupVDm9FkTlBzvPTSDg1tMd81zS_wS7k6-q2AouzFK3kIt97Oyjbi0L_sO95FHSlkKJep4820pY8bE-a0UHbEqaKUxa9c1xllRnbR62cfkDl8FlRE5xD0vPjED7O4E1MWvIpSRhTLOwr6FSfb-Y8t9nHate2HfrAvkEEAaag8S75eGWfjbpzJP0G5rM_03ajFEdVcNF5drn0cVyeG8wOjBvnhX1ZD97OZ2a6-4GPuhABnjdg2glb6w0tL9TxxHAVuy6VOpzW6GIJS6os3yQz_YW9MqJrujUjm-lYE3NxFW11TUNNfE2vjhjFJ3DVeMJ4nH1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWrFaBNquoBe-FxmBUfDr3XnwWNEN6M8kZN_svZ_YrDSwvLZ98TzaXiElz5dVS3wXWA5IZUnnWh45IG1ZeHbFMUoKYV8vY295R7pbR3flDONxuybnKj6pbMBn4Pg3a40rukyAi9eBavEV-RRdLnZY_JLpPt_BEPtHvZrDUricQqVdCtQFK3klMBf2U9WfeUGhBKEmlE9otsECT0dHgluKQAgJm_Dw4TIXD8foLcA3sZiT4Mm8sqVryGayLR48d3aee5WWcGSvTpmH9YnY4zsntM2mzJLXfBP7Fnof3DPUt49jzs8tAL2UzuvdJYI4d7EgX-xkOPad8tRyv5wfUQDhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGx4Xh-t-Vjj_ZBrF6I0PLN49d9G6UigL1r1dVdb7GnkfqxF0Tpf0qbuO7hCZmxTNUUe_kEG4q3a7dlxYlW-CtIOl6n47wDrT1_faDV0jsa6jj8yiysxgrTRVudXv_KXwmxoVs7y-dapTUvJ8hkUa4oVJk-cNxuJ3akU5vrV7aEFb9KUgj2t0hG3w0wSRae9ovhvwTpjAhl5gEV0fyGwEw8O1SaABKjPItSAXpDZhwtkaxMg1o7fLbnQ5iobBincp5t_JRQq_jmLIG0Jt_uMP9wplkn9Q58WaMvSoyzhQzHB5Q5yIfcu6YKGsz_Uoul6IODrcAqrB3R9YyqlY1NH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=H5_RMAGhuL5z6iM_NYg-LpOe2nBYXhHuuvS6JTadiVlL0qBRYU-i4J3_HJPd6Rdr2OA8ReFsrbg6lfv384Tpi_jMglMaQjCVxDNm2kEONZFwd-BIu2l6CgZVVhNqyImxD8vT1JvECDXYyBlCvlW8robmPotR8Sw25SZM-u59j37LIRen8dQ14H30ytn2qFLGVfkTS7pg8ZOudJTfFVtkQIHCi-UqjV5ts-syJKc61j1T9Kkzxsb4NyjOd1UbHxSk01GIHm5PGi2pbZPk-bIUrkt3yu-pe2uOq-szTOLOXqWSjfgQ-LIt5sMrusv1jcjvZ994V6u2lqb-nAfUEwFM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=H5_RMAGhuL5z6iM_NYg-LpOe2nBYXhHuuvS6JTadiVlL0qBRYU-i4J3_HJPd6Rdr2OA8ReFsrbg6lfv384Tpi_jMglMaQjCVxDNm2kEONZFwd-BIu2l6CgZVVhNqyImxD8vT1JvECDXYyBlCvlW8robmPotR8Sw25SZM-u59j37LIRen8dQ14H30ytn2qFLGVfkTS7pg8ZOudJTfFVtkQIHCi-UqjV5ts-syJKc61j1T9Kkzxsb4NyjOd1UbHxSk01GIHm5PGi2pbZPk-bIUrkt3yu-pe2uOq-szTOLOXqWSjfgQ-LIt5sMrusv1jcjvZ994V6u2lqb-nAfUEwFM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=A81qoct2hj1Megd-hzHm8S4PERxPvHhjhwZNYu47K9ElyOM_PasuZ9cB25RNaaaR5THi_dtN2qe-8InR_KZUjlfa59vxw8lrjyMYNcuV4nkgr6zJDq2mBN4zgUdTm1NQTdOs4H1iA6Hl1hRyezwvcL4xHgWgu-adpFP3FVytKtRiJi5ltON3WC2qfuCgCPdxqAbM7ytJFVGzsim9ZOwZdlRzfKKmTYocon289T4JEAbUCoTu2XB8e6X9Y15xDY8pm8e2NDNvB-sXt6BinNdcaI0FFZB2iLikeSnRsCXVsg4mFwhGC9f8Gaot9Ad3lDj-6PDIrB5MjiGRVLYaXz_Ctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=A81qoct2hj1Megd-hzHm8S4PERxPvHhjhwZNYu47K9ElyOM_PasuZ9cB25RNaaaR5THi_dtN2qe-8InR_KZUjlfa59vxw8lrjyMYNcuV4nkgr6zJDq2mBN4zgUdTm1NQTdOs4H1iA6Hl1hRyezwvcL4xHgWgu-adpFP3FVytKtRiJi5ltON3WC2qfuCgCPdxqAbM7ytJFVGzsim9ZOwZdlRzfKKmTYocon289T4JEAbUCoTu2XB8e6X9Y15xDY8pm8e2NDNvB-sXt6BinNdcaI0FFZB2iLikeSnRsCXVsg4mFwhGC9f8Gaot9Ad3lDj-6PDIrB5MjiGRVLYaXz_Ctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_8Y08vsbNEc9neJMhfwvX7uPNE83LO9ZX3m0LUcM1LcTcHaGKfG5fF_aRQLxMGjgmyWo84qIZolyEp3C0M28RWfzvPHKC09peMLqJPbBVFxmkGb0-t2KB1_5aMLi9OW-t3Cmf3YZRUJblMD94xdevoxaoYDdVfg8QE8j-Se0HgU7frgGZJQ7GFeQV81WRfmHMzSFBO8bd_E69UFDnhpDccQdIMhTH45CGmB64-XtN3gtUrGHFemvAf3E3gZH3pHDD-JaCXNUXCwSJLdfR5p5Hj8hy8ILNstFff3ZFkVRrJ1vj9iwG8C565CA4sRM_aBmq7GRjg3Kg0HK7LGZHeQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYzQdXQYMCr_eWt65C75Mmk3hYNJWqqZ7L9tkhd1461ltsgWLr9CNPGcNPZO8KE6GdTAeiybbzhm0ISw6E5HsKLqCWp7zeOAOFl8SRzq-B1xoERhk21oCIr7oEZghk-m3nB0CzUYq173Db31vVBG_Gw4wzUv2oxskphWFTbTNSC0EY3_b5VySbq5cCIsI9Y-usneXeIKTrwXlcmp8TzUgU4J3OKZsxXwQ_1onEFXoNGr_8T3K6laN41_zYX-Db-qVG33AtUQHZDuYKzdY9zBjgE9oGgTADhKAI8UdPGx1PIRGudldBbBcnu3HJep9Bpu05cXjBSGIyi5nzmyj-MyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEa2U0k1TJiLi147nSguqWUkbFWE08OYDcI6_-gn-51Aq9D73kCiGa3It8flrrZooDK22l3JPrHzQQ75ahh9q4HUd03TUHJbtuBnkipHR40Dnl9CbasowOKAuk8ibFBKw_Yyh-rUZLXO9GmXv6LXvfFvMFZmF8dvZJdnB_z2A2XU16ZrGTmt0YerpVujCwnPMZgpwz_C_lj0iC-1-Thv-UazVegBScWKMaKQAMCr-K0OyQRr5-FkZD-3I7I4DNfsM2t4XWU6N6TeU3leazx5sRQIZbjlD8hFbNOdVnKVqhRXIvsiwQVi20CnczAAVD3N8-GIZMPHeYd6MsOpqEX_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY4n07-wmhTPz9EqRLMmZ8SzNR1LXfDh3EomONlCveEF1yCEEZlJ1xsUEXpiUMC997DQJd176nTGsF08vnma5DctchHIE6B-GBVa1hA5ehCCshRHmGvGY-WEPb2q3NI33pc6kCq-JWb1hyF4sp5pwg8J3i1Zc9xob7m2xeQYEGFrDqDZySpi7UaGaC6rH19VBqTr9xdd-BpJklDrhKGLVlo4LrN9twIi-AZ3g4wuT0eaF3ikYqChdpetZdponLZySxpft5_cbkeLVUzL3EKmSbXtIPZF5Nwz4Ftbv4dXnheVoEJ9KbWYZiNkr_BpyHk0U-9lgOhAkROe4As0tPjK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9mSycXSav2DYpLpdyk-OxAPSEuus8BTG8tyePX6y8Sn4VGlHo7FXoi1_JWzQEEAXYXWsT2adjLkIMQvL3RGesYHpgxB0gAJj_r765YtC_zVbpONGVASeG-w3UJ9B46toa_lBkrZW5aPswjJC9xbFeKYzbEd2olqAyPHh1ROTPNG3TeB71oClYAVpeTMOSqd8TVn9FMERRNLtN6KGQBk_zx5XXaQ_LvmbhAgHUlZRyu0I7fKFqWs821XxHycJG5PXjAkWXjY7HdFueigo7XCik5KXpROIp8JSjbFvVi3hDCOxw60AAS9s4ZpKXfUhN32P0IrvGgBfZ5jY7HCljWgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ8F2lDtXilctanvyQOFw04fmHm6Gs5YKjekwOfKoGfW2A72ZhIr4joBSngJdYEORMr9P-KDyLIGXlfRShn-MK-kBvumHESS4UakZSZlol48WyeKX5E3BwLGLoCmkConb5L9NsbD1wXGAyvgKDVVn34YZMDHbQPW4VuXHE_pOI7aG404lYsp-rt8ziPaigXmc2eoBx-80IXsecljdp5sLFKculGW6hWiJHPk1wB4L-ZoEwHnAtwNgVv2AY6zgJVNqR1M1K3aFhIWivDBtWy897uFu0gdfsQj0_EiNb-WWRPKh6nx4U4Oeg0qNGtRzU5LSeHwakMyp0AbyioT7kAdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8ZM6f2spSh2pO8t877sxVoht6QBoSCLSOqqEzJeIwXYrI1ReFqBASQJR2bNE8E3LWOCyBL1G3UtJfbtxtruSeXRlHJo0GgQeu40MrH0x-l7o1zpOm9TV66lASb0or52vEGhcPMlXUfyDL1ii6BGVyK6z7cUgSRUqg1A87Hjbjq_rpyPSKYLHgJu8MLWRI77UJLebkMRcnmiL2OnweGq7hi-YE4nrw7reEMLbkBy_MvUXlLUMc4pUWd84ywSx8JqgkFA2rk8KPyzkcXVwJRlB_I936MpA-j55hpskxkQffykgancqLRAs_KC4h95Ln7Zbhu9e3oBcq_9SURuwhXlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_K63g6hW6o680AX6KYYpkiUrpuegDTidalpywTezaNMoJX-9_iAwdelewFMxqQtDKX81xAZ1MYdMgiUc5-sV5W2ViKPg2y_9zqYhm09VgybYWSlYo6iPhzj9M8oYZumdYwdpbeICN43R4yj7K-w8NbLfOhv7xShfKPQeX9pqVqbE-t58oTRJkvqHt3P8UgAoInz9DVkgy_bwNk2GarIjlqoXGUsczWcB57nF1GBbHYT1dq6h3f6yQU9qcbS-pShTVGu6mybx_aTxbICZbUEmBIgJVsW1fjXchr_UP5ccWbx2P1MiB-xg9qr4k16glvOwVqGmOMuTiF6uIh9jwZHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhd_v0QlrKnxESNjfzhD9prlG-mI9VBky2S8UjhHzGO7SSwh7b4TYH_d24ZNm-slPRry-QIt9WhqjGGhUGA6__tO-6lIHxyNNgYEMTj0SweMQECTcggLfG2NaW6bE-uBwTAXDBGn5iPeDUNfqjW_R7bhXB3mavjSzTmrCKWOg3De0rWj0Zc-7S4tMvGp5V7YD2XTKKZCYwB1yHsM63GtP4b8ZY8G62Y33RK_j1kP7OMqGulc8XjjBFcDQLfpUOL7cEb5SYSz3cAF5wQ9dO-SC_4lbr8Luz29no7Bq00DaWWvOR1lBsXafUH5fLVv8fKZuIzTd_M0fT1_-corKNPhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg7OmOArryY0AGO6qiWWtL3IdAg3E68rT5nkYEyiemYhmc_-faQJlaQ6S-WJ3BCdrfBZ7ucUw953LdkiP3OJntKkBhWczw7YfIfXPsGwgSP7sIk9iad8HABE1dH6Je4Sbi48xdwLL7-uMAiO9e8JUQJWhYDfEsgUhTb3vTX4A4zfsLb8Tl4Mmf8_PU4acqT-rxAtuASX7HWuqUPN3ZA-HpxInKnGKwN23pJ-PhEtaatP5slrHO-Eqyua3ZZpAs6S7pAlrwngKgEuUS1PfjUDAPC8y2bptEf0BkFGfYoBkGMD44XYHOMzkl71NRL_U8TVfVRIV_rcvEG9nYmp0o2dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1o1NlphwFbFPSYwZoPW-sizBiKwuRZm5JOldvFPQGcotnY4B9IHBgfptmuMwivmsLCy4NwgHD41ojo91tGCgJ4mob4uAGKhf6a1b53uJC5TNxVnPgWwZpR2eDFkizJ69EJW3ObKKingsy7E0lDHuK9wgy74OlHHVJT7G1e_5zEBULKMS7G6o8vF0pZy977zSrW5DT4WlIStwhwVIjQj_OpF6gBBbRvPACz_OnqiCLPgT3lIMD65THyi9dUEzhK6DBHKj4CqStQ-uqkAWncE2zQq9PyONzZSOyDrrE3l8XWo5E7PXi-hrUBPtdN990f8rH8DNpnE1bJbLrXF-QP83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4vBOdc0gYBOVIK_sto26poU5B1Djmit1kKVWFDIdvOX4kTsO8LqkDD4D9lA_YY_mvJDTCy6w7Hoirw7JtmvkXqBHtcPGH7KLzLA6BIC88fiJxkVVez5j2Qwh85gQpSxVAlJFVjPTrKjxsYX74Ng1ZmgJOtigHEM7AltPbBUyeWbDmvRukvQEOqOr46rXEnTFiPWy_ygAToK4JQt6bKVX7KiWgwHvoeRROUs230hNP37JchkMYMMAA6XQGSyauAGkC6uYFTz1XvQlDgGkqSpW8ZJLzQpNtxcEq4V40ePYToD2G7rWv3YwrZw9-AlUlZ_WaIj_ndTHdTCjcpLYBaGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et0IVQMa52c41TS1hO1kHwV0zBTwW3f92IKY_F-_6Q0MCnD8RyQpK0Um0g0kfbNQXp_uwBw9fQdj0N7M87gtszhjLHPTSJ-q9iU84mKsHdVDNGvKLOOQL44Pp9bO7Eyz1Xo71DtfMi-YSNc2lDdBJsuyiPCL8UhPgN8kwkzgDh1VVAahFv2-jNXn6PP0sy4-Py11V9348YpInfPrYOSdZo9esIq0eFxMoUzqsIpcR0SvH3wy1xTfQ7GwaZJPwFOedscdpcsi1W3y4Bnq70GiQ8QXWj8vucbMy2E3iwdXgxVt1lYdB9KZWTPX_bWjCAZyVvNp9bhv0vXEp2a0dkvx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
