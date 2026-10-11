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
<img src="https://cdn4.telesco.pe/file/Ndhhce3dJbQNgk54-8hnYP35qtbxE0BO76V8B7GE58wipUrYlnWLc1ixetFslxzA-_VdYGMzz8QDF8d5ksNtPm4UlKqB66ZRUVYH3Ny1DlK-gEP6E1RCRxbP_4HVg_ADmsgfIH7gyiOf8FDS7fiHFrsz3t5LVA1IK9lD7yutUHUWHJzxGs-lI8k_47omJBTSVabrIdZM0_isru86vgalRoWJgny8MaqFO9UGRM8v6ivF5bHNCJGDxYyOvYibs36bMgRg_HcvckY7iSF-oOb5D9MtBbeaMw6A5dnyPNZlYTnPuzZwhKrD3CpBaCcZAYUxB0RotS68XRjKD4GKtlh-_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-152047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbzXWKijO82krF2YFD_CTGIQ378IBM1gqO4cohL7wXfagcd2TZFjdmy2eqa668-1VTwbof69pzum8UOAgRS6_7b6B4fSJNVLQUKozuzsf7jlaRJ5x5r3dCfFQGlJlrXiDvjIK_tuSxYBLRMhyTW_z1Uv1fFkDastl7DtpN8_fMl3EefAIgf-SRC2G2rfwOUv2Ebwz__LnmhUsbraiqLWbx_6YrIsJuRzNVTokhVrpNL5iU1Htbb1OfiQVaHAtlYBQbK7p7Def7Tam1_j2MetBP7LZRIqumHJRzzJBuS8b4erE3l56eU66zYHOLLQrWrheE3g_ZfBGuDxbGtbm7Gu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ائتلاف پیمان مکه:
ما با قاطعیت پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/152047" target="_blank">📅 02:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04243f9871.mp4?token=HSs2zPsMLbqJbBSYv2jFtdrQS8cAr7JT2WX1vn8fQBK0nQmYRCbklB0msjmxSfwLFhcvfr6nwTt3-6Itv5-jlh28nN6JAeWKk1ZwKIjKCBchAqsKrQRO1_Dsm-ewu-SkUfUCLZR1yyU-sgOfeXoNTV1TR7aV7b-mBE-7ODFPCWz61x4M-AzLggqsAaxKCWhKuxCO1G54Sj5Ow5X2fQadZ003dpaZh2Vg6i8ugNmNWcM8JGqPi417S1-wKm31cjct88I-Q_cM9upngwotKOK75Ggv_sqUBq9NHN1Iqea07tXjnxhwgG-tXxNGG-q2BMhNywRzsVEkLYqcR39HSzhfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04243f9871.mp4?token=HSs2zPsMLbqJbBSYv2jFtdrQS8cAr7JT2WX1vn8fQBK0nQmYRCbklB0msjmxSfwLFhcvfr6nwTt3-6Itv5-jlh28nN6JAeWKk1ZwKIjKCBchAqsKrQRO1_Dsm-ewu-SkUfUCLZR1yyU-sgOfeXoNTV1TR7aV7b-mBE-7ODFPCWz61x4M-AzLggqsAaxKCWhKuxCO1G54Sj5Ow5X2fQadZ003dpaZh2Vg6i8ugNmNWcM8JGqPi417S1-wKm31cjct88I-Q_cM9upngwotKOK75Ggv_sqUBq9NHN1Iqea07tXjnxhwgG-tXxNGG-q2BMhNywRzsVEkLYqcR39HSzhfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جنگنده های ارتش اسرائیل بر فراز سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/152046" target="_blank">📅 02:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/py_JITd7UoKEmoBIBTdM5flaUExiA50N5fZHGmHRlHV10eR20XbtrEFz3t7sx1L452yldiFv_3oYVVdwll-gHmEn19X4ZzX3vE_7vWEqdBpdBIibJ3TXE7VAgyQWPGtpV8fzm4S3d9Y_2nrPYV4K5uYzx7swsmOJdQryzp6kyzToVvwp8Tsfci3O-ABwAq0X4oF2vjcaRwecMFe3wFY5AygRi5PPd8Q5dCe6gqxuGAyks6J3Jx5Re8wbZBgmMF3Hy9Q5GDrS5noPf9JilohueOWHSNiRbSwZ6QUfWWnNmV_LXOi2fgmPOur2WP7KW_vdi0t812G14hgJ_K4kzs7jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0ACZqBF_ZkfwUN55u7zyCnxfAU6_1u0fqdMaErImj3AfxEZc7ttna1HZD-CZdLWRIm0beMhN3zqcGQ-ghGxNoRHB_X32IPVBb_BPKvV-KVOE4vB_msRKt_OQMPRZG5_BlogkR7uljoQpan30XlUTJEp-A8acTTLufCvEN1-pxu4Nn1FZOh9yBkpRcFCgHAN7jg0nKISio45N5WdSCdkcRhqa7Lw6hZQQALzpQK89fyO_MADBA35kHLAGWW-N_vCE8KtmTBZ-sbgjPuX3wZ2AujRdFUOX8CnM5ZT81nVLuhMiqnJQbiyDG2_MZ83UMnxXtGS7XYgkBzqbAyTvXoTXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
تو سایت آدم و حوا منتسب به حسین یکتا از فرماندهان سپاه، برای دختر بچه های 13و 14 ساله برای همسر پیدا کردن پروفایل باز کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/152044" target="_blank">📅 02:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q89us4JNb7oP7WM87klg43aGrP3i1EnVbNjL1o982kkq_lH9fLOeB99illFVzvcPyrkq23RI_ttplcHdld4grYMv6eBfPyFf3j3rJcLIjI90dJXVEPd_o5KcxXpnSuDvy8TyapRyp7FxJc9vxya20HFpjSRi-LHWMleFSMhpQ4YsH4shoJQt2O7LEiFkrlorDZPLG2m0Qk268oF1uvoi9jxYJ1McdiETOLTYvC4_FvjNPRH8bS_yNoZIWPKTv0OhuKIV1XJOqnKDVtPLXUW0kwkCIBHF0xTWJkYKyVLs8-UYCUb2sUkAgoYqYo9OJNA9VZf8eJG2EG_gFUGC44MInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: ج.ا حداقل ۶۰میلیون طرفدار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/152043" target="_blank">📅 02:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZGAoJPH0NVET9jBK0LrmsVXj2WhTdJeG61lAv2xbM8nlXDOCNWzrI46xM-aya2ED335_J7NrbPQot3a4tOEKo3sf9ehSsPigw4L9mAONgI5rxFpL-NfG38d6GYRR89hnVtz09j0msYjD10NP8KhRiYar8V5oz2fbidRdxhU7WLDKiW9I2H-cdibSyOsQBXjrAoK0-ZkFrdWTJU599cuSZHpoo15dtTlo_5nvjxxgUpz5WOwSY_BE08YM6ZSnSeZpdrBbAwrWTMeRtMSx8AkGhK9Z0P8J6yUdf2jWKdWm2oTcFtrdAESHVRj-ARJCm_m2bWL8riZNnLaijLW9QOoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این تصویر عجیب در ایتا و روبیکا وایرال شده و نکته جالب اینجاست که در طول ۴۷سال حتی یک فیلم از تاریخ ایران قبل اسلام ساخته نشده اما اکنون از همان تاریخ غنی درحال سواستفاده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/152042" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/152041" target="_blank">📅 01:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h81OX7BiQXbOfWtRXj4Hw-g1tvELX_Cbw4hXhNqY75I7cC9HddBNdp9A_K0lp3OUt783tVAdmyKRJdTmWBUunUpX2zQ0z2w5Z0Nr4CTz2_KWsB1Opo6LU3P15TrRw8gVKccopDwBpzDxProw4-PAYl6DjM_-Q3juE-SVqFr8CJ5cRgMLrdTAHGUMuqpZHEE8wH05WS6NaAxjHAk9ivlkIGsziDs_1ITIGG939ONC2LGtoj7S8y47hfL2d69SbCCbN_LkODPQHEWmanCrSKiHZ31zF2DcysgH_Jo4DtgQx2zxXbsD-JOMFMpAf4K0cHSlHzbNBsCl5y9cg9hAAZyFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: روس ها به دنبال این هستند که ترامپ دوباره رای بیاورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/152040" target="_blank">📅 01:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152039">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP-2bqlmveIxmTqIjNUQY-PbA5GwYM6IGOBZKign75rVbeKPLW32XbLDBem1eENuehSDVb78inE77zFPyLx51bTpGDwUWlX-fYXDIbApI7zwwLlYhr6XZ4rG0vJ6x4Dmvoa5AqNAjop4Mr5PMm9XaMVRqE0ucuyT-aChFE0M3nvg0JU6L5jQU8ocmHhP_y8eWz-1-yx5_auXY0RMJDYJBX3bTI0YLlvUsQEEqp8UxCqeVU8fC6xOO3wk8ZMPR7n_Wwy7HKAe2Boo-2BeL0XOu72iscTv4rwml3JYOouKwzOdWhLvQYaNqkpmqBzqArwFkb2y7jc5kYK0wCjksDthRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران نمیتواند سلاح اتمی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/152039" target="_blank">📅 01:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152038">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/طبق گزارش مردم محلی، در بیست دقیقه گذشته، جت‌های جنگنده نیروی هوایی اسرائیل از پایگاه هوایی تل نف در مرکز اسرائیل و همچنین از یک پایگاه هوایی دیگر در شمال اسرائیل، پرواز کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/152038" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152037">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
اگه یه کانفیگ میخوای که تو قطعی اینترنت وصلت کنه حتما ووکس رو داشته باش
👇
👑
@VOXNET_BOT
👑
@VOXNET_BOT
✔️
با خیال راحت تهیه کنید
✔️</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/152037" target="_blank">📅 00:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152036">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6hm2-l7QIvkb-AIfwcO_XJwDvSdHgJa9hLpfxmoytpo1c29Mkz7UbnNrZFC9FA1MmOdngcjcOMbKjyC2LaLK93HSo3FKi9FI7ygTGxfadKivUAje2ai06CYcTuOkI1eq6zkNg2noAj4GblR1Jxoh5kYh-Myl2FXuRwOmBUn4Yxc20WLhtjfXMbC1lbb6JNOFmUWfKry0tfquGIKLu7VinVdzVyR8bpPLs7VzzwczvGrktuuykRifJbdaFzeMkiPWaHLVCs4vca6tFzUw_ciruymYqs0YfQA5QpjkORh0GbHlKnubIsuZkdaeQ_C4_HZjAR5_1nK-0rk8Ws1tog4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: باید به پوتین حق داد؛ او هم بر اساس منافعِ کشورش عمل می‌کند!/ اشتباه از ماست که «روسیه» را شریک راهبردی می‌دانیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/152036" target="_blank">📅 00:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=vsi4t-0AY4fqFvKwVis53u94t6L2M-L9Rkc1nUzeNEU3qqcrzRfMsKebjpjwwOY5BHHVcRcdKMtymkqlqGIvJlUQpS-TbAJP_p_elVNCFaB0yCZCSVvrI_XE7UeaGVz8TYyjEPfqSuNps9o308kdTCRGcIk2Ac-bK6IYtq_7Eon5082bVgJ7SSmFEOiKJTZxz4bBKGlVh3lY7hbkR5CNJl9InR-D-Z2ci2dOURYQR8rI77w8oy03mND2ChNjNW4QfQv5vCIzvPptUryPkXGF_TxbflD0RJVsZtUVjsNtXiYjZ4XtLUQ00aL5HO_BIeL62gtKSM7f5TeimPug-H-HXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=vsi4t-0AY4fqFvKwVis53u94t6L2M-L9Rkc1nUzeNEU3qqcrzRfMsKebjpjwwOY5BHHVcRcdKMtymkqlqGIvJlUQpS-TbAJP_p_elVNCFaB0yCZCSVvrI_XE7UeaGVz8TYyjEPfqSuNps9o308kdTCRGcIk2Ac-bK6IYtq_7Eon5082bVgJ7SSmFEOiKJTZxz4bBKGlVh3lY7hbkR5CNJl9InR-D-Z2ci2dOURYQR8rI77w8oy03mND2ChNjNW4QfQv5vCIzvPptUryPkXGF_TxbflD0RJVsZtUVjsNtXiYjZ4XtLUQ00aL5HO_BIeL62gtKSM7f5TeimPug-H-HXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
حرکات عجیب ترامپ در سخنرانی امشبش
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/152035" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152034">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=I2rDGTYBCwKQEVyZuWZzhVe9Qaem8PL8Lt2B6ZN-V7VDYu_3CVXxcTAPeZkIqqMKF3lg1squqhF157MLgrerrqMCGhoX_lZvT2FqpTJhN55Yq_Wmj7NzO2e9HxZSAby33MXYUi5y4b6QG5C7QhuUYk3PljaLMbyaLy3ZthYTV0v7HZpFlEpcWLhRP3yGPlFTe2kiYssH8JwkZZJcZe0ECJwsehad2ARQdvERFjL1MaYm_45yxNFhaBt1NICjkB7I8A7JzXMYRB3zSwXvhhqLtPTQsFynnBnbWMBqLnIqfuB7vmdu6AmHhaBwn3w_Jl5FZUDJX-eXRKfNQbydBHSn5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=I2rDGTYBCwKQEVyZuWZzhVe9Qaem8PL8Lt2B6ZN-V7VDYu_3CVXxcTAPeZkIqqMKF3lg1squqhF157MLgrerrqMCGhoX_lZvT2FqpTJhN55Yq_Wmj7NzO2e9HxZSAby33MXYUi5y4b6QG5C7QhuUYk3PljaLMbyaLy3ZthYTV0v7HZpFlEpcWLhRP3yGPlFTe2kiYssH8JwkZZJcZe0ECJwsehad2ARQdvERFjL1MaYm_45yxNFhaBt1NICjkB7I8A7JzXMYRB3zSwXvhhqLtPTQsFynnBnbWMBqLnIqfuB7vmdu6AmHhaBwn3w_Jl5FZUDJX-eXRKfNQbydBHSn5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به هواداراش: این فوق‌العاده است. من می‌توانم احمق‌ترین حرف‌ها را بزنم، و شما تشویق می‌کنید.
#میدان_انقلاب
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/152034" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152033">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: شاید نام یکی از اقیانوس‌ها رو هم عوض کنم. ببینم چی میشه
به این فکر می‌کردم که یا اقیانوس اطلس باشد یا اقیانوس آرام. اسمش را بگذاریم اقیانوس ترامپ یا اقیانوس آمریکایی‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/152033" target="_blank">📅 00:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=UN7S3KTTmsHagP-ulyNaAmI2GU60YSe9bFKwSn2CORtqVOmQzoLm8x14hojw_R8Oyfsf3sAnwGZuOnqf4NqVcAb6hQku2U6Xqn1roF_0QoTN0iSHRZm1ID5N3Xe4fxfeo9Rizva4mEw573G7JAcVcCBgdu0vqS1wLP_CwvOFkCn8FZD8pJWuULkNKGxBuXpepauTsuvN-1UIpBzZNai58jHnycsGIQk_vUjK80YiNeBINuXhokY6ziDGMJD2x3K089kfAz93S-o-WVRpiCtm3fHDboF8g1k1y2_GI3k88MNmYOkGyVkBMypREh98s-1xbCNzIzpzYnjIkUaD4PrP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=UN7S3KTTmsHagP-ulyNaAmI2GU60YSe9bFKwSn2CORtqVOmQzoLm8x14hojw_R8Oyfsf3sAnwGZuOnqf4NqVcAb6hQku2U6Xqn1roF_0QoTN0iSHRZm1ID5N3Xe4fxfeo9Rizva4mEw573G7JAcVcCBgdu0vqS1wLP_CwvOFkCn8FZD8pJWuULkNKGxBuXpepauTsuvN-1UIpBzZNai58jHnycsGIQk_vUjK80YiNeBINuXhokY6ziDGMJD2x3K089kfAz93S-o-WVRpiCtm3fHDboF8g1k1y2_GI3k88MNmYOkGyVkBMypREh98s-1xbCNzIzpzYnjIkUaD4PrP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران:
میتونیم خیلی سریع به این ماجرا پایان بدیم. اونا هنوز نمیدونن چقدر باهاشون مدارا کردم و مهربون بودم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/152032" target="_blank">📅 00:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152031">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: ایرانیا میگن همه رو می‌کشیم، اونا میگن الحمدلله الحمدلله! بچه‌ها شما دیوانه هستید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/152031" target="_blank">📅 00:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152030">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_68_yXS4yXzBJalwVZAdpp2PIVgNrN8FWMhBx3ZLEN0peGBnxhU4RCfLzyACmMyDIHJgovfOxFRMVDbLu8CH5ZCjEWpwTY5J8WRKRzJmRM7ZSKErO79F5HMnPpGUUW7uz_2EX9yE8RA52zVXwZj7hj8q5B4kXyL690opwy5oeiEjV3VBR7xXbJx7y8KHCezYp18h_iVpf8Nxs7HPXQrpQHiWedl8Y7LhdaH1abqUFiyhMJBASWp_vlmU8Kc8ztFj__Wv68GW_1AUjyuEbamLsXCbnAC3j8uBZsmBKeMiBZQFGiytbqQnhOg8ey2i9h_kbCwKtoVo5c7V-_LgrmuHUko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_68_yXS4yXzBJalwVZAdpp2PIVgNrN8FWMhBx3ZLEN0peGBnxhU4RCfLzyACmMyDIHJgovfOxFRMVDbLu8CH5ZCjEWpwTY5J8WRKRzJmRM7ZSKErO79F5HMnPpGUUW7uz_2EX9yE8RA52zVXwZj7hj8q5B4kXyL690opwy5oeiEjV3VBR7xXbJx7y8KHCezYp18h_iVpf8Nxs7HPXQrpQHiWedl8Y7LhdaH1abqUFiyhMJBASWp_vlmU8Kc8ztFj__Wv68GW_1AUjyuEbamLsXCbnAC3j8uBZsmBKeMiBZQFGiytbqQnhOg8ey2i9h_kbCwKtoVo5c7V-_LgrmuHUko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایرانیا میگن همه رو می‌کشیم، اونا میگن الحمدلله الحمدلله! بچه‌ها شما دیوانه هستید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/152030" target="_blank">📅 00:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152029">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/152029" target="_blank">📅 00:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152028">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت انرژی آمریکا: ۴ میلیون بشکه نفت از ذخایر استراتژیک برای مقابله با اختلال در عرضه ناشی از شرایط جوی، خارج خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/152028" target="_blank">📅 23:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152027">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86374dcf2.mp4?token=AvNOx8BFkzwCuOJu0UZj1qYTyUpHuJgILIOfvej7L-r6iq_VbVEdgp3aI8wkvglgQErYrswAqjDEo3H39Vo7FAW3EMmq_B2mjuU4hNVj1M9B7UyY6ys49sjQkI_Y6N5JAMMhObiN6KZ9apjCAMy1TPYy8ivSo5RuVDOAQtmsqN0mzHPNE-L0GVT1a6T2o1QzlNFg3GWdJVobPwuP_XZYjTJCD8qM3zt8KUAz1qktgOOcsUELVBHbLMvpkRg93o7geS2x6PfVMrd5jwY5dE-N3rnnDfLHK7X5_FvZMklH68HzM4StSmJxBiiiPazdvaBMFrGtnvOdHa5q99waJ4js3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86374dcf2.mp4?token=AvNOx8BFkzwCuOJu0UZj1qYTyUpHuJgILIOfvej7L-r6iq_VbVEdgp3aI8wkvglgQErYrswAqjDEo3H39Vo7FAW3EMmq_B2mjuU4hNVj1M9B7UyY6ys49sjQkI_Y6N5JAMMhObiN6KZ9apjCAMy1TPYy8ivSo5RuVDOAQtmsqN0mzHPNE-L0GVT1a6T2o1QzlNFg3GWdJVobPwuP_XZYjTJCD8qM3zt8KUAz1qktgOOcsUELVBHbLMvpkRg93o7geS2x6PfVMrd5jwY5dE-N3rnnDfLHK7X5_FvZMklH68HzM4StSmJxBiiiPazdvaBMFrGtnvOdHa5q99waJ4js3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها دموکرات‌ها هستند. احمق، احمق، احمق، احمق
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/152027" target="_blank">📅 23:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یک منبع یمنی به المیادین: برخی سرمایه‌گذاران و شرکت‌ها با ترس از طولانی شدن جنگ، خروج از عربستان را بررسی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/152026" target="_blank">📅 23:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز به نقل از منابع سعودی گزارش داد که در فرودگاه ریاض، ۵۰ نفر مجروح شده‌اند که برخی از آن‌ها در وضعیت وخیمی به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152025" target="_blank">📅 23:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون شلیک موشک و پهپاد به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/152024" target="_blank">📅 23:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رئیس اتحادیه صنف طلا مشهد: فروش آنلاین طلا بدون داشتن فروشگاه فیزیکی و تاییدیه این اتحادیه، مصداق کلاهبرداری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/152023" target="_blank">📅 23:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جنگنده های ارتش اسرائیل(IDF) از ساعت گذشته بر فراز مناطق وسیعی از شمال، شرق و مرکز سوریه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/152022" target="_blank">📅 23:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش قدرتنمایی جنگنده های نیروی هوایی ارتش برفراز برخی مناطق کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/152021" target="_blank">📅 23:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کارشناس شبکه خبر: دلار بی‌سابقه خواهد ریخت؛ آمریکا به شکل شگفت‌انگیزی شکست می‌خورد؛ آماده باشید، طوفان تو راه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/152020" target="_blank">📅 23:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt4HX09k82IdGoa_7AVtV-e_PawTRYWZGsyH1OFx8PYWMdvcTuJh_0Yj3Fjw58vUFY9g52utzzsbYZUuX3KUotB3ZFJ3U_xa4SaIudw4ChZIeK_moHkyDdt2O90UHfHTXalPnMA9cD-XzjSfh5of3bbD4cSonrq6D546qUgcznjb-tZNWH1GE14Oq5gpJGJSu5jLkz-dKP5ZP3V5aVXhkjpPlq1zuIGItkx880Bme2WhtjOv8jofGm4QWbdc3zjKHOcwrvYYvJ_2veiRTOSho-LQuvl2ypFEk3VPeRgUfOOsgtWA3ZrEm9QZslnkjl3d8jOQNDPN2LJ0Df6pMf_dPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح: کربلا رو هم سیاسی میکنیم چون اعتقادمونه
#بدعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/152019" target="_blank">📅 23:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مجری: الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
🔴
میرسلیم: این دیگه میل خودتونه. توام برو اونا رو سوار شو
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/152018" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا: به چندین کشتی در آب‌های نزدیک رأس‌الخیمه امارات متحده عربی دستور داده شده است که محل‌های لنگراندازی خود را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/152017" target="_blank">📅 23:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bvt52Y8hrvGJaENPb1G9AD-0ktc_Wqn1WD2hRjx1DbmyOUFny5Jcqe9w6c8mH4ZcnhyKMzR_du_ZP-xFxmbCc4Kfu6D9cCYApUJ293zPP2RTqtUJwfTM_dEjlo5g6XjYW-WfZ0As8QS-enameA6bZpjwjAkbyVDgSGqsHlyercnMZDBl-agTNaKBstQbv1Y5ixOze2vl7YaIMsBJpv6PoMH6zVqymJSwfs_e8LHiGOlgm0lL3Ip-ACk7wWGxkcC-Er6d9XM93o_73I1MX-iIj1CjBlN3bAEeKUcCZE8Mt838OKTiwMoAzzhbky0aX4RTw7z1NSEXAxoJpfOeaJce9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0dujuBPpSUWZ106Sl7Lo3xVvw49B4DjVNrYPq_xgh8S4AiWbM17iCtm2McRy4QPaUd2CKEQb2Bq_9kKFZgvY1Ud4EmBjVb0UzjgQeSzuU1ymy9_G9XqyfaC6SVqtigdxeScIhsW9jxH4OizJYxreIAJP9ty5HOJeWkews8aUNTQMmB5wnpiIw00GxUqPwNRGDgH9do89BG9AQWR3MxJmU1RO65LucyPasfbxfFtokuT64WkkUOdkx1C-hh-y4cE4rbrQOqbKIaHWHVWXcWxhyOSCOw6arRtXnm7V-gq6NP0H049Fg5WQJkbvX0XnBadooyYboo-pT_lwxKcdT3nOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دانشجو های بسیجی جلوی سفارت فرانسه تجمع اعتراضی برگزار کردن و از دولت فرانسه خواستن معترضینو سرکوب نکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/152013" target="_blank">📅 23:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیویورک‌تایمز: در مذاکرات محرمانه مسکو و واشنگتن در حاشیه سازمان ملل، آمریکایی‌ها سه مشوق اقتصادی پرسود را روی میز گذاشتند تا روسیه را به پذیرش آتش‌بسی محدود در حوزه زیرساخت‌های انرژی یا در دریا ترغیب کنند
🔴
مقام‌های اوکراینی از میزان امتیاز‌هایی که کوشنر و ویتکاف حاضر بودند به روسیه پیشنهاد دهند، شگفت‌زده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/152012" target="_blank">📅 22:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/152011" target="_blank">📅 22:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCwzrggLH-1-R542TP7urH82n5UISRagJwGhvZuBVBQOa3RXPYhvp2C8-6X3RwXEaiDfw5khpevAhvWwntSwYaw-JhKz-I726JTibl7z2aNwrYlznI6J-8CaI5Y3-BkfhhiKxZSPTQOchk9QQgaWXuARFLhINePtOMc3E-xi2bOT3w1m-S0pEvqGQUF1A71flTF2HURYsMzICq7iFToBurP2bx1Cdi0HUKpqLjUme1Agx0uZH_OQYBhaErfb0D1YKu366Kv0n30VOkRj-jAO0F6u6hKMUU8ZAfFcAcT0V34ftQvn8QbFWjZNzrIhKDvGbPH-UKYK53298GBN8M18Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: دموکرات‌ها، همراه با شرکای جرم خود، رسانه‌های خبری جعلی، در حال تلاش برای ایجاد روایت کاذب هستند که دونالد ترامپ آنقدر «نامحبوب» است که جمهوری‌خواهان شکست خواهند خورد
🔴
در واقع، دقیقاً برعکس است. من آنقدر «محبوب» هستم که جمهوری‌خواهان پیروز خواهند شد و این موضوع با میتینگ‌های رکوردشکنی‌مان اثبات می‌شود (از جمله میتینگ در تنسی که تا چند دقیقه دیگر در آن حضور خواهم داشت — به زودی می‌بینمتان!)
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/152010" target="_blank">📅 22:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: دو مقام آمریکایی و یک مقام اسرائیلی به من گفتند که آمریکا از اسرائیل نخواسته است پیش از انتخابات، حمله‌ای علیه ایران آغاز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/152009" target="_blank">📅 22:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwgFicnz6vWIaksqDxF0D9C91PUBHLXcQCSwhhVa7F-5q9KGNa0vE8yl--zMSRn7ux3RUxjTcHUYO8K7cx2NqUqJklDXNd0nDXm7HcS1I6JebDuCUDMXRg9PWPmfKfatIor3CTjVUkl4kBIG7ml1FZ32liNsgrPuyWbSLoJUSTMovxVxNb40DUkknQKCfm5p-LRGZOR5zBQ0B1RVAgJIA-Na49QX1yL5lKtNOZ8pccO2k8ud9HY1U1s_yFAhN-qfUGAxraCXFSn0SLNnpnSnS4TwQjDRF2HEnbHkRl99xJtNWO1LZiHavJWtQBi1i2Q_hjIAZ6g_mRXOxoF44GBcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد رمضان؛ تحلیلگر معروف عرب : به زودی آمریکا و اسرائیل به ایران حمله میکنن و انتخابات اسرائیل به تعویق میفته. ایران با یک سلاح بی سابقه مورد حمله قرار میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/152008" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
حزام الاسد از اعضای سیاسی انصارالله یمن (حوثی ها) گفت: اگر آمریکا، اسرائیل یا هر دولت دیگری در حمله به ما مشارکت کنند، سریعاً پاسخ آنها را خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/152007" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
صداوسیما: سود سهام عدالت ۱.۵ میلیون نفر واریز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/152006" target="_blank">📅 22:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
العربیه عربستان اعلام کرد که در اثر اصابت مستقیم موشک بالستیک به ترمینال شماره 3 فرودگاه ریاض تاکنون 6 نفر کشته و بیش از 70 نفر زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/152005" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ضرغامی: چون شریعتمداری کارتون پلنگ صورتی رو دوست داره بیشتر تو صداوسیما پخشش میکنن و حین پخش بهش خبر میدن تا از صداوسیما تعریف کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/152004" target="_blank">📅 22:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
هواپیمای توقیفی کاسپین در ترکیه به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/152003" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsIlLvDXaUE5zN7ND49HR9zgeLOeIX3rHd83_uqvS7U-LQ_DaQbLGyP95O9VIJ8GgczEFqufOg4USo5oNHewyPBOOm0dWu4tFWfe3EQoHoG1WVv0NJXUlBF0Ccfy6GlJ9F68hxwV2vRPNDVb_y-c6YN29P4vKyvUlbID8NcQNRfBJF36THtGUabCPTEyb16Pf1LlH4RD96gtcHwDeSU1zO-vRfdiTdISxadHAty2mSJFDISoctmr-tzBt4A7e_NrHsW8b3Jle34EEkgAZ5i3yPsEHm9BxvjK9z61fnHzZl3v2JDmYfpMh9m6m0VleYZHByIIxzxP5Nu1XmRfay3Apg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون یک هواپیمای دولتی ایران در قطر به زمین نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/152002" target="_blank">📅 21:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXKt9evN43LdSa_QnATpsA-r8pVFLkA05i2_tOmpiKxH6nwGT8LWAkydOscPjcJNpFJ9ziYqS66bHxcqrI_L_GJmDNooJ_O-89KBYF-WqHVA82tigP2CbVLomChyfCShFLWdTfkPGTHFmRmaxKEz27PD26wMeAYB5HyZwdYiDiOHwsMGKhjRccCU_Yl_PtMAfMZOKQxTd7MhY82dUsQoXJBWvzbsSakTTv1HF6kzXGvdBsYm42meNhp_5aC3ZJsVmPrFg4PJzCpzEaY0f5f3xusVc75KmTpHfrUIYo_v3wudCyeYG-0j8nqkVNC5EcIa4JXSlRfQvNXoCy-X-q99yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: یه آشی برا ترامپ پختیم که نگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/152001" target="_blank">📅 21:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
هو شدن بقایی سخنگوی وزارت خارجه در اجرای ارکستر آرش در سالن اسپیناس تهران و شعار بیشرف بیشرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/152000" target="_blank">📅 21:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3868b8a40.mp4?token=Zrg5YkRFWEsLu2wESTOOq2kKC5ZHv2tY0yTeJORRXNdcdphhJcBZvzwmj0vJBzzyKd4s5ehYSjFZGnqFVW4XAnRMb5YQOpFezA0r9rtYdOtuplswDfUcMSIZgRTyozxfJvxkYzCeAw7cICo_TLEr2Q2NoY_joqmEwrpXWTP46DW22YLgNqISqGUQdazL9GckUJR5ot4-U7nNUbryCKymFHht9nz2ghQoOS88VO4bHvtml3lQr4E0QwK4R6kZvpD3_zfyXGR0u2AVB5mbn1dXMPHEtdeM0ROrjmt1l45WWFSP3ElrwW26erBEFICb51KB80Im4Cr47MNekCYnQvL_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3868b8a40.mp4?token=Zrg5YkRFWEsLu2wESTOOq2kKC5ZHv2tY0yTeJORRXNdcdphhJcBZvzwmj0vJBzzyKd4s5ehYSjFZGnqFVW4XAnRMb5YQOpFezA0r9rtYdOtuplswDfUcMSIZgRTyozxfJvxkYzCeAw7cICo_TLEr2Q2NoY_joqmEwrpXWTP46DW22YLgNqISqGUQdazL9GckUJR5ot4-U7nNUbryCKymFHht9nz2ghQoOS88VO4bHvtml3lQr4E0QwK4R6kZvpD3_zfyXGR0u2AVB5mbn1dXMPHEtdeM0ROrjmt1l45WWFSP3ElrwW26erBEFICb51KB80Im4Cr47MNekCYnQvL_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هو شدن بقایی سخنگوی وزارت خارجه در اجرای ارکستر آرش در سالن اسپیناس تهران و شعار بیشرف بیشرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/151999" target="_blank">📅 21:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151998">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8616439e.mp4?token=jqvLm7EovCgMPcOMQg9g9-zMXFK5EdmgiiLNlzFzaiEJOvBx_KwobraG2XrHZlxYRZwzspn8WovCDxTsW3EVZzBYdqr6julfwpQSKmMKupkgam7jmRpE_QGcu4GrrPdKTiK6d6Q_xEt2frplBiNhBejWcHiJIv-1IGLy3kjsCc65AqPNefLqY0ZgUBOPbcOw1UnNYUQuT541M-4ZfrT6CAolo5mRiKJ39JHkNzBbYU3jtY2odCgYeDlnBYpmHtpRHuQ1M_dSjZQGbroJGedqHgUpmoorZEpu5sBRMA1OlyCvfjpls_UC6fGjwSsK_3zoyN-rCEc8cbidzx2NzVH7_JYvozcmya4G1OMEQLWBQJTuzfjIumPPmCqjPGGdeE3ebRr_SblrKLOecOPcJ4WQGxaNZm0mZ5Z5ZRlSs-TcS8U9bUBomrVsvfpELYcJk7UdL4WlwTVtOvyHDqGtylydz6bVfw0z8YgPkjZajeulpSTxyOnTA3-MM9iTMAAl6TOBhEGEhy9GxZts8b1GZqre7q6yoq8XQyT9U0oWvGh_Kll2gUyf5J126nx790RFDJE1ua4GJD4ebAAJB2t4LZE3vFcI0DUV7EoyRlGAbWpPxL1NIsuWb166k9yZZZURiNCxQARMg6m05Jz5CpZLpJkBygSED-4G-bc63C3FhF028RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8616439e.mp4?token=jqvLm7EovCgMPcOMQg9g9-zMXFK5EdmgiiLNlzFzaiEJOvBx_KwobraG2XrHZlxYRZwzspn8WovCDxTsW3EVZzBYdqr6julfwpQSKmMKupkgam7jmRpE_QGcu4GrrPdKTiK6d6Q_xEt2frplBiNhBejWcHiJIv-1IGLy3kjsCc65AqPNefLqY0ZgUBOPbcOw1UnNYUQuT541M-4ZfrT6CAolo5mRiKJ39JHkNzBbYU3jtY2odCgYeDlnBYpmHtpRHuQ1M_dSjZQGbroJGedqHgUpmoorZEpu5sBRMA1OlyCvfjpls_UC6fGjwSsK_3zoyN-rCEc8cbidzx2NzVH7_JYvozcmya4G1OMEQLWBQJTuzfjIumPPmCqjPGGdeE3ebRr_SblrKLOecOPcJ4WQGxaNZm0mZ5Z5ZRlSs-TcS8U9bUBomrVsvfpELYcJk7UdL4WlwTVtOvyHDqGtylydz6bVfw0z8YgPkjZajeulpSTxyOnTA3-MM9iTMAAl6TOBhEGEhy9GxZts8b1GZqre7q6yoq8XQyT9U0oWvGh_Kll2gUyf5J126nx790RFDJE1ua4GJD4ebAAJB2t4LZE3vFcI0DUV7EoyRlGAbWpPxL1NIsuWb166k9yZZZURiNCxQARMg6m05Jz5CpZLpJkBygSED-4G-bc63C3FhF028RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر از لحظه وقوع زلزله ۷/۶ ریشتری در پاناما؛ ریزش بخشی از ساختمان روی سقف خودروها
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151998" target="_blank">📅 21:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151997">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پاپ لئو از تمام کشور های حاضر در جنگ خواست سلاح هاشون رو به زمین بزارن و صلح کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/151997" target="_blank">📅 21:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151996">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Feef-XiF9n_rgJT5jioUOkHE8M4BZuDNx54649kinAEaUughrJvCKc-l6Hznr8tTbwl0OWQA6ynhrP-EeR63uzNh_XrJcQ_ypHwviDR09cBchnvZ0wl8-CjrN7FDNXKtVT1BTDJCsyYrGM05pNzj207k2yhLXC6OXY6KDJBUuu0Ki-q7CppeXYjfYFS8Yxl6kplzZxkwlY9mk4cL2e2tjE2VlAqNYGTiRaSO9GAyX-re5Bb1WPzYND5jypdPULCrHKEIL_B9hG92kI42BkSlWQx4ddzKqZmyw4bdhnUIzcZu0WX2M-LbTFRVIBiWbKhCQB7Ps8CL02Kt8DU9KJy77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: چین تو دوران مائو خیلی منزوی بود اما تغییر رویه داد و عالی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/151996" target="_blank">📅 21:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151995">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی: مذاکراتی اخیراً میان نتانیاهو و ترامپ درباره حمله به ایران انجام شده اما تصمیم نهایی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/151995" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151994">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
نیوزویک: ایالات متحده حمله به ایران را بزودی انجام خواهد داد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/151994" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151993">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سپاه: یک سوپرنفتکش متخلف حامل نفت خام در یک آتش عظیم در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/151993" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151992">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل به نقل از یک مقام امنیتی: مذاکراتی اخیراً میان نتانیاهو و ترامپ درباره حمله به ایران انجام شده اما تصمیم نهایی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/151992" target="_blank">📅 20:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f635d314c6.mp4?token=AkOpw7DdJD7lBR_d5f7ikwDD6ODrBTXxK8_DZQHJcSIQpXRoDzw4DU48_FiePtjV9p3tiRNglQTCw_9feFpaSpPnDAb0Y5BK4uuuf8SeRjwHft6eUkmsEI-5vMrsc9TrHQqtyyYmG_KbKcF8AUL0ljokpyseZVLfqqKF2ZPRwa7HVHyiSRbMfEw0MLPddq8CxSFf1hs1ZIrVYtXe64vWjX1V9LB3SrzUQIhbBq9Xgc5adwU0AdJ1KDUZs_gpGr3S1yyqU0b39zV4kSfa3rX6eNzl1wdNofmfdEZMEDBXwZHw1dFtcFr5vvxhLCq9YFMeZGkXriJK5Y1rGIRAXDTnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f635d314c6.mp4?token=AkOpw7DdJD7lBR_d5f7ikwDD6ODrBTXxK8_DZQHJcSIQpXRoDzw4DU48_FiePtjV9p3tiRNglQTCw_9feFpaSpPnDAb0Y5BK4uuuf8SeRjwHft6eUkmsEI-5vMrsc9TrHQqtyyYmG_KbKcF8AUL0ljokpyseZVLfqqKF2ZPRwa7HVHyiSRbMfEw0MLPddq8CxSFf1hs1ZIrVYtXe64vWjX1V9LB3SrzUQIhbBq9Xgc5adwU0AdJ1KDUZs_gpGr3S1yyqU0b39zV4kSfa3rX6eNzl1wdNofmfdEZMEDBXwZHw1dFtcFr5vvxhLCq9YFMeZGkXriJK5Y1rGIRAXDTnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من جلوی چین را گرفتم، و جلوی تایوان را هم گرفتم. این روند به همین منوال ادامه دارد. کی می‌داند چه اتفاقی می‌افتد؟ اما من جلوی آن را گرفتم.
🔴
من از وقوع هشت جنگ خطرناک جلوگیری کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/151991" target="_blank">📅 20:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151990">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=H6BZuK3QxZn3T8CwPu5dtDkFU6OQnKbgV-bQvG6N_CZvyzK18kuRULMVq5lXZcfZMEt2ANJCRGqpMEfO6tsoRvzwPvP8ZTFT4KXYyQrrUY8eQmA60WrmsWQ_W3XLpDQhHA93eg911jGHWx5tGEJ7WIfnGNVGPMMH6AYzfNqF9135f4HyfYwHKKXv9r2ZkEyn0cSnveBdb8AGAdmnl0W4V9lJJx4BpL7XctSeALGn3Qf5I8ZpinESSZv5ooUXsy_wtKaoIasc5WQa1VIETAiXM7F54A3Ft_wZfyNZAL2aK4mQnBK4FT9wtDzncELGahI2xBOGTF0zfLS7pN7-YjfuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=H6BZuK3QxZn3T8CwPu5dtDkFU6OQnKbgV-bQvG6N_CZvyzK18kuRULMVq5lXZcfZMEt2ANJCRGqpMEfO6tsoRvzwPvP8ZTFT4KXYyQrrUY8eQmA60WrmsWQ_W3XLpDQhHA93eg911jGHWx5tGEJ7WIfnGNVGPMMH6AYzfNqF9135f4HyfYwHKKXv9r2ZkEyn0cSnveBdb8AGAdmnl0W4V9lJJx4BpL7XctSeALGn3Qf5I8ZpinESSZv5ooUXsy_wtKaoIasc5WQa1VIETAiXM7F54A3Ft_wZfyNZAL2aK4mQnBK4FT9wtDzncELGahI2xBOGTF0zfLS7pN7-YjfuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: شما گفته بودید که قبل از انتخابات میان‌دوره‌ای به ایران حمله نخواهید کرد. آیا این حمله اخیر در عربستان سعودی این موضوع را تغییر داد؟
🔴
ترامپ: ما این موضوع را بررسی خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/151990" target="_blank">📅 20:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151989">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a642012a0a.mp4?token=kf4aNeqrCxJvMQnAfjW7nt53QmAUEJ8uDv4IoG8bMO4hyfTUrB6dBjECx5gMDKsBFNNYdx2uEnaPSoAPdpgtmmzGpHLF9QoY-20WT_gnUFgzYFeCjaw58EKq1vTExgg8jz50Qcw3kZWe1cGYvC_3K2hv43y4niiXsHzs2RYOnRCQ-187Y55nBMzBPPaT5kz-fxoSZCx2LqaZvmo7Q-prqoG7Y17jl01ynr0xVDNj72ebs4hjLqGCGHXESilqXFEH6aagGJVZoDH8-7oKgtRabVYAXy3kiTnas34oOvgeiVDq2TDafdiprJQH2PPDcRn2F113RsNM31XoktfxmNwmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a642012a0a.mp4?token=kf4aNeqrCxJvMQnAfjW7nt53QmAUEJ8uDv4IoG8bMO4hyfTUrB6dBjECx5gMDKsBFNNYdx2uEnaPSoAPdpgtmmzGpHLF9QoY-20WT_gnUFgzYFeCjaw58EKq1vTExgg8jz50Qcw3kZWe1cGYvC_3K2hv43y4niiXsHzs2RYOnRCQ-187Y55nBMzBPPaT5kz-fxoSZCx2LqaZvmo7Q-prqoG7Y17jl01ynr0xVDNj72ebs4hjLqGCGHXESilqXFEH6aagGJVZoDH8-7oKgtRabVYAXy3kiTnas34oOvgeiVDq2TDafdiprJQH2PPDcRn2F113RsNM31XoktfxmNwmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جنگ اوکراین: اگر من رئیس‌جمهور بودم، این جنگ هرگز آغاز نمی‌شد.
🔴
هیچ دلیلی وجود نداشت که این جنگ بین اوکراین و روسیه آغاز شود
🔴
این جنگ به دلیل نالایق بودن برخی افراد شروع شد.
🔴
نباید هرگز آغاز می‌شد. شما نباید ۳۰ درصد از خاک کشور خود را از دست می‌دادید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/151989" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151988">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d6ccae64.mp4?token=rZjrvsZ1ggEQPP_5Vu6RjE_FlBaJ9CEvGq6zXkef51NSyVhwVIorOVX3L5OQ0iQXO0K9gIFDzCSM6fsKH1XyRR1clQLSUvQcHLkwpv5pDJUFCOkagaMGvaEFkluSJXN6j8Xvg1CeYpMfGbWz7Xc4X5-5tcS6lReQtz1_apvDmMfTYs_C0_lU38yP3aLvB-xal4tm6B8eAsnQm1FMbdors86_1V3OWEFURV8uiHq-_5A5lpGL4PtxZmnG8__ASDiLO0yHd_GLoDeu0-SSd0gRdIGGl-Z9ZHFZTsnu4Ll0sDdrE1PF6I2ejH1oE4T0z3nWlFj7y_tKZTzuwpeW3lCgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d6ccae64.mp4?token=rZjrvsZ1ggEQPP_5Vu6RjE_FlBaJ9CEvGq6zXkef51NSyVhwVIorOVX3L5OQ0iQXO0K9gIFDzCSM6fsKH1XyRR1clQLSUvQcHLkwpv5pDJUFCOkagaMGvaEFkluSJXN6j8Xvg1CeYpMfGbWz7Xc4X5-5tcS6lReQtz1_apvDmMfTYs_C0_lU38yP3aLvB-xal4tm6B8eAsnQm1FMbdors86_1V3OWEFURV8uiHq-_5A5lpGL4PtxZmnG8__ASDiLO0yHd_GLoDeu0-SSd0gRdIGGl-Z9ZHFZTsnu4Ll0sDdrE1PF6I2ejH1oE4T0z3nWlFj7y_tKZTzuwpeW3lCgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها جایزه صلح نوبل را به شخصی دادند که هیچ‌کس از او چیزی نشنیده بود. تنها چیزی که ما می‌دانیم این است که به نظر من، او بسیار ضد اسرائیل است.
🔴
مشکلی در نروژ وجود دارد، اجازه بدهید به شما بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/151988" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151987">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb64bf3ad.mp4?token=heug5B2w8T06lsuESd8kM258zEEn3A9cTKf9ZoC8eyPjFmXVfBHtQQNSSZyxnl2PyfYd66TaYK12BUt1uPnjszxx-i0GekrzbMIXcrckPk3wRynu-CjhM6IH1Pj8mKctZrv39robfQbBnzTv9iXHyoSIqqvAXzeYzgPsSUcC5OkJjwJoIHMoPBDwghJaVqw9vhNRXReVOYlwciCjGDuPit6wz2uNgW-KWhY2jiV6EaXFBwoqfLQ59cCm138yh5HPTG9nBg1XeLh4icsicWPZL9ZL0waLBKSECR4fKhLcpI9Jn6B3sl_bPf1XLdkqrIkHaqL0CKxJPoKBh01GhzciJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb64bf3ad.mp4?token=heug5B2w8T06lsuESd8kM258zEEn3A9cTKf9ZoC8eyPjFmXVfBHtQQNSSZyxnl2PyfYd66TaYK12BUt1uPnjszxx-i0GekrzbMIXcrckPk3wRynu-CjhM6IH1Pj8mKctZrv39robfQbBnzTv9iXHyoSIqqvAXzeYzgPsSUcC5OkJjwJoIHMoPBDwghJaVqw9vhNRXReVOYlwciCjGDuPit6wz2uNgW-KWhY2jiV6EaXFBwoqfLQ59cCm138yh5HPTG9nBg1XeLh4icsicWPZL9ZL0waLBKSECR4fKhLcpI9Jn6B3sl_bPf1XLdkqrIkHaqL0CKxJPoKBh01GhzciJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره پخش زنده اعدام نیدال حسن، عامل تیراندازی در فورت هود:
شاید با نشان دادن این اعدام، افراد دیگری از تکرار رفتاری که او انجام داد، منصرف شوند.
🔴
من در این مورد تصمیم خواهم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/151987" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151986">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / ترامپ: در جریان حمله به فرودگاه ریاض قرار گرفتم و تصمیم خواهم گرفت؛ شاید به حملات عربستان به یمن بپیوندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/151986" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151985">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: زمان آن رسیده که اوکراین رئیس‌جمهور جدیدی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/151985" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151984">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: زلنسکی بارها می‌توانست جنگ اوکراین را پایان دهد، اما نخواست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/151984" target="_blank">📅 20:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: ایران در وضعیت بدی قرار دارد
🔴
خبرنگار: چرا اقدام نظامی علیه ایران را به بعد از انتخابات میان‌دوره‌ای موکول می‌کنید؟ چرا همین حالا اقدام نمی‌کنید؟
🔴
ترامپ: ممکن است اقدام کنیم. خواهیم دید. ایران به‌شدت در حال شکست خوردن است. ارتشش شکست خورده، نه نیروی دریایی دارد و نه نیروی هوایی. تورم این کشور ۳۰۰ درصد است و ایران در وضعیت بسیار بدی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/151983" target="_blank">📅 20:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQyPtPIK7k4tvfOZcBuOJ6qNxkoL4qCG7oOPxLnD1J0mmZLnsnzQl2nA176Gqld89734wlWnz_s-hFlYXbGYqDioBoSfdhN1cFK_fNRDf06vgRKSYTHxcpnPzOl_fQ9TtugEwSY6_RNRP5hCns_CkHmzg4Fj9a4itK89CBz54wAX34Bj6aWXA6txgBy-PzdY9yna_P0ArHkJytklaqogE26TN6jl7mSJZYqdHgUxlmbWSOaInLLpdA8MOIT8tjM8hylieeOdquGdXaAu6srSpkKxJwTp36otPwteECK2VM-Ksszio46MdX1rnNObR6aLFjxe5zvSMNbJK9U9SkJ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۱ هواپیما از فرود آمدن در فرودگاه جده خودداری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/151982" target="_blank">📅 20:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLP2tfXVeDM_0PLs0vWgLwk3P-yfnb02YPlcGSom3oK5yHKaTDbK7FK9Lw_UujKOVkYqFo-0l9pJxayDmvs-9vOZT9OELvC4yik_mCubIUw7gZqpPXhL_yluGdmin6rfa4fwVzl1jbIq5WdeNmOabCQE6MHJiXvcqbQ-_N0OWxG0vJCM9aHLkHV-lc43-pmfUCsfAD5aqhiseCTXZYjMiNxvZZvDyYWty48kzaguUCRQ6yiq4JMPBPlWsRyISJoIKz67nTDOObOLn8SqhsB_M7xiAkMmaE1mIxC_nTeN9P2anG9Gx-oLCzk41xvBZvkDy5KvD92Lp1Noh7pfcTU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون هواپیماهای هشدار زودهنگام سعودی بر فراز ریاض پرواز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/151981" target="_blank">📅 20:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
روغن با افزایش ۴برابری، رکورد گرانی سفره خانوار های ایرانی را شکست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/151980" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151979">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت ارتباطات: در صورت تکرار جنگ، احتمال قطع اینترنت وجود دارد / مشخص نیست که این موضوع در چه سطحی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/151979" target="_blank">📅 20:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ایالات متحده از شهروندان خود درخواست می‌کند از سفر از طریق فرودگاه ریاض خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/151978" target="_blank">📅 19:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرگزاری تاس به نقل از منابع روسی:
ویتکوف و کوشنر طی دو هفته آینده برای دریافت پیشنهاد پوتین درباره ایران و اوکراین به مسکو سفر می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/151977" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فرماندار ایالت پنسیلوانیای آمریکا:  در حادثه تیراندازی در شهر اِری در این ایالت، ۹ نفر کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/151976" target="_blank">📅 19:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تیراندازی پشتِ تیراندازی ۵ نفر در جورجیای آمریکا کشته شدند
🔴
رسانه‌های محلی خبر دادند که در پی تیراندازی در یک اقامتگاه در شهر داگلاس آمریکا، ۵ نفر به ضرب گلوله کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/151975" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=qBTkVyO7AiQH847eUvC3W1O67mBFoN02euFsLM7fWvAv2t57SSpc0nCIw4BXYltXLaWD4WEqguJqlkjvjiW3finXyLH8637ZrAAC3wrMYYKPdXV5TVfvWclz5vPKUyFspE_tY2fnYU-HkjSwtCoYWOO283Iyx81x2G6tdsO7JIqf-I7u8ninHj8g9Xsi8_YEqGYFydMMh6n4uBPexfi5UgmKrdz8hXtlNlnpMuIqtczmKSlVZvREFjvuYq3q7ynv6wMiusn936YBJvDdPaB4znbvpIsfap1sZndj5f4nfpIJbiYWUeS-3k2k1wphhMJ0WDkqRbw_KbegucZurGTRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6726b774fe.mp4?token=qBTkVyO7AiQH847eUvC3W1O67mBFoN02euFsLM7fWvAv2t57SSpc0nCIw4BXYltXLaWD4WEqguJqlkjvjiW3finXyLH8637ZrAAC3wrMYYKPdXV5TVfvWclz5vPKUyFspE_tY2fnYU-HkjSwtCoYWOO283Iyx81x2G6tdsO7JIqf-I7u8ninHj8g9Xsi8_YEqGYFydMMh6n4uBPexfi5UgmKrdz8hXtlNlnpMuIqtczmKSlVZvREFjvuYq3q7ynv6wMiusn936YBJvDdPaB4znbvpIsfap1sZndj5f4nfpIJbiYWUeS-3k2k1wphhMJ0WDkqRbw_KbegucZurGTRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی وایرال شده از یک مدرسه پسرونه که معلم داره درس میده و دانش آموزا ته کلاس دور هم جمع شدن و کله‌پاچه می‌خورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/151974" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBsTX4KwUkSjTtf2SqWso2rg7MjONbWEpeHl1lAziO0ZWgPa0b3fqTbSGEvJ5z9ki2UWmnBg9V9Vfp8cZSMrFP9iUydncllTxw_b6kVDsaBbprsbOk_cIr7f5H1San2rQgQB29kHG8_UxwcKa0tPOszgV5OkuEyY5NEEPkRQzGY3xXiL5dLcNvTSh4XghMsRlnqt2oats9e-q3LNcvNTOhxuKGlVi3_pc4y58fUpe4Dn89kuOnmFabczEUrsW-_M5r4J1kJy45xn1E9d-5ccMy7eCWm2eDkFCjWnF97nat5Iy1gNtbZA0OCpACy-zYQQEncO1xnUViVDfXy-rVefcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدمت چوگان ایران در برابر گلف آمریکا
🔴
واکنش سفارت ایران در ایروان به اظهارات روبیو
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/151973" target="_blank">📅 19:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8e7gFTqQiiPUiwLtBTjmo80msijiFXGbm3UeW5WmVHWjXrY2Unnz2-RtJtFRnasQGDoyG_-o11_9T4ZXtygxTEu0gUalbX3SZu7xUBrBPFIT0rp29XZ0mQq13LUlNnYJ2LSApTPfdCjQcPXEdtBsezFum9TH_dzligkloUOwNZQx-Uxs9zFxXhm5Ziz7pFCj0CVfipXjXOH-DZAxBBDp7HMiFiFD-HFSVcG32Be4UFdBx9eIoRNOffzyFEeRMF0LqbBuQDLKMaqeS-iXt2buL5lcRkURJkzei-4l-dxJxgTzkRUOM1w1x-4H0OBVC0flTxQKnXJiKMla7hPBF-5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان، کانادا و اسپانیا به شهروندان خود توصیه کردند از سفر از طریق فرودگاه ریاض خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/151972" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
اتاق جنگ اسرائیل گفته به نیروگاه حیفا حمله کنید ترور می‌کنیم.  ایران مدعی شده موشک های خوشه ای مونو هم هنوز استفاده نکردیم.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/151971" target="_blank">📅 18:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تصاویری از ترمینال شماره ۳ فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله موشکی توسط گروه انصارالله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/151970" target="_blank">📅 18:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b28f6687ce.mp4?token=H3tw9e_AJx7-mHc-b_d7zY4THDiJUfSqG1UZ9KJ-c3qcQRRXm2EazjZyMr1WJAMnEBQArg6NsS-cjvdZgy5txKDXX8so41zFhGD35HclKzz9ez19JsU3zAuRmSlxSTkrr9XGuab2A3tj3WuAIYJOwlrUfNK1Y_bgrm4DdSEHpKeXAkXbbmx2Uce_XrbdkTYN-3jg_Xg7fYAHWF1Sjch0eARQura7V6unPzvzY_ef5KEKfNNqeVGmU6cp6myh51mgDJuG0rRQz4OzMnCjTn6ZbN0FpuKnF1o8CXQ2mWjD5uBbtCVUtMmxvFOhqx4cA1ITxZG2Dkq9J80amdMal8xBqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b28f6687ce.mp4?token=H3tw9e_AJx7-mHc-b_d7zY4THDiJUfSqG1UZ9KJ-c3qcQRRXm2EazjZyMr1WJAMnEBQArg6NsS-cjvdZgy5txKDXX8so41zFhGD35HclKzz9ez19JsU3zAuRmSlxSTkrr9XGuab2A3tj3WuAIYJOwlrUfNK1Y_bgrm4DdSEHpKeXAkXbbmx2Uce_XrbdkTYN-3jg_Xg7fYAHWF1Sjch0eARQura7V6unPzvzY_ef5KEKfNNqeVGmU6cp6myh51mgDJuG0rRQz4OzMnCjTn6ZbN0FpuKnF1o8CXQ2mWjD5uBbtCVUtMmxvFOhqx4cA1ITxZG2Dkq9J80amdMal8xBqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ترمینال شماره ۳ فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله موشکی توسط گروه انصارالله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/151969" target="_blank">📅 18:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
خبرگزاری تاس به نقل از منابع روسی:
ویتکوف و کوشنر طی دو هفته آینده برای دریافت پیشنهاد پوتین درباره ایران و اوکراین به مسکو سفر می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/151968" target="_blank">📅 18:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek0YtkxEe5muZKg22fPSFD8P9yH5Y7lX3G2GHvCR9ZCUyaOFOjffisi_1y-xXLQJd8UWODrwRLcG0Ge3WyVgpIzLvB2c0Y4iLNHBycLSqgmyvENdpZqXyTM3vCyPSKXPSQ4a-dfHKB7CuhwS-E6-h36uqskIy1vQ0Adl-6sWy-DIYjBs_utMJ9OFGm4ZG6Fmy-708P9Fz42yY7ApFtPJVcW58i4-4cd8jGvMwkxnTmD4jlFOKJNAPp9RPBQu6KklqwQ-o-ZDczA4zdz8G-V7TTpx9N9IsNSp-I1j03sLZb_r2uh0LYLqIfRgI515gfj-93J--iZ98AuIlAaAZ25vZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست: پخش زنده اعدام؟/ ترامپ: موافقم
🔴
کارشناسان مجازات اعدام که با رویترز گفت‌وگو کرده‌اند، پخش زنده اعدام حسن را نخستین نمونه شناخته‌شده از پخش عمومی یک اعدام قانونی توصیف کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/151967" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=augQKQNgXqf848Ge-V1CNmSjskeeIqDB7QtN-XMKNhQOI_qY_FAnzDzyagdL7hq3KSRtAjVRJuI7T4aEG1--S8F0z3Xh5SM5wcimLa3N2dIvsWYrhYxdJNWaKcMM646WGQDGAqitLuHca6E_70L6_0vGa9kYudaXi015BgjOBaUXVQGHDu-R7LSkN6r4xujMbSkf0eTghMzN5eOu1wre1Xm7zEWy9JBEJsr0uePY7UOua4ORGvHajYHAWUbuaaSytOtFtHIkWQZk-KLOkq3Bmj9anQidhSyJNYuZ944pbbZ0AkLSwcPhGpT_uMEpmxQftJC08hxA57ZvMPEimQJrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=augQKQNgXqf848Ge-V1CNmSjskeeIqDB7QtN-XMKNhQOI_qY_FAnzDzyagdL7hq3KSRtAjVRJuI7T4aEG1--S8F0z3Xh5SM5wcimLa3N2dIvsWYrhYxdJNWaKcMM646WGQDGAqitLuHca6E_70L6_0vGa9kYudaXi015BgjOBaUXVQGHDu-R7LSkN6r4xujMbSkf0eTghMzN5eOu1wre1Xm7zEWy9JBEJsr0uePY7UOua4ORGvHajYHAWUbuaaSytOtFtHIkWQZk-KLOkq3Bmj9anQidhSyJNYuZ944pbbZ0AkLSwcPhGpT_uMEpmxQftJC08hxA57ZvMPEimQJrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض، پس از حمله حوثی‌ها (انصارالله).
در این تصاویر، خون روی زمین دیده می‌شود و نیروهای امدادی در محل حضور دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/151965" target="_blank">📅 18:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQnYUMnh1ysXu3CXtaZQPTph4QA9_QSppw5sUAM6uBn3xAQbPBw4jy3eH57d6YlUDumBXUKpJgpkE-zn5lRxMAnsH-ngQbipJubPDzkTpRtDOyKE0q6CTkIZNVxtaNwsaar5syZOUXxfol6GSbXtXO00DzgL_HrBgEO0woNr6r2rc-n1EouOQnbrVfX6OlZodYMGIlPPSfdU2W0YKjC-pt9cvMmPrkhaRA-2tukekk_hMwqUWZfXXaC7I4x2A8plzt7Gj8GadlF5RhIdZtAC8MDOe8qLDiPcrR-TZtYCiqIFw4bUvpzrRDHNlZQbjeUjz722ketc_hd5PEfgicuMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یادی کنیم از این پیشگویی تاریخی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/151964" target="_blank">📅 18:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بانک مرکزی: بانک‌ها دیگر اجازۀ فروش طلا ندارند
🔴
بانک مرکزی با صدور بخشنامه‌ای ورود شبکه بانکی به خرید و فروش آنلاین طلا و نقره را ممنوع کرد.
🔴
مسئول گروه فین‌تک بانک مرکزی گفته این تصمیم باتوجه به بروز ریسک‌های عملیاتی جدی در یکی از پلتفرم‌های فروش آنلاین طلا و احتمال سرایت آثار آن به شبکه بانکی اتخاذ شده است.
🔴
بانک مرکزی این تصمیم را از ۱۳ مهر گرفته و کاربران بلوبانک سامان نیز از هفته گذشته اعلام کرده بودند که امکان خرید طلا در این اپلیکیشن غیرفعال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/151963" target="_blank">📅 18:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciJ6_xbwjP1IEQL_xa1m2ryKVp_cGoGMriHgNEHoDz-UfV9EYjfSnfmFzkLZ6Uc8cdBddwcb37sxlg6dez_G1t31NaQCiB6n1TXy-kcsJL4-v0sq5cdw974AUQ4UzRSuYkIKxSTsBmh-MDN6rUZHNGsU1rz6G9Ul6oSEeoTArnH6daDWcuVqdlsY8Shf6EE1-okg9UKPTwmAPpt3ggMKwrSX451M2kwHvcXToUWtLstKl5HLb9tN0ZNRGD7bTyEmovgTNJcyqdQmyERxlMqtHPoLqUHG92tNbgWopIlCMBAreC0C2Q0W6mkDVmtUNJdPoLwcEoIWmFPLEAIvdzULeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظاهراً یک هواپیمای مسافربری در فرودگاه ریاض مستقیماً هدف قرار گرفت
از تعداد تلفات اطلاعات دقیقی در دسترس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/151962" target="_blank">📅 18:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCBC_ATpWav1h6vv9iejbmZefJJtGh2fl_4_KXs9GabqwFtjnxA3Kjz3XPIKnyXH22epJjfneNhK66LJq-k5n_J7wv7Rd-tXt39xMXOMAIBPtvtGU5yfGYY4mjdi94uHcI0-7exepAORhgQ95axNem7AAhYw5_9Mv8Jg3_3gL07qRULCKrn0-pUlGji4TGlf4jgfZqSRD_qRSP7kNcdNdXJCJZXtoI-HzzAQjdRLSWHi_4-DYvTu3wLWAimLnr7DUcDu4hbrx3CrFZNY-2S4VulbfuG1JxlyLvACxnEWWn_GET9Oi2YIPiv8cAPUDTLlWm-Yv-lkO6yfCICFahri4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
تصویری از تخلیه کامل فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/151961" target="_blank">📅 17:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
خبرگزاری فرانسه:  تخلیه مسافران از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، در حال انجام است
🔴
گویا حوثی‌ها حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/151960" target="_blank">📅 17:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUTsrIT_AGa-ZVHxXEMQbQPwc2vOB4dMNS3R-Z-PcPbPrC6VG1SpGLrb39vCDkCXMYwfj8eme6K63xYwsZtXiARw35OKgibXv8HTgLo8PrzAZueqXhjidz6LQdzIAlPjaql04gnf4EpyOPdDY1LQGn-N9S6NziMvjZsevzJ1jzlZBD9MNy7CI2l0eDbSmZh_P8ibtM_xUSZpOvV9Z_L51uvRzBpCSRcGyoJe7haCmTQ_LPbT3qV8RYZGladCbLASqDwnGtHb1UWRtO4kJ5YX_16n3xsR0RUOkhv4SblVe8Kq2KrheonVtV8cjRAjBZgIy2TFoO95kz4X5Ogs5NFb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز لیست ترور مقامات ایران را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/151959" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری فرانسه:
تخلیه مسافران از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، در حال انجام است
🔴
گویا حوثی‌ها حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/151958" target="_blank">📅 17:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آمریکا اوکراین را به قطع دسترسی اطلاعاتی تهدید کرد
🔴
فرستادگان ترامپ به مقام‌های اوکراینی هشدار دادند که ادامه حملات کی‌یف به پالایشگاه‌های نفت روسیه ممکن است به قطع همکاری اطلاعاتی واشنگتن با اوکراین منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/151957" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1f9cc921.mp4?token=CqPKDnvrbKITRohi5mNeSIPKCdHdFpzzcdzxxhrSeiRyB3Pcx7Jwq29hCGXVcbABxfuQuCyKePedvJ5JuaGQgWChYKXRHP5wgjXH6FxXY7YeSDuSoQEBRVxD1RSfakMGUbZ-4MDJNz8MLusoE9KAlRr3AMeq81vamnnj1qX-NXxyEJjkwT2d42RlE9dMX2SzBVZcoy4DLWzXZGBLYcXXgwSOOpDPEZuEJrn_g7Q5vO-1pf_awoUK2Ju-jkwIbRbSEHLrE7qrs-HV3zk5gWCrRdEZTmq3NzcdMc7ImYpyxmYmjGAWRzoqts3TLdS5C6Qsl21OnyEnYFghqEA6UOOmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1f9cc921.mp4?token=CqPKDnvrbKITRohi5mNeSIPKCdHdFpzzcdzxxhrSeiRyB3Pcx7Jwq29hCGXVcbABxfuQuCyKePedvJ5JuaGQgWChYKXRHP5wgjXH6FxXY7YeSDuSoQEBRVxD1RSfakMGUbZ-4MDJNz8MLusoE9KAlRr3AMeq81vamnnj1qX-NXxyEJjkwT2d42RlE9dMX2SzBVZcoy4DLWzXZGBLYcXXgwSOOpDPEZuEJrn_g7Q5vO-1pf_awoUK2Ju-jkwIbRbSEHLrE7qrs-HV3zk5gWCrRdEZTmq3NzcdMc7ImYpyxmYmjGAWRzoqts3TLdS5C6Qsl21OnyEnYFghqEA6UOOmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که به گزارش‌ها توسط ماهیگیران محلی در نزدیکی میناب در جنوب ایران فیلمبرداری شده است، هلیکوپترهای آمریکایی را در حال پرواز در نزدیکی یک کشتی در حال آتش نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/151956" target="_blank">📅 17:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkR6AGy6ihxPc6xY95gRwaEAXlkTuNKZwihfZC5vhRSABuyl0hukzHf0S0ESqeag6k3Wf8vAiMoqa9X9N2SEeICUwVkQA63TmaJZmYKTw2bvqW9956UjzMisDK_mNcJW_PLe-4wUxNxeywk80DftfijtgeLusfAiovDWkq0wr-QxvTMGnbeymj3PwwJnOTxQD8ojCycz7JuyVZ9oiugjyKsnhfnoUTsqF2wKR8_ksCXIr9L9fHFdZVqe1Na-SPH6bJx1buScYeSoNK2eAsCpnHDsv1VPVgqhBZFemUR2DN1zlMZXOtF3TZ-pBjyJkr4ozDrspzpb3YdnDBtTEFfJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا امیرحسین قیاسی بخاطر پوشش همسرش قراره ممنوع الکار بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/151955" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
برخی منابع خبری از شنیده شدن صدای انفجار در شهر ریاض پایتخت عربستان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/151954" target="_blank">📅 16:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/151953" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
خبرنگار المانیتور: در گفت‌وگوهای دو هفته گذشته میان اسرائیل و ایالات متحده، آمریکایی‌ها، اسرائیل را برای انجام حمله‌ای علیه ایران تحت فشار قرار دادند، نه یک حمله مشترک بلکه خواستار حمله اسرائیل به تنهایی بودند
🔴
واشنگتن می‌خواست نتانیاهو، نه ترامپ، مسئولیت سیاسی آغاز حمله پیش از انتخابات میان‌دوره‌ای آمریکا را بر عهده بگیرد زیرا برای ترامپ هزینه سیاسی داشت
🔴
فعلاً این ابتکار به حالت تعلیق درآمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/151952" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327194aa76.mp4?token=sW2hx2p7m15BBPtMt9mzq3p2Z9C8jqlRRaTfETLDt7JORxJ4qjUiay4KPR_tBelTk_aQcednc6NCbx2AJzgiUSMRIpMgAI0Qcc6-dTvQcRUsZ4DPVEaYQrPJ8fDdFeab1L-KnNSlxvJnjka8lBffSglQ5fW9lLPIywahl7kPSKU_AbgWTZoy1DdlMTHhL6KwHsDVvniQf4jAqC-NfeQR-7kOvhf17dNsqyW7GYWfzetFAmeOcIOBTb1OejrZWsN9e3fOB-WwdvnYKwdPLBwdo8itRpl4T8HGewTI5Fo8YqoiHUQ3EtPHX5dNhfv1aGejy0xq592W1Dc3pzuz3Dvp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327194aa76.mp4?token=sW2hx2p7m15BBPtMt9mzq3p2Z9C8jqlRRaTfETLDt7JORxJ4qjUiay4KPR_tBelTk_aQcednc6NCbx2AJzgiUSMRIpMgAI0Qcc6-dTvQcRUsZ4DPVEaYQrPJ8fDdFeab1L-KnNSlxvJnjka8lBffSglQ5fW9lLPIywahl7kPSKU_AbgWTZoy1DdlMTHhL6KwHsDVvniQf4jAqC-NfeQR-7kOvhf17dNsqyW7GYWfzetFAmeOcIOBTb1OejrZWsN9e3fOB-WwdvnYKwdPLBwdo8itRpl4T8HGewTI5Fo8YqoiHUQ3EtPHX5dNhfv1aGejy0xq592W1Dc3pzuz3Dvp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدال استاد دانشگاه تهران و مجری عرزشی برنامه تاریخی سر خدمات رضا شاه/ نیروی دریایی ایران در دوره پهلوی برای اولین بار به شکل مدرن در خلیج فارس حضور پیدا کرد!
🔴
هنوز از جنگنده‌های آن زمان استفاده می‌شود و حتی از F-5های ما در این جنگ اخیر هم استفاده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/151951" target="_blank">📅 16:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwN9EQtEKj6ZOHSVgfI1aF_-j8tonitRcb1_kjsWUWElSPkV11Y2lianQCCeB3m8wAu_f4Gl19zTlgAVoBZI77Zb2HvyUBxQPQQH2hc8QLjF4pTFtCmNzYwHS5hmNQ2CGt033CxdfhImQNj4JGFUoeSEM8o9b9guJgxSNBvBzgaXiBlwMcVEIxRiB_auvHVtBVnQnJA-boPLwq1LkPvIICUrEFb9IANpRTJoX7luOva_epS_7nOKXH7ORhFNROyzrnhZ18sAHsdF5qMWH0kb4oPbwdS1srnVOxdz4c6vpGV8Ag0YBUKd_o640iK9P738w_B_oOV-TuygaG6nLENQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ اکتبر روز جهانی سلامتِ روانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/151950" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عراقچی: سناتورهای آمریکایی خواهان خروج از مهلکه‌ شکست‌های فاجعه بار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/151949" target="_blank">📅 16:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوووووری / معاریو: ترامپ از اسرائیل خواست پیش از انتخابات میان‌دوره‌ای بدون مشارکت آمریکا به ایران حمله کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/151948" target="_blank">📅 16:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWD-MO4l1k_qOgkeejhCaDI-t5ctSoqf3_Yfz4Y4or4mMrgC3T0anNuZYtiImJnqhApmOA9yFtoH0-KCDFKZoeJRnuPvXYPe8W2lqqCVICw0Dw0jlvZ9SPLGTKm8kMquwWVs0RFYaCkPsXxZDTViuYcsWgWKP2GLpz2MTSFLvEDeAudRMQWMkJDUMhszzZ3XE8asCqGH3pOqnK26Rcm_mDYugya4_NHAayyh9zBgOhe-CBuaE9hkxX6OBQ7P3I7zAltBlJ6ZfO7N5xcw2aZ4275NzpPjtybcAGR3q0ArzkziT-FC50Fv1rph_LXpT_3sIHC6RthOWT5o303ChxLvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ویرال شده از یکی از فروشگاه‌های قم که به جای کلمه «کاندوم» از کلمه «تنظیم خانواده» استفاده کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/151947" target="_blank">📅 16:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جان سینا از دومین ایرانی هم لب گرفت؛  تو فیلم جدید Matchbox (2026)  | مچ‌باکس با بازی جان سینا، یهو گلشیفته وارد میشه و اينجوری لب‌های سینا جان رو می‌خوره  این فیلم اکشن و ماجراجوییه، داستان هم درباره «شان واکر»، مأمور مخفی سازمان سیا با بازی جان سیناست که…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/151946" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65fe6ddfb6.mp4?token=sn8fvZ_RT8BykfZ1aXyUX93Tyhu7Kmj2atauTNLJxWzvKUouh-YlymguZgzp8vjzkbt_6gom--r4VQrqEjIlzaIL6QIl30sp3i7M-VMtORmZhonHe-0NGFOAfNW8-tus6F3Q6mNV7jfu3MApT9dj--SexTxuaaUGF5JOhn96dFgiTLNaRgo286BB0QkWEXRVbywEptX0IQZt4Zg2agFoG9YjYqfKOK5lB5WiXkx61AqcLOs6anfRD0K1o3FhAsVaKzEQ5rgDXAi6M3Dt9gaURuv_rvBv1FKvEBfgcdvtDrGt5M-THSld181pu53bFBIdpGGMEf8JSbTY_8oj1R0n3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد علی اکبر رائفی پور تو این ویدیو یه جورایی از
خاک فروشی
حمایت میکنه و میگه چون ایران خیلی بزرگه آسیب پذیره
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/151945" target="_blank">📅 16:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151943">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رئیس جمهور موقت ونزوئلا، دلسی رودریگز، مجوز فعالیت شرکت اینترنتی ماهواره‌ای استارلینک، که توسط شرکت اسپیس‌ایکس متعلق به ایلان ماسک اداره می‌شود، را در این کشور صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151943" target="_blank">📅 16:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6EFMr6z_RLAFewe88csJd_sVOialw2mVEHNM7MSCi4FmHWQJwYIwJ8YdgW_myjgX62a7PyKT3LA5oyqnogtwLaEtDO_Ig_bQwXonzHcYkW3u11cV5mmqpM09dHkCm9GLNHrMbY_H1nwNhmULldfINksGvQ6eFUgqSvBICcE3vajL50sz5CBWjk8qu2NdUSA6-L2dYr9aHuh-9IYvJGtj_1nnE6b7-YGpCqjfzjmVm1gJzHe0W1Lt6A5xfP4mdYtBmkXxqEhayuCa18BwBZK6rwTGa3dXzxk4eHRcvkb1AozEPmjERiVEYlpwvfMl5GYxxYkEHEfLt1II6W7zpPQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حشمت الله فلاحت پیشه: آقای پزشکیان! رایزنی با قاتل احیای برجام۱۴۰۱ و تفاهم اسلام آباد ۱۴۰۵، رفتن پی نخود سیاه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/151942" target="_blank">📅 15:53 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
