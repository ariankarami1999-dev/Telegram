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
<img src="https://cdn5.telesco.pe/file/PpQsdMp-cW7KjfsaJ0lPWHcJhECRgDQ9-uk8ulpl2eNhgByEqOVTHiFRDSxstdUiNSw-6AXQZ6CALjNlDYjVQLHbP07LlEoBnSkweytOOhCZu5r9DoW0VCtzIrgJHfKen-C28xTxbBMZFDDEtFaxfuTb0wkGfq-i0oEbf6hnEtbRA62RN732XhhT3ybdIrFXfvPzthclRxLA1dGEEZeSE-CvxmUmdp_Kw-6Xzgeh_UFz1N7s9p4sSsY-ZUXXct7bfcK1aU3JySFKdtK4JI7IIULPVJkoiNtC1Ct0WrTMLaC_QJ86uyNEdEaVp1d9iUSPp7OUblsyP4SDIycUnlcvHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 699K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-96371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTW6_PtOCXCM6hiQeEe7dbsKb2gf7_p0IEGRZdoe7-8oqONC9OVXBc-LaQEwRmyOIb9U0EfH1VRDQV_NyEUKrHzDBaXN-JJbXJrMA4XK6wChaB1D4a_grx1gy_mz9PeuWojaBIFho_lXNiWzYnUy1huWrQ7ioxTmcaKOixQrbcSiS_R1qoIP9Kz_CCDwUv05QXx4UUIiNjtMMFl_IY7TnVICFmhpwH5REXWQCAFIWBWpKPF116klkxdUcSugD8CazA1zmNuOFmggRAZkwvCCQBZf15tdG7H5sN1k2F-th836MwG1XFNZn8qEQMUC-QvEe6d82z2SCSNSPq1lAFP0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هکتور بیو ، بازیکن تیم ملی ونزوئلا اعلام کرد که همسرش در زلزله 7.3 ریشتری این کشور هنگام مراقبت از دخترشان کشته شده است
همسر بیو زمانی که ساختمان در حال فرو ریختن بود با در آغوش گرفتن دخترش از ریخته شدن آوار روی او جلوگیری کرد اما خودش کشته شد، ساعتی بعد ماموران آتش‌نشانی فرزند یکساله این بازیکن را در آغوش جسد مادرش زنده پیدا کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/96371" target="_blank">📅 16:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVIFtQmwZ4NsTp2mdAv7OG5uX1hY9MSIZipQzYTRoMvF429da54d2ihO26iD9XIf3L3YAeTYCP54IS2eDYZVt8pgqcLJwgBZasg2ZNdRRvDYVfm7g3Kv76eO13ZwNYOgHGUxBKrprKKBLdjWYx0vk5dEnA7YGx-FWai0qBrHizrdXKAH_ILQUodV1xKd6wIcgKzSL0whU2qsVHcKu5EWGzJXnnLXPH_wPtylXqb-lLur7gpcWPlY49J9uOIJBsWkELmli87vTNE50hz4APsEkPd3fueJdEok71cc89eJaOeNYxhd7amJkJvB_o8zRVUrkVDa5uasMkrJPl8LuA9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
رکورد تاریخی به نام لوکاکو!
🇧🇪
روملو لوکاکو در سن ۳۳ سالگی جوان‌ترین بازیکن در تاریخ فوتبال است که ۹۱ گل برای تیم‌های ملی به ثمر رسانده است
🇧🇪
:
‏
✅
جوان‌تر از علی‌دایی
‏
✅
جوان‌تر از کریستیانو رونالدو
‏
✅
جوان‌تر از لیونل مسی
‏
✅
جوان‌تر از سونیل چتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/96370" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=Yf6wxom624GJVMIwqepOTdB66f4q9glWZ0wuzjaKCxwID75F2EHtRbE1761x0FQxv6bP8cCNpTYP-rl4L2Zw2yhEcZenNGOEzlK0BBKYEtBUvpgJPjZ7WUiWQXG28JOcWi8GKBO8LWwzc97Fc20fm7TUu0eEZJCo9TSvdtml8A3EZYe1gOsZvqBa61NbWchJdY_Hwobl4N04OaUSXw3VXlTUoCULPa7NJvpamGZ-SqtAWAR-DqmfpinXgnbN-Jg4FPMGE3tjJV12EYm3ftzH-SDgjajLznNEwRWJbZSlHmql1ZpFYW2mUqXExXLA83YKXfWOuYNFac80hmnZVOlFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/96369" target="_blank">📅 16:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffa49c692.mp4?token=qG7HPAdja19adN5UiGMGxGGRnmobmKFjFAMJ2vhidSJvLLFu3Ske3FjqezjpTqF-lIxf6xqvv_b350AJP3UjX8uS-8uO2ZRw2zzO-IJlYrbXQIo147Rp7o_NCj3DXKi1Bdh1TffI8GVdeWlSNse2_DC1iJ_wk1VCb6BrzYAkflESex6JKreEVJhS4Bk2DJyaYoAsNAxMcyWRwMP49-yzSwNH9KWZJscLxDFS1f52rPKGiTGSSCb_Rrt986bVVFxU3xXTBwYuD-kX2yycy1nICYSjATTam1ZFX-zueZ4tw0DDTv1fhU8QYoNnX8LTOYiqxK2LFEIepQTwsxZgsqu20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مارچلو بیلسا بعد از حذف اروگوئه از جام جهانی: «خود موسلرا این تصمیم رو گرفت که تعویض بشه. درباره‌ی تعویض والورده هم، راستش دنبال این بودم که با دو تا مهاجم نوک بازی کنیم تا بتونیم موقعیت‌های هجومی بیشتری روی دروازه خلق کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96368" target="_blank">📅 16:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b871ffb756.mp4?token=JJHloOba9ixYFHPEFD2z5mnJOsAIA8a_57MuS3x7njJZJUh4nOEIHENHWDTGFme6Sbe0hPJFjgBeJOedsTQBZHiR5S7cXHA3XTinbrO-nlahkkNb_7_PKz7mQGkZpoDtLlMhWnPreVVHxBcfy6gf4YrPk1EcvoT8oF-KWR4hUsrD6iLxXRSgzemQq7o2fw0lqAmqDFqQ3f7UPznm37RzaaI6Iwfa9qjIUsEjff0hzLtkiwxw8ko2uLkjMyrRFGnlczpp4lcCUjSpadmnfAYIwOKdw0BNZ7UOyl2coVU2M9YJ9eWcTj5RDESoVwfNJNlq-6f6lNezR-a6sXZ7uSlAZ6shPPtXBZ_kVBQBNSmuJp1GQjrhzepoNXJHUcJGirdT9VFfdkeFw4p9VOZ_KKVSoKtAUP0eGrRW72W-QPTfsuxiw-2k3TxTYF7f7sMsZ6In8Cza6V4WoqQfobB8q6N0BKFMuZfOrviwf-4grshyp-Q4MX7--K4KWjWvUbyC2UvjC0pv9Sa5K989tYpNRWhh576ehAKDOyL1u9tkG5kOhvLM2Iv-fO1G86_wjnaRk4ArV2MkUIN_Lq7uPwL_0dgbFbCAhrtiIqNb58MbcxwyTb7GJDRK4Ugvh_fkIrsr8cNIM7lF-NGmZEOtz6V4n787vxPerIOoONpOo18d1GIf66c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
عشق و عشق‌بازی کف آمریکای شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/96367" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96366">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f23a0551.mp4?token=a-qEhzjNu8BPVubC9mQ4B7rHL8s6DeeQwVp29wuFeCjvNr1TBycTzDhs_YzyLsw-EmFXMO4FXzkIBAZ0CIqlz2ZZySwS879k1mECmmvhRlgBoIT3FiEjBsWRS68kG_-6IDSuu-_HJ6_6JKEAzX-SK2XVJq_DNFheXlMKvzzUc0PVr9LejrfKm2fFMQt26wI4yasLbyRmmQjkees83sLmWTpNNK5xMwuGug-3hVTG-GhzCNiqw9VfLfVYIOwoaDmD5Xwml5QjZdEpbck_S3gvLciSRXBLq5K_hJ8CC7TkdjLO0K7gVvTPPet0WUToLJVJGBV_G15uvHHWYhw5PGl4xoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇫🇷
شادی دیشب فرانسوی‌ها به سبک وایکینگ‌ها بعد برد پرگل مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/96366" target="_blank">📅 15:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96365">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f46f8116.mp4?token=BNDLDErOp4hUhLk17Ky5fnrp5wAsgeFkt2fkGkEOkPbABr6qk1jZLyPy4CwflgV0B6e_yzqIt8v84pczwwxFHbjgqosdvnWpbvAusVYmHq5Nh321h5ia-LodoPTBx0CezygVrhGIUJnam7oPDOw248j62WYFcP4Xo0ZUDFI1OU5M5d7KMktMPvc6rxV79tj7HgfLwYXH7DbvLotgFQL70OSIer4kRLK_TkDjpWyjHigrbZI5VUQrACjBam7aec0EJ332gmjYJjHexnkcxsUPtV6jbIejZjAg_PiZP4BNkzgVKS_quVJjlxpL9G7GqTtk-T-8NnIfFluDpfTPpzyCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
شادی نروژی‌ها در میان سربازان ارتش‌کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96365" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b317fa40.mp4?token=hPRMHAtPZVH7qpTGXrRORFTjKiUNGiD-iQZ6Vc-T1yzPIvzFHVE-xDQzlYQoqVRDTjPXZLrcRs11wAqR35iutaHpcecO7LEYWVUbzBKRYr4k1dfxiSQcmKQyodVC8LP2qVGOWvVkUt_KPBp_9m6pDMDCXey_lUOrg28nvff8F2R1oRYp53XxaQGoCJIrypKT7s1cbRxRhYpZMwuOap5JhlHa_AHR-bXrVap-wDJx_V-oXLpw1H4xDVVBA-DBbwJCJrVNLN6arUn0vXvZpRbFjEke2YNx7ee4otq6HmXqa1E5JdJMoZYSZ4hV51U6Bgp28a9hvKz-dI9xSAUA1WbHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
مارچلو بیلسا سرمربی اروگوئه دیشب بعد بازی با اسپانیا کلش کیری بود سر خبرنگار خالی کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/96364" target="_blank">📅 14:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3TMZG4hzP5zRAcSX37MKgx9MyGbZHz5AIO6qdcZrSwStDI_u1Rw3mzDYt5rNlGE7lsfeWdd1-9bZBE22Ee2pthOnm8N0rmoc5PvOeKwI1kJU4U08pbK8f4bq6CZnYceSwqnuy4-rSgnJF7iHGzm9cApKFO7Pc1-eU_OW1ME7LmGjjZfwam-FvKcIOq1o5jcaOVrhFsFIB6XEQp4ukI2mgpmdy1td-3mOPuQ2pmwoYk74yrkPNWHQiTsgJCbWmDBdrWc2CO1X9Ao1vg-zG2SsD-Wp3yrg5Ild7YLMjF166nzO9vBSftgkrlhUKptxV-6DL98697_0b8sT5CnRTR28aq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025a2a9a9e.mp4?token=Vw7G5pwIhg59-9XKPxy_L9yJ3bIXsRvht0h8dfks5wD25MySZ-v8p3l6R5kZsQMPoFir9TevYEjYalzk_xWrQQ0Ckgcr1b7OUrWonk6mXekKLgDwfZXIvklfWmIviSHzJJ8xlyyPg9aPzcRipVnfvBl8KFqOrDiASo5t-X6J5cV6ZMJtB6UAnNhkdsbW0MSj74ohDJ3L08SmN5s4Co-7KmBG-EJs3g4b7tTrfhhF6tJtcwH13QCdv4XxsfsOWkOgMnXRyu1ZrWZoPBRcXelKWxgzq1j9n3gJb-X3KuHG7rlNI9dvngmikcYLxL0NJ8xHjxsZpWrecnDMHIwwMrQ-3TMZG4hzP5zRAcSX37MKgx9MyGbZHz5AIO6qdcZrSwStDI_u1Rw3mzDYt5rNlGE7lsfeWdd1-9bZBE22Ee2pthOnm8N0rmoc5PvOeKwI1kJU4U08pbK8f4bq6CZnYceSwqnuy4-rSgnJF7iHGzm9cApKFO7Pc1-eU_OW1ME7LmGjjZfwam-FvKcIOq1o5jcaOVrhFsFIB6XEQp4ukI2mgpmdy1td-3mOPuQ2pmwoYk74yrkPNWHQiTsgJCbWmDBdrWc2CO1X9Ao1vg-zG2SsD-Wp3yrg5Ild7YLMjF166nzO9vBSftgkrlhUKptxV-6DL98697_0b8sT5CnRTR28aq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو رسانه مطرح مارکا اسپانیا از درگیری میان طرفداران و مخالفان حکومت در سیاتل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/96363" target="_blank">📅 14:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=fz9aQSp-Z-JuKvPv4SUZQZVZQhtAqLHFrG98oihjkPbbxDjmjqeTeVDaMqqm9yvlSxO4TqOvdwPY7Q6dLEyK40MkXqv2xoWmayDBiqYHb-l3zLlP-hMYKuEhS6HBz5mfE9aS_jooMZdjh3vGQWpZRlWhmTcMUDRKijSO6J_V7_fFjx_zTbCQ_KgOB3GvYC2WUT7yBziqGT1F0GDi_nvcSEyesCPy0GjY6_k9xiVzu54pZTIeci8HECg9HyRtG1YQF2uSxVUiaPEjBNCGDV5-kElVkYP19HBxXvQ-DJRtRdFJnHb7FY-mXaIqcsCvtfWqUigQ3DBlvHyZeHppEbywJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96362" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdEY2h-SC0TT-3TV6J-R4aJoIeETBJQogduOkxrKQLrzZjU5IMPBDelxESbTb4xBICt9QzuOSrq37Opm6iEshAAKz3qdIao_rJQZE_60kxIR8saVzcOwjJHIYqo2sfNu0q2FGfXmoisVdAeRfZOHkaBByeD2S6TjW5quaf2Kud_sy5Qy_gYPLJySYQeh1PhHkuyCT7duR9V6RE4VtORF-eZNcqoi0KxRCEcGQTr0sklcP2LHl-T41-g845Lzwp7X5_X003w8keE3lmPy83vUoew2E3G-ABf0TNbvxNgunDOgWkadGEqQYARPjwFa9FNmPR57B6VHFQ-ZMWpxz2NZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آژاکس در حال بررسی احتمال جذب تراشتگن به صورت قرضی است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96361" target="_blank">📅 14:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bac0d662.mp4?token=kkwZe4bsx-2rrqeHAye1Cvvq73rjxz3TK68eGH33Zq2tbExcXnPd6bN5E37Ld5dQhZ0FPheeWqfbfOENeqSXVL5Hb75J6wnpk5WYECKUlsmlXWk2JqdBKEP1oDtcmwrXZogfOkQPUYINKiT-9L_J1w0NQ9xzL_EjfHNXUr-3rptrNrC6hgDs4TPiQ93CabwpxdHIuJnPpIQW8Irg6sU-zkDPTRONNx-oo0Lg5VzAX_J0pNJNzQsTpNYPS-6rBvkIelD8ERK8ucbsfe3lJrpHUbcutc_JZbpMgzwk8_wrMkdldIGZEtDJBT1UOGY7V-LwAqy3srK80PRnnu9AWNvWkXq5Qch_yyLYScGErIvLUaCC_3wnVuoVMPMJnA0vIPXQ-shSOxRm_M1raYiLA-sPrPjp-AhBw0cAUjXfs2kfSuuXgkgWj0W4tVAzhhhmVolgKEZYHegic5e5ak8w66g-F1XmdCtIS5LmRo_IHH39wC8sHdt5lx9Vo8oEoRUhIriQBNcATY_f9maaLzz1uDRBUIrxkTJpLPnKKmpR1gh-8nvZhLBcQUDBr7t8G4KJtOUCU6LAxVu7q7_NJQ6rFsWyLNMA6jvYW970FWr55fR34J-NrRZHwyilut9eFjg-ZUaXT2sGxr917y-ScQsm3F4QbtBYki6ZII5D9RR9d9U7iDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
🤩
کنایه بازیکنان چادرملو به پرسپولیس: به 2 روز تمرین بردیمشون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/96360" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czroTHHYzr5K5yrCUQLDU1M6WMvfVGXUsf-zodOyc_G9Q35B9h29tdmJJhFl40Ewq8pU9CTiDYk-xAQbVzf9gm92aAfZ01Ohz-f43jNm0p5XZivywzh3Nxbv_FD_jQnOaQbhtWiHelHGdIZN2XBxVa0M4AlvxWYfLBJ214MmlSvpljjTz-xnjhcNYM_jIWxTs9IOMK4PHgtuAoie7xrXZuVdT8sqUdYK55MNQoJvSGGz3n-ZZBwekMVp7WVq5mKoBZ5015twtEFgH2IJfAnhvJ3TlEAjtgdKztHnPHvwDRxi6H91pSHgkST9QlN5SeKeH3PFYzVnPEn2NUPz1ggSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه چلسی از لوگوی جدید خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96359" target="_blank">📅 14:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe474ed8e.mp4?token=ijid_Y8f26sTDvkJTkRM7yFOzGPM8rg0ggHVZOJ5qEgwWLOH1_hXusQmIphaMSe1wpKrDQZCUKBS87Rs2ik77W8_jajlIXawWguP_RBYdxXqpNSDtdyOA4bPy8HBohrvX8FXnJh_YjGkz8vCfJlDyHU17NoA-XT7QB0U8qfXZukSEmvvl9-6J8YFpuopfFBFy1Bh0CSqN1IAFuxTPnBN2sfFkx-16mdzhjkEDQmF1k2kfke-QfNQ2pv-N5TZJGS53aIV0B7-FeLjdNAt_7LOQN4MVy1dCrPC0CtmQ135JFRCJrsUNP2iX2Bcwu2UC6XkBx5EuJPkKm5I7GeeAofNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌈
مهدی طارمی:
همجنسگراها نظر خودشونو دارن و قابل احترامن و ما به همه این عزیزان احترام میذاریم چون این موضوع به ما ربطی نداره.
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96358" target="_blank">📅 14:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDCGIDMbxNLUOHZFk8lOz4Dt7B_N_krVyQtJV_vmG-pYB1QQcu8DYJnzATsrS4QbnMvnBmDv71B5Wi3cSp4ShxUf5gsX6T7v2JQri0kKpYOQkZGv-URnV0MvgeRI6rYWL9sRBrryYx6M6P0IYhMhQ7Y3qCtd3W6Fyne-wjoDVVBxcnwRff4SPcct8b80eDkRkRSvhrRqvUOiawKLS8HBagt0sIkH4rNHYL94KBmqwZZrLA6-sU5QMcCrJzRol8jA7FNExH8os6azb9ZAElh-WCWHLI7aNslfpYM2vzroDwmTsi2mc5K3dMqpIKVasSYS8XCFJQgzn98vj82Ozcfasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇳🇴
در میانه بازی نروژ و فرانسه، یک زوج نروژی در جایگاه‌ها نامزدی خود را جشن گرفتند و شبی در جام جهانی را به خاطره‌ای مادام‌العمر تبدیل کردند.
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96357" target="_blank">📅 13:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d12d8ac3.mp4?token=dtyR8xGaGWMXyHUZujAnDjdzhvm9ESVrADJYyABcikFNDu2PvVwJVZ5s_oMRHUixdU49RfbPFhQ1Oliogbj76Yk6tvvaOs71pd1SohtUXJJiXPsxPk_u-Et-a2p24TYVldjEtxq0fmO-UsY5oLFHhlS9uYDakYQGnC8reQFbt6Mhe7VAEG_fM3USSkOQL1j8b1Eti6-bEB7ohjLDvxQyOdr1a984toKugNSaKp6bPhbVKdZrpaCgjn9v0inomdy1C7WNi1n4kDha6FtOeuz6YTuRDlpX1teO83n6Ef-WwbyCAbmEOI78wkaw9d9Jvkx_FeDteFnNJZ8PtKuJpLc-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شجاع هم حسابی سوژه مصری‌ها شده‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96356" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014d5401dc.mp4?token=vZUFXhdwSrmOoGJcH4Gg0qezeCy7kbK1XP63FgelTmcjIEjz6NgNXVx14SF2pZDjW2VseJt15g5ZNKQBplsICMJKnK3ZasalLf4bs9W9SiN_3sw2EYaGv8e2maMzJFD79L-_YQEZHyhEE1cjk-u2mixV0uLyRxDzpfGhzqJUHhs9OnJulpRijgUvihzOlXbOe1NIXKRZXW1jWwFu3-5xtPsru_ZPWELOeK_iftIKlQ6QAxOPqbvbJUqXW0cQCrtp9Dwz8eyMPdcSIgg0WPbp0Tip4jUJP8NNIydwkpap7kP18H9jIyhX63dT3BetI2HZivR1oPkHhVgKNO0ZQWK7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
زلاتان هم از شادی وایکینگ‌ها بی‌نصیب نماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/96355" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql1JpjWoxFLPIWRnmIxdkzPX2fqUP6qCyYK1f6CYZd2w5acjvXDoGzFLGqSLeedOfMTOmin3pybMu4OCQZeRP7yDeer7_DmQKWIx3OLXNm5G-Aq3xTRPSyE5lYjc0VA3PlywELE73ErYUthLYpbTYTy2tXoKKWHv69hoSjVjPvX4WRhIgj14ura9mEyY5BbOxz3d3qceoGpbMsN6xwv533akKSwxEtLpUiUq8pEY2KH0CsLYNLbS7JC-qX97f8_1rv82TCm0gln7T8n8PTWGN_BWG3NAxxxVaQzRTp838wK3QkyPIDHY4dGtlPtdM9voLLQ0BulpHHai7gEbIjsi8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بهترین تفاضل گل‌ها در بین تیم‌هایی که ۳ بازی در جام جهانی ۲۰۲۶ انجام داده‌اند:
🇫🇷
فرانسه — +۸
🇧🇷
برزیل — +۶
🇩🇪
آلمان — +۶
🇲🇽
مکزیک — +۶
🇳🇱
هلند — +۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/96354" target="_blank">📅 13:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=qXeZLSRgu28VxgyYvQ42ADtRvJnde53ezRDrOyce-fHsI6lY8uPrgt5xGCk2d3fRYt9aVJ2HzpXK2TIlyYHKytCjaoVUeh7zLlY6Xp9qrmkswp5Q7dm6wBiRZUCqXJ1gUwDfVQUR8DkiH_IlzHX4AHCk_s4h0ay2Rq40lQjA8Smf_hhZJhoZNKP0zzWm2IrVFJjy7l8SjhOfbmqsidFgihVL7IfJSXlSNIG3ven2Vq954CQXJPtUb0Ul-RU3GwKmkELnpoa0U0WCuincirEzBaHJUIezKgFKWCMp4EMvL_IFhB9G_S9d8ldrYLLZVuNtwxccOru6IKzMVAzBkvBm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942a3cf51.mp4?token=qXeZLSRgu28VxgyYvQ42ADtRvJnde53ezRDrOyce-fHsI6lY8uPrgt5xGCk2d3fRYt9aVJ2HzpXK2TIlyYHKytCjaoVUeh7zLlY6Xp9qrmkswp5Q7dm6wBiRZUCqXJ1gUwDfVQUR8DkiH_IlzHX4AHCk_s4h0ay2Rq40lQjA8Smf_hhZJhoZNKP0zzWm2IrVFJjy7l8SjhOfbmqsidFgihVL7IfJSXlSNIG3ven2Vq954CQXJPtUb0Ul-RU3GwKmkELnpoa0U0WCuincirEzBaHJUIezKgFKWCMp4EMvL_IFhB9G_S9d8ldrYLLZVuNtwxccOru6IKzMVAzBkvBm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
دیکتاتور امباپه تو بازی دیشب هم نشون داد که چرا بهش این لقب رو دادن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/96353" target="_blank">📅 12:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4a20441.mp4?token=q_RpGG2eFsv1_y4xrPGycyONCSLp-Lc_SbeG8S0bdS5aJhstemtq73BIBOTP_mLMMuZMu26oT550wsvtHCoLqxOt1847kqc2S3YZMT7gcIefTResmWRr0grUdm8hq01-CPzn62rwF8JNH_spksdna0WMS-BBO5iyLM62tWfYyeSaH-gxMKe91SRG0GP2fsJkydTsorQRZqzYBenpsGdOEsytnOwBi6kzTZPkClZo_XaiS8B4j5_fwv-8Odu9tZyYi9MjAR3PeyZpdlJgPTuf10V2T4GMcMERUplofs96Pa2aU2zjqYZZZmk-whZ0ApS7jrI-3gGsYmu8CJaIljoUB6o4AHr82ji5v8kFNalrGAUem88T1yLgHB9ekQjNGLYSWRdlyaSTVque6khMxN7knBN7cGMcE1yvJyNy30CS2sRuTJcPEjqVtnyZpgdVAu_NZmw23CBZtCLIq5e7TveIJrJNNBsbSqBCuyiHmhkoTrTEei0vFTSc8OMRMQGIr4AS35W-4_FdrE9Zd_pSlLTOr7xQPbZs-YNVgpDUfdwotQyCIUkhuZHh0RYmTxVYtLcSZQznaoKvFDJAJPdJEgr9cxWjHxT8lepGIsmG7WTYxZbzn6q7lLnnJfG6F8fMoNvmXlUSdIZJc_gqWMCAJ0sYwxwK7UiapkQYTCtRgXEIdz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
تفریحات تماشاگران جام‌جهانی در محل بازیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96352" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGeAPVxu6zypOjHY0K2j0-5j07i0stN70fgW3a68AVPKo11yJHsEffttaFplUn2j0JWL10tMC6pIlgJxdqbxaXutXQtVywizhh_o9wEIAovEa--925iNivq9FNYkrYrmXP1xGDgjud-yYX7BkUz6HOC6ByH-Tg_focobK5-U2-FiMJyT8ft4Nfbx_Kn5oP6g74fi-e1oRiqy1WkifKJCWCMe27uHVD7pfn0iDBD9WchXrwSOpjY4ucqpCWB_s-Zj5yuI9x9dKEcufW-UhKjA4nAk2HILJ-IYdyszRWS2YWYPKlXmaxsI0Mys0a3NvEd8lhREVs9eZUsvbG7br81VWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در چنین روزی در سال ۲۰۰۹؛ رئال مادرید قرارداد خود را با کریستیانو رونالدو پرتغالی ۲۴ ساله به مبلغ ۹۴ میلیون یورو اعلام کرد.
🇵🇹
🇪🇸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/96351" target="_blank">📅 12:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b9d3e103.mp4?token=gVvl4VJgunU2Jo2j4Cq9WM2p6_SznM5LIbECMSUnib5ZFgiqMvtx5s21wn3Nazn8HWHlEezXYI0WPwyxEuHrl-Eg8eJn8ogPrArmZUv8lawb7dNOmKJYxLthL1J1mzN1N7DnpwMqsO9n_oWa2OG5wBlN0Qni0rpq8vR2w8ii6_sq1-mG_sfrTyRnnqVPf8EkbJxre2eVWU_SgvMrFwyFviLJ-b0W2Eh09-OMJMvM4dSVyPaLDfmrSxxzVoLP-p3AUp1PjX2gSqDGKPhsYSNLhQgDB3apIByDrvBH0kdGiAogc-K7IcgWo8sCRM3vBgs0sGP6Erc1z3LeLhCxbhz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های جالب و تکان‌دهنده تبریزی خطاب به بازیکنان جوان
: گوشی رو بگذارید کنار، عشق و حال زمانی کنید که جایگاه خودتان در فوتبال را محکم کرده باشید! بازیکن ۱۷-۱۸ ساله نباید مشروب بخورد…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/96350" target="_blank">📅 12:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CilKlrbYj0UeOYr0GgKX_zZrxL_9vSIhDYhwyJ_djixD7-QNTBoQd9v9n2zZ3i0z_fA4Ucx7skIBa8RFMdc23qd0U3LBv6naAA3Tsom1Ce7fxfBnVjOKmCewiG2WgpnUbh1NWRJDrr5QJdxLkybRSUenuenuHpWz0szTVrTIccBqGW54YbH8hFVFwrCaBm8HB2ivQIgtTZQZgb5g4kU3Ua1qFQzMRKsEcF-95z0QSH05OVTvjolYK12knPIW7sWN3GPB7T-eHXeH3BV3j54kbhlPzlGq_sED9GOZrxOStdd5uBvSWQbWBIdnwjtZcNsT0ozOX5CViVcZVjGs5lAVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96349" target="_blank">📅 12:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=UpsWhjeSHKOvJ7FjG_UM1gzISaQs_X_-cHejACagC_HjoA3ae9NsMMQHbowspHGb-n8Ow-XaN1iFGteA8sqTFkfr5fI-kn50klTqA_i30y7KHMV0iVOwFU1GFnbfNhrg1E3_qbgN4KR7bSV7cWY2MO_iglTT_qyPtKYTod61bVrkJWULrcBzzIW4V5MpKheirwArkyvE8uSqmze0Y109byBNfFI6NpxmgMx5oDH6NLQQlpXATw6RRme7xf3rbSYUMiKEgPVVejdadN7sgdBQdxGcxltOgkNUTmhDyhMLW75Lu7mo7W8f1knLIDI_GOYkYxgmb7Hicn_3tzzF-RDB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee48f95460.mp4?token=UpsWhjeSHKOvJ7FjG_UM1gzISaQs_X_-cHejACagC_HjoA3ae9NsMMQHbowspHGb-n8Ow-XaN1iFGteA8sqTFkfr5fI-kn50klTqA_i30y7KHMV0iVOwFU1GFnbfNhrg1E3_qbgN4KR7bSV7cWY2MO_iglTT_qyPtKYTod61bVrkJWULrcBzzIW4V5MpKheirwArkyvE8uSqmze0Y109byBNfFI6NpxmgMx5oDH6NLQQlpXATw6RRme7xf3rbSYUMiKEgPVVejdadN7sgdBQdxGcxltOgkNUTmhDyhMLW75Lu7mo7W8f1knLIDI_GOYkYxgmb7Hicn_3tzzF-RDB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
اثر جدید حمید سحری از درخشش دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96348" target="_blank">📅 11:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBGKXgViLFtF3OHrZ6b39QCHRBH_gD56SELJOlvSomq-P_KXrKgyE_LrelWQgFzm-FcY5fm9GviHbYk4MV75LL3b9GgQM2_2YQdxApNLPycuc_gqnm17MxAgIBmyqDQNkJWpPOlRyKQFa3X50Ktz8eikTVWiLOxcMcBFi9hOQMKeJqCC5a2VWn1cL8V9oh6O_kZaKIZkWCaXsSn_9Z_r9uyo6L2FjU7oyksFYsgvVXw8aiQRFgTvGGNn4dB2YyHzYu75ehtSmZ31mgpvxYAcfkC7gUF4LWnD8216JtqmK0QwjQIWwwYjRri07St5OO4805x-TM6kSvaxppybeyyiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
آرزوی هوادار بانوی برزیلی
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/96347" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=U7pYHEQoKRyNT9n0sZwdmwOfaWKnjoXhkblV9In4sw7g47_PdhNrs3ZtWA8PzpefngJL9WW9fD6lmhNm1ogAF4MhLebQZ-DAFomOQus8D2OjRYANhKoCVg3wqk_wfILufB8pcNwYrzCflpoSXx9IDHuXTq6h4WCw72uQ9ONHI21TJ8-EvoYcWvv-blkqTnEj9Warf0FJs56wM9Hj-AIi_01HAs8iX6HgANkHUns3DdBjfJ3TdEP5jlF5VDoqWye7s7FJpY2xDE7nY-7BpnXYui2lNFYTrjMIlfwni0EAdNW_JrYR7nquNEHNd16hO2302ApRvMjr4SD0HQltJJKe9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330a09c36c.mp4?token=U7pYHEQoKRyNT9n0sZwdmwOfaWKnjoXhkblV9In4sw7g47_PdhNrs3ZtWA8PzpefngJL9WW9fD6lmhNm1ogAF4MhLebQZ-DAFomOQus8D2OjRYANhKoCVg3wqk_wfILufB8pcNwYrzCflpoSXx9IDHuXTq6h4WCw72uQ9ONHI21TJ8-EvoYcWvv-blkqTnEj9Warf0FJs56wM9Hj-AIi_01HAs8iX6HgANkHUns3DdBjfJ3TdEP5jlF5VDoqWye7s7FJpY2xDE7nY-7BpnXYui2lNFYTrjMIlfwni0EAdNW_JrYR7nquNEHNd16hO2302ApRvMjr4SD0HQltJJKe9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
از هواداران جذاب و پرفکت رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96346" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Uh3AdcwEIadqOL8CgS9j-vajLc2eB1dyjQr6Y72aKWYJ1gxKNKaEOLeLPUy-Y4IB2kfu5elVst1OsU16mXAfiavLhYYtF7mtL6ZsRjXNBch5ZMaKQt3s7bOZoflXV7dZWhXGlJPIDMYqtyh7drpZJnFq5R2jBtNQK4To7oz5ExWQ0q3mulaGo4mXnavHVhbc0a9foY_kyFkD6yHYYQHF5ELsBu5q3F_iP0rcNCKemQHfTuwz8DAbRDDwwPqi0P9YZnXGzrIz9o7Y43wxqZyIoUG6YNX5COOQoMYG6JiSVpu82ptbM3M7SyLUqpSXlN1hWToFXk9AnmF9jVjtnBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ مارکا: نیکو ویلیامز ستاره تیم‌ملی اسپانیا بدلیل مصدومیت از ادامه جام‌جهانی بازماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/96345" target="_blank">📅 11:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsVoWfxZUlK-FFfF-ZBmkPEobYD3dgeHYoZhGAQlIA5iwwI7v20oi2O_taGzTL6HJOxqCny0TuoOp-OEuODpYaiUyJuKtGJx_etLs1NOAMbVairHKan1TQrJyWXJioe44qvIQkRRqciBU15wFbYI4XD79g1jct1tYYUf_-XSp4iTPJcTQEj1zL9BOJycQTGbIS9c2no80WyGTV6A66B6t6-Asa7eOphCbwMd875oKiypGm6ZS_7wX40-3UfX9r2pmuDd3_Ch87Kqwl20-wY0Uiw2zCoSbkNppf8f0xYWMIByq7vUSQLj8M1lXZSESjyax03V5gHP82eot0JhAf_7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
کیت‌دوم پاری‌سن‌ژرمن در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/96344" target="_blank">📅 10:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=YoRLDpj6jB-v_kVZimZSjU9h67PFzupEYkVqSm_AVxjlxMrocC823JcZLEpDQhUJ6nAMfu1h286JnCA1k50ij_59W7KaWaF-4DfU3TKeycmwTBLqBJaNyuDSBpUcqBMcKYdujuJ-ZDYazeOqWB3b0wnYspZ-jTZJsn29yGFL2PrRDPkBKuKF6QmhGv60CAyNYe3qwfRKPCulkkSm5ou9uyVEbjCM1UAPD3Q9EEiRhp6NJXQa-X5lycZCYX2vRA8QJDey2QdVwTVTjCQbF3RywUfWaugOA57D0dy9BCIvNarXA0_kdpIKFMUc7S47BVEmQCzxnfBoHpumyY_SIksilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4d474911.mp4?token=YoRLDpj6jB-v_kVZimZSjU9h67PFzupEYkVqSm_AVxjlxMrocC823JcZLEpDQhUJ6nAMfu1h286JnCA1k50ij_59W7KaWaF-4DfU3TKeycmwTBLqBJaNyuDSBpUcqBMcKYdujuJ-ZDYazeOqWB3b0wnYspZ-jTZJsn29yGFL2PrRDPkBKuKF6QmhGv60CAyNYe3qwfRKPCulkkSm5ou9uyVEbjCM1UAPD3Q9EEiRhp6NJXQa-X5lycZCYX2vRA8QJDey2QdVwTVTjCQbF3RywUfWaugOA57D0dy9BCIvNarXA0_kdpIKFMUc7S47BVEmQCzxnfBoHpumyY_SIksilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤣
تو برنامه پخش زنده ورزش سه پژمان راهبر به خیابانی میگه انقدر از قلعه نویی انتقاد نکن، خیابانی هم کلا برنامه رو ترک میکنه و میگه از یه جای دیگه بهت زنگ زدن پرت کردن:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96343" target="_blank">📅 10:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86220511a3.mp4?token=UVNt3cUiW0YPA1P1ynuDs1xxf74SE7B-biMCf79Hm6aSIHErizRGgUD1chmtziu2OGwlLQ0ORfKoqn6sx88Fb_e5rrLZnrS4nJglpy9QuxWXuH0pLKij7GGBgFy9hAOB3A7J0_uK1U5jizk3AQuECZ1WpwAXDnHEtjITDxY5DS7gliuTkY9Kcrv48p77M95zu-hkW20aDXmlWUNv7sLCMz19aeYbidYzoGead5hYYUANVIAzEBFzapM8slAttiwRHu7NDY_294Cty54BP5BrCLCZL2dA2dLvNyiVdNyzctVbjJH-Z6zF7JQniKWsRLirN32g748A5jvN1-haOs9u1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86220511a3.mp4?token=UVNt3cUiW0YPA1P1ynuDs1xxf74SE7B-biMCf79Hm6aSIHErizRGgUD1chmtziu2OGwlLQ0ORfKoqn6sx88Fb_e5rrLZnrS4nJglpy9QuxWXuH0pLKij7GGBgFy9hAOB3A7J0_uK1U5jizk3AQuECZ1WpwAXDnHEtjITDxY5DS7gliuTkY9Kcrv48p77M95zu-hkW20aDXmlWUNv7sLCMz19aeYbidYzoGead5hYYUANVIAzEBFzapM8slAttiwRHu7NDY_294Cty54BP5BrCLCZL2dA2dLvNyiVdNyzctVbjJH-Z6zF7JQniKWsRLirN32g748A5jvN1-haOs9u1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👀
آقای‌هری‌کین امشب لاشی بازیو بذار کنار تا این طرفدارت ناراحت نشه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96342" target="_blank">📅 10:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=ZPGn1oUtz9lnNAnsjjHBizrg233JlvOP4cA3HFBq-aC28lj5Jru1g5_YAr5Oj1EnYezY2vxAVC-QQIUUElnsH_-49ootrL-qboQI_Ot7YvbJPhDMjxn5TUlabvNoMPRC9gTRHwCLltBmXivyQvu_CvoyzssCbCjChJEiAihEoJdagmNJomIsDeIv7Vx3YLPr_aqvMk-anAB9JUvotSItIvX5cGuOqPUQrhSqq3oiraxCg3m7sFrmlpPTPOhBTejj0EDn3VHzgbJn4gz2sYRNegvYgDtUtvWDHHr8bxBAfX9OiPsK0jLLn9G3YyTvPoUr059w27pVbKnxLCNsn8Eaiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81f32bd6c.mp4?token=ZPGn1oUtz9lnNAnsjjHBizrg233JlvOP4cA3HFBq-aC28lj5Jru1g5_YAr5Oj1EnYezY2vxAVC-QQIUUElnsH_-49ootrL-qboQI_Ot7YvbJPhDMjxn5TUlabvNoMPRC9gTRHwCLltBmXivyQvu_CvoyzssCbCjChJEiAihEoJdagmNJomIsDeIv7Vx3YLPr_aqvMk-anAB9JUvotSItIvX5cGuOqPUQrhSqq3oiraxCg3m7sFrmlpPTPOhBTejj0EDn3VHzgbJn4gz2sYRNegvYgDtUtvWDHHr8bxBAfX9OiPsK0jLLn9G3YyTvPoUr059w27pVbKnxLCNsn8Eaiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
وضعیت قلعه‌نویی بعد تساوی با مصر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96341" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFL93_7V8wU8MoKlgfMc5X1I4F-V0NAsfUOmAflDENabtvI6-dSzcZWxtjPyb40shgIcWASiDZYoOYC1oMZbPRkRMIDj9mjsbgp4MJOE0xEkuq_-fzrONfWumgLo1zNO_Ia1SG8T3afpEFv9Xhh6Z11rWvOXsId5dOpMeAdzFNR2ui5iL70QA4ue7oBRNVNyoUqkbLSXhB16hW7GQxvSIcKL8qXJnTMabkIsxzYRBROINTPYhwPi__Y6YveluM6MkG03P6Uq9GPCmo-DjxgFEhKkE-Qm_kqXbbB_g24JoeLCzLNOBsm73vgu_93Qdq_7baCSDZXyLUHEUnJ7cKGdPJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFL93_7V8wU8MoKlgfMc5X1I4F-V0NAsfUOmAflDENabtvI6-dSzcZWxtjPyb40shgIcWASiDZYoOYC1oMZbPRkRMIDj9mjsbgp4MJOE0xEkuq_-fzrONfWumgLo1zNO_Ia1SG8T3afpEFv9Xhh6Z11rWvOXsId5dOpMeAdzFNR2ui5iL70QA4ue7oBRNVNyoUqkbLSXhB16hW7GQxvSIcKL8qXJnTMabkIsxzYRBROINTPYhwPi__Y6YveluM6MkG03P6Uq9GPCmo-DjxgFEhKkE-Qm_kqXbbB_g24JoeLCzLNOBsm73vgu_93Qdq_7baCSDZXyLUHEUnJ7cKGdPJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
این یارو هم از شدت خوشحالی سر گل دوم و مردود ایران نزدیک بود جررررر بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96340" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🎙
میثاقی: اگر بازی در لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات پیشرفته var نداریم الان گلمون آفساید نبود و برده بودیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96339" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی وسط سیاتل تریاک ناب گیرت میاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/Futball180TV/96338" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdrwaaTm8YCgQZZ2uogvtaK_35xs8sxyDDo3TIeO1NooB1_t-337PIIVU0e9nZskDMhwVBZqCJdclzHgrfSbjv-LXhN1b2ndoNpFw14dwNwTyWgRv4vrHyjRojedYIfL5WuWXEfIHY3AbU7K-BqL9RBLG9-osHE4oIXRKO9i01yvZBW-xuYPdlsFRQudNf2Fji7pf2L7XQkd0AqTpkJh_Lj-A96HeRY9kffAUMPe_EGzyeMohX1qtVWEglyC70AiuKeB43J-HEBsE2Gb8emcugqEIWyCUqUdNQFuHO4guYkbrh_8kzSzj3-C8MBP126lYigXg7qei2Xp6kTDV0jCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق var بازی ایران و مصر
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/96337" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG6WfDXaQfyNpuE1ofCJb5I5qIfeFdSXBj-L9-vDgsfjzg6kSLWyp-9PetEx_sBpajUvuhFDYVexjXik8AbEqAkhNADk5kAbpBVsQotFTFQ10VzndC64T4_M6OWXh-3jxs5J4pWp16ZGyaXJjisz_7kJNNl0tQxZfPeCObmoERtiNFHzT00BcrTEiKWBIRdxRM4eGfvvaByaZ3bfI1ao0Hoi9tb_DVK8GhrclB0OMpPWhDdksKlu4bY8t9P6pJBvVClRnCE4q91XjaeZmB2lGR5i0P-qWLYLkYv1TGAGXlrEoEK7mBzpbCSxdw8vADbCm5WAqnEk7WMjfMmvBEIn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
🤣
تفاوت‌سطح از این عکس مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/Futball180TV/96336" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی:
شاید خدا داره منو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/96335" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmR0KwTnxaVLzvGNdDoNSuVNnOdqzQObb5P80jLeM7D1GjOQaM91aLBjdLD557e7LFAk8jMIa9vUBb6XYAdU4Dv71Ko5BG93uaZgB13EaGRwRncAPZvkyuqxBU5l6ChrWLY1K-wEA5ykbvawGSyEyG0JN0FKHrZjHaoeCZ4SQH72NiW83MR85fC4CTlbBmC73fzFO007_VeA5-po9PrptIP_T8zURUuR2eWgR0jxN-Safj0KggcCsTlTSB7F2vrbzOgk9ATyjYw4HkRtE3TYQJIdR1Jkz03rE3VtGFWVjfPruLbRXdJNxcOSsNmio2OlGCuutvc0r4tIPjY1eUnOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/Futball180TV/96334" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztlh4B5_PEqsGdPWTpZY_aHlXUb7TZUCFDHlZdsw7Xt7GHnUyrcJFWIRRy3yAGmPJn75P33NogWhOLKlRPtpCVa0Qx2c9ol9Z3WTYuTwjMNMqzWPbQW8FNdykpZdvf2t-O2od7yZBGncZXVxUsYrEk07hG3UwlAXzh2oVnuX7Y2rD2WE3J2d1xSDFh3rOC_1Tb5yrMLIiTewS5Rh6crmkQaM1eBGnJXOG35xWmQf2tPL_Ki1H3kWf8W5ykTjstl4Hzzdz1t113QIdfv7s38wJMthYP4CqH9KPVHFiR2-P50Rq6cS7MA6gMANR7PEqCfPWtjgl9XxjGlZR9lpIbKz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/96333" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYwkwHK_jjqAaMWxbfs1CErAz3cSNkJ2_6ab8d-SwxuX3BduyXgRDYYF15jIQz-kd5qPw5wNl08H_ipRqlA2t-Fk-x-3kywo2weedQBEgaNmVngYFNKAs1CrXCCFk5QqnrdX5nwF_C4ToSfRN2V_GoY3S3--f0mqlOFKI-DGtBKTGShR06kCPsv8GlIHmUePmGM1N2lXknQe19KaCi2oSddbwToLuQPtb6makL8FW2Enswu_mxpDUW2ZL8MqNVCqnwfDbzgeXPysYMQ5hXWmJWzEbqcx4_QaL81aYAKxoUL19OvRK_unn8GKcNyS9IUaS6NEsjmmdAmdZnqzUubYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خلاصه ی بازی واسه کسایی که خوابیدن ندیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/Futball180TV/96332" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMN5OaVt-VYBJl2L6naIvRV2fnFnIk2qGTxIudr0mUHrWPiDEbullveZZgLfn4taSR6siH0uBwApB3Saw7th2L9ToJv1QzeaRDhg0KfwUW-TjjFyGiduVKqJOISyTFbT2iX8pfmZxiMXYxS_3l51-WyA0xuKsJeLvjS3XxJXoDfjzLd_2ZyNw5406GPeMAmrETtzIx-5qiPGDqwcBUjVUhHQQaP8HEJt6EBALOtmvYpw4Xft1xJZ6ucVxkgQB2hI3GtUr0O-f6Q3onUDblXqIt0CgrtH-F4LwOq0fec9zNA_yGuaNQc4J8EHLCERx2mPNwd1pDj1Zjxwvp5MqOLh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سه‌بازی حساس برای منتخب ایران:
🇬🇭
غنا - کرواسی
🇭🇷
ساعت 00:30 بامداد
🇺🇿
ازبکستان-کنگو
🇨🇩
ساعت 03:30 بامداد
🇩🇿
الجزایر-اتریش
🇦🇹
ساعت 05:30 صبح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/Futball180TV/96331" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKJvVbD9JMcffL2sMoKNZ2BHbPT3Zrj6VTdNXosm32QfRJlfv6ZtKIDecW_1SQ7bJTvIppK1e5iv-SMAXyOOZSB0079YmQFTAQlEWx4AGHhU9M26cDHvs-YGQ2TxGYUPcP_GHoEAkAUkMksbWDLJq6ludn4ous1F3PzUV4Sv-_IwsTY6dVfo120-_kYuFynDGozVu8Q5gqPXTQ6Eka4cAFTkr8un1M--3xA5i9S7hl25lsHw200DxyyUatdcdbRc7WgdJj-hOxdxCtoReBVxPkYLNuJyZXKFKi2zHLUb7n_yFZ4bQujp2Is6KkybH72SUETxBJHhvmxdGZlXLBuIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
جلو جلو ذوق کنی، کیررررررر میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/Futball180TV/96330" target="_blank">📅 08:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/Futball180TV/96329" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/Futball180TV/96328" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2BPYuZdCHuji-Wn6Gp9ImtXWCJYpkrF4O-AgVeaYL3cSBcKFfCedpt4pHffqBGVPv3q4aMu1SZJNY-upEPAhM7QRQKT1TnB2Vm0nz3oa1CI7nlFCOWM-Cf25D1wnvhS3ab5lNcb0qvmLw-xHgblC44B-7ChvqAK7oAEDF9RQyBWac631cuJatuxCCbvMxmnoNf8CeACCfJnIrC59C4Gyr1ifurAmXNlLk-T2lKll281usClNsgsgDLy4fORHep-WzwIVFn2NTEFpU8LWHAFFGHrycA4IdeYU79L1HrHa3dxh10JVSLAom8BzyOM-y3tRXxzscg2IcWpkE8Nvdle-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇪🇬
مصر
🆚
استرالیا
🇦🇺
🗓
جمعه 12 تیرماه ساعت 21:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/96327" target="_blank">📅 08:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTTS8DF2rnBAg-A8vyR89CG-8J3wlZy5qcmJE-Eo067nuCND1xcAxTV41B4Iw07YlOr3ahbsRf4XN7IpC68VHSvUu99zCe1dFvHTHh_Kio3X67mw8TdTtq744Ht06ctbs5DiABarEnJJWJjtKhj1Ldkceel-_Dv3akq1Szt9KxRoSKaIULk9XOhJyDfAI6aEtTLRG9__X0XIbE7GT42ZoXk6kStCkJ0YalkafwTsZnVtHShK81LVwqJb14PqWUgzXFVMPY4fiAa7qrxsqbNot4HINztrpocTr7IOzcx8RXgosQiwpI8jJXPNrDrvsqRpxh4KpiO-8incafTmoAkjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/96326" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ7Ts01mLxNULB8iA4TE5uBkUSTirQ7vn599cZUYZM9tbEsuEwuOLNhQ_oDFCf6HMQUoyXTwpe4_XS73yCft0WKhlfFbloBbIe9mxSlXYtOpaHl2TArTY70dFxWc885V2-52KsNEE60w8hg5Xi8dN457nsWr4hfI3e573xyJnRFJux3if6UO1DK4mCHfofQWzbyPCJnu-RLfpp2Qh7kpCqS1y75tIlw3AZKlf7gZSc99FVQyyDv43Y7po552a9z0_H2hla4TVLOv_cz2Yvu-hHiiPFyo6mp2RyuF7EBCl4gkUI7SAU7c4dJtorjv63FblQrEmDkJXRTXmJBZzlV38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/Futball180TV/96325" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇧🇪
تیم‌ملی بلژیک به عنوان صدرنشین راهی مرحله حذفی مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96324" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zanyo73ie3fztOgvX5pTm1i1njJdFD1BRsIq0bxWkrJ0XxDYslmMU-g_HM-aTCnpgo1Kb69INLudzlsXAvJVcSNWPYydKoMQ0XaAzYgypb_tk8FPRGOGxd17nnHZBesfsccaW2pYnFK2wG0FTyVmfjzMRmMQIH3uYdOrKLb2ZdRQpi9SguXMUlnIAioz5MSH8biEuaGNAT29_kI7hVrRJjsUFuKGXawLImsslJ3GKLroFauUyfhosegoLt0S3PCoqJZJdsn7o6XH-TfmIZR2bR-gFXOK_kSHObhSRQWsfwpHcoWT4Tf91whfBMZDlJpYoe5myRNYECLqqUJxsL4jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/96323" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=fumWQx2A2G9RtHgza5l_XNEfiT8S-xEZTQBfptu90O7sdg1oPJP3Op6bVT9IqP3n0wihzWiWh4bMjpwcqDfzTzOrUU78GwthA4WlFjuBD-qZiPVlaxjtWwzndWepH-h8xuRUcOVPedHs7jO42FbGB4SyEfyOJ_xiCmmYoLrDIwjLgVilqnSMiGGreaTskYhSIvceNZ5X4lidDCrk0uZ9T-nC4-GMIMkiiU3Gu_BDd0929nqMR46Pb9nfBTQg3RlSusuGw7GpOsuMEi6ZrUDmPkLHT0LW2iIPT9-m9hWjuXUycBw3EcmfP5P_9fZcwcMHUZscHxIL3XF43tWx00AObg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=fumWQx2A2G9RtHgza5l_XNEfiT8S-xEZTQBfptu90O7sdg1oPJP3Op6bVT9IqP3n0wihzWiWh4bMjpwcqDfzTzOrUU78GwthA4WlFjuBD-qZiPVlaxjtWwzndWepH-h8xuRUcOVPedHs7jO42FbGB4SyEfyOJ_xiCmmYoLrDIwjLgVilqnSMiGGreaTskYhSIvceNZ5X4lidDCrk0uZ9T-nC4-GMIMkiiU3Gu_BDd0929nqMR46Pb9nfBTQg3RlSusuGw7GpOsuMEi6ZrUDmPkLHT0LW2iIPT9-m9hWjuXUycBw3EcmfP5P_9fZcwcMHUZscHxIL3XF43tWx00AObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96322" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96321" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96320">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/96320" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96319">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنظر گل مردوده</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96319" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96318">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/96318" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96317">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شجاع خلیل‌زادهههههه
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/96317" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">😂
😂
😂
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/96316" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گل برای ایران شجاع</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96315" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایرااااان زدددددد</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96314" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96313" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/96312" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جهانبخش رو آورد زمین
😂
😂</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/96311" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پشمامممم چی گل نشدددد</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/96310" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96309">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بعد بازی قراره رسانه‌ها قلعه‌نویی رو دوتا شکم دیگه حامله کنن منتظر باشید
😂
😂</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96309" target="_blank">📅 08:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منتخب ایران بخاطر وقت‌کشی داره هو میشه
😂
😐</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96308" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96307">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قلعه‌نویی تو این گرما چرا کاپشن پوشیده
😐</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/96307" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96306">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=UzP49XvCTLNJmbr-AXFUu_o9JXxih53X7or6Aj2IEJdp7zXj-N6iI_EvJP3EjihTyve8rT2EIMCiMzz-Gy57n-hTJ-pp4mUkkZ9q43dJ41_M78y2OdL4JhTxqb3jp0ZQKJehv9e0M2-UPs-Wc7zxByFKVgkwcTzl0Ro8E1tcz9tfnyqZDigvEyjWwCFwULTgnCOCKWwHE9txS9bWnovZj4FO_ZCcyuZZ0K3RhKsTQGQ-GBOKUasD-MCbnZE38icRAlv1A0oaA35ymgsd_DDwhmlbGWCFWi-NigfnIa0zfRnWBtlKvQ-d782X-Z0zVkh6nj24at0zgWpy431d3XIbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=UzP49XvCTLNJmbr-AXFUu_o9JXxih53X7or6Aj2IEJdp7zXj-N6iI_EvJP3EjihTyve8rT2EIMCiMzz-Gy57n-hTJ-pp4mUkkZ9q43dJ41_M78y2OdL4JhTxqb3jp0ZQKJehv9e0M2-UPs-Wc7zxByFKVgkwcTzl0Ro8E1tcz9tfnyqZDigvEyjWwCFwULTgnCOCKWwHE9txS9bWnovZj4FO_ZCcyuZZ0K3RhKsTQGQ-GBOKUasD-MCbnZE38icRAlv1A0oaA35ymgsd_DDwhmlbGWCFWi-NigfnIa0zfRnWBtlKvQ-d782X-Z0zVkh6nj24at0zgWpy431d3XIbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بلژیک به نیوزیلند توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/96306" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96305">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصر صعود کرده کیرشه
تیم قلعه‌نویی ۹۹ درصد حذفه داره وقت کشی میکنه
😂
😂
😂</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96305" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=vbkg0CAkfMtcZtrQ6JzoXAzxfRYyAnULx2NbbP7IykbKIP6xR1zm2rWURwW-boyQQuSJCHIaYJHb7mg8v32Q6zNO1xE6IrMj-MSOtEFobIrXhWOsetBVL4GPg0Wubojzpi1roYtwUWb_d9FYq5wbPjjASHGuYivijN548SCyPHT6RpMvijKIhnQfHsXoQiLrrkPm-E9MmUQTFyJkp53BXBaSo3MMG2rj6p2u7We7Be2KOWr6qLOYhoc-KJyk91B4cfLwoh_6hUb2BF1z-WBETCEVAhMZaQbx-Xe_NidtydRbF-qLBvOHG9z5eg9oFcFIhpOcFYDZfkowE7pUHCPMug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=vbkg0CAkfMtcZtrQ6JzoXAzxfRYyAnULx2NbbP7IykbKIP6xR1zm2rWURwW-boyQQuSJCHIaYJHb7mg8v32Q6zNO1xE6IrMj-MSOtEFobIrXhWOsetBVL4GPg0Wubojzpi1roYtwUWb_d9FYq5wbPjjASHGuYivijN548SCyPHT6RpMvijKIhnQfHsXoQiLrrkPm-E9MmUQTFyJkp53BXBaSo3MMG2rj6p2u7We7Be2KOWr6qLOYhoc-KJyk91B4cfLwoh_6hUb2BF1z-WBETCEVAhMZaQbx-Xe_NidtydRbF-qLBvOHG9z5eg9oFcFIhpOcFYDZfkowE7pUHCPMug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول نیوزیلند به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96304" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بلژیک چهارمی رو زد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96303" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96302" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سعید سحرخیزان، آزمون، کسری طاهری و ... چی کم داشتن که نیاوردی
😂
حداقل میفهمیدن مردم که بازیکنای با کیفیتی هستن
دنیس درگاهی رو آورده بجاشون که نه میدونیم کیه نه بازیشو دیدیم
😂
😂</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96301" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96300" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96299">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/96299" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96298">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ژنرال داره تشویق میکنه سربازاشو</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96298" target="_blank">📅 08:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96297">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کارت زرد برای عزت‌اللهی که داره زنش از خستگی گاییده میشه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96297" target="_blank">📅 08:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96296">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">طارمی از تیم‌ملی خداحافظی کنه سنگین تره</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96296" target="_blank">📅 08:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96295">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWJyMsU58QwW88mAOE7kkz1JazM1lKiW3DzQlmszItk-DNeO7T3-viAbrRkYeOfRHgNPhXGmQZiO-893zyKNrVzplXjFDLqcPC_u2dDf7D_XDqv9bdC0kDISqktmVPpa4g78MEtqfyCxg9HtsOYAoluj6qofXaFs7Jld9r8_wQw2Ejk7Bo-xRpezqkE81BkoF_yPicTqfLPCm-n2t9l0kxOQz811ELiMNdouJ-evmVB15jzPLKLQ89bkzSTaeb35TfPaSnUvVZSlCqouvH2eIrvuIJ7T1_MfWnI-3l9KhOvyDyX_yiH_P5tpusVWbkKXKUZ9Hwi67HxdmaHiYCAl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
گویا صداوسیما هم دلش رنگین‌کمونی میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96295" target="_blank">📅 08:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96294">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مصر داره پشت سر هم تعویض میکنه بعد قلعه‌نویی که میدونه برد میخواد کاری نمیکنه
😂
😂
بابا اون قایدی و علیپور و بقیه کسخلایی که داری رو بیار مردک رولکسی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/96294" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96293">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3b7e026fb5.mp4?token=Q5VaVG0g8gT6LnqfTh93paF8knKa_KrzlHf71aF94aj2J9PKZss6uODhtdmNEoOPKvD8lEJdhaPh1-lvqytZ8F1x56811z7s1y2Euv9kMmtTfR3q5ECEdQzMdqJJYkwIE2mIy7aE0pIMf-RwE7olqc-pF5gqgE5njlIcA1E3ZAFpRG-0-vGq5ha-AE312JMilA-cY90VY8730nj59BllplT_kzn42J-YDQnH_j1QIinOGgK8dyxMLUCduEid7BNJr4DCAClqxQ4sfb6GZjJzm1KdQJqMaHSJcEjbucSNNz8cNZNqu2DfCQgIBGpbDa6M0-NkRA-YK6unx8jPNHOqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3b7e026fb5.mp4?token=Q5VaVG0g8gT6LnqfTh93paF8knKa_KrzlHf71aF94aj2J9PKZss6uODhtdmNEoOPKvD8lEJdhaPh1-lvqytZ8F1x56811z7s1y2Euv9kMmtTfR3q5ECEdQzMdqJJYkwIE2mIy7aE0pIMf-RwE7olqc-pF5gqgE5njlIcA1E3ZAFpRG-0-vGq5ha-AE312JMilA-cY90VY8730nj59BllplT_kzn42J-YDQnH_j1QIinOGgK8dyxMLUCduEid7BNJr4DCAClqxQ4sfb6GZjJzm1KdQJqMaHSJcEjbucSNNz8cNZNqu2DfCQgIBGpbDa6M0-NkRA-YK6unx8jPNHOqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بلژیک به نیوزیلند توسط دیبروین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96293" target="_blank">📅 08:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96292">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بلژیک سومی هم زد</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96292" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96291">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نزدیک بود مصر بزنه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96291" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صلاح تعویض شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96290" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEXqDzBUX2B9p4qgunCZNIPkpeKe5jzpLCxlh2dXxmdn4ZmPX6HCZEKr09B3IdK96ZWKVrtHmYHIZM5Z10SEEp77wYo3U1KLGQsIUMMvxsRQl4f76b1gcfx5k_eNe2hdbNVox0ifAONBgA0pPbujGgYQ-XMeipA0bsLp2ef4NuNZslxMODFJKhdW6bEK6oetEgGd6Ipco5iHed0yiwcpgxKncHbl8qvDh8vG-sHbvjwVfEZJmettUPkiv4KIOEjpYszhzCW2yZL92yAx1D5pZ9XhZgiXZGj5-9Ny7MNXj1XZNUWntvLrTK-uB4PDp1b4AlZWPIyF-Y3ILHnanRHYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
تصویر جنجالی نصب‌شده در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96289" target="_blank">📅 07:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سرمربی مصر چقدر پیش فعاله</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96288" target="_blank">📅 07:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چجوری اینا گفته بودن حداقل ۴ امتیاز میگیریم
😐
😂</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96287" target="_blank">📅 07:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نزدیک بود مصرررررر بزنه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/96286" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96285">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96285" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96284">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران گل میخواد بیرانوند وقت‌کشی میکنه
😂
🤣</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96284" target="_blank">📅 07:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96283">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f272e1c110.mp4?token=Eoal2CF_iTTmEfQnFP4TnaySBpTHFtqUOb_XJPRGTff9bYmKdxD1YJrMUreb5RFaFZ-XOkc-Lnaa3Z4otEewnLmR2xZpRUj_s439EGInss8Oa_odozaM8STYCRBxg6wKywDs9dN46SoUNWjFd3OBTIc2JCbxZWIev2HkNnLwvq7hVV72TWUJr51iRwpDtRXl9Avf7kTGrETy1n3QZq6HpYlbnnoAjkqrrJIfn2ecIlnSggtN-iy9rowaB_2tOd4TOWsn5394DfqqenP4LeudgTFPiiRjcXXAoONK1qT3Ek-ZEyM6IsbYku1WiOqViRj-z2H5j_cyRrhHTgWCaIGwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f272e1c110.mp4?token=Eoal2CF_iTTmEfQnFP4TnaySBpTHFtqUOb_XJPRGTff9bYmKdxD1YJrMUreb5RFaFZ-XOkc-Lnaa3Z4otEewnLmR2xZpRUj_s439EGInss8Oa_odozaM8STYCRBxg6wKywDs9dN46SoUNWjFd3OBTIc2JCbxZWIev2HkNnLwvq7hVV72TWUJr51iRwpDtRXl9Avf7kTGrETy1n3QZq6HpYlbnnoAjkqrrJIfn2ecIlnSggtN-iy9rowaB_2tOd4TOWsn5394DfqqenP4LeudgTFPiiRjcXXAoONK1qT3Ek-ZEyM6IsbYku1WiOqViRj-z2H5j_cyRrhHTgWCaIGwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم بلژیک به نیوزیلند توسط تروسارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96283" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تروسارد گل دوم رو واسه بلژیک زد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96282" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بلژیکککککک دومی رو زددددد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96281" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96280" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دنیس درگاهی رو کسی یادش هست؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96279" target="_blank">📅 07:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYpUjQW8PidUM_lQkJG1gHSpIRWI93Kow1DsCoQhJz3Jpz_XiUx8Yi9BSm-gSu_BKMoNnKrNIRgflH9O7tubs15paGWLV47bHp_INRcDEd_VUzrYtJQzy8L97CZdx6mntqrlpay-KEocYkp1GhK5QDUIY1Uf16li1VKBLQlqinJezQuMr9qSnMH1OdMrE5X8cMsq266VknnBmKu4BrL99C4ASVxi0o__0obdl7OThocf4eBUCziJoeMmvrIxUXcOJ1cwNKWbr5Rc1KbuoKAP55d0d8uxmR_lhWssiO9PSJzwxh9ZS94QSGQ2vD8jEKyptD-73N_qG6O3v4j4SNLfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
از اون فکتا که دوست دارید:
- رامین رضاییان: 3 گل تو جام‌جهانی
- رونالدینیو: 2 گل تو جام‌جهانی
- زلاتان: 0 گل تو جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/96278" target="_blank">📅 07:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عمر مرموش هم برای مصر اومد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96277" target="_blank">📅 07:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حردانی بجای کنعانی وارد زمین شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96276" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرموش قراره وارد زمین بشه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96275" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
آغاز نیمه‌دوم تقابل‌های امروز</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96274" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_0I1Pvt5KKEJKysRn4IORFYC55GVofBt2jciRy6B7oZDDcaBCraN0lAmU1AcVOwYIF4hKDnN_qyqW4408SxrlQGwwC6m213A6qSREFgQvHRsx6YB8yv1hiiZP5tmq6auK8-DW2XKjfCWeWp6snAxd4H5gJxjK2BWa1dsc0781_9Ys_2bAVYcBtA-qn9EjGuE8TWsyJ4IXlhgD3OhvYHLPbx7AVkh-Ir7OST47FLxMABus0i0b1AlkS7xvfUmeZ9Dgmz-L1w_Q5AN89O4MSZbLzIGwb7BOobWJH5Gs_Vlu8qGMb0MQIfFxiweh25RyMmI7AW83MLOiufD_-pmSeYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار کامل بازی در پایان نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96273" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jajwV_1pfaSb0_uFZuvHeaZ5zvVSTy8aYDnruQSyDvHvtKGCzSxh8lJ-2BFTmmRn-wp5MePMNjDhDr687boDf2sZRuOFaeB3M1A8emQ-h-wFBkukv-ANZtgD_1TLR1070LrG4Db82-wI70c7yQge5xg3zLP_oRqGn3F94zERIw0gVUNFBuYpAbKQDZaZOO-nEOuxflgQ08BMeTOz-RALgGbNuz_6P8XqlMYmly4hrX45m4jCiHdP1uKWWU8mNX6GCb3z5R57SLSmZ45K39EUECi_De331ZGGvLawRinttOyLSm0P3lVFfef5jVoyYKlf8JFxSiMtHhXNouvUifiWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بازیکنان منتخب ایران در مصاف با مصر از دید سایت سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/96272" target="_blank">📅 07:29 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
