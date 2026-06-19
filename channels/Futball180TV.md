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
<p>@Futball180TV • 👥 672K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-94344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3P_xgzTi4Sfn6VgZwXYqK2BB7XoI-tfZN4dClBzL5b4lSkdsry4YwUKLUYa3577pGujKogk-PCDBWDI0Ei51VrGji87_P7Mjujqs0AQ0osdyg9Q37xE0-v8msfkbpb5Js7YH2qBIU2Dlc6oy8d02cGGNkNsTcAuOaXYW5NJvsReOGP4cRG6vB7T9YvxjS9XeHxEl6jdErlRksxVdQb1mIB49d6dKxnhWiZ12F2RtWQJZQjlB-WTHcJ2pweydRGdxkshvxJoOgHu-Dy83Yr7NN8za_0E-MWXh5xut4pPj8mcqvPbadbghTuVNY4h4viHW9cdfr9ryRI_ejLlz7Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه B جام‌جهانی که تقریبا باید گفت قطر و بوسنی برای صعود باید برای جایگاه سومی تلاش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/Futball180TV/94344" target="_blank">📅 03:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94343">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/94343" target="_blank">📅 03:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=mtxJckcfTYWJjDnc4iUUYIC2VP88_FKKL9QGM-pCHRPXFYa3fTUeEek-O6P9N6zfQySwuqTdpY2vOVBaY9WJ7GewXtEE0oLm8gZvgm4d6X_S8Xz8YJqc7s67Nh7KhchuW_3uwe1LNZ0JbuMXfyfQAVrcblKg2dRWmhAbic1JbseDpyu_AdggBg7n7kYcwQgIHsSYwMDv3ifAi8w43YHmTSopqff_UTyfXtT1ugUKUUdnweo6dY7sojPtu5iVQrkzZ6SIyjQO0ODHCrYSarJsjiRqDs0iTtyAi-u8Nh9s0zGaHuuYsGdJmSwUqzz9TwsgwkAAPucqImylF8GHRzZF7X1DmBk-Bt4ThoQZG29Y-j9pPqUflswNX6ieR3fQ8PnsCuLbowDwQ9ficfzEkxA_y0K9W5JpWX-jt7cj8pzfsmnj6plb8GXPMKwV9_oHGldXNTCQyo115FqGb5Bv1aTSHUQ1Ugrq3n87giRpKy2XQB_RWWzCJtD73AbXg96hoyfWSrS8XB7MT_u-oDPDdZEITVkCqQuWC6gIWcby5OOOFPNAYMWiE7VxOp5motrIDzMTbB7si6VwhNHpjFqCNLrRXVjRLb8r_oMiU0fcUy2DUGyfKCGOlUnTjhICUakvW2F70_HJtKzxhwlOG_SPs9qKCZc6-QH-z6QoA7kdUMDLXv8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=mtxJckcfTYWJjDnc4iUUYIC2VP88_FKKL9QGM-pCHRPXFYa3fTUeEek-O6P9N6zfQySwuqTdpY2vOVBaY9WJ7GewXtEE0oLm8gZvgm4d6X_S8Xz8YJqc7s67Nh7KhchuW_3uwe1LNZ0JbuMXfyfQAVrcblKg2dRWmhAbic1JbseDpyu_AdggBg7n7kYcwQgIHsSYwMDv3ifAi8w43YHmTSopqff_UTyfXtT1ugUKUUdnweo6dY7sojPtu5iVQrkzZ6SIyjQO0ODHCrYSarJsjiRqDs0iTtyAi-u8Nh9s0zGaHuuYsGdJmSwUqzz9TwsgwkAAPucqImylF8GHRzZF7X1DmBk-Bt4ThoQZG29Y-j9pPqUflswNX6ieR3fQ8PnsCuLbowDwQ9ficfzEkxA_y0K9W5JpWX-jt7cj8pzfsmnj6plb8GXPMKwV9_oHGldXNTCQyo115FqGb5Bv1aTSHUQ1Ugrq3n87giRpKy2XQB_RWWzCJtD73AbXg96hoyfWSrS8XB7MT_u-oDPDdZEITVkCqQuWC6gIWcby5OOOFPNAYMWiE7VxOp5motrIDzMTbB7si6VwhNHpjFqCNLrRXVjRLb8r_oMiU0fcUy2DUGyfKCGOlUnTjhICUakvW2F70_HJtKzxhwlOG_SPs9qKCZc6-QH-z6QoA7kdUMDLXv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌ششم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/94342" target="_blank">📅 03:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جاناتان دیوید هتریک کردددددد</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/94341" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گلگلگلگگلگلگل ششممممممم</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/94340" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94339">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/94339" target="_blank">📅 03:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQjTYPaBZ9IvDsDh5wwf9hDJknrhoXqU4cTsC5HtDpn32RVkhG1Klj6-R5QbND12VqgiBhY6pGsczkVb8PfQVrYQslLQx6V-fK7m2WuzEDp9Xn3hwb2PdTK1cr-ClxkjjT4N95ne4GnTiSAEvetXhriSP5j_oA4z6g8ndnp8ajxLUfL2Pr1GDUSAJrS_kc5TwxMhhpG8Rt8mjpIuksafZv_lcbnWI4z6jojfvcGnINWWal6XmvmBg9sYo4I5--sJ5salIv7OyShfElPYxH9T0vwyoauxqva8ZIAlu1ei9xOZ6AeNKCSLhbZ39ToFnyOWVW9nodkLgLUADtSfa1o9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxggmGsASc7F7q4RuAxp5J2XaLM6tXrvNrg_Ja9YMD6dM6Mvmtbn79LDYBlEixS70Z2iXYZeQdI7MCtDSBpbyPV2MPbNhwVQ78idnCJtOP1fruOnbuNQiJ93Tzn6UOMrWxqFEzyB67oe8ImzbB2PdDPh5Qw0MHJLWgiz-5Vjp_5-wxj7e_ed7qFQ706meA20e7gN7JepofOGJE_1u2C0AQyDfA4HJtiDriXmM5XBljg7wl3H7NldJ8Mora1K7X5xAzqsd-G4lQnz5UZ2l-EQ7r1acyBoTrGro8CHNZyuqKEQ8RG3A6EyaRql4G5ZSObvSsrJdGwsuD8n8WypmG1w5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ترکیب کره جنوبی و مکزیک؛ ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/94337" target="_blank">📅 03:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94336">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/Futball180TV/94336" target="_blank">📅 03:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پنجمییییییییی</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/94335" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانادااااااا</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/94334" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Goallllllllllllll</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/94333" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94332">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/94332" target="_blank">📅 02:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گاگلگل چهارم کاناداااا</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/Futball180TV/94331" target="_blank">📅 02:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94330">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/Futball180TV/94330" target="_blank">📅 02:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=eyi9bhw6TL-6aer-XTz7VI4ZleuP7rSeX5wCGeC54727GSSdJKRMZCWppNJOqKxJMiUYlhTQaVa-TMLFWChw1JMz1yfEOl92Hla1Ck9HDbLhmft0R0WwOI0su3610xZvEBSIxNroDMtTbdjP5jmkGqVlgabge-I_uVbp8wGyGvkeMjv6ZFmxe727l_5I2WEquIx9kHeDO6DK1RYBLSEDF0BaKkNRKyva6TCllMxhXmEWT2Jgl15EiKiUmgoK9m81gbPpb-TwcntKv4q5uEbxTpBYcPF7tD6KWoWmJH2rXQDdr7hGxAybX-c8rGmGw-WXS6kigAzSiQ_5ihAQZ7J8lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=eyi9bhw6TL-6aer-XTz7VI4ZleuP7rSeX5wCGeC54727GSSdJKRMZCWppNJOqKxJMiUYlhTQaVa-TMLFWChw1JMz1yfEOl92Hla1Ck9HDbLhmft0R0WwOI0su3610xZvEBSIxNroDMtTbdjP5jmkGqVlgabge-I_uVbp8wGyGvkeMjv6ZFmxe727l_5I2WEquIx9kHeDO6DK1RYBLSEDF0BaKkNRKyva6TCllMxhXmEWT2Jgl15EiKiUmgoK9m81gbPpb-TwcntKv4q5uEbxTpBYcPF7tD6KWoWmJH2rXQDdr7hGxAybX-c8rGmGw-WXS6kigAzSiQ_5ihAQZ7J8lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/94329" target="_blank">📅 02:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUmquspf_PFxPEgCI-jH1G3jMFovnfCo5cpHfHKc7EMPMIYeOLTDwu1Pbq71Y8r3qsJfLjUyq260Z7jOdzhJgSLCwZnSyMRudIasXg67CC6x5VJnYHOk2p9Wkf-P_DfarJH75vePy1kro9sesVjmFsQsHMH-5sltv2ndfoS6emzca5jO8HKHsx2sV6vrwzanq9wAnkb--WlA7Ymuhvrvo1skFWqKEc7yBJq48YoPsli1NJZj_nGJodx1gzOkqwGSZ9IzUpkMBjEOUidJOdEfaoH_wOBJaDE5KhtSXGjV5LD5P5mD0qTod-GpEHqOvoDPOBj1HEf5D_gYPlZwdAzTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش قطری بازیکنو بگا داده زبونشم درازه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/94328" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzuMVgxUwdx5ung1-sQlpZ2cgt3KnWlLNlGiO4n0wFbyX-7CpBZSNqLzaucwclwNMJCxUMuEXIG5k_RFAWQrilieU7cCidHDyzFGRUUW1LX1cULg6PMcosTguVccZ0qDEoVAgdzF8k8A_I0-k_y1Cm81foKblyUchlvvqRjdUReebtZQWMW9xsEloE2fT4cpb6Aigp5QgcLMxfZNti6TKQnNRXzunq1lzF0oY3u2DFBgZOKlXSI7BiBSHvtj98It3hwcWT67711xqKFkTXGGiDtjvR_6YkQm1rSSuW85UMCC9Xd9ZOzSG_QpcU1PkqwUzO4PicHJvsSVDhv3l8XoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ریدمممم حاجییییی شانسشوووووو
😐
😐</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/94327" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtmoaC8m8FqMkC9ltpJGK0ASLAn-tCLZICU9Hd2cmHIpPye4ntQGv8IO1ehK0arGWkj72SroD97F9p0mjhGIBPCZCIsjTqpegoluGRiKNL-9HQwcwFlVHuJEKYs93yF-U-4tHS5nqnEpqZle9caqBYxIIn024itCHS3HgnvuMl08-qaK6AKU32bJJgPlh0X9Gcsti3-CeBdQP6wWE9qWazkr995CAg1SxnfgTPgdTEj4omM0Y5ph4_gD9cUq2OzL2Ese20BQ05SGPjgA2WOYlqg6ywXmxZbaNt3Mf_mPjSigdDkUYWH-dd_WC4hq5m7NWZi-SNMwlcJNKrtsn0b-KQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94326" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بازیکنو با آمبولانس بردنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94325" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBdDV8rvzb6QxAWrR2csf0_IMARgkcytNmKJgs_5HiJReg77wbpGEwigfG5FsLKr23PfqkNE21tUQIsn4ck5DbsUYxvDpkQuiAJif0VKnOspS0NTNDXwF2_QTgplPA3P9QzciKTB5Gp7ucCFfr_-l6H8hPIA3vZ1WJbDpCcI-OsRucWCsMPReNZzQTe2jTdrBHCYbNGqNSB-tirLXcLvbidGWyLxCgycW0t6P5pZmw7usXPR9IIHpYbOUB_6oKI9wCKReEOcsTqsdC9yGTnBpDBLdguhBfXSjvCvJS4qgDGYCoBbL79Eur-ll4rm0g7oyEkuR1p5e4DeDUCm4_Uvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دور بازیکن کانادا حلقه زدنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94324" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🟥
بازیکن قطررررر اخراج شددددددد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/94323" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
😐
بازیکن کانادا بگاااا رفتتتتتت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/94322" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94321" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لحظاتی‌پیش نیمه دوم آغاز شد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/94320" target="_blank">📅 02:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پایان نیمه‌اول بازی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94319" target="_blank">📅 02:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvKiI3eWxKD4Oyw22DSDnOwRMvzkxldvtAFVKhtnjlEOnScqqZclfK5oXyHq-UdYogVEwcp5XS8q4PWFzUEy7OenoaWG_7ol5rADVnGZQk2s2okj-WtWKEj9wqO95XokowefNzYVw8y2CLseDVEBcp70QBN1kq-RdjuZllffn-WRsG9eXx-q-0BEpIf5jiN1cCuZTt7jc6NVJR7lz51XvzRosEHGTGI94xj8M7KFAaCOCOb2hfYE1jW_JibFNhHJEP3IM0zK9ViylorUOB-HSB360yFmF8aImvAXXRScHzo5jGe6o7XpZmFeRpB3mwqzTBuaTjPeLAEzRB6npxQNNzdM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvKiI3eWxKD4Oyw22DSDnOwRMvzkxldvtAFVKhtnjlEOnScqqZclfK5oXyHq-UdYogVEwcp5XS8q4PWFzUEy7OenoaWG_7ol5rADVnGZQk2s2okj-WtWKEj9wqO95XokowefNzYVw8y2CLseDVEBcp70QBN1kq-RdjuZllffn-WRsG9eXx-q-0BEpIf5jiN1cCuZTt7jc6NVJR7lz51XvzRosEHGTGI94xj8M7KFAaCOCOb2hfYE1jW_JibFNhHJEP3IM0zK9ViylorUOB-HSB360yFmF8aImvAXXRScHzo5jGe6o7XpZmFeRpB3mwqzTBuaTjPeLAEzRB6npxQNNzdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل سوم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/94318" target="_blank">📅 02:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">درحال تجاوزووووو به قطرررر</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/94317" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/94316" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گل سوممممممم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94315" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگلگگلگلگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94314" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قطر ده نفره باید نیمه دوم کون بده گل نخوره</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/94313" target="_blank">📅 02:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94312" target="_blank">📅 02:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh0IDOlv6Sy2PTPW2kvhZ-ucHEd_KWbT72VgTGWpYqH7MIss0Vexvsx8B_gGtHDsKU0ACfZ8M9Ho4jjDXfo0SheS5ouedHYle-2XXpfvdfYzKwKsoolEz5VylIH-wrKf9hLc_nQ4GpA9HPjWDzyFfQQ615wqfFVtdXgEbjUOOkWF0q-IRwKgYUbindBP18Z27IbXB82kdnpf1c7gSKAG215MJMXfV63GgsHdWTnJ2tbLFrWK7vc6_XlGeigvgqws_ui0Hta13e7HnZd-cBQZDXGkbfhFqtgZBItMi98yGbI6wByhlFcpiWM1uMVOJdXvSEHONWjRHSGMGuGuwKqUKSAc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh0IDOlv6Sy2PTPW2kvhZ-ucHEd_KWbT72VgTGWpYqH7MIss0Vexvsx8B_gGtHDsKU0ACfZ8M9Ho4jjDXfo0SheS5ouedHYle-2XXpfvdfYzKwKsoolEz5VylIH-wrKf9hLc_nQ4GpA9HPjWDzyFfQQ615wqfFVtdXgEbjUOOkWF0q-IRwKgYUbindBP18Z27IbXB82kdnpf1c7gSKAG215MJMXfV63GgsHdWTnJ2tbLFrWK7vc6_XlGeigvgqws_ui0Hta13e7HnZd-cBQZDXGkbfhFqtgZBItMi98yGbI6wByhlFcpiWM1uMVOJdXvSEHONWjRHSGMGuGuwKqUKSAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌تماشایی جاناتان دیوید به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94311" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/94310" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94309" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوووووممممم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94308" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/94307" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به قطر توسط لارین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94306" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94305" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گگگگلگگلگلگل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94304" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کم کم بریم سراغ بازییییی</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94303" target="_blank">📅 01:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prq3VHHwgiSb4wdDECryJyNcUwIFw5zGSQXX1sGrSGHfEA5aAkQ-j8z47PTS71Vutj97Vcx_som90S_g475vWD8G1YOHjn6eci49pkJm7ecFVR85Y5x5u8gd1BkPQJ-SeYXMjcpXucf6cRZcMxwn9RkO-9S5uVTRZesf7QFj570-nqt1XVIKK7ohANE7wFrTI8SM8Ycs0XdtNXWZz_TgRkKYQXY0mFjpyN_4j8bqzEUfufcVUh5Eo_Iqjz8iYUVukisGmyMOauIXfB6ItQLxOoofRl1mDFsR5BWDcJPoyw-SkVyJnRLGk3_DqbDZj7UVHnzXL8weaYiUCVYvVuIArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇪🇸
گاوی: انتقادات نسبت به من همیشه هست اما بهشون توجهی ندارم. اسپانیا واقعی رو از بازی بعدی خواهید دید. هدف ما فقط قهرمانیه و برای رسیدن بهش حاضرم جانفدا بشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94302" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCUi2BIT8KaOWH7XECOd79c7An22B1aXvKfabS7zzU0FFyVqsthqxmq4lFpt1JVvO17JUrbo814JyMXMnRupE3SEoFjgB5eaVgafuGCpJyXNgugdwGgqsMLIr03UXGB-5rZf-4ypKOi1gXYu2MWHM9u7swkkA8HsFL_S3gjnORyUiebPL-6j5FuEi8xwXqKRDXZ8Hw91y6TwNyNqygB4-X9VyMNJ3E1Ti_muJwvJrC0mswnNGd6f6fGS4RuNlTuP8pbtj2GSzfqA6mSfIUiARCdIVzwoi2L_zeE1dUoFWn0ROPq-QAQNF7CmNS9PRV40j_50HF_gZNgzC28uIDaPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
دنی‌اولمو درباره انتقال کوکوریا به رئال: فکر میکردم به بارسلونا بیاد چون قلبا طرفدار تیم بود اما حالا که خیانت کرده باید کونشو سفت بچسپه چون فکر میکنم لامین یامال راحتش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94299" target="_blank">📅 00:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq290afVd9cVgr34Z56kOUR9ujS9QpORZDJNb1ZUgcmOmMN1oRgwjRBDawgvkwlGmxCSx7Ju64p8cjvOObEftdDSUN_3LTvXyEdYfn4DE026MgeDcdTFST3u9svo7jQRzdjhXn3VZv4PPvNF-0_BLwb95WXR8e8cZuYVNFQGe5VE9ldZNqTH-VBGURgDUdaYlMNUcZhjYa1Vx-Yjl2PQeq-x3KYdCugLUVGkgRbXwnfyge-1bs8prI2sayZLvg21pVSKNP7SWjNVnNNA2BEI9iJqUdZnA9tW2ZAvPnkNel3UPgCXMAmX_cVrHemirXTdzhLA1cq73dL0FPfhXLtyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آرشیو VAR:
پنالتی سوئیس به اشتباه اعلام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94298" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94297">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O41IpBm3bD7gsLjuEkwhzR6qLsY-YBTEQA4dX_y7jhmLWV-GdRR4C66dlua4eZyr3kixLzyQafDgeRB_OaKvSGffZVOs92Q78SXs114_qXPtsxikoeIhQGhTR76rMqAHk4bo17aNYRtCFe56eVaDOn8jf_PubLrcYgYWXRkaAATltJRSFg7gPsEGHPe49ObEwDEgIgWXoaSooqWhTzVYvjQEl3lNIP73jTOCMbrUv-KJLJ7Q8wfw5-ETV6L6A01AqfOFBPX7lq4QgrJq20q0FyJlEu5vGT6M2mapT7KE20lLT1MQu9dZ4S_FyNZaWy2_haSHXwR9TY3WRnhGKpo1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ یوهان مانزامبی (۲۰ سال و ۲۴۷ روز) جوان‌ترین بازیکن تاریخ جام جهانی است که به عنوان بازیکن تعویضی وارد زمین شده و در یک بازی دو گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94297" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94296" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlFoWqAdseE4yHapPRADZ1Uf_OTCoX_1UDLAGe0o4QiT8vehnevOt-_8Um5JG65VRtKLV6B2c_048eGhIIk0bFfmsI2AjRKYkElIU6-J8QCv3dNTE58y09zmkyP9Qc016YoydoqbFfBXHbq0Sn-YzCMloLkGxSXU4xmNsb_FsY52jK5hPODy9FYxgBmU2PtxsVBpQp7-oGarGJ8hgCnwAzskRmNX5DHbTUDhUunomkD6hmRLQLMJgdnBMrdzbf-l83yb_W_dKSqQQ-q8VoyNFj0QHAufTifFik9QbkFRbEqXyq4M-kWLQkcYEvnIybIOm_OPMBc7hZMvPpm_FN2q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94295" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ4FvjB7lusabPzCk24bOGEaWB8dIKBJKntj6PXEUztdgoByv3kn8DTnv_-bS1fIKXDg6evMUS5r_4Ze53YyLCCtSj5DSkN67BuoojZ4H7BVdjP-fModHZHxwpHvc6S2ORuWm_eccbm2wNKNwIA1BRWwTLY9iFz7IFtC7I63GtJqxSMLQvTdepRHw3OzbK5Iyh0dpByfs-NGKQZezSlxR7xSNGmpzydYHzM5gSOSMrxeqRoGvm_ZdRAOyjO0lccEdfWxL6S5kYEVkvMQ6OaweaFFH6U1IyIut7AOg67G0YxYYAQNZO-h2kMPDo-W7R-c54pi2hnCMuTO3dzFLTD5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تا اینجا جام جهانی 4 کارت قرمز داشتیم، به اندازه کل جام جهانی قبلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94294" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyl5ihN0EAhXsPyIjyoHFLAlFHvnK9MoUBU_2Uw05xkSHZfb2mCuJ4LSOEycepoub46JMFA32SdOpsYUw2DIeKVI9UmS8kBm_Ae4aaLBBoI5DiUFE_GfO5ubmm_QxU309R0N64q6JrlL7yi5rDiF6EiyXo8J9fZ1AAO4sibRxhqf6AE5McZoifDdgs8HYeMsxp2E_7DP-q8jhZyijvIG3Dv9LR9hRBaLhqGyI50TTdHgdsjpf8fvDIqlEbTSz6X_rABIj4f9N-l5ADdJluPkobuj2GVAsexVB9mOTubc8x7UDZYRVajmNvNMDO0JMtaSOTNMugB2aqZtxgHwZgtYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه تا دقیقه 74 بازیو نمیدیدین چیزیو از دست نمیدادین ولی از 74 به بعد:
◀️
دقیقه 74 |
🇨🇭
گل اول سوئیس
◀️
دقیقه 80 |
🇧🇦
کارت قرمز برای بوسنی
◀️
دقیقه 84 |
🇨🇭
گل دوم سوئیس
◀️
دقیقه 90 |
🇨🇭
گل سوم سوئیس
◀️
دقیقه 93 |
🇧🇦
گل اول بوسنی
◀️
دقیقه 97 |
🇨🇭
گل چهارم سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94293" target="_blank">📅 00:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8sGGO7xq207MQoim977vkrtkkIelnLWBLC61StsKy6E1q6ubk4nwrgEEGIjDDfsytlFegva5GcdcjtZsNrY-JX6Ms3Em0uzIimFutR6-N7iKyB0KBc3mFhdTcWtfwdfNvIHWCBYuOm3IFC4zt5b5NbnViw3siDsYGZooCNij09Mb045ozRwk3MwHgbjW-tjYv1N5q9G9Bin6OcD2LqeXLMRNOgCq2fyLN8sG3ttMODYMGTL7z6_RfNUXb3veNnpg4gQ8toM00b0kmvarap0CwprdKJx7Sddj4HrxmoZrcg7vwOMimigyT4G5kIn24EGgMT_dR-AOB4liJ-WaJgnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یوهان مانزامبی به عنوان بهترین بازیکن دیدار سوئیس و بوسنی انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94292" target="_blank">📅 00:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94291">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlSfONj_LBsmYn6DPWEV6bLH_7LjeeMUqgcp5zdqZOQo1TFcmOAiCvqCZDLTA8OtED7ZLg-ZviV0WsZZvKGoFYGY-V5CxAOGbIvbH3FPYOcPwzC29YHh_oOUAMEENRTvaJSJJslyXxadHrrlNPBXjCiPBXUcGAex1v7pcEsIUh46KxgV4nnNGBBC-pSLBfIH_WgB4hLGe-sbk4-sWMmdPPT122l-iz66mn_8spJLDobknHWz8TvDjqoDiQKZP0m2KQ-9ZiX95b616fhiTd2J7GdsBkUehWLLLPTnB46fP_vlQa0QnVNThseR8nmyNbALfF9rYF6cB6LK43JXJloTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇭
📊
سوئیس با کسب ۴ امتیاز، طبق آمار شانس ۹۹.۸۱ درصدی برای صعود به مرحله بعد داره و عملاً اولین تیمی محسوب میشه که یک قدم تا صعود فاصله داره. جالبه بدونید در این دوره از جام جهانی، ۳ امتیاز حدود ۶۶.۷٪ شانس صعود به تیم‌ها میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94291" target="_blank">📅 00:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94290">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E64l8I7htdMJ1oA27hbIe9wN4XegMxRD6FkCorRqddYUtQMReSaun8Mp4OYZDcA2M2Fr3PF_1J833TMx7JqDHVXDNUJGChV6ZvTD5u0CUKZB00wwyztwYsjtE01IXx3Iw0MRPSuOpDgkMhVRP1UGMK5I6XTt1eYABEX3Qn_OYtLfY0Io2alZMrSEY5o-8zYC4QYi0PWvyAhHDAZoWkHAbFYhUUjJ1HxB4Ls4ZP8iq764ZproJN6wGtmysdO7Q6Ut2_w_jIx6Hxm5pjtMlMuvAU_av7cNTpmDqYsjwnwN1ALQ2h62-S9qwhHpdEh0_coAOaMQbiDh_FMVSeDQ8t8Now.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آمار نهایی بازی سوئیس و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94290" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94289">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY4QP3uA_4_GSbE5HAbaXxoCxjgkOsuVogRKKGaR3giH32DVg3lgQfM6M6mkRiD2e9xeg18ksq5OqpjryCvX0Lf8kzHipg7Ll6CfuqxNdzFTI2O5WczpONuDl0YHW03o1MVmUGwTaQA7qwbzvaTNFJ-FD03XipTcZ0phb3RpEwBOCt4Jd-vpX8ghixh4wTSWHyC7mq2SKxFaNh65aDPvrP4FZzCWZ58dzUmh5SRhwVYjktVGgYS_s_qO9IjJPFroJs5evi8xy9jsAYmcY11S8tvTHjU4FciSJ6HC9csBn-fPoSKUfAgzdvf8zyaa6URyhDIH6BnWAG7hsJp46A7wIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|سه امتیاز ارزشمند در جیب سوئیسی ها در شب گلباران بوسنی.
🇨🇭
سوئیس
😀
-
😃
بوسنی
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94289" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم سوئیس توسط ژاکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94288" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سوئیس گل چهارم رو زد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94286" target="_blank">📅 00:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94285" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
سوپرگل یار تعویضی بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94284" target="_blank">📅 00:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلللللللللللل اول بوسنی</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94283" target="_blank">📅 00:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل سوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94282" target="_blank">📅 00:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مانزامبی دبل کرد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94281" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سوئیس گل سوم هم زددد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94280" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=OOB8hg_3mcn7E1PKL11QU_s-O9SR41bdevbHVStJ5ae2DUhOwyaCLzz19UP6u9n7ENtabv9OSIeTfjMcmTv0gZ5CkKhypF1YkwQA-b8yW3EIKXZmZwlDxKEBzuu-uY06bUw_nxg7Z-jZPyu-xz4PqRh8nxb_8jYceBxJTTj7g4CsMaoXaSy41jlIjb73gB4sAawqDm1TZse8aVySN-b--L33ak1_6bEOu0OF81L-jsKK4VzUlRfaAh7bdEJvDro0q-kG5icbaI-yqCUjCFxB28xmHPDwEK0yJxkRa-brYSdZmQ4pzALR5Nx2u1a6g5cmfU0NAYksShVLTAe34PaTTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=OOB8hg_3mcn7E1PKL11QU_s-O9SR41bdevbHVStJ5ae2DUhOwyaCLzz19UP6u9n7ENtabv9OSIeTfjMcmTv0gZ5CkKhypF1YkwQA-b8yW3EIKXZmZwlDxKEBzuu-uY06bUw_nxg7Z-jZPyu-xz4PqRh8nxb_8jYceBxJTTj7g4CsMaoXaSy41jlIjb73gB4sAawqDm1TZse8aVySN-b--L33ak1_6bEOu0OF81L-jsKK4VzUlRfaAh7bdEJvDro0q-kG5icbaI-yqCUjCFxB28xmHPDwEK0yJxkRa-brYSdZmQ4pzALR5Nx2u1a6g5cmfU0NAYksShVLTAe34PaTTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94279" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سوئیس دومی رو زددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94278" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/94277" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بوسنی ده نفره شد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94276" target="_blank">📅 00:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94274">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qN04hlktaHr2PE_dHSZVVK-D_wG49bRa3sc-lMwwOEH502gbn4tHgv6IzdK92AQikOx8CUiSmhqJfdxSiPhvWl0f6FsMPLktNPJ4S6fJ3tVtbgsjXPuhC-BDsrFrBGClsNJEbjr2rgmrCkBJ8RFvazevf_fRe--hsK1T_7kDPNpd0eaE1P7DEt9hDi3ivw5VlyhbTxcPO_9xK4lnw3x3qrB5NNA7RPB_hYm4iSY4d-ui0V2Ix5Gihpfn5YE6KbTQJBXU7wira2S2lnBEil9ziH1AvTeJcVwX6gk9zZR-IRXwYZPgTk35y3jGUiJvknBC-BHcEhtPQEwdOFqSN6B-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmWPhbee10rfD_azgmkLTWsFueaWaA5_NkNC1Q3yfDj7uV98JJlQIKlsnq-vxOd_4SSoQcpVvr9ml1GX4ii7IHWm4PUKAffh04K5mghKSc9_EX0qoXWOg8qZSjik34XFjIqW5qCWZE_vJyO_A6eMom_k4HITPpuPew2RtQMjKtp_Ya4_ApEw0d52ECX-BMWR1uk8VPteL9JagXRU8rTCJcj8AvL4tUdEwAb7UIwfTLdeQz7zvAILBg6pxo6cygBMLzm_xf2YQ_5pqTUax5w-j9iB0ov5-OVC0QkY9BSKsZw5n0lWq1UQ2zk3cW9c4l-rBd7DyFDYfvB1JP-01VGWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
🇨🇦
ترکیب رسمی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94274" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94273">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04d0160117.mp4?token=Xtqx483wg4SyW48Y7tzoQRz0KiD4Spd8NrrFDrMI0yK1L93AIaLMq6eZtgM-zBhUHYOE7BmyYR9cX_F4JnxzR_MOnSPC7k2Y67XXOBIiQT3HFgaSIxkMfB6AVfY5SWfAzWPnFe1jkG6uVE2sPwuS4RLBJ4mxUUL2EoU5CtnglsBN87pvbH926JBfNRQepFSoDb6fNKh9VFqny3mww-8AeZDYZBddeSLpPj1-CzWzipQW6FXI_hQx0vgOksnKbpfdELNf2qQb7pJH3ngX-SwfQ23rT36L6DXv8dUN5EXSErU2lPcu2TXwOSNpCoLGmq4sxiAjFOjkXBaHxJYSq28aIbybFS83GCT7PJFR1zax8B-WqoK1tLTqnKs2DGqC5qw_vn14DL_rqx3NbtdZVnNNT3nRIUkJ6D0RpLj1HmOvhKFXoyK2tmT9oAWIjlM8yij4Tu05nmnBCVA2zEcax0XXCGdYLVkWJ3Zeh7hHLEHXuZdS5a65bwpyxGUK-sCBHW7sYsqlZYMv4suaAORQNUSO-Q5yA4NHZ7cTLvXrtL9vO3ktJFyxuDArA5janprMWExA7ZW1HsEPME7AQyQL9v2WQPTMrgrV5YYraTYTglKKWNdqfZ7I2uPElZ7qdYNn9LBpTb5SuEYoNJ01ttk2op_W94Bqo0xFgScWoNyVg07ORU4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04d0160117.mp4?token=Xtqx483wg4SyW48Y7tzoQRz0KiD4Spd8NrrFDrMI0yK1L93AIaLMq6eZtgM-zBhUHYOE7BmyYR9cX_F4JnxzR_MOnSPC7k2Y67XXOBIiQT3HFgaSIxkMfB6AVfY5SWfAzWPnFe1jkG6uVE2sPwuS4RLBJ4mxUUL2EoU5CtnglsBN87pvbH926JBfNRQepFSoDb6fNKh9VFqny3mww-8AeZDYZBddeSLpPj1-CzWzipQW6FXI_hQx0vgOksnKbpfdELNf2qQb7pJH3ngX-SwfQ23rT36L6DXv8dUN5EXSErU2lPcu2TXwOSNpCoLGmq4sxiAjFOjkXBaHxJYSq28aIbybFS83GCT7PJFR1zax8B-WqoK1tLTqnKs2DGqC5qw_vn14DL_rqx3NbtdZVnNNT3nRIUkJ6D0RpLj1HmOvhKFXoyK2tmT9oAWIjlM8yij4Tu05nmnBCVA2zEcax0XXCGdYLVkWJ3Zeh7hHLEHXuZdS5a65bwpyxGUK-sCBHW7sYsqlZYMv4suaAORQNUSO-Q5yA4NHZ7cTLvXrtL9vO3ktJFyxuDArA5janprMWExA7ZW1HsEPME7AQyQL9v2WQPTMrgrV5YYraTYTglKKWNdqfZ7I2uPElZ7qdYNn9LBpTb5SuEYoNJ01ttk2op_W94Bqo0xFgScWoNyVg07ORU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94273" target="_blank">📅 00:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94272">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سوئیس گل اول رو زد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94272" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94271">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/94271" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94270">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtNPydC9ktX_UbGw9GNdD58jVNael1kczjTRY1szXv2QLUZGpcwWhaf8EHvE8Mmo0hqLROqe_zZ8gAZ5XYvcSoyI57ILhoXemFuH2zxkwkLpZKsRKOOnZ_H99m9F_njoFsK0fYOfGSpPEG0GFe615xOEdDNQMo_qbZnyalPKFa0P-8D-at_mYelYv1lmgtC2xFymPXAczvWR_CPIggA9Km99HXqewfgm3Q5oF6JH6hZqR5lbMyuuzYTfqJX-F6GaeUN7w6EVbj-qDVsVYyPbxr7hBmSVhwjqB7JDXQ0iKkxnTwRNfd0O-ozNZqk2xf7ClDb03VfO9BGGc0cQOdgUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گلر کصخل کیپ‌ورد 1.3 میلیون فالوور میخواد تا به تعداد فالوورای نویر که 20 ساله داره کون خودشو تو فوتبال پاره میکنه برسه
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94270" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkI9r8UQlWPSp5lRDSo343iffYCI7Fw1zKdsOrjMDy4kEtqBqMJ4x_A6TU6OLXNy5UHzW8YDdyC7cFRuBzUx7kTfgTQ7Uxev0xh9rZA8gsC41Mv_QENpRZaKDWNSDeZRU0nZXMS8KoycoMTez2EFn-juJAStXMAocLb6q3tKJXXNivuxzo8T6N_ZLe8b-q2XHq-FO1XiaLqBWkAbOxLVCx7m77K6rclfxaDkitVTUvTY7DAdlaTFxuOJfh_QCVU0m-qMMg32LmaXf8wereSh2E75qNLgS0qRSnotEibIGoFx9QSjiBD-ucl2hwCLcPZBs1UAAggT1u5Ha3_VpLzfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
خوشحالی بعد گل بازیکنای آفریقا به سبک رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94269" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqYyJRSMnIcK5AUluAGN3-y_mMuzrxOONn_2owy7QuhmDJ0NIpbJyfTc3jc_ZuekBx10bJtQiOPDGvoi_-pBe-tQ3gheCObII59cs8JKXAFvkXyi7eC-WQ-g4N7oOeWOZFhpcoYzBbAVyU0SEACFPc2ic-Mxgiswb4hqV_jWZXn4obcUimOzHw_RSb708QNGdIzsdPy6PP3BHH2UBjicXRqRlkPYt3GygWTY_WJCQ-NV-tVVz3BBdSnHCGXOI3m8ZOi6YYt3uK5ebT6U1iJhmJFk6PJwCRW2C4yhQKmeBq_xwyaVGuK_VmO0sMjkXV6UFBEEoeiY6SXZxBj09EsaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جیکوبز:
انزو فرناندز فقط به یک باشگاه فکر می‌کنه و اونم رئال مادریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94268" target="_blank">📅 23:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازی سوئیس و بوسنی چنگی به دل نمیزنه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94267" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیمار وقتی آنجلوتی‌ گفت بره انفرادی تمرین کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94266" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWRxWgj2pfrDkT5mPtSp224gPZWGMBeKTE-exKaQ9CpfFJD6cP5jMkMfTGDp7Ysg4-OgNL-Fbeay_5xIMFcRqN8wDkkAo56-xb_M0lZaZ4PE99gvcfbUc7Umfb2ywhkJCnXrkzVCNNLhhAj0CTeir_Tb9NznKlu5q8vXXcJdsrX73mP_XmiT4GtMIRbjWnipn3EsyaiM9yJjJ-yajSlswvQlaLAE1gt19a30gP_JfkQckZhqu3Zlt_nuIrAGDh9iq2YkFhwc7xcyTfsVB9akRHk4eoMAmUDlPTGF8XVrfPSrwfcMdqgGuRpJz6RPSJ0qd7oFyahJFt_Vgslir662bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فعلا خبر پیوستن انزو فرناندز به رئال فیکه و باور نکنید، خودم روزهای آینده دربارش صحبت میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94265" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdOj6fA38SeMHnVPp9b8lncrdWn7ioUjprbvt1ZwDptzVHGyIavWlk7lMqNm8zB3_XMCPrDCuxOzgVtraCyTsUUtFdAErZDJalFHRtYFZbc-KTqYcu6EmYFfIkQRY1zVb2bzKwaNnYMv1rJPuGv_WbG17gAagDqq2yWkCbleSCgEnK529ynNwzNFYld9S6kOuBOXThvszl9pS7SCL-NZICvrgriYLJ7V0kQtlZURs64DoCwlbh_eTWu3kroWweL13R4c_JyKIQ4p-IKIXUcbtxljrQnfKjmuDqr19X8HOhsWfRn7haz1z8psnnByeDgNKHjzZa6mjHp1elfwTTd1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا پروتکل جام جهانی را تغییر داد و به درخواست توماس توخل، به عکاسان اجازه داده نمی‌شود که هنگام سرود ملی جلوی مربیان و کادر فنی آن‌ها بایستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94264" target="_blank">📅 23:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPUzL52tjADM7nm2FpEXBJbSaT2fD5E4ntt-Y6Btmq7vYrgJlMCKtf3-4BKDTSzSBNMj2fQ9dnnhv9bWARNCnDhtGLhNn01qzgaFdOA2XCiBElUZR_fsK7H5ljC7K8kHd7F2nuVVFbXl-6TmqBfW2M_d8LWOaoxYkqFPUWejuNQ-J9FT-j0o0ochaNIA6i3WzFe9EGGxFFP4R1g8hFLolvtu0SbBcebMBzhNbnMQpIAfRHOeB8QN25IbekN0EA8Dh4ljckFrBKhCGRaRZnVn4jMYlGQ-37tV7EQ9RnQpe5K08E9bCw-71s3HcruyWjVfjM57GudhNuKHNARwOTg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
از تلگراف: بارسلونا و لیورپول به میکی فن د فن ستاره تیم‌ملی هلند علاقه‌مند هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94263" target="_blank">📅 22:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss3pZurxBrl2zCLXec2IkbLO1UOEe5WKwGMkh3xgYV-QlqTke9tyPuheAmjKMKhGW1-16Smp6PyFObU40PC7z7C8PoHtoEGUtKvrwDrlwF4itKGRFFQDP4ASIC1dfG_0LhpciIx-LO11HrP2K7kj0Pupsqi0Bh-Lf9JMguCG-4HEooknwHTe6oRr4NiOeC94GYoZspyIFh6N0mhY-GXZ34ctrUsWIaVYqBrKUDWRKvODayDmYuqV1N_92px2CLJGYvA9jbQcpdhmR9K90987hPpOFlduREHIE4JGfhrrirBJJiu1iaY0j0sv9MHhRzxb9M-adj6z2UdjJo4Ip7vYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بهترین بازیکنان ۲۴ بازی اول جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94262" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
انگری‌بردز ۲۰۲۶
🏆
بازی کن درجا و بدون قرعه‌کشی تا ۱ گرم طلا ببر!
💰
اگه تو هم طرفدار سرسخت بازی انگری‌بردز بودی، اصلا نباید
انگری‌گلد میلی
رو از دست بدی!
👇
کافیه وارد بازی بشی و
تا ۱ گرم طلا ببری!
📎
انگری‌گلد با جایزه طلایی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94261" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Fy2Teo_Fo7MrL0jSW13OTm8zRB5M-0ukNKcTI9ZfICttneu18n1fRscyk0kwFCw5NkNLrQmoI-Xwj2nIgMXt0coU1BXpck7loXfkPizmrxtNEwUmrddf7mQq-vLSG_eZT2E_ULUXqeRwYU0Inb4BJolW2M19ViFZfIstIsCYCHV2wnO4fYXCOBhmZKDAPpqa1_reetNeqndG7xCSWxeGwFRz6u8fvN6hvdqSmAfS9u3stIKYVCert42PXvAnas8L_-X6pU2bWstEtBZTmZfoSqMg0ElzYbzmazN8-vQIGscT6gu7z1vkU2C3ViFt3_py91ceCfTVR3Czvm5CIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوائو نوس:
همه می‌دونیم کریستیانو رونالدو چه کارهای بزرگی برای پرتغال و دنیای فوتبال انجام داده، اما اینجا همه برابرن؛ کریستیانو هم مثل بقیه فقط یه بازیکنه که اومده به تیم کمک کنه و کنار ما برای موفقیت بجنگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94260" target="_blank">📅 22:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8RdT6peF7tGLd7ktAHXdhSpmgcxCUwrT2kQellEvf_NwM6tsxbx5lxq4sUbz8Qzy5LWMqB9UkX75hkbv1-LrN2CzCL3AGP8k4BfhP1cemVWiaRkJJemRmnLD7iNx11xXTHpy7AmUWDAgwCsIeW7tS7DSV0-bQzzmw_UiuoAiLROIskJlx5ecJVUDuE7s3c2kRXjQpl9m_zLdagIs1oNHzWhu4xCU28Fn_gETjFzxGwNyGnQwHXi38ljqUQALb4lzpE3kyBD1KP0dA-GAKfXtlcnLOjP913HXI0gDQe4FRJeZEHpx8OH1Q3v2Rrajj9-sFdG-3cyjC3Vn33D-TxbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94259" target="_blank">📅 22:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6kgHgSANpfof8E5VrSCptpfYcwfqH-znMokmmw_ksVUBxTeER0sqIbhzm2gn_nNXae-FfJZf1BEPG9UUysjqhSZCYsATDiCCMoYNLcKJqlLRf3XF4u-wBXNU8_AUzryhLm6fO_DMpTLo2U3_GD_D_EMcuNtQGZzQCFAbnMrR6lnFybLSLfkwXCm5KKyOB9rlevahTx-xEdsr2pkGeXr5m4X5UjETtMypz8c00CVjO87MdaoBrwzZaU8BN5c1CzejL1F99w0prz8-xRBt9NTmiVg6W5z3OwIhtt4nGlPzW2jXZkmOIXd8d4K1ln-qGME294IkMdZA1nvverXZFf7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94258" target="_blank">📅 22:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjQNzvEV-RcUMsLCS9laJEwy4kdxsqAQHNn4ZIJxtPEo5F31bYQUZGTrTZGuP1cvtlvJ7pzoPfJI3pMVwdOHGVfFCLhihs_n3QGsn1eYDsnWjQOMQk8lN1OupZtNHqd-7lFyXYgl0gbsLW8ATJGnCiMUop0EzKQCQ715mDngQpUCJN5v-HL5Uy6nQbr9JCM1tIVX9ydvUujPvBiyh6MRKcr8MQ1mH-ImR2emMQR6MjQif3ySGTfXqzvf9K2mzHTp1K_JyKswVGHe4SMkiDIxtP3UIirjbs9AEgDeCrUJqS46oCC6Tj_2VxfofuGgu2M2_B2nlgSQ9OsnTJ6sieFfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری و رسمی |
جان پائول فن هکه، مدافع هلندی برایتون به تاتنهام پیوست.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94257" target="_blank">📅 22:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxeIF6ovyHWoiSDBPR911Ruyo1oMG2I1fxHpm6mYQchg3EcwfdiTSY7J8shfrJxflLZlcUhPnWs0cOwax5QYPXNZef4zT2_iQLwJwpbF2BEn6Vltxk64LE-d9ivloeQfm7WcK8cWXrv_hO2RFHwq8J5L8unvUUKXUXpu6dGLUSxyPFej5y2ujmXUMKHJubPIPjytm-Pa8G97QEPaUC_mAJvD35AGUDe5hhgdIfRgjyg_4MkofH0MyHpOPhxPjmynpBClbcMS0-xDFBsMKQ72Mwf7qVrcYdJt2gdSYCJRYd8jQsNP8TWYeQBQDa24GIp-qOQg-Urvq_cGXYpAAJU2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
#فووووووری
؛ کوبو ستاره تیم‌ملی ژاپن بدلیل مصدومیت دیدار با تونس را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94256" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFlE6iqo8rYkDgc4FhfsIR8w4CsiqIkmT_yQyCkwI44P-BiA8GgW-2OuliqzpSmvhAT21NOJqUX8y00i8UyliUluz8NGuePgtriwvxpzMqVdIrKYf5z3n_5EH8udt7Y_VuV9nbxgM7Hy5DpiovpmbDHNqfV029S0FPhQGRGueHhvdeXCuhh39tsnLafGHZNkCvm6d5VbxolSFI0HE1qt2RtUbjyTOzgZ1GzRUB5dHxkLbcvGmPOx_6tpUlBSbMMAIC-OnEK0YMJFYdZHXxJRtepC21FA1P6WGJ_61z7XJsFaBVvNueZNSENa4eykDL4TSdYO5mjEzWvlnN1LswaTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
فیفا، لیونل مسی را به‌عنوان صاحب بهترین عملکرد هجومی هفته اول جام جهانی انتخاب کرد.
👑
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94255" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYrLFVCv_VVqEePuYnIcWrUMAcDI_brb9YhGZuoBYPUkraYFgRlVVYfrlkDUIzKPIYrjPROZE9VVb5eq8wWAB395Or5upRov7ZRE6cfrmUjml_132QrVZ7tIKY_x199Rd-lgcTYUpPKbHlz3BSsWDPngWM9NGVVwWl1rk9JQNxgrI0tAUFR-Y7mjv9IcX3BeBM9D9Uu43dlrYwUqLb2Jsd41MBGzIcr5KkZBj3VeQwk3NPD0HakPu70l9nQoRlynbGS5r5wARzxi1j0TicWSTFUU4Yvxs7otklph6wwxl7NGRWrm3mBKk5PuFDAiFsoHO6-kKBWHoUgmUcBLdLCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اینترمیلان از تمدید قرارداد مربی خود کریستین چیوو برای دو فصل خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94254" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6ZckzrDP5u3PssI5NueHTJ6qOqNFjlhwj-k6kGwtkCvnXxuQlnvax2OhHaRr-m8TnULRxy4albFcm5sOhzsigpXrHfNG-prKpkmhummy1ey4BdTJtKLgehzpqkQlj3DayYszyMqQ9l8yucd1V0ybZWU20rrrZ3jfB5QfKcUKcVbSQ_4n6Os7ShSwVZPXNrdR5fxq9OrKLtmhKwVPfi_KQ-tIS-oz6FOiMS1_ZhJuwDKuXTH35jgA8D3RT6zXwZV4wANA61M5AwlcnrJepMX9TN9g8cn-tMRaCJ2aPXdOkwLAxM9MGa50XxfO5RCdsGPioVwC29TYaEkv2jy0CvsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوریییییی
؛ ویکتور مونیوز به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94253" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏆
گل‌اول آفریقای جنوبی به جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94252" target="_blank">📅 21:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زددددددد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94251" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آفریقای جنوبیییییق</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94250" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگگلگل</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94249" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtBX2r79azNhkU3XoQNdD7eyDQ6Vip52_F1xuGlbdFe7Mq6DjPS3XFx62B9R42bnThdR85hninPayiXpfLIusvM5l1S80Z6DMVFgA_EQ9Fuuw1nwp4HYjUmqazfA8d8yhF2MM-FubKp3PVQfSHwiKC49-hWrbXO_cZSGfiVdeuWzDg50ZMem3J5_iTDg68FspxtHi4GjYJPSkuVSUrzWmukOsz0gJtGG0dIHhTmFrPTCxcrxb7rqqXV_5Fxt-1VSoZSIpRWn7Ua3SlbzSuFR3stYRF-_lMtz1S5UCX5O8k9HmCbkMlc0qjv7p67qpdSgigsAM7nu8w60gUk4ExUS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فووووووری
؛ مجتبی خامنه‌ای: بنده مخالف توافق بودم اما بدلیل درخواست پزشکیان به عنوان رئیس شعام، با این موضوع موافقت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/94248" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پنالتی برای آفریقا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94247" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kazfHTtuQnMrGtO729QglGAk-bLbVMWjIn6Xzt8OKPFnWsOLSmW9Z1kTU5WhIBkzbL-RgZ1y15eG_bmCPloAlujZp3hcXK0nAh77Kk9OvyXdvVzPAz_htMgXSvD9GU7nddBS-RVCROR__0oGHCzSSnZgDeC2NSoV3XIPdDeLMAFm88s6Ia5YNkXOpr1hnUmBb-pDnXTSqexDdhlER4W9rHZkguRaBZPHkSFoxPy-vQnh6AwB-35hAq_hMFmTVL03uR3nrhtdZJQMQZC663fsD3wXT_k-GJgx0pqY3SBR95PVfRU14egucdhmPciIRJEMzpOzKdZTATo4d8BocSKOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇦
🇨🇭
ترکیب رسمی بوسنی و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94246" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZl4pZF_grmQ6_08AZ4n_WRsc53hJ5bsg3dkv620rnNr7mntSNE2Fho5aG3Abr12iT0LW4I2g76GDVqMxzuG6zrIhe5I2Pv0Od6E53HDcOcEqNOz77_1MUENSh3sLKfDO591aog0vfGtttzAemNCwqSWqHMgBGW3AWvlMbiWERM4oYPGYIOmTxS0gUJJhWSjBlZ5fha3qJ8QDl1LFFzXGmj1CDx-BzpdZDBNQSMdtxARvI8DbzAmhAYdTyvymNKVUmQ6ZeIhtWIOylUMKzzAu17VAH38CdGV0Qz0RHhLBtJkRIGl6kYlyOz65l2XsD3mAqpLZ59SMQcZ7a2oY9Oi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مارک کوکوریا درباره انتقال به رئال‌مادرید:
فکر می‌کنم هم من و هم اطرافیانم، خانواده‌ام، واضح بود که این فرصتی است که نمی‌توانستیم رد کنیم و من از تصمیمی که گرفتیم خیلی خوشحالم.من مجبور شدم تصمیم مهمی بگیرم و هیچ شکی ندارم؛ فکر می‌کنم این یک قدم بزرگ برای من است. وقتی بچه بودی، رویای بازی برای تیم‌های بزرگ را داشتی و فکر می‌کنم رئال مادرید یکی از آن‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94245" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو: به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کنه، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94244" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuYPrgNbTTld4qmiXTn5TKaHrANGHVBwIDV5uIxdmQqzdIuZ7kRBuExeJdYlOHBraDA-qmQW284oFRqSOcj05IE_GhXK_oXzxNCbILplUWIcfHBfqnD4_09x0M1PdkGsxngT_RIRDYnAMoVGBgFl3QFHO2Qgops3aEA5ojwMcGfrffcvL58Uo-KRBE6Dv9CVMxxZsRsV2EofhyF8G6nWHGfxhLUXF1xVkG18ffleFVsY-vOcCrJUCOiEOflLacFpUo7trOVPI9hfX5CCjldjM6VQVeFMkoU-f7NG_2IGeqLMWNulBuV8aXqUevInUGHW_LfUEAAIXUp63D1OkD4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بلینگهام : مودریچ بی نظیره، اون بهترینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94243" target="_blank">📅 20:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPUqdMn2xY5p3KivYf6kKQ-jfN4stZ4MWYFw33c9ehAdEN8j47l8poz4AvI1a8O8f_xDaZotKtA5A38DhPQC_6CX5GTYX89gGr_8ztVzeOM1Tb-FunqeXeO6uD1FrnRBTUyxz4PnPidN7kJ439yRAyG59qNmUWNCY_mqeHqL3zfA4q8HHRRwTLpyzk41ge1GwO50jj4VGgr27zkGe1bYSxQMBC17Q3s25F_ZemjebVz9gzLWcOIc-OzrGjnfDe9SFQNJjF5_vnZrPTlZusml9JVk7wM9cSZN5Dlhe_BwKZ41GxxdyME3LbA-HDZ1H7xyLNpwQwgFYG3dY1MbPlbvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
بازیکنان کره جنوبی امروز دو پهباد رو تو تمرین سرنگون کردن، فدراسیون فوتبال کره جنوبی رسماً فیفا را از این حادثه مطلع کرد و خواستار تحقیقات فوری و اقدامات امنیتی سختگیرانه‌تر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94242" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94241" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbFniDHZHGSvG0htsn1VdOGtZyffcUH3Zg3SP85wH_w0CQf0bwoqmZB2PdwehlZc4yPzYFoIQYJs34my_r9OzNFMXSYxDtxUDSFvoe6ssVg82HNbK-mMXRQsJ4Fgf81UfW56Fxqgv1hMLNr9C5CuPwEkTcHLRABMs8friSw6buE_7UJlgILnHCIO5C8IuxkFkNCjwvjQbHojoG466Hzd-MsSpdqAxJvM_28QXtczslbQpjuEOs3c6jbicETRwTxzRbdlGVDz-NltSS2vDUvWsjw4NVv0AF9AzVGHRwWWiaLjPd-izs9ejOew0jYHHyR51LwzDiPC0JygTJVwlWmsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94240" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
