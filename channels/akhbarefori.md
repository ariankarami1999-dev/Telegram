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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.53M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-659684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تیراندازی به کشتی باری در نزدیکی یمن
🔹
موسسه UKMTO از حادثه‌ای در ۱۴ مایل دریایی جنوب سواحل یمن خبر داد؛ یک قایق کوچک به یک کشتی کانتینربر نزدیک شد، به آن تیراندازی کرد و قصد ورود به کشتی را داشت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/akhbarefori/659684" target="_blank">📅 12:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای رژیم صهیونیستی به شهرک زوطر، مرکبا و شهر الخیام خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/659681" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c37af42.mp4?token=CTmPWzKNnr0CWfLr5Ctwxp-gAuyCiSy-dIRGlIHxEkUj9X1SiUIy8y3E4MGoR4z_38D57JrZJO0CxmzgEs8M792NrKi_1Lj-1NfjVPj43FmEcPfMKgunTy3R4vUBkLifoQbVsmwIXepfsVcr1sL6JLrro1l8HsnIpyr9XFobruheeIwJmuzG22EDMMrRzp6hSPwVJ4SEKQI4s29xxJtE1W4Hu3x_vZU8cVBn1wCLRvr9duHQ30IYiD_lPjlHUtWfb3TLrEDNKkOM7zbj7HfCfsb-ytKkpn-Tb7ObZtm9K2POM1n-noG42wd80L6Iwk152qO_JoAWndCcLrCVeDutBhxR8iAJW0eeXJL1W3VWQlobpfhLsneIibldtlFyR1g0Wrd6dZrPRm24BDYWzgF_xU3Sfzm52CEZuGC9oPNV7Tq-NuahgbxC55g0bWHPIvFOKXzK3Z4u36i7qNtiPVelPlHU4HJX1OC7g_41bagS3kYylXqMSq9gt0yBoc_Tq8DvFedhVjoBedu4Zf40ws_Iq5qOndmrkK_n0nhdFRQGs7shMo-pxhWMHDgZoPuW035K7kp4Q09Tg9Y7EFl82o8GDPV0GRba_a034h62jOSP1vw5VG9HaJtS2TLY9lE1FKHqaeFBFHoveOM2xP9qinmHMRxAtlbfPtlyAdzh-UYqsEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c37af42.mp4?token=CTmPWzKNnr0CWfLr5Ctwxp-gAuyCiSy-dIRGlIHxEkUj9X1SiUIy8y3E4MGoR4z_38D57JrZJO0CxmzgEs8M792NrKi_1Lj-1NfjVPj43FmEcPfMKgunTy3R4vUBkLifoQbVsmwIXepfsVcr1sL6JLrro1l8HsnIpyr9XFobruheeIwJmuzG22EDMMrRzp6hSPwVJ4SEKQI4s29xxJtE1W4Hu3x_vZU8cVBn1wCLRvr9duHQ30IYiD_lPjlHUtWfb3TLrEDNKkOM7zbj7HfCfsb-ytKkpn-Tb7ObZtm9K2POM1n-noG42wd80L6Iwk152qO_JoAWndCcLrCVeDutBhxR8iAJW0eeXJL1W3VWQlobpfhLsneIibldtlFyR1g0Wrd6dZrPRm24BDYWzgF_xU3Sfzm52CEZuGC9oPNV7Tq-NuahgbxC55g0bWHPIvFOKXzK3Z4u36i7qNtiPVelPlHU4HJX1OC7g_41bagS3kYylXqMSq9gt0yBoc_Tq8DvFedhVjoBedu4Zf40ws_Iq5qOndmrkK_n0nhdFRQGs7shMo-pxhWMHDgZoPuW035K7kp4Q09Tg9Y7EFl82o8GDPV0GRba_a034h62jOSP1vw5VG9HaJtS2TLY9lE1FKHqaeFBFHoveOM2xP9qinmHMRxAtlbfPtlyAdzh-UYqsEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان عجیب نیوزلند؛ بدون برد، بدون شکست!
🔹
حریف فردای ایران در جام‌جهانی کاملا غیر پیش‌بینی است. این تیم شاید یکی از عجیب‌ترین تیم‌های این جام باشد.
🔹
یک تیم گمنام اما اثرگذار ... حریف اول ایران را در این ویدئو بشناسید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/659680" target="_blank">📅 12:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659678">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a227b50007.mp4?token=OhivApMOS12oTWHKWR2legNwusWSHQV_8yvGssL1VXtbf9LzBO0xwnWeDU9na63qfgZ3RlO45BKMtgd0uFgMY7AMTexHp4HPi46fy73leUcJiGZsq2QqrApeODuysWXFfhX-kt2oA9xMfLPi03SZ8NbVh2JH4hg9K-CaMQ8TlPm0L5KZ2GvisJILVpuDKqx5kp8l01z2wWMQAjtre9HNJtY4GYAGVYOhApy3AUToZyhLJgFHPJiJApap3cLaDGqAg6TlWUGBJQErPSisSdMf-xNSn-9DNLydEWYz1sGlpenOqVcKFOsAtgeCf7mpxO388fyCAttE7CI3ttICpFHZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a227b50007.mp4?token=OhivApMOS12oTWHKWR2legNwusWSHQV_8yvGssL1VXtbf9LzBO0xwnWeDU9na63qfgZ3RlO45BKMtgd0uFgMY7AMTexHp4HPi46fy73leUcJiGZsq2QqrApeODuysWXFfhX-kt2oA9xMfLPi03SZ8NbVh2JH4hg9K-CaMQ8TlPm0L5KZ2GvisJILVpuDKqx5kp8l01z2wWMQAjtre9HNJtY4GYAGVYOhApy3AUToZyhLJgFHPJiJApap3cLaDGqAg6TlWUGBJQErPSisSdMf-xNSn-9DNLydEWYz1sGlpenOqVcKFOsAtgeCf7mpxO388fyCAttE7CI3ttICpFHZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ کشته براثر سقوط هواپیمای نیروی هوایی پاکستان
🔹
دو خلبان در اثر سقوط یک هواپیمای آموزشی نیروی هوایی در میرانشاه پاکستان کشته شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/659678" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659677">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e6a6c7d3.mp4?token=KaO9rDdQVp1W5smpFFTXdYl7OkGrJTmZp2cuL8lCLuffLq6at5rF6ydTlzFrEamkM2O-OMeC9r7aPG-xwLmaNZhatIHsAy51cYGF1RCkaMIJ-auQAm47LIxm44epSJVa6_kqZMdFdu2frQ2aW2MDiWIQIRpcdDGLU_jka3DataA3f8LBRpfGmLNAaespEB4cx0w3Ldf8sjobJje_W6FNP8A7J3vdL7AgV1JTM5wJUzHJ2mVWj2z6qsg7Uz8SNwurHNiOE0wVlZgrH_VkkclWalRieSsyxhIFLlk6oRNkadWwGCimAOfjzFMR8dLXsS5pFe-FK_PcF2dkWk8shFy4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e6a6c7d3.mp4?token=KaO9rDdQVp1W5smpFFTXdYl7OkGrJTmZp2cuL8lCLuffLq6at5rF6ydTlzFrEamkM2O-OMeC9r7aPG-xwLmaNZhatIHsAy51cYGF1RCkaMIJ-auQAm47LIxm44epSJVa6_kqZMdFdu2frQ2aW2MDiWIQIRpcdDGLU_jka3DataA3f8LBRpfGmLNAaespEB4cx0w3Ldf8sjobJje_W6FNP8A7J3vdL7AgV1JTM5wJUzHJ2mVWj2z6qsg7Uz8SNwurHNiOE0wVlZgrH_VkkclWalRieSsyxhIFLlk6oRNkadWwGCimAOfjzFMR8dLXsS5pFe-FK_PcF2dkWk8shFy4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم امیرالمومنین(ع) سیاه‌پوش عزای ماه محرم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/659677" target="_blank">📅 12:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maP9wXDK2O2C7uslZWesuFGHaOZKvQ7UcoX_h4S-MVvjwH4a3Hngut8LeQq_l1Eyl_CcL8wx5X8t6NkS8vDAk3WsUqF23ztUYwnTylQ1QjSUxoCIUmO8sCOV3CjMX_xXQXduXSuIMgK_ch6g5MPZ1L4hmbngrFvIAx9z0H4aBP76PiYy1qoKwKpYZo67wXQfN4JpS3jaS89JPBH6WMJ9VBteTv31Pq05KFUF4bcmgjaaoxaiWwn8VF-u4nfZmUORC_w3zAd92pr52dXgc-wcNygsHptoWDyt4ysKEEdrZtC550xZbUbX_vNU-C2xQ-xJGeH_B0ychqGVqdm6r5w3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تابستان شاید شب‌ها برق نداشته باشد!
🔹
جدیدترین برآوردها از صنعت برق نشان می‌دهد ناترازی پیک تابستان به ۱۳.۶ هزار مگاوات می‌رسد. این رقم نسبت به سال گذشته ۱.۱ هزار مگاوات بهتر شده است.
🔹
به دلیل ماهیت تولید نیروگاه‌های خورشیدی، در صورت عدم مدیریت بار، ممکن است کسری برق در شب نسبت به سال‌های قبل بیشتر شود. در بیش از ۸۲ درصد ساعات، ناترازی واقعی زیر ۱۰ هزار مگاوات است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659676" target="_blank">📅 11:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659675">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
لحظه‌ای که امدادگر برگه سونوگرافی مادر بارداری را پیدا می کند که در جنگ اخیر به شهادت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659675" target="_blank">📅 11:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659674">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سکوت نتانیاهو سؤال برانگیز شد
شبکه ۱۲ اسرائیل:
🔹
از زمان اعلام توافق میان آمریکا و ایران بیش از ۱۰ ساعت می‌گذرد، اما نتانیاهو همچنان سکوت کرده و اظهار نظری نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659674" target="_blank">📅 11:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659673">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI0L5q-yWDrarrKlD10pmulb1TeaXmXzWuJ6jOOULGelvTlpu1RjswNDG_OGoV6sXbmrNa6tJWaLo4tw4qNNUdbxpCq5bkWobIY7FE4Ic8FYQ6bl961p9fRAm5vvG5gR5k58FUmRVdkjaVkACcowFdbmSFMUEfZkJGVUy5sVOGoQXPawt8OWrlsa7sGZE4V0DufzOmnwFhBJJ_Guk8B_OKEmkTU7qXy-EnR38icRVqLs9WkptHAHQG6ALizwMzyXOUmOJMxlpn5OWak4i3GUHUhATcdNUzcR6nhcQltsncREbn9gCHvx3yDHpesMrOO6OkQVSZXffjLQobHnd6LFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه آمریکایی‌ها به عملکرد اقتصادی ترامپ
🔹
۵۲ درصد آمریکایی‌ها معتقدند وضعیت اقتصادی در دوران ترامپ بدتر شده، در حالی که ۲۸ درصد از بهبود شرایط سخن گفته‌اند.
🔹
در میان جمهوری‌خواهان، ۵۷ درصد اقتصاد را بهتر ارزیابی کرده‌اند و تنها ۱۸ درصد نظر منفی داشته‌اند.
🔹
۸۵ درصد دموکرات‌ها معتقدند وضعیت اقتصادی بدتر شده و فقط ۳ درصد آن را بهتر از قبل می‌دانند.
@amarfact</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659673" target="_blank">📅 11:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659672">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
الجزیره: شهباز شریف شخصاً در مراسم امضای توافق شرکت خواهد کرد
یک منبع در دفتر نخست‌وزیری پاکستان:
🔹
نخست‌وزیر شهباز شریف شخصاً در مراسم امضای یک توافق صلح در سوئیس، روز جمعه آینده شرکت خواهد کرد.
🔹
یک هیئت عالی‌رتبه نیز شهباز شریف را در سفرش به ژنو همراهی خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/659672" target="_blank">📅 11:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d02bab77.mp4?token=a-fXXSTcuj7xqzuJsnTemReqlH5LOXY9xGYbt2nFMKwcN-XESE1umN_9l7meBmFdMVxSEVn4zhi1k6FMzwsozj4MUvxkyAWVaKms9-OprZ7pc910XeKToZrlWDCi0uR0uaqg-QRDgpHdxXarOeaoOkAsPeGyf4bHNYdYyS82f0Sl83fNgVUIKkbSqZgFYyuxaqU6dcgQJUKNw5tVwTMEFCn8xZ_Hypl4gk8DPdM3zSCyALvqCpI63qHpmhWrz2CmCsumXH646RaXSXLr7KQ3rxJzU9VgsuVPoGbnI19uJCeWHOBaZUskFlPGIF5VEmZI94EMKK6iR5nsOmtKKbi_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d02bab77.mp4?token=a-fXXSTcuj7xqzuJsnTemReqlH5LOXY9xGYbt2nFMKwcN-XESE1umN_9l7meBmFdMVxSEVn4zhi1k6FMzwsozj4MUvxkyAWVaKms9-OprZ7pc910XeKToZrlWDCi0uR0uaqg-QRDgpHdxXarOeaoOkAsPeGyf4bHNYdYyS82f0Sl83fNgVUIKkbSqZgFYyuxaqU6dcgQJUKNw5tVwTMEFCn8xZ_Hypl4gk8DPdM3zSCyALvqCpI63qHpmhWrz2CmCsumXH646RaXSXLr7KQ3rxJzU9VgsuVPoGbnI19uJCeWHOBaZUskFlPGIF5VEmZI94EMKK6iR5nsOmtKKbi_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویربرداری از ضریح مطهر امام رضا (ع) از زوایای مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659671" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
واکنش دموکرات‌ها به توافق ایران و آمریکا
🔹
ست مولتون، نماینده کنگره: «مفاد این تفاهم‌نامه «اساساً یک سند تسلیم از سوی دونالد ترامپ به رهبر ایران» است.
🔹
گرگوری میکس، دموکرات ارشد کمیته امور خارجی مجلس نمایندگان: این دولت با این جنگ غیرمجاز ما را به سمت جنگی پرهزینه سوق داد.
🔹
رابرت مالی، مذاکره‌کننده ارشد برجام در دوران اوباما: اما این تفاهم‌نامه همچنین کیفرخواستی روشن و قاطع از جنگی است که پیش از آن رخ داده است، عمدتاً به این دلیل که دستاورد اصلی آن بازگشایی آبراهی است که فقط به دلیل آن جنگ بسته شده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659670" target="_blank">📅 11:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: دوحه، میزبان مذاکرات مقدماتی ایران و آمریکا
خبرگزاری فرانسه به نقل از یک منبع دیپلماتیک ادعا کرد:
🔹
دو کشور ایران و آمریکا پیش از امضای توافق، مذاکراتی مقدماتی را در دوحه قطر برگزار می‌کنند.
🔹
هنوز جزئیات بیشتری درباره سطح مقامات حاضر در این مذاکرات یا دستور کار دقیق آن منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/659669" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed890cb68.mp4?token=EtgklUCrmZhefLhDNN50V2ekQ_ka7aizpWUcK7d4Pe2tOmvlCpCWBd3XJcSZ2wVEwlWeqe1YbSJmoebEXh7ifjEj4bg9tvxCC4cZKmpD6afZ4XgBh-DcM3zQePhO7ok0O3epP-vDt6iNAcnStvAZWJTqGLjl8KPDzu4nY3GCmlQQvYxodfgjdp_uKRKJdIsGpYXCtXoVU-SoG3A3DJjiUs1FBE4gbdFEKqK5SV1xVFbM0jzLhoWR1HvsVrTn9d5d5S32kakJ8ucsjeqDQxz0Yhdk-rRjB-CM5Is_cWv7TWTk37J6i9LSCODc-kBl4Y3akoizitxIHlMbVLwiRHeRU0gs-ZcJJLoFWybILMu7EQ49cbxQX2VClWon99o19CGOAM149fm8QoE01XPTOU-rTwZVBTF0wGbpnhCac4Z56V1esW6RiL0UVHf0q0geRlI_MC883nZdkCbKwWrpsaVxQn5bEHBsw9PgUVAU7k_uPXOU5KYldHKVNkSyt4MBsYZdaYW3qBrpzym7jbRrJ_-yhRk2ZI7Gwn1BbaCiKk6UDfsAKApi0j-wm6OT9wwijnQeMsICGe_m4OtFr61aKp1Vx98-uT1cIowplsdj6CmTDTiRkKsEVbT2x_e13FH0BxcPHMMbroMfNedRD6Y7iep2HbodB2fC4qebc9SA6jhkNxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed890cb68.mp4?token=EtgklUCrmZhefLhDNN50V2ekQ_ka7aizpWUcK7d4Pe2tOmvlCpCWBd3XJcSZ2wVEwlWeqe1YbSJmoebEXh7ifjEj4bg9tvxCC4cZKmpD6afZ4XgBh-DcM3zQePhO7ok0O3epP-vDt6iNAcnStvAZWJTqGLjl8KPDzu4nY3GCmlQQvYxodfgjdp_uKRKJdIsGpYXCtXoVU-SoG3A3DJjiUs1FBE4gbdFEKqK5SV1xVFbM0jzLhoWR1HvsVrTn9d5d5S32kakJ8ucsjeqDQxz0Yhdk-rRjB-CM5Is_cWv7TWTk37J6i9LSCODc-kBl4Y3akoizitxIHlMbVLwiRHeRU0gs-ZcJJLoFWybILMu7EQ49cbxQX2VClWon99o19CGOAM149fm8QoE01XPTOU-rTwZVBTF0wGbpnhCac4Z56V1esW6RiL0UVHf0q0geRlI_MC883nZdkCbKwWrpsaVxQn5bEHBsw9PgUVAU7k_uPXOU5KYldHKVNkSyt4MBsYZdaYW3qBrpzym7jbRrJ_-yhRk2ZI7Gwn1BbaCiKk6UDfsAKApi0j-wm6OT9wwijnQeMsICGe_m4OtFr61aKp1Vx98-uT1cIowplsdj6CmTDTiRkKsEVbT2x_e13FH0BxcPHMMbroMfNedRD6Y7iep2HbodB2fC4qebc9SA6jhkNxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد برزیل ۲۰۱۴/آلمان ۷-۱ کوراسائو را در هم کوبید
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/659668" target="_blank">📅 11:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راه‌حل نماینده مجلس برای کمبود دارو؛ مردم داروهای اضافه را تحویل بدهند!
علی شیرین‌زاد، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
می‌توان یک درصدی از مشکلات را این گونه مدیریت کرد که مردم به پایگاه، خانه سلامت و بهداشت محله، مسجد و...یا نقطه ای که در شهر مشخص شده است، مراجعه کنند و داروی مازاد در خانه را تحویل بدهند.
🔹
بلافاصله بعد از جنگ با کمبود و گرانی چند برابری دارو مواجه شدیم. برخی از  داروهای پیش پا افتاده برای سرماخوردگی، آنتی‌بیوتیک‌ها در بازار کمیاب شد و مردم دچار مشکلات عدیده‌ای شدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659667" target="_blank">📅 11:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بهروز رضوی درگذشت
🔹
بهروز رضوی ـ از صداهای ماندگار کشورمان ـ به علت بیماری درگذشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/659666" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26019626b2.mp4?token=Ng1oKc1a-nQ7J7kyh9fBeg_lniyqz1mbegnB6JRHWsrUhYVcVzDSujpknmKxgAQR8E1r4HDKCNqXDbX8pwpztaq_XOjyZfNL6jlUgpgUzYZQtZ8r7gDfiklNVKqsC-NtBtCdjmXUT7gTN0V7HVWsfsTwXSB6fJtu0Up5ZMpziTQK5yjWZd33g-S2NBW295lmm3gFVDS3BByjQiwrbQT3CMTmFzayFPBzqdPfhXzt_brf5ojpaeVhX6VL37E1pqXIFSJumAvZLTqZXRNCxtoMQhdCsHssGurT_yxs_vwrJ6k7uhXlbRu_74Hu5VeX_ZbvrG2aqUgEHRQr-LWV656TqlxmKWtXvSbeA5gLu0YxK4Poyu3DERVulgRLJjqrTuZfdpQ2CCvi9qyPKIT-CA2OhzkwdPCVRN6FYZUblUKRM3CwW5T_XM2BYJFAk7c27R0IS_IE3CnlFJwLmspbOi8gJdEL500IQKcZDVGLlgMPImeI6fgSXH-fUyCzX_yj8y2BIP0HNSG4iwS8o33l1Rfl8a65e1D0k8-VvGM0RfpUXXZkBGgUF0MctSnuFhDOVboXswPVcBWq19copKOV_M6-d91gZBw4qIeDSTlxvj52v6IZHdBqYy92qX4IEoBtdNBbzABT2NVH3x4OaRWTbgcB0jOx5_wm_FO8PdUKZjpty7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26019626b2.mp4?token=Ng1oKc1a-nQ7J7kyh9fBeg_lniyqz1mbegnB6JRHWsrUhYVcVzDSujpknmKxgAQR8E1r4HDKCNqXDbX8pwpztaq_XOjyZfNL6jlUgpgUzYZQtZ8r7gDfiklNVKqsC-NtBtCdjmXUT7gTN0V7HVWsfsTwXSB6fJtu0Up5ZMpziTQK5yjWZd33g-S2NBW295lmm3gFVDS3BByjQiwrbQT3CMTmFzayFPBzqdPfhXzt_brf5ojpaeVhX6VL37E1pqXIFSJumAvZLTqZXRNCxtoMQhdCsHssGurT_yxs_vwrJ6k7uhXlbRu_74Hu5VeX_ZbvrG2aqUgEHRQr-LWV656TqlxmKWtXvSbeA5gLu0YxK4Poyu3DERVulgRLJjqrTuZfdpQ2CCvi9qyPKIT-CA2OhzkwdPCVRN6FYZUblUKRM3CwW5T_XM2BYJFAk7c27R0IS_IE3CnlFJwLmspbOi8gJdEL500IQKcZDVGLlgMPImeI6fgSXH-fUyCzX_yj8y2BIP0HNSG4iwS8o33l1Rfl8a65e1D0k8-VvGM0RfpUXXZkBGgUF0MctSnuFhDOVboXswPVcBWq19copKOV_M6-d91gZBw4qIeDSTlxvj52v6IZHdBqYy92qX4IEoBtdNBbzABT2NVH3x4OaRWTbgcB0jOx5_wm_FO8PdUKZjpty7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی هلند و ژاپن که دو تیم به تساوی ۲ بر ۲ رضایت دادند
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/659665" target="_blank">📅 11:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_ANDtoVRClBu30kZjFKyW-_q13-AGTRlJZ-xnQlK9pboc6gXhpYPoTAAGOBWYOMNFOeZIbzis7XRf7-hf5Ce0frUSlKTTFdrHxkjoHXsrE08KRZYKnklKdWI47PyzEJUpLyW8NCO0RoEs1d-IPnveDjYKmS1MJ7Aj5rq9buVkrmqPB6b0s2tvvKGzX06y2nAeb5Vva_FxkWS3NOb4jlNC9OO3oaLjMdjDBSFcjAem776_F2cHizUwJCYgtUnnSScguJS-YiqGIzVZo-c1_16mt8rQ0cNxClYEkhQVBRU16dRBWOo5KtPLpz-zdxe3rRMpQKgtvU9PF1bnTJ4TeG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از سایه خودتم باید بترسی...
You should fear even your own shadow
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/659664" target="_blank">📅 11:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb903a030.mp4?token=YI_lJFWvVkOrbmGNzBcbZyIV4HcBk0qSYLAAWv5HqBgOsMdYnFak8EG-LEDaj1gnuhr3m01pHN5rxFoMbZVN1xQ8zyOFfZmYUcQWxGEeLS3hiUeMmSvlZkmbVGh-0fYbpkeE7yK_f2qI7UyaXkDf5S3xxNzV26fuQQk38RZaXzqxXxri2a0hZnQLXzNaB5qotMah5gAQxw6l-UCGZxytgvYgtCy7jOUC3BsUbbMzKTYbQt4Y2oJWTGu8UywuyYypONj6UmtUg7-8TFDH1s9f4mntwzePpCHsDsKFKCCaGL1PDg69hxrWYSUY5Sqqs5o5fkLruQAMkfGv0kbhII6UmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb903a030.mp4?token=YI_lJFWvVkOrbmGNzBcbZyIV4HcBk0qSYLAAWv5HqBgOsMdYnFak8EG-LEDaj1gnuhr3m01pHN5rxFoMbZVN1xQ8zyOFfZmYUcQWxGEeLS3hiUeMmSvlZkmbVGh-0fYbpkeE7yK_f2qI7UyaXkDf5S3xxNzV26fuQQk38RZaXzqxXxri2a0hZnQLXzNaB5qotMah5gAQxw6l-UCGZxytgvYgtCy7jOUC3BsUbbMzKTYbQt4Y2oJWTGu8UywuyYypONj6UmtUg7-8TFDH1s9f4mntwzePpCHsDsKFKCCaGL1PDg69hxrWYSUY5Sqqs5o5fkLruQAMkfGv0kbhII6UmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: زیر بار زورگویی آمریکا نمی‌رویم
🔹
ما که تسلیم نمی‌شویم تا هر غلطی خواست بکند. آنها منتظر بودند ما در کشور با قحطی مواجه شویم.
🔹
اگر دانشگاهیان به میدان بیایند، از بحران‌ها عبور می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/659663" target="_blank">📅 11:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در مبارکهٔ اصفهان
سپاه اصفهان:
🔹
به‌دلیل انجام انفجارهای‌ کنترل‌شده تا ساعت ۱۳ امروز، احتمال شنیدن صدای انفجار در مبارکه و اطراف آن وجود دارد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/659662" target="_blank">📅 11:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNdf-f6BbYs-6ioPTmSfXUh65uCB9xB4ce_WSW4-cZHi6B7c_GcrrjcgzHUWaQ1PUI8mEPxuUoEASzyDCcaOOlxx4kIQWrhfj82p7a8JjWEpG73T4EjcdcH7KMnQXx3C-UEV6IYcHF1lbjNOlJDx973kV-zNZzHCsD53SH5Pajh0-_UleAzoA5YD34sjYMNJXzJO46ljSvqHT2n-eUaeCEdL7ZiK5_muIX_3li8P7GdA1hP94IUj0mF4arkb3QVRN-BihTDcvdoMzKYZR4f_vvYjoZBONuJLzNX7WkH78aukndDSpn2abAHBUTfcdm5BUwLVucYTq2bEdztZ4mP-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e895ef02.mp4?token=p9lfzsM__Sn_fS5rSLl9xJGjdyg0F4SWmgskBOBJgJM9lIuOJkEEDnoPB-SHJFis9FTo9EoAyz9E1yfqzBDyZapAktPOqOTWF6AiTdEj59I78WFxkEWdOVvska-MFEyINfwsT-b0-_8NOSZN5SAOuomHLzow5XuQYL7vIIWEF9q1BSG2B9-Y4ei8UuDDr60ygBsaaQtsGeYOVTqFJ7G-bKe1_0gKzhnFXciRgGyBDc5XGaPTRJjbrYe7rmq5_6SeXLDhulF3NcJkxIBgTW-8XM3zOlmkmRJQZsODANCEC1AS8f4FLN4fOVGIJlTDLHFrClPV2L_i9gYc87VHaLIWGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e895ef02.mp4?token=p9lfzsM__Sn_fS5rSLl9xJGjdyg0F4SWmgskBOBJgJM9lIuOJkEEDnoPB-SHJFis9FTo9EoAyz9E1yfqzBDyZapAktPOqOTWF6AiTdEj59I78WFxkEWdOVvska-MFEyINfwsT-b0-_8NOSZN5SAOuomHLzow5XuQYL7vIIWEF9q1BSG2B9-Y4ei8UuDDr60ygBsaaQtsGeYOVTqFJ7G-bKe1_0gKzhnFXciRgGyBDc5XGaPTRJjbrYe7rmq5_6SeXLDhulF3NcJkxIBgTW-8XM3zOlmkmRJQZsODANCEC1AS8f4FLN4fOVGIJlTDLHFrClPV2L_i9gYc87VHaLIWGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب جمع‌آوری زباله توسط تماشاگران ژاپنی در بازی‌های جام جهانی
🔹
رفتار تماشاگران ژاپنی در جمع‌آوری زباله‌های استادیوم پس از پایان مسابقات، بار دیگر در فضای مجازی مورد توجه قرار گرفت.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/659660" target="_blank">📅 11:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بانک مرکزی شیر پول را بست
🔹
بانک مرکزی در عملیات بازار باز با وجود افزایش ۳۵ همتی تقاضای بانک‌ها، عرضه پول را در رقم ۱۳۰ همت ثابت نگه داشت.
🔹
این موضوع اگرچه نرخ بهره را بالا می‌برد، اما برای کنترل تورم و جلوگیری از رشد سفته‌بازی مثبت ارزیابی می‌شود. موفقیت این سیاست منوط به کاهش انتظارات تورمی و گشایش اقتصادی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/659659" target="_blank">📅 11:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db98c3f70.mp4?token=VaV7nuCRoONt7ifLS5oWx0fhYkbLRCIe4cWc4eXrY4ILTxeZe9l_JAb2ZuSpau7A0rMN5CftkRFSHGdzC5oCg_vvnYVfOPjQq08WmuMyHB91w-blsZvSk1EHxPDbL8FF_9QzAnCWDWPQ1IYXUuFvC0o4zg0i8pEkAgfrn1d02ib-mxcbm0A_DiTFn6fWX6yfGpiuc85TVWB-BI0lJ1HwUvtHB8ZAZlEIl-TZvzif4N-QRY6CPAVhbgai0S8nI6_MUKMWuxgcrtfVvrAhn1CAZG92XBFF7quuJZT_OM7abUQ66QD8bZKUmBBxSJsfmlvYRXaK8tqCnlrPyXaPvGh8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db98c3f70.mp4?token=VaV7nuCRoONt7ifLS5oWx0fhYkbLRCIe4cWc4eXrY4ILTxeZe9l_JAb2ZuSpau7A0rMN5CftkRFSHGdzC5oCg_vvnYVfOPjQq08WmuMyHB91w-blsZvSk1EHxPDbL8FF_9QzAnCWDWPQ1IYXUuFvC0o4zg0i8pEkAgfrn1d02ib-mxcbm0A_DiTFn6fWX6yfGpiuc85TVWB-BI0lJ1HwUvtHB8ZAZlEIl-TZvzif4N-QRY6CPAVhbgai0S8nI6_MUKMWuxgcrtfVvrAhn1CAZG92XBFF7quuJZT_OM7abUQ66QD8bZKUmBBxSJsfmlvYRXaK8tqCnlrPyXaPvGh8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور میشه که آدم‌ها با یک‌باره قطع ارتباط می‌کنن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/659658" target="_blank">📅 11:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4dtqws0AimmRtui05penRJcuFUmG2qXnD4Rs1i0zEw6VY3xNr9hShQXVJ02sbG_DEQKuE9F3Kby15GHWpIBUDEtl735U3riUWNPDfENnZ9hgZtMIAxViBe2flwZgJ7zcUvQo79xZgGhR2KR3rtoqFui6jhVsB3H_owVyCkSh5ftapGJDgJFiJ4CX9nOVfie1FUaI86CfSBIVFGUq-j7bm7I-AFAOjWerlGVGBP8kr2y5URIoLr8A-Iefjx43bbevqxlJ2iwCW-vQrs0J2LxBMhPGKVfjbTGVIGQ5zyxjpC474tlskFNVsFz0-Vq0enbmDtwhmBbPb-ThJ9gEByKyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از اعلام توافق اولیه ایران و آمریکا، نفت وارد کانال ۷۰ دلار شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659657" target="_blank">📅 11:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tee2q2_bMeiJt9aIFyB9zPXcU05e5Kq-C6DCZtvRhL3S95-IkCrWGZ28JFBqhe0tAL5hlcqdmstoxnrUMn0NYEp1saYX-fDIiMKBFfEYhUq1ACZCWUBjzLlmJQIBJZgMsNhDTKk2QjkCI4y1J0PiN91tD_0hvVEb5SkK-nVbU3hrkzpVQbgxf6IxjTWc-6E5CuyC1dB9sc6Z8eNWY4URolB8HGGgQm5b7trLhm38_S2_YCQ_f13nuidbPCsmf0z-xZY_OZyy2a27tk2C7cdmWDsndWvier8_zo1XIxmiGPiuGIerWqRhSTngH2LgM0YrLmiqJA-EJm0viFF-SMPhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد کودکان قربانی در جنگ‌های ۳۰ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659656" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFxvoANu9zc_cg_tcxVqbuVdhqHIrgNrEq0nE1c09WbcVUn28jX2L_aHphBRC6bBcwij7AMSfS66HXJEAk_gcqZ_lIYw_R3IDZbtH2DxvY_XqiXnpIV62IzAjgH8rCYmToFrmawcLT6m1t4kqnWGERzfgMemV92rN3i-RvMDWYh6nkUmnSfQr_Wo4Ninvd-Z-yEPbZ2enDJ80B8_nHXnxXI0m2RX5MhYuNBI7-i6N_sHe72uTYbndxmZUSXyUR0lHY6Tcn8b9zUS1MouavKwHwoEYheVCWHtUl0Qum14FjO2XDaHsul9vUxbZWYLP1H1DXaixpR-wItiZQpsw7XVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رده‌بندی تیم‌های لیگ ملت‌های والیبال ۲۰۲۶ در پایان هفته نخست
🔹
ایران در رتبه پانزدهم.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/659655" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c129946cb.mp4?token=qFB7UuKMlN1GKKg-Sii42pJuCUSMGB12g9WTveVPkArSOPZLwB0TmZAJmDnznPrC1Ldp0lnodrkyhIq9jTPvBMf2wTaGtAiii9iY1chbWSchK6i0OxK2TfBFeQJ0UwPMC-z7-qdUywP5A2rNCYUmSKuKucddKJOXocl0dmkjpSE6qTKhd7zKHls5rrqHvTgstfYLgfuj8cd4PwTTAvcQjy8BkvVtFo8eSdZ_RupdllM5V2u2NEXBhlSyt7Qw2j6nc1UyvQbmq264RCVe4rmRBSbEOZNNdTxoeGB653mir6gEjxfIzXuDbsFXrwV1IeBVOAed3yCcC-YNZ6VL6bF-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c129946cb.mp4?token=qFB7UuKMlN1GKKg-Sii42pJuCUSMGB12g9WTveVPkArSOPZLwB0TmZAJmDnznPrC1Ldp0lnodrkyhIq9jTPvBMf2wTaGtAiii9iY1chbWSchK6i0OxK2TfBFeQJ0UwPMC-z7-qdUywP5A2rNCYUmSKuKucddKJOXocl0dmkjpSE6qTKhd7zKHls5rrqHvTgstfYLgfuj8cd4PwTTAvcQjy8BkvVtFo8eSdZ_RupdllM5V2u2NEXBhlSyt7Qw2j6nc1UyvQbmq264RCVe4rmRBSbEOZNNdTxoeGB653mir6gEjxfIzXuDbsFXrwV1IeBVOAed3yCcC-YNZ6VL6bF-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکر ال‌ان‌جی دیشا که متعلق به هند است، اولین کشتی است که پس از اعلام تفاهم‌نامه از تنگه هرمز عبور می‌کند
🔹
این تانکر محموله‌ای از قطر حمل می‌کند و مسیر ایرانی از جزیره لارک را طی کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659654" target="_blank">📅 10:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تصمیم بحث برانگیز در لس‌آنجلس برای بازی تیم ملی ایران
ادعای نیویورک‌تایمز:
🔹
فیفا ممکن است اجازه دهد تماشاگران پرچم‌های قبل از انقلاب را در بازی افتتاحیه جام جهانی ایران مقابل نیوزیلند بیاورند. گفته شده جلسه رسیدگی به دادخواستی که ممنوعیت هیئت حاکمه را به چالش می‌کشد، تنها چند ساعت قبل از شروع بازی برگزار شود.
🔹
روز پنجشنبه در دادگاه عالی شهرستان لس‌آنجلس شکایتی برای این موضوع ثبت شد که صدور حکم مقدماتی در مورد این ممنوعیت صبح دوشنبه ۶ ساعت قبل از بازی رسیدگی انجام خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/659653" target="_blank">📅 10:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
بن‌گویر: توافق ترامپ برای اسرائیل الزام‌آور نیست  وزیر امنیت داخلی رژیم صهیونیستی:
🔹
توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع آمریکا نیست و ما مستقل و دارای حاکمیت هستیم!
🔹
ما شریک این توافق نیستیم که به امنیت ما توجهی ندارد و این توافق به هیچ وجه ما…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/659652" target="_blank">📅 10:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX5YlR2IvQqmjyc6QT6qWU-CoLurkyYfP_idT7rABNQ6Oc9O1lc32BbSq_U-yVQZrQbTJWa2IZY_uaGAZQGw_G1ZYaEQFWwrgsg75qNygIUtZQRdz_eSTC4a4GRvUmNciGOqRcUcgzqfAVv5J1MTkJ8x-t5E1dQOB17LLDxExthB5puOb4u5iu4b9KhdVm9OTRv9pvdkeiI6x3Bq2N-2UHkMZPOj2GFjAx6VSgmUmdNGeqHH6q2qC805NyHC3BmFmR3qyPq-CTKGY6JFGudJpM5GIU_GTw6Pg6gXJHJopErPF94NiYL9qCjS2Y5xowcQOVkbI1vzkxla5UTiVyzVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوباما: بعید است توافق ترامپ با ایران بهتر از برجام باشد
اوباما در گفتگو با ای‌بی‌سی‌نیوز:
🔹
در مورد توانایی دولت فعلی برای ارائه فرمول جدیدی که به یک پیشرفت واقعی فراتر از آنچه قبلاً به دست آمده بود تردید دارم. بعید است توافق فعلی با ایران بهتر از توافق سال ۲۰۱۵ باشد.
🔹
دیپلماسی باید با وجود پیچیدگی‌های فزاینده منطقه‌ای، در اولویت اصلی باقی بماند. تجربیات تاریخی، شکست تحمیل اراده با زور را برای ارائه راه‌حل‌های پایدار ثابت می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659651" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0KdCqddupTfvg3IKY6XZ2IPvyFwACJvyrtWwAi0Xt6pdox-CxgLfajbzrd3l7qTYEe9Dkfn857jfVAadUsirFTjik-9M2Mn89DBKm-HjSm-eMsFFfz9SnusFKWWm2drnst4-oct23KbsHHQwrHsc8_RwqXJNiLkuixe-irKRLyKw8HuAdLgnFGvrrEb1pklGIfh_T0ViqUtHH4hSPOuEhbRR0qyoTcZTN33epoUrHK9v18o3yv4Kp7ygWJa6SG81hE-nUzIHSKkfQTqFHhDyYlMFF26ZohIZheWCR23XIUqmf2Tm6TAb7OocLG23XQ6iQP6cfk-aYNns2Hb3Yl6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا که نه در میدان و نه در مذاکرات به اهداف اصلی خود نرسیده، اکنون عملیات روانی در تلاش است خود را پیروز نشان دهد. گام بعدی آمریکا بمباران رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659650" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4426e7ff.mp4?token=fFncdccsb7jBfXi3JWwgNhzoWnNzYDSWVDIHVXwNYilHcY-fATwurYWt42ndghtN8hr1goXShtydKtgbwTu8fu-wZNUv-ba0447ThMxinmnunjr8nrygPmz_RRzRM5f7XWARMkLJa0-oEVRV8LlABDTVprnjcA5Kip3ytgPTGOSF7SBXCxpfx8Hf0Q8Cnv7ySfQHWAeMz7uV6DzFbuajOoRWE0giAlhyTMrlQS4pEz4p-KSbhb1xkhMqQM60KQ6UJIaxYh2cQQ9nGWaDnzEHx_vx7xXmihgXGPGy_5ogwX_ZYrSx-jUmtccdtNC8MxoZHrmmnQpZLRPpYV0Dj5RNkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4426e7ff.mp4?token=fFncdccsb7jBfXi3JWwgNhzoWnNzYDSWVDIHVXwNYilHcY-fATwurYWt42ndghtN8hr1goXShtydKtgbwTu8fu-wZNUv-ba0447ThMxinmnunjr8nrygPmz_RRzRM5f7XWARMkLJa0-oEVRV8LlABDTVprnjcA5Kip3ytgPTGOSF7SBXCxpfx8Hf0Q8Cnv7ySfQHWAeMz7uV6DzFbuajOoRWE0giAlhyTMrlQS4pEz4p-KSbhb1xkhMqQM60KQ6UJIaxYh2cQQ9nGWaDnzEHx_vx7xXmihgXGPGy_5ogwX_ZYrSx-jUmtccdtNC8MxoZHrmmnQpZLRPpYV0Dj5RNkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار نیمار از دست هواداران در میدان تایمز نیویورک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659649" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
بن‌گویر: توافق ترامپ برای اسرائیل الزام‌آور نیست
وزیر امنیت داخلی رژیم صهیونیستی:
🔹
توافق ترامپ ما را ملزم نمی‌کند. اسرائیل تابع آمریکا نیست و ما مستقل و دارای حاکمیت هستیم!
🔹
ما شریک این توافق نیستیم که به امنیت ما توجهی ندارد و این توافق به هیچ وجه ما را ملزم نمی‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659648" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تداوم اختلال در خدمات غیرحضوری و بانکی ۴ بانک بزرگ
🔹
به‌رغم اعلام رفع مشکل توسط شرکت خدمات انفورماتیک و اطلاعیه‌های رسمی بانک‌های ملی، تجارت، صادرات و توسعه صادرات، گزارش‌های مردمی حاکی از تداوم اختلال در سامانه‌های موبایل‌بانک و اینترنت‌بانک این مراکز است.
🔹
در حال حاضر بسیاری از خدمات غیرحضوری این ۴ بانک همچنان با قطعی یا کندی مواجه هستند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659647" target="_blank">📅 10:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خروج از کشور مشمولان غیرغایب در محرم و صفر بدون وثیقه شد
سازمان وظیفه عمومی فراجا:
🔹
مشمولان غیرغایب دارای معافیت تحصیلی یا برگ آماده به خدمت، در صورت داشتن شرایط قانونی، می‌توانند برای سفر زیارتی عتبات در ماه‌های محرم و صفر بدون سپردن وثیقه درخواست خروج از کشور ثبت کنند.
🔹
ثبت درخواست فقط از طریق سامانه سخا و در بازه ۲۶ خرداد تا ۲۲ مرداد ۱۴۰۵ انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/659646" target="_blank">📅 10:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90646649b.mp4?token=hsxGFAC1LjPQipi-f73dWN046kxBkVPl-YTX5P05lHsS4uDW6iQqjJli0rkBnd2QtZwR06PkBAOOmzzh8PFZOKkyFW62zZ9Hubl8yspViru2VDdZnDyisxW0SCatvlsIkjKZudsEeRP6Pq9r0M-wdPkgbzRz0_BudfKkJFg_XPsMusRiPt_cW1-iKlL1VJpHplKKTnqU7xLoOuL45SkRTT6NgXuwH100OUVbtYc63js775w3EZjejAsLSF2KjYOBZUd4rOHwA0PERvtnC-Rk7iLWBJ1qkrNg96nh_1g5iBku2hpNjHiQ5rkJ50Tj3EQkk5eJDc9Qs55vgxZME4dQ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90646649b.mp4?token=hsxGFAC1LjPQipi-f73dWN046kxBkVPl-YTX5P05lHsS4uDW6iQqjJli0rkBnd2QtZwR06PkBAOOmzzh8PFZOKkyFW62zZ9Hubl8yspViru2VDdZnDyisxW0SCatvlsIkjKZudsEeRP6Pq9r0M-wdPkgbzRz0_BudfKkJFg_XPsMusRiPt_cW1-iKlL1VJpHplKKTnqU7xLoOuL45SkRTT6NgXuwH100OUVbtYc63js775w3EZjejAsLSF2KjYOBZUd4rOHwA0PERvtnC-Rk7iLWBJ1qkrNg96nh_1g5iBku2hpNjHiQ5rkJ50Tj3EQkk5eJDc9Qs55vgxZME4dQ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی تماشایی از نمای جنوب غربی کوه دماوند
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659645" target="_blank">📅 10:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHZ7g9PmaXPEVx99Rj-ZL_JHxUDAHx3N1CtOeu_t672kiOi9aLj8xJmL1WnbIO1qEA4prJVskX7f8N2nNjcj2CwPFPXylx8ZyxZY0i1Xd-w1f8TvaP6puNJJbEzxzCjNVCE7S8PczuH10qbnYZ1p7LXe-T_gFylCyOSgdewgt_cVKVCRnAzL592wPqvYv0GIcfquMhEUC-b7hFcfxBCkaNd89jMkFC1UNtARJt2h63eatEfdwCNbqQ447KUaaeyyfWsNj9RX82I3B6KQcfHKYVV0PGmqVtX-u2oD19zsgXDJDayXNi5W08up4hYVWBa2LCZvguXz9CyC0uXv4n--AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: قدر همبستگی و وحدت را باید دانست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/659644" target="_blank">📅 10:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نتانیاهو خطاب به ترامپ: اسرائیل از لبنان خارج نمی‌شود
یدیعوت آحارونوت:
🔹
نتانیاهو، به رئیس‌جمهور آمریکا اطلاع داده است که ارتش اشغالگر خود را «ملزم» به رعایت بند مربوط به لبنان در توافق با ایران نمی‌داند.
🔹
نتانیاهو به ترامپ گفته است ارتش رژیم صهیونیستی در مواضع کنونی خود در داخل لبنان باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/659643" target="_blank">📅 09:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTiDIT1RFtVHkJWLMv7CwxKB482-CHJEfDUAisp6c0I6KvPWZLSNiWLAcaLu3_0KPgXwaTfUBaa9iU8-FvhoPS7lv5bdmnA-XlrMg60GV8-4BlQavEDv82MrAH0Thqt6fDqWyyO_VfSyLsBe1YU1VmL_s_HxDutAIslzQSnZgoOSslPflRPPICopt2i99WX4DSwrIVo0D-E5B6VHIh0L7zhYmrrDc3mAWpKvmal5HPPI_ZyPOTqQFjmxW-6mSZHArd7S6cedBpmTZClVenrqBypk9ZvlZULRyDgKxnvvBHZ0_xZb7IZEyhvPCenFSmeYhrGGNHNfmx8o6ElZYa1PbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتایج تیم‌های آسیایی تا بدین جای جام جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/659642" target="_blank">📅 09:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2e12e6a9.mp4?token=WhHs0vGooQABUfsOxlHXOV9p7Zk6prLtYQS3wPM2-lCDGV9u2f7aLcynNON1xmAEzLqwO506w8r-tpVw6lMNONcHczt6t9pddr25ockuzi4za57QLwkBR1Kljy_0GFzsno2g3n3MBbKqNHsD34-5ca7hG93_hHsSm_AS6UMqVBJUhsr52PtCwQ14wh9iEkKnOQJ7AeDKHAWqdn0GuOTkn8CqnRrPDwhDWlpygVxVihTeTwDp4LEPq551gYuN0bZMvMVepF9OahJVyWLWWywVwvRrweYwGmyddyTuB81TrEYdg3MJew5GqpvFXNqMi1GwEfgowlOkeN-uD0NG6kumCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2e12e6a9.mp4?token=WhHs0vGooQABUfsOxlHXOV9p7Zk6prLtYQS3wPM2-lCDGV9u2f7aLcynNON1xmAEzLqwO506w8r-tpVw6lMNONcHczt6t9pddr25ockuzi4za57QLwkBR1Kljy_0GFzsno2g3n3MBbKqNHsD34-5ca7hG93_hHsSm_AS6UMqVBJUhsr52PtCwQ14wh9iEkKnOQJ7AeDKHAWqdn0GuOTkn8CqnRrPDwhDWlpygVxVihTeTwDp4LEPq551gYuN0bZMvMVepF9OahJVyWLWWywVwvRrweYwGmyddyTuB81TrEYdg3MJew5GqpvFXNqMi1GwEfgowlOkeN-uD0NG6kumCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ قلعه نویی به عدم حضور سردار آزمون در جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/659641" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFppjKS0JyEryOIZYxXLyahxutEeoO9e7eOHOzoVMf2hlDHkX4rj3ifa2COhk8rShMKpp_YFrGdyN24_jQR598XOgalfOdhjAOAYWMCD8BjRjEJjwwaKCKrGKnBxgfWYHe4LxLKMz49vCj5l1PhiIuRIIozOAqUEmGqTkcLEBJuAdMAHdxCshcet7DOMVTTnlzQXderYvnHFVTmDNhdvHldLYsuAI8yrVZiirtOXtt_BfUcC3vnI5HX1tbM5W-DbtZKYHnHCE_rrO4kzg5HWyZhw4_RodtZZ-luSS2jRBqVvdTcZ2r5pxkMs5Kt1kQk7JYxe5CPTqOyLqoMiePD-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/659640" target="_blank">📅 09:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404b6caac2.mp4?token=L72alOBlnI8YqxKJ999rxcIeul5iS7E7uVD8VGVYkI7Wh2WfxJSI8ig6wJQqL83N_f_Z9t8_gWorlehFpBpjm3vOjmuiFIUkQlUE9qlStgee1zuDDIpiGjIO81Y8zwJPQ_fjUuFPP59N6pLdKg4BKRhc76vFa3dxFVVhDdkfZfx50bIh-4Z-tzMNdqT61OP8eBPreM5BRHwTx5I80DktWQcpOfSrQpPrRNLBuqa1krCXVGUVbhu8loF7Hn-MnZ6gpW_oDwywWSTTJotkBRHJRVO8zN_RPbOldKrFd7YKDpQNByif7Y6TKZAY8jj_tRnZDFTfjIznPe4zAR5tfrOsag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404b6caac2.mp4?token=L72alOBlnI8YqxKJ999rxcIeul5iS7E7uVD8VGVYkI7Wh2WfxJSI8ig6wJQqL83N_f_Z9t8_gWorlehFpBpjm3vOjmuiFIUkQlUE9qlStgee1zuDDIpiGjIO81Y8zwJPQ_fjUuFPP59N6pLdKg4BKRhc76vFa3dxFVVhDdkfZfx50bIh-4Z-tzMNdqT61OP8eBPreM5BRHwTx5I80DktWQcpOfSrQpPrRNLBuqa1krCXVGUVbhu8loF7Hn-MnZ6gpW_oDwywWSTTJotkBRHJRVO8zN_RPbOldKrFd7YKDpQNByif7Y6TKZAY8jj_tRnZDFTfjIznPe4zAR5tfrOsag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صهیونیست‌ها شبکه‌ آب‌رسانی در کرانه باختری را تخریب کردند
🔹
منابع محلی گزارش دادند که اشغالگران رژیم صهیونیستی شبکه‌های آب رسانی در مناطق «عاطوف» و «راس الاحمر» در شمال کرانه باختری را تخریب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/659639" target="_blank">📅 09:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
با وجود ادعای لغو در صورت توافق، محاصره تنگه هرمز تا جمعه ادامه دارد
ادعای سی‌ان‌ان به نقل از یک مقام آمریکایی:
🔹
به نیروهای آمریکایی دستور داده شده است که روز جمعه، مشروط به امضای توافق با ایران، محاصره تنگه هرمز را لغو کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/659638" target="_blank">📅 09:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b718f0b981.mp4?token=tn6ZgnlIpSQkjSYSWLqwUjJDooPRxRA_sUraJWtGNKr8tC6m2GwWz7y4XiicVsIDmzadOeKcjuiDfySBj0riTMPOSq6rgPCDKJ1tA-yXFJgGyX88AwKPAoT7Yl3wsu_m8NkxTc7KHlgQwc2mC3XO63RpuaGhrp4iuIIKBaaC05zkLSdaFxcp8Gr8XJSgiftlEQqgsHJg7CnVTxHjm2HnOWZFwdTMOes5TO7lTDkH4cXrM42AlEVdwnChvPAy2gTbWcZXqgOpd4ZexeQYOAbp3TjdOZFQZHHVVqqIhsklXwQE8Fgw5x_GllnHohEx4opL7QxvAkcmB7zoGbA42NCmtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b718f0b981.mp4?token=tn6ZgnlIpSQkjSYSWLqwUjJDooPRxRA_sUraJWtGNKr8tC6m2GwWz7y4XiicVsIDmzadOeKcjuiDfySBj0riTMPOSq6rgPCDKJ1tA-yXFJgGyX88AwKPAoT7Yl3wsu_m8NkxTc7KHlgQwc2mC3XO63RpuaGhrp4iuIIKBaaC05zkLSdaFxcp8Gr8XJSgiftlEQqgsHJg7CnVTxHjm2HnOWZFwdTMOes5TO7lTDkH4cXrM42AlEVdwnChvPAy2gTbWcZXqgOpd4ZexeQYOAbp3TjdOZFQZHHVVqqIhsklXwQE8Fgw5x_GllnHohEx4opL7QxvAkcmB7zoGbA42NCmtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ حمله ارتش اسرائیل به کفرتبنیت در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/659637" target="_blank">📅 09:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOZ_LqCEDmLWBijhnYcFeKKuDG1cQIzd5AoZpLDbL70aFC9nlRf1OPPqLu6xaufilrVL312uecRcKTNHqyJmz-ak5c03KA7hg60RGPrGRmcbUkdaD5qBLV1Rk5MYj1NBGOp1rNxkW9wy0bouaj84cRJm4g7BBjtiFdkcIeHfSEiiQqvJjowvMn3Tu9Ze8AIWlm1ZbERtTEIFuH-WvHstMCkCwt9qmdx9962GNINJvehDcslOcFuB2_LK5wp3A0pDg2O5cyJ6LUF7Qbzs1KfUUGeekfHahiYbCzBKBfW_mL0SIomg7mpKzfvzyKf_jEbkEaCqL3HmQI79rztkwFIk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس وارد کانال ۴.۹ میلیون واحدی شد
🔹
شاخص کل بورس تهران ۱۱۰ هزار واحد رشد و قله ۴ میلیون و ۹۲۹ هزار واحد را فتح کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/659636" target="_blank">📅 09:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6952c7235.mp4?token=hetQq8zxSexoo79SV-wfAavrW4M_JDou3SlMnZ2rk_X98-Jk3a5V6fxOx2mF-dFe4Dm2oZTYho-ntuTzt9mm_C4znabysCl733PMyprJXNNjdQkyX9CL2uM2-JP2meAO53_GxB8IKKl8wZ_ba32XdzVbO1Rc7H9yUbpm8P-6F1GpmmgF8ryHvGV6C2jtt95np8Of3uZoP9vFU3evRXrkNXTC3HTJvEcAh5qGL2cQDXDOfJWpzOwbZ-VkZ1fp9Bv_jCALt9AOiy9llVCZ11pqSKyLSAIqpJBi47juqPfZgP-hqesPoEMERgG0g22B4Mo-AUttkevOPKe1onqC8wyniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6952c7235.mp4?token=hetQq8zxSexoo79SV-wfAavrW4M_JDou3SlMnZ2rk_X98-Jk3a5V6fxOx2mF-dFe4Dm2oZTYho-ntuTzt9mm_C4znabysCl733PMyprJXNNjdQkyX9CL2uM2-JP2meAO53_GxB8IKKl8wZ_ba32XdzVbO1Rc7H9yUbpm8P-6F1GpmmgF8ryHvGV6C2jtt95np8Of3uZoP9vFU3evRXrkNXTC3HTJvEcAh5qGL2cQDXDOfJWpzOwbZ-VkZ1fp9Bv_jCALt9AOiy9llVCZ11pqSKyLSAIqpJBi47juqPfZgP-hqesPoEMERgG0g22B4Mo-AUttkevOPKe1onqC8wyniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شست‌‌و‌شو و آماده‌سازی حرم مطهر امام حسین‌علیه‌السلام برای ورود به ماه محرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/659635" target="_blank">📅 08:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منفجر کردن منازل مسکونی در جنوب لبنان توسط اشغالگران صهیونیست
🔹
ارتش اشغالگر رژیم صهیونیستی بار دیگر در جنایتی آشکار خانه‌های مسکونی شهروندان لبنانی را در شهر «الخیام» در شهرستان «مرجعیون» در جنوب لبنان منفجر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/659634" target="_blank">📅 08:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b96ee15a.mp4?token=AVDX4GPwV_qJXXSIw7ljoQPOHs2NLp5521vgTGFN2P_wapeBeBCpp8ZIUKSMENxuW0Q-fIhwXLx8xzI43h4Pq0UACse6mffhyTxFcMNdJK79J6ncHWkzldsPdyjSYH6aCUb-yYcPVwxTb-piHHjMJGPFRTjePOCmzhyDAaw_NW7-a5YaozdM1oy9C5FV1Vh4Y2Hx5sJDM09-_W4DHsEBehlssDjmKZUItrE_18rJki2Po1b2EJxFguPMelu2epHysKBNpIQjDY3-kI8rCIJagQzk2ELlu8aWkqCN6GwuYCPsB5jKeARw0Nvq4O8WCINDu_nTK4FHCziLS1PxiBgcTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b96ee15a.mp4?token=AVDX4GPwV_qJXXSIw7ljoQPOHs2NLp5521vgTGFN2P_wapeBeBCpp8ZIUKSMENxuW0Q-fIhwXLx8xzI43h4Pq0UACse6mffhyTxFcMNdJK79J6ncHWkzldsPdyjSYH6aCUb-yYcPVwxTb-piHHjMJGPFRTjePOCmzhyDAaw_NW7-a5YaozdM1oy9C5FV1Vh4Y2Hx5sJDM09-_W4DHsEBehlssDjmKZUItrE_18rJki2Po1b2EJxFguPMelu2epHysKBNpIQjDY3-kI8rCIJagQzk2ELlu8aWkqCN6GwuYCPsB5jKeARw0Nvq4O8WCINDu_nTK4FHCziLS1PxiBgcTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صهیونیست‌ها مسجد «النور» در رام‌الله را به آتش کشیدند
🔹
شهرک‌نشینان صهیونیست به روستای برقا واقع در شرق رام الله یورش برده و مسجد النور و یک دستگاه خودرو را به آتش کشیدند و برخی از نمازگزاران را به محاصره خود در آوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/659633" target="_blank">📅 08:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjLVV0E5vag2LmNnxOOKmNjQIkzCGv6Vv9JHTn0ijuYEmZ_PVIAuRucJxKXf0uPTArhx8l9rQfcVsr96edbs05l5yXFICF7XKnpBCiVSGEVHT4FOiPGTf-dbqqi7wZ-17EmnEZmy1W13wYegtEYet3-WEO9mwuewOcY0lyh5wj_MalyKCV7WNVFMypNKlf6g1gfLxf8RcmlYUxLjNxAY-lYyDk267rmXBiI6wULFiZYs_HAwMnZzCpQMB5vC5OnlSGDrgim257suqYskS3iCbdfmHznn3rjiTKHz4dOurPdnoSMd8ixPuO4Z8iIDOszjW2oKZdQephbvpCWYUko3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهروز رضوی درگذشت
🔹
بهروز رضوی ـ از صداهای ماندگار کشورمان ـ به علت بیماری درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/659632" target="_blank">📅 08:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdnc1ME7F0KQ7awez6qD4J3gnwHgmhKZZUgkmVOhybN2C8pe22YOUBS5oi2rczep6X6lbvabn_RcLwVFhHfaaPWIx0cyI1xYQXPxWAbqS7FodC24MxyvLjIvI254IEYqqS09I3BSGe7Cq4SthEYOFj99g9fRFuk1bfA0gQVCXhS0bRq8JAurYDSED7IqzhOXL2eMd59VauG08h3xcj2INk4RIoJKNMNpaOEFR1R1eS63KT9P4N4XMRXqEuF_G7N2KUjOa0cxnwDqgJdbUMNRPNPDq7T_hF2HWewp7JN-btQpi9bH_D98LRMY-_Rff8GZ73cjRJhAaPd2rRoIJzueMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تانکر ال‌ان‌جی دیشا که متعلق به هند است، اولین کشتی است که پس از اعلام تفاهم‌نامه از تنگه هرمز عبور می‌کند
🔹
این تانکر محموله‌ای از قطر حمل می‌کند و مسیر ایرانی از جزیره لارک را طی کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/659631" target="_blank">📅 08:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1277c020.mp4?token=R9QWd4h3LYlz1syKYL7DZIRepu55dd91nFqwRZcwZrxUT3IXzH1Ot91-YjryLQk_mVUZxovDbX_lCjDwwA6eYo-Pnftv99bLjg8iSm3F0NhGUDL3-VCvXOuBt-yhAkI2JWGCviyFeigAK8uz3NnmEeIJphr6Qd8LuMrjr4iqJ0yqwyssJlxWZhTvL8fLfJitanaH3ttvpni3bb15b3bqcOpMb2JH9HDXdSN-PmMB1nWUHEN5uvq_mtB5mFIvpIegRkU_QVx2qQKVSH8lNZJ4BA9lHE7yqY-SvZ_x0irRTKoMpmwjFFIT9dT-XG2wux52T8fdICstDz5b-wjdSqsFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1277c020.mp4?token=R9QWd4h3LYlz1syKYL7DZIRepu55dd91nFqwRZcwZrxUT3IXzH1Ot91-YjryLQk_mVUZxovDbX_lCjDwwA6eYo-Pnftv99bLjg8iSm3F0NhGUDL3-VCvXOuBt-yhAkI2JWGCviyFeigAK8uz3NnmEeIJphr6Qd8LuMrjr4iqJ0yqwyssJlxWZhTvL8fLfJitanaH3ttvpni3bb15b3bqcOpMb2JH9HDXdSN-PmMB1nWUHEN5uvq_mtB5mFIvpIegRkU_QVx2qQKVSH8lNZJ4BA9lHE7yqY-SvZ_x0irRTKoMpmwjFFIT9dT-XG2wux52T8fdICstDz5b-wjdSqsFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: «بعد از حمله اسرائیل به بیروت، شواهد زیادی دیدیم که ایران قصد دارد تعداد زیادی موشک به سمت اسرائیل شلیک کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/659630" target="_blank">📅 08:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945bea0c9d.mp4?token=Z65S4LF6bzbVvdrqjj3GdrJ7NE7w8VGIjl7f_rY1tZYJ1mNuoQ7vu8-JoUUw0KoNLLQFfETObRQszRpN8828jotUdyFYLpgO-F-FsvpcMpHV48-cbkfHCES6twohZF_eWsHTdJj62JyypsMIl6TYlT40MUtsiVm3nO0igkzWBPXWxJ8TD4hWxdLSwE2Hp6dlm9qaVI_5JXr0lGKqLYZ3GaeGhjneiMuVQdZ49KObge4WGSRgoJO2-5dVdbGVhnOHnGY9sQJK-YUNeFjPNEcRgRE6Upz3tuXz6zyQQEsIQprsHt9uDei-HGftHE_C2SKIl90nbcasjLalD_7w3Pty1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945bea0c9d.mp4?token=Z65S4LF6bzbVvdrqjj3GdrJ7NE7w8VGIjl7f_rY1tZYJ1mNuoQ7vu8-JoUUw0KoNLLQFfETObRQszRpN8828jotUdyFYLpgO-F-FsvpcMpHV48-cbkfHCES6twohZF_eWsHTdJj62JyypsMIl6TYlT40MUtsiVm3nO0igkzWBPXWxJ8TD4hWxdLSwE2Hp6dlm9qaVI_5JXr0lGKqLYZ3GaeGhjneiMuVQdZ49KObge4WGSRgoJO2-5dVdbGVhnOHnGY9sQJK-YUNeFjPNEcRgRE6Upz3tuXz6zyQQEsIQprsHt9uDei-HGftHE_C2SKIl90nbcasjLalD_7w3Pty1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلافات نتانیاهو و ترامپ
🔹
انیمیشن از: کمال شرف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/659628" target="_blank">📅 08:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yx2YkTIuGU_TEqgut-U67IOVvfB8VaSWgKGmkpPMS-iJwob7lDK1_5Phoyo6biogpjEvcBUCfTdTnCZTXwUGr4KCx_aoXzhKVX4-GnnkRKDmvYlV4Fe1bVZWDQL5pjwYYdV_n2LT1YDG-SOySyoMH93Fou72aQSB6nBWfszNpjspsQ5EriHfwAW_T3dI90xU_WZpND7P2j7BizeWbRtWkikRjkAaMUQrHmYSODw5U_Kc7W08eEaiQdFm2oI8N57Xc4LFxXeTUxfcL2LQJPlhC1jsqzyGOirTHNH7ntWIfAHI9DnZYwWz8JQi06Tg17I2lHg-4A1XfQ2iux2u56mK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2ZC_vypfSIMXzLksCDDK1W7jgfsEw2uYyOLtZ0nzcbmAnhDIsALgUD3PmQUa4JZJxD7HdPHeEBvCLruXC9CSXbiH2NWheBu15lZ-PyIRiNyQC6lLzEOxwWOrRj1N4OlmwR8Dgg5yud4bCM3OvHJVSBcCy8VibMOk47Eb6MYbsX2spAl6GILif3UFLi-LAUKNLqhs4ig4CgM9clj-D9QkvPYKvdiQzGlxJevyTeBqnUSuqqB-o0Jgsqb7rPfxgr5dOskWKKrMoQ7MKMlZWKbJ6qJ3N9PzqWFfzc-u2Y5qrIwuQhuGJcSfAuiOFHOX8Rgp4kHEl0iHetBMC162GuLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqKwPOD5oCF0yyk0sxoG5f7JdVrKTLMAqSGblUXDhg37KMj92oyZmCGHUOy-GvFY2dZjPqMt66Q7K0gDlW8xOCfyyr8h8rtkh522uBcTpRQ-PZWTEBOBxZo8WrAaChp83ss37SLt38G1iE_pTvY9K66U9kcL1zmb6MADG8zz679zMu-1j9plFMfdk6ZqY55ZJEeBqqIzHNaMR1y-vzV3eS7VhTBpXeo5W9lAQPgP77nLV6WIxcdBtcBr8FOqYJXEJMHJ6QkWFa3OwVlO3L6qrjKtrUj4-UqCoNmMduno25KEMPN2URJqd3DTAtyio5YTvMxBC6xQOdKrQqd5RVeLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyyGDj4GifZgcPHh45SbTf34T_264utDEn41xEJg-dFKamtEJXSiUzkUwbBjoHHDJ8gSlyzJZRnczFuzaTT0C5Tmcig2RpvxTPqGZEZ-Gsx0njh82TdP0JVJGNbzCq1GMhyKgrKS16hiu48iAYdI_I-em1VEVzmDULfAYzStuN20C9YKUjo-u2Q1M3E80cU8O_3LhYryrOZBPUFP3Oig4lNz9A1ddifxzUbc3u78inPdzCqFgD81De9Nd1i_2OYqo_y8r3abK3GbBfjkxKgFmKxTevjG6gFkpsdndQ2IiOpQUp4Y8S0TOTZz7yp18XrFjT956LyqtktH4nKuOXmpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2fpHKtOULJahQFUcNUjSSRpHnMoZ93RLOAWLmdXk2kitv8QPG4DEdB8ERuFdqlckgSw0YbThJssLdVWKus24-36MNph7uRTNuPrVWUg-fiWDfvls5T2pUPDt2mE53W7tSfjVMShgUI2CfInF9yo63CqWoSbqV5j0ZfDfX2V6ECVDq7LFDEi5RB6yyZ-OcS17S27Yc6TXzWp_tMifakrTube5-XwPoDSgc_O3aQTEyVoqTMzCvv_tmVDYGlEKGFeIuCSDmFFzaPFDr6u2PQ9znenltcuw5ZKH3f9ZKNbJaIWQDLpMxM9yj05rw_iEplbXyeSrYI6EHNVD0oAke-Kow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید اعضای تیم ملی ایران از استادیوم سوفای، محل برگزاری دیدار فردا مقابل نیوزیلند
🔹
این دیدار فردا ساعت ۴:۳۰ بامداد برگزار می گردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/659623" target="_blank">📅 08:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5e9cb0d8.mp4?token=FlnP0Fr__purtJE-FxV-H02YN1Ehf_pGnQoC-pUnAQGvHzICKG9TreVkUJ7Xz0pw2GG-G6jVx9XKmvKv3qmaOynyxNT5TQwvDBc0QpxwNdfcOGQx5nrnPxQWiE6ZSfPamMqD7m1QyECShyb-Yyu7vy-Ay9c0Oh6v0MqtEkpYaMKOcOS-8feewMoelz7vLOy7_WOiDcFgfV30-8FeB2PF72nnzWS-g3QBksvFDtce7HtM5Zr-hZHd6wpQzsbTujpJ_hgDhgr4h8_baNTLYhHD92yGJccxGRY8xpseu5vBj2qNB3qdt6jQI0sSGmfyvTU4Eo5h3vQqSpj8GqwEeN2j2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5e9cb0d8.mp4?token=FlnP0Fr__purtJE-FxV-H02YN1Ehf_pGnQoC-pUnAQGvHzICKG9TreVkUJ7Xz0pw2GG-G6jVx9XKmvKv3qmaOynyxNT5TQwvDBc0QpxwNdfcOGQx5nrnPxQWiE6ZSfPamMqD7m1QyECShyb-Yyu7vy-Ay9c0Oh6v0MqtEkpYaMKOcOS-8feewMoelz7vLOy7_WOiDcFgfV30-8FeB2PF72nnzWS-g3QBksvFDtce7HtM5Zr-hZHd6wpQzsbTujpJ_hgDhgr4h8_baNTLYhHD92yGJccxGRY8xpseu5vBj2qNB3qdt6jQI0sSGmfyvTU4Eo5h3vQqSpj8GqwEeN2j2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با روزی ۵ تا ۷ دقیقه سلامتیتو تضمین کن #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/659622" target="_blank">📅 08:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وزیرخارجه پاکستان از تفاهم ایران و آمریکا استقبال کرد
🔹
اسحاق دار، وزیر خارجه پاکستان، با استقبال از تفاهم میان ایران و آمریکا گفت این پیشرفت نشان‌دهنده قدرت دیپلماسی و ترجیح گفت‌وگو بر رویارویی است؛ این توافق می‌تواند پیام اطمینان‌بخشی برای جامعه بین‌المللی و اقتصاد جهانی، به‌ویژه کشورهای در حال توسعه، داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/659621" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqD8L0octp2Z5uXlR6icHzeYzT6y6sxNQGs2Y6WKblwIL_ASvbkGxD6RX-Fla1h60yH63l6yos_EEl-mdrsINfuwTYTfkLKaR93yUOZ6HFyeWHJ6I4M-de95bgaOBkoNtUksYAxiiF0zNXXJK1jRoVmeK5BjHhgIuwZQGrk1U2paD90EIyjwbgnwyYb6l1im_Z7wwF5I46TdI-xq_13hfRp6m1aX10l9E0bPBJtVKSv4wFuSQxddgpwxqimtWENDicZylZyW3qt8D5o9raZDfi2Oo6udKzOa1zuy3cf1-e-kNZmBZbR0aUQhl2GR6g1z1dUQaa7F8AQOT4WtPlou8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی: دنبال شاد کردن همه مردم ایران هستیم
ملی‌پوش فوتبال ایران در نشست خبری قبل از دیدار با نیوزیلند:
🔹
با فوتبال، کشور متمدن ایران را متحدتر می‌کنیم؛ چندین کشور مشکل ویزا و تغییر اردوهای تمرینی داشتند.
🔹
این نوع تنش، شادی و پیام فیفا و مردم ما را که فوتبال، صلح می‌آورد، تضعیف می‌کند.
🔹
این جام جهانی می‌توانست فضای بهتری نسبت به الان فراهم کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/659620" target="_blank">📅 08:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c704aadf.mp4?token=vZfysrl34Pv2aX5XywnpOLEvAFaxE1cxwKTm3_qkDpf63lPh2_rTPTkj1Kqiv0brvnPCLqNoTPtEJCGceW3Kak8Idsf2zJYzl1dk39Xe6TtZxvkaqBGUA75iefFaBk7dYyNp-mRNlLvGReM4_UXpYcyWTpLZffRy-DCM80lNDpitWfUluVQ2YxJsuj2z4JeC3wJD_c8niyiFYbtwu6BTITR87Jg5W4oc8SyS1MojD4YYVfYZf6GTSXkV1GL46f_Emi6PuVCQqzsxB6wboL-eHWAjFgDPO2F6ooa3MMZ4fMrTKm75i_rFN6E2Jxi7bzwtnIDA_PJwbSfvpjyOkjm7XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c704aadf.mp4?token=vZfysrl34Pv2aX5XywnpOLEvAFaxE1cxwKTm3_qkDpf63lPh2_rTPTkj1Kqiv0brvnPCLqNoTPtEJCGceW3Kak8Idsf2zJYzl1dk39Xe6TtZxvkaqBGUA75iefFaBk7dYyNp-mRNlLvGReM4_UXpYcyWTpLZffRy-DCM80lNDpitWfUluVQ2YxJsuj2z4JeC3wJD_c8niyiFYbtwu6BTITR87Jg5W4oc8SyS1MojD4YYVfYZf6GTSXkV1GL46f_Emi6PuVCQqzsxB6wboL-eHWAjFgDPO2F6ooa3MMZ4fMrTKm75i_rFN6E2Jxi7bzwtnIDA_PJwbSfvpjyOkjm7XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌زمان با نورپردازی ورزشگاه مونتری مکزیک، میزبان بازی سوئد و تونس؛ صاعقه آسمان را روشن کرد!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/659619" target="_blank">📅 07:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
حمله رژيم صهیونیستی به یک منزل مسکونی در جنوب لبنان
🔹
خبرگزاری ملی لبنان از حمله هوایی رژیم صهیونیستی به منزل مسکونی در شهرک «الغسانیه» در جنوب لبنان خبر داد.
🔹
بر اساس این گزارش در این حمله دو شهروند لبنانی به شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/659618" target="_blank">📅 07:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAtQTNOUZ7ojN0idOZkPRLMsEvPCkf8ssMpYRl0f-s4pz0iP7BZzBh8kuK7cj_q_e_WBl9wyUnLovL7wigwFd3qcBGig6uS3W78-dptyMvqGGmor4kQmN4I57FuyEgvT_P1TGonFaNepBWSrw8V4ZPwSEAcO9OgjAh8PRGjjnX9pQ4B28H_CRm_H5ocbEkAF-n-lRqHC59MEudncckm7TLtoON-bXLk5PBuKtPk1ucow5ICmCjwbPmQJKGzzVA0XtFZyO6yyINBrk0mprPvkejL9ks-n9FTkYSiFdEnpbHwnEfjZdAPiLzjGGdH4APyMIXJOfQ_W_1UmoqEuCFLRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bImdUXc-a_n0nKGHcwBVQM2PxB_U80BuLq8wU9HuB-6rN1aJi6KMjqu-K3pH5HMlVU0e_R2e6TJTtzFm6pB9T6sSEk_A3tJfLwY1e0BNxm2C4J165FsE4JxkELXNVcRR6Smj8wUNw5OXQVg9wQ2B-zdsXdEjUhoe3T2nJDvFkZ4dazSiA0b31WrbpqTJvr8OdsEFm7g0EmlE6lgizzUAFo8MHkJ4luoQYOR4HWz6_J-QTxfiXVMt8GQ_Ujye7JDtl-iUHqiKg5axgIMkkCIw7flCVZ4jzK4rHm09VgPHQny6HIhl7WdgllrQm5gBihm35ooDtMCITNsXJp2tYeApng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدول گروه E و F جام جهانی ۲۰۲۶ پس از پایان دور اول
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/659616" target="_blank">📅 07:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267d498b0b.mp4?token=kegWhiBCOyPMrt1DA0rduNcMndLO6oof4Q3trO8BGh3oL4nT8bMiz8GZ-roZOw4IB5QQJK5BzsCYXpHTxrixQW4yH58BcwSfuRHEfhF43TSvGqrw6aAIXx53ZENKMqhn-j1OI-xT2CqQjEzWJiC8yI3PWHedT85JHf5CrQbOyX__0zpA-JxQz7_QpJcVIaE6IGw9Yi_vN7Jd6o4FbO_MWv-tscI3r0yU1ZzsPIhRsSYB2iV7BwTX_hT-XVDwqT0esUjunLzsw1mG73rg81ZcExNWMXES73WNgViCMPhsNWkB0IWc9WcM7gNVZ4dY0_nTRL2famlTimWVA-3gmCpEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267d498b0b.mp4?token=kegWhiBCOyPMrt1DA0rduNcMndLO6oof4Q3trO8BGh3oL4nT8bMiz8GZ-roZOw4IB5QQJK5BzsCYXpHTxrixQW4yH58BcwSfuRHEfhF43TSvGqrw6aAIXx53ZENKMqhn-j1OI-xT2CqQjEzWJiC8yI3PWHedT85JHf5CrQbOyX__0zpA-JxQz7_QpJcVIaE6IGw9Yi_vN7Jd6o4FbO_MWv-tscI3r0yU1ZzsPIhRsSYB2iV7BwTX_hT-XVDwqT0esUjunLzsw1mG73rg81ZcExNWMXES73WNgViCMPhsNWkB0IWc9WcM7gNVZ4dY0_nTRL2famlTimWVA-3gmCpEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساکنان منطقه نبطیه در جنوب لبنان پس از توافق و اعلام آتش‌بس، به خانه‌های خود بازگشتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/659615" target="_blank">📅 07:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد
🔹
بر اساس اعلام وزارت رفاه، اعتبار کالابرگ این دوره تا پایان تیرماه قابل استفاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/659614" target="_blank">📅 07:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIHuRVm_c-vOwJ9DIOnkUc6-OgNlCOOt6xX3-6fTnRUwOnsRDcM4eg_-TvO3YAjKQBaq2Dp8ISh8uCkMgDQ9XRGD3fEwcTCrAfZ1kr1Wy6GlMu12v1KBM2K7jyAfLl0Pm3hpcmAD0i-J76Y1owq2bWe36cHHiFaBmzmpYJRGSts2SRq-XYj37MwM185Cp0GfMXkNfEza0snxHeEGYlI8iwLm5sbVj13m_NehbjVMa6nsQOdxSUadEyiQRmKe-qo7SPjXtPsfNt2BOLV6GRlL7sqYGGs4_yZHtiO_UhqwCQkLmQA9lih_C1mcuyvfvVnE9ZbZwsHYjlqrmpCilAQgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۵ خرداد ماه
۲۹ ذی‌الحجه ‌‌۱۴۴۷
۱۵ ژوئن ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/659613" target="_blank">📅 07:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔶
فراخوان کمک برای یک بانوی مبتلا به سرطان
🔸
خانمی جوان مبتلا به سرطان سینه از یک خانواده نیازمند دارای همسری کارگر و مستاجر می باشد که تاکنون۹۰ میلیون بابت درمان  هزینه کرده است.
🔸
برای ادامه درمان و انجام شش جلسه شیمی درمانی نیازمند ۳۶ میلیون تومان است
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/659612" target="_blank">📅 04:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJeEpwXyTC8m6BffvWxx3P9LbgGF22bTO7VSrV7ddGQ2H0j93tmfL8dbFbkaeC7KzKFUdqNgwhU7NJBS-9gcNOsaFLM9ys6bk8z_UbPNWamv7Aii23l9ii1FRn7MPBYaaAjRitSoaa-Y4C_IhsIOZ9UithC5_KAUKNkSUr0RAFrDYSHucPdz8psL2q4nit644_lwD7X56JpRz6YwQrLdZphQFkBJ6CTv4-zhj06XZnE1Lh5ddS83yY2YzWqdUPOwjLjnb70sXNmqere1uw9odIw6DQhX0hwjYZ32v0YY66e0XfzjjzcN9ZbnP7Cfsitm_XC0rmWyOQlBmSeBf3HMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: فاذا فرغت فانصب. هیچ وقت هم نباید خسته بشویم. شنیدید آیه‌ی قرآن را «فاذا فرغت فانصب»؛ وقتی از کار فراغت پیدا کردی، یعنی کارت تمام شد، تازه قامت راست کن، یعنی شروع کن به کار بعدی؛ توقف وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/659611" target="_blank">📅 04:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659605">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f03eff7c.mp4?token=eI-hAKMivYpoNuD7SFhPdwDUGd_lLouA0l_sM2BRbxlLNXPF69a0o92OHLpBxYauXuJuN9nYGPJactI4SShATOb2D8QIvpk07FnMPhHfg-AxjrB1xYccQdvA1g53ItwS4dM_u18Qt-q8DuCmxYTlEWsrgKDrE5ObpHtyIqwAqUTqtaL-pqCjlN33EuFZRKFgw0jUhKgi45f-iL9oztRPV-rr667-887kh4Lnk3Xxlq-Bmoz7foNgVNX3kPLuW_KHLuqCdgU1BtPmrws-lS68LzDshgtbImS94jMxYwe5IQNiEprTJ3h-LnhufXr9WURpcG4VCxRw1kumb8OmWsvxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f03eff7c.mp4?token=eI-hAKMivYpoNuD7SFhPdwDUGd_lLouA0l_sM2BRbxlLNXPF69a0o92OHLpBxYauXuJuN9nYGPJactI4SShATOb2D8QIvpk07FnMPhHfg-AxjrB1xYccQdvA1g53ItwS4dM_u18Qt-q8DuCmxYTlEWsrgKDrE5ObpHtyIqwAqUTqtaL-pqCjlN33EuFZRKFgw0jUhKgi45f-iL9oztRPV-rr667-887kh4Lnk3Xxlq-Bmoz7foNgVNX3kPLuW_KHLuqCdgU1BtPmrws-lS68LzDshgtbImS94jMxYwe5IQNiEprTJ3h-LnhufXr9WURpcG4VCxRw1kumb8OmWsvxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب توافق ایران و آمریکا در رسانه‌های جهانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/659605" target="_blank">📅 03:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pIlQVsTsiJFy5-31Lqhz58fT-QpSgWahdmTzKBZ8Z-OEOFREoL5o4FXCWraOolYQJJz6affxC1QZRyKw-NPuK6mPpGUUi-9jvaKOJWC_cTEsEcre_ULnu6_AjDjpgwKH1w_8O0WSWAsYrj16YNOPT_VryQZiNWyz95udCcx-s2NedIRWoRAkvhhRzc1__8RONdB6dzJpzm_ugwNSUJX1lO5PO0JUeUxPB3uG4UTwO8s9r5F5mWdi9BFFlOAdNVVKA3-Ksg_dm2CWaQK0it9dpVRKGcTuhQrZdGZUXxxW1b7UovUP2cHr2oNy_DgI6Bc8DHbc1m2jNfXFHkJk7iplyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فیدان به یادداشت تفاهم ایران و آمریکا
وزیر امور خارجه ترکیه:
🔹
از توافق میان ایالات متحده و ایران استقبال می‌کنیم و آن را گامی به سوی صلحی پایدار در منطقه می‌دانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/659603" target="_blank">📅 03:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هیات قطری پس از ۱۷ ساعت مذاکرات فشرده، ساعاتی پیش تهران را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659602" target="_blank">📅 03:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
خبرنگار المیادین: رژیم صهیونسیتی با حمله توپخانه‌ای، شهر النبطیه و شهرک کفرمان در جنوب لبنان را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/659601" target="_blank">📅 03:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a44d4e47d.mp4?token=YVjjx6PTxXPxd3xmObooYgc4ruPppMH4p1DK317FPTYJ0fBekktnWKYUQg0vv7JgggPUkbB2VffYrgEnXRatmV-bofQYtBbGM8aHJYn-18oQSblDUn2j7bKjtJb9Itu__F8YHtL8b6g--vhXtN4fO8ZpFEKLkfYtybCV2It1QHPyYHhyfPs5Tnx-LS0LBerqmXu8EVZZ6soub2rlBhwiV0i5gMEJTjh9m2Y1XSVQtX4ejiDbi7normTHZxHSVcQjpCYN8nmuq9thtiYxTR-4Blw2-NiysVDw4Ak6dXZTHnoZFij4zV0EGX_QYiBlpwFL7U_6t09NAdKl8lAjpLN-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a44d4e47d.mp4?token=YVjjx6PTxXPxd3xmObooYgc4ruPppMH4p1DK317FPTYJ0fBekktnWKYUQg0vv7JgggPUkbB2VffYrgEnXRatmV-bofQYtBbGM8aHJYn-18oQSblDUn2j7bKjtJb9Itu__F8YHtL8b6g--vhXtN4fO8ZpFEKLkfYtybCV2It1QHPyYHhyfPs5Tnx-LS0LBerqmXu8EVZZ6soub2rlBhwiV0i5gMEJTjh9m2Y1XSVQtX4ejiDbi7normTHZxHSVcQjpCYN8nmuq9thtiYxTR-4Blw2-NiysVDw4Ak6dXZTHnoZFij4zV0EGX_QYiBlpwFL7U_6t09NAdKl8lAjpLN-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود اتوبوس تیم ملی فوتبال ایران به هتل محل اقامت در لس‌آنجلس با تدابیر امنیتی ویژه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/659600" target="_blank">📅 03:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سعید آجورلو عضو تیم رسانه‌ای هیئت مذاکراتی ایران: به دلیل بدعهدی طرف مقابل، با یک تفاهم چندمرحله‌ای روبه‌رو هستیم تا گام به گام پیش برویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/659598" target="_blank">📅 03:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به عنوان نگهبان منطقه قرار خواهم داد
🔹
حملات اسرائیل تقریباً توافق نهایی با تهران را از مسیر خود خارج کرد.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/659597" target="_blank">📅 03:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نیش ترامپ به نتانیاهو: او باید از ما سپاسگزار باشد!  ادعای ترامپ در گفتگو با نیویورک‌تایمز:
🔹
تصمیم برای حمله به ایران در اواخر فوریه و اعمال محاصره دریایی، بعداً خاورمیانه را به نفع منافع آمریکا تغییر شکل داد.
🔹
کنار آمدن با نتانیاهو فوق‌العاده دشوار است…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/659596" target="_blank">📅 03:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: توافق با ایران در نهایت تضمین می‌کند که تنگه هرمز برای همیشه بدون عوارض باقی بماند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/659595" target="_blank">📅 03:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw0sRVnpkT-ZvRqBguhUrDAsQsbA9aqDEUeQpytgqlRG2AueIlOBODcQsoz1OgFXGnqAVq344zsjFlzetsDfMQ_SGXF4Vf2PqWQLcaA0eAqiT5ugGVc6am3yyiEmR0KTgLJJotSzVGwFI_W8GhiTPGBV7nIi0s1PSZKC-LqNTd8dUCs0Ac9zdNnnPd-zcUWnU_5FsmO8XlbUN1sc68yScOGpJ601tT-pW702g-D9lNfye8COnM4fyu4yUu_OGCZ49NWiqlUrfnuviq1rtrQ5DVxerdASEo8RtMLxuKIQ8q2UnvAU54mLl7vOBP2b3zWVQGK4FOxOPN29o0mhdq_4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: تفاهم احتمالاً منطقه را به وضعیت پیش از جنگ بازمی‌گرداند؛ اما با این تفاوت که ایران اکنون با توانایی خود در تأثیرگذاری بر کشتیرانی تنگهٔ هرمز، به اهرم فشار جدیدی دست یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/659594" target="_blank">📅 03:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTGbWxjCgrT7VyVYbZ0psArBieCOZZF6cATkCdaClLW0fOfth6fpQyOlkZm1p208CZ8BLRmUlRC3-3KJ7I6dedWFiT_nqdMtG9A9WqVoJxqkrPUF-_4YQWYIuT0wDmTW6HYhQbFtP2ouuARGRPNacNs3cYB8MaNleHbXK_Exw7ryyeFs0rlwcAfz8T2AUfYTuilmUkYCYDAbr4zplawlEmy8ttPh-pnhxIsfuvfXrdKmtP4VuFYyH-Y_H5IzuIOGPiWxTmtH6-J_38BEEYFAuM2EmO3-9CzyEIURlul2FbndUBPRw81NSuz3C_87ECtvH8inuzyb0a62OUz-rAoRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندسی گراهام: از شنیدن توافق با ایران برای باز شدن تنگه هرمز خوشحالم
🔹
طبق قانون ما، هرگونه توافق هسته‌ای با ایران برای بررسی و رأی‌گیری به کنگره ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/659593" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: توافق با ایران در نهایت تضمین می‌کند که تنگه هرمز برای همیشه بدون عوارض باقی بماند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659592" target="_blank">📅 02:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
غریب‌آبادی: دو اقدام فوری از همین لحظه
معاون وزیر خارجه:
🔹
دو اتفاق فوری از بامداد امروز رخ می‌دهد؛ اول پایان جنگ در تمام جبهه‌ها از جمله لبنان و دوم، رفع محاصره دریایی./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659591" target="_blank">📅 02:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ماجرای تغییرات لحظه آخری یادداشت تفاهم ایران و آمریکا چه بود؟
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
پس از آنکه روز شنبه کلیات  یادداشت تفاهم در شورای عالی امنیت ملی تصویب شد، از صبح یکشنبه با ورود تیم قطری، برخی مسائل باقی‌مانده مورد بحث قرار گرفت. به نظر می‌رسید که این مسائل لاینحل بمانند تا اینکه حوالی ظهر امروز، اسرائیل به منطقه «ضاحیه» حمله کرد و عملاً از خطوط قرمزی که ایران تعیین کرده بود عبور نمود.
🔹
در این لحظه، ایران آماده می‌شد که از چند جبهه، حملات گسترده‌ای را به سمت رژیم صهیونیستی آغاز کند و مذاکره به سمت تعطیلی پیش می رفت. اما با ورود مجدد ترامپ و امتیازهایی که در ازای عدم حمله ایران به اسرائیل ارائه شد، تیم مذاکره کننده قانع شد که این توافق در راستای منافع کشور و منافع مردم لبنان است.
مهم‌ترین تغییرات لحظه آخر عبارت بودند از:
🔹
برداشته شدن فوری محاصره دریایی (به جای بازه ۳۰ روزه که قبلاً توافق شده بود)
🔹
پایان جنگ و عملیات نظامی در همه جبهه ها و همه مناطق لبنان و ضرورت احترام به تمامیت ارضی این کشور
🔹
نهایتاً این رایزنی‌ها تا ساعات پایانی شب یکشنبه ادامه داشت. در حالی که همه چیز برای حمله به اسرائیل آماده بود، با تمکین آمریکا در برابر خواسته‌های ایران، عملاً موانع امضای یادداشت تفاهم برداشته شد و قرار شد روز جمعه این یادداشت تفاهم امضا شود./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/659590" target="_blank">📅 02:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نشست خبری سرمربی تیم ملی فوتبال ایران و مهدی طارمی
امیر قلعه‌نویی ایران:
🔹
خیلی خوشحالم از کشور بزرگ و قدرتمند ایران اینجا حضور دارم و امیدوارم فوتبال وسیله‌ای شود که کشورها و فرهنگ‌ها به هم نزدیک شود و خوشحالم که از طرف کشور و قدرتمند ایران اینجا حضور دارم.
🔹
ما اینجا هستیم که به نمایندگی ملت بزرگ ایران بازی کنیم. فقط به فوتبال فکر می‌کنیم. ما سیاستمدار نیستیم و فوتبال از سیاست جداست ولی همه ملت بزرگ ایران برای ما قابل احترام هستند.
🔹
بخاطر مشکلات کمپ ما دو بار جا به جا شد اما جا دارد از مردم و دولت مکزیک تشکر کنیم. ما ایرانیان از سختی‌ها فرصت درست می‌کنیم. به غیر از شادی مردم کشورمان به چیز دیگری فکر نمی‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/659589" target="_blank">📅 02:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
مذاکرات نهایی با اجرای کدام بندهای تفاهم‌نامه شروع می‌شود؟
منبع مطلع:
🔹
بر اساس بند سیزدهم تفاهمنامه، مذاکرات برای توافق نهایی پس از امضای تفاهم‌نامه و راستی آزمایی اجرای بندهای مربوط به رفع محاصره دریایی، شروع روند بازگشایی تنگه هرمز، آزادسازی بخشی از اموال ایران و اسقاط تحریم‌های ایران در حوزه فروش نفت، پتروشیمی و مشتقات، آغاز می‌شود./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659588" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بیانیه مشترک رهبران بریتانیا، فرانسه، آلمان و ایتالیا: ما از یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و به همه میانجیگران، از جمله قطر و پاکستان، تبریک می‌گوییم
🔹
ما آمادگی داریم در پاسخ به گام‌های واضح و قابل‌راستی‌آزمایی ایران در مورد برنامه هسته‌ای‌اش، تحریم‌های مرتبط را لغو کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659586" target="_blank">📅 02:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
یک نکته مهم از اصلاحیه ترامپ با فشار ایران؛ بازگشایی محاصره دریایی آغاز شد؛ بازگشایی تنگه بعد از جمعه
🔹
ترامپ، ابتدا در پیام خود در شبکه‌های اجتماعی نوشته بود که از این لحظه هم محاصره دریایی ایران پایان می‌یابد و هم تنگه هرمز بازگشایی خواهد شد.
🔹
با این حال او دقایقی بعد با تاکید و فشار ایران، سخن قبلی خود را اصلاح و تاکید کرد که بازگشایی تنگه هرمز بعد از روز جمعه (روز امضا) انجام خواهد شد. او در پیام خود چیزی درباره تعلیق بازگشایی محاصره دریایی نکرده است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/659585" target="_blank">📅 02:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
برخی محورهای مهم بیانیه شورای عالی امنیت ملی درباره تفاهمنامه ایران و آمریکا
🔹
شورایعالی امنیت ملی، یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان می‌یابد
🔹
محاصره دریایی ایران بلافاصله به طور کامل خاتمه می‌یابد
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659584" target="_blank">📅 02:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
فوری/ بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔹
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/659583" target="_blank">📅 02:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf836a8c5.mp4?token=VMtP_b_P_gt70GDDoIt-44wEIj2TTAecDQIry_wamfT21LZeKoo5Vg1k2G7D0VTJOi6Nm2zJUBtXTGCIbxAWRgWZMvykQCDLZiXQXjLf5UscbsuGMtGgK1OTx1E0FRrlj12iG6g_h7Yxi_vh_ph531Xh3StVe6KO-rYPr2yMH-fgBnIyGrOGB-U0zjaHyg1kXG7I1mGU7xYfQHHDHEbYjWklYFraqu5lb0IdeRJTJKDKWaQcfGeYEpPXOiax1PUA-AC3N4o_yG1FsLmzdRFXyq5t6-GfawZgiJBlI6qw_OSN7A_s1O6-xOegC407pQqZbsQ_jRNdjJiLxAk5zTjgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf836a8c5.mp4?token=VMtP_b_P_gt70GDDoIt-44wEIj2TTAecDQIry_wamfT21LZeKoo5Vg1k2G7D0VTJOi6Nm2zJUBtXTGCIbxAWRgWZMvykQCDLZiXQXjLf5UscbsuGMtGgK1OTx1E0FRrlj12iG6g_h7Yxi_vh_ph531Xh3StVe6KO-rYPr2yMH-fgBnIyGrOGB-U0zjaHyg1kXG7I1mGU7xYfQHHDHEbYjWklYFraqu5lb0IdeRJTJKDKWaQcfGeYEpPXOiax1PUA-AC3N4o_yG1FsLmzdRFXyq5t6-GfawZgiJBlI6qw_OSN7A_s1O6-xOegC407pQqZbsQ_jRNdjJiLxAk5zTjgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن و پایکوبی در خیابان‌های لبنان پس از اعلام توافق ایران و آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/659582" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: تا زمانی که ایران به تعهدات خود پایبند باشد، از مزایای واقعی بهره‌مند خواهد شد. اگر ایرانی‌ها به این توافق پایبند بمانند، این توافق خاورمیانه را طی ۵۰ سال آینده اساساً متحول خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659581" target="_blank">📅 02:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCq_3gUk1052F5-lxBdHvXY65aWzW1R3otE1FkbMx38nDumRz4MsbSSv_TGyPr2mYypXjvA1iX6I4Gf3R5lwqSbnrn5myvGO0xE-ZAGjkUAn8PeLTd9wgnPilZm9xHGAruzVbgPIvo1y8Kx2802QSkOBRQ7hBp8Xhgzp0Qt4MgdxYTWHdNqlMr065j7l3vXf3dMqSpFX-Ix-nl7SfGJPSLxlxvJD79cuP2I-o39WSVxjC0k3i6tsrFbkrTd9SWssZVvl9i9VEXa98CcJbiDZbhMyhp3jIh13VQD7JE1mLYqazypkTOAF9q-G-3OCS__NhhwsXQZ9KACi7BYDd0gcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باوجود تکذیب‌های پیاپی رسمی آمریکایی‌ها؛ نخستین محموله ۳ میلیارد دلاری وارد تهران شده است
🔹
براساس اخبار دریافتی، یک فروند هواپیمای اختصاصی اماراتی در روزهای اخیر با عبور از محدودیت‌های پروازی منطقه، در فرودگاه مهرآباد تهران به زمین نشست. این پرواز حامل نخستین محموله ۳ میلیارد دلاری از دارایی‌های ارزی ایران بوده است.
🔹
تصاویر راداری تایید می‌کند یک فروند بوئینگ ۷۳۷-۷JZ BBJ اماراتی (با رجیستر A۶-RJF) روز دوشنبه ۸ ژوئن (۱۸خرداد) پرواز مستقیمی را از ابوظبی به مقصد تهران انجام داده است.
🔹
طبق گزارش منابع موثق منطقه‌ای و بین‌المللی، این اقدام در راستای اجرای توافق مالی جدید میان تهران و ابوظبی برای حفظ ثبات اقتصادی منطقه صورت می‌گیرد.
🔹
با وجود تکذیب‌های پیاپی رسمی آمریکایی‌ها بر اساس بخشی از این مذاکرات، امارات متعهد به آزادسازی ۱۰ تا ۲۰ میلیارد دلار از منابع مالی ایران شده است که محموله ۳ میلیارد دلاری اخیر، بخش اول این تفاهم به شمار می‌رود. این اقدام نشان‌دهنده دست برتر ایران در اجرای گام‌های اولیه توافق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/659580" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
خشم رسانه‌های عبری از اعلام یادداشت تفاهم بین ایران و آمریکا
🔹
کانال ۱۴ عبری: کاری که دونالد ترامپ با ما کرد آنقدر بد است که حتی توضیحش هم سخت است.
🔹
شبکه عبری آی ۲۴ نیوز: ترامپ به ایرانی‌ها خیلی چیزها می‌دهد و در عوض هیچ چیزی دریافت نمی‌کند.
🔹
دیگر پلتفرم‌های عبری: به نظر می‌رسد این توافق شامل خروج از لبنان باشد.
🔹
خبرنگار رؤی کایس: چه کسی باور می‌کرد که یک حمله واحد در ضاحیه جنوبی بیروت، صلح جهانی را تسریع کند؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659579" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUrD1T8aKGE40ZugGdcHpj_UMDGPdUYJCA_gPOAaTFB6Jpukf4y_0_p65g_3jac5NBuBxwr_GKjS5tIe9y85n3dbPPDkEBJ-6GRNJX5xF5dGDQb4USg32O3GwjWbb6yD8Ps8H8wSlwh-dvh34vFM2WnVEmpaA9RmZsZhde1ixyls5RWSXXY3aI-Kbb845AMeLgizRuMETCu2_2-rSr67iGSzmpdGQm6ZyqJty25-r9eNgqFJ8nVK6LsK_b4-MUx_vFNq3XKWtRRoJ-diq9jMpKsWuRaWI66kUZk7Zp2hcA7CjEi7hFpj6PqJqn0-10fgpZ_tR52djBWL_E9M_NmxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei2-ivQJ95DBbcOfIG54vaIqpNg1uzjiN6FONbZakLqf1PVgrMV2g2W-DmTKJ6zL9HwZmcWlStj2cYGVpTGF5wuYcwFILeHTep4Tg-nxDCw2cm0TZhGrelSxCIRvds6fDwJ82W1NB6TTdivlVwXh4hWDjj5Gw5_D7b2pes78Q9j519XI4phESx_YtXB3qIg3eD9FCGT_C36veTwVlvRUmyLOBRukSFbNJwmoFrto9Q5HXuJ7DQGTGOBUjWXMvg9V-Zr7DD3Q6J5MY73eDM0Qhi54JBvjugRiLN4KXoMm4-w9fZzQknWk8ucq5bgaUXL-tQhFvy9fHg9qQXKLwlFmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMylVMOumttWYj8Zg48hp5Ql0XBdzhYv0yi4bT9Du3YZfIKWVElDVEgtID2zsK7Rx-o8m4TA8TYrEbniPdhsE8tVpsQ1abJxqtfFjEb_Q-_58jUjNBxIRlrh0778giCoVpD91o_SnKpHiWCORfuh-jVOn6Ij6A3KHWW7A5GF6MXPUPbGMsf3aIgewAZjKB0MwBfnSDaukon002VJdG_Ks5BVTTEBNgmWKK6-gIxZCgEZBq52CHproVd7mB5x8Nj9wEtiWF6mkg99kyXDD2M819BvJSDfFJO206mI7diRfXu36hvDBoOMy0pZwJ4IzF-v6HKmUeZTOjdghijaaE1ArQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش بورس‌های آمریکا، اروپا و آسیا به اخبار توافق/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659576" target="_blank">📅 02:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659574">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
جزئیاتی از یادداشت تفاهم ایران و آمریکا
🔹
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
🔹
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
🔹
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
🔹
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
🔹
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
🔹
براساس جزئیات این تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را در تاریخ بعدی دریافت خواهد کرد./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/659574" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
یک منبع آگاه: بازگشایی تنگه هرمز، پس از روز جمعه و امضای تفاهم آغاز خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659573" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
یک منبع آگاه: بازگشایی تنگه هرمز، پس از روز جمعه و امضای تفاهم آغاز خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659572" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPxAWUJnPY6fy8_RaE3BcbaNqRiMdvJWpHxHN18UO01JxyRCmwvQmG-_gbMWk0nYoreAJa6H486eWYordAHEGhfOHUuhx4uZUOn6rUz8NvB6pje9DUR0KhmhA9WuEN1naIKnsXGAZaKWaWqqdC3SYaRHyAzWkPlI3b3QRVOrmTgkhFEBIASaBd5JCD5uSrF7oWDTy3cnoc1Nt0t9fxfF9RVLo5_aMk2urJ86Hon2xOtM9RFadVUA-pyRUVQ7hZyGWA0y_lVFQ-OPx-hZB-Iqhzit89DyIAN21tuhN36TBP9XO1Cz7EVyULpZb2JNoYOFoCSlZSHN74UL4B42T8Q2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والله که از خون رهبرمان نمی‌گذریم
🚩
‏⁦
#WillPayThePrice
⁩
‏⁧
#تقاص_خواهید_داد
⁩
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/659571" target="_blank">📅 02:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659570">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2jA8OmYO3Mwl3foFylbCiYNgo-rV5yp9PONilunfiLKdMUK2e56a9AeFKAbS8pkLJgdu2-LAzhnp04ZUG_2ZBfZC8y4oWXocND7RSPqk2JzMfhMlH2qp2ieUfXQlB5ihykLMiI4Hf0dhrrowlvC8C7QDjFPB8qWb0SMQqZNkNrqc4p1GWT--43QDOo6cR0dvD6KO35UbIiCgA4OXvgVgV1qGK4l2eC6Svp75wkWYr4_IC8psEUvFBSfndAYRYrnz8ZnDs5Vcty0D4_GGRcrXHnoRtm0ftZPC5u7fXDpmyYWMSpemWFC8zzODo59G0VyQa_hfmyxiPB6LdTn9Nz-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
🔹
رؤسای جمهور بسیاری تلاش کردند با ایران به صلح دست یابند، اما همگی پیش از من شکست خوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659570" target="_blank">📅 02:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای معاریو: نتانیاهو به ترامپ گفت که اسرائیل خود را ملزم به رعایت بخش مربوط به لبنان در توافق پیشنهادی آمریکا و ایران نمی‌داند
🔹
بر اساس منابع اسرائیلی، اسرائیل قصد دارد نیروهای خود را در لبنان نگه دارد، عملیات علیه حزب‌الله را ادامه دهد و در صورت نیاز به حملات پاسخ دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659569" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGpF4RZACujGsEHeSyJZVFG0YjlNIRpzlIgT3aA4gfLekE6uCNzcM-Jo9OzUEpGAQ1J8KLm0qSpumpSmid2HCqPWxRRJvj1KF3Oeajz5yStHRu_pZIJCmKEmb2VlvmtUwJBPKHGxTQopciLAfEdljHATLHm1cSirJ3yAdyd7dfjl0LUjzog6EjXzqrcw6KMbnRhHmLdNK7GRBeuYMSPlLhXtu67aCfqqNkRmWdnuHkUqL66SGZ1BiumsZucwcVz4qNGTaMtpD-JFubqrsWxAeijkMA_pZ10MDr2wNVbgKkLd9_OWYYZAaO0SSLev4KbxsFw7xDAwFBAfqxpW_A-p3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر مرندی:
۱) حماقت نتانیاهو بن‌بستِ مذاکرات را شکست. برخلاف برخی گمانه‌زنی‌ها، تا پیش از حمله جنایتکارانه او هیچ متن نهایی‌ای وجود نداشت. این حمله بود که ترامپ را وادار کرد خواسته‌های ایران، به‌ویژه در مورد لبنان، را بپذیرد.
۲) حماقت نتانیاهو نتیجه معکوس داد. این یک عقب‌نشینی تاریخی از سوی «امپراتوری شر» است. هرگونه نقض توافق با پاسخی سخت و قاطع از سوی ایران و محور مقاومت مواجه خواهد شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/659568" target="_blank">📅 01:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-h5n6Y5tMyv657DOW2lf92nfjmsCZbmvCsep6sKyprCaJj1T27GRoYDmZPiGhrWNUN6FSLevHclTx5AmJp9WjbbYoFS3mIm_nWPZDJwDTnbeKwzEaFytXkbILHt4OIvvQsHxUjLsvPlgbxWmgfwrWhZzSWjIuelIw2DMoBNL_lUxcbEaZZ_6ji35OntMVj76lWHG690TT_1h2A1cV7Ge0Zi_3mkDoeZOuBRAHnFKn5GInbs6tH_OZ2iAFdHaF7cExIPMKvXWkFmF6yP5MilCC55tMR1tva6Hd19ZyTq4AzqWso7oY97mAJb2QWhGt1Nn0Aa671wmnbyeSmJc91V2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صعود ۱.۱۳٪ ارزش بازار کریپتو و رسیدن به عدد ۲.۲تریلیون دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659567" target="_blank">📅 01:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
/صبح نو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659566" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قرارگاه خاتم: مردم و نیروهای مسلح ایران ثابت کردند که دشمن راهی جز پذیرش شکست و تسلیم ندارد
🔹
مردم مقاوم و سربلند ایران و فرزندان دلاور و شجاع ملت در نیروهای مسلح مقتدر کشور و جبهه مقاومت با عنایت پروردگار متعال و تحت تابعیت فرمانده معظم کل قوا مدظله العالی با تحمیل اراده الهی و پولادین خود به دشمنان زبون آمریکایی و صهیونیستی با قدرت ثابت کردند که راهی جز پذیرش شکست و تسلیم در برابر مردم مبعوث شده و جنود پروردگار متعال ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659565" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMLBX1nL-YZ47SxvkNnRZw_TL_HXURC3sxHzeH_HyScxsLc-qjDXKKnzsh2UmBBCD2jITl2qnbtPkX2gz6i5C-82MAkmNAFF7NMh0wXJmfjKRM3cAT_E2F0JCltn6ZtMNLmMAAi8NFQnnUYz14iKHuNL5vOwSe5bEkp74_sEJV3tCgiss04vTD5MxJT8ileIqR8Fy4xfpRs6rGfdVfQtCRecU7pIDcGkQqc_JmQodZUN_eT_5vSbTUUlMg0K9nTPCSWSk8oapX_1WiYCklAvm09xDzwfJolfs4-zirphGoQWUGHMdwIKnDkKAhnE5KV6V25gI07iRJiVVz2yWOiXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۱.۹۴٪ اونس جهانی طلا پس از خبرهای توافق ایران و آمریکا و رسیدن به عدد ۴٬۳۰۱٫۲۶ دلار/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659564" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
