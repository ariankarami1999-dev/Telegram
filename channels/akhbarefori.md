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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-657232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZlDezO1L0otqDNVHc4x6_91VcKA2q1zcn12s8qYCJxpwf-ksckyRRJGUW6nRVpRS1tnrTUqyeWEMub0Dl43mCTrN9B_jlBiPhsVeic8tG4HK6bqJ6ZxG2nCOXHc5hgCiOIE5GVuXKJC-j-QUPSOaq65dV63MMwu3WBkIIT-QO4KiWQUkxyO-BfCDi8l_GXLTNe5wRrREYmKCmdgtxIizlXxAivOEhH3G-1IKzyqbOHXshnVk7miL1kRjkQHn8NshUn5U1RWO6SekYU5tijU83TBTy1UIx1hRBlLsGVbgKes96kn8v3y_rAFRJorSlgTU6M7opG3xHNywTtmAYytrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از بقایای موشک‌های شلیک شده به سمت اسرائیل در محله‌ای در شرق اورشلیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/657232" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: رئیس ستاد ارتش از دیشب سه بار با فرمانده ستاد مرکزی ارتش آمریکا گفتگو کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/akhbarefori/657231" target="_blank">📅 09:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKwiNSDmUy7_rGF3SNd7bZt6ellfxC2Wq3GeH8m_oYGY41XWXOeOwsU5LZZM8xXhuiPiBgKi5QNXXyZVSbUTqybJGlv1ZqvF76HjpMT40bBdA_6mhwA7BNHohdJUDs9h_eh8iYr05byaxRCb3r7VyNabMiTaoEIUAopDILc67rGh3cYLKSZPnUbG7DXk8y3X6PJOYUlF3tRf_7KI0Tw8Hyl_aZVm1VVUGS_CeExDsEYbIXiq7YxTfgIkB8EULjOZ0NZabNMM0pbETn9FlIBn55QmBAzNesw_pKfe9eHmd7zbm-scudpvzdxX3DF2G6c43fXIT0zgooyoc5pSWeJDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندوزی: جریان ارتجاع، بزرگترین فرصت سوز تاریخ ایران است!
احسان خاندوزی، وزیر اقتصاد شهید رییسی در
#گفتگو
با خبرفوری:
🔹
مردم ایران عزیزتر از جان، در این ۱۰۰ روز نشان داده‌اند که روح تازه‌ای در حیات جمعی دمیده شده است. مردم خواهان نقش جدیدی برای خود در اداره جمهوری اسلامی هستند و خواهان رفتارهای متفاوتی از سیاستگذاران در دولت، مجلس، قوه قضاییه و سایر ارکان حاکمیت. اما ظاهراً جریانی در کشور ما وجود دارد که همچنان دلبسته روزهای پیش از بعثت مردم است، اساساً بعثت مردم را مانعی می‌بیند برای استمرار گذشته خود.
🔹
"ارتجاع" یعنی عقب‌گرد به پیش از نقطه عطف یک جامعه و در سال ۱۴۰۵ مرتجع یعنی کسی که می‌خواهد ریل جامعه به همان ریل پیش از بعثت مردم بازگردد.
🔹
اگر بپذیریم که مهم‌ترین دستاورد خون رهبر شهیدمان نه فقط به دست آوردن فتح در میدان نبرد نظامی و در اختیار گرفتن تنگه هرمز بلکه همین بعثت مردم بوده، آنگاه مرتجع کسی است که می‌خواهد موج خیزش مردم را به موج مرده پیش از بعثت بازگرداند.
🔹
امروز جبهه‌بندی‌های خودساخته پیشین مانند چپ و راست، اصلاح طلب و اصول‌گرا، دیگر کار نمی‌کند؛جبهه بندی اصلی ایران امروز، جبهه حامیان بعثت مردم برای کارآمدی و عدالت است و در مقابل، ائتلاف ارتجاع به پیش از بعثت.
🔹
امروز جریان ارتجاع، بزرگترین فرصت سوز تاریخ معاصر ایران است. ارتجاع ضد بعثت مردم می‌تواند نام دموکراسی را یدک بکشد یا خود را پشت پرده نام‌های مقدس مخفی کند اما واقعیت چیز دیگریست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/657230" target="_blank">📅 09:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93a8aefd4.mp4?token=V9N3iJ2pkJiRA8B4-wkOkEsW0oIegVFJir_s2GSYCmlR_Nqyb7Bg4PdiLQ-F3g1pGPsFzqTZbu6s8d0W7KAAGzgeWXYQ420mBaqwMNeso_vZDPMayXqZt6_xH1lDBzHMX08SZgdaPBO4EZNgq3hq9AY0uUyJW9hhVihnXgZlTUR5zp3CO6PadwuuWJXAed9ExaA1tutuBgprlT35dduxHYwweJKyBUx4XubtIcTSPzPvLTahM-kPrWVi1INI2uDrdJpWs7cWFrQbc22npEsnuIk5msAiztWH4W-2aYRAHk6iWITAc-hR1OczaByf76DP6B3503UkIUPYu5L9XtTXgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93a8aefd4.mp4?token=V9N3iJ2pkJiRA8B4-wkOkEsW0oIegVFJir_s2GSYCmlR_Nqyb7Bg4PdiLQ-F3g1pGPsFzqTZbu6s8d0W7KAAGzgeWXYQ420mBaqwMNeso_vZDPMayXqZt6_xH1lDBzHMX08SZgdaPBO4EZNgq3hq9AY0uUyJW9hhVihnXgZlTUR5zp3CO6PadwuuWJXAed9ExaA1tutuBgprlT35dduxHYwweJKyBUx4XubtIcTSPzPvLTahM-kPrWVi1INI2uDrdJpWs7cWFrQbc22npEsnuIk5msAiztWH4W-2aYRAHk6iWITAc-hR1OczaByf76DP6B3503UkIUPYu5L9XtTXgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام سابق پنتاگون: حملات به بیروت با چراغ سبز واشنگتن بود
🔹
برنت سدلر در مصاحبه با فاکس‌نیوز تأیید کرد که واشنگتن به اسرائیل چراغ سبز نشان داده است تا ترورهای هدفمندی را در بیروت بدون عبور از هیچ خط قرمزی آغاز کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/akhbarefori/657229" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2VmKWW3l1Q4bt6acvZ-pMvi2yV12w9ldfl_1EnRTOVnmlHEtE14SJhgwGoTCc0HjX5hBXGVL4E1dvfQpwmucQZATN4reU7yOnKvHRqReyfvx9lIndYqO-6lxAfBbfuV67kBjHXSpsVEZUpRfJl-BinobqfD_f-ZbgDx4fBre5ccHHT8sTvmp4T7_-o7aY5HpTYkMZVe4RNHtw6JqkuQLJlvfNCbtCfr7PN5bzlZyh9EVj6iPd5uONw0VLNzBv9AAIdHL1qFu9PgSG3Gyh3gjOcHowmOA5OEuZY0jdI8UP29aEftILtgaZp7jPbBYf_dKDbFHAiioirjL4_JzUx1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: برای چندمین بار ثابت کردیم که آسمان سرزمین های اشغالی و منطقه، تحت اراده ما و در تصرف غرش موشک های ویرانگر هوافضای سپاه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/657228" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba266c931.mp4?token=TrYR55gVihZcdArQ0LT6wkRbgX-fRSOpAH-ggaGaKjXccFhjt8euhYNNZCliz45IlIZ6n6kDWoTHvhOFYmxxU7MYZ7Ffc7TgAb3kRXfTGKuaC40pz5x8gYnZWTxDLtv6Q5iQKQ6psQXBN5Y9GeIvUz49THhrSFDdlLl9pXbFKZNUCDBgrh6_cnMsebEYGd4EYfBkDRU4COvXwdSKXdy7AaWne2gG3ov8DtE8YnIrSDIPO_L7CjSPJCAMZaPF3dqj_CbutZ5cDRnH6r8R589iRx6cOnlNMrWmAnlpd539uDO4ibokH86Q-qITeKHqUWUQPL1q4Z2-9U8ZuqP-yhrmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba266c931.mp4?token=TrYR55gVihZcdArQ0LT6wkRbgX-fRSOpAH-ggaGaKjXccFhjt8euhYNNZCliz45IlIZ6n6kDWoTHvhOFYmxxU7MYZ7Ffc7TgAb3kRXfTGKuaC40pz5x8gYnZWTxDLtv6Q5iQKQ6psQXBN5Y9GeIvUz49THhrSFDdlLl9pXbFKZNUCDBgrh6_cnMsebEYGd4EYfBkDRU4COvXwdSKXdy7AaWne2gG3ov8DtE8YnIrSDIPO_L7CjSPJCAMZaPF3dqj_CbutZ5cDRnH6r8R589iRx6cOnlNMrWmAnlpd539uDO4ibokH86Q-qITeKHqUWUQPL1q4Z2-9U8ZuqP-yhrmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۷.۸ ریشتری در فیلیپین
🔹
زمین لرزه ای به بزرگی ۷.۸ ریشتر جنوب فیلیپین را لرزاند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/657227" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLZZhsmCTfHM9C46sxSC-ebl6_wv5AUgucKLTE0UWb_f7jxX-WWsU6-DO1it5KDDbeTYgFgN54gyJdXXwtqrQA8WEUIC59UcYeiaZwUFe0_L43LinriISs7P3WyEp9UJ4gJQQlJQK6O2_e26A4_7UER8vILZNMTRLgF_wLKjlIjwzPkMxjtgyd_hEpKq8cNDTJB1-wrLT6qBcSxajgu3w0a71rM80OcznxhDMqsBctSkl4yB8ILZAEVdgK5h3xKmFIwk_OwNlN58lrbDlqAkMX4wWYOXEFLeQmh6Fq91tn0BTDb9p2FKBzXxx63xg19ruOu-mN32NrHqKSMOz2ekuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجوز‌ حرفه‌ای ۶ باشگاه ایرانی تأیید شد؛ خبری از سپاهان نیست
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/657226" target="_blank">📅 09:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228113d64f.mp4?token=vUSMbX04yDPdS3m2uusc6qF4p8-kpmCnmipNQIC73N4fJ0h_7URuLrbORSywSePPa1kywZwipF893jkUJ43WBmKvXVTd5Cs2mMGHo9JtKdsNlSApSgjMfxE-wBnn_tYceNrYfzQF_U7tqkT8YjhLdqb8TbdlBfkyJHGn_TqzyEsLZ8FImNibKDaZQ9A6_qhqsWD9DknJHdSwoxoQvZUr6tipsw2_64g9LwW_-e689vlAPII9NfLak2hLYs5nD8y-E7EutiSyTvtnTcTjnbdZtt80ALzCyZFQGHMbL8Pk2HkEWO9LHz3HNDFIo0Uo8o-vtUxftm_np3Pc3RCztNtJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228113d64f.mp4?token=vUSMbX04yDPdS3m2uusc6qF4p8-kpmCnmipNQIC73N4fJ0h_7URuLrbORSywSePPa1kywZwipF893jkUJ43WBmKvXVTd5Cs2mMGHo9JtKdsNlSApSgjMfxE-wBnn_tYceNrYfzQF_U7tqkT8YjhLdqb8TbdlBfkyJHGn_TqzyEsLZ8FImNibKDaZQ9A6_qhqsWD9DknJHdSwoxoQvZUr6tipsw2_64g9LwW_-e689vlAPII9NfLak2hLYs5nD8y-E7EutiSyTvtnTcTjnbdZtt80ALzCyZFQGHMbL8Pk2HkEWO9LHz3HNDFIo0Uo8o-vtUxftm_np3Pc3RCztNtJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یمن قهرمان دریای سرخ را بر روی کشتی های مرتبط با رژیم صهیونیستی بست  نیروهای مسلح یمن:
🔹
در چارچوب مقابله با تجاوز آمریکا و رژیم صهیونیستی علیه محور جهاد و مقاومت در ایران، فلسطین، لبنان، عراق و یمن، و در مخالفت با پروژه صهیونیستی که در پی ایجاد «اسرائیل…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/657225" target="_blank">📅 09:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
یمن قهرمان دریای سرخ را بر روی کشتی های مرتبط با رژیم صهیونیستی بست
نیروهای مسلح یمن:
🔹
در چارچوب مقابله با تجاوز آمریکا و رژیم صهیونیستی علیه محور جهاد و مقاومت در ایران، فلسطین، لبنان، عراق و یمن، و در مخالفت با پروژه صهیونیستی که در پی ایجاد «اسرائیل بزرگ» تحت عنوان «خاورمیانه جدید» است، و در راستای تلاش برای شکستن محاصره ظالمانه و ستمگرانه‌ای که دشمن آمریکایی بر مردم ما و ملت‌های آزاد و سرافراز محور مقاومت در لبنان، غزه و ایران تحمیل کرده است، و بر پایه اصل «وحدت میدان‌ها» و مقابله با دشمنان، و در پاسخ به تجاوز رژیم صهیونیستی علیه لبنان، ایران و غزه، نیروهای مسلح یمن یک موج حمله موشکی را به سوی اهداف حساس دشمن اسرائیلی در منطقه یافای اشغالی شلیک کردند که به فضل الهی با دقت به اهداف خود اصابت کرد.
در این چارچوب، نیروهای مسلح بر موارد زیر تأکید می‌کنند:
🔹
اول: ما ممنوعیت کامل و همه‌جانبه کشتیرانی دریایی برای دشمن اسرائیلی در دریای سرخ را اعلام می‌کنیم و از لحظه انتشار این بیانیه، تمامی تحرکات دشمن را هدفی نظامی برای نیروهای مسلح خود می‌دانیم.
🔹
دوم: تأکید می‌کنیم که در برابر هرگونه تشدید تنش، با تشدید اقدامات پاسخ خواهیم داد و عملیات‌های نظامی ما متناسب با تحولات میدانی، روند نبرد و هماهنگی با محور جهاد و مقاومت، رو به گسترش و افزایش خواهد بود.
🔹
سوم: بر حق مردم خود و ملت‌های آزاد امت اسلامی در مقابله با تجاوز آمریکا و اسرائیل تأکید می‌کنیم و اعلام می‌داریم که در برابر محاصره ظالمانه‌ای که علیه مردم ما و ملت‌های محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق اعمال می‌شود، دست‌بسته نخواهیم ماند. همچنین همه تلاش‌های دشمن، به خواست خدا، با شکست روبه‌رو خواهد شد و عملیات‌های ما تا زمانی که تجاوز و محاصره علیه ما و محور جهاد و مقاومت ادامه داشته باشد، استمرار خواهد یافت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/657224" target="_blank">📅 09:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657222">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
حمله بامدادی به مرکز نظامی در تبریز تلفات جانی نداشت
مدیرکل بحران آذربایجان شرقی:
🔹
در پی حمله بامداد امروز به یک مرکز نظامی در تبریز، هیچ‌گونه تلفات جانی گزارش نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/657222" target="_blank">📅 09:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
لغو تمام پروازهای فرودگاه مهرآباد
🔹
تا اطلاع ثانوی، تمامی پروازهای فرودگاه مهرآباد لغو شده است؛ مسافران پیش از مراجعه به فرودگاه، آخرین وضعیت پروازها را از طریق سامانه ۱۹۹ یا شماره ۰۲۱-۶۱۰۲۱ پیگیری کنند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/657221" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رسانه‌های عبری اعلام کردند که گزارش‌های اولیه‌ای از عملیات حمله با سلاح سرد در میان بیت لحم و قدس اشغالی منتشر شده است
🔹
روز گذشته نیز عملیات استشهادی با تیراندازی در مرکز فلسطین اشغالی رخ داد.‌
🔹
دو روز گذشته نیز یک عملیات زیرگیری با خودرو علیه صهیونیست‌ها صورت گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657220" target="_blank">📅 09:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rydKWqhJzZGXMbL3_l2_NwA369EJNvWHHpGiEcjGt8glJpC4HKhza7mBzZrOcR_9gxAkbATUZuIFBJwtrZs2u74SsxO7hCALVEndbbebCZKaOejwg9EVfsHmbF5X_Pi0n2dS5xES3A3oAMrjE-I0YVat-zZ0Mf-6SusCj6Oqgy7gCCGPItKDWnPFWyTX1GoyztaORQYB1WAzSHU8B1fdl2Z3LzAnjVwuHYGO9z6ZYB_Dv0bc2OUAP2GcwHx6vuUsE9OEvJk_mETCew6-1jKDyQrO3J75GNkGoB9e6OkmgSwTu_Y8yLiRRXxxudTxilTzw4jgzloKiW-Bs4z9sCXprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت با بیش از ۴% افزایش به ۹۷.۵۶ دلار رسید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657219" target="_blank">📅 09:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIn3ThFHKO_AvCF9WZG6KBuN5sPgr2QlcXngEoj53zsBWToiTk-g7sauiGZnEZCeC2AcJmgnhcEzrF9jICHP8Fx43tf4UP7GeGeOTmO4_GPXYR1Mc-Knq78GbWk7lahV1J2G9BybBEdrdQz88bdt5wniz7-xCePoAvtIs8RSbKcmaSDOlAbCPVUvZYwHkuDHSnZ8fSw9DzQ2ztq8f4VwPW4Sf9x0f_ObBJRWdyBUZjeVuvO6j-EI70doRbDUhtiUEO2nprpUM5BK9zn-kVhVD0B4lrpwqaIKyMbaVUl0CkdjepQu35765KaV3z4QNzhc1vO_BaqQCQARbr74IMxSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز فعالیت بورس تهران با افت ۷۰ هزار واحدی شاخص
🔹
شاخص کل بورس تهران در ابتدای فعالیت امروز ۷۰ هزار واحد منفی شد و به ارتفاع ۴ میلیون و ۴۴۲ هزار واحد برگشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657218" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مقابله پدافند هوایی کرمانشاه با اهداف متخاصم
🔹
بر اساس گزارش‌های دریافتی، فعالیت سامانه‌های پدافندی در نقاطی از شهر و اطراف آن مشاهده شده و صدای عملکرد این سامانه‌ها در برخی مناطق به گوش رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657217" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ساداتیان: جنگ باید در لبنان پایان یابد
ساداتیان، دیپلمات سابق در
#گفتگو
با خبرفوری:
🔹
آنچه اهمیت دارد این است که جنگ در کل منطقه از جمله لبنان پایان یابد و محاصره دریایی برداشته شود و ایران هم تسهیلات بیشتری در تنگه اعمال کند و عبور کشتی‌ها بیشتر شود. آن‌ها جنگ روانی و رسانه‌ای انجام می‌دهند تا خودشان را پیروز ماجرا نشان دهند و طبیعتاً ایران مقاومتی می‌کند.
🔹
ترامپ تحت فشار کشورهای عربی که به خاطر تنش‌ها نگران منافع خودشان هستند، در تنگناست و احتمالا به جای جنگ تمام‌عیار، به تفاهم‌های مقطعی رضایت می‌دهد؛ در حالی که نتانیاهو همچنان برای کشاندن آمریکا به درگیری تلاش می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657216" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تداوم فعالیت بازار سرمایه طبق شرایط عادی
مدیر نظارت بر بورس‌های سازمان بورس و اوراق بهادار:
🔹
در سناریوهای طراحی‌شده، تا زمانی که امکان انجام معاملات و تسویه آن‌ها برقرار باشد، بازار تعطیل نخواهد شد.
🔹
بر همین اساس و طبق سناریوهای پیش‌بینی‌شده، امروز بازار سهام هم فعال بوده و معاملات بدون تغییر ریزساختارها ادامه خواهد داشت. /ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657215" target="_blank">📅 09:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رادیو ارتش اسرائیل: تشکیلات امنیتی اسرائیل تخمین می‌زند که در آغاز یک رویارویی نظامی است که چندین روز ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657214" target="_blank">📅 09:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908c1ae762.mp4?token=kR-G9RGLMhxZSGFXmOZyBU9MDWjRS6nIGNiYGDruF3OQtNnoEX8UPkqBsoUXx1kZfyvbpiBklAt0LsqlKzeRCfX6Gs3c7_O3YlFvVc9nAT0ugELwa6gfjLsLfV8TrcT63Ht7I6zPq6eBbzwtrnpGkHN8Fb1pOXqKfG_pukppuvejCtuGrPSFMWtEzn6toWMHJezyHFTUDhAowbUKGXYc_oaMs2DrtwPu_YH58objAd9ea_2XMJeVXNr5lh8AlmpH1IddY-UV7ib5bJ8Xzq7lk-I1Prme1FWTvvz38n4CEQkMlDV8jepO6pynuxau4z_uxf_vOZXDGW-rqEKiTRK8MBET_rY2-zD99RBOa2-N5_r8pO-mHvjzyblo3KTAcOx6v1Bu5rCofVbp89vK415KybDD-hvmlkQKuQW0jyAcCutMLsBxm9y_tisVZxRPWpVnVoQQrxf5rKvvqyiX1eFWDKL1MvMhVlk3Lg74-Kg0SYZ9t3Q9UGnzFPUo3A7T56zB8U_epmP893QNVjWaN_0Y8EW5uGqENLYdC5Hv_NOvfg1vzA1yLiRphioPnGCcirunSSWbBvidJfw1Q_aZdQ9mRd4t_ufOqg3dzuSBTC_TRLEv4tIit4KkdDBuduKdOI2X54MqJ1spUAuxs7sD0Nxw_IWXM8z1uKy5z2k0UKJQ_40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908c1ae762.mp4?token=kR-G9RGLMhxZSGFXmOZyBU9MDWjRS6nIGNiYGDruF3OQtNnoEX8UPkqBsoUXx1kZfyvbpiBklAt0LsqlKzeRCfX6Gs3c7_O3YlFvVc9nAT0ugELwa6gfjLsLfV8TrcT63Ht7I6zPq6eBbzwtrnpGkHN8Fb1pOXqKfG_pukppuvejCtuGrPSFMWtEzn6toWMHJezyHFTUDhAowbUKGXYc_oaMs2DrtwPu_YH58objAd9ea_2XMJeVXNr5lh8AlmpH1IddY-UV7ib5bJ8Xzq7lk-I1Prme1FWTvvz38n4CEQkMlDV8jepO6pynuxau4z_uxf_vOZXDGW-rqEKiTRK8MBET_rY2-zD99RBOa2-N5_r8pO-mHvjzyblo3KTAcOx6v1Bu5rCofVbp89vK415KybDD-hvmlkQKuQW0jyAcCutMLsBxm9y_tisVZxRPWpVnVoQQrxf5rKvvqyiX1eFWDKL1MvMhVlk3Lg74-Kg0SYZ9t3Q9UGnzFPUo3A7T56zB8U_epmP893QNVjWaN_0Y8EW5uGqENLYdC5Hv_NOvfg1vzA1yLiRphioPnGCcirunSSWbBvidJfw1Q_aZdQ9mRd4t_ufOqg3dzuSBTC_TRLEv4tIit4KkdDBuduKdOI2X54MqJ1spUAuxs7sD0Nxw_IWXM8z1uKy5z2k0UKJQ_40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه ورود بازیکنان تیم ملی به مکزیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657213" target="_blank">📅 09:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وزارت خارجه قطر: وزیر خارجه قطر تماس تلفنی از وزیر خارجه ایران، عباس عراقچی، دریافت کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657212" target="_blank">📅 09:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7BVF4OQDUUlRjV-0134hSB1xnIizH4e1RCldz1sy2BugwdkulCTia4zerqXPgEX2H8sgiNuUjdziR4M32XpFyrR4D28SAbHj3bwewlnC8FUYR_wjawXIeqoHjXtOqrElWywFimvrguOOfO3CCdRO5kE6FFK9hBhcSzrv84H1D1udmg7POuwNBSEK_GpBloen263yN71z1gYQQfamjtzJozQUi-Oxl3Jd4_yRMKkBYzl1nyCmsTtc7c59btUOLXv-jIeF4iSILhfOdUArVGCqHqxMKUjA5Y3ounWGyijypriUDMoxw3dlHgH-7nmCn0IGj3mxs3hV2S0xruVryo3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود شی جین‌پینگ به کره شمالی
🔹
«شی جین‌پینگ» رئیس جمهوری خلق چین با ورود به پیونگ یانگ، دیدار رسمی خود از کره شمالی را آغاز کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/657211" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کوشکی: آتش‌بس یک‌طرفه برای این بود که متحد راهبردی ما، حزب‌الله را نابود کنند
کوشکی، فعال سیاسی اصول‌گرا در
#گفتگو
با خبرفوری:
🔹
عملاً آتش‌بسی وجود نداشته؛ آمریکا و اسرائیل از همان لحظه اول با ادامه حملات، آن را نقض کرده‌اند. ادامه این وضعیتِ یک‌طرفه، هر لحظه زیان‌های بیشتری برای منافع راهبردی ما به همراه دارد.
🔹
مذاکره برای آمریکایی‌ها و اسرائیلی‌ها کاملا موفقیت‌آمیز بوده و توانستند در قبال آتش‌بس یک‌طرفه و مذاکرات بی‌هدف زمان بخرند برای این که لبنان و متحد راهبردی ما، حزب‌الله را نابود کنند و از طرفی توان ما را به تحلیل ببرند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657210" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی شناسایی یک شبکه جاسوسی در قلب سرزمین‌های اشغالی شد
سایت عربی وای نت:
🔹
اسرائیل یک شبکه جاسوسی مرتبط با ایران را در «بیت یام»، در مرکز سرزمین‌های اشغالی را شناسایی کرده است.
🔹
در این گزارش آمده است که این شبکه جاسوسی اطلاعات حساس  را در اختیار ایرانیان قرار می‌داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657209" target="_blank">📅 08:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657205">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaxuxPydbwftSWeb_vKcpY3AVxh2Kb8oi3rtm26o-NZpjAHxJeNbUXPny1TRP9I2xkyWwse6hfxMNvvMUs_mkeVFVLApDsh4teRLKImmUylpXgEXwYVzEjeA9arETq4PdwLNNKK_Ym8Y9bjzbkbW6p96vFS3Rrbpdi1aVfDYwNCwCIfDFW-iEh2Eq-H1hA6-xesPTRPIl0xS9c7n4Xhwh7cCMTTkvDeAfUY_4uiGfwHDx8wj_OwyB571olW16gAOEMm6t-YGOzDx5WyjQgdQZ9HOY8ukwOQgoOCK6z5ixS4zqKk6pzceTJRCM-p_r4b5g4u_g1rpppKbzEeusNiHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrcO8yEdbwMuVJOsnbhTVlGL5W7byqwgTlQjyWM2qr2O4FXQV6J6hKq5HP7quMH_nI2PgwvQ-s5lTFmNqM--AEhnSKESKvK-gezlVgPWHV4kEj63lFNMVptr_F7-Cves0_R4Woa_DMCQQ9J9Pqm0MWtH0yp9zFqs5wpsavPyySlOP5LpL32V-AZwb-LPzPPqLrBl0AtkgKzRmeX3ehHb3sCpKfXawFmHggaokW_L95-UM8uOxb72eOBBYbiFe5f5_9Wyj9pdVNpZT7ES3KJjKE4mJLQWbWmAMBjW3FivemBk3YHlWOLaUsaAqAY6miyQ8qufbn5hdpMORlYZ9tYFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHVULsQec5rKua69ie9S3390sHBudJbr8mC5NjSe-ClEkIei8lDPEHS1Tk1wLMe5MyGhRmAOlZFQmAwYesaSsVAFtdurqlDPVerut72NcXHtuo56oLxz5JoBj1lypyA4bFRGiVWFJcHmgM-ybuqnu-6JrCag93miYR5kkXhkCMdXsAx9KkXGSQsB9nAjn1QLHgjQ3Z1Vd1MSkQ7BnamGoDEMm0AXEV9ehA8zLotyxX_dKMkXjm8IYbcis-UnMmMNmXhL45ZnqSzV5XbocEd3euRLxLPRSWqllqHCuRjfSW8CGpHIljSCl3v2iA3xLg8_nwTuPoCua7G5YV-ks5g6iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe8b22aac.mp4?token=MB7sF50MK4vHPOnpL4DeN0lncKqC77_X4jTWFlbXOpptr2f8Awzgsgw7xpzWRzObUd4VARI96keie1M9Qe6SWsUmui8Z6Y9Q5LEOokMQZDtU_mq08BB4JLaKxQMaeYAXml5wu0aM0KGkgjU0O5hWuaRSVHnk5UJpH3BO2_inipTI0LW4ipkf2_oiDMWUIWnOGnk5bDHncN4qe7bVidsZngmg0oRUhxCQ_nLmQ3VXjY8bHGyoavTh64ZiB29A7nuJuz2Q06pc8LlKscjiSLQjHKKiaXV4zhLSTj3mteiAtVOGjpYIVbqnHn1rpzM7aD9HOOX9Zy3ihfUFU3VMa-bSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe8b22aac.mp4?token=MB7sF50MK4vHPOnpL4DeN0lncKqC77_X4jTWFlbXOpptr2f8Awzgsgw7xpzWRzObUd4VARI96keie1M9Qe6SWsUmui8Z6Y9Q5LEOokMQZDtU_mq08BB4JLaKxQMaeYAXml5wu0aM0KGkgjU0O5hWuaRSVHnk5UJpH3BO2_inipTI0LW4ipkf2_oiDMWUIWnOGnk5bDHncN4qe7bVidsZngmg0oRUhxCQ_nLmQ3VXjY8bHGyoavTh64ZiB29A7nuJuz2Q06pc8LlKscjiSLQjHKKiaXV4zhLSTj3mteiAtVOGjpYIVbqnHn1rpzM7aD9HOOX9Zy3ihfUFU3VMa-bSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از  نخستین تمرین تیم ملی ایران در کمپ تیخوانا
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657205" target="_blank">📅 08:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657204">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUTJ1nKSutOG_m1yYs2TtHnDNMqUVaOZtXo-Ypi7wAin0Dsm8MxQ504t-P1tGiAmCMJ9tENfVzuFKWAxXhXoqLLgF0jrvhPm6asoZaxtNdil0akYlItTxpm1xWzDw5PNhs8bEoPR2WaJdxv26_e6CMvJMlL3nu9SfdbeyFqyorMYRpc_8KGd0ehkr_IKGU7NDjm2Lw6UjKleZoKadYFzjR6OA2mf6Nt8Xh0xMDfhjPuXUrLoZF-PpTvUq-1OjAIpm5RTUzEHYKiWf5Ojj8vHqmYWxo_IeJrT1UODs4mHR_Oc4jiw16fMxKo4MI0gBYX7yTI-o7bxesvD5ckLNPGNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش فوق‌العاده محصولات کیا (کوشا خودرو)
به اطلاع متقاضیان گرامی می‌رساند، مرحله جدید فروش فوق‌العاده خودروهای کیا از ساعت ۱۰ صبح امروز ۱۸ خرداد ماه آغاز می‌شود.
✅
نحوه ثبت‌نام:
فرآیند خرید به صورت کاملاً آنلاین بوده و متقاضیان می‌توانند با مراجعه به وب‌سایت رسمی کوشا خودرو و ورود به منوی «فروش اینترنتی»، نسبت به ثبت‌نام و خرید مستقیم اقدام کنند.
🌐
وب‌سایت ثبت‌نام:
www.kooshakhodro.com
کوشا خودرو
فروش و خدمات پس از فروش کیا در ایران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657204" target="_blank">📅 08:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657203">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
درخواست محدودیت‌های جدید در فرودگاه بن‌گوریون
🔹
فرماندهی جبهه داخلی رژیم صهیونیستی درخواست محدودیت‌های جدید در فرودگاه بن‌گوریون در شرق تل‌آویو را کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657203" target="_blank">📅 08:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657202">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
درخواست محدودیت‌های جدید در فرودگاه بن‌گوریون
🔹
فرماندهی جبهه داخلی رژیم صهیونیستی درخواست محدودیت‌های جدید در فرودگاه بن‌گوریون در شرق تل‌آویو را کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/657202" target="_blank">📅 08:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
انتقال بیمارستان‌های شمال فلسطین اشغالی به پناهگاه‌های زیر زمینی
🔹
رسانه‌های رژیم صهیونیستی گزارش دادند که بیمارستان‌های شمال فلسطین انتقال بخش‌های اورژانس خود به پناهگاه‌های زیرزمینی را آغاز کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657199" target="_blank">📅 08:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657197">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
العربیه: وزیر کشور پاکستان بامداد امروز ایران را ترک کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657197" target="_blank">📅 08:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرفوری
pinned «
♦️
آغاز عملیات نصر علیه پایگاه‌های تلنوف و نواتیم  روابط عمومی سپاه پاسداران:
🔹
با توکل به خدای متعال و استعانت از پروردگار قادر متعال، دقایقی پیش رزمندگان شجاع نیروی هوافضای سپاه عملیات نصر را با رمز مقدس "یا حیدر کرار" و هدیه به شهدای جنگ ۱۲ روزه با هدف قرار…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/657196" target="_blank">📅 08:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
انتقال بیمارستان‌های شمال فلسطین اشغالی به پناهگاه‌های زیر زمینی
🔹
رسانه‌های رژیم صهیونیستی گزارش دادند که بیمارستان‌های شمال فلسطین انتقال بخش‌های اورژانس خود به پناهگاه‌های زیرزمینی را آغاز کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657195" target="_blank">📅 08:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آغاز عملیات نصر علیه پایگاه‌های تلنوف و نواتیم
روابط عمومی سپاه پاسداران:
🔹
با توکل به خدای متعال و استعانت از پروردگار قادر متعال، دقایقی پیش رزمندگان شجاع نیروی هوافضای سپاه عملیات نصر را با رمز مقدس "یا حیدر کرار" و هدیه به شهدای جنگ ۱۲ روزه با هدف قرار دادن مراکز مهم پایگاه های هوایی راهبردی نواتیم و تلنوف آغاز کردند.
🔹
این عملیات در پاسخ به تجاوز موشکی رژیم کودک‌کش صهیونی به چند سایت راداری در سه نقطه کشور انجام شد.
🔹
سرعت عمل در پاسخ به تجاوزات ارتش رژیم صهیونیستی و گستردگی بانک اهداف جزو اقدامات گروههای عمل کننده در این مرحله بوده است.
🔹
کلیه یگانهای رزمی و عملیاتی سپاه پاسداران برای انجام عملیات عبرت آموز گسترده در تمام جبهه‌ها در آمادگی کامل بوده و برنامه های اقدام را متناسب با سناریوهای دشمن تدارک دیده اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657194" target="_blank">📅 08:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb81cb41e.mp4?token=QccdUMY5-K-Y-BSUZcUPI_Ec9rAyt1YfKVg73UJ-Ow84BUNKUSv4Q2EBTj5S3Q6k7DvLc95elYrrE4diRL7j3Za1-kMYK44GIRPw7fUG7_Xuv33ET1um2ZOW3k8pPMp6oADQvBwRKVzHKVoW1PlhoUy0Qmv8D8qWJS5JkAVdJwfrVu4aMWXdsTvCmZXJKrLe2At38BPCtkJt9GnpYsxv8oW537KTXhjy9LbADgqXN0NrsJLLhdrpxtefeYBYSdrVo9dkE0kPCIJyDlV47iDitakjnl5PVqNCXs2OdNsU4-yeFmjNPU9o7JNtQiCkqi4jODOkHnJtgDeJHH7Ucm5jlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb81cb41e.mp4?token=QccdUMY5-K-Y-BSUZcUPI_Ec9rAyt1YfKVg73UJ-Ow84BUNKUSv4Q2EBTj5S3Q6k7DvLc95elYrrE4diRL7j3Za1-kMYK44GIRPw7fUG7_Xuv33ET1um2ZOW3k8pPMp6oADQvBwRKVzHKVoW1PlhoUy0Qmv8D8qWJS5JkAVdJwfrVu4aMWXdsTvCmZXJKrLe2At38BPCtkJt9GnpYsxv8oW537KTXhjy9LbADgqXN0NrsJLLhdrpxtefeYBYSdrVo9dkE0kPCIJyDlV47iDitakjnl5PVqNCXs2OdNsU4-yeFmjNPU9o7JNtQiCkqi4jODOkHnJtgDeJHH7Ucm5jlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفتالی بنت، نخست وزیر اسبق رژیم صهیونیستی: نتانیاهو «قادر به تأمین امنیت» اسرائیل نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657193" target="_blank">📅 08:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اورژانس استان تهران: در پی اخبار منتشر شده شب گذشته، تا این لحظه هیچگونه تماسی مبنی بر وجود مصدوم نداشته‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657192" target="_blank">📅 08:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
به صدا در آمدن آژیر خطر در قدس اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657191" target="_blank">📅 08:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر  معاون امنیتی و انتظامی استانداری خوزستان:
🔹
دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.  #اخبار_خوزستان در فضای مجازی…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657190" target="_blank">📅 08:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c669511a.mp4?token=mUmEQStaVHpKR_9J6CsZyusybSF20j1OMc8iW8CJr4UeZlwgK-WEY7a0fDbKxZlZQHLBzGlV9xqT4oHWoDqgaiFKHTd3xzTcEsEKkAxtNmXzQTuXDo1ijY2HTsdNJfuFOMXOsEQG-rCFhOsDlxL3IawPSG4d4gdOVN9rXOypotZc4GDp6_L3vJu7wuGmKit490gIiwan6ICt509aIi3Ydn1a3a74SfNiOfXtOZ0qLSMjPhgRxmDZZuVhqh0SgYiQVTAYIjF4zZd6ghDSZfz7mlz4NsWcl_OjMGzx_KyDlaclRXilJ3E87FctwdITmghJFtgF4qO5MjgrINRwFfNLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c669511a.mp4?token=mUmEQStaVHpKR_9J6CsZyusybSF20j1OMc8iW8CJr4UeZlwgK-WEY7a0fDbKxZlZQHLBzGlV9xqT4oHWoDqgaiFKHTd3xzTcEsEKkAxtNmXzQTuXDo1ijY2HTsdNJfuFOMXOsEQG-rCFhOsDlxL3IawPSG4d4gdOVN9rXOypotZc4GDp6_L3vJu7wuGmKit490gIiwan6ICt509aIi3Ydn1a3a74SfNiOfXtOZ0qLSMjPhgRxmDZZuVhqh0SgYiQVTAYIjF4zZd6ghDSZfz7mlz4NsWcl_OjMGzx_KyDlaclRXilJ3E87FctwdITmghJFtgF4qO5MjgrINRwFfNLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از یک خانه آسیب دیده بر اثر موج موشک‌های ایرانی در سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657189" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
هیچ‌ منطقه ای در کرمانشاه هدف قرار نکرفته است
🔹
از نخستین ساعات بامداد امروز دوشنبه، هم‌زمان با آغاز عملیات موشکی جمهوری اسلامی ایران علیه سرزمین‌های اشغالی، برخی شایعات در فضای مجازی درباره وقوع انفجار، حمله یا تهدید امنیتی در استان کرمانشاه منتشر شد؛ اما پیگیری‌های دقیق نشان می‌دهد این ادعاها فاقد اعتبار بوده و هیچ‌گونه حادثه‌ای در این استان رخ نداده است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657188" target="_blank">📅 08:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شلیک موشک از جنوب لبنان به سمت اراضی اشغالی
🔹
منابع خبری از شلیک تعدادی موشک از جنوب لبنان به سمت مواضع اسرائیل خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657187" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql-2Af2Es3BMrhkLjqmrWDe26ys9So6XXk-sKuVTuDrgaT7v2eOrBTrBf6rvsAbjRVq2s4fKQixmVAv8LR_WFKvSvHzhtrbwXZ9lTzxJZ5aJvLdmdzg0Q9bQr_aluhpB0JAo6w1rvT1CvbO0mRC55c2hrIAWUckPxI_A8hPWd3YEdOCLoxqn_NNZnVnXxg2XaW4QP0tEBQ_Hs0pp3EJ38hOLH2HNLr4JPFZCx08kiQr-tw1QrXdSmkSRyfTdo7FGVb5uYwlqZWTACfU4d04E1q0DydScoxh0IdYCJisg7QVTJuBH7XwO6Q1XM-V0QsrngVLtcYCBCfv7Ayt2XpLK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی،
مشاور رهبر انقلاب: انتخاب با شماست توقف حماقت یا ورود به موازنه ضابطه‌مند شدن دو تنگه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657186" target="_blank">📅 08:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZGqZAy6kGJqVzQ-NDNkGz-kMQ1wvjIkz_Fewpf3d2AXsygjBb8dIxk85Q4df-0oBywxD9fhjVWKHGjqqRj8Ejrtk662Vyf6P86PpIRfb8wmypZRMzBdIQ4Fk__kaTkgthC_uQNCcOE6JYMbv3eGc0q46psu_I8GcKjMNTlr2M9iwzpf25yM1toqT1rrfCDiXgFuV7ABKWvHOt1Hw2giX5W3ZsOEq1ZYogDq745NR3LhBQG2FM9x1r-yhnuIZcasyPVedhdJBLXfWukui1moMKZvDJVsSfL24y1PLAHi9eJyT5vG9IB7nXeK1aUGw6DN--hoJy7W3Ds0rBFZzA8aOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازنشر دست‌نوشته شهید لاریجانی و بیتی از اشعار سعدی
اقلیم پارس را غم از آسیب دهر نیست
‏تا بر سرش بود، چو تویی سایه خدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657185" target="_blank">📅 08:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657183">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ac715433.mp4?token=U40GTPveTx0tzDy98Il8Cx7wAlOCHK4nkb3gWpCVcDBFCezPe5KxCdAOqS4loqLB_ib4_w0E62qnrgCMjMYAH--uhQQT_og1r1hJyvKZOf4YOIdQRz2ZRPkHPJ5WNNCgnF-RwLFAhPJoFlUjVb7DowjBowO49yxRjzSPIDvYrUzNuKjlzw-NLc8bzx4Z2StvhCYs9z1Z0-cA6b6MBLru6jcRv8ft01hKbXREmevpe7lk6WEwTB3fMeVTQ4kGBmTFdCfV0ArFJGB0OHZ6cwbaNVgiVR4_s5GafZ36iga97k7NJ4wieEBLAIdVOvOZR0Ub0OSSzd5tmgI4uQw1H8XBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ac715433.mp4?token=U40GTPveTx0tzDy98Il8Cx7wAlOCHK4nkb3gWpCVcDBFCezPe5KxCdAOqS4loqLB_ib4_w0E62qnrgCMjMYAH--uhQQT_og1r1hJyvKZOf4YOIdQRz2ZRPkHPJ5WNNCgnF-RwLFAhPJoFlUjVb7DowjBowO49yxRjzSPIDvYrUzNuKjlzw-NLc8bzx4Z2StvhCYs9z1Z0-cA6b6MBLru6jcRv8ft01hKbXREmevpe7lk6WEwTB3fMeVTQ4kGBmTFdCfV0ArFJGB0OHZ6cwbaNVgiVR4_s5GafZ36iga97k7NJ4wieEBLAIdVOvOZR0Ub0OSSzd5tmgI4uQw1H8XBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در منطقه نظامی واقع در کرانه باختری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657183" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657182">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سفیر آمریکا در اسرائیل: صدای انفجارهای مهیبی میاد
سفیر آمریکا در اسرائیل در پیامی در شبکه اجتماعی ایکس:
🔹
الآن توی پناهگاهم. صدای انفجارهای مهیبی از بالا میاد.
🔹
امیدوارم که رهگیری بشه. یه روز دیگه که تحت تهدید رژیم دیوانه ایران زندگی می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657182" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUygTsQ8Vugp3JsWwi0MB9lHiRW69iDfwH2nWFIEpML_UrtMWq3r-RRfq9chrWRmfyEsPkS86tTgQU5MXFT06nryhFUWvNo_HuPUg8n-JqdvPQE4DVJeGYgrktdH9YlYS1Z962ji9o0TSQ5xwSGM_gL8Llgq-VWlojqAym1WXkxEj9yoD-Xx6J9M2uOz67pUV8Z5fnkL5bUnn5aqv_8hasPEaoAkKeILmk7BkO-3PUCrlE700lrEQyl-Iqc7UjSMXdCzUJrDlM8n2ROfUF9kfR3LqNiAExGJigtg4UIe05DHYH4aakNAwdeBY0Qqv1t5cTpxTnb6unkCeHITXAjuUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657181" target="_blank">📅 08:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
گروه هکری حنظله: از شما دعوت می‌کنم تا شاهد ویرانگرترین حملات سایبری علیه زیرساخت‌های حیاتی و نظامی دشمن باشید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657180" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شلیک ۱۰ موشک از ایران به شهرک‌های صهیونیست‌نشین کرانه باختری
🔹
روزنامه اسرائیل هیوم از شلیک ۱۰ موشک از ایران به شهرک‌های صهیونیست‌نشین کرانه باختری خبر داد.
🔹
در این خبر آمده است که سه ساختمان در کرانه باختری آسیب دیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657179" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d2f3e172.mp4?token=v8feavQrfHSVs80n4OzCYpHl3wNHTnyI-8b6tGFm_wzvRthrh-3mSQ__uxSOGebxCLQTf83wruZZBtoMMl57WpnSuaXXeti5K2Zj2PRfma57LG09AxNUm3O6QVpqMFNZmU3rb0GPX5awkatjPVBt-8eElZaLArznU9L14u1wbcGj3XnXSyNyEYOUx6dlqHS1GDid_gQvWmH7bgK4YlrbiX4JDFA1gXkTikZXp6h8rML_kau-TNF6iiztLjLpiJmqez1zdIq5fLUMNipNdY_hNWYS-v8kDnJ0uDCpYzpEghS8RgXqXOHRQ7Nl3AMaYuruCeUS6aoMKNvhQ6v4fhjMGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d2f3e172.mp4?token=v8feavQrfHSVs80n4OzCYpHl3wNHTnyI-8b6tGFm_wzvRthrh-3mSQ__uxSOGebxCLQTf83wruZZBtoMMl57WpnSuaXXeti5K2Zj2PRfma57LG09AxNUm3O6QVpqMFNZmU3rb0GPX5awkatjPVBt-8eElZaLArznU9L14u1wbcGj3XnXSyNyEYOUx6dlqHS1GDid_gQvWmH7bgK4YlrbiX4JDFA1gXkTikZXp6h8rML_kau-TNF6iiztLjLpiJmqez1zdIq5fLUMNipNdY_hNWYS-v8kDnJ0uDCpYzpEghS8RgXqXOHRQ7Nl3AMaYuruCeUS6aoMKNvhQ6v4fhjMGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل پس از حمله ایران دیوار غربی(ندبه) را تعطیل می‌کند
🔹
فَإِنْ لَمْ يَعْتَزِلُوكُمْ وَ يُلْقُوا إِلَيْكُمُ السَّلَمَ وَ يَكُفُّوا أَيْدِيَهُمْ فَخُذُوهُمْ وَ اقْتُلُوهُمْ حَيْثُ ثَقِفْتُمُوهُمْ
🔹
پس، اگر از شما کناره نجستند و به سازش با شما رو نیاوردند و دست از شما باز نداشتند هر جا بر آنان دست یافتید بکشید. نساء - ۹۱
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657178" target="_blank">📅 08:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657177" target="_blank">📅 08:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657176">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هیچ‌گونه حمله انفجار یا تهدید از بامداد امروز در خارگ گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657176" target="_blank">📅 08:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657175">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نشست کابینه نتانیاهو برگزار می‌شود
🔹
کانال ۱۲ عبری اعلام کرد که نشست کابینه نتانیاهو ساعت ۱۱:۰۰ صبح به وقت تل آویو برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657175" target="_blank">📅 07:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657174">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بیانیه مهمی از سوی نیروهای مسلح یمن در ساعات آینده منتشر خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657174" target="_blank">📅 07:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657173">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم اسرائیل: موشک‌ها و ترکش‌ها در بیت شمش، غرب قدس، و شهر بئرشبع در نقب فرود آمدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657173" target="_blank">📅 07:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657172">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgGctf-EWtCtqlh8v0LmGB3ta8hNnAUQcFRHjhRfrXLsIzOxpwzX7OrkfFPHjChnGgs54xEPBZ-q44V16ElK_OLvFYvGU7yJi9_wlFSWAy9kwBQkI3fXzSdxDCD6NudPqPUU_yBurgQ44FX87n_gDtsSDrNDJtvL8GfmAxbFJY0XOSbZ8s_5RGYy7wVtx1jU2_QM9nTxf4yFRd4uEiFxLntrgeXMYJxyMyAi39PBhvz0mHCY_Z83EFyHTfNAkM5w25rJItRAK3nnXW7NYET5VEy-bR7UBOndWn9I9bfTgpefLURByEPv2FyhLeLo9aIQEJ0kiMmtN-460h4i1BMKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آژیرهای خطر در اراضی اشغالی بار دیگر به صدا در آمدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657172" target="_blank">📅 07:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433729c5e7.mp4?token=rACk0IZG4kfMAfxsyrrmxTI-b8mJIo6smG9MToMi2NfcMwZxMp2sijn3jBWaNlFLNR293ycN5j6hvKBFP-FDDkV0bMrEJBNNldrdNbaa0CNo89Ha8h1umv4RqdV_KTxmZLWsYamwakvSBXMm2l7g4FWVMCg2z7UogSgZ4A8fka6Y-tmX4s9vy7w1NkmRaP_BYKoz2OONnByvyF2X2JNTsE5Z0GflFhe-08ZzlS4Gw9Aw5iNuEODTcKcjVHA76nGwzoYZWczSv4IJwntHAvTqySXVvwN7kWceI-qxR3_fqiv9Wmck7quLsj3F1nw56otdH1mXrH5iccOdE-HhIiPjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433729c5e7.mp4?token=rACk0IZG4kfMAfxsyrrmxTI-b8mJIo6smG9MToMi2NfcMwZxMp2sijn3jBWaNlFLNR293ycN5j6hvKBFP-FDDkV0bMrEJBNNldrdNbaa0CNo89Ha8h1umv4RqdV_KTxmZLWsYamwakvSBXMm2l7g4FWVMCg2z7UogSgZ4A8fka6Y-tmX4s9vy7w1NkmRaP_BYKoz2OONnByvyF2X2JNTsE5Z0GflFhe-08ZzlS4Gw9Aw5iNuEODTcKcjVHA76nGwzoYZWczSv4IJwntHAvTqySXVvwN7kWceI-qxR3_fqiv9Wmck7quLsj3F1nw56otdH1mXrH5iccOdE-HhIiPjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل از شنیده شدن صدای ۳ انفجار در قدس اشغالی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657171" target="_blank">📅 07:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAzC8hx9rqJFzaxRpw8cia-niF8w_DrU1PnXESivMQpIdk9MW9QO-oShCk-_irIRfRis8l3ijM9lQfHKcNSTMhgNVvK7gcue0l_YyRXkYizb8FljI2Iv2GJ3SZsW5nAak8tpIVdrloTDtTENTPXil0jf2pBa7BxeOvMfLs-DJzII3upHiuVCKcAQyTNTrGvK6NU_cg03owVWyKqJIwQGeCZUbDbfB_6duYgQkFFB_U_JNDgu1f2I_uuWqIbnlNBdQk0rS9KcoE8emydr7I0ioeBSfjQlO-MTdBSoF_QNQmhPi21-ja4ZN76Mn4S118Z1xTRPYdfEhgh0N-qMZbISpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیتر روزنامه لبنانی الاخبار؛ ایران به جهان: لبنان تنها نیست!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657170" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل از شنیده شدن صدای ۳ انفجار در قدس اشغالی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657169" target="_blank">📅 07:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrJaHQT5UyNVvitPWO4gh_qQGzDeePDuIWVjmyd4l9RVa0rzR_0rRKYpWD8sKw0j4USDduL_PzT2-I-yEeuGJMkP8ufbc1jMoLMh9_2mNqDF6JiPh1tFxhBStYX5FSvWnaIS8fb8Vz5Syi7Vj0Y2GfLEAIy92ypsdT7ia7Hqvmta7SXmBcmUReYvYxdPCe6KHRbtzKRcYncTc1n7oj5Sma4lqAKWStsPbjZPTqhmLaRfPQv6IDkFoZ2urNBgq0-ffTD76p2V4Y1m_GFr7HQqQ_NJPOLepROFZm8uAS9fGmGtqVa7CrCnzuKKVo8jLRP6STifomzcXnsPSLE4afXBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szJFBxq-advBVQAbs6Jvd0tSp4go9p-CVnfgNssyg6oKeQmxNPCO3KpYXGC90p7x5a65vBJNNyul-VL7n4Pz8lncmg34vWv40cMH9i_ifu64pehNl0U32l2KlNetf5HrYnQz5NGLeDap1B_k_EX51XUkqEo3dp4d8NpMUdckS_C9wcThr7EqJF0of9T-_CuH3OKdl_gxs7DyRpkaKicoBNuE9b8JsIBRpBJyhGZ9HfENh2khGKJqge8H8NQTCHL9EQLMbPt7Ha4mnnaM7xiPPA7AaJiZCLC28pC2kFuKq9o6xEqghC1k52jwvIg-Oo4K3WiVnEgvnuBJcm3eCSYzLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mc1Qzn6M-WV5XhvyFENWTyCzuszzucU8D_v28pieoEW8hMwtgwOPkhQbqNroktkOtytl1H2O1DAxtHZOAiscsE9qKY2KY13JY9DlTH_zrgFhEu-UK2cDC6n28Q3H2KzQuWd2Na3MGJG5FCc4sFSY8tEp3xwApkQUgdxlN6-S9M-b5EHTTOjUol8m2IUHIT8KaT5Hp7m2hp4_JjhLYv0xAPgeBkmZMuAoCotFDkTWy7bwEqIkQcxDQEMOcyUg2AiZ_8nK8smx-XIbeDv4RBk3PrFxwnD6y9OEm1umHcN6B-Z0OPc5LSF9BXQi53R_qD9BesYei6w1xdoLyQOIo12URQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صدور آژیرهای هشدار اولیه در اراضی اشغالی
🔹
وَ قاتِلُوهُمْ حَتَّى لا تَكُونَ فِتْنَةٌ
🔹
و با آنان نبرد کنید تا آشوبی برجا نماند بقره ـ ۱۹۳
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657166" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxBC1lfMrgoKQFNaaeHHj2N2fNCPLVpruNSEU44qS2HuHGsJWJTkUQ1iF-kcSVDuais0DVj1bTtJoUCoS1JYoJHBFhWRaEk1TcCEYn9dsmd6dIdStZrtwdGzz2ZxTFs2dQL6ujw7fBaKvsFmBBl_NqglC-hCiaDWjU6vCzbq596CWm8E1dsMgP-qcnQyP8fNrC9oHsfXEwUBcbAdUWpdOScsnLx8ANqBP_RQwhWkwM47IlB851Xa_l55YEAJMis1bE3vXAzr-Oa85RWhKr9MJvt1aUwvjLFcf4dB75-xjOHlVeCsmwodyavZFBcH497NmkiHQKcVKZP51dy8SP0FmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۸ خرداد ماه
۲۲ ذی‌الحجه ‌‌۱۴۴۷
۸ ژوئن ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657165" target="_blank">📅 07:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKQtxJqhKrl6EHtgRQmNpWz4iQHbLITQ-_eswtU7DK76asnsvIDmxpkti2Gb1h-m_Y77YhjjUDmIeqgfEIIf_sh2W1eMYunDXa2IMNaT18zUBHmnnxb0z2k-MW_N3vd3XLDssnGxMGV6_uDBW1s_nrepfyOlPIB83xl_i4nCJimYA0l3hjP-PLTX1ZimRAWl3uXQw9ibOF8oqPhJSPZSp-Xa9xqjasXG5RZSVrkl1EzhhHnkTernz6U5RfGyfYVWGP3BFEZluv2p9ZLw_YKrUI3tgPShLgZGnpaeZ_wfRx3HKEnUQLIOkXSV6yjupJMCdIZl8-WycVEdhTIsRZNpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدور آژیرهای هشدار اولیه در اراضی اشغالی
🔹
وَ قاتِلُوهُمْ حَتَّى لا تَكُونَ فِتْنَةٌ
🔹
و با آنان نبرد کنید تا آشوبی برجا نماند
بقره ـ ۱۹۳
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/657164" target="_blank">📅 07:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14fb719d4f.mp4?token=EHAkdmVhSJVeLhRGRvzP47Hyr9hOC3LAILfWqU_Npkw_aXfkEREbqc8bTH9HpczTDE9cDauLxrBpS5BwSqPQ8JiL6yh1ubgP8Xay2y44zxKfXn1jav6IvtPQo1_AznPtMj1TeFJwEclHjUMpl9-ePl0Mw9clzayy-oxXKjsO_ay_cOCymN9wvzitROpzKraBYUj0UG2svXwuQkvqLAi69XOxvr-xjqlZxvNdmttX_4ZBFavto2EbZ-lCxtVm4xXpUuNXNyxnUlwpVm_Y5rAOGLGQUBrsr9QQM2PJlmQ2SrF3sb-SOji8_6sDu02d8ERefoey_RWRhoqnjoXLwCtjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14fb719d4f.mp4?token=EHAkdmVhSJVeLhRGRvzP47Hyr9hOC3LAILfWqU_Npkw_aXfkEREbqc8bTH9HpczTDE9cDauLxrBpS5BwSqPQ8JiL6yh1ubgP8Xay2y44zxKfXn1jav6IvtPQo1_AznPtMj1TeFJwEclHjUMpl9-ePl0Mw9clzayy-oxXKjsO_ay_cOCymN9wvzitROpzKraBYUj0UG2svXwuQkvqLAi69XOxvr-xjqlZxvNdmttX_4ZBFavto2EbZ-lCxtVm4xXpUuNXNyxnUlwpVm_Y5rAOGLGQUBrsr9QQM2PJlmQ2SrF3sb-SOji8_6sDu02d8ERefoey_RWRhoqnjoXLwCtjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه به صدا درآمدن آژیر خطر در فرودگاه بن گوریون هنگام حمله موشکی یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/657163" target="_blank">📅 07:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رسانۀ صهیونیستی اسرائیل هیوم: حملات اسرائیل علیه ایران با هماهنگی آمریکا انجام شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/657161" target="_blank">📅 07:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd48a928.mp4?token=E4lGiRzmq77lvTUILplPJtfAre8zDo54ilqZTwvs-sXaO0VDZF0tiLMvBkuOWsi0aFs3kXQ0bFEX_mlkFVDVy_0__H2uJNSR3E2B7zIsB1MBDYWShuHSBDGt8NgHSUNYNFc1jeMDqWASPVNsMa1TPGbPmJvAOR6xGtKrr71cyL-r9nkyh6vJ5fwUeks2YRqid7NIVmbTksilK6-epw5YbGrp1PasQE77LvsnXDlYrLAzCviT55dbFL9R_5l_VxlFeudDhOOPhGLmkXdwxd2trFL87vMi0pkjhhyQz7kQdlRcV8mQDJfhyZn0iN5-lYkT5J0c-ZYj7fsdLFrUO2idJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd48a928.mp4?token=E4lGiRzmq77lvTUILplPJtfAre8zDo54ilqZTwvs-sXaO0VDZF0tiLMvBkuOWsi0aFs3kXQ0bFEX_mlkFVDVy_0__H2uJNSR3E2B7zIsB1MBDYWShuHSBDGt8NgHSUNYNFc1jeMDqWASPVNsMa1TPGbPmJvAOR6xGtKrr71cyL-r9nkyh6vJ5fwUeks2YRqid7NIVmbTksilK6-epw5YbGrp1PasQE77LvsnXDlYrLAzCviT55dbFL9R_5l_VxlFeudDhOOPhGLmkXdwxd2trFL87vMi0pkjhhyQz7kQdlRcV8mQDJfhyZn0iN5-lYkT5J0c-ZYj7fsdLFrUO2idJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه الجزیرة: شب گذشته چهار موج موشکی از سوی ایران، شمال اسرائیل را لرزاند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657160" target="_blank">📅 07:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDBPNM6kXlZPt3VUre4j_VJCU6CU7ePZYS3P4AY3d6VkeTWGvqAgP59-c9pNV11JD6Y2kfJGMl8rDJpeqMdc330C1Ob59NZvov6kCBAbrv4dTRXYwmfxA3ZXBPQS8odoTL_o7qTTN51MoDgwSvaHh7pARQ9Pz6VOyxSJiXzbHHzTZqu0WbsrL4IRRa-KcRKFmxHdtBVPnd-rnFh525EORjDkM5YAdZ_gjp_Q07vyfLmWLsoPtOKRQzIAqVjPgHFAiPZNMxDfCWpqr5y8VLL2PQVgQcbzyV0UCqk0p-jjSct8AFvWvk5V2zByOdNKmWu9JTQ7bNowBzuV55bqWJTI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انصارالله از معادله وحدت ساحات خبر داد
«حزام الاسد» عضو ارشد انصارالله:
🔹
تهران-بیروت-صنعاء-بغداد-غزه: امروز در میدان،‌معادله وحدت ساحات را ترسیم می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/657159" target="_blank">📅 07:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سناتور دموکرات: نتانیاهو ترامپ را تحقیر کرد
کریس مورفی، سناتور دموکرات آمریکا:
🔹
این جنگ برای ترامپ و به‌طور کلی برای قدرت آمریکا تحقیرآمیز بوده است.
🔹
وقتی ترامپ اعلام می‌کند که با نتانیاهو تماس خواهد گرفت تا از او بخواهد پاسخ ندهد، اما نتانیاهو ظرف چند ساعت دست به حمله می‌زند، میزان این تحقیر بیشتر و شدیدتر می‌شود.
🔹
ترامپ مدت‌هاست که به طور کامل کنترل مدیریت این جنگ را از دست داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/657158" target="_blank">📅 06:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رادیو اسرائیل ادعا کرد که دقایقی پس از رهگیری موشک یمنی، پرواز هواپیماها از فرودگاه بن‌گوریون از سر گرفته شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/657157" target="_blank">📅 06:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d98e8541.mp4?token=b2S_QmmoXpnvJ1NpAtI6OGU1o9bUzViBAXkYmyTcYCKp4I799F5WgWpHn8OfU_ihm-as5RFDOyTFFDqUGnbbd0f00RoGg2vvrJ-t32mV6pnssnENvSoxAAYCt6zTlFMbKqlUVPQ82aEdKXbneYlqAS5Ry6bCw2Sn7beM2GagWTDH0H2-Vcfln27OdhA3VrQEIhjW2pcyXTnwcGy7J5eRtb1rnaOWjZZXyYBVh2fBSX4_jGiKJAtfgXK_HFiU3MDDUgpak395ezkr1HIbyfBpDNKeNEuiGDHkD4BVRnbnP-_LYbdg0zklQI18Tkl6WFWvEItFEbr605c7_RkX0VDFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d98e8541.mp4?token=b2S_QmmoXpnvJ1NpAtI6OGU1o9bUzViBAXkYmyTcYCKp4I799F5WgWpHn8OfU_ihm-as5RFDOyTFFDqUGnbbd0f00RoGg2vvrJ-t32mV6pnssnENvSoxAAYCt6zTlFMbKqlUVPQ82aEdKXbneYlqAS5Ry6bCw2Sn7beM2GagWTDH0H2-Vcfln27OdhA3VrQEIhjW2pcyXTnwcGy7J5eRtb1rnaOWjZZXyYBVh2fBSX4_jGiKJAtfgXK_HFiU3MDDUgpak395ezkr1HIbyfBpDNKeNEuiGDHkD4BVRnbnP-_LYbdg0zklQI18Tkl6WFWvEItFEbr605c7_RkX0VDFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۸.۲ ریشتری فیلیپین را لرزاند
🔹
سامانه هشدار سونامی ایالات متحده، تهدید سونامی را برای این زلزله اعلام کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/657154" target="_blank">📅 06:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حریم هوایی رژيم صهیونیستی بسته شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/657153" target="_blank">📅 06:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آژیر خطر در تل‌آویو و مناطق وسیعی در مرکز و جنوب فلسطین اشغالی به صدا درآمده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/657152" target="_blank">📅 06:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه‌های منطقه از حمله موشکی یمن به فلسطین اشغالی گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/657151" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در پی گزارش رسانه ها مبنی بر شنیده شدن صدای انفجار در پایگاه هوایی الخرج؛ یک مقام آگاه نظامی به خبرگزاری صداوسیما گفت: ایران هیچ شلیکی به سمت این پایگاه نداشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/657150" target="_blank">📅 06:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه‌های منطقه از حمله موشکی یمن به فلسطین اشغالی گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/657149" target="_blank">📅 06:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeRvVrq1WrqUYoLKSTBbGDEoyKQhb9ojgRsbFBCWHm_dotRgzGsB4g2v5z7YUMSNRstiLLJd1vL9_i5l1pkstEBByh7vtKfLIczQk-p71qWfDDTbQITLYbphSkfhYzviefNR1otHX45se8wtrw52v9Cmve2lsqBkBoQoAe54CgFtH95geww2jc9jX8QxPO1ar1alXF0Jqchf_Y73Xi12jRCUpU4_r7woHBx_BooBaOJR0pbpxpVmOPd2Z0U-MqIwz-hiHzfMLAq-pMKxP65f7tfSY4S7ELFIeBK-31SmGdGhfWoqdbLNtLAJvZJXHwoJP80kELktbtzDB7iLe_xaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر مرگ در اراضی اشغالی به صدا درآمد
أُولئِكُمْ جَعَلْنا لَكُمْ عَلَيْهِمْ سُلْطاناً مُبِيناً
و آنانند که ما شما را بر آنها چیرگی آشکاری داده‌ایم.
نساء - ۹۱
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/657148" target="_blank">📅 06:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نفت برنت به حدود ۹۷ دلار رسید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/657146" target="_blank">📅 06:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
برخی منابع گزارش می دهند که پایگاه هوایی شاهزاده سلطان در الخرج، در مرکز عربستان سعودی، هدف حمله قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/657145" target="_blank">📅 06:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیدن انفجارهایی در  عربستان خبر می دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/657143" target="_blank">📅 06:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی مدعی شدند: نیروی دریایی اسرائیل در حمله به ایران مشارکت داشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/657142" target="_blank">📅 06:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657140">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZzStTZZspuVEAW8TevylCsR11jSx0I1iaH0rX7KveSOYE2zreIhRIaF8l8Um54GYhkwlzvToyaJn9xJoM_a8SOZ8p-gORyCJat2coX-HlW_4jH6_R1zM6pwTfowl4F3sftWQwGkUBkZdCJWnZZzqPvXLSbl3687AUfDwl8yjBCYQ0ynNosL6QE7PEaw2XtZFno2o8A48eoj2rEVj-XFqfSAPIozmHUK-YaUS8AcoR4uRM_EQHJj9ytCV1azV4-E1mT3WsozdXjeLQ0shOk2Cz90ut7Bt4_LiiFOFO68RGon1ixxjlrhU5oI_Ibn7o3Ci8E64uUavovl3sNiW6hfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان سعودی برای استان الخرج، محل استقرار پایگاه هوایی آمریکا، هشدار اضطراری صادر کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/657140" target="_blank">📅 06:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فرماندهی جبهه داخلی اسرائیل: ما محدودیت‌های اضطراری را تمدید می‌کنیم؛ مدارس و مؤسسات آموزشی همچنان تعطیل خواهند ماند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/657139" target="_blank">📅 06:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657138">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به نجف آباد اصفهان تلفات جانی نداشته است
معاون امنیتی استاندار اصفهان:
🔹
این حمله تلفات جانی نداشته است. بامداد امروز نقطه‌ای در شهر نجف آباد مورد تجاوز رژیم صهیونیستی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/657138" target="_blank">📅 05:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657137">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
نیویورک تایمز: مذاکرات جدید بین اسرائیل و دولت لبنان با هدف به اصطلاح دستیابی به توافق بین دو طرف، ظرف دو هفته از سر گرفته خواهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/657137" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657136">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
فرماندهی جبهه داخلی اسرائیل: ما محدودیت‌های اضطراری را تمدید می‌کنیم؛ مدارس و مؤسسات آموزشی همچنان تعطیل خواهند ماند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/657136" target="_blank">📅 05:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657135">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای
کاخ سفید در اولین واکنش به تجاوز رژيم صهیونیستی به خاک ایران: آمریکا در حمله اسرائیل به ایران دخالتی نداشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657135" target="_blank">📅 05:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اطلاعیه آموزشی هلال احمر؛ راه‌کارهای کاهش ترس و نگرانی در شرایط جنگی
🔹
اطلاع از راه‌کارهای کاهش ترس و نگرانی در شرایط جنگ و بمباران به مدیریت نگرانی کمک می‌کند. بر همین اساس ضرورت دارد تا:  ۱. دریافت اطلاعات درست و شفاف صورت گیرد. اخبار و اطلاعات را از منابع…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/657134" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آتش‌نشانی تهران: نقاط شهری هدف قرار نگرفته است
🔹
صبح امروز دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است.
🔹
سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/657133" target="_blank">📅 05:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار المیادین در بیروت: صداهای انفجار شنیده شده در آسمان لبنان به نظر می‌رسد ناشی از موشک‌هایی باشد که از ناوهای جنگی به سمت ایران شلیک شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/657132" target="_blank">📅 05:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه پاسداران: اهدافی از خاک کشورمان مورد حمله قرار گرفت
🔹
سپاه پاسداران اعلام کرد که دشمن صهیونیستی با استفاده از موشک های بالستیک هواپرتاب اقدام به حمله به اهدافی در خاک کشورمان کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657131" target="_blank">📅 05:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای ارتش اسرائیل: تاسیسات نظامی در غرب و مرکز ایران مورد هدف قرار گرفت
ارتش اسرائیل مدعی شد که نیروی هوایی این رژیم شماری از مواضع و تأسیسات نظامی وابسته به جمهوری اسلامی ایران را در مناطق غربی و مرکزی کشور را هدف قرار داده است. / ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/657130" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار المیادین در بیروت: آرامش محتاطانه‌ای بر پایتخت لبنان و حومه جنوبی آن حاکم است؛ هیچ حمله‌ای در طول شب گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657129" target="_blank">📅 05:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادعای رسانه‌های اسرائیلی: جنگنده‌های اسرائیلی از آسمان عراق موشک شلیک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657128" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">همزمان با اعلام آماده‌باش سراسری در سرزمین‌های اشغالی، مدارس اسرائیل تعطیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/657127" target="_blank">📅 05:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اطلاعیه آموزشی هلال احمر؛ راه‌کارهای کاهش ترس و نگرانی در شرایط جنگی
🔹
اطلاع از راه‌کارهای کاهش ترس و نگرانی در شرایط جنگ و بمباران به مدیریت نگرانی کمک می‌کند. بر همین اساس ضرورت دارد تا:
۱. دریافت اطلاعات درست و شفاف صورت گیرد. اخبار و اطلاعات را از منابع معتبر دریافت کنید. از شایعات و اطلاعات ناقص یا غیررسمی دوری کنید. اطلاعات صحیح به شما کمک می‌کند واقعیت را بهتر درک کرده و اضطراب کاهش یابد.
۲. ایجاد حس کنترل در این رابطه مهم است. تمرکز بر اقداماتی که خودتان می‌توانید انجام دهید، به جای تمرکز روی چیزهایی که از کنترل شما خارج است. برنامه‌ریزی برای شرایط اضطراری، پناهگاه، منابع حیاتی و ارتباط با نزدیکان، حس توانمندی و کنترل را افزایش می‌دهد.
۳. حفظ آرامش در رفتار و گفتار نیز مهم است. آرامش خود را حفظ کنید و سعی کنید با گفتار و رفتار آرام، افراد اطراف را هم آرام کنید. جملاتی مانند «همه چیز تحت کنترل است» یا «ما تلاش می‌کنیم همه امن بمانیم» کمک‌کننده هستند.
۴. حمایت گروهی و همبستگی باید شکل گیرد. با خانواده، دوستان یا همکاران کوچک‌ترین گروه‌ها را تشکیل دهید و یکدیگر را حمایت کنید. استفاده از جملات تقویت‌کننده اعتماد و همدلی مانند «ما با هم هستیم و مراقب همیم» مؤثر است.
۵. تمرین‌های ساده تنفس و آرام‌سازی باید انجام شود. تنفس عمیق و آرام: ۴ ثانیه هوا را وارد ریه کنید(دم)، ۴ ثانیه نگه دارید و ۴ ثانیه خارج کنید(بازدم). این تمرین‌های آرام سازی را انجام دهید. پنج چیز که می‌بینید را نام ببرید(صندلی، پنجره، چراغ، تابلو روی دیوار، کتاب). به صداهای اطراف گوش دهید و چهار صدا را تشخیص دهید(مانند صدای تیک تیک ساعت، صدتی تنفس و ...). سه چیز که لمس می‌کنید(میز چوبی، پتو، لباس خود). دو چیز که بو می‌کنید(قهوه، صابون، خاک، مواد غذایی). یک چیز که می‌چشید(آدامس، آب، یک تکه میوه).
۶. تمرکز بر حل مشکل، نه روی احساسات مهم است. روی کاری که می‌توانید انجام دهید تمرکز کنید، نه روی اضطراب یا ترس. آموزش پناه گرفتن، آماده‌سازی جعبه اضطراری و برنامه‌ریزی و شناخت مسیرهای امن از جمله اقدامات عملی هستند.
۷. استفاده از روش‌های مواجهه فیزیکی با ترس باید مدنظر قرار گیرد. در شرایط اضطراری، تمرین‌های عملی برای کاهش اضطراب و تقویت تمرکز بسیار مؤثرند. یادآوری کنید که ترس موقت است و اقدامات شما می‌تواند ایمنی شما را تضمین کند.
۸. مدیریت زمان ترس نیز مهم است.
بپذیرید که ترس طبیعی است و کوتاه مدت خواهد بود. با تمرین و توجه به اقدامات ایمنی، قدرت مقابله با ترس افزایش می‌یابد.
۹. حمایت روانی پس از حمله باید صورت گیرد. پس از اتمام بحران، گفت‌وگو درباره تجربه و احساسات با افراد مورد اعتماد، کمک می‌کند استرس کاهش یابد. ارائه حمایت، بازنگری اقدامات و یادگیری تجربیات برای آماده‌سازی بهتر در آینده مفید است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/657126" target="_blank">📅 05:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رسانه‌های عبری: اسرائیل درحال آماده‌شدن برای پاسخ موشکی فوری از سوی ایران است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657124" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کانال ۱۳ رژیم اسرائیل مدعی حمله به فرودگاه مهرآباد تهران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657123" target="_blank">📅 05:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرنگار المیادین در بغداد: صدای انفجاری با منشأ نامعلوم در سراسر پایتخت عراق شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657122" target="_blank">📅 05:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدای چند انفجار در اصفهان شنیده شد
دست‌کم صدای ۳ انفجار در اصفهان شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/657121" target="_blank">📅 05:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارها در بغداد و بیروت
🔹
خبرنگار المیادین در بغداد: صدای انفجاری با منشأ نامشخص در سراسر پایتخت عراق شنیده شد.
🔹
منابع عراقی: صدای انفجاری در منطقه طرز خورماتو، استان صلاح الدین، عراق شنیده شد.
🔹
در عین حال خبرگزاری محور نیوز گزارش داد اشیاء ناشناس بر فراز بیروت و بغداد دیده شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/657120" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانه‌های اسرائیلی: اسرائیل در حال آماده شدن برای حمله موشکی فوری از سوی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/657119" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تسنیم: صدای انفجار در سمت کرج نیز شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/657118" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
اخبار تکمیلی متعاقباً ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/657117" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657115">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارتش تروریستی اسراییل با هدایت سرویس اطلاعات نظامی به اهدافی در تهران و غرب ایران حمله کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/657115" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
