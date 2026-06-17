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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 643K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-94007">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFPWA7fMiD02vGEVE3Gc_oUU30ZqIH7aIM5VX7hY4SGM_WrfElyNUOG5zBkhrrgQoA2UTFtcJe97BG8pC5SVh8pmozKDLr9U4XT4XfWVOkFipUEpF6KdfptnLt1IAW_M7u4hZVJPYx0Eruc_xjw9wTlhRox2vggdAliiBZsoMKhWPQpinvBVCojHUJWyCnq-iLMmbrCIyKKCt2462anw_W5QOKX7nm6WMbqMnRcZDI-tVfLd6b_bUB3gowyDpcjhMxxD1MynIrNKeWAgtIO4CLT6ZJsXF-B5s43lfPPdyxNzCSSbiK6fyZG7GRNMzLju0_tpE_Y1pWCvNGkyun31hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی داداش یامال واقعا کیوت‌ترین آدمیه که میشه دید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/Futball180TV/94007" target="_blank">📅 23:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjEW1C7wF_GtUx2j02cp1bbLVVOobMAjL53OaMWkakW3LLeUqec3XUvatwI8YFasxh63RmlSZX67AxfrPlFPH3YV4jM-Axi8QQRYdl0z-QDSw6v7XGHsJPUTlzVUvrRVFKZrxmRb3_FOVA5SkhjkIfY4Kd5h8_laDcy7sNM9xgeMO68o18DgMAzv7DwY2T0Sy_V7IGQA8VoFWBD8MlEtaDNpXpZw0QyhZ5Maqy1zFvPW2fAryriNWam6X2zebWxKhbAxzM3vqcVF6Dgc8_FZMpNrKGGye1gzQwjJaGY9KPoY1rVrvzC8gI-kGJIer4p8HsqDH8XrauuEx_qVp5s9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با توقف پرتغال مقابل کنگو،‌ رتبه ششم رنکینگ فیفا به مراکش رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/94006" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNLSpGffeys0ycpul_MX0WzWEU5MHIa_3rPBdsQCB_lBJfTym0Pe_VDrIiJoRoamd7HMvZasTOsZcFY8k48XL4eVgYR77nTpn6OjXkDSdPa7ECU4iOkb2A4d72Q-NJTNZRYSPv2D76TrfVVBN5RvRJCTo9GObanaI-3-0AgnQPy1nX5DfKR8Ynhlib5OadF98vQRBIj0Y22qy7L2q8S_j9T65nR7uEvONUiTfzzrMSCmUXpGESwdu0kkvAUT3mUWg_-1dfV0yZ5FYQaY9A4ma_JEL2Wjt1jhW2NYd86RtEByFjrySMXxQ4eHNUoi_vn1zibBddYoieP9vzazuXyU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تنها ۴ تیم در تاریخ جام جهانی بودند که در بازی افتتاحیه متوقف شدند و سپس قهرمان شدند:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان ۱۹۶۶ (تساوی)
🇮🇹
ایتالیا ۱۹۸۲ (تساوی)
🇪🇸
اسپانیا ۲۰۱۰ (شکست)
🇦🇷
آرژانتین ۲۰۲۲ (شکست)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/94005" target="_blank">📅 22:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
#
فووووری
و رسمی متن تفاهمنامه ایران و آمریکا منتشر شد:
— توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
— هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
— توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
— ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
— ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
— ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
— ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
— تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
— ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
— تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
— صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
— دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
— یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/94004" target="_blank">📅 22:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94003">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnFCqBP_ZKif1zBQpb8GhpoHJUd8h3qKLbMaYNxEeRRpKgQqdPB_g6sU10cu6jYcczJsOP3dFAT5yhYwVaPMY3x93GKtH4uWi6ZX9Qz_aT1Ei6r8JLSb7jJcArcQDYZbg_FJdhhLd3vZm364pBo9yeEFRyssaosKOkswAd_m1nqsGr9_WUHZK3W7FlcnfINgIfKl3SCf9xGFEZd9ipR17SKLpGB2CuRMNEfJ-skulmd6N9LCDkzLW-pbgsaqp417R7c0KHbWiI3erj7tcb2_ZtsOfQdr05X3LjXnMASE7cIWfE8hZst_raDXAX3kmleifFo9NgRacpCq8sJCH89bqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
📊
عملکرد فاجعه‌ رونالدو در ده بازی اخیر مسابقات مهم و حساس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94003" target="_blank">📅 22:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94002">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEc2DH3ko34aWTfaM2BDwvjYJ5wqE0mB2nr_ct0zDQMuYNXl7xrL54aiJdtjgeitH2YAVWHHjL4ZS6QBTarrzahttcc2GUvP3qY5O5UhkNJV4qLWbPTNKI62H_sVBWCAz0gavYTPGBTJzsKTVnpJYZ42Bf-saB2sSGuKm7HFfmz-CCUn6eYa7Z9jxdJULD5EpbuHX-BtZJeTEao0kRfJ5_i12LJmLd25m4S0Fx3D1mQ4qjF4v-8c2oac2kih-HdjqffrDX7DfUbWcX7YPU2_q8QGrJUwfNWcNQ6kNdizah-YOBHzLD0OTTIeTnc5BrP3US4WwbQWThd6pT5L3B_Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد کریستیانو رونالدو مقابل کنگو:
⚽️
0 گل
🎯
0 پاس گل
🥅
0 شوت در چارچوب
🕺
0 دریبل موفق
🔑
0 پاس کلیدی
👟
25 لمس توپ
✅
19 پاس صحیح از 21 پاس (90٪)
⚔️
0 نبرد زمینی
💪
2 نبرد هوایی موفق از 3 تلاش
❌
3 بار از دست دادن مالکیت توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94002" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94001">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQcAp2DlRdD0hkUDmYBUdrs1MaiQSCIGsRaa7F_ziFGWE-sKXSyTq8hqn0BMoaCJ3Fcjn1tNn6HjFNXbFBu7PAER_2qLLwD3eZ56haNDuqQiNkMX7RmDSlQXgIiWWfzAU1p5GbKGt1auGkgW26M3s54KO8v8DsPLsFwllzxYBVhydDQWl5p8zrAblHf56XNueRRqh5EDjYOwLJDPZvdgpPQMF5YkoNzybXWCkj83XxhaUWbCS-qJq7x3h37aKxAkT9Elh_hUln0anU50Tfo9aJ1Tj5UzB5VOFBIo0yJrgwMhCmmivYTQ7i6NvtZwjY1k9DncwQiuj9h9Upy2FbJ5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
❌
پرتغال برای اولین بار از جام جهانی ۲۰۱۸، نتونست بازی افتتاحیه خودش در جام جهانی رو با برد پشت سر بذاره. آخرین بار این اتفاق در تساوی ۳-۳ مقابل اسپانیا در جام جهانی ۲۰۱۸ رخ داده بود.
🤝
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94001" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94000">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckqZ6-QM81LPJQ2Efrz9XsELK3k5JVcaiGz9ru1avMtTs5rz4e5xIpF2x9vL9p19o9Xl9UR3hgKnP9S0ZvuIKaHvWBvCO8ODUaor5M09Msn6Jlw_M6fwK-W7aGC7p_H8PpepoLCjIsNU4OVqXEdXpKiCQKoBKIBsIEUbUKq5KZQjg9PTxR6jjylMQIRVU5grqujxAdbrhfZyH4bfujTKEwrnuzpQBvHFAU5EGokVc53qfDjL02GkP28DwqAwfnVSPaYXU4qFqsBhYozmd29lS5Ji472_WcnSG6G4kdck9Fr-HDfwMdrE1u4ACFZy1j-2_GiP-DNmw3EUXkf_R1X_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🚨
نمرات بازیکنان پرتغال مقابل کنگو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94000" target="_blank">📅 22:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93999">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAuZMpEQJEYQJeCs690u0hbuFKfK4Bja64H2E6ngtGbsylx7XdnVC83phBXboofWzw_GoRG4eHnuTjTu9tWNnVtCEQAfrUZKyFpKwfnSkkay6KkmUwUTRXeqS_lonz1LWXOWWmsQCB7VQ6adipQPSzzJ06raTuC87Z8YFk-qv5iIPmLK9Vl2lLsdZrhGCm2_6CnxoPCM_0W7Khhb0ggL15GB0xY8DjCx_td7wR22rVpWmnHMMuVckl0ja_kv9kPD6V_lwiHSHZM2X9bV75hZ1_GnLcMagoOM9Pv7ia71cJp8B-ENZYEePgR2IxMXkZWEy5HVR3KjHpEWTTlhzwbZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇩
آمار نهایی بازی پرتغال و کنگو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/93999" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93998">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6aoZIsfwqWj0-hecjeQR-EfmevnvmH8bJSht08sjLvjgXQ_rGPS73wh-clGPCdzOt4-sK6zH8hgr14UO1-TAbNvUWnV7R4xyHCSAQIrz-xAYMhl9StOW4pT3bEETctwt64FKnRsvbLDS_-K4Z3Yb3Lw02K8vqFv-xFxBv9VpA1zTLmDJqvMJzPM3DArEMR7fIiga3NHg5p96GU3zC9TFypybysK6UGpmpTOFSofBsG05QbkrjYZlACpLWCwRSmuxaMiniB5ZUl1qfDdJeNkFWv42thX-Mq-KccL2imIjG9K02eNDDAymdnu8Zn8-gYjrGkqXSx2e3UYVrNbAfzcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تقسیم امتیازات در جدال پرتغال و کنگو؛ رونالدو و یارانش متوقف شدند.
🇵🇹
پرتغال
😃
-
😃
کنگو
🇨🇩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/93998" target="_blank">📅 22:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93997">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/93997" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93996">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پرتغال ضعیف ترین مدعی بوده تا اینجا</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/93996" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE1uxbVlju48FxHM1PEwngoXxOZ6b4f5jFO_veEkxeXWb_rAM9MiykS7j592mcDP5StEcZNL-yZJahJBhuRB3sHVg0UVekscv9E5bte-sPAJvOc7MiiSfLwcuaOz5PeSVW4fEvipoLxBLyoYjV9AN-5l6VA6bEdIe7RXPhjPWKw9InjBJWemhteREHp1CZuYRng3_9a7XnXVEa1xm-IJIE5PUE52GJ_nU83_r1dmUht0sKXDPUGiJhK3m5G7P_VdVlODhjioBqd_nTzRGas91kmiWKN77taQER0XeN8M2oQmkBZN3ArLrFoCUlICy4W00nmlhqGY9XQKiUFvuHbRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquqVOcs6hGSFup6-hjRTULNNPEAXZgbdIDBKFG2yckfJls8MIzn33jO7eE1NuZlrOL1ieCQRAgNGAIWd4dlNF1kCtv2L9JOzwdl9NkZ2H6hfUbDUG5_cHnuOnOUFjTdGhykWzbr1BtzCL7N10lJ3gd09_A9tbR6DcJ0KEZGRxFywuzp6YmwlbKgYGEgWZBe1jDp-KWV2huR8YBlnHWZQ7kwF5_bqjww4H6L91kIz9uxhRFf_OIB5ErC6Ql5QUWADP1WK0X5EwORrQIRRrwG1l15YCK21dqA3uV9yXw2UJ1JBitSuN25VEHSP_N1-OWnfgW7vAlvokmI5ugFomdIdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب رسمی کرواسی
⚽️
انگلیس
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/93994" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcFOpP40v41qgNXAgjpPxx83E7jHosuG4kxMrjEqAgKQ4jHa-PlHVcriE3mJt7xU5KJveaUpTcITJHE0kTtQTdYFjc5FuH1VlWBCrCGmrNQO8Yr4UhpwG3vAG0U4Z7tgXv_6-rFY2Jh8fX1rBj4Wxz1JWrRqwCbAhqCLtaB9kN2Ft87cYDL-UMUVxqQG3-hOurql-7DUQqdfooEALwh73K7nuaGK3iG4N6yDYCN-CNcHz6yZEprB8MwytU2_VkUMQ2LZXRl8j9tvC_Mm9_v2Qm0-hf0lXkM-xipqB5S8HMahiCUOgl-tMl4-NK6x449x_MyJwk-wBHVXr2G3tVF9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو این توپ رو گل نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93993" target="_blank">📅 22:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وااااااای کریس داشت میزدددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93992" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلللل دوم پرتغال اما افساید</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93991" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سیلوا با کونسیسائو تعویض شد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93990" target="_blank">📅 21:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93989" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkslZm-Sz5LEBVLmPp9AUAfkbRBIipUQersWOYYIMnqjQKPgs8_3iaTssoFj-aefBr3qfK3H0e03YmHAPXycQiMa8ipJq2lEbXXfYxsZR_OYc3QHSVKfvrvdZaQ9cG_I3Y7YDMMeKdMTjzC-1Q6ccVBzlZfzlyN_SXBT_OQwh2-OK8N9jjMkLq93Urt_LCFycyTCNGms83FV5YpJtisr880pafFrqPXeR9Huaf86ICmlEVDBNoJNDHREzkcLR7wxLJd0vB6_QmvCuPGO2g74jaBQbxWf4nCLkMgjQvmXfuyjBXS9x8QkCQBqufQQ-L8eFduKSfGSQNMV2ZZToKKszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وضعیت آمار بازی تو نیمه اول:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93988" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPHyljT0eDh4JftAicDB_hog-XI1n4ngdIBqkYpgb2YneOwGQ9DWOmsWHmeSZGNTIk39DIhsl5IQ0MFMFrp0XNALtHNYU99oJkQVXSrYNFAnR_OMmxr_BIVKwoD984MhAqk1lErKlxxKFUz9Ll-3d05K5D0pBqTVed7zDLaR9nO-kjX_w9s25Aum66Nmdi1Od8vYCeD7IFMrNJPFh0NywTdNw0Y7C8EYTxKyTmB3Syr8mcFhISiOSi1IR7HgFZnOKP5Pnv_0p7CQNkrDt71ACi_hBJioeavaIVBeniyXmu13CdT_qYCrr-lpt_l1TiT13Z66bkRmtxlo9MolhrvcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی به قیافه من میخوره پرتغال رو قهرمان جام‌جهانی کنم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93987" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1K5VL2rALuBJlTvP5i1aA1la6ATNSQmcJ-6tnGYG9e9-m9z-w92P8aoKUGztLrE-jl_2fo95qTyCnSyOISZO8dkLdVSfPg6yIOPyrc5yyDnr4o7rIQlxqb7-VErIbX4Zlf-iM3BHJbvTEB0a9_5OLgNpXdt6MCZd7HhaiSVI-sq7ERI2wlXr8myB-wVfl4EtS8Gk0B1K-8wNFDf_AEneQaUoTitZARmtzNMrInSQ_3LCC4vhrSr_Zg5rtwzq6f9RilqUVoTjoCXJTyv1eakjpD0EyfFIc-Kbg_JITp2fjHFEa8ySwVAYgcfZA0emb5rnpTsAEMGk2WsLxqKMjJywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6K2Cog3nUzPQSAjMC_IiW4KKIiIWZWlTaitm5l53JE7E4kKl-7o3dGvgzEfPCs6mpcWPwt-kue8xbE74dwLYP0mMfisKBZNqeDWHCgPrkdhMKLIOO0ULrNyxWBIQsxmpGWtiQlNd2ImDSwV6whSf7DCUBWlUfZvdMy7WHRFoAAtyj7KtG5cfB74llHIS-7HQJmrU7hX598v6Q-Fd6cVDSYMkkSqTXo9SK3o1HiOMOgj9SZdUFBKf-67AcchHKyru7_sSdSVSjGE4pMV6OIHPktLVNeXqsmaQrkcOxKSpZbjGp2ngKMrBmiNrLt8qzwCV2-0vi6qJfMH78ZesAttug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uswXIckOBsoJRsbDXW7gEy6htEpQ0vYFrfPWaQKCjIdXnNkWxPTW3ruCVcvIJBWGEc9qLMlvEuFo3vS_RtwXwmcvQl1dpmpTeMpcLzZrvhHRX2U651P2fHaqYcxiumBk2JPLygOMF8Ecvu0uedYP0MdXjXRC7gz4LBm3PKEgU51kI2g86jgN7J3hGQ36C_73RB_twBs__ILbxP88tQW_svLOGW5FyyNsxzsyvkFuAqF2jHrEWia3g8zdLfg4JGOveMz-LodziMswrlh_aeRlTGUypZZFsxckAzCQ0umdAlFY0FmuTz1KIHdH9S1QmTUuP1Of5UqNSTURpJj9CucLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYndzJH792wy9zZ7snMpqsH2_ypdIu81eufkBOBauNMjJOyuLIGLpzuVN3dqJ8ZcQS9Qs_Y3amUlo3xmjL8ZnlBO8ILKU7SwQLyUa73jCAerspLt_PRAr1FnYxlmZE8r6aYUFHdlT9XBuXJ8AtyM0M7P116ZzS30sudZULpQ2_LG3qWkVfGf3i6sgZ9RgGWovCr27Jx27LTQf4ogTCUBZIx-4sJk0_Lxuk1yjp23yR3-LLnHoEdfC9RPPWUv7w6yOdeoRlHw2cHNapylIXQSG5wixsCBCZgaSmAH0BxbwzWfXR6Wgad6marVT4dM3E6u7GvjQidbsD0prRlGdVDREQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vamos Portugal
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93983" target="_blank">📅 21:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پایان نیمه اول بازی
🇵🇹
پرتغال 1 _ 1
🇨🇩
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93982" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇨🇩
گل مساوی کنگو به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/93981" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارتینز پدرسگ این چه سبکیه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/93980" target="_blank">📅 21:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پشمام کنگو گل مساوی رو زد
😐
😂</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93978" target="_blank">📅 21:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFZ_sNVGx9SoBlUES9DYFLG7lqAaqtb7OrcekCGvmLfE_B6DOKaAmYfHEriz3rSumLK17y0WEf3VWSwnbhoGCpqFXOcLMhLtr24vkH-ujfeVkfxjrCPqs6F3rjdy1RkUpHGvF86OYfnZqJH3rmciRp9yAo7sivQSGAqwSe_9ib5fsYddP0x4eTAjjnZdhJ4NSMQ8mcSe_pHZFMJEHBOxAqNht9HDvjWr0OWMTfDJRVXNlELGf1McfCyMAbRE6QnIpf5ijMJG_IGYlQs0IlzrJtj17pv93DUDL4Wj3SG6ESbYY1ArjmTMKoizAUVwhZemGzr88EQSrzJNxtzGx7_B2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر ژوتا تو استادیوم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93977" target="_blank">📅 21:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3nkmlrgvVadNiFhbRmfYhKwmPpH-_jWEuqZaQMxIkYq5XJoE8Kh6AqIBu03XxXryW62g6co7CgcFfSZpHVeGf4El2ga0DwfT7eBZw2ra9gvfyJb1HdrKoQk7mflPMx2D1QGfsFvTDdnFGunoicKEfKYK20DcybHifhxNuO1wiGYQ9xoJIGzRc07zK6ucmA0AG15u_ydM6azTzjpmS51EuRycd839V2CFOGx1sxlvsAblMDwZLj1FA1HHBHXpEIex83Mp2bxQVd6Xoc3vv1cqpX7PxnWnvn4XkZL7da9ec4qeXAabUMCJk7-88iCjfzW3g8iII9r7DbYSyqbQ24bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فوری از آرشیوو وار:
تکل برناردو سیلوا قرمز مستقیم نداشت چون این حرکت به عنوان بازی خشن در نظر گرفته نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93976" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St5d9ut3yW3Qk6A41U8wEujmJvNZ2qmvRhJzov0WASQ0pVOe73-49nz-NQA8GYlHGALR8wAxm2lWw92qLGEa-LFhnGEU8diGBmqPzMI98fc_JTTFPNkglS5EDSdj2MIpUf1xmi7IJf5blxaj34pcvHj9kecsiAZtQJSLCaE8adL9DXqgNXcV1QGYA-tcuqw8FMwKgPQbH0Srab0a9f17AQHU0nEHwcKxP-5PCqV6tDOCNlea2qKYItJOrVB7LA1NwIUJBrmUcUd_s26cr0ajF7JTvcyyOsAM27tLFGJzZM9kk78TH6z-W0NU5Kc3T5UFUHvmW1jp6fcMQUqoamMKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال عزیز امشب زیر ۴ تا نمیزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93975" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کارت زرد برای برناردو</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93974" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به کنگو توسط نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/93973" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شوووووت خطرناک بازیکن کنگوو</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93972" target="_blank">📅 20:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پرتغال اولیییییو زد نوس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93971" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93969" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC9-8WG32QNLAxEqBNuRW_g3ciVUJjVgIOJ-JhOmdMtGVtXn0hAT-PhGXHgeM5_qECGbC9tmyHrNH8YjfOmZwi5OK-96-SCrkAB40-caYlGxG2zGAsAMugtHSZR7kHxoOK2nhdBY7I-Axt3Ahw99a8gFhl2rRb8mesY9BGTEOk6BizaJ5koBfh-FEC18QrEBwLBt5DT-75CHS9fTkbCwM4inDMd-mPAMFS2noKS1XwUZ-Nd7iLH-L7s3xNF4dakpk7_EhftotvWtzu2CI8tXFEVzvhP9YmXt8tCak5G86eMs-QMbXuQuIVuBwEp32c0H1HSLZdTB4XLTHYSe9GfFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادبود ژوتا در ورزشگاه انجام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93968" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کم کم بریم سراغ بازی کریس و رفقا
🔥</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93967" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8532e0a977.mp4?token=vCG9ALkpdOIMP6Cf35cW2laQSYJdho-k383fKbKncle5jbXYkU2dzomod1G9ccb84ACtsMYbZ03r6Dsewt6a3nIvD5Q0MylXIF8cY3md4-fT4XVCZskgnKDUBtbljCr70EamQn-mjla-UTolwMv0-3bAM5TZtI9inKc4eQEwGlfc7L0ql-9dWyulpGPubIbbkDPuNzMexrMCzn80zSs21FGbMpbmrxnEArwvgerp1w_cNACNBTrw3DyP7H3tQ_g6qL8gaHrpGjWrRAAfdjyjnAf6BpEzKwvIlHB_3gLIVCWag-ArXT5WD9Xia3K3eTSJAQ7S_LbpcSRlVI1q2jNGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8532e0a977.mp4?token=vCG9ALkpdOIMP6Cf35cW2laQSYJdho-k383fKbKncle5jbXYkU2dzomod1G9ccb84ACtsMYbZ03r6Dsewt6a3nIvD5Q0MylXIF8cY3md4-fT4XVCZskgnKDUBtbljCr70EamQn-mjla-UTolwMv0-3bAM5TZtI9inKc4eQEwGlfc7L0ql-9dWyulpGPubIbbkDPuNzMexrMCzn80zSs21FGbMpbmrxnEArwvgerp1w_cNACNBTrw3DyP7H3tQ_g6qL8gaHrpGjWrRAAfdjyjnAf6BpEzKwvIlHB_3gLIVCWag-ArXT5WD9Xia3K3eTSJAQ7S_LbpcSRlVI1q2jNGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇲🇽
🇳🇱
عیش و نوش مکزیکی‌ها با هواداران هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93966" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64954456c2.mp4?token=PAAAhDaUC6fGFzKGEJzr77gcf-sPbKdxmUuNa1tI59YqRDtACrHVPWPQD-UqBBnk64F2S1ph0djsFieYwumGaWvKMuwc1qMadpkyoo7abeb2X4l_eFNsnc75fkX_dbZilKdl2YKofK3Vy5STGNxtoDN6z0Fwf4a-Go_jG62Ob0Ngnw2ngUTsp9YwTSDXVlzbqXSKKyRnEaSI4nMlk0ZF2RJpWj70oyxFaxgW1TVNRODbDqUy5E54YaKdP-0Wy7bbr7c8SlNarVQWlyvQIfwi8n8PmVwUL6m-2fZNrNxLrxdTEpBjgKdNtPgBn78OJOAmG7YnHG0dDEOWZLpakF21NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64954456c2.mp4?token=PAAAhDaUC6fGFzKGEJzr77gcf-sPbKdxmUuNa1tI59YqRDtACrHVPWPQD-UqBBnk64F2S1ph0djsFieYwumGaWvKMuwc1qMadpkyoo7abeb2X4l_eFNsnc75fkX_dbZilKdl2YKofK3Vy5STGNxtoDN6z0Fwf4a-Go_jG62Ob0Ngnw2ngUTsp9YwTSDXVlzbqXSKKyRnEaSI4nMlk0ZF2RJpWj70oyxFaxgW1TVNRODbDqUy5E54YaKdP-0Wy7bbr7c8SlNarVQWlyvQIfwi8n8PmVwUL6m-2fZNrNxLrxdTEpBjgKdNtPgBn78OJOAmG7YnHG0dDEOWZLpakF21NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😂
سوارز مناطق محروم در برنامه ابوطالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93965" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggtDpojK6jgZK2s_oGzQof1pHGcYvjOLp65UuuyJVzN68thbwUqoa6BYcJfZg50mJjhyXTOW0gWiu0WQPx69Gy4HmTmDlQCziYLPkkgxwSlUcRixM-QJYcvcwa7tTNMIdL2m7Y8RelWtOM_48Ejb-5xUVSmX8TJAfYMXVSHDTDSaBiyjbsRmRg55yfRwnGh6lIz_rIiupSHFZX8fDc_C1zA86RDMWRnXI1HMPdsXa8_2aOf0YU8Dom-ZAqJv92EcEGal1nAb-r9JA9QUs-m0V8wAbTVNZMDF_FaoSIHOqvQ1fbV36L6EucNNERAU2uNshtIwqjND3vPmiu_Svhde5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگ روی لباس رونالدو برای ششمین جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/93964" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfyNFvPIpYb86ZFPH35as-yPp9cK45PV3GBDoXfcy18nXe6mzBgTmKuPcw-tiXjkltEBq6vPcsXYx16NL8IZQcBXbOLhIJ43kR-N91HbexCz5sCmW7609DSFIda0Pgzf5cSaJbwo1APwGGzaUz2PnRY8vhAax1FboNAVnc29gMN58aNTyPzni01rfakxiG4TwXHBIn1hn-DSUhbC56AZXmnOf5kExr16z7tdQT2pLQt9tqFyh_OZ1ieYMLMFgc_jhVsAtxTS7idjpF6_xbVjj6NvPHhPdaWKht0NlD_OVUAkG3ZvY3aqegpZDK7WffdY5wwRY2OwbHQj4sdeeKMfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
🆚
🇵🇹
۲۷ خرداد
🗓️
۲۰:۳۰
⏰
پرتغال
🆚
کنگو
📌
نبرد تجربه و رویا در جام جهانی
؛
جایی که یکی از قدرت‌های سنتی فوتبال اروپا برای افتخاری دیگر به میدان می‌آید و تیمی تازه‌وارد به دنبال خلق یکی از بزرگ‌ترین شگفتی‌های تاریخ خود است.
⚽
🔥
پرتغال، یکی از مدعیان همیشگی فوتبال جهان که شاید آخرین جام جهانی کریستیانو رونالدو را تجربه می‌کند و با ستاره‌های پرشمار خود به دنبال تاریخ‌سازی و فتح جام است در مقابل کنگو، تیمی که برای نخستین بار حضور در جام جهانی را تجربه می‌کند و با انگیزه‌ای بی‌نظیر برای شگفتی‌سازی پا به این رقابت‌ها گذاشته است.
🚀
⚡️
آیا پرتغال می‌تواند با هدایت ستاره‌هایش مسیر تاریخ‌سازی را آغاز کند؟
یا کنگو در نخستین حضور خود، یکی از بزرگ‌ترین شگفتی‌های جام را رقم خواهد زد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/93963" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf_Q9jwhMgK2IRLoyiS_IVBx5bb5sx6_oaMc_ZMFH8Lyq0tJMcrgnfMxopVrbMYauZnTZqQT2vpsoZt2ENZ56Abit8YMN4ddqyt_Ce1AOEMBcToW7N_L059M7k_u5rxHjso3osyWkCZLRTlMKMMulm1ueBhtPs8QIsS_QcYFpr-Ox2bP7iBDrnKp-XJrO3_IBi4UUMUu6ZaO7pzvW4_u4njo7rymkQUBVNarWaVfPo_azzDtIOUziwwCblEyqFxauaItdudSpDaRlZnV9VEHMSQXcudlUs3-vkeUvfTbjTGM4x9D6ySp4j8YewRvLnruXzVSyt8qexQQgzYswyrFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇩
این وسط یکی هم پیدا شده و 292 هزار دلار روی نبردن پرتغال مقابل کنگو بسته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/93961" target="_blank">📅 20:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ادعای معاون وزیر ارتباطات:
اینترنت دیگر مثل قبل در شرایط بحران قطع نخواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/93960" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q84D7TtggbgKgFmctn9BAU8L1HafrTkCvzeZnI-OLJzqoZnRXO-KhlH3wHRoxZc6M6SKg7EI0oNWw93pLVIvbkhV1RnO6ptvQPLKE_uBsvTpzR2p9885tMnNauNgrhh66zEFmIgdKPCLAQ7Rd9D3MlzYQnvnCe5dQFC8nOWuYZZIhREE9K5ccIQ8X4_EThCi6PEgT8iyiBDdG9CvtykZgh9mjcP5skwPFUEEafYfOvfIqSSv_mPQD-GLXm2_Xw-CO02kSwBojOK_4V6uS2uYOXtBC1lzKveWrJw44Qc53W6ZP6FL9gultWOKaFz7DPZCzrFDkTzZtFkdA5DLrV4vYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : خیلیا معتقدن تو بهترین مهاجم دنیایی نظرت چیه ؟
هالند : من جزو بهترینای دنیا هستم ولی امباپه و کین از من بهترن و این فصل بیشتر از من گل زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93959" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ4wbMOZGWYmkQ3P3mFsUROC-DX6PyIpLBvJSp0APmUS6nHrc34JA--5fuDJRRj3PkjOeymfQBarXRbwPWmYR07X44tA5YcyqDTQ3TFOsOpHdZLYpt5wGrl-J6c6tawtnTK6gQcpNERwV1VBbYU_Apl3IiD9-ikjgmGT3FC_9l7AdixFREWANEKZacooNG9fztzhDLgCqoLFFINMCE7wlgCTFpQ38St2PEuc_qP3Pwh-NbusgY00ahmbQqZQxgVLnfysiCSMWCSPBqANeHbioPLRcmh3ShSrTOijaGALu2fEu9oAkrI5kwm-6d8Wh0IbPNPG7G-yE91ZW76yoaOKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردهایی که کریستیانو رونالدو میتونه مقابل کنگو بشکنه:
✅
در صورت گلزنی، اولین بازیکن تاریخ جام جهانی میشه که در ۶ دوره مختلف گل زده.
✅
الان ۸ گل در جام جهانی داره و فقط ۱ گل تا رسیدن به رکورد اوزه‌بیو (۹ گل) به‌عنوان بهترین گلزن پرتغال در جام جهانی فاصله داره.
✅
با ۲ گل، به تنهایی صدرنشین بهترین گلزنان تاریخ پرتغال در جام جهانی میشه.
✅
ششمین حضورش در جام جهانی رو ثبت می‌کنه؛ یک رکورد تاریخی و انحصاری.
✅
در صورت گلزنی، اولین بازیکن تاریخ میشه که در ۶ دوره متوالی (۲۰۰۶ تا ۲۰۲۲) در جام جهانی گل زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93958" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/93957" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93957" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoO3suMcvi91nBrlRDGHlj8SIzzxGihGAntNzq2OvpLdYXJMfMw4glW9wMQLifpSSvvY093N47UNiJ7hx5nc4Z_jBc9ROHhG3vr5AdVu-HluDX0PEhXhwL57cAxLFv0M8V549Xj4pknMvAKl9movq3lLMWeB2_L8LhAUx6wouMhlhoAHCNfQkoOV5eLnUL0RXUDlIQnI3kwc_EXV8zxirB24rpnAM-Yf4y3ArmKXPJCxM1zTcLYLo_5I2hbul8fbIbPgO29tvDz3IXU-XV4ZYxTkB-0Hm0gJ0yMh2iqT-5rHyleXaBoxp51dNviI0UC0fBGTJmz9twDFlkh2ZZwYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93956" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv5H2blIh6UzP55T1gFRpoMMH-es51XHh2Br2th1e5e3FBtdpC_os9TMyK3t8OZAQqaNi-Gzl_hacRzrtO_ecU4amFX-GMNLCKgzHy1On-yX4_cJiLAELze5LTcMTfqfG2agfoC7PlIULWDx0QQGQgF-I8B5XWA1Ln3tjFboowY1I_xsQoS9CyXT2kiDJST7ur9yjJcttRMEVlc8FsmfFQWaF5_lxhSYnZJqfMqwInwykj8RoXuHU2eYD_WrgjkYW_fuC5nWQoE_ExigWdAkn_fqPHRB86GtknI8f_MQHAofeHj4pBvT84MPhBLJFh1W6Rp8ax0D0ehICm6Z5K02ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو پس از لیونل مسی دومین بازیکنی میشود که در 6 دوره مختلف در تاریخ جام جهانی شرکت میکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93955" target="_blank">📅 19:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G37HdKffdw1TuadNB0yF_WL2upvigI5I3WJsyKn10swqOMuNGDNPqigQc-95aJbSQfRTDHp7kyo_RGmePoHTJCWgMKFnRjMO0OHNSDlrGuhIApMJSsiBXRGHtjucOMYrdAIrvAN_ezqlJETRymVNjWJVLMXmxmDrjO9WRMKHMmurPeI4C3vXZLEZQ7m3PwRx_gszVHn8cPurptV-SA1oQiF1a4xQlDe0u8uQ4vrdVdd-XGa4dnNvF4BPo2IZ7qHYsRJPMeHtqKpqDNTdawiyfwjV74PQ2z-ygzxK2f82mNbdgI-d1XlWoj9cW0C4uX8tNW7VTdx_nsMNgmgBM2zlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین پسر
🔥
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93954" target="_blank">📅 19:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baXnMa5mA9_DDXzh4STnJBuHzzIg1uZ7fIqEPStJSUTvv7xSpRKtUDR4hIP0tO4S5KPTvfYWaOvt5O0TzguLJ7NNoWvprT_Aee9iKyGfMktQIWB6BZvBcxQK_HJ9kLKG-AggM3wRg72v6tam01QELqpHNfqLSOIYDThbx7_11_Eel4bO74mj_kXi_htSt1ndA8_Thnv9cxAPHv5MFJ6Y7X_qrRerAjPU_bzUZgdK-H3icwscnCQFc0mGP5w-h6-hQuazLz9y8IlFNm2loc0kzjNqDgQUCsywCpLYmA_diTk_mQyBRaRiDAbr9WZHUZkrQg3mJDe0jctjUCJgHXirvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب رسمی پرتغال مقابل کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93953" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibnlhqvsvBfBikO93h8H1rpe0fRPvNFbHHvhlD4ao4Xr6lSWAuB52TWJrqN6e6J13y3AclT8_a2powQ7-wN6WC-v4C1eJG33ypkJiGkh8p3kkt5w2Zf7KUmGHlACGq2fb-BGbBxl73DkhrhUCdvO-YCBaiJVp_olZpMCKEIw71KOKY6IfpzoFmbsbvRIlkJJTDQttPgwVaVV5-1i2V0NEm4KZerd5lK9TiHrEjpfJCijNquRIarGPjAO6VypLlxDNEnOcKgI0W53dSh2zofXFlqBHu1n3d_KmIdqe7tbaeJnOROImXWASwZ_RurkoLXv26vwKtpDiZPi5Ycum1AVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها راهی که امباپه برای بردن لیگ قهرمانان اروپا داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/93952" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuRd12mOJVZsvayTJvuMARMmNlgZtwBARdrTdY_BhJmsWN8PU5CEp_wQ8UmQImBYWWGppX4UIptjXiQSZVcGxgN6f2Pv146pEPmAAD2z3Wu7G2MZ7hLGjW53y34yWGEzI8tD6v-IxWaJXPUlwS06qMOhtVlrtuw2g38qcdXYccLBUJ-7KvhVgMDXSzBuhEM-OuUs9U-GID72ZvozMmyoA24h0M-HAAx6rJsbnEEZQ_xNybFC8T2T7w_97WGiUN1iEXlqnnqACKdtOci22_4KhFasEQUtG3JXSWtoWsLwz8UbM1ptGWkPfTXziQV4FXXUUep3irnHS8BeiK11A_bCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب رسمی پرتغال مقابل کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93950" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXCDIIN04uqCoOOmys1bHaq2LKa68eKiFMDbnrrZMhr7I5PBZbOmKl3UVdvC1qHAuu3hz-MleHTJ35Jm0dIf0GbhjhvhxbazjzQ5DQdmz_pQb1_KP7hOkBa6qQUR1Xq6QTfP9XEWJ4rvrBhwl9d6z8_01HrGyXeYUOsmSyP4rD9plvlTioW4yY7GD8jIbqQ1a8ojLAF3dyq2zW5zePK1LPakjsd3Lk09Te2x96LRAd3s9qPIcY7jT6Hgbzvhy4cCdBIHYwV1_WKOFQvJ9_qUNHgRRxpyvI804cbupTw606bw_IHfnmXvQcZPsvoy3Q7P_ES8B749C29HqmJM2DVLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
وقتی خدا یک شبه برات جبران میکنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93949" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYc81HfAddK4OV1W-tf068qAmy6CHo87jSmV0EojYr9syiZUGOqwLbna2V4DerWPGWbEBB4E_QiNxV5c3R97WY0QS-ir8GRPWhA-qFVo4e4gWYiZ-jVcXw8r3a925i0d7OvCwEbgAJ6zk33pIZecwPIwfRRdphcX-TVHisgD85cCEpywKhbjBL9FGW_kSUWC1iHL6WX-qNA5AbdV6N1tHuy-nyDJFMaj6VMaqI0jTim_JiVXEbrv1ieWz1wPMs1ia_P6gJMUgpD1A13nqYMc0IDyYKEmpOJOwIKoNs18E2OQP_QzI6LnciDrkod-X-Z8OrRlKinOp9ghtfkQzEmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به ورزشگاه رسید
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/93948" target="_blank">📅 19:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ece8d3dd0.mp4?token=tbqTEZDxyUaBBUa6B9RwrS4EaAPufBQ213VIbNwwpmKk3c4hI9H-6D8KXE4B0YejPBCJhfBSbOGZbuBKRCTqk6dGphboBNyHssbbNC8cLSP9FTHTn_k4JsIFEH5_-5usOBgZB7TCFzfwuoWYKVQoiUsrX3wyFlbZ2HvZyBk2rvDfekInB_5kpNj-cBOCxflDDFWZEhgbAeonjf-D_kwigvNcGY4KAzRbwBq8zd5Ovoz33jWsXKBPAhOD6r2LXaoPzbHkHGmtUwZe67ERsM0Lx7WCoy0azBGkeWZOAdH-L2drtRhpeZjD3I-fFZ1FD85tN_yjwKLbvm3ri0bhrkSPm3QSrmeX4WfLKYmD3mWxxhs4Q_Us7vDHw54pmimMET3Nk4t8HW2b7O-uS-mZ8cU4t3nf_qc9s03fCTXJIdJc3r_Oi9KVkH5njbEgQQrviH4nyw-hgcpjoZOKcI5pUtEGmr-kPdH9wjvGb1DlNPy95lbWw48hDJ1O1JBzBj1NsDq14QsCZstEdDcUteGW5Tag9RXeVuRonuS-ftFGmAXq2w6jU6yNpN_j8yyqU3M9Fi454dZCE5JFLZ9D94DFAEkmxUVxS1IsvRWJzbVQVfz2S0hvNus0tTcxkRxO_IA36nSnFPbV7AfohJxyadTFnfV3e-vZoAOdhO3ZkoFSWQX8gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ece8d3dd0.mp4?token=tbqTEZDxyUaBBUa6B9RwrS4EaAPufBQ213VIbNwwpmKk3c4hI9H-6D8KXE4B0YejPBCJhfBSbOGZbuBKRCTqk6dGphboBNyHssbbNC8cLSP9FTHTn_k4JsIFEH5_-5usOBgZB7TCFzfwuoWYKVQoiUsrX3wyFlbZ2HvZyBk2rvDfekInB_5kpNj-cBOCxflDDFWZEhgbAeonjf-D_kwigvNcGY4KAzRbwBq8zd5Ovoz33jWsXKBPAhOD6r2LXaoPzbHkHGmtUwZe67ERsM0Lx7WCoy0azBGkeWZOAdH-L2drtRhpeZjD3I-fFZ1FD85tN_yjwKLbvm3ri0bhrkSPm3QSrmeX4WfLKYmD3mWxxhs4Q_Us7vDHw54pmimMET3Nk4t8HW2b7O-uS-mZ8cU4t3nf_qc9s03fCTXJIdJc3r_Oi9KVkH5njbEgQQrviH4nyw-hgcpjoZOKcI5pUtEGmr-kPdH9wjvGb1DlNPy95lbWw48hDJ1O1JBzBj1NsDq14QsCZstEdDcUteGW5Tag9RXeVuRonuS-ftFGmAXq2w6jU6yNpN_j8yyqU3M9Fi454dZCE5JFLZ9D94DFAEkmxUVxS1IsvRWJzbVQVfz2S0hvNus0tTcxkRxO_IA36nSnFPbV7AfohJxyadTFnfV3e-vZoAOdhO3ZkoFSWQX8gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرتغال در حال رفتن به ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93947" target="_blank">📅 19:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9-6tDeoUgNr5lGonVkqlvjSkr2AhAUUyN2Q2YJQgcyM9WwdmLo1V0r1xoniy3MzZKYM_nqtVawfGXS3yBvxCIktOY_EbAAdRWKNhSg3ufdlfGpHAQpYL_NDEEvFJvNln5RG7JVXyGyxepJmEtj7kFgoRGQagEdyXssToKFibBo--fSY0y6RPFEZiblovV1lONYZjr7sy_O1SESF6PTkQpxODW6xL2v7Ai1lKMPasJA7SxvkwiZDaXPJ0DCA9We1iE4sMAHKLqe4LeBmdlmtdXbzy3v77qN_ELno6Kc9h4ZGshVKGgb--z_FjtqpBM76b1T5gKQ2TYuVEAGATGlIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریتزیو رومانو: متئوس فرناندز خودش می‌خواد راهی منچستریونایتد بشه. مذاکرات بین بازیکن و باشگاه بسیار مثبت پیش رفته و یونایتد هم در حال مذاکره با وستهامه. وستهام ۸۵ میلیون پوند میخواد، اما یونایتد قصد نداره برای این انتقال پول دیوانه‌واری پرداخت کنه و…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93946" target="_blank">📅 19:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf1k_zp-OdwDAD-twXvG5PD8cLY7cUskqzK6_qrSr9mg3Innbt9wzjPEDTY3nTb0rG-i2lFlJREFE29DIrMwdVIvtiLZEuAlRnC9BGA5coK6ZUnY49qjPsp6oObMIl1bz5SBSZyu9s6x4qLYhYWDiAdgHvNhCnwh5WNYcCzK6wVE22UTfGrK5v7jYJj9ABbsIfl06_XcOKlVM6DgamQW7jgeWZE7mXI8ji-3sU1zuxZgDWlwOZRm0LlnIjND3rwXgRky-L5VMrdSm9b6CXg3ZV3v1trbnaJkS6scZBOdcVr9_gSxwexqhOWE-PCxlLh91hKz4cURIZVLv9Ag_YxQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووووووری از ماریو کورتگانا(معتبر):
⚪️
انزو فرناندز و متئوس فرناندز گزینه های رئال برای خط میانی هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93945" target="_blank">📅 18:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8990694f70.mp4?token=I5Oxt3FseUol91kDLPbaV-Q9jhVFYaifIuZ5Kmnwipx0w8pFUM4v5oFlYjZp9W3soEm-4_3ddIhiiY5M-jL4ThstW62C3zStxg9d5xe0dbCsboC5pr05Utn9HyEYFrCXF3W7UAdKbfwdaCTb7SjuR7q6GKduhUp2aMpB2yfgj1ARvyD-ZUlRMxQD5bre3kBmLo2kn9dF25PiLN0QgnpnWgsm6_o377E09j21FaOVS5sKKyQh-oBvfj1kO-UQ5aG0ashoQAmKZenTvMxqLcJUR9XmzGk31GTMZAaQY2tPEZS-gdIwqaVC55ykytjGgLolFoGy0Wnv-F-yisCimIEW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8990694f70.mp4?token=I5Oxt3FseUol91kDLPbaV-Q9jhVFYaifIuZ5Kmnwipx0w8pFUM4v5oFlYjZp9W3soEm-4_3ddIhiiY5M-jL4ThstW62C3zStxg9d5xe0dbCsboC5pr05Utn9HyEYFrCXF3W7UAdKbfwdaCTb7SjuR7q6GKduhUp2aMpB2yfgj1ARvyD-ZUlRMxQD5bre3kBmLo2kn9dF25PiLN0QgnpnWgsm6_o377E09j21FaOVS5sKKyQh-oBvfj1kO-UQ5aG0ashoQAmKZenTvMxqLcJUR9XmzGk31GTMZAaQY2tPEZS-gdIwqaVC55ykytjGgLolFoGy0Wnv-F-yisCimIEW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
▶️
تیکه سنگین آرش برهانی و خنده های قیاسی وسط برنامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93944" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d573a1f0.mp4?token=kGkR8NZEbe-UfnnIrUWy5qPHb-4YKT-Y55kL4E6jRMm9jqgTzOyM2aSOi4gt4yVCZ6CzizB6liqkR6XTcovPhck6wcYBraf_uEMUrQptZ-TVmgASU8OLfQohY3_vaGgxBz5bKGLIHCFIGRtX2gMp1A8i1_xwnlXMVgux2kgnmD0uI1gG1RBkJOLg0qAwmmQ1LgmqPnq1l42NxDebJJbvUVpbcE7hYEkpNQmAJW3_IzlNzKRbLQIOWbzm9S_I7ZbUMhLkmCpYCiWbdGj1OggPa-RT3DJFiTIt47Wn4fAEATdFXPj7xJkPHgmttig2owfkxc9nE3Hxdkvw04eyzE7TOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d573a1f0.mp4?token=kGkR8NZEbe-UfnnIrUWy5qPHb-4YKT-Y55kL4E6jRMm9jqgTzOyM2aSOi4gt4yVCZ6CzizB6liqkR6XTcovPhck6wcYBraf_uEMUrQptZ-TVmgASU8OLfQohY3_vaGgxBz5bKGLIHCFIGRtX2gMp1A8i1_xwnlXMVgux2kgnmD0uI1gG1RBkJOLg0qAwmmQ1LgmqPnq1l42NxDebJJbvUVpbcE7hYEkpNQmAJW3_IzlNzKRbLQIOWbzm9S_I7ZbUMhLkmCpYCiWbdGj1OggPa-RT3DJFiTIt47Wn4fAEATdFXPj7xJkPHgmttig2owfkxc9nE3Hxdkvw04eyzE7TOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کلیپی که از لوکا زیدان در تمرینات الجزایر وایرال شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/93943" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42957956a.mp4?token=iJbRMLHpKeW9BCot-1G4w-M5WizpcSShSWPqJ_kq5ThFbHmOeBilqL_1ELcLNLGG0S1fwGq_QtKttprXLghx9wqGQBkFJKigQI5BBmVmhfTF1O6wt07gHgE5xl-PcT6vwpfmU-rr6ZsL8-5st_ng2bAvsCfylnyUBRBQA2Y2NRk3mmdQV9S0kvqtK5gEDL3GdhPO7HfQxKEkuPjV5miulTkvNsV1hnkKykIkcluFrwlxtNon2newLY1dmJYiblh39mrBBFB7G-iQPTpYEahXL2jvDhR3OtrvRPaFYONp7VPRfidLB-HsJbSQE9h9C9mx5wFnVHJBUhvcoSohjYJ01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42957956a.mp4?token=iJbRMLHpKeW9BCot-1G4w-M5WizpcSShSWPqJ_kq5ThFbHmOeBilqL_1ELcLNLGG0S1fwGq_QtKttprXLghx9wqGQBkFJKigQI5BBmVmhfTF1O6wt07gHgE5xl-PcT6vwpfmU-rr6ZsL8-5st_ng2bAvsCfylnyUBRBQA2Y2NRk3mmdQV9S0kvqtK5gEDL3GdhPO7HfQxKEkuPjV5miulTkvNsV1hnkKykIkcluFrwlxtNon2newLY1dmJYiblh39mrBBFB7G-iQPTpYEahXL2jvDhR3OtrvRPaFYONp7VPRfidLB-HsJbSQE9h9C9mx5wFnVHJBUhvcoSohjYJ01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کصخلم که میبینید قراره 90 دقیقه امشب مقابل پرتغال، رو سکوهای کنگو به همین شکل بازیو نگاه کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93942" target="_blank">📅 18:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b05b74b10.mp4?token=AcMracilCgF0z3kxGoV1YDnbmLJL8qGXwUykyLP9Vk_X5QAxVK9JmvtrVNkkUgf-KGGSVpCrgbvVJt05AdQlN9dPvQcVAUxxwy4486Qi5J-tNicvaDFcKdiyvb1CiP9nMgmK0DR4vrGOBGWhZoHvIWU5ydvTzstYHQtYeXWxjBlsNvkyqMH4jDdJlZ8MvG40msZCGetGxb8r41_q2_Vs7diltzeCtRnpGLgkoGp_PqyNxMi0rNluhKOpggDTCfebPLATpDPumf2VqzzB5cPXz6fQ5mAapFm1SgDN6KdkeYxVARTtpITzAb4bEshVHF11kh2t7rDWf-L7eJ0-U5vz4m_7uaIUyGvuNBQGPHQx4U_yKu9PeBabnzsm6QRfOxnKDeOzv-9o3IgnRHojAfw8XxQpExojbu_XxZC6IkCLa5tQxNHfQoJgMlO53guwJ8k1ZdqrlcfN9DS3J4BdW_qcDHCavxmvbSxql5ZOf-20twqzPLxkTIWLWNTKSTycJHl6MkzPJQTpyqp7usPO_aU9MjL-np8V9JUunUhkWyaX-C2xXgbjxmbvnvPGgcPE8GYnUYytsUFYbSm2duYVKHPMVFr9ThdbXuKPeLfiZDadqn3mwLT97MJstjnoK5vsvCdSfQy9kzGiS5hgGukPOMCh5gAZ7zoIxdij90gaNe1m4IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b05b74b10.mp4?token=AcMracilCgF0z3kxGoV1YDnbmLJL8qGXwUykyLP9Vk_X5QAxVK9JmvtrVNkkUgf-KGGSVpCrgbvVJt05AdQlN9dPvQcVAUxxwy4486Qi5J-tNicvaDFcKdiyvb1CiP9nMgmK0DR4vrGOBGWhZoHvIWU5ydvTzstYHQtYeXWxjBlsNvkyqMH4jDdJlZ8MvG40msZCGetGxb8r41_q2_Vs7diltzeCtRnpGLgkoGp_PqyNxMi0rNluhKOpggDTCfebPLATpDPumf2VqzzB5cPXz6fQ5mAapFm1SgDN6KdkeYxVARTtpITzAb4bEshVHF11kh2t7rDWf-L7eJ0-U5vz4m_7uaIUyGvuNBQGPHQx4U_yKu9PeBabnzsm6QRfOxnKDeOzv-9o3IgnRHojAfw8XxQpExojbu_XxZC6IkCLa5tQxNHfQoJgMlO53guwJ8k1ZdqrlcfN9DS3J4BdW_qcDHCavxmvbSxql5ZOf-20twqzPLxkTIWLWNTKSTycJHl6MkzPJQTpyqp7usPO_aU9MjL-np8V9JUunUhkWyaX-C2xXgbjxmbvnvPGgcPE8GYnUYytsUFYbSm2duYVKHPMVFr9ThdbXuKPeLfiZDadqn3mwLT97MJstjnoK5vsvCdSfQy9kzGiS5hgGukPOMCh5gAZ7zoIxdij90gaNe1m4IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
تا این‌لحظه بهترین تصویر از تماشاگران داخل استادیوم با اختلاف به نروژی‌ها رسیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93941" target="_blank">📅 18:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_YHf3NQ6jfB0n7-h1YIASvUcYtGEU1Es9GvuHYukMLyow9ylxULmrMsteBE6Et6DHJSVglvRsghMOXrU6U-f89u9DIEpuYcTXrBmsK4tiNeFevIV2HP3bGdSxk3mWiIJfcrzvMSSQmo6mvVhxXel_pzfhYGL70VMfrcWfqkwWOQ_hjwk-3zWmooXl8A1DXp2JIwD-GAHbhsFGgGgX4WjLvN7nQugJuvcgn9fmk5lT-M0N07lMYnwJvX2fWGC19dFCl0KDDq4gi95GtlrTkhv_D1ZvfsJyOIR4OLL1mWuXbQ1dPaf4gFgkddR5gpvvhUaaEAgFL6OOzCB0X81Q_1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا هشدار داده که هوادارای انگلیس با شعار علیه ترامپ ممکنه از ورزشگاه اخراج بشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93940" target="_blank">📅 18:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db21436b4c.mp4?token=Xw6zt0abkMJb0q2AY2AjV7RRhn2jRSkkxu87hTWcJEMkp0zpI7RWSGzio-IZPl13gpGHvsq4SiPiFQHGWVvHEzQC9jgTtV0m2p8qtyRuiKAmUDC6GtNxjDOWWHrq7do6ZkfJwvSdMVyhRF7mjLglbmIEN0BeHrvzYXAAQpAHwfZCw47pAZ3Zhs6lAUKXcoaILnBlgMAyGdl9JMcsvKD9NCek6WZdEWxE-RUJSdf78cS3U-5BfxZ6evZufDA3TNp1Nc6EYVu3WDRei5gd398-bFlrKo0dlnJFNdC2AiiGLItyLiwJHkCpILrpjeajgOOMGV2HQtitC1qA7GS4FC1NvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db21436b4c.mp4?token=Xw6zt0abkMJb0q2AY2AjV7RRhn2jRSkkxu87hTWcJEMkp0zpI7RWSGzio-IZPl13gpGHvsq4SiPiFQHGWVvHEzQC9jgTtV0m2p8qtyRuiKAmUDC6GtNxjDOWWHrq7do6ZkfJwvSdMVyhRF7mjLglbmIEN0BeHrvzYXAAQpAHwfZCw47pAZ3Zhs6lAUKXcoaILnBlgMAyGdl9JMcsvKD9NCek6WZdEWxE-RUJSdf78cS3U-5BfxZ6evZufDA3TNp1Nc6EYVu3WDRei5gd398-bFlrKo0dlnJFNdC2AiiGLItyLiwJHkCpILrpjeajgOOMGV2HQtitC1qA7GS4FC1NvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار آرژانتین کنار زنش : مسی رو از زنم بیشتر دوست دارم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93939" target="_blank">📅 18:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjxRyQa5EbWoOdWrjpou13vR6GU4TldeEt2fBfBSTwS-xhqASoSElxtke2qkBJNP6-x3rXXluj1z9iFyLCX_XJgALtoOetiszsoBo0GA8Sw-5y4M1ojyZb7-rsK5VKj_ggpfhueBEKeC70n6mdG46qBzd02jRBq9ZIT9Hs2SNha-BYCOurii0WktRMYpG_g12DE1i3yHLUufrgpNa7Xow4afpD4PGc6ZeLvttWNFwOQDbEEKwJr2WinpVOGJkLc3mLvgGFq5kEl4O_--MyffByFI5JxQtoF2uekIcn5tiq0PADPkTTcbqwD8r1V7BXRNQk1lcX04ZwkkLmmHcHTPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93938" target="_blank">📅 18:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s62TvJEIQO5TPoYwd26e4rgnJCVwah7Re8WMHFm4ZViERo3V4o126d5L7Z6t57pGGHrJLJMBvhaCE1P6NfoBDjXaT_yZt0nnkvoYn3Pj0JIrnqrOGGWlP0kBMhU24bsgOALUf6AXmDTpLUjVnEY6Sp8ApMMo6S_GVuW3CfNGkPXTv0dKB_ogvGkr_x2nTL2RzwRod2WBYIl6Rc1_ZwXkdxOP7-PZgUkiVTrzpHrc6Ma4k6rsIdDGIhF0IwgwkXwzd_2BJCBR-q71Iks5MzFK9w5bR2YJrvYpV-GjsZSv_F3dCEd3M3C0_TppS1H2onsjYvy5hgJqAVS1AtApTfkT_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند خیلی خیلی جدی رفته زیر پست مشترک رئال و برناردو سیلوا کامنت گذاشته: تو نیمه نهایی همدیگه رو میبینیم.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93937" target="_blank">📅 18:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0c7f99cb.mp4?token=V6-KUa0X0URylLw-s1dXNA_ThFwZ4xNQxMamtiXI_eB-Gx8Zy3ja8a9P5GTlUrujJfhPTLHxqmKQSIaROWj5Gw---oS0zwGslJl86CV9NDnTc9p0Sq0wgQybuaadouvP2YV4sJZblF_4IHibVhxf6psPTqkO8S97_iSMKsnSdc5yCpB_BMmZq9Xu3CEGEfqf_MhQ27-UNh1cvDElrwlHW-n3tK9ZLqfVlvIxY4r0rJF9BHqRKAwl-4XjSkcgM91iPfkw-wSIdo14uvP6fdlR0mfSA94b6VE3lq2OWGlElPEo6X9JRZdVsa2avuP1w1Os9OBRliE5_0YfSPArfAYiwQ6ZfSr2Nz68HSoal5-xc7vwEzuDlABN1qSGwYI2ISllgA_dLXWLpFUu29SqcTko-AvgdtqKwPNB2_Oi2SD45HXgyfpoJtLy9Ck5FjVMNG5P6Xutp6vfyPlDlDcV49VviZGfNs5La8aZLQ-20tXs1EuyLgqYlADRV6ncsHskiK4OAGh96wxECax93UgwUdAhs0z6OGGpVIIphOKWRNuGIRGIXL7JK4AuxWu1Q0HWA-sbmXKtngbUKp7weOiW-pZB7rot8YTydGWFF9u2D7Wd2N4gZBt1tjHL_PyalQIA5vP886HUSiFBOlDkqi6dxDJutdB5y75_CJN3LWRL3GIFVaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0c7f99cb.mp4?token=V6-KUa0X0URylLw-s1dXNA_ThFwZ4xNQxMamtiXI_eB-Gx8Zy3ja8a9P5GTlUrujJfhPTLHxqmKQSIaROWj5Gw---oS0zwGslJl86CV9NDnTc9p0Sq0wgQybuaadouvP2YV4sJZblF_4IHibVhxf6psPTqkO8S97_iSMKsnSdc5yCpB_BMmZq9Xu3CEGEfqf_MhQ27-UNh1cvDElrwlHW-n3tK9ZLqfVlvIxY4r0rJF9BHqRKAwl-4XjSkcgM91iPfkw-wSIdo14uvP6fdlR0mfSA94b6VE3lq2OWGlElPEo6X9JRZdVsa2avuP1w1Os9OBRliE5_0YfSPArfAYiwQ6ZfSr2Nz68HSoal5-xc7vwEzuDlABN1qSGwYI2ISllgA_dLXWLpFUu29SqcTko-AvgdtqKwPNB2_Oi2SD45HXgyfpoJtLy9Ck5FjVMNG5P6Xutp6vfyPlDlDcV49VviZGfNs5La8aZLQ-20tXs1EuyLgqYlADRV6ncsHskiK4OAGh96wxECax93UgwUdAhs0z6OGGpVIIphOKWRNuGIRGIXL7JK4AuxWu1Q0HWA-sbmXKtngbUKp7weOiW-pZB7rot8YTydGWFF9u2D7Wd2N4gZBt1tjHL_PyalQIA5vP886HUSiFBOlDkqi6dxDJutdB5y75_CJN3LWRL3GIFVaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز قبل بازی عراق و نروژ، شلنگ آب وسط زمین ترکید و اینجوری زمین بگا رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93936" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1540ce85.mp4?token=AoHuvVcSOdscoWViXhbSz4Whtde_45YvaiPjULKJzinjJjssdKqCf46Jd0mgOkXr6hRIM7dfj8mLrbybqUVnpfegKh8r5sMGbG36_Qh6P9HZZeQjg0yw0Aa72YeuFxzk0EEuu_aInOTZVPfIUrjsLmXlS_eCwqu_vFTpCoVqjUZAZWiTClGm9l_MmXA4O6LdWVhwJo_YFbPGSjc1B8oNLaN90BYZ-VUcl0BKxcs31Di_bU1VEnjmfovNjfJxcHbv2ho-EZXHpgq2MurOut8RPpOGntIxS994zB0-7MQbPy3sxhc4RPaSUdjLT9g3_P-kvQ2Quq3NHun90jEB0V5PXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1540ce85.mp4?token=AoHuvVcSOdscoWViXhbSz4Whtde_45YvaiPjULKJzinjJjssdKqCf46Jd0mgOkXr6hRIM7dfj8mLrbybqUVnpfegKh8r5sMGbG36_Qh6P9HZZeQjg0yw0Aa72YeuFxzk0EEuu_aInOTZVPfIUrjsLmXlS_eCwqu_vFTpCoVqjUZAZWiTClGm9l_MmXA4O6LdWVhwJo_YFbPGSjc1B8oNLaN90BYZ-VUcl0BKxcs31Di_bU1VEnjmfovNjfJxcHbv2ho-EZXHpgq2MurOut8RPpOGntIxS994zB0-7MQbPy3sxhc4RPaSUdjLT9g3_P-kvQ2Quq3NHun90jEB0V5PXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🫣
8 سال از هتریک معروف و بی‌نظیر کریستیانو رونالدو مقابل اسپانیا تو مرحله‌گروهی جام‌جهانی ۲۰۱۸ گذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93935" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00991204c6.mp4?token=AOCGux6vPasekWUq4ZLFSOPAbqog5696dqdr5gM6vE32FGYaVPWqmORV3L8j1tfIUxA_NDnSDVBd4Q-PkDyJ562xGAzayT3BMSEsTPEsnNm-ovC_T41aD2yPapQW3eRNT8gxgFucz5YsdkNul0S0guEp-JnwfT-FoVO_ld7kigY-v8XYPW1jPdRZBkTxS_hR0ehHRsA5xl-Vzcq2l7XTmMcwfiMZahjfyNtjriDBk1QY_rmTHY9eUxllEl7gRP07PZH_lPmueDkN53MDRv5SQrt06cmyK46QI6NhHLNdPBR2SVFtqEHkbIXrvqwCAb66LK2lsLIz_AcPqKQ3WRaORhRUqmhAD-JCXBCzfDELSQex3MQxLR-MD0J-yT9P3sHnzJN6A9hnnEiKHMYydNcBFGU3xjZXBP4TQ5XIR_Ha0h8TZZIvKi5ZEM3FkfoWW9IVpOHdJ8rZhKWDCTtgkpMvOF3v6VK99m_qwpLWnGBOtOxboGCHd58Cw983i2v_2q6G1i41WepPPwaH57r8CiNcObywryakYR3n0tIzqSZd4g9SL6TMu8lPS08gUw8ESBJHhEK9Xvifb9RtaE16gxDxcCzJ3pNp8vVoDARlSIPFtHG3PBeONDtQuGTY2QcfAdbKfr7dToj5g6yjpZsNhuPghApBuLBcK8QXuEU8VKqohu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00991204c6.mp4?token=AOCGux6vPasekWUq4ZLFSOPAbqog5696dqdr5gM6vE32FGYaVPWqmORV3L8j1tfIUxA_NDnSDVBd4Q-PkDyJ562xGAzayT3BMSEsTPEsnNm-ovC_T41aD2yPapQW3eRNT8gxgFucz5YsdkNul0S0guEp-JnwfT-FoVO_ld7kigY-v8XYPW1jPdRZBkTxS_hR0ehHRsA5xl-Vzcq2l7XTmMcwfiMZahjfyNtjriDBk1QY_rmTHY9eUxllEl7gRP07PZH_lPmueDkN53MDRv5SQrt06cmyK46QI6NhHLNdPBR2SVFtqEHkbIXrvqwCAb66LK2lsLIz_AcPqKQ3WRaORhRUqmhAD-JCXBCzfDELSQex3MQxLR-MD0J-yT9P3sHnzJN6A9hnnEiKHMYydNcBFGU3xjZXBP4TQ5XIR_Ha0h8TZZIvKi5ZEM3FkfoWW9IVpOHdJ8rZhKWDCTtgkpMvOF3v6VK99m_qwpLWnGBOtOxboGCHd58Cw983i2v_2q6G1i41WepPPwaH57r8CiNcObywryakYR3n0tIzqSZd4g9SL6TMu8lPS08gUw8ESBJHhEK9Xvifb9RtaE16gxDxcCzJ3pNp8vVoDARlSIPFtHG3PBeONDtQuGTY2QcfAdbKfr7dToj5g6yjpZsNhuPghApBuLBcK8QXuEU8VKqohu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
وقتی امیرحسین قیاسی وسط برنامه زنده زنگ میزنه به زن آرش‌برهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93934" target="_blank">📅 17:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ3jtqbNCEuZ83SSHy1bmrlUWVxF0I67zdsYVKFbxPRyfrSQBJR5D4opX-EhZE9orx8yjsB4J-kFW559fOF29Mn3aphvGQxTb6as97-sHOFftOAz4ofEHkPIF7o0nH9sygBCK_8Wr8_FFJHg0kA-wYkEa7RDWGTSfk4eHFbKnJ6kDhS5Ifx8jDCl19Emwg5Uz4zvLuTimYFuQ0ibno1f4dE5p3_aKSzT34ZNPpG4lHUz9G2MZYQCuRe2tffJ1jd2ZnxP72FNe40cOvgHc_tlGbZwvOnZHtmB5kIwQWf25bc7tGexIYAE3-P2Gc3qFDN6pVEAZPDL_SQ2vWotvHLalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Diamond
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93933" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf_mNi1QwGoseJ0Bd4olD3E_qIeYHI5st6_vuu2hImZpyMnU7uWo0in3UaBAmGvKV-XMQF7NDjl12iHLojss8CVKePzcJOBtkp2pBHLuo059u34YClTPdXHfetkPBdCFiGov4x7lwFSTAAF-eHKGroK8_5MFR1G5w2i5ev5RKkd4zey9ed9LbLnoxaUuMNr0scKTqRPfWvxNNV8qPYhpUx74jWycMszdzRZl1xdirVLutI4Q3KGHkg5NfqzBbcaOjR2p5zJdDAxiGDkvHARkCS6Poom8xQ9NHgfJeTrot1v0yPl55784txgXP6Zn7kfzxyDR8o2hPMCFyuysmBqOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو نازاریو:
زمان آن فرا رسیده است که جهان از پنهان کاری دست بردارد و این واقعیت را بپذیرد که لیونل مسی بهترین بازیکن تاریخ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93932" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
🎙
روایت تلخ رضا جاودانی از پشت پرده برنامه جذاب و پرطرفدار «مردان آهنین»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93931" target="_blank">📅 17:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c860678c61.mp4?token=JCOmqvDWEe-0xDfaisAoyZtPJbHff36t_zAAhKq4h9wVgFrhSGyOHH0Atjdb4BKJ1NXYQyDjP0Hum9gvJKFdbTG8cX0ix0dmg1pFxWuig8GoZFC_z7QzdqzG_cUqnqJgzugGvyQaU4f_I6vFhI07ALdZWTfz0-4ueIyrElQkmvq84fm6amt6xm70veLpjqgGhe1Nmuvfu3jPTafjuYLgKSoE8uv2D4a-niN1qDTHUQCUWZF9ysVWM5X9ip3pp1sPmTyInEykk7-46DEICS5S-VA8JAZbM1tQhtMxGcjlH8pkkClY8xjsns8EWH7_q3UsEzcjMLaPg1SZaBK74DgyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c860678c61.mp4?token=JCOmqvDWEe-0xDfaisAoyZtPJbHff36t_zAAhKq4h9wVgFrhSGyOHH0Atjdb4BKJ1NXYQyDjP0Hum9gvJKFdbTG8cX0ix0dmg1pFxWuig8GoZFC_z7QzdqzG_cUqnqJgzugGvyQaU4f_I6vFhI07ALdZWTfz0-4ueIyrElQkmvq84fm6amt6xm70veLpjqgGhe1Nmuvfu3jPTafjuYLgKSoE8uv2D4a-niN1qDTHUQCUWZF9ysVWM5X9ip3pp1sPmTyInEykk7-46DEICS5S-VA8JAZbM1tQhtMxGcjlH8pkkClY8xjsns8EWH7_q3UsEzcjMLaPg1SZaBK74DgyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرینات سخت و نفسگیر شین‌مین‌ها دفاع 20 ساله کره‌جنوبی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93930" target="_blank">📅 17:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3804d558c.mp4?token=FzdAzJoBKAS4sW2GjWFAQMv6Fb9rqKFMhW626jZrUib0TqMPwy2AotqjUB5cv1Tqz3maR0_lHDl5Gr8qMA6WMVXxoZcuaFxbWqdurUVEeasJ7Z_bxqFACiXqjRmgKa9KNj1qeWMjBouLZ31dn2ySONdJDvDltd90_f8vo5oqOWjeC8ftSwTeXoD8AwpaiQ2-s9chvHOlXJvhZkDW6RCmsC8D1hYS9S7hjfLgNLAju6oXY8K2hWOM46q5JZGNq-3-faRujzHY4YBqmRVa-qc0IBOCUyew0hzDfeCqr_DhxoTPe77inhnWyJMqzbfDYipDXuPcyTnH70rfLGt0m3tBNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3804d558c.mp4?token=FzdAzJoBKAS4sW2GjWFAQMv6Fb9rqKFMhW626jZrUib0TqMPwy2AotqjUB5cv1Tqz3maR0_lHDl5Gr8qMA6WMVXxoZcuaFxbWqdurUVEeasJ7Z_bxqFACiXqjRmgKa9KNj1qeWMjBouLZ31dn2ySONdJDvDltd90_f8vo5oqOWjeC8ftSwTeXoD8AwpaiQ2-s9chvHOlXJvhZkDW6RCmsC8D1hYS9S7hjfLgNLAju6oXY8K2hWOM46q5JZGNq-3-faRujzHY4YBqmRVa-qc0IBOCUyew0hzDfeCqr_DhxoTPe77inhnWyJMqzbfDYipDXuPcyTnH70rfLGt0m3tBNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
🔴
اعتراف امیرحسین قیاسی به استقلالی شدنش؛ بعد از گل آفساید گولسیانی برای پرسپولیس توبه کردم و استقلالی شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93929" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93922">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4sBd0x0QjYGjegmjfI4-ahOVFO7bqeItg6JqjUIdDNwKCudNqhC0lBxIMde0b4h9AnMzKOnPp2Vf3kpdZRijDUMofwVy_wsYQxMRwprY2q4CJ-VpZG3dd_9hwkg1H5MhHmM4iH1ubVES4LAz-75FmhrYo98Vjy9hVWGbzXW5N-CJz90SLL3BU2k3sTVcvOI-BRk0WFft1jAwpOOCC0F2rC8eAPtWOqLrfRekcy9Ij0kzluZ0df7UcuDTbwJrXZSsFXAr8b2YcnMtJzkLO0CH9-7_xMmP9X-q9pGe8POYrQXyGlfmSMuniU6jFna75i4dooA6TPp-imsGCeH5BiPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCAgsYpPDVwmbI4If5eIPnC-bEhivpMjngpNx07Sa6JEonquXtlg_51E2ePRlSZWkBLLl4HJXK6Ldvm4MsFnfPefCH03NqvDiPBA1Nd0T9yWEnjVriCr0jKg7jOQdrFdvk_t8B568LAUFsMkvMqRvScvgjEq-Y4BPpNcQhXDxst9HGlhIZc7xxks9x9EFF62-gBcSr0R4Vq0Vp1PM3wpjoOkJPpV9WKFFD9no4is_4_i3Fgqz_sxlz7YtAUDe6YMXmTKn4vknMdpWLA3HXA8v3E_yNvQi5rCF8UfhVqLOXwxWHMccbSvQCDUra2PQXAcMa-13eQQwfIDhaP9IMWT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3VOezO1rXchWDeLJMxD1mZhaIu9bLE0jmYNEOpnmXpeXP0Nuz6Xp1wXPo-1_25xpdyU8_34R6gndfla0sfUfbSbVP0eIWKCnc2Mg-LuKYagGMul2xWKuW5hAakmBly1mvSZqxnVXlvtJ2w9weHJ7ojgzteqIBntSig0XEa9GFJIiQ5d5N6CObYBXwZYCOswhowGew0JdPaJ7ZZJ5odjulvtZp6VPZyFaf0U8qfUfInpqziV8aeCHvND5MCAe1jt95zcjdD6H5kMqBqYrkkdvPnw2gvpiH790yzj0a7SOfHFDil1ZvGomSB-7k8Fw_K5ehcSsI2kZlHJmFP39IupoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7hVIGMv0f-juJs-ArowbZp87_IbHoVkowau1C47bPUSh-uiQ6169YXW5XgyQa8F-cQKxZYPiN73R3K9IpQzWjoEhBLmJR5-FTycxTlpIUPMFcoQRNESOqp6fw9M2sa1xo_wS2dqDXffzQ_2IR-9aR5ZQIemngHco_ql24he0GMwwNPgz5ikXkgqpoZ8o-a-EtUSptQvLAwdkRLqiA_taYRHws5jXWikL4xiVhQtJ3I7xKsqz7Z74wLEnH3mBHVUZcKbR2oFIfuHARAQvGJvtrB9kCwejHVjUrLnNaE3A44WMgSPogi_A_YxPA21qrAw5FiJ7bjJd1Xmv-6wR04WqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoJ8MFYpnD_MTWDauXZzUpMS-nE0BZ2TKfVBqCUovxnBLF2r_b571YYe2MvaKK2LUyRlUad1DA--It5MArbR19Jr6CRxJegABQWBZ0_WlVRAA1h-SOXblL4WKnEL9vEHhC2NKbnYuKDrUD28cVT0laTuxPjegkVVD6QTNQfxfJWM-lwW63CkeQTPN833g29r926LS4cVQK0oleK3yFlVxmda_ZMMX4EvV5l-4SPp77772lLoGNVCUCXc4YKIPFYhnhL_kQuhnsPcsxWl5_Y-dBJNJvFKGWGhKlxkNB2-S3e0aR_Sqnqt0vGSYtdPIzO_a0EN_o2R-EqR1Fm2ErGFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpbS7EnNbJHks-8OLHdbTq2C0Lud2KM_0FfuwBUrVfksYwHmqbKWCPtds-DiYCYeheIdZpaV3tUpkDOyJiaBTTdD0pN-KUkALrGS24_Ie67gmsdVCIQ7Pa2D2bXyhFecZYfiKT2kQuOYr0YCqgiyhq7gqGQvv0jQQWGJgEjF6c9lTWrgO6IIu_D31AeQai43dH-7Ii6OiEte3aQj0TwM5mOS3mcIHvmmo0yVDUpIuCMSkHE3rfQswPezNJ3-1i9vZiOqWCwHXvweKn68ahrQ-1llH9O0dTGFa1Dkq8v65g8H9cKLZu3hYH8OHA3y3JqxsCH7iALSq7ie4AMTE6gASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DblquF1ZAgP9I8jzMlUcBleoqT1tEQLJCEEKNxZJe4m6CCaAom-yDpXLj87_AfMM4t7_ZyocQufvX4YTYCuqLL77mNFR_29vkefT8H2MP5SRF0pi0Q_vc27NxVi774yBuhQz_ZdGPG-kG7tEszRPEZ6wnSdd2GEPtCLwxwwShTTKne5rerK4aGy2egZhK-rrIA6nwMOMXJP9VJQ4G1eexBWIx5BZt35eobuQlBSM6HcsVNLxvoOz-eZzBoAhXQCLiIoeHRfqXAeLwAkauyNmDZQ8q6fOPGyQK6YG6mQmirNsg9im_Rul77qGhHWjIDWUHMnwd6Of3VA_iRxMRBn09g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای آرژانتین و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/93922" target="_blank">📅 16:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f946f90fc.mp4?token=eV10I3OuRCVpaL0YPhVTuQzIbbpjJaXs9h0Ril2ZXXBMpXPn4Ho4krnAWG11FtqXMnfPZaF0xtwqT21OEqODwPqxzncoE_1wr8zOqh_Iq5tTL78wip5MGm5AMRF3NUhzzUwwuaDh9h7iJxA89FI3Tc11OajBDwBdQvjZwqmx3kCPWxWhMQVYoBtxSjCErYVk-difKyedKm2VfZTEEc14Nuul5TElpuzHYlqcH-LhbD0eOfVdJOamssuezTI3CS724gAHGI2OJkmwYyKaPQKUaEgy60iSDRYpNxZxb0v4GhwiQEbFLkNBvomiATrbOn6jbg6mev_P4rh4bIt_zLkvkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f946f90fc.mp4?token=eV10I3OuRCVpaL0YPhVTuQzIbbpjJaXs9h0Ril2ZXXBMpXPn4Ho4krnAWG11FtqXMnfPZaF0xtwqT21OEqODwPqxzncoE_1wr8zOqh_Iq5tTL78wip5MGm5AMRF3NUhzzUwwuaDh9h7iJxA89FI3Tc11OajBDwBdQvjZwqmx3kCPWxWhMQVYoBtxSjCErYVk-difKyedKm2VfZTEEc14Nuul5TElpuzHYlqcH-LhbD0eOfVdJOamssuezTI3CS724gAHGI2OJkmwYyKaPQKUaEgy60iSDRYpNxZxb0v4GhwiQEbFLkNBvomiATrbOn6jbg6mev_P4rh4bIt_zLkvkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حواشی امباپه در ماه‌های اخیر از زبان عادل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93921" target="_blank">📅 16:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqDLdDgpF3UkbuY_Inr-yvM8kFxYRomCEaRGV3iXWiCLX79o6FWUo62tXTfoC7q8yeBNfFGAWyBHpsJT5XbVnn2aODZhTIGf1-67B545vmFjabYAqGgyK9aSxazn9poy0JAt9IvKP5p1q6I7kKK8juuERnKD5kdelrLbgRRx7dy6w_DZFkX_IgWDjNC1rCnKWkEwpvyTx5ZizzspuqpkwVq3u2yLonnYqWiDqWgrKBiS3LM0WY0hCbCrQrJNuCmooTPsToZf_ubU0GC8JAc1O9LwlISyKjYpk_A_RkvEMfSDf8EFdLqejoJTFnG7beJmREv5LFghjQCR2XBXgGCU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔺
#
فوریییییی
از خوزه فلیکس دیاز:
رائول آسنسیو ممکنه رئال مادرید رو در این پنجره نقل‌و‌انتقالاتی ترک کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93920" target="_blank">📅 16:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93919">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TWrnwnUokBx38txOsuMRW8qykDsCdwLXD5k2BPrNl3VrcfzGp66RGFMeizXUqzVnsYd_Ni_xlMY6osSbcVKJVmDmfVYo7W2WozTWp17LnJSpkKQT-6yZ-W6JQW2SnPP5WJvWajHByoDJUBpKRfa_hGUX8LLAy8peJWA4he6NdjkQsrU2eLH8oitXLiaUfGBzR1DVlqPxauZuI_M7K3VFCKHWXQde2OrMJD-D2rgzTIXU1LPoqnY13Fuq65Izw4I7bs3BJJEN2rttPMWSo9kTtFlFO8ocYA4yXK6cyhFWivLHDBWG9eN7kYtX7eo8Vg14Z5Aqetllefy-riunAStd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
مسی در پنج بازی آخر خود در جام جهانی:
🇦🇷
🆚
🇦🇺
مقابل استرالیا | گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇳🇱
مقابل هلند | گل و پاس گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇭🇷
مقابل کرواسی | گل و پاس گل + جایزه بهترین بازیکن زمین
🇦🇷
🆚
🇫🇷
مقابل فرانسه | دو گل + قهرمانی جام جهانی + جایزه بهترین بازیکن تورنمنت
🇦🇷
🆚
🇩🇿
مقابل الجزایر | هت‌تریک گل + جایزه بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93919" target="_blank">📅 16:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ee7676f0.mp4?token=BbXEeg7W9OYztNq_XCAfIubybvxzohYzlTysHao0FsRHngikvAbPmphOQUWfyQ6UdIKzZ4QpYTpOxp_s5mg_tjtBqTvjgAnt2z449hFuhlZtxtfZe2ystiHy02syadtlDQdTzz-pe-LVFc7RZBjN1YE5pHL9f-DH9J6bKWS6qQ12WGCBpu9bykXaM92ei2XVCkavhU0eG0BL_TZ814pImywiYOjV9clP5QVcTN3jz95HJHk6Eii4sp7_Jdl59JzHby0YUkUCRxwjuUUC-gcuRx6HPU-jANTCxAeqtJhUEEStqipNS_ZOPaI9sHQoAWdsO408fPug76n5IDSvHWWooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ee7676f0.mp4?token=BbXEeg7W9OYztNq_XCAfIubybvxzohYzlTysHao0FsRHngikvAbPmphOQUWfyQ6UdIKzZ4QpYTpOxp_s5mg_tjtBqTvjgAnt2z449hFuhlZtxtfZe2ystiHy02syadtlDQdTzz-pe-LVFc7RZBjN1YE5pHL9f-DH9J6bKWS6qQ12WGCBpu9bykXaM92ei2XVCkavhU0eG0BL_TZ814pImywiYOjV9clP5QVcTN3jz95HJHk6Eii4sp7_Jdl59JzHby0YUkUCRxwjuUUC-gcuRx6HPU-jANTCxAeqtJhUEEStqipNS_ZOPaI9sHQoAWdsO408fPug76n5IDSvHWWooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
انصافا این دوتا دختر ایرانی خیلی خوشکل چالش موزیک جام‌جهانی شکیرا رو رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93918" target="_blank">📅 16:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpkpqooji0tkkL3HwJ-Jvslv4LCH37R9LqCbPtsyAbDVxwRplLZmrbYmwPvY_aAx6KItP6s82-kzRbvkOc6t0ViS6okZWaAKTLxiDJiXbdz3XVJLERjhAJbH1kmR4pje2uUaO6NvHvBZ-wqIX_1ScidgDTCcmC9dcYvJW4VgYlBvHYsTOfOG230la1xXCXb0C01qKXfd4Man-Uy9saJQjGi03Tu8sfcmU2BZvYwfepcPpzsBrej6uv5dxntHG7n5peYJ-Lvs4bpraQPWtcREyx3fNECfse2ofFEVXOEhforgAwJxOlNfs2BZ-2BtEIAfufVsgTHXsPzLNSyY5m8z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
متئو مورتو:
ژابی روحش هم خبردار نبود که کوکوریا فروخته شده، هیچکس تو باشگاه چیزی به اون نگفته بود! وقتی رومانو توییت HERE WE GO زد تازه فهمید که بازیکن تیمش فروخته شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/93916" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871e6d3b20.mp4?token=HhIhSFLrdZIwkTXX9ljQc4Sr7Ji_a7CDVeFV9D0s9oLVhoz56xA_rVXs-gg0rFDwkJ3J_Ns4k7aNeneXEewOsymuDh9OaA-4MkixSm43fou3mWWKdLN8lf73GZkRVbRBLydgZQtraNZbYE4lMNC3kQ-T4PaJJ7wnNK6soNm1IlcoCe3d3R0yVK8-fXVIuMaSOoV6q10Mz4IXSMbSmDq_G5qcE8vttxeTmIcHqPaM3POgy8uZcSbtZxPPAInMsouEeAeqNTsysEI-2cqJzpLaPLJZ4eSdHQI5BmoqWMMnTr8vUCidnRg85Vt8niLhiQOLFXBxzSH2_c_oOE5rkTPOPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871e6d3b20.mp4?token=HhIhSFLrdZIwkTXX9ljQc4Sr7Ji_a7CDVeFV9D0s9oLVhoz56xA_rVXs-gg0rFDwkJ3J_Ns4k7aNeneXEewOsymuDh9OaA-4MkixSm43fou3mWWKdLN8lf73GZkRVbRBLydgZQtraNZbYE4lMNC3kQ-T4PaJJ7wnNK6soNm1IlcoCe3d3R0yVK8-fXVIuMaSOoV6q10Mz4IXSMbSmDq_G5qcE8vttxeTmIcHqPaM3POgy8uZcSbtZxPPAInMsouEeAeqNTsysEI-2cqJzpLaPLJZ4eSdHQI5BmoqWMMnTr8vUCidnRg85Vt8niLhiQOLFXBxzSH2_c_oOE5rkTPOPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تحلیل جواد نکونام از ریدمان قلعه‌نویی مقابل نیوزیلند؛ عادل و جواد جفتشون روی کیری بودن این تیم نیوزیلند تاکید کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93915" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9036c6b9f.mp4?token=pvTR2Ot2iizJB75stkDAZLkzQqmX28QnrhBFfwbR_LUTKZRXfQbRKacxSxu1W9PVwWtDyYL3MbPVjN1hiWrBgxTvLjU5rldHimzejEOeIBTArpUle4N_toAxDfVGvlEgNcTA4KqAL5Av7wsQzvF2xyv_T4KkbXX5c9ModIss0IYIok2JnSIWkr52--uumQUtqOytViK4KR2GpMxwZ_mQErcF-Nv9h-YqIS5m0gZNHOs8uNOxyr4QAtHVMDM6LC7WwNKRJYoca3rlKMsx3lqp6gTER7oQMTcytvVjhO6xzZurg5aWVN4VO2HAZj_XEWhy8uXTpbXppDcppIbV84Gm3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9036c6b9f.mp4?token=pvTR2Ot2iizJB75stkDAZLkzQqmX28QnrhBFfwbR_LUTKZRXfQbRKacxSxu1W9PVwWtDyYL3MbPVjN1hiWrBgxTvLjU5rldHimzejEOeIBTArpUle4N_toAxDfVGvlEgNcTA4KqAL5Av7wsQzvF2xyv_T4KkbXX5c9ModIss0IYIok2JnSIWkr52--uumQUtqOytViK4KR2GpMxwZ_mQErcF-Nv9h-YqIS5m0gZNHOs8uNOxyr4QAtHVMDM6LC7WwNKRJYoca3rlKMsx3lqp6gTER7oQMTcytvVjhO6xzZurg5aWVN4VO2HAZj_XEWhy8uXTpbXppDcppIbV84Gm3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی و تند علیرضا مرزبان مربی سابق سپاهان علیه اعضای تیم‌منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93914" target="_blank">📅 16:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
رئال بابت پرونده نگریرا رسما از بارسا به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/93913" target="_blank">📅 15:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
رئال بابت پرونده نگریرا رسما از بارسا به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93912" target="_blank">📅 15:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc6d87c9a.mp4?token=GV1H9BFtiPwm-dWj4j9JHUEz5Gf5Np4pG7KdICmcMmIas1mkNBo--NA6541El2nbKsSmIQMvwoDrZO0LCFv9OqN2Ndxwhqv7CE7TlTo05PDQfUYILxzQNUKc-FxxpVPXTumcvpAePyqjHrPmrskqTU9crwCrgoywr_FpYn8VQJmzQ-qR_DhxyWQg_iPO-MyprxIGQztTwKQmbFbxZZzm2sf5zgnGdBbDq-J_myZm5fznafFFfnYbFsHrTouEyZgPt04yHQmsQRvfEAurNtZD6DOlVIGIG497s06eBE3FiwVi-J9JRSUIHZIRw5lA0mUsxuPu9N2IYxO-Tj3pK7XcAl-ohZcin-WG7S61B_46nwSxpM5LduiW6xQouEWlzHQE0wttU3Bv-ynHfFNblGTABtZTyIj0HnyAWyxlAHszYIrBw9fenL4PXHusp6eyC7NQf2R_7LD20kGnwFlysPpdW3l96IdAsJay1HTcBf6_JaXzangEwEVNGrszoylM00pJpi1OSXfv03Vuv9WR6H3mEG5n9eB2q2ajPLtyGAsjFx2D0Th0Y4PJ7cnGFnQCd70SzYqVeTE1XUx3uKfwL4XB2HXRhL175YfC6r647DtRmegqZVYLcE9V3JGefZNvxb1UrT4SynbqUsUW8nH6SHuoN4eZsKMFQLoLerHowoYVZhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc6d87c9a.mp4?token=GV1H9BFtiPwm-dWj4j9JHUEz5Gf5Np4pG7KdICmcMmIas1mkNBo--NA6541El2nbKsSmIQMvwoDrZO0LCFv9OqN2Ndxwhqv7CE7TlTo05PDQfUYILxzQNUKc-FxxpVPXTumcvpAePyqjHrPmrskqTU9crwCrgoywr_FpYn8VQJmzQ-qR_DhxyWQg_iPO-MyprxIGQztTwKQmbFbxZZzm2sf5zgnGdBbDq-J_myZm5fznafFFfnYbFsHrTouEyZgPt04yHQmsQRvfEAurNtZD6DOlVIGIG497s06eBE3FiwVi-J9JRSUIHZIRw5lA0mUsxuPu9N2IYxO-Tj3pK7XcAl-ohZcin-WG7S61B_46nwSxpM5LduiW6xQouEWlzHQE0wttU3Bv-ynHfFNblGTABtZTyIj0HnyAWyxlAHszYIrBw9fenL4PXHusp6eyC7NQf2R_7LD20kGnwFlysPpdW3l96IdAsJay1HTcBf6_JaXzangEwEVNGrszoylM00pJpi1OSXfv03Vuv9WR6H3mEG5n9eB2q2ajPLtyGAsjFx2D0Th0Y4PJ7cnGFnQCd70SzYqVeTE1XUx3uKfwL4XB2HXRhL175YfC6r647DtRmegqZVYLcE9V3JGefZNvxb1UrT4SynbqUsUW8nH6SHuoN4eZsKMFQLoLerHowoYVZhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه‌های تند مجتبی‌پوربخش به میثاقی بابت تماس تصویری با خبرنگار حزب‌الله وسط برنامه فوتبالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/93911" target="_blank">📅 15:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui0ZsaeB8a-NwHujIa8eB4BrNrwBIC7dijk3hcRz5U9mzwW5ZofmhDjxw-A-r7NaPEUuXTjEsMbNCmcooJjM7jAS-_yKRLO-nFpBCp8DiNj9AIzxBxucm2RZXOKmai6AYe8GEW9eRP6h9uhHLD7PrSE95cvi8JtrYqO07iDmF-uOBIW3YKSi-wdVjxfcMxK6vT6mU67OBXbzJlGsUJ3tG8iu-nKFqF9I3oyS4Hwqi7-tjmshXpLO7_lnmqYS1mPjOMS8n5k1xOLtb-RTk65cSAZkYm0Yu3JR9bY8Cr9bE5yhk44Y8OgTq-SgbbJ1zZNXqNc2NiJSy4ja2GtNMDg_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قصه خودشو با توپ و چمن نوشت؛ قصه‌ای که سال‌هاست فوتبال برای دنیا تعریفش میکنه.
👑
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93910" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🏆
ترامپ:
وقتی تیم‌های مراکش، الجزایر، تونس و مصر را می‌بینم، از خودم می‌پرسم چرا این کشورهای شمال آفریقا با هم متحد نمی‌شوند و یک تیم بزرگ تشکیل نمی‌دهند؟ اگر این کار را می‌کردند، به‌راحتی قهرمان جهان می‌شدند. این نشان‌دهنده کمبود رهبری است؛ شاید بعد از اینکه کار نجات آمریکا را تمام کردم، برای ریاست آفریقا نامزد شوم تا آنجا هم کلی پیروزی به دست بیاوریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/93909" target="_blank">📅 15:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568815587f.mp4?token=LLWcErIWWGPKPiP5jyJFEqByjcc9wpTlKAykA-nyeWQrCV4hPcMC70vmL8jgJqrlwlf3YQNDAQA9W_TqtnZL5MyR5RNo_KT5B5pYG3iD1Gqq9W6wjblw_kxZySA6gOzWFfZukgivAL0y55PQj6P8TcDH42SSfvidCK9TSe_3kop0TcDKAMRNkLXrOO6ojM6qIgrk0lzH-uTNcKmHa95d36FhRw_2a1NQPqmPmLJ_bKQBKRHgVQEntia7_JJQp6SsKika2QmAyfE9lJ5qqBjDea72V1KCOyDi5I1uOAOMCY-7rDBQscPvvdy0o7-h5g5D54AQCeQnClZMSQKv7DbKUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568815587f.mp4?token=LLWcErIWWGPKPiP5jyJFEqByjcc9wpTlKAykA-nyeWQrCV4hPcMC70vmL8jgJqrlwlf3YQNDAQA9W_TqtnZL5MyR5RNo_KT5B5pYG3iD1Gqq9W6wjblw_kxZySA6gOzWFfZukgivAL0y55PQj6P8TcDH42SSfvidCK9TSe_3kop0TcDKAMRNkLXrOO6ojM6qIgrk0lzH-uTNcKmHa95d36FhRw_2a1NQPqmPmLJ_bKQBKRHgVQEntia7_JJQp6SsKika2QmAyfE9lJ5qqBjDea72V1KCOyDi5I1uOAOMCY-7rDBQscPvvdy0o7-h5g5D54AQCeQnClZMSQKv7DbKUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
خوانندگی بدل‌اندی در کنار رونالدو و سوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93908" target="_blank">📅 15:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8d4vYdaqJPSC1wJQgUTbTPCkLWcuvcQbfxZQ_9dumnPm4lI8SEfG60-N0HoY09RmQVrrdPUv3nVtaZRU-vOeAe1RhSbExvx7H9QXmHRnPE_VX-yXzR0jWKUyU0gYOm4KaUSoD8yU-W7pxX2F5elVuHA5dP1seCBopjRk5ALgqYf6ZdkyTE77-STBgtdUFVjHZBNrDjqNUWFk-SGjrKDhdKQvWHzThrpyiK4BRnqFsk7tPmMnQVCas17IeVwBpDGR_5S7dSqpbWt9eo7qFwzRrQfbi4vRnEJ6AoSD3Gsczv3dbbS44FtsIK6CePU867PJdzkTA3wj5OVfExobtjeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین:
هدف ما قهرمانی در جام جهانیه، این موضوع اصلا جای بحث نداره و از روز اول هدف اصلیمون بوده. میدونیم کار خیلی سختیه، اما تو سال‌های اخیر بارها بهش نزدیک شدیم؛ دو فینال یورو، یک نیمه‌نهایی و یک یک‌چهارم نهایی جام جهانی. امسال هم با مربی جدید و چند بازیکن جدید، انگیزه و هیجان زیادی داریم؛ هرچند فشار این تورنمنت همیشه فوق‌العاده بالاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93907" target="_blank">📅 15:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059027f16e.mp4?token=OhUQUoo5WVWNSkVSehlgYj62rGzLylnZvW0Rbc1WHegyo1VFJavYtmyY5ms_5FkpJE3oVT1EVSrLHurZhWll5xzf_fm2x8Cpk5q16DgDfG0ySNatQr6_uuYY6-kEqdTD2ELsF-kRw-3n4nGfc7tfM0KbLTokDjs96nfIeikMR_mJXw9UoB0iJiMpbi13qCWYlrVwQnxbzotOqondjBcaNkyxO0wQ7_SMdrJDOhE5sxde0aYYCEbzX3xdrRg4ciVuNLKIoLmNwSm0FmsAdPzMcHG5HRKPpcFzJGBMeYaC918mSM8K1X3MVSZAHL7yFLQZUJj6SOJNofjqEiY1_DDMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059027f16e.mp4?token=OhUQUoo5WVWNSkVSehlgYj62rGzLylnZvW0Rbc1WHegyo1VFJavYtmyY5ms_5FkpJE3oVT1EVSrLHurZhWll5xzf_fm2x8Cpk5q16DgDfG0ySNatQr6_uuYY6-kEqdTD2ELsF-kRw-3n4nGfc7tfM0KbLTokDjs96nfIeikMR_mJXw9UoB0iJiMpbi13qCWYlrVwQnxbzotOqondjBcaNkyxO0wQ7_SMdrJDOhE5sxde0aYYCEbzX3xdrRg4ciVuNLKIoLmNwSm0FmsAdPzMcHG5HRKPpcFzJGBMeYaC918mSM8K1X3MVSZAHL7yFLQZUJj6SOJNofjqEiY1_DDMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ابوطالب‌حسینی بدل‌اندی رو‌ آورده برنامش سر به سرش میذاره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/93906" target="_blank">📅 15:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93905">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2fuRmXlzzOjGsncA6FnmaAxqc-iD87tS0y2kyCOh5J9bHoFuoGXzP8f4EOgKoczDWKj5pgcOURLAzOerbYMj4HGcSwTv-eBQjrRaAoP3ZnbvZRyI8f64NGHUM65en7CBUN1ylVbneFHqSvL03VgR_2zkJJ8k1qzgHwoEIVx9VZ5T-O6JZBGMBWxUZNKkTjyZxSO2LgLvbtOKGZJai6nw4QRQe1UUUqy0aurM3bMs_jmkvdHX_kV2B9wXIoLRQfNAsmetoVE4MSZhNqz0LPjhHMII1pROpL4ny9QzR60eSs6pJBX7HG-BsZR_N8JZt3LsA7eAYYm9ifhZQ172hqF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
هدف اصلی رئال مادرید، مایکل اولیسه است. مدیران رئال بعد از پایان جام جهانی برای جذب این ستاره اقدام خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93905" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93904">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5799d9a11a.mp4?token=pmKsECnId-IFOdl929d6afHO9Qc3CSNaWdiupz6H2fVf1e68zXJatO7OYFtJhgFk5XjTA2leBKuN3uI6mfaH0sCM4EiaE_Kus9xo7aKFRuJwWd8nzPlzXMwhmb_AeqMbOoR3YnKiWIzaUFGlUBwBg0cyBDZ5Dz-F25jBIf6u26YY8R14wx3QrzzVioPFr_KolAI9k3YFZwqAn5EZr01W2aDMz54DdyCb-jKgUMcX8YlAEyaGXHwhVCoQb7y1rFaAGfa92G6MOWEDWvu8I_g9k7wA76FhXHfeJ1NlHCcU-Hb709M2Sh7P3TBV2ljM4_jtknizw4zX5SzUtDYFlJ2r9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5799d9a11a.mp4?token=pmKsECnId-IFOdl929d6afHO9Qc3CSNaWdiupz6H2fVf1e68zXJatO7OYFtJhgFk5XjTA2leBKuN3uI6mfaH0sCM4EiaE_Kus9xo7aKFRuJwWd8nzPlzXMwhmb_AeqMbOoR3YnKiWIzaUFGlUBwBg0cyBDZ5Dz-F25jBIf6u26YY8R14wx3QrzzVioPFr_KolAI9k3YFZwqAn5EZr01W2aDMz54DdyCb-jKgUMcX8YlAEyaGXHwhVCoQb7y1rFaAGfa92G6MOWEDWvu8I_g9k7wA76FhXHfeJ1NlHCcU-Hb709M2Sh7P3TBV2ljM4_jtknizw4zX5SzUtDYFlJ2r9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شوخی خداداد و خیابانی با مجید جلالی و داستان ساعت رولکس معروف قلعه‌نویی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93904" target="_blank">📅 14:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99108c1877.mp4?token=Th2xC7A9GULIyQdMT10DyIQR1HNixrdoxnAeTVhCLj8s_R2p8C9FNavKFPknwPKwBawzkX489z-Q8JJHnIIrIhf5wanBV8-mVA5JUvofVzCyEO9b05eUltWi9IgLPqRF_pmxTbJylVQUtsbHWnzD09pDWQ-PSj3iVls7Bs5m5Mrxcih3bNQO0Epe5Hwa_yBGPQb0F9BatoIPVFvuErVflAmnlPkH4qXlPYj5a4Iio-rAHSSnqxmqk-j0HO9VrNwEXNBpCTtDlVkBvbraLgbWsizginpt3_eAejrvLIhnLAw2l_9BY00SrSkN9dTaJiP53yBSg5tqeGn-Kmrfujc_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99108c1877.mp4?token=Th2xC7A9GULIyQdMT10DyIQR1HNixrdoxnAeTVhCLj8s_R2p8C9FNavKFPknwPKwBawzkX489z-Q8JJHnIIrIhf5wanBV8-mVA5JUvofVzCyEO9b05eUltWi9IgLPqRF_pmxTbJylVQUtsbHWnzD09pDWQ-PSj3iVls7Bs5m5Mrxcih3bNQO0Epe5Hwa_yBGPQb0F9BatoIPVFvuErVflAmnlPkH4qXlPYj5a4Iio-rAHSSnqxmqk-j0HO9VrNwEXNBpCTtDlVkBvbraLgbWsizginpt3_eAejrvLIhnLAw2l_9BY00SrSkN9dTaJiP53yBSg5tqeGn-Kmrfujc_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تاکید مجید جلالی روی موضوع بهتر بودن قلعه‌نویی از ژوزه‌مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93903" target="_blank">📅 14:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba9c2b70c.mp4?token=jNJajgSFoy18XnUz8lE9PqbLOayh6GkLZeYWhgTfVBOz1K1jyI_z6XTiHyliBqf0Tv2OrFVr1PrO2nImG5kfvO1h_gr94q2MVRM4sBBW4QlbrldcoqPN3BLGSBL6Hc8-5Yaign05JCNvxJ63TJTo5diEW_vXQqEoywGaqeI6uZpwJZjvWfRusHCjBqTKrNlqy7BRbbfDKcucIUzMfoykVJsbgEFC4YuCdHrc4ZeExQ5WPT1nVmEPSMZj6uKPL-MwJ5z-gRVyAtUP8GofmGjeXKVpu5xt5JtNVbseCXsuGlaWMUTHOGbqWHmmf09rKEQ1SfLh8-uHrE6NDDYm7g50jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba9c2b70c.mp4?token=jNJajgSFoy18XnUz8lE9PqbLOayh6GkLZeYWhgTfVBOz1K1jyI_z6XTiHyliBqf0Tv2OrFVr1PrO2nImG5kfvO1h_gr94q2MVRM4sBBW4QlbrldcoqPN3BLGSBL6Hc8-5Yaign05JCNvxJ63TJTo5diEW_vXQqEoywGaqeI6uZpwJZjvWfRusHCjBqTKrNlqy7BRbbfDKcucIUzMfoykVJsbgEFC4YuCdHrc4ZeExQ5WPT1nVmEPSMZj6uKPL-MwJ5z-gRVyAtUP8GofmGjeXKVpu5xt5JtNVbseCXsuGlaWMUTHOGbqWHmmf09rKEQ1SfLh8-uHrE6NDDYm7g50jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇧🇩
شادی پشم‌ریزون مردم بنگلادش از گلزنی و درخشش فوق‌العاده لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/93902" target="_blank">📅 14:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5wekczXM-Xt00jEceOvfbhaNovJGW7tuzbGR2hgmpod8Dug0styBmPa9DcfnnCRm-9y-Gnj2UmeC9r-Vr0hniIeI_tbDoLkb08CiQY0e2RMKdVvGCkjiHQ1AtzOJX_-qkMbO5GdarnNwIcIBQX9470lR2FdTjWMPHm7YbNcoDsNCPMS0gINhwlfMh7mPJ9KGIsU0pVYrz9MuXwuf-IkcpoHapJ800p5GjWTAn_Kzl-fNyzHz0uIqCCM58p_XsoSVT9z94Z41dTtFJciMNhJTnrjzXieKk5nMjuyUwiMcr34ro0N5iRhypmRdN7U2v-zx_2ojdVjMQtZ5cj4-ddYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
؛ رئال‌مادرید طی ساعات آینده اولین پیشنهاد خودشو برای جذب باستونی به اینتر ارائه میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/93901" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgDjQTVGgiVjG1BugU10fp8Z12IhuJV4gazUBbc1T5hkkCUkHD8Z9ObHdEBD17RpcW3sxH9oU5AITmQLvBubWs_eRHPyiVDRpWStYt_uWXG8fhkp94Cso-D5fPMIYL6Gd5-7e5HTKi5hjVqEgzDglwJ2BpXgP5PX1T8YHdt_wQueCc8_zv9vVcqEpgE1Lyn435lpMoafZw2NaqaFEGntsqNFrbDMkO9HFBhAuw7JJbE6WtQKk5n98jdo8xTAtVTxjSeeyh4uJFTvj2Kwgs8RTYZ9aTaXM175rFMs5a9ON3eekod2RVSdUdbYaG0mb5IJ-WCkL9BgxvU9jmabfeTKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه کریستیانو رونالدو امشب گل بزنه، به اولین بازیکن تاریخ جام جهانی تبدیل میشه که در ۶ دوره مختلف این رقابت‌ها گلزنی کرده.
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/93900" target="_blank">📅 13:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93899">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7feb575370.mp4?token=fRgV3HsXXr4bMpe25KTdINORX5-5HEpgWIa8KGpqOKYwZhKD9qRSO7y-E8C8Af1Z89EuowdoCHQABXn-t2tXG286oOoLmlM0YztI2tLrmQe40axlE51Jl4tCv1MuL239hvbdWeYtpSL4jXl7uOj1kAM3CJG4ZuZES7Ew_MnamfaL1nyjnJ2xhR4jGN2sWlCf9V7lctS7QMchR3ncnzv03lJm_dDRvUN8V-S_1hSCzD-tTL0LgMQfJqovK9ELPwdcCKdRpKGZrrZ2o9j9-sAXgyfDRHt_CAOW-xdyLk3UFB71gUGtnsrxQA3WJKQN7la2BRHKW7FP-5ZS1NthynT-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7feb575370.mp4?token=fRgV3HsXXr4bMpe25KTdINORX5-5HEpgWIa8KGpqOKYwZhKD9qRSO7y-E8C8Af1Z89EuowdoCHQABXn-t2tXG286oOoLmlM0YztI2tLrmQe40axlE51Jl4tCv1MuL239hvbdWeYtpSL4jXl7uOj1kAM3CJG4ZuZES7Ew_MnamfaL1nyjnJ2xhR4jGN2sWlCf9V7lctS7QMchR3ncnzv03lJm_dDRvUN8V-S_1hSCzD-tTL0LgMQfJqovK9ELPwdcCKdRpKGZrrZ2o9j9-sAXgyfDRHt_CAOW-xdyLk3UFB71gUGtnsrxQA3WJKQN7la2BRHKW7FP-5ZS1NthynT-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت تیم‌منتخب ایران در جام‌جهانی ۲۰۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/93899" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93898">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHfiMr0gAOFT6BWixbiKovovTJp3y5_6c5pz-8UYBPDKRr5PlcfBm1IOgfhN6P2dmtgGIZZ03So1x6_1UYkUqiSO2mdjN8VisQUImY6DrgBltyRWeLzXQDAdaD6QZBoRt00AjwrSAQpNeoBKNCIaEF3zDBsiLcw-5K7_H2stgpltenCjoauAWVs1S8H0y4Hkdo-yYyIE5PgfoOPyXApDkdmQJCEzWkmEXPUA4E3DbuJgabsA8gB1kj5c02CEX8ERYGwnletugxMDWdyOhqqyJMprRP7x9l_pmUktIKiTaOv2C9m1VElH0Kkgcs9XYR6tptny_DTf-AGUyguYurlB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید بانو وندا با کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/93898" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3wih7bXtCKisnDgk5efkUuZ_Gqb1JqLqYPJ-SI51pB6OY2BrTHnQYnAJN_qg0uoG9HnEe8X6zfkAoDokYQZrRNp5ZGGxsBIBD9QmtmiNR5I3QMgj6w0zc5xrC2R3LWXQ7G1k-ZW5GNEt4b0Mz0iu-OlH7HACI2R_-S363qCP-qFAlgcEi8uO7_39g0pr-96Bm2uzS5pMu7lMNswtVCTB59oY3NhR-hZ0DcOIM0lKkYnoxgJfdMFw-p2M6ahn5pK7qhv15ZH6sAFa_FLpZMD83uXGFLg_eEUSj5p_PnPQGF8oXsW4zkuo8R0ozojWqYBDVinNQqg5qHtlpV7dDICyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
رئیس اتلتیکومادرید: به‌نظرم فصل بعدی خولیان آلوارز بازیکن تیم ما خواهد ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93897" target="_blank">📅 13:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bb140549.mp4?token=sKxUmcfj_sBw4unBUD41MtBgsvsSlDgkzRYskiONbbqYEbXyX8DEWkrIvQNcXgUIt2kfBOTRsRXX3WBNFYG1NwSyptioPP3x6-zZqG_3q0slZPOirieaUehc8J5As7Fer6tRRwyHPaZ_maWyj3VIdn9Uj73ADefqkICr75qZC2ZhMTZbb9tKFCdkDYM6_qOSmTUIxQ6rrDtBwUam1Wum9Cgb66PYWv-qT4lSHBdUMpVjtXwvT3sUAsNTHibDFJZxRMbcM3GZmHy8MyjLpXlm2g1YwFTffjE408UpPiIhv5KBDD93L6eP4_rev73mL3uB9Ha3idvJNA7EDSxt3oYQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bb140549.mp4?token=sKxUmcfj_sBw4unBUD41MtBgsvsSlDgkzRYskiONbbqYEbXyX8DEWkrIvQNcXgUIt2kfBOTRsRXX3WBNFYG1NwSyptioPP3x6-zZqG_3q0slZPOirieaUehc8J5As7Fer6tRRwyHPaZ_maWyj3VIdn9Uj73ADefqkICr75qZC2ZhMTZbb9tKFCdkDYM6_qOSmTUIxQ6rrDtBwUam1Wum9Cgb66PYWv-qT4lSHBdUMpVjtXwvT3sUAsNTHibDFJZxRMbcM3GZmHy8MyjLpXlm2g1YwFTffjE408UpPiIhv5KBDD93L6eP4_rev73mL3uB9Ha3idvJNA7EDSxt3oYQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
بدل رونالدو:
این‌طوری نیست که من بدل رونالدو باشم چون اون خودشو شبیه من کرده نه من شبیه اون؛ رونالدو صد تا عمل جراحی کرده ولی من نچرالم
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93896" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=uFckn2O9W45TcDyDWT9HDTrJ7oBEmZXd4Wz84HBd3P8uNCVSkmfODzOsDWR3PEMz5dYvHgYFwgtA4uGzie327B88oUrroCcOSaR4aKukh81V7JNxLCX8ixyjmpUPttfaUj-nMt2BUfcM8S1u-YyhJwYWUpBy7uB-gQ1OB50Vf4VJzzH88lpEBoLEZFR5LQ_lWLl7WLjN6y2H2EjcZ3KSbHZtYqha-RTrmSfn9MC_hGJ2HX43-B7dSBWxvgucOLApaU1AYYbnJwzGxP5MECozUJhWA8LDj_qwUb1BcMs_ZjxCSeHQcrYL3zOZYc8x-OqH6XZs55iL1reE3y7_4-gx5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=uFckn2O9W45TcDyDWT9HDTrJ7oBEmZXd4Wz84HBd3P8uNCVSkmfODzOsDWR3PEMz5dYvHgYFwgtA4uGzie327B88oUrroCcOSaR4aKukh81V7JNxLCX8ixyjmpUPttfaUj-nMt2BUfcM8S1u-YyhJwYWUpBy7uB-gQ1OB50Vf4VJzzH88lpEBoLEZFR5LQ_lWLl7WLjN6y2H2EjcZ3KSbHZtYqha-RTrmSfn9MC_hGJ2HX43-B7dSBWxvgucOLApaU1AYYbnJwzGxP5MECozUJhWA8LDj_qwUb1BcMs_ZjxCSeHQcrYL3zOZYc8x-OqH6XZs55iL1reE3y7_4-gx5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93895" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏆
🇪🇬
ویدیو وایرال‌شده زیبا از مربی مصر درحال توزیع آب میان هواداران داخل استادیوم. بنده خدا از آذوقه بازیکنا به تماشاگرا داد تا گرما زده نشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93894" target="_blank">📅 13:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=X5B_6l97SFawUf02gLYVnlJWY1wQ3py801mvxW1vBREsS17xMqOpi7QeXoBA3kWe5K2E2zkFjYLihxdqGR8GUJJfHRqmIZNoRdGow83Watx9yrIhXTFF_-a-SVSPG80Ucz2CI_sozJRakNvEX07msd2ALrAnw67WG1V4wpkqLLHGRGI84yDf00CGvfamxfBNxT7L_6hzAV-Xe1SkoVqdMtRLs4k3FJgjFpKw8DoAm4v_jkNiLSJ5dXlceaRFyRtGmv__Q_dzI7cGz0S5af1vhMm45QaeF-aEjolmD-Sa_5Q1Y9ArHDoIltf8rh2CNct1Zv577tbyCwJr6LPm4Ka3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab3ff261.mp4?token=X5B_6l97SFawUf02gLYVnlJWY1wQ3py801mvxW1vBREsS17xMqOpi7QeXoBA3kWe5K2E2zkFjYLihxdqGR8GUJJfHRqmIZNoRdGow83Watx9yrIhXTFF_-a-SVSPG80Ucz2CI_sozJRakNvEX07msd2ALrAnw67WG1V4wpkqLLHGRGI84yDf00CGvfamxfBNxT7L_6hzAV-Xe1SkoVqdMtRLs4k3FJgjFpKw8DoAm4v_jkNiLSJ5dXlceaRFyRtGmv__Q_dzI7cGz0S5af1vhMm45QaeF-aEjolmD-Sa_5Q1Y9ArHDoIltf8rh2CNct1Zv577tbyCwJr6LPm4Ka3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
نظر دین‌هویسن ستاره رئال‌مادرید درباره کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93893" target="_blank">📅 13:00 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
