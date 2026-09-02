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
<img src="https://cdn4.telesco.pe/file/Mw51jRYg7_Ij66wchzLCKonqFMuLWzUkOdp-j4ijMrD036jxt2pzysbAu654XKR9DMQ18o815_P5LxpMeXcKv7ztWNoEItPF22WWUKQpD2Ob76yAIg0Xlkalwhqu7s-DstTr8BKhsc0OK3bJ76vzTL8HoXhCDlSpHMBB9Q2q3fg7y8Ey02OLY2jj4FTzDy8lL3pYreompPHv7zfmTgZSe5ExdAC7YgwHsxQnB2l9aXDKctbVBfCThOE7IRUT6OhDdS6URNysPwkuaPTatNxazQr1ulD1BkzZ_CTFiBTnpg9R2r2RDTGnh-tpeWTkNCu2zFht3PzYXs7nhe0E8hAx9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-686679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fe8455fc.mp4?token=sUvWAV2cREmqwlS_JVPtAWtkFRk7i0ac_-6pSPih9IuxrUWk9MvMlypCQnJJCdje7TLGRf6tQ4UqFOSpu6wl9nWmAb0hsMsTz_XlpWKwdy_gbdfe8QjXuT0bI490D9xo338UYlE0kg8nHaq7qjKmX_gKlqKmk9sqSqEygH_2eswqFy9QV2UBi6Iv39ZhYZuOFtHDCHCS-Aj8n662DgRMkkKJhDHgX6FtviiyD7cZSj-Gl9fqmypW2x2WfcN5gIkp8ZP0muxLBRx9GuiZDfNvyjSRr3PCzWELw4rQKewx_Ch2QbpxlUYc_HsqQuu63dMm6e8VkBi8lCAXyZs5AKaVtYQQUvV3-Q5OTYXAPE5dGYk1rdSp0bPqpQCZZK7ROjD69vtPs76e5kB5R-5sNr9Di22cTpgmUcEo8C21EipxFeM6Rf6HfdHyCZ3RF_kpCYATwG2Kp5wwwVJ6EdyeCK7GeoWtrM1ogYv_y59CT8H8AoPsceO0khaGeiGoHktNAzjMl21GI6n8O65QSd_m4cDwLCdJdU0vueiKD9m1AWk8mrktQ02BLZJIj-OF83Fjx7kbbfjS4fnEBvcFDIRzuVG_ZS4NXTZe_q37TU4JopjmryjPH6NKKRYY-7AaWVfMW4kzBsws89YEXx-sU5Sby8H38fRn2mYtGRDpKfMOh3sNMKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fe8455fc.mp4?token=sUvWAV2cREmqwlS_JVPtAWtkFRk7i0ac_-6pSPih9IuxrUWk9MvMlypCQnJJCdje7TLGRf6tQ4UqFOSpu6wl9nWmAb0hsMsTz_XlpWKwdy_gbdfe8QjXuT0bI490D9xo338UYlE0kg8nHaq7qjKmX_gKlqKmk9sqSqEygH_2eswqFy9QV2UBi6Iv39ZhYZuOFtHDCHCS-Aj8n662DgRMkkKJhDHgX6FtviiyD7cZSj-Gl9fqmypW2x2WfcN5gIkp8ZP0muxLBRx9GuiZDfNvyjSRr3PCzWELw4rQKewx_Ch2QbpxlUYc_HsqQuu63dMm6e8VkBi8lCAXyZs5AKaVtYQQUvV3-Q5OTYXAPE5dGYk1rdSp0bPqpQCZZK7ROjD69vtPs76e5kB5R-5sNr9Di22cTpgmUcEo8C21EipxFeM6Rf6HfdHyCZ3RF_kpCYATwG2Kp5wwwVJ6EdyeCK7GeoWtrM1ogYv_y59CT8H8AoPsceO0khaGeiGoHktNAzjMl21GI6n8O65QSd_m4cDwLCdJdU0vueiKD9m1AWk8mrktQ02BLZJIj-OF83Fjx7kbbfjS4fnEBvcFDIRzuVG_ZS4NXTZe_q37TU4JopjmryjPH6NKKRYY-7AaWVfMW4kzBsws89YEXx-sU5Sby8H38fRn2mYtGRDpKfMOh3sNMKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار سازمان ملل درباره آب شدن جهان!
امینه محمد، معاون دبیرکل سازمان ملل:
🔹
رهبران اقتصادهای برتر جهان باید روی یک جزیره مرجانی اقیانوس آرام بایستند تا واقعیت افزایش سطح دریا را ببینند. افزایش سطح دریاها در اقیانوس آرام روی دیگر این داستان است و گرمایش منجر به آب شدن سریع یخ‌ها در جهان شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/686679" target="_blank">📅 20:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6730a56a0e.mp4?token=P1_ScNeyef3_4LZ5My-xzwN0Hw70-T3AO46sUPBAqkLBGvpPBKyd811cdGZKeE3e-J1A3QfnUn6LgN6FWiG9TF186tll-zQufOSg3YwAUIIkKFd_oA9EQ1ChqpM_IXb0HkF95HO-vz1sayRznd3NKGI3iR42IRZ_SyNW5wsrehyj7CEt5ZotP_UH78mO-jnh0o6lB3CeQQVTUEGuIQ9crfMsu4p4f3smQtj-emmC8j36DggdtpZd4KnSKaEhYNMB_MzynhYlceQF71_5F7SrF-AJs9hIW35D6-RGutFbWwKBI97rqrkHKdH-hPeY38_eHOiafT1tztBVbqnbL1syXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6730a56a0e.mp4?token=P1_ScNeyef3_4LZ5My-xzwN0Hw70-T3AO46sUPBAqkLBGvpPBKyd811cdGZKeE3e-J1A3QfnUn6LgN6FWiG9TF186tll-zQufOSg3YwAUIIkKFd_oA9EQ1ChqpM_IXb0HkF95HO-vz1sayRznd3NKGI3iR42IRZ_SyNW5wsrehyj7CEt5ZotP_UH78mO-jnh0o6lB3CeQQVTUEGuIQ9crfMsu4p4f3smQtj-emmC8j36DggdtpZd4KnSKaEhYNMB_MzynhYlceQF71_5F7SrF-AJs9hIW35D6-RGutFbWwKBI97rqrkHKdH-hPeY38_eHOiafT1tztBVbqnbL1syXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یه نکته‌ کوچیک، کلی دردسر رو کم می‌کنه!
👀
این چندتا ترفند رو یه‌جا داشته باش  #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/686678" target="_blank">📅 20:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/686677" target="_blank">📅 19:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkspnN2SLL6wLCKnY7hRo1WHKK7bsFugQjQId5TIyMgaI_K7fl_OM8dC7HOY9KVDSz_vzEhoud4wqWjtnwV346LIIuu2hxouu75EjWu5AG4XeWGdVUOcBvffJNEXhN96sH28uQVaHNHNHd3lFW85TSuiimOd7DVu3jvXz4kxUuHpzLsTBx_5uGv5Z6eVsxFm14FreWXPPT2-PUmFgYLaGcbYQ66FlvDBA-x5SC2rBaGYfZhLASdjoFbkuIG4Yo94ag2U2BfqCEo7Ss-SZoE0WkIoXZprO6GJvOV_AY_ANXsuwor-k5w4E4FlM05hQ8pVbWj-aWHBZRyKiw-OyrBnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول بازیگر اول بازار ارتباطات هوشمند کشور
🔹
بازار ارتباطات ماشین ‌به‌ ماشین به یکی از بخش‌های رو به رشد اکوسیستم ارتباطی کشور تبدیل شده است. این بازار از کنتورهای هوشمند و کارت‌خوان‌ها تا سامانه‌های ردیابی خودرو و تجهیزات صنعتی را دربر می‌گیرد.
🔹
به گزارش اقتصاد آنلاین، تازه‌ترین آمار فصلنامه بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی نشان می‌دهد همراه اول با سهم ۷۱.۵۱ درصدی، جایگاه نخست این بازار را در اختیار دارد.
🔹
در این بازار، ایرانسل با سهم ۲۸.۲۹ درصدی در رتبه دوم قرار دارد و سهم رایتل نیز ۰.۲ درصد اعلام شده است./ اقتصادآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/686676" target="_blank">📅 19:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f262048d3f.mp4?token=RvLxaEA85GYdjKsPcukW17u217IMGh04inVh-_s4SI-VJeOHBzAb-8cggEPlvIgtLe8ENmeqYFAtC3o4A4DyZ3CaBIa_rXPPyZ3w4YNe762HbLDDLb9sbYv3r9YVeVBG_swIEVNZC0z27Zk-mDwwetyhyDuIuBEyLy79v9Ohmvs_A00nzuGrPi-AXPLD-neTxz5lbbQ1tZS3bjioM_UOJcdk4-A4KPE_V7B5e_H5dnQULwGBUqWVp5fbLWF3_c-nSCfONN6ASBX08jIWJXoRU-9Gu_f7DFttyV6dyJwT7Ip95UwbzbPodalnvWbXlPa9SH0ELCGSgnOnG7-MAUeuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f262048d3f.mp4?token=RvLxaEA85GYdjKsPcukW17u217IMGh04inVh-_s4SI-VJeOHBzAb-8cggEPlvIgtLe8ENmeqYFAtC3o4A4DyZ3CaBIa_rXPPyZ3w4YNe762HbLDDLb9sbYv3r9YVeVBG_swIEVNZC0z27Zk-mDwwetyhyDuIuBEyLy79v9Ohmvs_A00nzuGrPi-AXPLD-neTxz5lbbQ1tZS3bjioM_UOJcdk4-A4KPE_V7B5e_H5dnQULwGBUqWVp5fbLWF3_c-nSCfONN6ASBX08jIWJXoRU-9Gu_f7DFttyV6dyJwT7Ip95UwbzbPodalnvWbXlPa9SH0ELCGSgnOnG7-MAUeuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلاب سهمگین در تگزاس آمریکا خیابان‌ها و منازل را غرق کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/686675" target="_blank">📅 19:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9fee4971.mp4?token=fD9IOC--ZIrS-A8UwuYHN0varonJ3txC_C7EOgOAnrFBlX9gXW7lm0Osj4x64kao1Mx_7xEPJicLUbs37TG0DgPXEqP2MidcKhTgfdUv-L4Rig8o1yyJowV6Cq4kZxBRBuTkxvsV8mp9yDcQluFJc_Xa_3FWyerhpohWG2pKzbRZimYKQOfncH1SD8oN2CsyWd-qTiLhT0mE-RxNpDH2whxAqQBWZ-NYnAdHQ62w_ydUWK_JEmIxnIIoQgdM-CQ047ZnuZw6Me1PLDtUFwp7TbCZAbZepGWfn_gNyD4juGwrIJjtEwHLgLZv3ZIVzdPLIe4HCSBA--wCOZo7Dzz_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9fee4971.mp4?token=fD9IOC--ZIrS-A8UwuYHN0varonJ3txC_C7EOgOAnrFBlX9gXW7lm0Osj4x64kao1Mx_7xEPJicLUbs37TG0DgPXEqP2MidcKhTgfdUv-L4Rig8o1yyJowV6Cq4kZxBRBuTkxvsV8mp9yDcQluFJc_Xa_3FWyerhpohWG2pKzbRZimYKQOfncH1SD8oN2CsyWd-qTiLhT0mE-RxNpDH2whxAqQBWZ-NYnAdHQ62w_ydUWK_JEmIxnIIoQgdM-CQ047ZnuZw6Me1PLDtUFwp7TbCZAbZepGWfn_gNyD4juGwrIJjtEwHLgLZv3ZIVzdPLIe4HCSBA--wCOZo7Dzz_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دقیقه یک بطری انداختن شروع شد
🔹
طرفداران استقلال هنگام کرنر زدن بیفوما شروع به پرتاب بطری کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/686674" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/686673" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686663">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaNL5keODMjwVN-PnWxOjtYoaTShcpS0ImV5rcv1O6fKNPJHR9lJVqijRZFQoltAjva57J_Okuob65d2jGuFgiPXvSzU09y7DenveeJ5PCo88Ir9jTkHiNSYu5mw1LP_GpoK8mNHR4hgu_kJu1SDx-UxgBPdsTogrBvga9qR5p02UMVmOgRjkblUBlomrAWDxaWNVJY4yYW-ilLfOjU7zeiv_D1_hyqL1OCkTUy0xsQ2gZT6nAQt10I1-Su2FIe2nXKwLqzuG9VvMfJZSEniseYZQrHuHOwVeW_lxTVS7HlE_Cd-z60u1k6h9ppeYUq3ROqpE6hw8OusjhqSKQTJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIvn2fDsna-BnI8O7pg3swxNHyYcJsjyIE1zPNzzL73FqnocWLpwsxBgMSWN1uFIlNS34g8ym20-NmLmCP6YRNj-DeajequJlNOctAnXUZ_4-igGrJpgXJFUGQ_VwfCx_PztXBaNK1MhJAtSzsPu2W8QpKXKjnpZ75JjWbdKJ7pg7hEWltzPWBIs7PkxY2HLZSaTuhvfBC8sDFY7Is6C0Jo4CSBHt5yxSYdO4-Qbh38tvZEwwas7teCeRhbe1fj7DmX-IwUMlofj2AaGMYhyGVcHRB5Zop1W-F5_uoVKPfgK6gyI5idA4I0IsCVRJmeR635YEpJsct4smTRRbkOxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkYQ0ISjsY6_yqjpeL2VNiEyZgyDC0FcrOpx5vQXL4IElys5WFG2dzEHxzo1ZwyHNukgubeM7LiCFptp9t2l2IQztzYy_1qPKcKgAfidtw-XPqiOmscEUeQiCbBuzxVhtHNr-02dE_wKeqlEU92RisQxwj1aFpVx_j0RHy6JhV7VNKnS6K8TwpyIB6DPIlvhUMbJsXzLXcDPz5GM0v8gwFXFgfF5koe6g5uFvkf5U55FrL6PrUsIrTIB7Kw1bIOdZhmkNVnvjNit6GfVTzsxdhs30aOGeE900u-aHTodkQDJEYuGLWET3tu8Elb_QuG7XqxF-JiNHYdbb4zmLx1b9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwNYYXVrYdexTqx6w50ytQYSu2DD-Tx-lxaHcrXdwJ-h43v1BQfXeM8aFhhMgO3K0PxkcfIiWepyCZ3vcuk42jYmycxz6vWhyg0Rjby4DsG4aQnd-V-SrAKrIx_JSOnVnr4d44LNhwlULhVgRRyNyc3qmrhaCMZsw21Cls-Lzp4MJK9J6jV0ipL59cOvoOP5MTUAcpWustEK-bHosnsmuZfWF4WLYUisU98aphtDGeQAB1Xc_VOFNqjObpktfZ957VynTcaeJPKZ27qGMaPmN6J55M0-neehPgCc9A8DOUwVGBTBWYPP6qCVo3MBeUCIPeFYhj6jjX5bGmaH3uxGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwQbhgvniKmkYqotzGhduMjOGaeZXFyULwd2gTE6q19ATRnWfZnKvqGjjgVN7ZhE5kbvBCWtcHvtCeL0LG1JvfrgFvXchWdqyCyakn6JMCyQyhDfMEYwE_F3EFGcHoz2bjCeIVMA9_20nRMB3mHNnG8ExbJg2jHsDjpMOiDDCzOBl7H_Jrts1hkEMg7NYYzW_--s0phejlHZxRGxOu6gFyn4RKL4Ea7EYmefuPPvp4r3OdyueiXU6aqc6uWOXhrqXrst41MpDsdma4NpzYPdcfYbIQ3sK3CQIG03Kb2uoLkE2-TgLU6fFWN0OYhnOLobglCkczmbH-4oTcxhqziu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QASivp7yqGm90UYEtOQg911Lndu4p7oz-srufjWQeipPwc3DqHmLjWfVoiD8gu6zerRC6dJiAtESPfVGVEt5_9Ub1OmnVJdUPAo2P0wS3aryZYgZ88D82qqsOQHm2xXyb4yMfyrN01ZyHp3-9g_Wwn7U3JdX7OPJY1SFHx-_UPvmqbtfsQhm_SNVMJU1StmYrgFApJ6bvk7qcuFlhUGUWC-NK2rL5TFxpInG0RBKeF3GSlzUj_oNwFcsX2Cqscpj26ERZsrCkMOgGa7v3i69Om11fcnA10OQ01mGldV3p8RPcqzS21ruGuXMcaJl_9ygBTgcO64pJZsZ9kPNGce8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG0UCxocBVoqdsXGjzKkb7gf5P1Oj5RGXaEs_cWo2s-KyWDKd2a6A3Zfc4LS8ZMS_Bc8Yq2-PxlzMJu5fnxNyNYp6ikNIm_2FkSUPSgGVg3c1-bW4yCJ_V_P5484TfBJV_eP8CGs2qPUovyvvCOpuJSxzyiWJDPL9r8mNbbOp3VKCetZei_HrDaII9QsCWlPMOx7XLbTmnL_DrTRsHtoevaQDcIG2TrUvs6jofRT0zbyETPX_RItnRAaP4C-SmmVH2rT1_ZQ7F46IKDj63x4DEfH9I9914m3OF7j2ofNhHShNY_XeShEcLXcDNjeni2cRL9jsyhD0b0wNSC5G_W5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPr98t0PhE4okUDkMXRaNbTXITDFhZqIqDMm7Sa5yjgRbeI1DjpjzOh7iYO94jt9JlE_Bs7l3iNtwFlsct74-7KzboCPC3jF696BoJNGCwIOqikUf9tNtIaNRVMQ1bmamIeKge2h4LgnTZzaR_ZB_EFl9aUFGHvcJOvRD9ZEY5P_dohGtSLwo9IDezXP1cnkcuEZYgFFIvoGNAoJfASnHArebHccTIQvL_BUUuLoxprOHc0Mlup7TV8BoUikGBTv731IcduFLtjfqL3WQ6V76lF_jwv-0NxRr2MjlFHu-3eRer5KwhXPyMAY6wzOGd2uPix6jao5a59i0obSXNQhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrElHxjzV5XGUQxlhyBGY5viVcvcL6VEOCQVw58VOZoqo8opkhGbePETLYFZw_Lh3CgMLiPC1zFm3CID5RTePS9kDqjNr-PFjb-m6sxNPx-6pEmIHOPujQwvxmVYSYRw2z2Byglg1VpGekQaceTcwyv2z2VMW6bLSlXnE80oN2KTLzZORWn9E5p4xiTDCuS75V7KKo-5lCtYYnyRJJB6Q7lVCCSRMMAPA3Cs7RKquNJq6a85efzL6fkE0BrlxO3gbPIXVORDMWeIg939INJEZ46CGra5Z_hW09pvnJXGH4Yy-cAlVHrWXpQgKj1g5RfrZAiM3nptPLH_QCN1lNljNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKZZH-ODwVhthjVAXGAUsuDN-CwT4YpSwdnJ8gSny5a4BwGw-NsBLvGSPjfn9Izu9oinxNzVprxrSIKrE8XN8NgTYu00Caz5-YEOW7QT60ZdyJX_rhbJGF3D9WMzkMYKefzDIlB0w9-WfGRSVluVooQVotsMtbebOJbeCxJGQYmA0L54gJ3Ny0PEOUsY_O6La1KPLjpFHnGdqaVFveBAFoS4bLu8BG1bgijBMPSSzY6o98uzYFHO_zHfELcRq5Ndv-lJ6JnP94SJ3hNo4SsINJ6QRzf8HInyKSfm7Es5_Bodob8uvPk_gev0p37oU_XtjIjY9gxHcF4P-w2YsRl7iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید مدیرعامل بانک صادرات ایران از نمایشگاه الکامپ/ رونمایی از محصولات نوآورانه توسط افشین خانی
🔹
مدیرعامل بانک صادرات ایران با حضور در ۳۸ امین نمایشگاه بین‌المللی الکامپ به بررسی آخرین دستاوردهای حوزه تجارت الکترونیک و فناوری‌های هوشمند پرداخت و از ۲ محصول نوآورانه این بانک نیز رونمایی کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#الکامپ
#اخبار_سایت
#بانکداری_هوشمند
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/686663" target="_blank">📅 19:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686662">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xvlfv5VMsyKfJHBKaFZe6KiobAmsmBAlC-1hxoMtePgn1ag0CgNkVg37dUvaYYhbJdlWcFgllLywBCpYuexA3Ek8pypSb6Xl9CTX8smLhLpge9YzwS5MdISmQhFXGeMrN7vRbvbS9udVNSXSoOat1wPcvpQAM9z5DKarkZYznHc_EoOSsSgJUNDrXF0Mjp5lkv_yOfztZ0X2hFs2GR-gnOgtWT91bSgwL4GKjNIH-ijyznnVY0_R6P-unJXrPHrQ1S38qaoEjRJ3RUjwaRu0VZke09GQjp7q7oOhZmiiAxxtkK691Ix4xYJXJm4pG3295QBrue3BAi0EgGL7hMSIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ نشانه‌ای که متخصصان می‌گویند نباید نادیده بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/686662" target="_blank">📅 19:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP0DTlKm0eR380VycBg7oIpX2NBo8Udn4quRBGJgmwUeNZFbmY1tkgYgJLCRde7CzFQeto6z4ovijgnXXjQOJkcIhrywjgS7dmVQgGBOi1pnnMiPFKzxyu7oAfR9H6Qxfm4jCB-Ui6YckG41BkCKH-LBx-Dbia9oVucW_Smh9cS3K09hqMEgEqOJDjcSs1RoDphHHoJMhkDDo7g_NFJ99DcTQYU0TeePf0j-QjeVhGA6TXMB_ocYlL-Gtv24z6cyBEEBAIwbgLDEx1savDT-jakpVT75i3YndvBvOiK5RKzJuLZDVnALCp8aig1DZLDc88y38zvhWPxMKO2grxU49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محصولات ایران خودرو باز هم گران شد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید بدون پرداخت مابه‌التفاوت، فاکتور و تخصیص پلاک برای مشتریان انجام نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/686661" target="_blank">📅 19:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32586f319.mp4?token=UunHrSe-pyzGvqAZW-SSWBtCHwH6WWNiZfwWFR3ihFuakcqIL1y-PJ9jyKKDC2H7dhR2gTAO6w8UaCUz0_zm22Rm66zPqUa2Ezq-1SxzIjVUd632emDgRe2KI6NhXamdZP2cSlcq5pRKZ3SVTy2jzze8SCGTCxtPEvsIc3matQnfmzZ0fo1dXk5iPkLTCxm88p0re1GdGOaB3ms-UkhIImnzyUnxxfUjWUGgxAMqboqgyi8pMA2bXHa-kmAcHJSaQz1AVrxcR-zT6LcOmgb_1gErpfKQk6GQO26IllPtvFGx0myDQdrEpGSQmio0YYUpEBFm9LhAeCV8EcAWWAe9uKZQGa_sVxfYzTdxWuZaI3-V4xZ_czEzc0HT7QkuVcZBd2OWHfGi05z7KKYk7mCMzKGOWdNwqao8lpS6UCMFZyZAUehmzI2MKnNGogUjszv-6Lgs7O96VqqqqFVpfmvpBwG3H9Mw4aUOClmYBtF5rLDm1vwIzW9qZ67QQXFdJ4r-u4l5FvZuj2bXNo2q61onbOX6zK-931NvU20Hx_A_dXDUwHBkXMFZgjmPWY2dJSisYFmypvEM4B-uFUfpknXV3fi8nvR1PxpwSYqbdiRlgMKWBFqpDvsWYr714EdEZZDOUdTJG6KUomrVX22-Nf5RMZbXTfO_G2nEKyL02TjGt-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32586f319.mp4?token=UunHrSe-pyzGvqAZW-SSWBtCHwH6WWNiZfwWFR3ihFuakcqIL1y-PJ9jyKKDC2H7dhR2gTAO6w8UaCUz0_zm22Rm66zPqUa2Ezq-1SxzIjVUd632emDgRe2KI6NhXamdZP2cSlcq5pRKZ3SVTy2jzze8SCGTCxtPEvsIc3matQnfmzZ0fo1dXk5iPkLTCxm88p0re1GdGOaB3ms-UkhIImnzyUnxxfUjWUGgxAMqboqgyi8pMA2bXHa-kmAcHJSaQz1AVrxcR-zT6LcOmgb_1gErpfKQk6GQO26IllPtvFGx0myDQdrEpGSQmio0YYUpEBFm9LhAeCV8EcAWWAe9uKZQGa_sVxfYzTdxWuZaI3-V4xZ_czEzc0HT7QkuVcZBd2OWHfGi05z7KKYk7mCMzKGOWdNwqao8lpS6UCMFZyZAUehmzI2MKnNGogUjszv-6Lgs7O96VqqqqFVpfmvpBwG3H9Mw4aUOClmYBtF5rLDm1vwIzW9qZ67QQXFdJ4r-u4l5FvZuj2bXNo2q61onbOX6zK-931NvU20Hx_A_dXDUwHBkXMFZgjmPWY2dJSisYFmypvEM4B-uFUfpknXV3fi8nvR1PxpwSYqbdiRlgMKWBFqpDvsWYr714EdEZZDOUdTJG6KUomrVX22-Nf5RMZbXTfO_G2nEKyL02TjGt-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات نائب رئیس مجلس درباره نامه دبیر وقت شعام درخصوص ابلاغ قانون حجاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686660" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=NhPjjDtEz-kIDFqRwPFszKfKfz7VbkukAmCztyiVVcNHEABZbWSn3q1EOmP5ShpJPZDG-n207riuGUjYKDTs_a1QCyD3veUEMuJ6huhes7za65Dzz8xr46cyNP8DkC4_j3vI9RXk-FdeklgKRUtMvDcA3iHig_J_rjvNDNC5njphnWsUD920xWjg-HmnGxyT8AQhPCMpYmkeJ4ghKF3axKQCRx75fotmrXnWVNdHrU7KzWmCnDFfY7xKXkwIgMuDJHA9ayc4oFPopksQRPLeBYue5aKHIcRwivig3amUOGokomamqk8omzVvaYQvT6zvlMpKwYW91uPJllMMmPjdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=NhPjjDtEz-kIDFqRwPFszKfKfz7VbkukAmCztyiVVcNHEABZbWSn3q1EOmP5ShpJPZDG-n207riuGUjYKDTs_a1QCyD3veUEMuJ6huhes7za65Dzz8xr46cyNP8DkC4_j3vI9RXk-FdeklgKRUtMvDcA3iHig_J_rjvNDNC5njphnWsUD920xWjg-HmnGxyT8AQhPCMpYmkeJ4ghKF3axKQCRx75fotmrXnWVNdHrU7KzWmCnDFfY7xKXkwIgMuDJHA9ayc4oFPopksQRPLeBYue5aKHIcRwivig3amUOGokomamqk8omzVvaYQvT6zvlMpKwYW91uPJllMMmPjdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: رژیم صهیونیستی حملات خود به جنوب لبنان و منطقه علی‌الطاهر را با شدت بالا ادامه می‌دهد
🔹
از بمب‌های ممنوعه فسفری تا انفجارهای مهندسی‌شده در روستاهای جنوب رودخانه لیتانی.
🔹
هدف دشمن، اشغال منطقه علی‌الطاهر و ایجاد منطقه‌ای ایزوله با از بین بردن امکان زندگی در این مناطق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686659" target="_blank">📅 19:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686657">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کرونا صعودی شد
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس داده‌های نظام دیده‌بانی عفونت‌های تنفسی کشور طی هفته اخیر موارد مثبت کووید-۱۹ افزایش یافته و ۸.۳ درصد از افراد دارای علائم عفونت‌های تنفسی، به کووید-۱۹ مبتلا بوده‌اند.
🔹
همچنین ۵.۵ درصد از این افراد از نظر آنفلوانزا مثبت گزارش شده‌اند که هر دو میزان، در مقایسه با هفته‌های گذشته افزایش داشته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/686657" target="_blank">📅 19:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686656">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5338e0f8d0.mp4?token=rPYyM7qSWSB7BBmQyZo12g2ZSnboZ-k4yyhSCJAiJuSCRYxVwBP2MvMpCUr6vilVg-UUPOr_FUNh8txM_DRzIdHzFxZb7Npua5vWCTGzqzyinlYb6E31yPHSI7jPMDabcf9F7PDmfLhKoIyKCAC7-eRBgdhsHQszH5ewEb8ugh2wyUp-MGDQ5r7IZttaXrpGqS5KAIyYf5Be9Y1TI3BKa6UiS20bJzC7xAnYYVAUw2OtXlvNYFZz7p-cMm4FsKYJD4-WKoopHvoB7uLy-GW92utJLIkfriGLkHcnr7wwgKJo-x41lDoVyaDG9oEUYRUtdiJuZsc0mNBmkZK_7Q1lnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5338e0f8d0.mp4?token=rPYyM7qSWSB7BBmQyZo12g2ZSnboZ-k4yyhSCJAiJuSCRYxVwBP2MvMpCUr6vilVg-UUPOr_FUNh8txM_DRzIdHzFxZb7Npua5vWCTGzqzyinlYb6E31yPHSI7jPMDabcf9F7PDmfLhKoIyKCAC7-eRBgdhsHQszH5ewEb8ugh2wyUp-MGDQ5r7IZttaXrpGqS5KAIyYf5Be9Y1TI3BKa6UiS20bJzC7xAnYYVAUw2OtXlvNYFZz7p-cMm4FsKYJD4-WKoopHvoB7uLy-GW92utJLIkfriGLkHcnr7wwgKJo-x41lDoVyaDG9oEUYRUtdiJuZsc0mNBmkZK_7Q1lnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش عالی هوشمند روی ریل فناوری؛ تفاهم وزارت علوم و سازمان فناوری اطلاعات در الکامپ
وزارت علوم و سازمان فناوری اطلاعات در الکامپ ۲۹ برای
توسعه خدمات و
زیرساخت‌های هوشمند و الکترونیکی آموزش عالی
تفاهم کردند؛ همکاری‌ای که قرار است زمینه اجرای پروژه‌های عملیاتی و توسعه زیرساخت‌های فناوری آموزشی کشور را فراهم کند.
📍
سالن ۲۷ | پاویون دولت هوشمند</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/686656" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686655">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سرمایه‌گذاری ۱ میلیارد دلاری دات‌وان!
🔹
رئیس و استراتژیست ارشد گروه ارزش‌آفرینی دات‌وان: طی ۱۵ ماه گذشته ۲۷ شرکت در این مجموعه ایجاد شده و تمرکز اصلی دات‌وان بر آماده‌سازی زیرساخت‌هایی است که بتواند زمینه فعالیت و رشد کسب‌وکارهای جدید را فراهم کند.
🔹
بابک زنجانی افزود: طی ماه گذشته نزدیک به یک میلیارد دلار سرمایه‌گذاری در مجموعه دات‌وان انجام شده و این مجموعه معتقد است باید به‌طور جدی روی لجستیک، فناوری و رسانه کار شود؛ چراکه این حوزه‌ها می‌توانند به حل بخشی از مشکلات کشور کمک کنند.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/686655" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686654">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxSvQp3-XVg8qem8_hyiuUVxJS17P32Oyp2BV2lQ6UcIp_HhUJbo4zFFyioIB5YgPYvHKYX5FpH5tdjFry5UcQjdArzX1rUaDSjDHqGhAu7NT_yfI-UrafkjGf1A8rVfN1DZwRC4FU_envS21Vnw1w-OOS8ggmW1xPwJSx1gm2De7Av8IBvHp5Gbl8TFZ4APUpwub2y7xdCqYmvRZJRNVdIDKv-ayYFru0dA3NPQS99zPZ2rZsvZRuxr8rYabfgCZ2PBPbPpcRab5AneL2Gwy2jOP3jLoH9xNVpuk172XirvIb7FdffQdVXkB5y73NBcGM8YYcUlgJSUME4hH07zTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم: حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به تنگه ترامپ تغییر دهیم؟؟؟ مثل خود آمریکا، «داغ‌تر» از همیشه خواهد شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686654" target="_blank">📅 19:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قوه قضاییه: صدور حکم اعدام برای احسان خدادادی کذب است.
🔹
زمان ثبت‌نام آزمون وکالت از ۳۰ شهریور تا ۵ مهر ماه و تاریخ برگزاری آزمون، روز جمعه ۲۰ آذرماه ۱۴۰۵ خواهد بود.
🔹
آموزش و پرورش: معوقات فرهنگیان بازنشسته پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686651" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d3da04bc.mp4?token=B5CTTSRWa4-PLVSe-_k4TEhUWs47t3sjE-Xi0QcLIUGmcY3Ba-xSyggcSrWfhkqJEFzLeK6bdPpMbihjfqS4qk-h2geMmfvrtNiTDwMNjcuemgvJCuV4A_1COF_sONftTfaLdi_vB0_ZOm0_5ZkYbNtmg5FiPY9V994yZ9ZJXgfu8_su6H2a5cihlnz7RwNbjnROpNJlb38sgePks2J2HoFKd4leg9o-9m16o1aUIE-vEZFuOsxsD57pESYQBroa-oE6jArowwztm_IHGYRg9jVJIAa_wDdIdvUHqu-YECJMiPOTTIqxkkRxD3sOqtGlgIXNqajp5zJvS8vS33SFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d3da04bc.mp4?token=B5CTTSRWa4-PLVSe-_k4TEhUWs47t3sjE-Xi0QcLIUGmcY3Ba-xSyggcSrWfhkqJEFzLeK6bdPpMbihjfqS4qk-h2geMmfvrtNiTDwMNjcuemgvJCuV4A_1COF_sONftTfaLdi_vB0_ZOm0_5ZkYbNtmg5FiPY9V994yZ9ZJXgfu8_su6H2a5cihlnz7RwNbjnROpNJlb38sgePks2J2HoFKd4leg9o-9m16o1aUIE-vEZFuOsxsD57pESYQBroa-oE6jArowwztm_IHGYRg9jVJIAa_wDdIdvUHqu-YECJMiPOTTIqxkkRxD3sOqtGlgIXNqajp5zJvS8vS33SFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهوره‌ای از اصابت‌ها در پایگاه پنجم دریایی آمریکا در بحرین
🔹
صفحه اوسینت Egypt's Intel Observer تصاویری از اصابت پهپادهای انتحاری ایران در پایگاه پنجم دریایی آمریکا منتشر کرد.
🔹
این صفحه در تحلیل این تصاویر نوشت: آثار سوختگی تازه‌ای در یک انبار واقع در داخل این پایگاه، در مختصات ۲۶ درجه و ۱۲ دقیقه و ۳۴.۳۸ ثانیه شمالی و ۵۰ درجه و ۳۷ دقیقه و ۳.۹۱ ثانیه شرقی مشاهده می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686648" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/835d4c8879.mp4?token=eH_WzgAo0JqYLeLRCbe-pba-yfYYRZIDXCXfOyjYMci6EyQmUpKs-3sQXdclf6jVvn2hkkzhA3bPD6YLMvgNfzfGh44qdzxQj045qJhiTa8GhytTCpKnzg9HXco1LWRam0ABMFWMuw7oQrp2_A8MnYO1jqHfYiTshr_2N7c77hVi4pO1qfxPrJ3Cj2wedN6r2d_jr7CfLc0lwpRiMi7b7rkLagh2a2YzI5UgdPx49E6-G_kZGlv9SlwpgAIUG8WmN0xaVF2XZXLNWxjfyq7HKFurgh29LuqvG_xcgojUyZxofEbo6SkuNYJxM7JCnAIemb41uRL0tlQ585jpwStVbBQFYHiSy0XK6qUku-319ingSDcjuQ7lTlFWM4P4busOO1O7AzR_PrZ6iDDGImDgGldy_pydTj97z4_T_vZnutFop7pZHoqnPOPrMC09So0YVVOcxJ8YC-CVJCB-Ugrt7enjxjOmMh-T3yDv_7Y1yk6qU58FSr3SHMd_byLftGWo7YwPdua6JEP_QjUTkXgvkrMbbZUbL3NsISChSBdUDJvqRM68HCoXLS1Xh-Oi7LrtnGgzX8WVbGucdHNfsa-R89OFiLQ-Zc_tDaXT5TokkLfEgnzGCB0THxbGOQ0g2QQx6CPiY9Wt4d3scxSjyN_f-Z_5vgqTgHNBFzxk5ioFhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/835d4c8879.mp4?token=eH_WzgAo0JqYLeLRCbe-pba-yfYYRZIDXCXfOyjYMci6EyQmUpKs-3sQXdclf6jVvn2hkkzhA3bPD6YLMvgNfzfGh44qdzxQj045qJhiTa8GhytTCpKnzg9HXco1LWRam0ABMFWMuw7oQrp2_A8MnYO1jqHfYiTshr_2N7c77hVi4pO1qfxPrJ3Cj2wedN6r2d_jr7CfLc0lwpRiMi7b7rkLagh2a2YzI5UgdPx49E6-G_kZGlv9SlwpgAIUG8WmN0xaVF2XZXLNWxjfyq7HKFurgh29LuqvG_xcgojUyZxofEbo6SkuNYJxM7JCnAIemb41uRL0tlQ585jpwStVbBQFYHiSy0XK6qUku-319ingSDcjuQ7lTlFWM4P4busOO1O7AzR_PrZ6iDDGImDgGldy_pydTj97z4_T_vZnutFop7pZHoqnPOPrMC09So0YVVOcxJ8YC-CVJCB-Ugrt7enjxjOmMh-T3yDv_7Y1yk6qU58FSr3SHMd_byLftGWo7YwPdua6JEP_QjUTkXgvkrMbbZUbL3NsISChSBdUDJvqRM68HCoXLS1Xh-Oi7LrtnGgzX8WVbGucdHNfsa-R89OFiLQ-Zc_tDaXT5TokkLfEgnzGCB0THxbGOQ0g2QQx6CPiY9Wt4d3scxSjyN_f-Z_5vgqTgHNBFzxk5ioFhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رییس کمیسیون اقتصادی مجلس از فعالیت پشت پرده تراستی‌ها/ رسیدگی به پرونده ۲.۵ میلیارد یورویی
🔹
سید شمس‌الدین حسینی رییس کمیسیون اقتصادی مجلس در نطقی جنجالی، پرده از فعالیت تراستی‌ها و میزان نفوذ آنها در اقتصاد کشور برداشت.
🔹
این سخنان بعد از اطلاعیه وزارت نفت که مدعی شده بود صحبت در مورد تراستی‌ها، بازی در زمین دشمن است؛ مهر تاییدی است بر فساد گسترده در فرایند فروش در وزارت نفت و فعالیت مشکوک تراستی‌ها.
🔹
به تازگی دادگستری تهران اعلام کرد ۶۶ پرونده تراستی با ارزش تقریبی ۲.۵ میلیارد یورو در دست رسیدگی قرار دارد و برای ۴۳ پرونده قرار نهایی صادر شده و ۲۳ پرونده نیز پس از صدور کیفرخواست به دادگاه ارسال شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686647" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9e676a56.mp4?token=kjoCtv5UhOz8mfo1ZpTpvUc9gykR9Z91RpkGN036S8Lvzs3QtH-To80r1xMC6DFs0N0_9vkxsbBisW2ZfsxD-ENyB0J7_Ui8WVK66idzmxvMDoCoe4fnfE7BuDURyQoxYZ7DoWnbmJNTAMJe7bqZfOrP3IDT7rO3q2SSkdTZDi3FkTCNbDxzCXa1K7RL3pVn9BcEhVqioi8eOP8LX3IEia36BR1AmLHQgHmy8a8ijkUTWMu6Z8aiMqBlnaLGg-QzmpIC4ca7zfP41NsJ1SrSSqpzECl4wx9BGarqXONH4yKdM2Kz0_O7K9HDgHTVfK_wDncwI70Li9Xa4OmzCb_2-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9e676a56.mp4?token=kjoCtv5UhOz8mfo1ZpTpvUc9gykR9Z91RpkGN036S8Lvzs3QtH-To80r1xMC6DFs0N0_9vkxsbBisW2ZfsxD-ENyB0J7_Ui8WVK66idzmxvMDoCoe4fnfE7BuDURyQoxYZ7DoWnbmJNTAMJe7bqZfOrP3IDT7rO3q2SSkdTZDi3FkTCNbDxzCXa1K7RL3pVn9BcEhVqioi8eOP8LX3IEia36BR1AmLHQgHmy8a8ijkUTWMu6Z8aiMqBlnaLGg-QzmpIC4ca7zfP41NsJ1SrSSqpzECl4wx9BGarqXONH4yKdM2Kz0_O7K9HDgHTVfK_wDncwI70Li9Xa4OmzCb_2-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان یار؛ رقابتی فراتر از یک مسابقه
❗️
اینجا قرار نیست فقط تماشاچی باشی
🔥
اگر فکر می‌کنی برای این چالش آماده‌ای،
میدان یار منتظر توست!
✌️
قراره وارد میدان بشی، رقابت کنی و توانایی‌هات رو به نمایش بذاری.
🔸
تیراندازی و مهارت
🔸
کمک‌های اولیه و امداد و نجات
🔸
تولید محتوای رسانه‌ای
🔸
پیاده سازی ایده های کسب و کار
لینک ورود به کانال پیام‌رسان تلگرام:
https://t.me/meydan_yar
لینک ورود به کانال پیام‌رسان بله:
https://ble.ir/meydan_yar
لینک ورود به کانال پیام‌رسان ایتا:
https://eitaa.com/meydaan_yar
صفحه ما در اینستاگرام :
https://www.instagram.com/meydan_yar</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/686646" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FETVkDcZZjU5PI68cd1e7albPg6tsaSI_FBQjkMeZiAW8pyGhHjAPDotFNeq3ryamIsKW7IvjmAEti7979-eXe1Ppot0H-oc7AqpPdFhiRdFN9WjiUZdL8rFd08_YylJtyjp7QlDsC2WFsc9xcEpvskoLDmB2-KqEDNDQHHXBNOksBDH5kn3Pgp8n4V2VgVtXr7LnJkpI7-45fF2U-J9iUwpg-CS0MI61to-q1xaHNv8we163YVdCEHUxnpf1PJBezTir7jsUeDhPFNt6hOpUlGdyjJp4ZV893TznR0ft8GoRbUrpygJxVD176GsMsfquwlwVr6Ce-ncOSmaGAFPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشکش شیطان
🔹
آمریکا در ادامه‌ی جنایت‌های پی در پی خود، شب گذشته، یک مراسم عروسی در کوهستکِ هرمزگان را، با دقیق‌ترین سلاح نیروی دریایی خود، مورد هدف قرار داد. دست کم در این حمله فاجعه‌بار، پنج شهید از جمله یک کودک خردسال و ۵۰ نفر مجروح شدند. این جنایت، همچون باقی جنایت‌های شیطان بزرگ، در تاریخ ننگین و خونین آمریکا، ماندگار خواهد شد.
🔹
هشتصدوپنجاهم شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686645" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686642">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5KGoOlW1ycrY0DzpGelMjTKjXMFpkmyzD5wMQlSyQ2qiPgF50A8vByuFxdQn8fZkcofnGVhpBqHR4OYJpJp_vX10XBJss2ItCoKBrZ3HH6qq9OvD3cHv-CAdEjb_aV-BybvpylcmnSBh__zjENa9ak_Xd0IgfT-R-HLsDw1PMog5kkE9HrFc04dHPWT-WvFsaAtzb6sHrpoir4skKtQasHcy79s_CfC9RjTi3y9-RByj-5_l2PfKovue9Yw4rdanxjWokCCZPcQxa0LlSyFUtRzKxgSlteRc2-a_4uif1cHPjqU33DEWyL4P-h7w8sxq9auvERWCv6B1hXeFkQrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqb-IRTsbOb8E5ZmhlsczfGBRHOAARcspFu8_QDwdl8yISyR7oKV3UwjKSjJ_AtczrC7Cj879ukYMLpGXJE8FvPui7erl8_gdwc9pYdaVJeL_XbcuzGuGHxQZe2zxhve_tFG6M4jlDDi9pueiUXy3uRGwfytv6xbX13KoYlIzBCaP8hGFWVdhzdIfC8bPw23_PuZSs0kQf-pp4wCcwiwlCg9KsjsCaKX10_kQFM_TRUM4raTE_Khr-OvsKvGe_UvaJ23p17lvK_pCPNxWeT9hbC_CMypAHFkAfWtSJj6lwlLJJKGy60osMuPuahgOgFfyGN9ZGjNJW9lJKG9hI38fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب استقلال و پرسپولیس
در دربی ۱٠۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/686642" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDpp4IiOQRmt6sas6xgy0tdUmEnzYDjZ4jQGxDVaHmJjbrhDHOuxyvLlEaMdGol4yg_ujJjjvnprbXxqFyjSg8s7s7psDKODcLNxWbxwt6-CIF-6MgcClQx_FxcnHmsfozfwXL2gsUA8eTv0KQRWh5tMt3ddyJl8rBr8TsNeoOmvIr9calaNH9fUcmFrX0wLzAOnRzm30lLdJBENGSUqDlpk8dYgUIkKyvocuwnHrnvF97kZpO5Jq1g29SNXeuaeHsbjYus8nq8el3EErtEvhmqWP7A7wV2sXydCqqt0E3jep-hsVZ5x11Omtw74f-5AiG3EmJ-iDJsyg_IkHZhKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ امتحانات نهایی شهریور اعلام شد
وزارت آموزش وپرورش:
🔹
دانش آموزانی که در آزمون‌های نهایی تیر و مرداد از یک یا چند درس نمره نگرفته اند، آماده باشند.
🔹
امتحانات نهایی شهریور از ۱۴ تا ۲۵ شهریور برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/686637" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b7363f91.mp4?token=W2t-0Qs0CunmsQJ-DkUKcVPxPoapt68N6x_-gdzMMkkDR9cjLnKqA1QG7vQj_TL-BhhC1PoaIGaHlqfFpNQ5q098eJrsx3MOD0lbC4WQyp5-_GJhlPld3gC8hslqMcwFEXTm27PfFUfUQl14VJvFnhujvFAIbNyzYt6gNs22K6vbnlnjdrffDFUUn74YD2QZljheK48DMpfv-OChXHRk9-ZiEFJYhAfLo5vbdPV3m5LAqx917alsBOlU3ZsAXCP7jIy9gMbshhuhkD_HxDrQsU4Ak4y8KOwx-Q8XrXduQ2a0dpnjq9IMnJYGPVAL_8cFvfc2eflJmI9yewtSWODswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b7363f91.mp4?token=W2t-0Qs0CunmsQJ-DkUKcVPxPoapt68N6x_-gdzMMkkDR9cjLnKqA1QG7vQj_TL-BhhC1PoaIGaHlqfFpNQ5q098eJrsx3MOD0lbC4WQyp5-_GJhlPld3gC8hslqMcwFEXTm27PfFUfUQl14VJvFnhujvFAIbNyzYt6gNs22K6vbnlnjdrffDFUUn74YD2QZljheK48DMpfv-OChXHRk9-ZiEFJYhAfLo5vbdPV3m5LAqx917alsBOlU3ZsAXCP7jIy9gMbshhuhkD_HxDrQsU4Ak4y8KOwx-Q8XrXduQ2a0dpnjq9IMnJYGPVAL_8cFvfc2eflJmI9yewtSWODswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت یاوه‌گویی‌های مضحک ترامپ را تکرار کرد: ما ساختار قدرت در ایران را تغییر دادیم!
وزیر خزانه‌داری آمریکا:
🔹
ما دقیقاً تغییر رژیم نداشتیم، اما ساختار قدرت را تغییر دادیم. نفرات رده اول را حذف کردیم و بعد سراغ رده دوم رفتیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/686636" target="_blank">📅 18:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUn1NxcBPIikEa1yn5oq9bgG_zPhz37JhQX18WVe6yh-3CmkvrlrNSzY1zbDx6inp0cP7F5xZrNiCExEs66E2oDzQGBJrRrrgxH1gY8_N-jRgjd7lOz-MdgtV6zPbNCGgkv5VYG5ZYAhwR8M4uAdyvSJkBUTtnSNFH1-6BmO4Fg0RqFlXEmNoPsdrt8sXDdeUVSfhwHxRc6jZyINv7QTvsDyuvoe2weAJ3rukOaPjuaFTe2N8SxzDOqAaGosiSU522K1gNAQCgH1aRMqlDo3UdAh0-lPL5fsLPJ7IfcjMCdgW8A12xCH5e24CALqyGLbqE5_IlUSrvaPBsI9Csokug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYJvOPihev5bhOCYN2KkyqiFUJzdMiUoaKodR9r_3J2kcQvwTKORdF4eutmRCbVtB8FP72CvuovpxOGKJx5EV-eE4Io3Cy7vIMLepHrzF6gP_c1AWzQZT7xak2LJ4k8uFCYzOi7d6BcQndg0vTo6TorrwRF6729rXmkR21Zqk0oat8tJ3ONaF8HZFH9FLeMDzE_UhkM9117zjebEXrv46iPsMZ_4Twbpl9WO5Vlmm2mGBpvnuUblT3ePCdTz8VrHTaqTa8yzRVrTgBaLEuPGaensohcmB5nE3CH8G3Nhp-qO1Ms93Jvmy8EYdJkL3-WweQVaLLV06S_4FCxfgcTmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWtiebnN1mAfu3gqXO6DFFynN0Hd5dXj17nwU7IePRIuPv4rNnJx80cRlgBaYr-XYcjCDg2CyjwTRvPXnbmoSVRxpX2mAlSSkB2hdBn9KdMvnfCpnv1Sb4KQ8S7YhWdZEhxscymeAhYLCR3L57uZYxc4w2VKjXyjFN470hQ9xLX77xCBAuyT5QbaAb8uwAtEkeMibeiNv-6_cVg2nQV8qSfB1Xf4HIzDp8zUYJBNN6paGR6FxBNAfBW5JFfr5gWKgz5WdORpZMFAB2GIp9n4HJlY-imVQPsXaFsBKjbh2ceIif69IuxFrccfnABXaVabyYd-FuA2i1DrDlOu1adEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQa1IaLycrEj7mUcMe5fgmgiVTqSt3b8t07mbvqc6-DtPuiXtJA97WFYT_X6KcCNOIrYOa43OZK3TQUdXMvLz4NwcOeStotODGsRrSKV6KLqatnZ08mF_9C4IxlAeYc8yDqRsTXK_SQ-q1TxuTt_rDg7fWNRHJ4DyfS-EE9VsoN-CmQozc3PgWNIsytnPPfC5GGKx5FyfgFzy8QudXIlnSNcjEXxDywcQf8Xze3P78AvQzkpoaLXGiGeAXe9hxQz64FbvY-v4OtqUmtdY4Pm_WDh4UWIGtpb4BtoPsxpNtBFL4A9fg987eZTGNgarFjsJKRlHisaqejXP5ENkxTkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovGx3-sdzrW1yw1K0bBkM-jCws-fuaoSNtGpgjwlibmfXQqQb_jEInAwMWSOLo9x2N265zqdtDXX7rLakXAsqTG1MLDNvphMbXHRJha7GuowiclAqI9UKmHYqg9C0-tDLyBIZXdGcndPVPDq3XJz0-BCoHoxh7k0NX7jMeq2TDb1E9UfIBPtjv57gSSzJAwo_4qc1iMV2akDWyCmQdDhym5SdOdJFl7h2GB3O_tQQEQBLDNFZGpL0pZ_ZFn_Wnnrq-O0zwSOZepkjyAuRLoyb6RgcsXE77EJtdf8LHMKkHqWv3NsWOTJqvfSXIDwPohXpdjboyVPhoaLreQo6WVykA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استفاده از این قیدها در بین جملات انگلیسی تا حد زیادی می‌تونه سطح زبان انگلیسی شما رو بالاتر ببره #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/686631" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: می‌خواهیم فشار اقتصادی کافی را برای وادار کردن تهران به بازگشت به میز مذاکرات ایجاد کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/686630" target="_blank">📅 17:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUxgW-MktLHVHqSwg7kn6w6oNIgkuyjR9Cd9DHv3jBUQaXUeOijHkk4ISMusg_bx8orORP18wlsehBkAca-COF5QdNG1BWL4SDTYh1VtFxRnKJqlYTL4PpdlmEWa-aavxlbPl08LmX9rk8kThCimEkFkbW3DT6e0vhBQmHa6S9ywR_IwkSMRDttmsSzviryYJNPvkHFdjKGblEqa35RNufdLpkqoPKQEJXliysW5mBjB73w3HlSw6xW88UW8os4Zksg-C95mbYSTOVT6Ycq3D4UyvuIkkSzsG7HNhLJrT2e5OBzjNlQiphbY3Y9IiSjU8DWzzk2ybseSo8KjDoJpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCubbQpK5F2yDXF-eS-pDw9wj_awNheF1FnTu8uK7cnNaMZ0jJR33CTROTqZhOOA0FLqpaN7a_zF-3pKxWIHzjpHReVg41MKuzKFQujWLipDeL1yAfHtW9sKLQ9WX6l_emIhXVCcuEEfK7lX_cZbc4WzzspLB3uQdCrdyNKJxEm6-r4GkEIS7iGzOLGI6sETdIbn1kI9w0eGnOKmJXhpAW4WEElsSKVdckITvufHREZM7ZLCHXrX-zkWE124c7HxgN2Fd5RgTfR5pyvOGGxDujgUxX63RE6c2l9DxsTyfNELEP5DYcZMqVjdwDXl-a8zOUucV87eAZPKmYmzR9FzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvcKZyCr9IsPNiCc6FopAEVUsgfnO1uYxHmwShMpJtpzfXkf6sKsC7nLpDIdpxewPj8m7Wf2YvXYSLwDJdGqTsqW8iq_RDBa6T_UNeuUOgmpiuJY73uE7Y3NQOIKCVljzIa1rQqJ5skG1JSG4xCXpLsdrVKO_nYP-xP6ycs2TXEsw2sPlIerAe-burQeMrllf1L_IKqRz1UtlwDhdip60QjGASS5PCLyfB6K5pzqaA8f7CBb1Z157d1vb40jTvJObvD4NYx0Y98gsedimhLnaQXuL-CemjUFTO75Oc8CfTOvTcVmDB9sMpLb6SaTx2TqRtZ6Vyhzg4unR4H7_VavKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندار مشهد: علت تصادف بلوار وکیل آباد ترافیکی بوده است  فرماندار مشهد ضمن ابراز همدردی عمیق با خانواده جان باختگان تصادف رانندگی شب گذشته در بولوار وکیل آباد این شهر:
🔹
طبق بررسی های انجام شده حادثه شب گذشته صرفا ترافیکی بوده و هیچ علت ضد امنیتی در وقوع…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/686627" target="_blank">📅 17:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39663bda8.mp4?token=htATF1BfRN2PueuNZ2ZauLEUGMWHPXsxX8E9N08__-JWvR6GFIHJMNZXU6pmzvV4J1j09ArLcO4tNQDzvAhz46Ovvw__UPa251GJ2Nd19oSomubLXvsIu9liUyw9eGCHMEzm4a6RP6_aemwyiFIKG9unua5KcFCEqBJ5DA87ZTQG-Zz8W6xFnDorYRSoHUVt0nvh-KbZvPn-GjeBgwfYyV1s7F-eUIzFeFj-oVvz4LgcHLJUUNotEKo7h_VWyRx8GSfpBUZZkwfdeks_nqJR6yFQoeoXbhveublix1gxGWCjfd7Iu56HRxW-psMwlvUZnxeoBK_O8uQVIDkdZupUj4ImunFIcyp-U_kFtrFcdIa_qtMtbLFqjLwgfYfhhQlcAtFxntTilX3u-81h-RxeG3ticvul4RHUncqmbRrSlT0Ew9EYRwsuWBR_u0ycBlumpI5GqJTICydg3ml_w357ylmeoHx6bMFa6a1AYeuJqjMLpqa1Hwace0SbEXOA0DBeYLYFK07LeCEyRxKnNb9AjnKn8bccFL4T8d5qjiPYx_A4v_PqBf_0d8JfxnvyUtSE7JW6m386V8LDkMwpvDByGkE7SByFmWcHu8SrXXRkZLLKF8bPpT6syuIlPzXyN803TxiWAKNy_KQycOm3o7z_QVCnGJJnOZW3ofdCRk_Hk-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39663bda8.mp4?token=htATF1BfRN2PueuNZ2ZauLEUGMWHPXsxX8E9N08__-JWvR6GFIHJMNZXU6pmzvV4J1j09ArLcO4tNQDzvAhz46Ovvw__UPa251GJ2Nd19oSomubLXvsIu9liUyw9eGCHMEzm4a6RP6_aemwyiFIKG9unua5KcFCEqBJ5DA87ZTQG-Zz8W6xFnDorYRSoHUVt0nvh-KbZvPn-GjeBgwfYyV1s7F-eUIzFeFj-oVvz4LgcHLJUUNotEKo7h_VWyRx8GSfpBUZZkwfdeks_nqJR6yFQoeoXbhveublix1gxGWCjfd7Iu56HRxW-psMwlvUZnxeoBK_O8uQVIDkdZupUj4ImunFIcyp-U_kFtrFcdIa_qtMtbLFqjLwgfYfhhQlcAtFxntTilX3u-81h-RxeG3ticvul4RHUncqmbRrSlT0Ew9EYRwsuWBR_u0ycBlumpI5GqJTICydg3ml_w357ylmeoHx6bMFa6a1AYeuJqjMLpqa1Hwace0SbEXOA0DBeYLYFK07LeCEyRxKnNb9AjnKn8bccFL4T8d5qjiPYx_A4v_PqBf_0d8JfxnvyUtSE7JW6m386V8LDkMwpvDByGkE7SByFmWcHu8SrXXRkZLLKF8bPpT6syuIlPzXyN803TxiWAKNy_KQycOm3o7z_QVCnGJJnOZW3ofdCRk_Hk-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لایحه نفوذ علیه کسانی است که سازوکار مملکت را علیه مردم خراب می‌کنند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
اگر دولت خودش اقدام به دادن یک لایحه نکند، مجلس خودش وارد می شود مانند امروز که طرحی دوفوریتی در خصوص عوارض گمرکی در بحث شهرداری ها و دهیاری ها مصوب شد.
🔹
دهیاری‌ها و شهرداری سهمی از بودجه دارند که در حال حاضر معطل هستند و دولت باید زودتر در این حوزه اقدام می کرد.
🔹
همچنین در خصوص سهمیه قیر، اقدامات عمرانی معطل تخصیص قیر هستند که چون دولت اقدام نکرد، مجلس وارد شد. در بحث نفوذ نیز وضعیت به همین گونه بود و ما خلا قانونی داریم.
🔹
در خصوص لایحه نفوذ این گونه نیست که آحاد جامعه درگیر شوند؛ نه هدف مجلس چنین است و نه عقلانی است.
🔹
خطابم به مردمی که نگرانی دارند این است که عزیزانی که تخلفی ندارند نباید نگران باشند. این قانون برای کسانی است که سازوکار مملکت را علیه مردم خراب می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/686626" target="_blank">📅 17:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDytO8_s-Of5UOw15sqUAMJL7OeBYiEEpz_cucbeF6-1MEAOHDgIn2hfngmoa96ymQ6cqyu-fSSTjYkl76O_kCVR69yPD02VAJLZoQVWle0Rg_WdigDYn6TVj3tl7vKlumuV2EP_G2XhP-KRJvrc8RJXEWH9dnmjsHtc9_dTMppAdXH9nvAecJd7s3EHwR6bGd_GhlTYG9e-jcfilKGj5QcLwHXm_C0nu0SQPGg6Tfm3zJ7mxgfHUEx8Lq4qwwnU9Z3sIlNbD11HXMiSTit0jINmP49j7HkTSzPMZEQatKQRZjLQxaze3yrGHaLEXah9oQtEQAd4d8kqbTliiCdFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکهٔ ترامپ وارد بازار شد
🔹
فروش سکهٔ یک‌ دلاری دونالد ترامپ امروز چهارشنبه شروع خواهد شد؛ عرضهٔ سکهٔ ترامپ در حالی انجام شده که استفاده از تصویر رئیس‌جمهوران زنده روی پول آمریکا سابقه بسیار محدودی دارد.
🔹
در سال ۱۹۲۶ نیز تصویر رئیس‌جمهور وقت آمریکا کالوین کولیج در قالب یک سکه یادبود نیم‌ دلاری استفاده شده بود. این سکه از ترکیب مس، روی، منگنز و نیکل ساخته شده و ارزش اسمی آن یک دلار است. ضرابخانه فیلادلفیا مسئول ضرب این سکه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686625" target="_blank">📅 17:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
برخی منابع خبری از وقوع یک حادثه امنیتی برای یک کشتی در نزدیکی تنگه هرمز خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/686624" target="_blank">📅 17:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b5feae79.mp4?token=BqacwVdCM0dNbIdi4pF7snLRbkseWLd4eNA5lLbxxB3dffHzsmjMSIvZttNQlTppnn8yPAHUd6gofKc2EGLIYxAgpIYkFJGqLuZqGnLzDfM_UbBhns93TUQ778b7cx-6xn2e-LCOV17pNnFkjZnZVif7kp648RY4U5HdSJpahOt89pppb8JpkO7pHCS5rwxkXCaZRpAs95VVKdDUzXLnH3pZ6llX8EZWPQaWirSyvFjgdapNkp8_hdAIyLIu-8L8N_BJz3wY1F_KPgyICRQIlsIoepNHSJdE7isiYbb3Rewa4U-9fzQ12dwoSqO5WMn86JVpvjoKGjeM6xvi3AO28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b5feae79.mp4?token=BqacwVdCM0dNbIdi4pF7snLRbkseWLd4eNA5lLbxxB3dffHzsmjMSIvZttNQlTppnn8yPAHUd6gofKc2EGLIYxAgpIYkFJGqLuZqGnLzDfM_UbBhns93TUQ778b7cx-6xn2e-LCOV17pNnFkjZnZVif7kp648RY4U5HdSJpahOt89pppb8JpkO7pHCS5rwxkXCaZRpAs95VVKdDUzXLnH3pZ6llX8EZWPQaWirSyvFjgdapNkp8_hdAIyLIu-8L8N_BJz3wY1F_KPgyICRQIlsIoepNHSJdE7isiYbb3Rewa4U-9fzQ12dwoSqO5WMn86JVpvjoKGjeM6xvi3AO28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ پیش‌بینی دربی
🔹
در آستانه دربی ، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی استقلال و پرسپولیس را با ما به اشتراک گذاشتند.
🔸
الوفوری را دنبال کنید
👇
#دربی
@Alo_fori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/686623" target="_blank">📅 17:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشی متفاوت از قلب بازار موبایل
میان رده هایی که پرچمدار شدند. تب و تاب این روزهای بازار موبایل. کدام مدل ها بیشتر می فروشند‌؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686622" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlu6mP_OSQQLYcAWcrxvhbGioq_6oVziz6rI6SgI_rex62jBMHhu-lXPlET0orxBCaqdOB5NkDThbpTx2xYH3zlwOXqgrrcxCpuCFE8sS0dOaCpMUapqYMgJ5WM1Cm0BPemkoePepuBDVewrRVmF1pJBLnQ8xIpvPeHeIq2JOtOptkClyNjfaZ_-fmlTnZ-NpnkbqsIfys9HoUxVNd4VVAEh16jyyU1aOxY0oXPzI99RihSITfGjDRtyI-dUnYN1sqo89Yy3X3lA2JTMXAz1WBiPPvohT9Ir-tPH8Ivje3Hs1gHyx-DyxR896nxcXiw_kBEqSLi-9NuUpSzm39L_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: ادعای سنتکام در حاشا کردن حمله به جشن عروسی در سیریک، دروغی وقیحانه است
سخنگوی وزارت امور خارجه:
🔹
«تیم هاوکینز» سخنگوی سنتکام، در انکار جنایت سیریک مدعی است که آمریکا غیرنظامیان را هدف قرار نمی‌دهد.
🔹
ظاهراً او سوابق رسمی ارتش آمریکا را فراموش کرده است: کاکارک در سال ۲۰۰۲، مُکرَدیب در سال ۲۰۰۴، دِه‌بالا و وِچ‌بَغتو در سال ۲۰۰۸؛ حملات مستند آمریکا در افغانستان و عراق که به کشته‌شدن تعداد زیادی از غیرنظامیان، از جمله زنان و کودکان، انجامید.
🔹
ظاهراً او چیز دیگری را هم فراموش کرده است: حتی سریال Homeland، محصول آمریکا، در فصل چهارم حمله یک پهپاد آمریکایی به یک مراسم عروسی در پاکستان را به تصویر کشید؛ حمله‌ای که حدود ۴۰ غیرنظامی را کشت.
🔹
واقعیت آن‌قدر هولناک است که حتی پروپاگاندای آمریکا هم ادعایی را که هاوکینز امروز مطرح می‌کند، مطرح نکرده است. سیریک داستان نیست. غیرنظامیان واقعی‌اند. قربانیان نیز واقعی‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/686621" target="_blank">📅 17:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bd7a197a.mp4?token=uLWoWe9mjC_II7bKvHKk2Rv3aVV1i49V3cE5cpCgvQ0S8MZ85P3WMWr4fvaf-NXsnOKpdaj4hk4LpLOeVAmX81GznKWU2ABWOOxXmdkiSRs_HapULRmTkSwXg5LCho5YyrwzZRKcrQBWwE9Cg25eIHXJbyovSzReErGeH6pmV_KQlcXrMqd7tLhcy9pQc7nzXAi7EzlnPDqFZRkjSIWgUNbktso3RmnS4akd_sulstzEkvD4AhEIH-drLPJ7ir-QrklGkQFJQH9XSms3PtsGx9IZpgD3ZGV77NHX6fb-ajvz4mz_XqMCXwRE65fnTNXOXVwAvwtQ3awVKMw-m0UmTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bd7a197a.mp4?token=uLWoWe9mjC_II7bKvHKk2Rv3aVV1i49V3cE5cpCgvQ0S8MZ85P3WMWr4fvaf-NXsnOKpdaj4hk4LpLOeVAmX81GznKWU2ABWOOxXmdkiSRs_HapULRmTkSwXg5LCho5YyrwzZRKcrQBWwE9Cg25eIHXJbyovSzReErGeH6pmV_KQlcXrMqd7tLhcy9pQc7nzXAi7EzlnPDqFZRkjSIWgUNbktso3RmnS4akd_sulstzEkvD4AhEIH-drLPJ7ir-QrklGkQFJQH9XSms3PtsGx9IZpgD3ZGV77NHX6fb-ajvz4mz_XqMCXwRE65fnTNXOXVwAvwtQ3awVKMw-m0UmTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی یک متخصص ژاپنی برای کمردرد وایرال شد؛ ادعای کاهش درد توسط کاربران!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686620" target="_blank">📅 17:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=s7m07pz9dL21cQ1VMr4yS9VCv-3oH53fqUJz0Gfpb7zmWfZcoL21Y8gQ8xoPUM3DHDEjzooXFg_86R3rXZDVA5xhU3-6oCLFqMD0rCX7aVQboWEanH97EHbFxT3jZ2ZvEzfyPN99KdBPAhSGX40a4NL1Nvr6gTzaVGDw7IwNERxtQDem7tTfKttE6jydWx5aQbPJxNTDIDE_qHGT4zkBYA9GYztbY6XpRN2tNXeYj4uHsyGUeoUVykaxpqz6vHmIhpiwtecaYgTt-l08peZwWuRqqCI4ZCfvoXM77TXEIj4hSqQDaqnnD09ot4Bvp4Hzj3mBEskLHJDrppUffBxZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=s7m07pz9dL21cQ1VMr4yS9VCv-3oH53fqUJz0Gfpb7zmWfZcoL21Y8gQ8xoPUM3DHDEjzooXFg_86R3rXZDVA5xhU3-6oCLFqMD0rCX7aVQboWEanH97EHbFxT3jZ2ZvEzfyPN99KdBPAhSGX40a4NL1Nvr6gTzaVGDw7IwNERxtQDem7tTfKttE6jydWx5aQbPJxNTDIDE_qHGT4zkBYA9GYztbY6XpRN2tNXeYj4uHsyGUeoUVykaxpqz6vHmIhpiwtecaYgTt-l08peZwWuRqqCI4ZCfvoXM77TXEIj4hSqQDaqnnD09ot4Bvp4Hzj3mBEskLHJDrppUffBxZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز همچنان بسته است و کشتی‌های مختلف هدف قرار می‌گیرند
🔹
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله نیروهای متجاوز آمریکایی قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سپاه پاسداران شهید و زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686619" target="_blank">📅 17:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686617">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI9zs-0apWDJHtjULxcxOv-rFNvqWWiRgqrrOE09opiJ6vjYn1mw5dPILAAtjb9-oFfhiaVJujWmVB2xC5-1cz1KVVBQEirdVACJe9Blt39fqxgCFgi7NP6gvOIhxr9dMYv6abZj8p1K9LKFdxh3GXfUGB-pJkZ6In3g15_aVPRuxV8AtLdV-wZQiMzSeZH0KlyGTla9CFGDwePAmDbUw5m4cCjS9ltYC_zrxUSswdI-Wf46XW-lMBFu3ufKEH_Mu51ToAgOzFIPUCuJNJ6JakjhQNWfB9h8zSbCDYxVsk_xzrkrHB0w1jSWHQHV5BdU-4jxDlXTP4sLoIv-Dlp7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ موشکی و پهپادی ایران به حمله وحشیانه آمریکا
🔹
نیروهای نظامی ایران در پاسخ به حمله شب گذشته آمریکا، مواضع و پایگاه‌های آمریکا در پنج کشور منطقه هدف قرار گرفتند.
🔹
مخازن سوخت و کنسولگری آمریکا در اربیل عراق، کمپ تیتین (ساحل عقبه) و آشیانه پهپادهای دوربرد پایگاه پرنس حسن در اردن از جمله این اهداف بودند.
🔹
سامانه‌های راداری و محل استقرار نیروها در پایگاه‌های الظفره و المنهاد در امارات، تأسیسات راداری و مراكز تجمع در پایگاه شیخ عیسی بحرین نیز بخش دیگری از پاسخ ایران بودند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/686617" target="_blank">📅 17:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686616">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جانشین فرمانده کل سپاه: تمدن برآمده از ارزش‌های انقلاب اسلامی هیمنه نظامی آمریکا را درهم شکست
🔹
مدیرعامل شرکت ملی نفت ایران: ایران صدرنشین کشف گاز جهان شد
🔹
جرج کلونی، ستاره سینمای جهان: دولت ترامپ توسط کم صلاحیت‌ترین افراد اداره می‌شود
🔹
چین و مصر: جنگ آمریکا و ایران، دیپلماتیک پایان یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/686616" target="_blank">📅 16:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای نتانیاهو: از نوار غزه عقب‌نشینی نخواهیم کرد. در حال حاضر بر ۶۰ درصد از مساحت آن کنترل داریم؛ قلمرو تحت کنترل خود را گسترش خواهیم داد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/686615" target="_blank">📅 16:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686614">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شهادت یکی از نیروهای راهسازی در جهرم بر اثر حمله پهپادی دشمن آمریکایی
🔹
بامداد امروز، یکی از کارکنان بخش راهسازی قرارگاه سازندگی خاتم‌الانبیا در شهرستان جهرم، بر اثر اصابت ترکش ناشی از حمله پهپاد شناسایی-رزمی دشمن آمریکایی ، به شهادت رسید.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/686614" target="_blank">📅 16:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686613">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/196b45b251.mp4?token=KZm4_O1S_G91yS-dX0O4kO6dfkaid2YKr2kV-ZIB9duSe4_hCsfmsyq4uarN1aTjCqNtymI4sdVcoWpWUGse95p2_fkHM8SzTqEvoDWKI2a0PSLd2XAkY0BgA166GCrxeY5O4ZwRWz4R4_ilFHQGJQ48r2UOLUDMxvdpoY6ltSQRFPi_stoM4sJ-b3IrI6rq9q7EFrxGnY03XfBo5tD8I9ll3NBubgI5F-vXlE9FV218QdlKEoBDF6FQBJItyo8GSIs64pKH8CeOx8Our0YAinHrjXMb-5Bit4obd7-cfBtygVJHJksxYjKDQxLS8EyQgYSeuTySchGf39MoZuFCp7O2FTKIvgglZuAPrYDru52Vur-spUjiclymi6EkspT1TiqClz127jl9-P8HZiCNM_qmxOC49m6vOA-jyeU4hS3vEo8wgERVmzPW6LiwiXliti2lTNEr2IKhyFiU8tDJkcwmnJ-z5MZsvBUktwFZ6CuTNBnQk8zMCHz0n2cQmJoumjAS-yZugYK7IC_R9Odr3SfN8nXbWqdg2hhEvtx3moLl4Purwhv4lZ8eP7S7Mz9AhsA0o1DdscPbptL4ulqdy912RnJxLtGT6aSMh0C6VgBSH8flNV2A7ewKWs9pxkuv_ZfUgVf7FdEMbCo81XZoNSaopEPDYWhsJIVa324g0WU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/196b45b251.mp4?token=KZm4_O1S_G91yS-dX0O4kO6dfkaid2YKr2kV-ZIB9duSe4_hCsfmsyq4uarN1aTjCqNtymI4sdVcoWpWUGse95p2_fkHM8SzTqEvoDWKI2a0PSLd2XAkY0BgA166GCrxeY5O4ZwRWz4R4_ilFHQGJQ48r2UOLUDMxvdpoY6ltSQRFPi_stoM4sJ-b3IrI6rq9q7EFrxGnY03XfBo5tD8I9ll3NBubgI5F-vXlE9FV218QdlKEoBDF6FQBJItyo8GSIs64pKH8CeOx8Our0YAinHrjXMb-5Bit4obd7-cfBtygVJHJksxYjKDQxLS8EyQgYSeuTySchGf39MoZuFCp7O2FTKIvgglZuAPrYDru52Vur-spUjiclymi6EkspT1TiqClz127jl9-P8HZiCNM_qmxOC49m6vOA-jyeU4hS3vEo8wgERVmzPW6LiwiXliti2lTNEr2IKhyFiU8tDJkcwmnJ-z5MZsvBUktwFZ6CuTNBnQk8zMCHz0n2cQmJoumjAS-yZugYK7IC_R9Odr3SfN8nXbWqdg2hhEvtx3moLl4Purwhv4lZ8eP7S7Mz9AhsA0o1DdscPbptL4ulqdy912RnJxLtGT6aSMh0C6VgBSH8flNV2A7ewKWs9pxkuv_ZfUgVf7FdEMbCo81XZoNSaopEPDYWhsJIVa324g0WU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم اخبار را از کجا دنبال می‌کنند؟
🔹
پاسخ‌های جالب بازدیدکنندگان بیست‌ونهمین نمایشگاه الکامپ به پرسش خبرنگار خبرفوری درباره شیوه دنبال‌ کردن اخبار.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/686613" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYsZsD8_Gvz9vtd4ABjLU-Y9fRgOFXWqFh3AqEEU2U3uRjj1R4CkmZF-WXhjn2EIBHPLeyCqVTSJAGJ_5S-fhG-Wh2Nm7w8uQxl8lPNoJXK8nRvi-vy3m1c2AfMZAWJ2b5I3Dsf1aVKOgY58p9XPhNDb51mCFGv8Ge-Ve0Z9t49GtwcnGr3nX9UDwbnKDIN3Wme7Z7DyAgPHDcHZo9JA2cOWSv7KXFhRBJ52hoq7iJrPUZUcMGdE80zZftgX4XorMbr8zxaddVKKPl_3q3wqNMhdHwhp-KtLyPR5IsRUg9egUiz5phumzlLZ3l-T1IjNFd4Cg91e4yzq6LMrXxQ_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر شایان: «بنگاه‌سازی» را از «بنگاه‌داری» تفکیک کنیم/ بانک تخصصی باید طراح تأمین مالی پروژه‌های بزرگ باشد
🔹
نقش بانک‌های تخصصی در ایجاد و توسعه پروژه‌های بزرگ، با ضوابط شفاف و نظارت مؤثر، می‌تواند در قالب «بنگاه‌سازی» و ایجاد ظرفیت‌های جدید تولیدی و زیرساختی تعریف شود.
🔹
بانک باید از تأمین‌کننده صرف منابع به «طراح و راهبر تأمین مالی» پروژه‌های بزرگ و پیشران تبدیل شود و در کنار منابع خود، از ظرفیت بازار سرمایه، صندوق‌ها و ابزارهای نوین مالی بهره گیرد.
🔹
اجرای پروژه‌های بزرگ تنها به تأمین منابع محدود نیست و به شناخت صنعت، طراحی ساختار مالی، ارزیابی اقتصادی، مدیریت ریسک و نظارت تخصصی نیاز دارد.
🔹
اصلاح نظام بانکی نیز باید هم‌زمان با اصلاح ترازنامه و ارتقای کفایت سرمایه، بر مدیریت ریسک، حکمرانی شرکتی و بازطراحی مدل کسب‌وکار بانک‌ها متمرکز شود.
🔹
بانک دولتی با مدل کسب‌وکار سنتی نمی‌تواند مأموریت توسعه‌ای جدید را دنبال کند؛ نقش بانک تخصصی باید از تأمین مالی صرف به ظرفیت‌سازی برای تولید و توسعه گسترش یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/686612" target="_blank">📅 16:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کاخ
کرملین: در جریان مذاکرات رئیس‌جمهور ایران با پوتین، هیچ درخواستی از سوی رئیس‌جمهور ایران برای میانجیگری با واشنگتن دریافت نکردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/686611" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHeWs2b91FI-kSYB0tOXWcx5JEQsRHzu7xIMteYvPlPOPtYw8-o3UItshYRhBOVOsdau2RLGymVa1-WlrC8Tg9IETUaPur5rSb_Md1xO8wvsrTa6aqpKnYKRSXgxG4bENrauxAfIQVwE1TYfSkw7_M7JzwkU5wx961ojX9RcH8zzx_R-4QO8XBPA_ehuUCSAWrewvMAzumIgNfyxlJFsxjWmOKVmERFsxcYCODqehRSTWz-jlfUAaIIeInuE4xopxhPemx5bRtCdd-rvQtMpGvxxQoJll4lDrAF4P9kk-tbFdH88VT-i-oSkYZn-ONukysQtgjl4IHBvt5TCODASFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری پردیس احمدیه در واکنش به جنایت آمریکا علیه سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/686610" target="_blank">📅 16:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-poll">
<h4>📊 🔸به نظر شما کدام تیم برنده دربی امروز میشه⁉️</h4>
<ul>
<li>✓ استقلال💙</li>
<li>✓ پرسپولیس❤️</li>
<li>✓ مساوی</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/686609" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سرمایه‌گذاران طلا چگونه به نرخ دلار جهت می‌دهند؟
🔹
سرمایه‌گذاران بازار طلا برای محاسبه سود و زیان، علاوه بر قیمت اونس جهانی، نرخ دلار غیررسمی را هم در نظر می‌گیرند. به همین دلیل، زمانی که انتظار رشد اونس یا دلار وجود دارد، تقاضا برای خرید افزایش پیدا می‌کند و در شرایط معکوس، معامله‌گران به دنبال کاهش زیان خود هستند.
🔹
در حالی که قیمت اونس جهانی خارج از کنترل معامله‌گران داخلی است، نرخ دلار غیررسمی می‌تواند تحت تأثیر رفتار جمعی بازار قرار بگیرد. فعالیت معامله‌گران در گروه‌ها و شبکه‌های اجتماعی و افزایش تقاضا برای ارز می‌تواند به رشد نرخ دلار دامن بزند؛ نرخی که خود به عاملی برای تصمیم‌گیری بیشتر سرمایه‌گذاران طلا تبدیل می‌شود.
🔹
از این منظر، بخشی از نوسانات بازار ارز را می‌توان در کنار عوامل اقتصادی و محدودیت‌های ارزی، ناشی از رفتارهای سفته‌بازانه و تلاش معامله‌گران طلا برای جبران زیان یا حفظ سود دانست.
🔹
این امر توضیح‌دهنده خوبی برای افزایش نرخ ارز غیررسمی در ده روز گذشته است و البته نباید این نکته را از نظر دور داریم که انتظارات ناشی از کاهش منابع ارزی به دلیل سخت شدن تحریمها نیز بر تحولات نرخ ارز اثرگذار بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/686608" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: ایران و جبهه مقاومت در یک مسیر جوهری علیه استکبار قرار دارند
🔹
روس اتم: در حال مذاکره با ایران برای ساخت نیروگاه‌های هسته‌ای کوچک هستیم
🔹
نشست فصلی شورای حکام آژانس دوشنبه هفته آینده برگزار می‌شود
🔹
فایننشال‌تایمز: ترامپ در حال کوبیدن آخرین میخ‌ها بر تابوت نظم جهانی آمریکایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686607" target="_blank">📅 16:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHdzvC_Kk3cPUxfdd7cQiPPh4Uzx-O4A4FXkibKtJ35bRJ26NfsQ9rJmoHkjooc4XU8j7oppjll3SFGPIGkYyF5Yxott7z7cU_mm8pcrwVwbvOdFh4v14dxVLoVnf468LILVSgjxznAvLpjjRiGNn6KsxAGiS0Rq7lv8mXUcdjirMFg91RoRGCzWz5yYSZSLm5n6BDoLmogC8Z9lw1e-4hPV2jDsSFQOH0wzAz_pTNVQr13TnsVHEwxMSLDK9WOwbIj8AIBYt_bIYubYA3nA6OR_xUpncPqmrGhsInoZx3Ek7OmBCz_4HVGaOLHMojd4o-yM_7C0S8BvWajkXpU9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تجاوز نظامی آمریکا به ایران و پاسخ دفاعی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/686606" target="_blank">📅 16:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16dda89c52.mp4?token=psMyyfq683NJqSnroSuzhMmcsWxFAxyig_eri92W7oVMruQEi5DPd-JHpTd5krwfkKz6vFc2QcRdKR_jAIEfmlImw0Bdf8qCqCaSmXA-fjZHfOdwRmPp3Kmpl8ZpA32P1pnwoJhZNbnpmP17oTwH75UsFQSD1xvpklY1VbJVPqgs1VHNL941oK0ro4V0k12QMYTT7SSjXBhpTfQuFWSy3gVbYaHQObDkVNlhrTW_3xCM1T0Q_wuiYSuq2cNsrmG5IZnu0wgrsc0O4QVS8RjjhETRuFGbesN4zhenQBCuT_fzhbjO0JJ1FFfp8SFS3L36WmqUhuMjpNvRYRIX0JPzXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16dda89c52.mp4?token=psMyyfq683NJqSnroSuzhMmcsWxFAxyig_eri92W7oVMruQEi5DPd-JHpTd5krwfkKz6vFc2QcRdKR_jAIEfmlImw0Bdf8qCqCaSmXA-fjZHfOdwRmPp3Kmpl8ZpA32P1pnwoJhZNbnpmP17oTwH75UsFQSD1xvpklY1VbJVPqgs1VHNL941oK0ro4V0k12QMYTT7SSjXBhpTfQuFWSy3gVbYaHQObDkVNlhrTW_3xCM1T0Q_wuiYSuq2cNsrmG5IZnu0wgrsc0O4QVS8RjjhETRuFGbesN4zhenQBCuT_fzhbjO0JJ1FFfp8SFS3L36WmqUhuMjpNvRYRIX0JPzXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت سپتامبر اندروید با قابلیت‌های کاربردی معرفی شد
🔹
در این نسخه، کاربران می‌توانند محل مدارک و وسایل مهم خود مانند کلید و گذرنامه را به دستیار هوشمند جمینای بگویند تا این اطلاعات بدون نیاز به ردیاب فیزیکی ثبت شود و در زمان نیاز یادآوری گردد.
🔹
ابزار دیگری نیز برای کاهش حالت تهوع هنگام نگاه کردن به گوشی در خودرو اضافه شده است که با ایجاد حباب‌های متحرک هماهنگ با تکان‌های اتومبیل عمل می‌کند. همچنین امکان اشتراک‌گذاری یادداشت‌های خرید در گفتگوهای متنی و ابزار راهنمای بصری با دوربین نیز در این آپدیت برای کاربران فراهم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686604" target="_blank">📅 16:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaZ5mOJYEMznlWBzcCxh6pwzn8OQemPrT2FWs60ftNIhCLpi9fLkJX-M-B04VwTzYClOQIwNDd-IbIfzIhp5ypTCjXf0PGVzbQw25vFHhme_b3rOZ40TtMhZEQTWEdWcorOZcmn5cZ-F79FWCVi3o0JkMC3ofnWy7bXXM5ER-WNcV-6xE7T7UZDe2AtIDHDPVfrJCjUfsmCUAfGlsKaTlORAaas4-FVyMqj9f8BW55F8GTwWKkBQm5lwi92y93kitYhy5qn0MkNrqGQVczspEkmCjdHabG93-Kwx1qIlGY6-Yp-N13ULupXH3_3-ilHbOYq-1UZdusKdpBHTpt8T6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت آمریکا در عربستان هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در بیانیه‌ای اعلام کرد «با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد».
🔹
این سفارتخانه همچنین از آمریکایی‌های حاضر در منطقه خواست هوشیارتر و برای احتمال لغو پروازها، بسته شدن حریم‌های هوایی و اختلال در سفرها آماده باشند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/686603" target="_blank">📅 16:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc4a509f0.mp4?token=DMcL1dOAhn-sRmXd9nBFbPm82_dmMwlMu9qxP2vSiXJwdkzu7U5C8KiFmkfZuSmVv_liM6erUo-RDC3h5cgP8QuhSuoSwm79cx8abi7KM1ApVIIza8GD7LNyukPJz-cfp9sBSh39r2Vmr7v_1JIdXVsfms3q2OTlVdpLzmjcVRzTS7qWbnxxfyTpKOB5uynWCunx7Z3N4I3bqhF-ytRZmxMkIQnxV_HsTMOslQNHH0spywTP5yuzXEXfb2YT_ginyYcDfaehL-lsrCsCMZK-HdZJQTMhDugaWjEJ6lUrkiSEw_K4JtzoOc2vLZT9LroLHpdP2_0vNgrE95jK2zGIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc4a509f0.mp4?token=DMcL1dOAhn-sRmXd9nBFbPm82_dmMwlMu9qxP2vSiXJwdkzu7U5C8KiFmkfZuSmVv_liM6erUo-RDC3h5cgP8QuhSuoSwm79cx8abi7KM1ApVIIza8GD7LNyukPJz-cfp9sBSh39r2Vmr7v_1JIdXVsfms3q2OTlVdpLzmjcVRzTS7qWbnxxfyTpKOB5uynWCunx7Z3N4I3bqhF-ytRZmxMkIQnxV_HsTMOslQNHH0spywTP5yuzXEXfb2YT_ginyYcDfaehL-lsrCsCMZK-HdZJQTMhDugaWjEJ6lUrkiSEw_K4JtzoOc2vLZT9LroLHpdP2_0vNgrE95jK2zGIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای کامل روش‌های انتقال وجه در بانک‌ها رو از اینجا ببینید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/686602" target="_blank">📅 16:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/686599" target="_blank">📅 15:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا به فاکس نیوز: ما در حال حاضر تحریم‌های بی‌سابقه‌ای را علیه ایران اعمال می‌کنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/686598" target="_blank">📅 15:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6258e5b0c4.mp4?token=eV_cdInpSVEyQoXA3nNClFDUX4U9lBvNcU-iiSYAIaXx-J5Q6aQQ6-LuppTquFF6zw5uJYim2gS10eR6ekCli3WZCB5RXus102mZM8cxzJ9qf5CBI6ujCkcxE0sMygftBff4b14NpkFMP_RFOzVzCjcPmG9CRUQIshwKuxOhHHBcty4a_6fV22yGdxvPRLkOV07loayWPGZBPeom4wxA1IDnY5poT6VILmiMAdsExhNXk5oFe1wV4GkNY5QKC9ILEl_1vl7CIyQRMQb3vSpcHi1f8ZBSF0J0SmoEUUj7wbTDXTVaXnAVDeIUTr8BACyIFVKaj1XPEy0t5zRsoRQRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6258e5b0c4.mp4?token=eV_cdInpSVEyQoXA3nNClFDUX4U9lBvNcU-iiSYAIaXx-J5Q6aQQ6-LuppTquFF6zw5uJYim2gS10eR6ekCli3WZCB5RXus102mZM8cxzJ9qf5CBI6ujCkcxE0sMygftBff4b14NpkFMP_RFOzVzCjcPmG9CRUQIshwKuxOhHHBcty4a_6fV22yGdxvPRLkOV07loayWPGZBPeom4wxA1IDnY5poT6VILmiMAdsExhNXk5oFe1wV4GkNY5QKC9ILEl_1vl7CIyQRMQb3vSpcHi1f8ZBSF0J0SmoEUUj7wbTDXTVaXnAVDeIUTr8BACyIFVKaj1XPEy0t5zRsoRQRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به اندازه‌ای ۱درصد از تولید ناخالص روسیه به دلیل حملات دریایی سیاه آسیب وارده شده است
پوتین:
🔹
باید بگویم در حملات دشمن به کشتی‌های ما در دریای سیاه و آز‌وف آسیب کلانی به ما وارد شده است که حدود ۱درصد از تولید ناخالص داخلی کشور را تشکیل می‌دهد البته این یک آسیب بحرانی نیست اما با این حال، یک آسیب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/686597" target="_blank">📅 15:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا به فاکس نیوز: ما در حال حاضر تحریم‌های بی‌سابقه‌ای را علیه ایران اعمال می‌کنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/686596" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ece111bc.mp4?token=oPilpzujjtwKN4orAnZxeGb159TvEmXaDb-VIAEdOegpQHjQPHeZ3Y9nhoV86p3J2rcyGBUBsrzu3_Q2HXQYNuMQASP0ojP1-Mye3P-Rd_a6igzwdcNR9ppCjxOHGIgnJXhrHCqcTkP2hrkmSbryZC0QFqMwFx5VNXfYFXm-DvXBWXgf20fgHMyFsJsyCm8yv5QS07T7CGcSncMA-k4jcOXHNW7Qnzw1SOXbnSI0esQJcVQRfaddc-6WUsFccFOYSHPHvXe9ThyjY1IWbaWU8AymssXZqAtguOw1r3XLWDaOHwsUTiTSODWsD7q7ZDTkk8X7oHMMGJ35mdor6Z5Ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ece111bc.mp4?token=oPilpzujjtwKN4orAnZxeGb159TvEmXaDb-VIAEdOegpQHjQPHeZ3Y9nhoV86p3J2rcyGBUBsrzu3_Q2HXQYNuMQASP0ojP1-Mye3P-Rd_a6igzwdcNR9ppCjxOHGIgnJXhrHCqcTkP2hrkmSbryZC0QFqMwFx5VNXfYFXm-DvXBWXgf20fgHMyFsJsyCm8yv5QS07T7CGcSncMA-k4jcOXHNW7Qnzw1SOXbnSI0esQJcVQRfaddc-6WUsFccFOYSHPHvXe9ThyjY1IWbaWU8AymssXZqAtguOw1r3XLWDaOHwsUTiTSODWsD7q7ZDTkk8X7oHMMGJ35mdor6Z5Ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعجاز خلقت را همین‌جا ببینید؛ جایی که مادر نهنگ، با ترکیبی شگفت‌انگیز شیر رو به دهان بچه پمپ‌ می‌کنه تا رشد روزانه ده‌ها کیلویی بچه‌نهنگ رو ممکن کنه! #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/686594" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajs8wcwVIJhlotA8irytqRqFtATDxJEdqFG7EDJv_GzeAq83q9Apn9SeEz_IpAq0Mbbj5WQJ37r6s9vFRp8ej0hFcKHooLMzosu6HO__95MH7sB8j_aH9EvfquwgJgzt_Y6mXyCZ1bvz6dojnzMnAVHW_XL32SQQyj6C-dieoHYYGOwvcA9LEUx652ImLK7lWoy2MZbILdZ4RTJOqAbUhdK0DqpDPOYS3a0818zVzj9OcNh13M9F2zbuB90jlOw46AWL9k30kxLv63FZhka3DrYhEJfVI12oM1aA4r9aodcuWDjuoiClm6xRd854-ATRPi4T0tifiqwN_-21R2XdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسری شدید مواد اولیه تولید کاندوم
🔹
با رسیدن قیمت دلار به محدوده ۲۰۰ هزار تومان، افزایش ۳۰۰ درصدی هزینه حمل‌ونقل به علت محاصره و افزایش قیمت ۲۰ درصدی لاتکس که ماده اولیه اصلی این کالا است، بازار این کالا را تحت تأثیر قرار داده است.
🔹
بر همین اساس، پیش‌بینی می‌شود قیمت کاندوم در آینده‌ی نزدیک، افزایش پیدا کند و این محصولات با قیمت‌های بالاتری در بازار عرضه شوند.
🔹
به گفته cnn، اثرات موجی جنگ آمریکا و اسرائیل با ایران، محاصره دریایی و افزایش  هزینه تأمین مواد اولیه، از مهم‌ترین عوامل احتمالی این افزایش قیمت در دنیا عنوان می‌شود و باتوجه به وارداتی بودن لاتکس‌، ایران نیز از این موضوع مستثنی نخواهد بود./ چندثانیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686593" target="_blank">📅 15:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWiIEF9mH9rCqrE27uNXS_Yu2PVCc9BopONRaCclMdPJ7J5tiB-e0uiuBd_FZ99fMclE3amqFVv4MEpFAJL5EgAeoOltwWHynGIAjy0lrV-QG2zI_GxHjYsLZBDwV5yjSib4Z-CbQ4OmHtKnN6cDsirkQVaem_Zb6BFUhrPgFkChRcg6QdllC5GVYzRCKMR6BxmHFtmsbp5WEW3UYpv9wCYsgAP-CBGVzFqMQUQS1VIiHq9l8dwxCKsX3Zur8VT3QGbK1AYYX6FDtAR_-82WWjWpDw5yzz_x2IxhLbS53zHsY4045Kr9TRfcDetsCGnJLM9dFblZ58-QdOqNq8DFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به عروسی بعد از عقد و در زمان شام رخ داد  سیدعبدالکریم هاشمی نخل‌ابراهیمی، نماینده حوزه انتخابیه سیریک در #گفتگو با خبرفوری:
🔹
این حمله بعد از مراسم عقد و در زمان شام رخ داد که عمدتا خانم‌ها در مراسم حضور داشتند.  شهدا و مجروحان این حادثه از نزدیکان…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/686592" target="_blank">📅 15:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z519sB0rBCruTBNkMtuWkUA1lJFr3ZogSscmvah3AN2p17NIuGxuLL_F37P1csjkd9xZhY-1tfAQP7akJiFs4H3Qkiz1-yAlEjVJrEHBP0yq8xJNBgUxmLRn7OLXbnDWwa6DT5AzKMOJNHbzRQ5i2murQ9d2bK5e0qney4Lr-NhjyzhNVj_N4yIg1MVBkO29ehpIeNwkIiUocAg5NLikuSoDdSZEhzQ2BDlJvSXjw2oSEtPV6ILjIqBKUwShpS1OpIbUWJEtzLZV3mMiTaYNQ99MOpJH9YIlxdEYVKMTcTJ_pELkuvZWaRbNlSb6onxIUl2eBbwYcPk7fpVYeK9hHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: اگر غنی‌سازی نکنیم نمی‌میریم!
🔹
حیات ما به غنی‌سازی وابسته نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686591" target="_blank">📅 15:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
گزارش USA TODAY: ایران نسل جدیدی از موشک‌های بالستیک را وارد میدان کرده که قادر به عبور از پدافند هوایی آمریکا هستند
🔹
تهران دسترسی به ۱۵ پایگاه آمریکا در خلیج فارس را برای همیشه قطع کرده و عبور حتی یک تا سه موشک خیبرشکن می‌تواند پیامدهایی بالقوه فاجعه‌بار داشته باشد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686590" target="_blank">📅 14:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAyMBEViCYingBpFZBWhdxGPCPNXZnX4_bzzVdgePE4wTIW-0zrEU_JSCuYVKPeYXApdvREPay3W9JmS5VkB59_CjopjvOuFqlFRDCI56_LhkJjn0-fBDbmw7rd0yBuPc9HzachHSZ5kh_ETRW5QxKb4495rJZL8at-wTfloTI822IfddWtUO0JVLeD3xnGorK1Iqyhth3khLiYalITz5ZD4WVPBMhbObf_2nWBrUIgL9mDxr-bQkCPhieTW-3FtjGlxKyNsWEANHCJJXhuAGLRob-dl7uOkwQArAeALFqryamwQDWl99__veEx8jEL-6Arc9c5KwCwA9ancUjnKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: بنیان‌‌تان درهم خواهد شکست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686589" target="_blank">📅 14:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkGNia1Z2GXZ8TwuGpC1DL54ihtuZli8Ghib4v9FyI3Y2gsQ56sHQp8Xx6Hkb3k4PLdFTKOY3KbxfRUXKfH1W1JGKyh6Tndqhmm28DhthOf2MBEMBry7UHhY7fkCYDbjUlnbttbhNPJbs9TH5yRGtx48SU14bze_CpmT3Tjpr9w9jl9XDwzr3mNqTjAXOFNkPB_PmibrrMHqEbnkdmqxKrQjLpENvYsHq8HUZEoFOIlCTVu0yGi5jydna9NNfDuKuJfUaXXrv3xa-wGesX2RzEuY1PXQsNHO6fm-oPaheSBsguC3H9kynz4CHlsqN8uPipZRq2gf7g2r_U1NqiysbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/686588" target="_blank">📅 14:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIC3rTzzvAIwT68Q-vZtT4BpmaoMS972PSaU1ThOK_bV9_vimCoHjO3wSMoDDEHw0FC88O9M7vC9bWtEdWTohzhn9dQnfLQNlPumkZzOs8ZgyAPz5kopV4tqIVUJvrDiLcMyv6xr5RtZqKFabtkuoY0xPg3myu9StoOQvrIXsggrUcOurYgwvRvgpZ7-ZGTmRE1yD2pXy6HADzuWFOx0ERvNImynnmEI5Gj_-MfIZDWJ_lfHYT3K9S-6JKUiGarbwMnyjKlI46fbRQ46Jjao3fd6MIcMP60GKCvCB_ZA_SCB2-vj33kcsEZ_9JLL_qJssyTAvlop9gyyuA4poOf2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا ایران خودرو را پشت سر گذاشت. از روز واگذاری ایران خودرو به بخش خصوصی تا‌کنون، سایپا ۳۷ درصد بیشتر بازدهی داشته
🔹
بازدهی سهام از ۱۷ بهمن ۱۴۰۳:
سایپا ۱۰۵٪
ایران‌خودرو ۶۸٪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/686587" target="_blank">📅 14:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f101f2f.mp4?token=JdricScShgblFSM0WVXsjt_0O_acZjSEMJTe9B5wpmDToovTghi10-G71h1nh2_WZywIkeQZcYlFY6pYDiY4wOWD_sOc75ZYHoV-ykKyPEuGWANrb5O0OD2OJpC2vdhewyL1NDr24nBmfU_XxCTUKiB6_exgeMesneLCuJ9fZDcz9w7bw7zaKbz1UP1cyqDRhZq_pVnCFcMU_MIGhcgLRUgRnqIf4ef4Gfge5FVdipCzPqedELxxAj5rEFqVKTozPkEBrhGkikrAkPiZRd2Rtps9UsgQioA6z8WInbVDDzWwTG2t78aXq1XOFdfTZTubxJUxeN5avs8OxLo3NJxBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f101f2f.mp4?token=JdricScShgblFSM0WVXsjt_0O_acZjSEMJTe9B5wpmDToovTghi10-G71h1nh2_WZywIkeQZcYlFY6pYDiY4wOWD_sOc75ZYHoV-ykKyPEuGWANrb5O0OD2OJpC2vdhewyL1NDr24nBmfU_XxCTUKiB6_exgeMesneLCuJ9fZDcz9w7bw7zaKbz1UP1cyqDRhZq_pVnCFcMU_MIGhcgLRUgRnqIf4ef4Gfge5FVdipCzPqedELxxAj5rEFqVKTozPkEBrhGkikrAkPiZRd2Rtps9UsgQioA6z8WInbVDDzWwTG2t78aXq1XOFdfTZTubxJUxeN5avs8OxLo3NJxBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در نیروگاه برق اربیل
🔹
برخی منابع عربی از وقوع آتش‌سوزی در نیروگاه برق خبات در استان اربیل واقع شمال عراق، خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686585" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شهید ۶ ساله عروسی سیریک
🔹
امیرمحمد کریمی، کودک ۶ ساله که توسط ارتش تروریستی آمریکا به شهادت رسید.
🔹
خواهر او نیز در این حمله تروریستی به شدت مجروح شده‌است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686582" target="_blank">📅 14:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773878b9cf.mp4?token=USTT97Cf2cbDdhz6MYuB3FycWX9cXCSfpH1v83a7FCuC9N_nk3vapKWOufKgcrvrCf45xNtGVQKf0BuPQkEwq1Iy4GaAXjQUSGVReiv0GE55bmE9BWfB-JHXfZdtHYx6qiCZYeh1syo70TZCiWZhdi1SBwVvplEmgf7lU-jwIrT88gCuWxq5mFoSg_n3LEN9HcIzkqKpCsI1gbcTGC8y28m_sCVq3jH9moKj7EmoL1hg54yKx_TmwScb7JlVMngpEFxhopRCrzvNrRfdui0pv0N7z_sRkOqfei7fwslJlZ6vSVd2sCKCx8juE7Bs7xjiXRAZ8_uAbddjsdvaYz-A8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773878b9cf.mp4?token=USTT97Cf2cbDdhz6MYuB3FycWX9cXCSfpH1v83a7FCuC9N_nk3vapKWOufKgcrvrCf45xNtGVQKf0BuPQkEwq1Iy4GaAXjQUSGVReiv0GE55bmE9BWfB-JHXfZdtHYx6qiCZYeh1syo70TZCiWZhdi1SBwVvplEmgf7lU-jwIrT88gCuWxq5mFoSg_n3LEN9HcIzkqKpCsI1gbcTGC8y28m_sCVq3jH9moKj7EmoL1hg54yKx_TmwScb7JlVMngpEFxhopRCrzvNrRfdui0pv0N7z_sRkOqfei7fwslJlZ6vSVd2sCKCx8juE7Bs7xjiXRAZ8_uAbddjsdvaYz-A8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در الکامپ ۲۹ همراه شما هستیم؛ نمایشگاه بین المللی تهران؛ سالن ۶ غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/686581" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رویترز: نفت با تشدید دوباره درگیری آمریکا و ایران، به بالاترین سطح چند هفته اخیر رسید
🔹
نفت برنت در معاملات امروز تا ۹۷.۰۴ دلار و نفت آمریکا تا ۹۲.۲۹ دلار در هر بشکه صعود کرد.
🔹
تیم واترر، تحلیلگر ارشد بازار، به رویترز: اگر مرحله کنونی تشدید درگیری ادامه پیدا کند، بازگشت نفت به محدوده ۱۰۰ دلار را نمی‌توان منتفی دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/686580" target="_blank">📅 14:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698db1137a.mp4?token=dTx8serwNCAW3iLvZ9hYJ-soEU6n56MSOmBban4Ee9XL10Hvj9ZgIrjFdSV5zbs37ZDuZfrpWZjPytrvQ692mEUZZhBuxjj0IkJ1W-OwLhqJpiF1i8Snb9R3FQF3BleRJ5uPJgjvK0u9sd6ry7TFpYthubcOB76mCoLNHj4agmMW6BOLb6kh2iGsZEpv62-0eS_iDQCjCBHQNxX820WZRbetPLhj1osewAEGqIMNo2fQrSr2H4UuOEIU2Q-mhUswJL-yt_C5wPwyjudcNoEQLmFKm93Q7MUZCaNHnt__L4As3T4CdGGqlvK-bwvqJdVatU1iC0IzkDawi_R3L31hLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698db1137a.mp4?token=dTx8serwNCAW3iLvZ9hYJ-soEU6n56MSOmBban4Ee9XL10Hvj9ZgIrjFdSV5zbs37ZDuZfrpWZjPytrvQ692mEUZZhBuxjj0IkJ1W-OwLhqJpiF1i8Snb9R3FQF3BleRJ5uPJgjvK0u9sd6ry7TFpYthubcOB76mCoLNHj4agmMW6BOLb6kh2iGsZEpv62-0eS_iDQCjCBHQNxX820WZRbetPLhj1osewAEGqIMNo2fQrSr2H4UuOEIU2Q-mhUswJL-yt_C5wPwyjudcNoEQLmFKm93Q7MUZCaNHnt__L4As3T4CdGGqlvK-bwvqJdVatU1iC0IzkDawi_R3L31hLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیاتی از هدف قرار گرفتن پایگاه مهم تفنگداران امریکا در اردن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/686579" target="_blank">📅 14:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9UmcnL0UClXaNGtIfGbMnalmclucFkIdmlq1T6NQ2C3ZmwWMM4bwOom2lPCgWd3uBRnvHwlr6LVyhFfQEkEZq1uozGU5UMtQPPHSQMZo91aArHRPHEEgCw-B1sfOl14YUV5sx7Egh7jbk6moLCmZGvnicqfeiCoix8cKeaaq_yDDMioFkvDcRq3eC0QT8j0_2PZVrE5GlPRWCPaczCCl4j9lBQPBKEpUcwR8FGit0FP6u34hhz4b0SoPqzSuD5IKoghCSfcUtDm0q4sDZd4M-dRauFIFcJNWfCi0VpRILuRuYu6e5XAaHvFAm3crHfpjTGCHJeKmnUXFZNUS0NRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هر رنگ کت‌وشلوار باید چه کفشی پوشید؟ #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686578" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhomgIaDmrPZKjGd-DcqETPa1aNp95v3XPC0y9t8sTwYwQupYINHOoose-divwiT8MS7fzwmJZz6Ie4us7A8w_49-78WXwAHGP9RpODfNM9yiK6zxzQneA7uqONvcgfSBH4gtgHP0fZp6St5SGHg6fxYxM4Bg2n30Ge7JrMA2JELVsaFuYw6y3xWwIiyQasGqjUNS-N-_dtaBJuJPeCaHEq089l382rfO-jL12U6JRJq1ISXfjPDXU-V07GenXwKGA0sZr_JlOEZQ8iqNiKoToQlAgm78v6-LYb-2mnhxptc1TZkIy9OGl4DgDp_lc0aP_RodoB1Pir0MzBFxnfUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO6jtfpQPYfKB_yYV-YO1X2ASvUyFAM8cLjw0sOg0ZkU5WV1nyfPSWmeqFRXammSmIihMbMkLLwqagUlSfkxs4X8IrGNR3DyvGRe7CvVOJVa1SFNJ9I46PYmUt-gVTBc0V0m0hfm1Q6U0XZrQSUqVIneS_yKhX_-lqwJlYAfIKX2RPq98JMYE9whiKnagm22azg-DwN_A16PRY8A-9sPCeNkuezBtNZ6vcz8LAkbAs-f5so-vToHiC-ZoWXEc2PJ5ygcUzc4eBzQJ4PxeymRIaqZA9GT_02ay1WUMQdjqWIvJRo60GteUO5HEDbIRD_iTrnNMqEbs9V5rNLUPA_Qww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شکارچیان خاموش زیر آب
شناخت مین‌های دریایی و روش‌های مقابله با آن‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686576" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0718e5256a.mp4?token=s3sMU7MwK28U9FCf14C9zQD9mReMa2IjLnHfKk8MFlMuHJNF_b0NWS9m-lYXmfA8KdPLf6ZCa15FXtoxEJrRtegf5AQNE1wrN2-OyL4KprWIp3rBEqQQ_H5Yt-O2Dd0OyumAK6794zzs-709tYiO1o4wYuF6M62H4B6fLuK2TUh_fopgMqLjqiQy2de96RX0_KWRTwc_5HWnOW__jo9FOToEQx-5y-kVq2cBYVeRayPh3DpSDWnD8tG0nS8T-9Fy8Zov7zb9gRkt2fk7JkguHq3Oc9M0QGI3829tzP5NUmgFerVkzCV-lRaPSWl81uV-TuAFWWeStldY7XjQ1ac67Kcht8lRyjsLTQD8N3qXevsXbg9z-wG3QuZm2M4dAGy0NCmaOhVnfnI9vNcxvb4RIYskQlmmmv9KxOLqw-uEuvaDMV661yxdk6FHaoqDOsYtUkWwEgXCsPxjFbv379jBpgXSuVhQ6VYV3YebdChNP3_vT60eXA7SmCZ-niQpyzC2RNZVYQ6MsG6HpzCcE27-Ooaq7AShMee9n8FqY5rIXAshH64kONcoHkVMnCw9qa_Y1kRp2wXsErCZvQn1WkfC_-0xQ8JkYJR46ysHLp8JX5t2ncPmQAXjamYn-dZSccoWB489bd1MED2IcIDFQ2wRLp-fB-to82IGQtaovJNpEBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0718e5256a.mp4?token=s3sMU7MwK28U9FCf14C9zQD9mReMa2IjLnHfKk8MFlMuHJNF_b0NWS9m-lYXmfA8KdPLf6ZCa15FXtoxEJrRtegf5AQNE1wrN2-OyL4KprWIp3rBEqQQ_H5Yt-O2Dd0OyumAK6794zzs-709tYiO1o4wYuF6M62H4B6fLuK2TUh_fopgMqLjqiQy2de96RX0_KWRTwc_5HWnOW__jo9FOToEQx-5y-kVq2cBYVeRayPh3DpSDWnD8tG0nS8T-9Fy8Zov7zb9gRkt2fk7JkguHq3Oc9M0QGI3829tzP5NUmgFerVkzCV-lRaPSWl81uV-TuAFWWeStldY7XjQ1ac67Kcht8lRyjsLTQD8N3qXevsXbg9z-wG3QuZm2M4dAGy0NCmaOhVnfnI9vNcxvb4RIYskQlmmmv9KxOLqw-uEuvaDMV661yxdk6FHaoqDOsYtUkWwEgXCsPxjFbv379jBpgXSuVhQ6VYV3YebdChNP3_vT60eXA7SmCZ-niQpyzC2RNZVYQ6MsG6HpzCcE27-Ooaq7AShMee9n8FqY5rIXAshH64kONcoHkVMnCw9qa_Y1kRp2wXsErCZvQn1WkfC_-0xQ8JkYJR46ysHLp8JX5t2ncPmQAXjamYn-dZSccoWB489bd1MED2IcIDFQ2wRLp-fB-to82IGQtaovJNpEBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زود هنگام‌ترین گل‌های تاریخ شهرآورد تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686575" target="_blank">📅 13:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزیر کار: ۸۷.۵ میلیون نفر ماهانه کالابرگ دریافت می‌کنند.
🔹
وزیر علوم احتمال غیرحضوری شدن دانشگاه‌های جنوب کشور را رد کرد.
🔹
پرو در اقدامی ضد ایرانی روابط دیپلماتیک خود را با تهران قطع کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686574" target="_blank">📅 13:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
برخورد با خودروهای دودزا و فاقد معاینه فنی در تهران از ۱۴ شهریور
⁣
رئیس مرکز اطلاع‌رسانی پلیس راهور تهران بزرگ:
🔹
از روز شنبه ۱۴ شهریور، به مدت سه روز،  برخورد با خودروهای دودزا و فاقد معاینه فنی اجرا می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/686573" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038eafceec.mp4?token=EmYfPQFe_fV4rG2G4L1HOJuoGrOIYp-ba5ouJMOXXVAiSGll9mTye3OH2RcPILxZKxwaPJwWd8s2C9LGbdkpYXipCMWJ7o2QgfE5WKBXrEHJbLvdc68Vpdjy3pWa2JY7De3o0w8ViWGRlDH-RcUwbYJFh672hxoe1JFEFWuOeBdNPl89k4ieN8KT_WuC5HUnlHK5HnlnCz-6lNeFwZ1fBURpC_JyfRWlI_CfmoYzqZEQcAYXdW0aJCIzDLfdjgpPQBfVrJzAt5ZiOGnhnYpVk8f2mPHctNb1cMMOUw4JdbIGHg3CvAxjBbraaLVEt4wxvIegsIJazOkLxWHbvxWglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038eafceec.mp4?token=EmYfPQFe_fV4rG2G4L1HOJuoGrOIYp-ba5ouJMOXXVAiSGll9mTye3OH2RcPILxZKxwaPJwWd8s2C9LGbdkpYXipCMWJ7o2QgfE5WKBXrEHJbLvdc68Vpdjy3pWa2JY7De3o0w8ViWGRlDH-RcUwbYJFh672hxoe1JFEFWuOeBdNPl89k4ieN8KT_WuC5HUnlHK5HnlnCz-6lNeFwZ1fBURpC_JyfRWlI_CfmoYzqZEQcAYXdW0aJCIzDLfdjgpPQBfVrJzAt5ZiOGnhnYpVk8f2mPHctNb1cMMOUw4JdbIGHg3CvAxjBbraaLVEt4wxvIegsIJazOkLxWHbvxWglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پایگاه‌های آمریکا در اربیل عراق
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: مرکز تعمیراتی، انبار تجهیزات فنی، سامانه هدایت بالن جاسوسی و مخازن سوخت
🔹
نتیجه: انهدام مرکز تعمیراتی، انبارها و سامانه بالن؛ آتش‌گرفتن مخازن سوخت؛ کشته‌شدن تعدادی از نیروها</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/686572" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حمله به عروسی بعد از عقد و در زمان شام رخ داد
سیدعبدالکریم هاشمی نخل‌ابراهیمی، نماینده حوزه انتخابیه سیریک در
#گفتگو
با خبرفوری:
🔹
این حمله بعد از مراسم عقد و در زمان شام رخ داد که عمدتا خانم‌ها در مراسم حضور داشتند.  شهدا و مجروحان این حادثه از نزدیکان عروس و داماد بودند.
🔹
در این حمله بیش از ۶۰ نفر زخمی شدند و تعداد شهدا تا الان به ۵ نفر رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/686571" target="_blank">📅 13:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242958f52.mp4?token=pcjVCbV1aqPt2fNHHr32-30svR9M3o3wnJNBheSCF1weM9_r-0k4j4tC4p9QoIKKtX4na_FG-_AXEbu98lP2fN9fHgrLA60EqL_9rGcPHWGdAjtlHFPO63TqKN9RnBuadx3ea7fVrb9GBVYWIE5AFSuHEcsOCDmyClZ511dpMGrzR1RGfCa8J1z45_rX06ftdffOzDB9ZCoroqr7I_SgJpft_GPcXU3bf0kF8SXXcEtCvgouiw0aM0VkjKOq98GQxgVWFGU0K5htNU3Y3xC1G1HZUpXzDtUn8zpKPh-MFI8tLp979ruHOyqIZglib54J074SRPsYGef6V3CvMeBFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242958f52.mp4?token=pcjVCbV1aqPt2fNHHr32-30svR9M3o3wnJNBheSCF1weM9_r-0k4j4tC4p9QoIKKtX4na_FG-_AXEbu98lP2fN9fHgrLA60EqL_9rGcPHWGdAjtlHFPO63TqKN9RnBuadx3ea7fVrb9GBVYWIE5AFSuHEcsOCDmyClZ511dpMGrzR1RGfCa8J1z45_rX06ftdffOzDB9ZCoroqr7I_SgJpft_GPcXU3bf0kF8SXXcEtCvgouiw0aM0VkjKOq98GQxgVWFGU0K5htNU3Y3xC1G1HZUpXzDtUn8zpKPh-MFI8tLp979ruHOyqIZglib54J074SRPsYGef6V3CvMeBFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس جبهۀ مقاومت: مبارزۀ جوانان حزب‌الله در نبرد «علی‌الطاهر» گلچینی از مقاومت مهدی باکری در بدر، حسن باقری در خرمشهر، همت در خیبر و حاج قاسم سلیمانی در حلب است
🔹
حسین پاک: چند جوان عاشورایی شهادت طلب بیش از ۵ ماه است که در محاصره رژیم صهیونسیتی هستند و دشمن را متوقف کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686570" target="_blank">📅 13:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B78gaAQWVdfFo1oAXNPM3lUthtU5YDfH56mryxY-fSA5VopxC3zfi-UzmZIaWKStep6YUoL1YfiF6i2heLi7pMgF34YqVRQZE9itM22u0fQemOfky2TF2e_VoGDIHF1maLYDhWF2fZUUBcwOuOGzWQS8RT4lvrhftdC0-pjbyKTH-AQjR93nKg5I304blCOO8YGYcUY0AJ-kmJMooW5KdveS5e_j00YMg7xYLvEy2YgRT8miwmsZ66dbkM60-YRyGMWQpowU96pWP42lDOLuBi3SaSAKgx2lc2ANoC1vb9arLN5v8Kvwx7Nh6wS5xlN29dnwvjQetUr5wHKGDVeWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کمپ تیتین چه می‌دانیم؟/ شاهکار سپاه در عمق مواضع آمریکا
🔹
آمریکا پس از افزایش آسیب‌پذیری پایگاه‌هایش در خلیج فارس، بخشی از آرایش نظامی خود را به سمت مناطق دورتر از تنگه هرمز سوق داد؛ اما حمله موشکی سپاه به کمپ تیتین در ساحل خلیج عقبه نشان داد که فاصله…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/686568" target="_blank">📅 13:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPn2G2JjtZMi6S7L2yf6Uru8ut3XCtObt0RxfIozzbo-lkvL819PMF1jzs7opOi0VwCBUit-gnVFPudcQOR_amcSer6YYMpanttPee7hGoY7RfvwIsLMDruHOpxim9o-ZhsWvwpTl1KmRAd8_6q1YvbEsx_W7NrjSG8YZlh_RzeEF3nlYwrQALpiXirULptTtdWmyq_x98_YzAA1-HTN4K5hYXhK2GWEkyFSB4BT86abu2XYhjUwzlVgGVStu2z6zOU05mJhU1eImswZgRifNU18_o0JpuwgSJSRk0KW0nxfKEgixOr2C5cgXswlMqTL_3_9rDDy6qr9QyBCViIqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای حمله دشمن آمریکایی به مراسم عروسی در بندر کوهستک شهرستان سیریک
🔹
محمد ملاحی ۱۶ساله
🔹
زرخاتون طاهری ۵۰ ساله
🔹
کلثوم ملاحی نژند ۴۳ساله
🔹
امیر محمد کریمی ۶ساله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/686567" target="_blank">📅 13:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=puagFR-uRcwmb1KjawJ7-rp9mMbX4H8--eIBqB6tZz4a36M4iirR6abMHR9o23iFN_FNJDjvQT7QXFMkOjAddCwClAtV_iQpYI2QIAQ7JOTgCRO73TyIwU0sFCN8haABUA6HR5ATluqHscz76SBp9QbYzDnC_dBm6oYYClJeJOzz6_4wDJAQGhx34bv0MCIz5ToTLEPVmC_POsyuonFM9qzXQC-wm9GJeVmtDVr9AExdP0inO-qJYfskaA3E_jNQI5uqrp__93kQvbIj9weuIPrkO1lK-IA6YMxB1Nqp1p3UrGXUVAZpgvVHeAfW4WWMrkSyMYNtaeOMkY3Gj4VGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=puagFR-uRcwmb1KjawJ7-rp9mMbX4H8--eIBqB6tZz4a36M4iirR6abMHR9o23iFN_FNJDjvQT7QXFMkOjAddCwClAtV_iQpYI2QIAQ7JOTgCRO73TyIwU0sFCN8haABUA6HR5ATluqHscz76SBp9QbYzDnC_dBm6oYYClJeJOzz6_4wDJAQGhx34bv0MCIz5ToTLEPVmC_POsyuonFM9qzXQC-wm9GJeVmtDVr9AExdP0inO-qJYfskaA3E_jNQI5uqrp__93kQvbIj9weuIPrkO1lK-IA6YMxB1Nqp1p3UrGXUVAZpgvVHeAfW4WWMrkSyMYNtaeOMkY3Gj4VGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس جبهۀ مقاومت: خبر قطعی به دستم رسیده که در حملۀ دلاورانۀ سپاه به پایگاه آمریکایی در اردن، تعداد بالایی از سربازان دشمن مجروح و کشته شده‌اند
🔹
حسین پاک: بالگردهای آمریکایی مدام در حال انتقال مجروحین به بیمارستان‌های اسرائیل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/686566" target="_blank">📅 13:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
‏خبرنگار صداوسیما: محل عروسی دیشب با سه موشک هدف قرار گرفت؛ در کف یکی از اتاق‌ها گودالی ۱.۵ متری ایجاد شده است، ۶۸ تن از مجروحین بستری و حال ۶ تن وخیم است و چهار نفر هم به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/686565" target="_blank">📅 13:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0eO7pwCgJX3tCaWiE5xaijhK9j497CM0G1Z6ctE_jU_VLnN8uRG3CuNgXljnvcq_8ZDQtAeRkzCx4eNuZxWBLSWRVMB91qizWWegjjUY5_S8XcAX49NNwb_fS9AkXNBKHvd9tVHhuLvJDtTXsCE-rEh7I_KBBaCUEptkDSlTBuzF9-V00vs443IunVHycp_pBVwAzSKOOfDdSmCTZK3LQickFwhQwSGgsE19B1uKJHvEJHTVApNEF9c8-jpw4LrYEyFZqvFPY_S12Zs5zYtX3DiIVxaMC6jEpFI6RbCIgGlP6vK2L_yQ-FnDaXoVyf-Bg85d5Bp1d43ODtHMIrxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imK1otUHTKijOxxGtXJNL4T0GrBxC9oIE25WiXsVYl_5uRPEWqokbkCq2E6nVyRgde2RQR5UDWZzPAVqhRLp8q-uZDzdKRE-Ktp4KBVjtKSfsBjITw-vt-Dsg5mTJH_ry5P2eTQ2p4VlezTMRkz3OlCbMeERD5sk9NUdA-L-Y05qZGDqTlJ0O8txVQ52fnSCBQ6fDe7TDmHHyiOOe1UR2ahDUvsPeugCyWuL13OXNhYrO6bKCWSMP6kpey67SyIA14SAdfV5O8lIJDpA_9lK6ECf770fyWie6BkfgdhoSee4NuUMHLg2Jmq6_07ceBEkPyHgoEH9p9uzkKPNs9cH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ube7ClP4jo8Esj0yOwscR8ZT8iub_0_GwscmB-tPaLLaM_nUs6x836aUx9W_STAdY7peQxMSEBU9gEr4EHJhM8GyUFnmvzr59W6fSt3uMqR7OCnlw-GSrNnsh-xc1qyiyuaz2qfyWE3OHgpHwQhb2OyZCX9zQfCTnB16Q63SHKueowirXY8l-y1vlk55HwZcFliWWTw3zQOsriMoyf4KNJg5Q0QD3x6BvNB6vn8SnPAFmUf2C48mf6GpRDDO-uU1H83Ims24YdftD1TpSrLCWPknzfawiqCnWayUQAtFjwnWSt_OavzfjU9XZKqVoIL986JzICFxP0Z9QtwlpfBHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnCJleXeRWPnSnXSw1mZIZjUxL0eLcqnHRKN7jWYR6mOUrTjevFmN8zH7UMhUj0ykWCVt0UWZm2qb-uX1r8xgP8vJloHz2x_5W6n9IhPi1q4NkpLi3x16JbZHf7sBK_AdBcC0nNZlFjl6fEaOXaODi5yP4i_hkNHWkvBwFY8JrxbLpL5xy7cgLnhyBA8sXwceE915Ci9nkRgilo9mWK6aCRqj1WUlPjCzTiLVm9z-3MFy7SC3FLLCTLBxW9IBE0nIEjnHFLSeylvLbCu5xz4NB66fPrZnF1aAtrJWBGvLYZhpCEUBQrsaajVFikr6ZOOWaWBBVAhdgvw_lYizfknTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tcy_G82oH0gRMAarDkxMh3Tvql3CMrkIqvzk-6cTaFNWkk8YHLCvs2sGw6iTpED36rVGmEDoCFEIvpAroWNhtdF-FYiLGbgfP_f6MHs25B07nJZHt3uEVmF4-OLISWAlBLut1RLM5vuL1W6eAMMdpWhooReTLnkYS_PESokBRSJ2zmwi-3_-FM90punhhrmXgoIew3_KZhL_FhFEU7fYjPcnOd7TLcqzAMT9GoYwQaOrIxIsZI_NK838SMQs_6PBFywnZLUjtioUUIMRma6-WImAiZUa77yRLaOPTKz5hJdAQ5NlqNMrkuDT9zMLga7yyrSYWGXSVxFSGsk_2xAg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcyDLpj21E7xS98hFDbW2rYYBrPxmUwe27hLWpDsvlh5PkMVIv--0PRd1VV8dX5I6V36Zeh2rw5uNaS9lKp7iKdHPYY6rfBEWDtOIUZtL8bBSlhD6_jwVI6mvRweuTOTbID62Qxsbp4Sb3YhkMaQ99t6Qb74EqZWfMxEfIdDCrGoSTg5W_uXwgnSj2Mf7XPFWtk4f6ZiSuVoZ5yZvlTRnzZRbM7pEvDVuixtgZmfRtMNkmilGCbIuAejzSahwUUn81k-X_vnZVLQoVor59ZFw3CeoZQfGIXWDHPFRQ24655dU6R0i6SzMwH4XeqvlxHYfTdlfF7Oi-SEwXcncM-3oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
واکنش هنرمندان به تجاوز دشمن به مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/686559" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lliva41VQO0M2rtN8fproAIu4ZkrI-qqm7IJZ_EViJ6_ySwhc7PA16ZSQaMdmg7rXDjm7nqx-OcFhz-jYt-3n5N9CyD7RR5O-20ldtqAl7p9jExTEelK61TjdKrS2eXpW5YtONXZd11FS5JDGBUxxj3-T1TFZYLGOIO0vuBdAeUQVBFW-6Av1RkFruDMOJp8-XZA29ehUNpJMFVgqiyVvOV2rlXd7sTkF5JlxWV7VbhzUtmMOXJcroREmwU7VbVAGQjAkz3bh8yWo477bV0lKqpbRrGShHwuXnVoUz_r8GsmOQd75B7ws5CdE-D_Xew5kbnDJnxa6nYQsut41VGq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام ۲۰۰ میلیونی تارا؛ بدون نیاز به ضامن
🔹
تارا امکان دریافت وام فوری تا سقف ۲۰۰ میلیون تومان را بدون نیاز به معرفی ضامن فراهم کرده است.
🔹
متقاضیان برای دریافت این وام به یک برگ چک صیادی نیاز دارند و امکان بازپرداخت آن نیز تا ۲۴ ماه در نظر گرفته شده است.
🔹
کاربران از این وام می‌توانند برای خرید از ۲۳ هزار فروشگاه فعال در اپلیکیشن تارا استفاده کنند. از خرید طلا و وسایل خانه گرفته تا کالای دیجیتال.
▫️
دریافت وام
👇
https://tara360.org/tbl
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/686558" target="_blank">📅 12:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
۷ شهید و ۸ مجروح در پی حملات آمریکا به خوزستان  استانداری خوزستان:
🔹
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/686557" target="_blank">📅 12:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytpKt9rTK4IQARZAgb5xrsOzkkCElqKKSy8ofA2xWKHWVTmaUHZM5fSMo1K8fW_3A4EWTwBruyT6i5E9OPahlp-imw1fvKUsd41ax7CcGEh-ZW03KL2nL2ge1T2Q05D6i5AVuUp2LxhTAUJDsaQfgCmdymtsLdBomG6pNjmADu1gaKwNULzCkFJu5WhNkOYSomhegvk7CAhkXXXOrYbAV87aPAOlok0yyAYNcchc3hTJwZycwA3LfbwniIc_o_qY4T_uOERMixwF1sCRx1OWWM3yAy9uzDSdxDeatHSDt7rVZ5kfaJlCIqOXMFThp01H-VdfuHWVBR9V_M_LU59Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بورس
| کاهش ۷۹ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با کاهش ۷۹ هزار واحدی در پایان معاملات امروز به ۶ میلیون و ۵۰۳ هزار واحد رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686556" target="_blank">📅 12:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd62eb16b.mp4?token=L7OyWQx1fQmHirfrDB-w-0e6v-EB2GzzKxiSvWNOVjZ-3nhQ5kkePKD_5pb22oAUOaOGj_VA-UTvUUaEYIMa1BrGKxWALXxKp9cZ7RCkGLMk9TPi9KXlHQxYaS0sCtNbk1vGvfUkuBH5QP5kfmilAQ480c_49MPNAOR8XkHIPhqhnqmaZuxH60SW2wQIvf49KzdAzauZsGLc8ppHBBYASH8dFSe0mUTe8EnOidXDF1SuoBa6bYf_gljiTGR94MXRWIaZsRY_GzyC7Ltt3LVIQPvemOt4ixT1ZK0dj7ffYj9WgF25wIIbqcEsa7dXWTa48jsKwg8Ld6bC_aKcuVKo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd62eb16b.mp4?token=L7OyWQx1fQmHirfrDB-w-0e6v-EB2GzzKxiSvWNOVjZ-3nhQ5kkePKD_5pb22oAUOaOGj_VA-UTvUUaEYIMa1BrGKxWALXxKp9cZ7RCkGLMk9TPi9KXlHQxYaS0sCtNbk1vGvfUkuBH5QP5kfmilAQ480c_49MPNAOR8XkHIPhqhnqmaZuxH60SW2wQIvf49KzdAzauZsGLc8ppHBBYASH8dFSe0mUTe8EnOidXDF1SuoBa6bYf_gljiTGR94MXRWIaZsRY_GzyC7Ltt3LVIQPvemOt4ixT1ZK0dj7ffYj9WgF25wIIbqcEsa7dXWTa48jsKwg8Ld6bC_aKcuVKo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از جنایت آمریکا در مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/686555" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جلسه هیئت دولت امروز به ریاست پزشکیان برگزار شد
.
🔹
شمار جان‌باختگان سیل در نزدیکی مرز نپال با چین به ۱۱۱۴ نفر افزایش یافت.
🔹
قیمت گاز اروپا به نزدیکی ۷۴ یورو به ازای هر مگاوات‌ساعت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686554" target="_blank">📅 12:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6S6sBOaZMAziFj7eifcRPg9lQg3pXoc8LmbvKKNwq36eYVdm3AI_PcfOMdycQyeB8NfFpYPKyrxMmYR-DKI9nCgYG5lmq253MpSeV7mC7dCjEc0s5FFLnuNGcaRFdq5boTUmUBspvxCwwN8ZmR5Kwb6-GaRi1QF11C6dX-TBQGj7SO1Kmd2oOwTIXQoIJEeAxqq4fkyFhsSwotHoTU2eCnVcz1dd72cTcoMdEvvc6773ghHhSrWSDTh2dxt9KrgOywm2bq6SYaNGr6RZdui0wrZ7uCLVBy_VvEiyZOMzqPqMEI3yJ_6SNpt_NtnbD2yb3keH8rJuv944zpjkzPr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4wQSSJ7nE6MNizzAa8w16F0k9bZ4gyxvS6waeeq2HpCuMw6bYMJaKnL_DfMhZ-1NAN3rcI7j5m4Pii_CTITDg0j1KWsGF0mdC6CVhSVMVHUzx27Hc-sRQpnFmtg-rw3BF_uEHpRO9bjou1MX-2yQuKXpN9S-lJBjertfx2m7ZKC4scdLj9vUj7nw4kbtqnWX-xuEztBLKO6B400NVMGtIUA6tY4S4DE32tm45ZKSBr8JJm3orq_ezEGNo6pe3DqDsn_KbRxyXcIqYCg1xZRsNq6DSjsoh2hZ2SS9w455oyNCsHtFaY-rO2sutyyyzfhD_O6La91ImON9E4vPbggZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Heo8dgRwgtHD-2Vzcg6LUBqbkMNg20JJ39LAfR3SrPvu0CwKEZ7Luuxx_pGkB2ss_qf-A9toAMmWRgLnV7m7TvE_uIJ_CRgZTcdLel-LK5IHYgWABfeXvV3ot8fs71kmlKck61eWcomr-mU-c2zdefabsR6qYV-2UdFg-afhGR4sF1aRGIQ2ytVwScPufT02PZ1efLKLHhOn7SKK5qjTWJA7_Q9Dkk-M-9ot1LtPe1AHhZJXIs1z4L3bpp9kSlX0cb2G0XQST4D9ZPQziTVGAaa2xySff9fVMmUXaVIOxPpSb6Uc777CkqLSl1ePX7vZEe0bUp8naqskYHBzoRR6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7PROz6n7XuSqrBtrlx2T95AXtk2kBt6hbqNv0Kizzq3hGizQ60uycpji4c07tge3OfIO0bg6V26nqnl-wQD-ryt_cMoxSzRhfsi7tg0igYFQVX0gqrtDt1FEkXaPCoMWHiIHtVvN-St0RlcllGTR3UKY6Gn9PExMLAdh_n2p9cf25DfixuSRZjVH9-pN1yd1n6r9KQ_v-Ln4OGczhpVLDO_PW-eVguAZ4Cuvc1Wl60kk1arifM2pm9zFeB4EnJWI7cyt-5qykJ_lEI6ImqESgjklrenPPXcydixzzQJEkqDLaCtqcf0qXfQ02Bfvs8tqowewA-d9MBzc76URrL9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrtHv9VuXLyDWOSH2H6n7kqieEMpw7mCm7gnHKSxIZBFGnhMLdMfAkd0RQAj0akBoXNhhUrKiqbzLMSdLBSf7bWgVz-suLU3JZCPQRdIo2miS5eF2ONYSR8Fn1Ou2HGSqghjJJcE-v2qBe9QCYhF9g6rDHcuArs8aVBnu4jlb-xGNFuySOjYcRw6cVwH-GtHAklvO9jEuRuEDjqRv4vUkQbPMTNJd8Xaa30LvYp_AIf73IXt0RLii3uBQ94zvFp1QEcNI5NHPfGhBsThI8o4RcyQEjUJbuAECBgOYodZUPqgHU-hEM5YoPiXeDTLmfv39N5V7Mimp6akRcjjv96ETA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوشه‌ای از حال‌وهوای غرفه خبرفوری در سومین روز الکامپ۲۹
🔹
روز سوم الکامپ هم با حضور پررنگ بازدیدکنندگان و مهمانان در غرفه خبرفوری همراه شد؛ روزی پر از دیدار، گفت‌وگو و لحظه‌های تازه در قلب بزرگ‌ترین رویداد فناوری کشور.
📍
نمایشگاه بین‌المللی تهران | سالن ۶ | غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/686549" target="_blank">📅 12:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAoTSMcd8pJP5GyM6wB7VRS5Yl7BahFN1egc7n-4ctFBEz1hUM-Stwo3eZs9AXHWu5fX8Z6Atd0qUjmPljt7M5BoA4cT16RKzSslcemssVUxCOEhlwMAAYjyIH7PgLL-Z6vgGxZDOzIbsmMwO1UqWCHo6aXDs4pyCeDgSmZSrqvs-dHyHibv1DiAdLvvWLrBhb073g99epOk56AsN8247dtvzc-wilKG-ncnrYFiKHtPokdKMxNqmm-O_Il4bUZBrySvbC_DGsRZXKt7NOBk2alKgsW16nzgc2ZceW3frB46qjaemj3-GnUTCGoSl31Z7HRlQ4V0HbhPKgbRoY6oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYAn5b01cySDolwDkd1jcGSSQ5s_sfY3vZ8JGmwc6yPDmrIdbd8haB2PLt-JfHVQc86lHP6raJ4B1uerAtTHStZLApAGhCJfgg_XIZocn0Mnz7H_pR1YDzCaderF-5C6NwJNxGF24uffEg9VVUChIpFgXQUm98H-CTCYbLmVtBP4xwPYrrMEQ_7SYATrqnVbi1ieabDoY6qFx1U1NMHAjwkmlJQ2IbvXjMiYyEjM-uBBF1n8H-uxfOlRVQDY5Y2YC59f1bwE68G7VcsElMERJMM5sPU54WOHPIhWTNeEXs3xtfoLCSXl1UQ6rc5sQGujo7fLGLbmAcD0GisiFaAryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvXtdUaJ54TMB-mlyvHEXdD-cql0DE75FtD2skq40-45R2ZMY8Vu7SV47tIM_kwFEZg04ace83J_upT2HqThzA-cN5sQVOprxK8qkFTixLqHkQYYWFKEvrCKoohwYlKdk_ia8yWNVyT9JOrH3AHloykhJE175hhonmgc3mTUyvgvvsoutfWThfa3HL_0mGCHwJ5ZUoarTjoj0CpZAfuAgheDb1RaKKbssKD18Lmrqmgj7UQOiQXAoKoc8IydQztxCT4_BqP4G_cwD1wHkZS4Y7fWXzuLeoq9zaTMYnHiG6KxDkr3qR0iOk_5VF3jl1HRAbAbqtNBh0QoTZrRI2n5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkndsozVsdipDIOigBqGbZhWwRElT2RVQUhiyhPDAOwiLuj20T8obvAryPUzsxDVBOSz0xVQdGbxoXEndwD7sM3lINhIXaQ9i-CsRj_UUQBoPNk74UfQQl3Dsg_kCVHFZgV0cudOLfyDZMNPDnHBInoHQvewaz446baGIuklaH7Y_kDpfasQnWNHumPY040neT-3mEE1OjQ-UiURubkQqRFmOVBL33IIB3dFnhKEfTcuXgnusMhdWFal6FV1iO5st6UxKoi8u7Qp1rOiotlkXT_hmRRT943r5042KWjfJopTrTX1lbKoW5ZIrc74i6Kk1MG6pHcVswqMiV0fni9YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2ctA8oY3QlFfJBaPjttWBF427Jtb_j2yWvcUz7VlpGXYNf1ImH-IE0ITvHC9YhArPuSvcYmLKjEXdu-Zl_ivmjM6uSJr-zZOYju44GuSdtwxLf84Nc0pqd30ifdtDdfiI5YW8mD1HEc4VI4_mVxYAxNt9GPlGbUc1eA-G7YOE-9kNFKeldqagm2mPLN5pfBUjllmFeYoGuT4UJzKX8E_ISi3x9mXRGjd7vki91QB7l2UxOCLFISPBwRZ-LEx9ezuPnlZ3vdyGbj465DjHTvymx74FSKjy1_KuvWQvgGHL_7MpPvvm7xvegOKMeqGHYF2kW3DClPe_2ftDUjweqtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnrIfKAadjZVUTh-43qVYbnNT2nNBUnqCIeVQxlGu6QCOCJeL3EV-PwpqRtwmM7WnehW-okp7g5dPV0VZCKNK7cItsvXZ0bO9fFH1ETkPnT-DsbTjG3Ui-D8FaD-_Zz8s5oWGXUIWzoNR6DP8TovVtTrW0Z7HHFowf1k1Dbcf6zXiPPyyHFpkjd1FlwV2R0tWLpRbhmoVFpcWnp8xtyU1KtpvepMe8-C0oQl-rOm2uFWVgXxk1X9oYIsEHl96TKpkFdxAlZj6Yx9XjVoiAeq6WACp0MSodUBMhGgVU2XFuTlj2zLelR9bmuTOS-8SpB-glnzE7Dbqh7YuCZQbOUyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNltlLH-qoj3bal5HJMNDoZrR9EJUyPqCpz2_DQ44MuoFCS5zQ3pnqlLzVCAVo-PdCABUR90iOYB87VDegvr4oStw5oNwpF4WthVoVrBia1giSFPvBCFpOhzUn7vxgtEWbT6YX_GIFKmtUmQMxt2vUFKVSQ0hxnTmEVQ6aVw-IguYILD9ETu9QHd8FXBrH34L_ClJpGQhIcTNqaimv1jP4_XmnVUGn6SSe3HB5344gvltCrOdKbPy8xKNXcI55LOyuUSun12d7ae3OvfQYyJnmO89td_uPAwgDtYgsJL6PNsYweu-LrEJ6FwfmJb1K6Qe9MMI_3TW41CqaytOSu5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6ppJQYIjirVoSsFjHf2JAKSZdeEDJwva8uv7babNYZAbr1s7OA8JY91me8aCU9bBhp48M_hekhw_iZ7kUGReO0Otgz4Dc4aNa98kngilsNcjBW8vYZF9vKpNTPYt7EfzDyyMyz_Yvv6nQWgVyCTndir4QSkskGEJ3EQWxkq9wxuLx9HpSB_ohBcXeCVartRqQjcvGpFZW4Q0t4JFPO4f-lKRA_Y_JB0z65S2rq5fHBGXVKCXNpOuYG1qClnw9y25z06bfkIvn7BRhCmrqNIIz1RMevV4FBoeQyqL5up5vDUwcyc-WkIuo70VNG_c-qrNRjnrvC0IwwCtymiSdDUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbOoIC5z3cFVOrkIOX8rHRgQs1qalETcolzw8iS-_pQ2Kk4vYPqg0Mw1e36h20PyIreYVM5Qw0nPuuRNaY9tDzhMZu0x_rjBRYk6ckbGL8zDH8PlWwnjFSSfWsxJ7GYkkiB3VuBTgyYXd_RZ-nCua46PWmuqrq32iFbsVkktQGOmq2Rkt4hD7jHphagIqODEkp4NtgqE27-3pCk4_1D6lUHUPIsKqeE0SbdthbTwVtzmrDFq-lqH2JT8JN8Of08wdtFwco18xxrA4cyUZBla0mL87bJQmBEyayQIPwgyEbAuT9wKQ7HR6QK1Y3HUwUtNUbRpcHv_CZ-JAkrx2M9xAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noFreoBi3MLhtGVn6DUNhghKkimp197acsFb3aC0Ns0WP9SSbtD4Q9JkvWJwmEpf17_tE4akKloCykvOZOjLr12n9VVMofi5yR3RdeAR4rAlzpICrWu853TpWJ-dbu4bfL-ogf9wDRTHRqbNCt-PsqyIbNXLm0SyLtJAXo41cklBoME4HeVD3poBqNnlFJoODmZUy6yUZr0iiW-T7dE-NmE_DzJhKAr3BmiOW9CcOZcmA1LCRkx9TIqQWiS3yxNY4u9wabXyP09LuXc_0bdugvtg-X8ZBAGagCBtYYb_XpjNV9VCRHOlgEh5BgAmGUv-UmvqieMTCsnXCNljiIN88A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
انعکاس مشکلات تهیه دارو از زبان شما؛ روایتی از مسیر سخت برای رسیدن به داروی بیمار.
🔸
روایت های خود را به آیدی زیر ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686539" target="_blank">📅 12:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c58e3b120.mp4?token=kvTwmeRD9uaWxCp159a2rOsF3HHQDsf5iOeWG6FveVRkHbQfb4GdIURbcGAsSUUHWYFB3eLTjkoqt1kj3XiYWMC2sN1q_NrfsjV1A0Ep4L1gQRt2A8EuhotY5Z7vDm3lbduoZLKG-r9sZfsNZ2iOivBJ80SE2PfV4aYIFgOemqwogZmFYN6VsKdIQp3Rbsf_JPIBsQr6LJa3sLCSdeb8Apr7kiIPd4DgeV5Sbi2Nd6r6_mG40rOz9m2jvuHKiXY_s9F8Bm8fA8BYXLn2euzm4nnlk8q1A0EEYFJ0YH2q6f2xXpRrCTUY78Y7ZVVIc2sW0AeW7H7EtK9sm4uL_RwDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c58e3b120.mp4?token=kvTwmeRD9uaWxCp159a2rOsF3HHQDsf5iOeWG6FveVRkHbQfb4GdIURbcGAsSUUHWYFB3eLTjkoqt1kj3XiYWMC2sN1q_NrfsjV1A0Ep4L1gQRt2A8EuhotY5Z7vDm3lbduoZLKG-r9sZfsNZ2iOivBJ80SE2PfV4aYIFgOemqwogZmFYN6VsKdIQp3Rbsf_JPIBsQr6LJa3sLCSdeb8Apr7kiIPd4DgeV5Sbi2Nd6r6_mG40rOz9m2jvuHKiXY_s9F8Bm8fA8BYXLn2euzm4nnlk8q1A0EEYFJ0YH2q6f2xXpRrCTUY78Y7ZVVIc2sW0AeW7H7EtK9sm4uL_RwDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از جنایت آمریکا در مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/686538" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پلیس: تصادف خودرو با شهروندان مشهدی عمدی و امنیتی نبود  رئیس پلیس ترافیک شهری راهور:
🔹
حادثۀ بزرگراه وکیل‌آباد مشهد، براثر از دست رفتن توانایی کنترل خودرو ناشی از تشنج راننده رخ داده و منجر به فوت ۴ نفر و مجروح شدن ۱۱ نفر شده.
🔹
رانندۀ خودرو مردی حدود ۳۵ ساله…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/686537" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_fuQsVLAtBz4xWijbx4wPeVy-ZxZTZ1-EjqFjLDhJVUbZa1Uhn3iSJPxFbF724k8NIbvGptZ16W304mNZEKfB8e_z1iHl-7xVRjI8cAxad718g-l2cuq7lZQqm3C3xdfF-Wol4Pj17k-gt61yLkOUze2mb8EDSR9ApMHzmIciYCQoj8O-X5ZGU3jjPRZawxmWSZfrx9qSWUpE2CvbQRMRndRwDOVr2pMl2Dm5awAW1VrLX3h7rnRg4paEFW2NKvqLJEID2bXbdqSyhbzbrJJfXO7f2MdEsTewxSaLBYjwUU8NVucTtoXGC7Cm1YfewjpSlhEss957ILCWFRPJHgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قصور واسطه‌ها رافع تکلیف وزارت نفت نبود/ توجیه تراستی‌ها پذیرفته نیست
دیوان محاسبات کشور:
🔹
واگذاری فروش نفت و نقل‌وانتقال وجوه به تراستی‌ها، تریدرها، شرکت‌های پوششی و کارگزاران، نافی مسئولیت قانونی مقامات مکلف در صیانت و وصول درآمدهای دولت نیست.
🔹
طبق «قانون وظایف و اختیارات وزارت نفت»، مسئولیت فروش نفت بر عهده وزیر نفت بوده و قصور یا عدم ایفای تعهدات واسطه‌ها، ضمن آنکه مستقلاً لازم به رسیدگی است، رافع تکلیف قانونی وزارت نفت در وصول و واریز کامل و به‌موقع درآمدهای نفتی نخواهد بود. بانک مرکزی نیز در حدود وظایف خود مکلف به اتخاذ تدابیر لازم برای کنترل جریان وجوه، صیانت از منابع ارزی و وصول مطالبات بوده و مشکلات تراستی‌ها نمی‌تواند مبنای توجیه تأخیر یا عدم وصول مطالبات دولت قرار گیرد.
🔹
بر اساس ماده (3) قانون دیوان محاسبات کشور و ماده (37) قانون محاسبات عمومی، موارد عدم وصول صحیح و به‌موقع درآمدهای نفتی به تفکیک سال، مستندسازی شده و در دستور کار دادسرای دیوان محاسبات قرار دارد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/686536" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab8fd704c.mp4?token=BikdpvS4m6uPYSjWumcFbXd5kfv2KDgAu8GadNzkVlw6yWITjzd03JKyGFT6GbmXH7ovtIqniev8KjPhD8Kc0SxZltKMsbmtPuSVUqXGjbQYiptEzLGVaaUtx1HtI0CNvPYOOCCZhb1nymyl90FvqcALuvAOBgTpqW-3vAv--hT3H9xBEagWSbbv8XfErK3KLSCyp3focKTkNRIWP4L9dwu0A8T6R5tSdjCAm4b7NYVvI0MJub09cqwbuMwZtPZJKoR7HCard3BdHJaemHZ9PUni4ZgjFRsTR6AbRnu_6jD0BdF35-P582oxUQnxXHuOOd02gyvCoH1wL6qtJMR3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab8fd704c.mp4?token=BikdpvS4m6uPYSjWumcFbXd5kfv2KDgAu8GadNzkVlw6yWITjzd03JKyGFT6GbmXH7ovtIqniev8KjPhD8Kc0SxZltKMsbmtPuSVUqXGjbQYiptEzLGVaaUtx1HtI0CNvPYOOCCZhb1nymyl90FvqcALuvAOBgTpqW-3vAv--hT3H9xBEagWSbbv8XfErK3KLSCyp3focKTkNRIWP4L9dwu0A8T6R5tSdjCAm4b7NYVvI0MJub09cqwbuMwZtPZJKoR7HCard3BdHJaemHZ9PUni4ZgjFRsTR6AbRnu_6jD0BdF35-P582oxUQnxXHuOOd02gyvCoH1wL6qtJMR3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا دیدی یه مادر برای کمک به جنوب کشور اینطوری از بچه هاش بگذره؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686535" target="_blank">📅 12:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ3BS4J3qtROTb3Tt_LROsQbBnq-eq6I5cn4JOw0NXEjYz1qml3uYo0bTblTBmqMDyMdfPa2zZqTTprI9MrkszCgNDiAffJcJWC8PwpTiykGqPB4Fsoai7D8ALsU65tyK0sbbIaCCrwyCcdN2-2KwunBeG-keWI88TJEp9tc_5ZS4sVUX7g0ywvhWNQd7hi2DBc6eH9fEtmrfaxQX5l97IGGe1AN2_NrQ_FFDPJUN4Q5CE6VGcU4XOvkdIJUqNd8Yk3lQS4FNCjV_HEPp0TlWqqWpVuHKTGVHIy-RDfz2160klirEQK1o2KMWxXnHiew7MZuJUTzFVTo_HpCJ23kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه خبرنگار WSJ به ترامپ: از «کمک در راه است» تا «چه زمانی مردم ایران قیام و مبارزه خواهند کرد؟»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686534" target="_blank">📅 12:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2746fbcd68.mp4?token=FqGYHuvtKmqbKQLQJHkbPIicjsB-uHcGqhRSAy-zmMEio6NI31VwViCJPEIQZFpLda2gURcJBkUsPqmWmli8ofiOjkfy38FuhoEGq7ZMSoQ3Db9mq4MkPoejb2hurVCyxPSdjxHNFzJbVNa5is_z0xTD05J1eL_H9lKloSp_azTUg8ciqeijzbP7CiYeSVLiI7UUP9cZ9BgZUeSGfrvjdwI3x4QDV9fXL29yWJLOf_gJPP2XSK4uDOGzEpghSW4hoi5tEP6rIHVrVzwtl-JAGMoUMoQl1VLK6VyieRbr2Rqtpq6Bev8cq6i1H3GxgfV5-f5eEHnZnYAydiVcu1orAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2746fbcd68.mp4?token=FqGYHuvtKmqbKQLQJHkbPIicjsB-uHcGqhRSAy-zmMEio6NI31VwViCJPEIQZFpLda2gURcJBkUsPqmWmli8ofiOjkfy38FuhoEGq7ZMSoQ3Db9mq4MkPoejb2hurVCyxPSdjxHNFzJbVNa5is_z0xTD05J1eL_H9lKloSp_azTUg8ciqeijzbP7CiYeSVLiI7UUP9cZ9BgZUeSGfrvjdwI3x4QDV9fXL29yWJLOf_gJPP2XSK4uDOGzEpghSW4hoi5tEP6rIHVrVzwtl-JAGMoUMoQl1VLK6VyieRbr2Rqtpq6Bev8cq6i1H3GxgfV5-f5eEHnZnYAydiVcu1orAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند یک‌ثانیه‌ای آتش‌نشان‌ها برای باز کردن درهای قفل‌ شده
👨‍🚒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/686533" target="_blank">📅 12:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBCq_Vh8ifCWD6wlrlGZu5S3FkfLeDJCwBzvnUB-n4L_r5W9DQ4Sli8PcuaJXo3PID-8_RMVf8F9PTjkEDErQxGqz6BZEf73td10alWAHtjJVHX0rCnnRJb5p4Lw9SHi1v0RWfsRYtriabDIrLIH5OLIYl2maVWEPlwULUD_mhoLfHD9_PC-fFTJn7iHguP1QJXSDCmgiC019SQrHS2CUNpPqbEvxvcorI05p8Do-mVC2hsNRF7giujAq7D21yaxBQAEPNIZ_4-dTm9fcJ1wXpbmVBD1poIcGqqVNOLOEPwSkmvoZnRD2AXrbxcwmMpVFwCy4NYYpC3k20U8NJyMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید طلا در روزهای پرنوسان از پلتفرم‌های آنلاین ؛ وقتی قیمت و هزینه‌ها شفاف است
🔹
در روزهایی که قیمت طلا مدام در حال تغییر است، یکی از مهم‌ترین مزیت‌های خرید آنلاین این است که کاربر قبل از معامله می‌داند با چه قیمتی طلا می‌خرد و در زمان فروش، قیمت معامله را هم به‌صورت شفاف مشاهده می‌کند. این موضوع کمک می‌کند تصمیم‌گیری برای خرید و فروش، به‌خصوص در روزهای پرنوسان، ساده‌تر باشد.
🔹
از طرف دیگر، وقتی هدف از خرید طلا پس‌انداز و حفظ ارزش پول است و قرار نیست طلا به شکل زیورآلات استفاده شود، خرید طلای سرمایه‌ای می‌تواند هزینه‌های مربوط به اجرت ساخت مصنوعات را نداشته باشد.
🔹
یکی دیگر از مزیت‌های خرید آنلاین، امکان مشاهده جزئیات معامله قبل از تأیید است. کاربر می‌تواند میزان طلای موردنظر، قیمت و هزینه‌های مرتبط با خرید را ببیند و بعد تصمیم بگیرد؛ یعنی به‌جای اینکه صرفاً در پایان فرآیند با یک عدد نهایی مواجه شود، از ابتدا تصویر روشن‌تری از معامله دارد.
🔹
به همین دلیل، پلتفرم‌های آنلاین طلا در سال‌های اخیر به یکی از روش‌های جدید دسترسی به بازار طلا تبدیل شده‌اند؛ روشی که برای افرادی که با هدف پس‌انداز طلا می‌خرند، شفافیت قیمت، مشخص بودن هزینه‌ها و دسترسی سریع به بازار را در کنار هم قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686532" target="_blank">📅 12:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
خبرها از هدف قرار گرفتن یک کشتی دیگر در تنگه هرمز حکایت می‌کند
🔹
گزارشها نشان می دهد که یک نفتکش در نزدیکی سواحل عمان با شلیک سه موشک هدف قرار گرفته است.
🔹
منابع عربی مدعی شدند نفتکش مورد حمله، متعلق به عربستان سعودی است.
🌍
تازه‌ترین خبرهای ایران و جهان…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686531" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9e369c4.mp4?token=u40Np99bDRo0EJaW-R_2Voaixu3bK0PahtsAGg015LEtLmEmWruVPVCXhTAYCm9_xpONlpixBnWu7b2KBaKh3bE2t54vcVyCGofxWIuU6ppDzw5AG4gAxaI1FiejHzQjco9bbjF4eKgVrN0nHPBv80jrtvN-DqoaYa1wOr_yWYaWyqoEY6Eja9xyOrjEfPpQsIJeBj6gkzfr9GvMS4REmMaQ59PevpoK91bc4PvGR7Yq3hHrTU8P0orWcBFA0EpuTdN5ipgolL0NCGjSHt3AXxmAXt0UAZz-rW4rwOAZWAL8ipC1r8_3yxFOkVrshth9gGvoGPwQjMyigSln-f-NLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9e369c4.mp4?token=u40Np99bDRo0EJaW-R_2Voaixu3bK0PahtsAGg015LEtLmEmWruVPVCXhTAYCm9_xpONlpixBnWu7b2KBaKh3bE2t54vcVyCGofxWIuU6ppDzw5AG4gAxaI1FiejHzQjco9bbjF4eKgVrN0nHPBv80jrtvN-DqoaYa1wOr_yWYaWyqoEY6Eja9xyOrjEfPpQsIJeBj6gkzfr9GvMS4REmMaQ59PevpoK91bc4PvGR7Yq3hHrTU8P0orWcBFA0EpuTdN5ipgolL0NCGjSHt3AXxmAXt0UAZz-rW4rwOAZWAL8ipC1r8_3yxFOkVrshth9gGvoGPwQjMyigSln-f-NLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۵۰ میلیارد مترمکعب بدهی به منابع زیر زمینی داریم
دکتر تابع جماعت معاون وزارت نیرو در
#گفتگوی
اختصاصی با خبرفوری:
🔹
ما در سال گذشته ۲۰ هزار مگاوات ناترازی برق داشتیم که امسال به کمتر از ۱۰ هزار مگاوات رسیده است.
🔹
شرایط آبی ما امسال نسبت به سال قبل کمی بهتر است، اما نسبت به درازمدت چنین نیست و همان کمبودها وجود دارد.
🔹
ما ۱۵۰ میلیارد مترمکعب بدهی به منابع آب زیرزمینی داریم که پرداخت آن سالیان زیادی طول می‌‌کشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/686530" target="_blank">📅 12:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
چین اجماع گروه ۲۰ بر سر بند تنگه هرمز را ناکام گذاشت
🔹
چین در نشست گروه ۲۰ در برابر فشارهای آمریکا ایستاد و با بند پیشنهادی واشنگتن درباره تنگه هرمز مخالفت کرد؛ مخالفتی که مانع دستیابی اعضای این گروه به اجماع بر سر بیانیه مشترک شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/686529" target="_blank">📅 12:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJspHxSu3b9xSIeOy-yd0ibQhzRlF52lN98pRuXbNfyTvdV3PaRSjk6r7KUuqyjODBkxdsw9blJXxWntkff-zUOU9rpVGpEA6JWmyUViV51P9nJv97EsVBbub_OLtmHkmn_s_H1_Vm3uggT_iyLesxAceiaa01IBiIkh7wwrYjd628-yf8w7ZxfkTnAFwMkxRCjmV7x74EaqDOXjnKdRt8CLjEa6ppohBl-D_11p8p8rh7RQ6_Aqs6E09-_wTRu0ik0jdhDzwR00iSq0z_bh0B7eEFsAJs8C0sl_O1Vyuif61thi72YJQ3aK4bK5sjuKDpNxOcOvCE_KYS7bVf18Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت دلار، طلا و سکه امروز چهارشنبه ۱۱ شهریور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/686528" target="_blank">📅 12:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfO3b3OxtkFRi3_CVRoAqcKcU7QqzCbyRR4Ntg94zMWnA4PwtFmqTj9PhyKK2KLYldNqApulJQwpo51BK3bwqMrQDOsZOKdOX689yFWYYUjlB1SqFuuWkFBiDaQ0Z7bwUmXfoTaTmXDfFWquYnDR98dZiTRQyeNaQyOaAceHrEM50dPV8QvABGo_g4fIK2A540leH-K0dhrNmK8b_-WNIH6Jw7vPhoop5C4YSVYN-2erK95XZ0NiORTq7Iseh9Vkc_Xe2SxatCRBkrg-osXUXohrJ_eo1_0ca1hIwPLkGUTroomupBiWCb92P_6GPskgfacR-2qXZz6tAivaOU7vHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/686527" target="_blank">📅 12:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8SYTUGEgSMnakD3_9Ueg-0q4nSdkxWmtxqfAOyuiIFv8s0bqQBONQdQRFrxuFfjh4cyIpd2RXdYO1L4E4qI-6IYLcVAqClUAQc-uf5dHMoqZyM1dyNIEtL_6XDe-NI8a7ldsFM4yrCMpe_MEfvmQjLdPEjibmHu-O7ZiowagxSd7lGRkKF-A3VkCs1pRSH0IJy5ALVXb-K8ygFGdxFZtW91Iq-JFWFfZO_fd35Fwtf2yo_fOcB7cCOGlKpt9MHEqKNNcoPP2ef-JHoh4zwdJsqrzp4ek_MZXI3xF1tuTOByEwxyuQDubV922bxVZykjZ-e6TpTa6SwJb39GfIM2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بهنوش بختیاری به حمله ارتش تروریستی آمریکا به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686525" target="_blank">📅 12:04 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
