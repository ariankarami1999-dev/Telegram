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
<img src="https://cdn4.telesco.pe/file/k1Ysu6uzzdxB7ceUNoYWSFRoy-4nQhNg0kuMT4bYML-AIFchJUsO68ub7WaOEiUO2Nyf0OIzjgDJisezcvvPVY0cdf_zUH6nJ2BYCu8KsY7_Ay4fjPY2NlUgeZmDXN52mk3V5TYBr8Q9Vt8tp3dVK8mDFOSODR3A_H2Jqo6o6UGdFIR3CeGGnzVKLL6UyFR-xIII1coKtie7I66cjPT7EAvIfDj7E1giZtyE0fkm7oYzPfQYs7lsQNh9fCr_81J5TaaMZ26PkEOQ4pipV19Usro1w7btI5x96CL0N3ysJrb4Ys768g5USbBaeB_70I1rE0zRFv7USR4RYlN158P_iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 13:07:41</div>
<hr>

<div class="tg-post" id="msg-680808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99c18cdd66.mp4?token=ZDDHdmnUlEnFrbMyaMlB_bpuC4Fe9GWkCZxzC4Hj90JbwK4yXyi505qQH-R4txtE8FuPo7dCa6D7yW9q_T_5NjhcGSmwoIpV-aKd2jF17JzoLmV61uLgXZ8hJEa60YinkvixGrPv5LoZg926gLgcNYkxw2VPTl-vrLBjcUhKCpGn-1uhdzhPhNHnV2kRPkhNxNp088QN1xn-Caaga9HQpVM7ENiqC57PvRrI-qEHMmc53ZzSnDDxJlMWMdZ93j6CFbQYvDqlhYnmjSb-o-XSjDYEAiMdCKIpjCM5rXE3AFm8gDNxajnF2rDi19u1LfzX9RTFcAJ8p9mqf4woJPBZFWoRHNbRKaeRhI5S1oklmrwWlW53waZEVycjekhMnky5DhXuR-oEJ3sWed_aAFSB0v5Dkq5gezAhTFcXfEVon1CT1mQZ6U_aRexYK4w_uQobrgShNKxd_WBXmQFjD29ZDqgM3aVubfzDFbu2Q6G8x-WHKYX-95nSCR6aEXTVGONzcMNnXzqvqDvDxJAXMYITrFaV6DFSwERHx87WPT1RcLGcAunCbSKEzJPw44Ras4FT2lSESdOrpUnstkfeF2fL6bgBZ5P0C9qTeA4GW-RaB0c1ONq3KOF5F8z3mGqKG0C3HcSXPvUEvlCgA4NDO6hb49ZLhMjHiCBQmjH6NcxaTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99c18cdd66.mp4?token=ZDDHdmnUlEnFrbMyaMlB_bpuC4Fe9GWkCZxzC4Hj90JbwK4yXyi505qQH-R4txtE8FuPo7dCa6D7yW9q_T_5NjhcGSmwoIpV-aKd2jF17JzoLmV61uLgXZ8hJEa60YinkvixGrPv5LoZg926gLgcNYkxw2VPTl-vrLBjcUhKCpGn-1uhdzhPhNHnV2kRPkhNxNp088QN1xn-Caaga9HQpVM7ENiqC57PvRrI-qEHMmc53ZzSnDDxJlMWMdZ93j6CFbQYvDqlhYnmjSb-o-XSjDYEAiMdCKIpjCM5rXE3AFm8gDNxajnF2rDi19u1LfzX9RTFcAJ8p9mqf4woJPBZFWoRHNbRKaeRhI5S1oklmrwWlW53waZEVycjekhMnky5DhXuR-oEJ3sWed_aAFSB0v5Dkq5gezAhTFcXfEVon1CT1mQZ6U_aRexYK4w_uQobrgShNKxd_WBXmQFjD29ZDqgM3aVubfzDFbu2Q6G8x-WHKYX-95nSCR6aEXTVGONzcMNnXzqvqDvDxJAXMYITrFaV6DFSwERHx87WPT1RcLGcAunCbSKEzJPw44Ras4FT2lSESdOrpUnstkfeF2fL6bgBZ5P0C9qTeA4GW-RaB0c1ONq3KOF5F8z3mGqKG0C3HcSXPvUEvlCgA4NDO6hb49ZLhMjHiCBQmjH6NcxaTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آغوش امام(ع)…
🔹
لحظاتی از حضور شهید حاج قاسم سلیمانی در حرم امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/akhbarefori/680808" target="_blank">📅 13:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سردار سنایی‌راد: در جنگ احتمالی آینده تهاجمی‌تر از قبل عمل خواهیم کرد
.
🔹
رئیس سازمان بسیج مستضعفین: تنگه هرمز تحت کنترل و مدیریت جمهوری اسلامی ایران است.
🔹
گروسی:سازمان ملل در حال مرگ تدریجی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680807" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f319d54a1.mp4?token=fnuyY2hG6zY2ZVsxAixf5b80Vm_60omIbFygeV66yyqK3qLAFzaJ-d4X5l1_jedKM6_KRvXlAhhlGvRg83cjLdmOoiol7327TcznNqkLzHzVrV8AfmN0xEiVpfaAhFdtH_c2AFrUrCk8wu8PJXOHxmjUrQxSPkFx_RajNkto6rpp9ZhliAH4LgaOsakJS2D_DWQ68m5SAVBeg_uTGF3BrWIfNfHNwyape_0TFEzmFitPxero11xzmt3vrQ7ruC_et4x-fHObGf7KWDEwt80MicesTralIiiPrvJzpCWhD1TQKz5W6HpwdAG1L2gvidGpYhW1VgmMIfBlDrdQROKWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f319d54a1.mp4?token=fnuyY2hG6zY2ZVsxAixf5b80Vm_60omIbFygeV66yyqK3qLAFzaJ-d4X5l1_jedKM6_KRvXlAhhlGvRg83cjLdmOoiol7327TcznNqkLzHzVrV8AfmN0xEiVpfaAhFdtH_c2AFrUrCk8wu8PJXOHxmjUrQxSPkFx_RajNkto6rpp9ZhliAH4LgaOsakJS2D_DWQ68m5SAVBeg_uTGF3BrWIfNfHNwyape_0TFEzmFitPxero11xzmt3vrQ7ruC_et4x-fHObGf7KWDEwt80MicesTralIiiPrvJzpCWhD1TQKz5W6HpwdAG1L2gvidGpYhW1VgmMIfBlDrdQROKWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۹ سالگی دانشگاه را رها کرد و فیسبوک را تأسیس کرد؟ پس ماجرا به این سادگی‌ها نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680806" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تعرض شهرک‌نشینان به مسجدالاقصی
🔹
شهرک‌نشینان تحت حمایت پلیس اسرائیل با برگزاری آیین‌های تلمودی، رقص و سرودخوانی در مسجدالاقصی، برای تحمیل واقعیتی جدید در این مکان تلاش کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/680805" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قیمت ارزی مسکن در تهران به ۱۳۰۰ دلار رسید
🔹
قیمت دلاری مسکن تهران در ماه‌های پساجنگ به حدود ۱۳۰۰ دلار در هر مترمربع رسیده است؛ سطحی که معادل دلار حدود ۲۲۰ هزار تومان در بازار ملک است.
🔹
اگر دلار به این محدوده برسد، مسکن همچنان ظرفیت رشد دارد؛ اما اگر دلار عقب بماند، رکود می‌تواند مهمان بعدی بازار ملک باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/680804" target="_blank">📅 12:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
قیمت نفت کاهش یافت
🔹
قیمت آتی نفت برنت با ۴۲ سنت یا ۰.۴۷ درصد کاهش، به ۸۸ دلار و ۵۶ سنت در هر بشکه رسید و بخشی از رشد حاصل شده در ۶ روز معامله گذشته را از دست داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680803" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680802">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18209d3d0f.mp4?token=KKFQ0rnRYFgmqFWCfGv0jycx2D--2jBHg7Vkk8Kr0QMzZs_GdS9zRQ-_EyuXK-6XiA8R5trW13eYenhHrQ9DflhRTzWl0JDilXxp0TlCX1fCOl-wpHSgJSmnfwgoC190NX2eyztGx9Mu1laAK-qcFCXKsLndijT-AY1g8K2uWHf6YEKNDJOHB_Fy721ffNGBOa7Hl2xCLDclY1bP_HofidUuDF4-WKVd3LZMlpkZFHdyq2MjD617q_QmYISFRSW1uOZatuYjjyMWEHVaQ2I9VlZx5aLhrBdjtygODzS6aGJrf_yWvSYGjOFLBJO9g462i6Ih5BjD89V2yR4aiFDvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18209d3d0f.mp4?token=KKFQ0rnRYFgmqFWCfGv0jycx2D--2jBHg7Vkk8Kr0QMzZs_GdS9zRQ-_EyuXK-6XiA8R5trW13eYenhHrQ9DflhRTzWl0JDilXxp0TlCX1fCOl-wpHSgJSmnfwgoC190NX2eyztGx9Mu1laAK-qcFCXKsLndijT-AY1g8K2uWHf6YEKNDJOHB_Fy721ffNGBOa7Hl2xCLDclY1bP_HofidUuDF4-WKVd3LZMlpkZFHdyq2MjD617q_QmYISFRSW1uOZatuYjjyMWEHVaQ2I9VlZx5aLhrBdjtygODzS6aGJrf_yWvSYGjOFLBJO9g462i6Ih5BjD89V2yR4aiFDvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پناه‌گرفتن ساکنان کی‌یف در مترو
🔹
با افزایش نگرانی‌ها از حملات گسترده روسیه، ساکنان کی‌یف برای گذراندن شب‌های آینده به ایستگاه‌های مترو پناه برده و در حال آماده‌سازی برای اقامت در این پناهگاه‌ها هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680802" target="_blank">📅 12:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
توقف اجرای طرح عرضۀ بنزین با نرخ پالایشگاهی در کرمان  مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضۀ بنزین با نرخ آزاد پالایشگاهی در استان کرمان…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680801" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680800">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZz9v209agNHe3PCVw59Ek0t3waiuCag4kD5jwrzX0JYe9_uDHf7qhFFS6suH7nZrEUaymrPJSC77xsq7FgvdRwl5JdD2EAzvS-8pls1A27T3dzhzl1E7qT0ZgYH7YIPFlbdoJzr4_NTZYVShOG9LA95hQTuMi3r5rFYenJqOPSLItWhQhZtu71HYGQk3mzWaTIgGVtCIIgYZmsdkTaxl_k_Dc_ArbCkADVu3OgmREOBlFWWK8ZTiVXIcaE24VC2eLKpMfszU3HbJg7RTmUGcmAitKOvLh7XIjN882l1Homz6u2nPfzJlDaBt1Ze6mV2Hh11mlvv40NoyvOq17BWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ۱۰۰ سال زلزله در ایران؛ کدام مناطق بیشتر لرزیده‌اند؟
🔹
نقشه زمین‌لرزه‌های ثبت‌شده در ایران طی یک قرن، از ۱۹۲۳ تا ۲۰۲۳، تصویری روشن از پراکندگی لرزه‌خیزی کشور ارائه می‌دهد.
🔹
بررسی این نقشه نشان می‌دهد بیشترین تمرکز زمین‌لرزه‌ها در امتداد زاگرس، البرز، مکران و خراسان قرار دارد. مناطقی که در امتداد گسل‌ها و رشته‌کوه‌های اصلی کشور واقع شده‌اند.
🔹
در مقابل، بخش‌های مرکزی و کویری ایران در این نقشه کم‌نورتر و آرام‌تر دیده می‌شوند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680800" target="_blank">📅 12:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680799">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزیر نیرو: محدودیت‌های تأمین برق طی ۳ تا ۴ هفته آینده یا زودتر برطرف می‌شود.
🔹
۱۵حفار غیرمجاز و ۲ تُن سنگ طلادار در کلیبر آذربایجان‌شرقی دستگیر و کشف شدند.
🔹
ارتش روسیه مرکز فرماندهی نیروی دریایی اوکراین را هدف قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/680799" target="_blank">📅 12:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680798">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c3075fe50.mp4?token=uJw7Xwayccoma-u8eBN8HnYFVVaWjjsEkvv08Hh8XNPnscgBwiFVF21VoEQCcJiLmbM_R0GZTbAsOSXtOqr326RNU1_PX1KPRPB5dDZktkEvyIQWZ5s_PKHSmKdMF4ZOgX2qBtp_H9-Fyp7rchFk3V6SztnsbOTIBj2HVcAexrc768VhYo-PL1S6baXLL8YDfg4Sm-Z2dYuWyUAK0wFgwqpF1rdmg50raG1BKPxRM0cUsaVZhK9okTjEymfVkkucDAa5xV6DIk0TPMwk95G1ludrJN8J3I0G2cUuQJaulPLS6p8szWQIVMz5GnSklyWCJzygMyUSxHakcpmQujZigoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c3075fe50.mp4?token=uJw7Xwayccoma-u8eBN8HnYFVVaWjjsEkvv08Hh8XNPnscgBwiFVF21VoEQCcJiLmbM_R0GZTbAsOSXtOqr326RNU1_PX1KPRPB5dDZktkEvyIQWZ5s_PKHSmKdMF4ZOgX2qBtp_H9-Fyp7rchFk3V6SztnsbOTIBj2HVcAexrc768VhYo-PL1S6baXLL8YDfg4Sm-Z2dYuWyUAK0wFgwqpF1rdmg50raG1BKPxRM0cUsaVZhK9okTjEymfVkkucDAa5xV6DIk0TPMwk95G1ludrJN8J3I0G2cUuQJaulPLS6p8szWQIVMz5GnSklyWCJzygMyUSxHakcpmQujZigoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جغد عقابی با وجود ابهت و قدرت شکارچی‌بودنش، عاشق نوازش و محبت است و گاهی در آغوش انسان‌ها آرام می‌گیرد؛ ترکیبی عجیب از قدرت و لطافت
🦉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/680798" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680797">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f661e3f11.mp4?token=lAAh3-veCqT7IFf7mXAoT9hXLXxxQOxRRyq0H-sIlAm-d3bHXI9iQ7DiVtOWb_fNsijWcu2ZSXigLszGldONzug8fPgOJCv60pb3PSdU-mXmeHx_MSanGNrxkLn3_WelBVxCFF1hQJ_h-mqBKx0E2l926UGponWzQFiSWBsosME1V20eR84z8fzOV_mXPek269Yt-QlqNhjpiF9WhxqZjA9WL1ysQ03UVRSKhEZeBRf_jAQMCyt9bYOvc5c5zEfv1kvPa8shiQzN3oyyAOEpqC04oYqrcwqsAMW6AtEn3fPQz_s_4cZ8fnxf97EEAPtFAX2Vh2DcCuVj-LFMQzPz7j0cpoR1gISHa33lnIiAUr4G-qjtodft4z_eOOuD_qHCEzdSL-hf6S7aKYURurmzzYAGcfFaqb-zRt4o3SehTEL6nRE55Xa-tR7nqW2P8FFKQgu0UQtOFn19b5g9TxMfapSJA_0q9rOFxHi9DhCodl0XWCYmC44tmOTQr1ahXho_BLVXsFN024ohkrUITon0A9T5XAx0PawyQ3xSXEWVgqskgMIxuHTiSOSGVFEgEM-GKgt4djbV0RxAFIwWk-jvYbrLqjNMjgnUl1NktRPO_OKVz3uIo_dltMSHPcVD5VNs8LHi08dEYXYKc0Y4hfygWQzZ5BeyNR5C4U9-raTmOME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f661e3f11.mp4?token=lAAh3-veCqT7IFf7mXAoT9hXLXxxQOxRRyq0H-sIlAm-d3bHXI9iQ7DiVtOWb_fNsijWcu2ZSXigLszGldONzug8fPgOJCv60pb3PSdU-mXmeHx_MSanGNrxkLn3_WelBVxCFF1hQJ_h-mqBKx0E2l926UGponWzQFiSWBsosME1V20eR84z8fzOV_mXPek269Yt-QlqNhjpiF9WhxqZjA9WL1ysQ03UVRSKhEZeBRf_jAQMCyt9bYOvc5c5zEfv1kvPa8shiQzN3oyyAOEpqC04oYqrcwqsAMW6AtEn3fPQz_s_4cZ8fnxf97EEAPtFAX2Vh2DcCuVj-LFMQzPz7j0cpoR1gISHa33lnIiAUr4G-qjtodft4z_eOOuD_qHCEzdSL-hf6S7aKYURurmzzYAGcfFaqb-zRt4o3SehTEL6nRE55Xa-tR7nqW2P8FFKQgu0UQtOFn19b5g9TxMfapSJA_0q9rOFxHi9DhCodl0XWCYmC44tmOTQr1ahXho_BLVXsFN024ohkrUITon0A9T5XAx0PawyQ3xSXEWVgqskgMIxuHTiSOSGVFEgEM-GKgt4djbV0RxAFIwWk-jvYbrLqjNMjgnUl1NktRPO_OKVz3uIo_dltMSHPcVD5VNs8LHi08dEYXYKc0Y4hfygWQzZ5BeyNR5C4U9-raTmOME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/680797" target="_blank">📅 11:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680796">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
طمع ترامپ برای درآمدزایی از تروث سوشال دردسرساز شد
🔹
ترامپ به‌دلیل راه‌اندازی سرویس پولی Truth API برای دسترسی زودهنگام به پست‌های او و مقام‌های ارشد دولت، با شکایت جدیدی روبه‌رو شده است.
🔹
اینترسپت و بنیاد آزادی مطبوعات در دادگاه فدرال نیویورک علیه ترامپ، دو دستیارش و دفتر اجرایی رئیس‌جمهور شکایت کرده و این سرویس را «بی‌سابقه، فسادآمیز و خلاف قانون اساسی» دانسته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/680796" target="_blank">📅 11:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680795">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال کاهش قیمت گوشت در ماه‌های آینده
منصور پوریان، رئیس شورای تأمین دام در
#گفتگو
با خبرفوری:
🔹
در سال‌های گذشته در بهار و تابستان حدود ۷۰ هزار تن گوشت قرمز وارد کشور می‌شد اما امسال کل واردات به حدود ۱۲ هزار تن رسیده است، با این حال تولید داخل توانسته حدود ۹۰ تا ۹۵ درصد نیاز بازار را تأمین کند.
🔹
با افزایش واردات گوشت منجمد و فراوانی دام، انتظار می‌رود در ماه‌های آینده عرضه گوشت افزایش یافته، قیمت‌ها ثبات پیدا کند و حتی شاهد کاهش قیمت گوشت در بازار نیز باشیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680795" target="_blank">📅 11:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680794">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad4806f68.mp4?token=uOpqufIEYarAQzDtGq7iVBfRv693VbwTyh9z7-BDl_StBa1k67Y3f-Vnvm4T7ncX4zF-XsasoRDAqiqnUvu_i9VEunl0dL6gH49yVJwOkc-gkZDPnMxgHZufLOMUevtARn-j5_g2utgk5mqm_UZei9tgc3DEuXwQrNpxqm0tBh6za6j6Jz9jUf1s4LG3tGcs3WtqV-JlGYeHNNP39mj30SxdKTN5z9wg5nIoidRm8w-QQZm7Jw32uLD3rL0tVenFBhghue75ElRZWxUzrc0sKKTraWtufkiu1PXvhc4skvL-pZeW7BghgEOYDjHDv2ihLd76Qr0ZnXyKpfqmEAsjSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad4806f68.mp4?token=uOpqufIEYarAQzDtGq7iVBfRv693VbwTyh9z7-BDl_StBa1k67Y3f-Vnvm4T7ncX4zF-XsasoRDAqiqnUvu_i9VEunl0dL6gH49yVJwOkc-gkZDPnMxgHZufLOMUevtARn-j5_g2utgk5mqm_UZei9tgc3DEuXwQrNpxqm0tBh6za6j6Jz9jUf1s4LG3tGcs3WtqV-JlGYeHNNP39mj30SxdKTN5z9wg5nIoidRm8w-QQZm7Jw32uLD3rL0tVenFBhghue75ElRZWxUzrc0sKKTraWtufkiu1PXvhc4skvL-pZeW7BghgEOYDjHDv2ihLd76Qr0ZnXyKpfqmEAsjSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگوی جدی قالیباف و عراقچی در حاشیه مراسم شب شهادت امام رضا(ع) در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680794" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgokO-PTqaXz7gdOMDeg1gf22TaXygx2v6TypWp4Khoi_EpP4ITJQxvbt82rCdZvBDqfgTe7mj8oBObRwYDIlXOGqHHKiOevjDXO_X3Uyn9kk38XnWMTKkq0edvEXUQpjhjgx1XVJ2q5mE_Dj4IQVraHyqYyy1LijDKKgMNEwClK2o6MtNt3FXmF3QxrSiUQAH3icoDZsYlxZdmjsEWjnCq1T0u1R6LGptoC5oFBztsPhDINaky36_LHt9g-CbcfQGFV0cgLuYbgoZgKWCk_hIBx9Q5_jq2t_huBdL8our5te7xAQ6lkpuKsZ_R8Kqe_xvavYUH2TGj49nSSXhOqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIkZGPLXvVamE3uDzDjjXrfSxW0FusjUxBfBQhwM88J7FF6bTvzBaRPUV7-Z926TiRz4fiJFcE0LSljN065vzYJ-v5iy_5pYkUFbycFevcJuw5RfclwwE1o9Oq1Q0iOfNfncF3rrA49vC-cYnyN02JloVH8IUvL4khzk6lv9LbGzHNBxKUVBCmwXjpwhsANUuCNCsy-j8nX-Q-DeqiVg2oS51tpvJ8EM2sBPMbsHPeJemC5qc3G3i7SaJfhVtTtvAGhsr5ZujMPF4aK6ZvPfaAA0ZHYtpzVax9daFNCjxhfS0YhYDsHnMtkCZ_Ah2iC2ADJgN3ZbpyGYio70HXfUEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMEVI_3qYloyZ-6S6ISW0SvniI_JmiJQl4nlaBvkwpap7vpvY_FI3GD_LF6LEcvnNjegYL0VQyOEXdjRFMQAFj5dHld2HkiiVz_KkLqTFA5QqiwMNpB9rLQw_gRZWuwFZ0F4MWQCnyEcVmHwWs5cTu9qs7mfKksYRdNI0gv1MIEia2vH6MLTFi5ZYB0gXGiW508WiAO7M2JYi8ZZ0inNoRL57qfJzqcURsVx629rc6-wEMasKWVa6gDY9BMthiTjIlchZmIDtGUvz3e4qJ2uSb8xhMuEhuj2K6cloEzBg38vZIy5c0GSNai2WuVDVaNZaRE8-EzivwUa7XZ2BeGN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkORJQLuuZmd1OWztU9RzLto31QoY6Jsd11HOwdu6YZvlZblwNXSAbNtkJ02nn2_EdXOO9QzT0ILx45yjdoGBVr-vz0ADMxWg1t_AdFMHXN-qZfq6W5qtboXt33HkdLSs0-Ioww5Cnd54RGoHJNhnCprdee3Jz24N_DpJ-6vwTclF_jjeszce4cXlNeA_Wo6OgSXRg3_rO2veuo3Ll1IE6WY9TFjO3w5PCkeSRjtkeCAj06oY8JBkW6kJPL0C_0yC0Qt207Ra_5XtNLKDjBSFzw8DXgdCI5e97P0EycfVGkf-X0fNQa0-0rMh3JNzxO3Ib1x_iTu77-BqOQtKP6bUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvvCiAt_q-mUzPjEi9EZLcQMhrQOxchZ5sktQ2hhP7thDpwyyPMaERxHbDe4F9aPgmjGFlWAbskjib1z_YtWk0RsrY_fnYWiLm_MnWaLppagFO2xPD87tLCFk9iXbg8Hg_8DhHNqCdJFkBZdfu2Suu7yAL0xzCgwYbKn6PNBBBOHrm1W1g0dCqTj_kxB3izaA4_zTLnih9mTp9sNEqK-KazkDKNymdqhwvCH5rBcaKStquWu-lUlSf3b1FKsxybI1Ofaz-6D3dD2Ix_9WyYrK-6YO2ZxhRzxncjD6EKOnpTk3R2pzN1F8wafD63eHQu8U3VS0jP3Q4-RL9J0yDtwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai50DeVPamXDjnbTP1p8fKnghQGl5g14jjIsKvisPkcnDw5kPGmgX3QUpWWdSeAjD1Aa_ERUcLdvTzYF6q5fRQI6B_PmBsICB1T2-76jYuprWPyive7pI0fZz1SKZppZe4gkgn0qkvRUs7-44CPkc_fzDYny9WMkro1sQWpAbY8iKFSGc28bYU9aJqPrJh0fH188w7j6t1yZi8MXNVdcMLp23GVuRJTX8_BZX6dzGdvetoNWsDrPECwU9UYGXgMut_iS3vtO5zdHibT4mInpwgLWdbVDFXKVJ_5Mb6o1H1fSM-N-8aH4DOSFEzXuBBg5t1y6T8infSWTLUMgToiR_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از شهاب باران شب گذشته در آسمان کشورمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680788" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BByEozcjTFr-Hh2xkpgj9utOBNTpOuIQHHqUEq38j2XP_hCEqKqPefHn07y8Dr2_OV84NuqyslmWpfIBkd1bzErLsq6b7gYEDPJRxU-sl0Xt4Ov12TI_igWZl1Q_TNGg20iTRtclAV48utEWQysmfyx2i17cgMrV1R-oPr8EJXY6Kt_fbchnEQ6xR_ZGpjm43CX03UFgPhONeC0zhE4rQazqbGkQghzrGIPC2QoEyouhB38feyHe_AKmoK4rm7UMRjaWgZcY99KCUcTIaQ8-peO6iX9T_p0lqWZ26956rFdXBppLKtjeuSdeU4-t3OERwfRdokAAh56OWGdlgkVm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی خطاب به مقامات آمریکایی: مراقب اخبار و اطلاعات جعلی باشید
وزیر امور خارجه:
🔹
ایالات متحده مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگه هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
🔹
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
🔹
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680787" target="_blank">📅 11:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بلومبرگ: ایران در حال تهاجمی‌تر کردن ارتش خود است
ادعای بلومبرگ:
🔹
ایران در حال سازماندهی مجدد ارتش خود است تا با توجه به جنگ خود با آمریکا و اسرائیل، چابک‌تر و تهاجمی‌تر در خارج از کشور باشد.
🔹
نشانه‌ای از اینکه حتی اگر درگیری فعلی پایان یابد، خود را برای یک رویارویی طولانی مدت آماده می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680786" target="_blank">📅 11:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680785">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a99ba6b3.mp4?token=S9razJqrD39UFl3SovmcDPiomuNqNGORm4y8iE4OFC0QSOjYpZiPtd_nDECIOR9gwXH5QZg4IpRlKtZdEwU5fdAGM_QiNpPNP129kc77TJv6KRAoAGa_FSYUmowAMRNT5ivfAEj17_lhvuO6CbJ3_pQCui744J96QGXEVEaSFuQNADcWPsIPeVBMpdVYI99jGp_nk5lhOi194jBSpcdkw89S0xgS7BlwrjcbLzTc3stOlkNL24KA_b74JJjdCd5m4TDC6c5ySgML7t8DRzHcdBcKZe2vLlUpcBG2HwU0o5WkjsSKblEYFrOj5SgzOS8rxSIVMdC1yso2vJyR2yrbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a99ba6b3.mp4?token=S9razJqrD39UFl3SovmcDPiomuNqNGORm4y8iE4OFC0QSOjYpZiPtd_nDECIOR9gwXH5QZg4IpRlKtZdEwU5fdAGM_QiNpPNP129kc77TJv6KRAoAGa_FSYUmowAMRNT5ivfAEj17_lhvuO6CbJ3_pQCui744J96QGXEVEaSFuQNADcWPsIPeVBMpdVYI99jGp_nk5lhOi194jBSpcdkw89S0xgS7BlwrjcbLzTc3stOlkNL24KA_b74JJjdCd5m4TDC6c5ySgML7t8DRzHcdBcKZe2vLlUpcBG2HwU0o5WkjsSKblEYFrOj5SgzOS8rxSIVMdC1yso2vJyR2yrbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680785" target="_blank">📅 11:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680784">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llMP_c8Mrv24xfDjyL0yp4YnvsmOxjvrmCMzVWDXBN1azggNJzryL-gXRUTWsxFCnMH43rxY4mb6HLL9OkxDMMfvjd34j-shhNVAwiqBHQuJ8ZdhjqZs-C0uyRTMRGPdzL97qh4DHWXlwBHt28eNHfE7zqGEd1C96Db2J8XNUi5MrQrdLCHIeliFfFX8Z_9mOV-mmpmK0W2uaujvZM8eS0gn9tMxcArOrmAtxUXnH7O6RL747UkAzhk6Dy2dOzh74CVr1IfKpYSJwFadTpTKaI0HU6wBLg6VPdO8OgFastQN70u0jbqKuha6RIvNBsb6Ls1f-dM2ByAXyAcaQcUMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در خصوص ادامه شرارت‌های توسعه‌طلبانه رژیم صهیونیستی علیه فلسطین و سوریه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680784" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680783">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmo1s8RWXR02NDPqHYmWydHaQ9DlFC49bSI_1vz-WBsKfRhlsK-KrTUdC4Jl9ev-HHI0rvhGSyiBpJ2gDxtaoO2oUHZM71nopTisTXndNszylsPhPwIrD7FZH-sqIJ1XdIS8LA1BHdEUvJk-A_z97mPteJF2L25FzxcAGgJAKzOhWLVShIkiFTgxXjC8dAg4WDqduL_vfRgYRK_jx_551G8Ua8G5p7koxYwkcN_MuBA1zZvXTl5YLLxjnN52Q-JWhqyo81BttGwL5HLt9IBKJEhFXq_SgaFuRwzf8h-4Ma4yXaWuhx2bIZyvqRJsYr_6QrNxoVa7X2JlpWgBLrXjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکارچی غیرقانونی گوزن و مجازات عجیب قاضی
🔹
یکی از شکارچیان غیرقانونی گوزن در آمریکا پس از دستگیری و زندانی شدن، طبق حکم قاضی موظف شد تا زمان آزادی هر ماه یک‌بار انیمیشن «بامبی» را تماشا کند؛ داستان بچه‌گوزنی که مادرش توسط شکارچی کشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680783" target="_blank">📅 11:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680782">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای آزادی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در امارات
ادعای هرمز لتر به نقل از چند منبع ارشد در تهران:
🔹
امارات چند میلیارد دلار از دارایی‌های بلوکه‌شده ایران را آزاد کرده که شامل ۲ تن طلا به ارزش ۲۸۳ میلیون دلار نیز بوده است.
🔹
بر اساس این ادعا، دارایی‌ها در روزهای ۱۱ و ۱۲ اوت با یک فروند بوئینگ ۷۳۷ از ابوظبی به فرودگاه‌های مهرآباد و پیام منتقل شده‌اند.
🔹
این منابع هدف اقدام امارات را جلوگیری از حملات احتمالی آینده ایران به این کشور عنوان کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/680782" target="_blank">📅 11:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680781">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng2zJbrC7akL3HSR2-vQ3qOGAX29BNRJnT-A75g9yajgPcbZTRdPerFhaWnCwtbNpK-h1HUqRAU6xYsmOIGJ7r2us-zgtG3WtX10vKtVqKCQPYwfDyuewvBMT3PemxS_odQDmpivf966vSQBbqXFn9fXbCy77Pukzx88f5WP-9tA9PovAN5LqsZ2oNP2TJAkeJ9HiTQSs--hmYEHM7h9W6AJtOSaghwCCzTbKmDme4Ku53xc82OHQJ_k_SCCNBnjT7QPO1-eTrpnMHvJw-WA9v4KOe5aPUWPRsHghGh0Eg2-wigPhhgxX-1AdOl9hlAqOhEucWU0MSPM1i4K0UfH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهارمین تماس نخست‌وزیر ژاپن با پزشکیان
ژاپن‌تایمز:
🔹
سانای تاکایچی نخست‌وزیر ژاپن، به پزشکیان، رئیس جمهور ایران، گفت که تضمین ناوبری آزاد و ایمن بدون هزینه‌های اضافی مانند عوارض ترانزیت در تنگه هرمز مهم است.
🔹
تاکایچی در تماس تلفنی ۲۰دقیقه‌ای خود، از رئیس جمهور ایران خواست تا با جامعه بین‌المللی، از جمله کشورهایی که از این آبراه کلیدی حمل و نقل نفت خام استفاده می‌کنند، مذاکرات دقیقی داشته باشد.
🔹
این چهارمین گفتگوی تلفنی این دو رهبر از زمان حملات امریکا و اسرائیل علیه ایران در اواخر فوریه بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/680781" target="_blank">📅 10:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680780">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2eee1044.mp4?token=gtBoYrgJC1M-DNZr7iHDSgv1WSsq12eNE9R10ouK-KmyWwM-JeY_rWkbkft2BVI-BvlGq2rr0p6mFgTbq3qhrNWKSmyC0_UZyymQ9NAyo9JlaSppKtfa-QlorFhUhySQNYAXWRHskbCcliCSkmyN9Yg8U7hPpML8CPPUTHZX75VMXfterk7XHkd0WnfrCY23Ilc5dMVmqxq53G47d1Ss9UwBsTGrKMyWStauXr-plvyIdwsFcsaLPOeGUElEbZHjSS5BbzllsH4ViObI7GB7aeJwPgo49Lm-1EyjhGq5B7ROwCKXIR6QhsigjCfM2iTPWppzNnsq-LHt4icyq-nlag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2eee1044.mp4?token=gtBoYrgJC1M-DNZr7iHDSgv1WSsq12eNE9R10ouK-KmyWwM-JeY_rWkbkft2BVI-BvlGq2rr0p6mFgTbq3qhrNWKSmyC0_UZyymQ9NAyo9JlaSppKtfa-QlorFhUhySQNYAXWRHskbCcliCSkmyN9Yg8U7hPpML8CPPUTHZX75VMXfterk7XHkd0WnfrCY23Ilc5dMVmqxq53G47d1Ss9UwBsTGrKMyWStauXr-plvyIdwsFcsaLPOeGUElEbZHjSS5BbzllsH4ViObI7GB7aeJwPgo49Lm-1EyjhGq5B7ROwCKXIR6QhsigjCfM2iTPWppzNnsq-LHt4icyq-nlag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رم کردن اسب در ساحل بابلسر؛ آسیب شدید دختر جوان
🔹
یک دختر جوان هنگام اسب‌سواری در ساحل بابلسر، پس از رم کردن اسب به سمت پارکینگ خودروها کشیده شد و پس از برخورد با چند خودرو، روی زمین افتاد و به‌شدت آسیب دید.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680780" target="_blank">📅 10:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680779">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نجات ۲۰۰ نفر از حریق یک مجتمع اقامتی_تجاری در مشهد
سخنگوی سازمان آتش‌نشانی مشهد:
🔹
حریق در اتاق برق یک مجتمع تجاری-اقامتی در خیابان آیت الله شیرازی با  سرعت و هماهنگی مناسب تیم‌های اطفا و نجات مهار شد و حدود ۲۰۰ نفر از ساکنان و مراجعان این مجتمع به‌سلامت به بیرون منتقل شدند.
🔹
این حادثه هیچ گونه مصدومیت جانی در پی نداشت.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680779" target="_blank">📅 10:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cccdaf35a3.mp4?token=EoQbn5la2d3mmwG2rOg-7fQCYo7uFzOPp2F98VkzAFial6lpwLyK27JtP1rslyCy7oCzLWLt0Ddxb-zk8BW_WUJZWjfsWHTNow0JS3W6zjWKBper-GrocG21ueEeTMi0jiaYhKg9NPOHOfuRQeAFPounOCELb_KzPzln7T5HXAlqm1L7SNZGdsKTiBggutrHm7bIvAi0D3t4WUrM6i2KzqO-I0IA9kBk2vNIA1Kp_PNL5maXPZoMs5eqN6J93Y0v3Fy5ehnLPXnmHdlds4t04gLw-dfHRq4N1SP_a8rJ4l4O_3cdgna0zYNZ5H_bGUJ6Ayj5Ba6FP6JFs805X8Zwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cccdaf35a3.mp4?token=EoQbn5la2d3mmwG2rOg-7fQCYo7uFzOPp2F98VkzAFial6lpwLyK27JtP1rslyCy7oCzLWLt0Ddxb-zk8BW_WUJZWjfsWHTNow0JS3W6zjWKBper-GrocG21ueEeTMi0jiaYhKg9NPOHOfuRQeAFPounOCELb_KzPzln7T5HXAlqm1L7SNZGdsKTiBggutrHm7bIvAi0D3t4WUrM6i2KzqO-I0IA9kBk2vNIA1Kp_PNL5maXPZoMs5eqN6J93Y0v3Fy5ehnLPXnmHdlds4t04gLw-dfHRq4N1SP_a8rJ4l4O_3cdgna0zYNZ5H_bGUJ6Ayj5Ba6FP6JFs805X8Zwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابراز همدردی کریستیانو رونالدو با کامنت زیر پست لیونل مسی  رونالدو خطاب به مسی:
🔹
لئو، در این دوران سخت، آرزوی سلامتی و آرامش برای تو و عزیزانت را دارم. امیدوارم قدرت و صبر داشته باشید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/680777" target="_blank">📅 10:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده ۵۰ درصد کاهش یافت
حسن کریمیان، رئیس انجمن مراکز اسقاط و بازیافت خودرو در
#گفتگو
با خبرفوری:
🔹
مراجعه صاحبان خودرو برای اسقاط در یک سال گذشته حدود ۵۰ درصد کاهش یافته است.
🔹
در حالی که ظرفیت مراکز اسقاط حداقل یک میلیون خودرو در سال است، اما بالاترین میزان اسقاط ثبت شده، ۳۵۲ هزار خودرو بوده است.
🔹
اختلاف شدید قیمت خودروی نو و فرسوده، نبود تسهیلات و وام برای جایگزینی خودرو و همچنین نبود الزام جدی برای اسقاط باعث شده مالکان انگیزه‌ای برای اوراق کردن خودروهای فرسوده خود نداشته باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/680776" target="_blank">📅 10:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
این مادر نیازمند حمایت شماست
🔸
این خانم مبتلا به سرطان سینه است و عمل جراحی ، شیمی درمانی و پرتو درمانی انجام داده است که هزینه ای بالغ بر 600 میلیون تومان  در بر داشته است.
🔸
به دلیل نیاز شدید مالی و بدهکاری ناشی از درمان ، وادامه درمان نیازمند حمایت شما عزیزان است .امیدواریم بتوانیم بخشی از هزینه های درمانی وی را پرداخت کنیم.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/680775" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1325d5d528.mp4?token=G9fmv9yFpQ-hpHyO9xlZV7pgvWjJhe1AAIaF0CLFGFgUL0KnQcsSS5QhEHLYUJ9Ayk0faxQmYoEtzVU_VxhwVSJ_6IV-38u7haroC32OpSZXEm4vG2XmDHBtNXPUzjuVhF4LlACd_exKsHlEWS4GEaDqWK1eOf1W-HMAKsQBDHAWNNIbzHkc-bXe38BqvPbamI-p1muWqQZDs1FoBto8_hG2aqNp2baYQHyr58qWg2khCSpiOdctIRbaiPcSQIJ8hPqlJt4RoXyNkFZKIR1m82FF3lM1Pr_23yTRDObzi-28CJpvQHyFy6aaLa3xfaD6DiN7eeVTfQak5vEe16u6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1325d5d528.mp4?token=G9fmv9yFpQ-hpHyO9xlZV7pgvWjJhe1AAIaF0CLFGFgUL0KnQcsSS5QhEHLYUJ9Ayk0faxQmYoEtzVU_VxhwVSJ_6IV-38u7haroC32OpSZXEm4vG2XmDHBtNXPUzjuVhF4LlACd_exKsHlEWS4GEaDqWK1eOf1W-HMAKsQBDHAWNNIbzHkc-bXe38BqvPbamI-p1muWqQZDs1FoBto8_hG2aqNp2baYQHyr58qWg2khCSpiOdctIRbaiPcSQIJ8hPqlJt4RoXyNkFZKIR1m82FF3lM1Pr_23yTRDObzi-28CJpvQHyFy6aaLa3xfaD6DiN7eeVTfQak5vEe16u6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در تگزاس
🔹
یک بالگرد تهاجمی ارتش آمریکا در مرکز تگزاس سقوط کرد و آتش گرفت؛ هر دو خلبان کشته و ساکنان اطراف تخلیه شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/680774" target="_blank">📅 10:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680773">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
امبری: عملیات امدادرسانی به نفتکش حادثه‌دیده در سواحل عمان
شرکت امنیت دریایی امبری:
🔹
در عملیات نجات یک نفتکش حادثه‌دیده در سواحل عمان مشارکت دارد و شناورهای امدادی به محل حادثه اعزام شده‌اند.
🔹
این شرکت تاکنون جزئیاتی درباره نوع حادثه، وضعیت خدمه و علت آن منتشر نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/680773" target="_blank">📅 09:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680772">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است.
🔹
فرماندار جاسک: عملیات خنثی‌سازی مهمات دشمن امروز در محدوده هوشدان و پارک سنگ سیاه انجام می‌شود.
🔹
۱۸۱ قبضه سلاح غیرمجاز در خوزستان کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/680772" target="_blank">📅 09:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIgKN0WNWlwihZga6xkl9aySyccPn544cACo1jnrRaMSXDqpEQx6OAV-BIaltNhU_R5tY8oMs20Lgo8HzUVFCIlgAFG3k78I2fGdGOTgPdtoYHCODhcf_0RlAYr8b1rYNgDu4VA6yGhMdqzzxz9LLTAllYUepnLzcTy8a22CGyTJKuN0rdxmSc8Om_-u0IvxkVAqqsdm8LTBq6szAIr8f2EN1Un2thNUCCCftHRhXs9Lu2COZiltwGYMtYG-FZYGR_Cvfk-7dVl2fW9g9V-ay1vLJ-IwnTqtTx0ySustmvR186AmBZdO4Tn0l1GV9wvwnJSn4PvbqvX_QzJ_Xi1ROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680771" target="_blank">📅 09:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
جنگ، بازار طلای ایران را تکان داد
🔹
تقاضای جهانی جواهرات در نیمه نخست ۲۰۲۶ کاهش یافت و سرمایه‌ها به سمت سکه و شمش رفتند.
🔹
اما ایران و خاورمیانه برخلاف این روند حرکت کردند.
🔹
در ایران، همزمان با جنگ، خرید جواهرات ۲۶ درصد و خرید سکه و شمش ۵۳ درصد در فصل دوم سال کاهش یافت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680770" target="_blank">📅 09:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb0ms43HDm3FwqUEFDKXycS7YoUAqwIgSUKrLRKSbiEm7J9IHn4iXmjQ-9fRp_OsVlDe8EwTAdXSnSUzAKIZkDEO7hvfdTTRdO1Z7QXM8iX1rBjRWnLr8YCuIUjh-hz3R3gzi6CWKknCHtRP3dqDSTTOinNuJFQ8Ar0igwq8kqBP6yew9BMKl4bz06yGw53cIF2OxX1GcvhVljjU8zBM8r4ip3homxrk_6hMYbL0BQdS4TNW2ik0epmf_KahD_APFCy2WPCbHYZHF_lsd3P6o8Mg3cI-Ykx3uh_zzLcwCXPZHrFDmEx1ia3is9LRAjfhvO6panratVkddZNwywbizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53a12ca2c.mp4?token=JIH1qxRup4BBaWF-X0_k_13BWyQVAeDKiNuP5v-x5W5U4l5kMli-NFspznhrLVryDlQHLg-EHCdf7BErcjkSxU-BBYECECoCQhiF4mhWP-UVRnN9PDfs-CxMBMWkj0vHIGDpaae8K1wfoPfVrNp2dDJPomB3jtC946D1Z33blZ2-gfHwXtEBWbCIN59PspF_E9s5wrK38YFFhK7oKGS5qGt---tjMH21NEqqQLVO5ZF1oJQ1EdHUVtajSpRqb0FGxKOE1O034-qkAxDnSPosOVWsnY4uGE8HalWn-uxgIJ0Cpho7AZpfVF7Ck6jHXlvKCvJfvJ4g5p1ysGCMNyJR00AoMgOauuqbW_sefDVoFcESbo9IdxGqUrZiYkpykgEHpm5xSaBPfADsYpBhERs_04X9fUIYqF-d6EtFISt2jN6lcDQkGT8XEo2Y1dphqex5FftwL0vDMeyShTk4Qx99n-HR9jvAdi6-XPKspfQUknXrTcYlr5yvBtZyscB_flvFB0OiKkZU6YPFffJc1YDku1fvAdqYdcLeCqAd6Ev6kTjQBj6pOfyLhUxJ_mocludTsxRV60RxOvaa9-1q9VmwmcApD3OtKfFklMSadBuoq76wa0Ep6Ib7u0rt10wnoT1OOUZIcHVg9v43FLO0jLj63ui6mB6vZPrsNOJvhjwvUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53a12ca2c.mp4?token=JIH1qxRup4BBaWF-X0_k_13BWyQVAeDKiNuP5v-x5W5U4l5kMli-NFspznhrLVryDlQHLg-EHCdf7BErcjkSxU-BBYECECoCQhiF4mhWP-UVRnN9PDfs-CxMBMWkj0vHIGDpaae8K1wfoPfVrNp2dDJPomB3jtC946D1Z33blZ2-gfHwXtEBWbCIN59PspF_E9s5wrK38YFFhK7oKGS5qGt---tjMH21NEqqQLVO5ZF1oJQ1EdHUVtajSpRqb0FGxKOE1O034-qkAxDnSPosOVWsnY4uGE8HalWn-uxgIJ0Cpho7AZpfVF7Ck6jHXlvKCvJfvJ4g5p1ysGCMNyJR00AoMgOauuqbW_sefDVoFcESbo9IdxGqUrZiYkpykgEHpm5xSaBPfADsYpBhERs_04X9fUIYqF-d6EtFISt2jN6lcDQkGT8XEo2Y1dphqex5FftwL0vDMeyShTk4Qx99n-HR9jvAdi6-XPKspfQUknXrTcYlr5yvBtZyscB_flvFB0OiKkZU6YPFffJc1YDku1fvAdqYdcLeCqAd6Ev6kTjQBj6pOfyLhUxJ_mocludTsxRV60RxOvaa9-1q9VmwmcApD3OtKfFklMSadBuoq76wa0Ep6Ib7u0rt10wnoT1OOUZIcHVg9v43FLO0jLj63ui6mB6vZPrsNOJvhjwvUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت امام رضا (ع)
🥀
درد و دلهای من فراوان است
بگذریم از شما چه پنهان است
پیش تو هر کسی که مهمان است
درد هایش نگفته درمان است
شهادت
#امام_رضا
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680764" target="_blank">📅 09:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
گاردین: چند ملوان ناو آبراهام لینکلن قصد پریدن به دریا را داشتند
🔹
خانواده‌های نظامیان و اعضای کنگره در مورد تشدید بحران سلامت روان در ناو هواپیمابر آبراهام لینکلن هشدار می‌دهند، چرا که ۵۰۰۰ ملوان و تفنگدار دریایی این ناو، استقرار بی‌سابقه‌ای را در دریا…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680763" target="_blank">📅 09:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزارت حمل‌ونقل مصر: کشتی تیهاما (TIHAMA) که در سواحل یمن هدف قرار گرفته، پیش از این هرگز وارد بنادر مصر نشده بود و به سمت مصر در حرکت نبود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680762" target="_blank">📅 09:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNSaYmvrGdB6dUEaBMd68TqZ1Hvq0ql4IuQ7XA9TyClkvY9FHAxbWcQWpY4SfB9mg04o_MgKd-JrYDlYG42cSDiHLPHAe_pUAVeEtxtJiB9pjivCFwgZWZt6_WvrNC9rPy07kEIPTupOhOQ8pKtpNicv1p9vTME0lGHeuRZZdgVTkLBap01Rx-8vXL2RY68p2__rixf23nkk6917ddO1tBL4pO_bm6qH06OS1RXy0Po_jfML4vmD6EspqPnycq8sI_Q7Xvce876Ug6xqLgKBSdkzRSuCbg7-cwlPYjFZ_jjGVCXuCnwcReJ4UmcYxN1OGf6Wa-hUiiMcx1gMQXgBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پردیس احمدیه برای شهادت امام هشتم(ع): ما عزت خود را همه مدیون رضاییم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680761" target="_blank">📅 09:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOBBvuFoB5Wi0ig_byzQNPNNPINJyKYKLeAbOqhheMkNDw1GBJHtJ9k48yszQgzIW68quFnN6OYiv7aWk44yHNjsPqdm6mo9FygSs80IFlv9hQgw7ER2p3Bo67j5Mn2RkPXv6CiuA6Hc7acvQYHMYEKQiIV6R873Um4_kufSvVUG_KUZ9XO5bFeGh4Zv506O53VL2Xy7ZWHP__kCzg3AmYGiAkcOLm0WfIEs7fKQ9ZyoQCGfAV-zn3QFw5UwmZFoIQ-_J8RULJCIGv1Spx5FwfPVNTl0MzsDU8SI0hzaO7XFykpkkCaVbyJsj7sxxqengsXPPhoglLN57FfpCAFGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ان‌بی‌سی‌نیوز: اولویت ایران از سلاح‌هسته‌ای به تنگه هرمز تغییر کرد
ادعای ان‌بی‌‌سی‌نیوز:
🔹
ایالات متحده اولویت ایران را از سلاح‌های هسته‌ای به تنگه هرمز تغییر یافته ارزیابی می‌کند
منابع می‌گویند مقامات نظامی به دونالد ترامپ، رئیس‌جمهور، گفته‌اند که هرگونه عملیاتی برای تصرف تنگه، طولانی، پرهزینه و مرگبار خواهد بود آن هم بدون هیچ تضمینی برای پیروزی./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/680760" target="_blank">📅 08:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680758">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428a512e23.mp4?token=IfLOXkmbnMN35sqAkWeYvZWOQst1Z-0crB1mWr7lPSS72J3yB3IZTkjrBSB09D2ztkjwqX9Fg5i6-rK0Cf-Atd2L1THObIZk8xlcggMajxzYR-81f4O6zxaWzJozgjJufAfb-LY-jLTyBVR6oURfXJ8ZrlJMHyuANhpMeXDnU1qt8ORMEbSyp-m50I_inYBiKwjGNoF_bfy0nOmcPYCMmzoyCF-pcu2ZO28R6hSVhMxohObkPNE5mZKhm8i4yBkxngdmrfF-vto_yED6qJUotYJTnA7iVx5aGciL66I9b9x2VWyGxaz2ipLi0Wy78MpyNI_tyfjjculK_1Z53pRGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428a512e23.mp4?token=IfLOXkmbnMN35sqAkWeYvZWOQst1Z-0crB1mWr7lPSS72J3yB3IZTkjrBSB09D2ztkjwqX9Fg5i6-rK0Cf-Atd2L1THObIZk8xlcggMajxzYR-81f4O6zxaWzJozgjJufAfb-LY-jLTyBVR6oURfXJ8ZrlJMHyuANhpMeXDnU1qt8ORMEbSyp-m50I_inYBiKwjGNoF_bfy0nOmcPYCMmzoyCF-pcu2ZO28R6hSVhMxohObkPNE5mZKhm8i4yBkxngdmrfF-vto_yED6qJUotYJTnA7iVx5aGciL66I9b9x2VWyGxaz2ipLi0Wy78MpyNI_tyfjjculK_1Z53pRGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
چایی حرم دوای همهٔ درد های ماست…
🎙
حاج سیدمجید
#بنی_فاطمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/680758" target="_blank">📅 08:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374cf66245.mp4?token=tw9HP0851i3KZSau9p3pXWEq9oG90AhCQSG2vnABVwopaCyFSeYvu0R_HHe4zEe7jZJfvfQjytVz_dEt0OUX2NWXPt1b2FlQXj9_mnGFhvlwhgtbiw3SQqd8vnGJyuSsafUUbNAOQzGCyUF5YpC7m8le7j4SKWgeJgNOnIe05FpZbyHhF8rcGmUTrGhm-kh3mr_YQWJvwS5jfqhYUPAhWkL2v7eVr2ma3VGoeYwQlVSMDyGhKJplmGjFP11_VC75-ZtWYCt0t9EoMSRaCTm3RiIEwSDnYXrsiVFzPwHvY54Zwxb865eP8WUVPPa1Dfd0YGa1kkGXdFEHOFZPFAK22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374cf66245.mp4?token=tw9HP0851i3KZSau9p3pXWEq9oG90AhCQSG2vnABVwopaCyFSeYvu0R_HHe4zEe7jZJfvfQjytVz_dEt0OUX2NWXPt1b2FlQXj9_mnGFhvlwhgtbiw3SQqd8vnGJyuSsafUUbNAOQzGCyUF5YpC7m8le7j4SKWgeJgNOnIe05FpZbyHhF8rcGmUTrGhm-kh3mr_YQWJvwS5jfqhYUPAhWkL2v7eVr2ma3VGoeYwQlVSMDyGhKJplmGjFP11_VC75-ZtWYCt0t9EoMSRaCTm3RiIEwSDnYXrsiVFzPwHvY54Zwxb865eP8WUVPPa1Dfd0YGa1kkGXdFEHOFZPFAK22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی خیره‌کننده از طغیان آتشفشان اتنا در سیسیل ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680754" target="_blank">📅 08:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/680751" target="_blank">📅 07:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuiKPjJqtIbtbSeHL3G6sFGsvglBVKIFB3-6dfy4bUzUclLyMgrc_9pQKnG_KFKeyGvFiPjTjZNGbaKDvgtHbzzMfoPnfdG4q3vQfzeCFcqTzz-c9VY95ntnKUSF2pMgeDW52nMZ4sRGPUvL_NdjsBjUg1jl-ApMgaxRXDR_FPfeoRoN79n_oJYcx43oDLqMDutMCLE-28CQPriCYxvZhCNLvE19VE_ZHo5orPGTloIOxhkgzYKS1KAxHvLnn6_j5ihrWcxAHvI-FA-K2AvhDnwLGmAcBJD1aFf5BikEoZEFfVd3p5dW3AvuFP-ZXIcID9vlUyfZD9eSGjEEKDOjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: از ریاکاری دست بردارید، واقعا از اسرائیل حمایت نکنید
وزیر امور خارجه:
🔹
کشورهایی مانند فرانسه باید از موعظه کردن جهان درباره «حقوق بشر» و قوانین بین‌المللی دست بردارند. این ریاکاری آشکار و شرم آور است.
🔹
حمایت شما از نسل کشی رژیم صهیونسیتی در غزه، و حملات تجاوزکارانه به ایران، هرگونه جایگاه اخلاقی را که فکر می‌کردید دارید، از بین برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/680750" target="_blank">📅 07:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiOqu88qacbTEPQXDA4---BfDudzwHLn8JUayMhdHP2x_ppElqLEHlJI1LIWp1LicPfpX3JChEt5URqbIZUzTd2f21HnaLW--FmGfq4qaCspNmvbdPXTzBwMORVrco1Y4YyPtcQO5dxZEdLdBoXAUfP-zaYn_SkrhEqHxumyi9okry7dcEiUQkY3UyMogcd9UqYSmUuifqN4a8EKHDDbLEtFsh-pqdLf1NH_T1NVAR_piepH_HUsWbNSzIDms2ipiz1rtQbhUHc4Kt0vpZ2fZ4ayJbFqg5MfZ9TBYaVBy4avHCHxTUZBR2pHxq3lNaMJIFhPW5DAj7uC_k4AW8aUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایکس، حساب یحیی سریع را مسدود کرد
🔹
شبکه اجتماعی ایکس به مالکیت ایلان ماسک، حساب کاربری سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن را مسدود کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/680749" target="_blank">📅 07:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT2bVvl3dKPdpSgP-WWiNK_254twKQp6Ke-YS3gj8WNzQtAfDmNf-cSr0IbHYZce6ehSay8EAku3CA0Y6waOhePmYMUz18eigrIAElLGkMMgwZ9bSQt_1uXp_ufOPO9PFi3vx6RxazUbFa9uCrizMBeUGLlgGGVEIahpeT42fnOKUSaByWGp23lCpSRNVGlg8onGYo__ZHU5-L6A8QZGhbrJPYDaJdnhX8BMQGf6wsGkfq4ueUO63hKowgJNIhoMPIWe5n8Znul1xt6O3WEjs67ms_IQhJwG8yynGVGzx__OCLVhWawePrpWrf23ok4AuG3YjfIoZ33EM6j6MO-UPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۲ مرداد ماه
۲۹ صفر ۱۴۴۸
۱۳ آگوست ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/680748" target="_blank">📅 07:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-wkqVx9--JBWNiC5bXvMjuMA7FpZl_FcL-cmYAMEOv8mrLNReZVolGDKShSW6MDCm_7xjFuS2UFFxAN7bBtYETz5FmMVj2-pDKVaATcwZQ8dCnRshH38jnLCfN4Yr4GzcLgtwv7UhaNk05xXajgzqaIfuN_-Ch28tC0JNNifUr0Z6VEi2EtqHMvagjpiyUqWBY9W58nmsqDpe6HHCxerRIEZ_ZsAqAZOreEoCvBrUaMVZTKUl2P7Q3m7vjU6TkLA13ataXYUXaXRj9KhF0rjXy7IIPr5tAtE-XvJVLeGy6ea3hStEDCZz4UVFCncvlYape2LR46AVCkQWSyZ1oNvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمِ پرنسا ۴ ساله
، به‌جای خنده و بازی، تخت بیمارستان و شیمی‌درمانی‌های طاقت‌فرسا شده است
😭
💔
پرنسا برای ادامه نبرد با سرطان خون به داروهای ضروری نیاز دارد، اما خانواده‌اش با درآمد اندک کارگری و خانه استیجاری، توان پرداخت هزینه‌های درمان را ندارند.
😢
بیایید نگذاریم کودکیِ پرنسا روی این تخت‌های سرد جا بماند.
🥺
🤲
✨
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
5054167000199647
6037691990491185
IR690640012874000943700001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/680747" target="_blank">📅 01:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49436f0adc.mp4?token=ikJyDo9LPc55g_xy-UKipkjSp7pIiTFQbIY3NNyfxyFVg3kDfSqRmIpv07Xa5V1n-pMaTQZtIQ0M8UY3aoajUnYb41o2H23Xcst1jbw7HHwe2_y3_n0Q8OfSryFViFkE_00_6JDkHzYJhGXEBf5Z3ARs7EG1rLJMtw7yyDPDQUdKIOqfOyzck-1GRdk6ZPG7J5i3b_YWbxgplvncGs6VwKNfyrRTnrIpf_bETjGIweeOUt0LrUrIVBM1GaVjeTKgTC5bX5q8pbk7mzX0uYHiu5vD8Od0_Y66_upVsdf0qGdv1Ity7GiKfqjLlUSbr-fQGk8DwIvAN-MbGnZQm7vBmQj1Ipu-kA-KBTBbfNTNjfpoLQxYEmOk3QF1fRlI_l94veWMZd1ky86BYNVbIp5m1SlStk3T_e1Ag7OeJauu6BDbau1QHlkXdxNJWyQUKH9_XEQfEOsvOnSzs3nUTP8AI8z2A1EXbZJ7Jwk4R8wwVFJFDW4T6kB6sJv7H_cCKo_8c7HkaZSn9RLdjaqWUwZk4YOg9r1aO6MuVFW2NwgW0ecNVddrdD-OPp3_P0eoDeAf3QMFyk7PFhk7M1J3G0afZs4OYsZ7T07ryus1CdqvJt0BMkEiJSbpWQoPmtBfRAfkYRBKdir8RXbW4QY1cTO5xY3cwowCsk3MCcgO25H6grs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49436f0adc.mp4?token=ikJyDo9LPc55g_xy-UKipkjSp7pIiTFQbIY3NNyfxyFVg3kDfSqRmIpv07Xa5V1n-pMaTQZtIQ0M8UY3aoajUnYb41o2H23Xcst1jbw7HHwe2_y3_n0Q8OfSryFViFkE_00_6JDkHzYJhGXEBf5Z3ARs7EG1rLJMtw7yyDPDQUdKIOqfOyzck-1GRdk6ZPG7J5i3b_YWbxgplvncGs6VwKNfyrRTnrIpf_bETjGIweeOUt0LrUrIVBM1GaVjeTKgTC5bX5q8pbk7mzX0uYHiu5vD8Od0_Y66_upVsdf0qGdv1Ity7GiKfqjLlUSbr-fQGk8DwIvAN-MbGnZQm7vBmQj1Ipu-kA-KBTBbfNTNjfpoLQxYEmOk3QF1fRlI_l94veWMZd1ky86BYNVbIp5m1SlStk3T_e1Ag7OeJauu6BDbau1QHlkXdxNJWyQUKH9_XEQfEOsvOnSzs3nUTP8AI8z2A1EXbZJ7Jwk4R8wwVFJFDW4T6kB6sJv7H_cCKo_8c7HkaZSn9RLdjaqWUwZk4YOg9r1aO6MuVFW2NwgW0ecNVddrdD-OPp3_P0eoDeAf3QMFyk7PFhk7M1J3G0afZs4OYsZ7T07ryus1CdqvJt0BMkEiJSbpWQoPmtBfRAfkYRBKdir8RXbW4QY1cTO5xY3cwowCsk3MCcgO25H6grs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انهدام انبوه پهپادهای FPV اوکراین توسط پهپاد روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/680746" target="_blank">📅 01:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNb_sxNyBky7zbLFqHa0cPSh8NyP0WRioBiRbACPPSDc-TherGgmWGdU0dw_ejXjq7IvCw03PuW5BATP1F0CEc8cYxfBj4uu94fvxWZ9UI9v9HjOD8zSwMZCMaBiQmKWiB2XkjPWnVRujk1V3B3Buv80hCxUCufGT2qK9BhQoLU3gty96NiVd_S49kTY5r0iK9to_VxRC6ui1U9mF7mdycBwHPkeH3ISWtgZFQjd6gQMFkoC_jDXANrrHMWxdr_1w-XZ-i87ApKkoEIG3JmG-T3NjYiJXv8O7NCrFFsTX1lgOK_H_ImKzAbx3pyVpNjenHU3tvB0QsnqNV8ZVEKwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b56de157.mp4?token=scpo2MdkmGYHyBVvg4j1QKlUs7E5Ac13Kv2BT4h79ecn5tBgP5J_c0ak6J7xHIHeVcTtg2NfoT_llfDydZjyJY4OOYzqi5p7Bv4iEriyndH8Q1eoY0nwTjRuOm_-RYRoa0fv3Gd6GobXgY6L1Yl8gF1qagobbRwBXvbY2-K1Sgm2p1B7RS0fULr48lPhpWHXCzajMPtmRtOcS3ZAKAYfjO7O1cByWcKEQ3ZSjvXBEynt9XuBEuNqJLRD-NJ_kR0m9B1DQKPK1ZLc4Bg4iNi753H3TxU1kesSQaKblbUB3M3WR4aq4uhsa9YTPqbQmIZuaQdEUajZAwi90mLh8YbDAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b56de157.mp4?token=scpo2MdkmGYHyBVvg4j1QKlUs7E5Ac13Kv2BT4h79ecn5tBgP5J_c0ak6J7xHIHeVcTtg2NfoT_llfDydZjyJY4OOYzqi5p7Bv4iEriyndH8Q1eoY0nwTjRuOm_-RYRoa0fv3Gd6GobXgY6L1Yl8gF1qagobbRwBXvbY2-K1Sgm2p1B7RS0fULr48lPhpWHXCzajMPtmRtOcS3ZAKAYfjO7O1cByWcKEQ3ZSjvXBEynt9XuBEuNqJLRD-NJ_kR0m9B1DQKPK1ZLc4Bg4iNi753H3TxU1kesSQaKblbUB3M3WR4aq4uhsa9YTPqbQmIZuaQdEUajZAwi90mLh8YbDAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش بقائی به آلودگی نفتی خلیج فارس: هر طرفی که از کشتیرانی تجاری از طریق تنگه هرمز منتفع می‌شود، هم از نظر حقوقی و هم از نظر اخلاقی موظف است برای جبران و رفع آسیب‌های زیست‌محیطی واردشده به خلیج فارس و دریای عمان اقدام کند
سخنگوی وزارت خارجه:
🔹
چرا رسیدگی به وضعیت زیست‌محیطی تنگه هرمز و آب‌های پیرامون آن باید بخش جدایی‌ناپذیری از هرگونه سازوکار مدیریتی آینده برای این تنگه باشد؟
🔹
در روزهای اخیر، ویدئوهایی از آلودگی نفتی در امتداد سواحل جزیره قشم منتشر شده است. این آلودگی از سمت خلیج فارس به سوی ساحل حرکت کرده و شواهد اولیه حاکی از آن است که یک کشتی فله‌بر خارجی منشأ این آلودگی بوده است. آلودگی در سه نقطه ساحلی و همچنین در بخش‌هایی از سطح دریا مشاهده و ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/680742" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680741">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تاکسی‌ها و مسافران در کرمان سهمیه ویژۀ بنزین ۵ هزار تومانی می‌گیرند  مدیر شرکت پخش فرآورده‌های نفتی کرمان:
🔹
سهمیۀ بنزین ۵ هزارتومانی به تاکسی‌های اینترنتی، ناوگان درون‌شهری و برون‌شهری و مسافران در استان کرمان اختصاص داده می‌شود.  #اخبار_کرمان در فضای مجازی…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/680741" target="_blank">📅 00:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680740">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
بنزین ۸۷ هزار تومانی در کرمان عرضه می‌شود
🔹
معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی به مبلغ هر لیتر ۸۷ هزار و ۲۰۰ تومان از بامداد پنجشنبه (۲۱ مردادماه) در ۲۰۴ جایگاه سوخت استان خبر داد.  #اخبار_کرمان در فضای…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/680740" target="_blank">📅 00:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T94uDfZ0PpcTbNN0tZ0h72ywlfu1FN3i_JQehDnUj0HC4p7A9ZbTDTWfLYnsTyca0oL0VvX8XhWH5B9dbHzGj1hboeG_tua5IvA9BlBclVPdJju961abGG9BTOIQ4reAaMuM3JJaeb7oNBnn4JxcrBWPSE4lbk4Bax32tfCUfFKHtWUpMlaCvup9RTZ-NAw2fxG1m1W-Qc82mZW1YPDHSw9OPpQixC226HZxL9uZa9mIkiQnp-LvqFpc53dAmHL5pB_0LW1MS6jeHp-BAybxsjoSPgxMpSXArMEprrOUEtxpDaHm8QnJe4y_Yls87Q-pk7M32zqg2AjMWBnCF5nnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07115bf6ed.mp4?token=ZTEtYFUWaroMG69WS9g-x-gpOuC0gMbLyNWNeI4JVGbv2oF50JhvudN7PVh5WI1LzkRzFDtU3UZVhYDgMrPATFCccY4wFltgkpbLuVgc-ev4ruQlLtgMl5Ob98Fyk5nSNoLlB-eeC-lHY2ukJrbOobKuljiONCJm1C_0AQLrWx1L4HxFqhmmGXfe_AqQ8u41f1PqRefKi7dkymJw_miIcPO-yGmt3Kq6VZgDUZF3CFqknAhA8TPvpRujPYmPS-xXsN4o8rjdjBGkvhT4K0qHs1N0zo6gvr0U6F-2SsoX7jjM1vMYakan2B5Uz5ODCRifRqNAqwqgpc5tfV6WltJKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07115bf6ed.mp4?token=ZTEtYFUWaroMG69WS9g-x-gpOuC0gMbLyNWNeI4JVGbv2oF50JhvudN7PVh5WI1LzkRzFDtU3UZVhYDgMrPATFCccY4wFltgkpbLuVgc-ev4ruQlLtgMl5Ob98Fyk5nSNoLlB-eeC-lHY2ukJrbOobKuljiONCJm1C_0AQLrWx1L4HxFqhmmGXfe_AqQ8u41f1PqRefKi7dkymJw_miIcPO-yGmt3Kq6VZgDUZF3CFqknAhA8TPvpRujPYmPS-xXsN4o8rjdjBGkvhT4K0qHs1N0zo6gvr0U6F-2SsoX7jjM1vMYakan2B5Uz5ODCRifRqNAqwqgpc5tfV6WltJKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در تگزاس و کشته شدن دو خدمه آن
🔹
منابع خبری از سقوط یک فروند بالگرد نظامی آمریکا در تگزاس و کشته شدن دو تن از خدمه پروازی آن خبر دادند.
🔹
این سانحه هوایی در ایالت تگزاس رخ داده و با آتش‌سوزی وسیعی در محل سقوط همراه بوده است.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/680738" target="_blank">📅 00:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680737">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e488a8c9.mp4?token=d_VVtxe-sNlHXSjszzpbf7eXCZWPpStlKjmz3Nhg4Pa-bu6N__mjX19yR2VuJpiMCJ_mjNFdChvKxmENMU6XIU3rNUDSDBKWODQJwFOOcndOnGF3-3mUHDUkdSvxwsfdc7xbzfi3FpFjhILI9qXYUEyNgzXwtBMF9ZfTVK9YtDV1iUbww2S2mhFqThP1b2VJ18_nTIP_7FdWoGTYR3LzhOIeHFb10R7zbiZ8KVgJCBItIQZ1rdRkGmei_yV0U_9pQFZXj3A5tlaEc2uVAFbgfnrUubpSzgGoTYptgasDP7RDRnAOwxmDUTpSziPfc4JISvoNqhvbP0_em5ltgnWLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e488a8c9.mp4?token=d_VVtxe-sNlHXSjszzpbf7eXCZWPpStlKjmz3Nhg4Pa-bu6N__mjX19yR2VuJpiMCJ_mjNFdChvKxmENMU6XIU3rNUDSDBKWODQJwFOOcndOnGF3-3mUHDUkdSvxwsfdc7xbzfi3FpFjhILI9qXYUEyNgzXwtBMF9ZfTVK9YtDV1iUbww2S2mhFqThP1b2VJ18_nTIP_7FdWoGTYR3LzhOIeHFb10R7zbiZ8KVgJCBItIQZ1rdRkGmei_yV0U_9pQFZXj3A5tlaEc2uVAFbgfnrUubpSzgGoTYptgasDP7RDRnAOwxmDUTpSziPfc4JISvoNqhvbP0_em5ltgnWLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در تگزاس و کشته شدن دو خدمه آن
🔹
منابع خبری از سقوط یک فروند بالگرد نظامی آمریکا در تگزاس و کشته شدن دو تن از خدمه پروازی آن خبر دادند.
🔹
این سانحه هوایی در ایالت تگزاس رخ داده و با آتش‌سوزی وسیعی در محل سقوط همراه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/680737" target="_blank">📅 00:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9ef581a5.mp4?token=EhkVZjSK6izSP8DZGV_X1S-diti8gam7--K6QFfRFBr-vXEKMDFZuU_Q1OmP8UBkYXdKON3JJobBtoYpZI4eTXwS-60dd_8e7f5WNcUUKBYoHGb4kx0vpvFMpJoPjONhZBTb9A-1nGRgdRl4PYrg8wICvyRhuCl8v3llBxpQAsiEo4RermVVgqJEbqMxvrPlzx6wK-mSfok2iKkYFdCfaFKAD1VyrwCKMP5HUeiZN-t9YtQLPhUnzNXYzvO4NxKKN3oUu6X6uURnMGQXrQcvJ8-eRHzdDilq3MiYMtW2ULjoQWGthzUZ8m09_OdcTlqFQDm8XT_N90H-nu4sN05krw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9ef581a5.mp4?token=EhkVZjSK6izSP8DZGV_X1S-diti8gam7--K6QFfRFBr-vXEKMDFZuU_Q1OmP8UBkYXdKON3JJobBtoYpZI4eTXwS-60dd_8e7f5WNcUUKBYoHGb4kx0vpvFMpJoPjONhZBTb9A-1nGRgdRl4PYrg8wICvyRhuCl8v3llBxpQAsiEo4RermVVgqJEbqMxvrPlzx6wK-mSfok2iKkYFdCfaFKAD1VyrwCKMP5HUeiZN-t9YtQLPhUnzNXYzvO4NxKKN3oUu6X6uURnMGQXrQcvJ8-eRHzdDilq3MiYMtW2ULjoQWGthzUZ8m09_OdcTlqFQDm8XT_N90H-nu4sN05krw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشید گرفتگی از نگاه خلبان
🌖
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/680736" target="_blank">📅 00:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHOBuQYDBp4R48E2kVlUCgnL79u8uRuBKBFdT50w6tC45qFemsh3RW2SARmbiT6voaG-c3VC1dVx9UBnMTryqZV3qEsce8o9tZsz1XpMtxlgqpHzf3TazrmMwaXlxdqgKv0nrsWeMXjywJisR-za72GkExdnTfTFnAKWCp2EY7rMwfLcd3auUMo_CWRdIdB_twIGDdEl5FN-oBNKKL6Fp9D6Qqew8RyR90_FxmcPfUgNYqfC9zrk1FYlJJKxjMNfwZFQ0mDXb8LHoxA_vvcJpcz56ZUm2sdUG57umoZCatVNas9PuL4WlQ-utb3ixfV4WnfgREDbSXqXqvPkg5QuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/680734" target="_blank">📅 00:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680732">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec71b08d89.mp4?token=T3gkt9GoRbnxXKlPuM0d7jdwmOh6p2VNKSZsDxWnsCmfys-2wkS7F1H6iewK58NhTC5aXYV2Q3zw_GIDx0Sh0Y_F_eRf4QPq2k1xduRXsJjgvQKuY4XoJaNeEYjmPgGnEp_iI8PYdP095B_-fxPx_vV6EMlzj_dCvMEBckinLLLU5WIwItV-NdOmsuFthDGUf3gv7ANj6umUaGlAoKIVrC-lLeJvNd8vdqFlXELps-TLMR1ScUCSmFMLQ6DOwRgGW1cw67vQo3LrsIUHMUvgjDsiv0YiaVr05fEPhc8ioyE57EMox1ARbbrYoyW8bwACsQ69YvjV16MlGc1PjRLRoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec71b08d89.mp4?token=T3gkt9GoRbnxXKlPuM0d7jdwmOh6p2VNKSZsDxWnsCmfys-2wkS7F1H6iewK58NhTC5aXYV2Q3zw_GIDx0Sh0Y_F_eRf4QPq2k1xduRXsJjgvQKuY4XoJaNeEYjmPgGnEp_iI8PYdP095B_-fxPx_vV6EMlzj_dCvMEBckinLLLU5WIwItV-NdOmsuFthDGUf3gv7ANj6umUaGlAoKIVrC-lLeJvNd8vdqFlXELps-TLMR1ScUCSmFMLQ6DOwRgGW1cw67vQo3LrsIUHMUvgjDsiv0YiaVr05fEPhc8ioyE57EMox1ARbbrYoyW8bwACsQ69YvjV16MlGc1PjRLRoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمان و عربستان سعودی «کریدور امن سرزمین سبز» را راه‌اندازی کردند
🔹
این مسیر، بندر صحار را از طریق بزرگراه ربع الخالی (بخش عربستانی تقریباً ۵۶۴ کیلومتر، با هزینه تقریبی ۵۳۳ میلیون دلار برای ساخت) به بندر خشک اسپارک متصل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/680732" target="_blank">📅 23:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
رئیس‌جمهور لهستان با انتشار ویدئویی از جنگنده ها و با لحنی تهدیدآمیز: صبح بخیر ایران عزیز!
👇
khabarfoori.com/fa/tiny/news-3237227
🔹
جزئیات مراسم تشییع «ایرج»
👇
khabarfoori.com/fa/tiny/news-3237275
🔹
«زن مرموز» در اتاق بیضی | ترامپ این زن را استخدام کرده تا در جلسات بیدارش کند!
👇
khabarfoori.com/fa/tiny/news-3237260
🔹
اوکراین پدافندهای اطراف کاخ پوتین را زد | اقامتگاه بدون دفاع ماند
👇
khabarfoori.com/fa/tiny/news-3237246
🔹
ورود هندوانه و خربزه ایران به عراق ممنوع شد
👇
khabarfoori.com/fa/tiny/news-3237310
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680731" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: کشورهای خلیج‌فارس مدیریت ایران بر تنگه هرمز را به جنگ ترجیح می‌دهند
وال‌استریت ژورنال:
🔹
کشورهای حاشیه خلیج فارس در حال پذیرش یک وضعیت عادی جدید هستند که در آن ایران کنترل تنگه هرمز را در دست دارد. مقامات خلیج فارس نگران این هستند که جایگزین این وضعیت، یعنی بازگشت به جنگ، بسیار بدتر باشد.
🔹
آنها توافق در دست بررسی برای بازگشایی تنگه را که کنترل ایران بر کشتی‌های ورودی را رسمی می‌کند، دوست ندارند، اما آن را به اقدام نظامی بیشتر بین آمریکا و ایران که زیرساخت‌های انرژی کشورهای عربی را به خطر می‌اندازد، ترجیح می‌دهند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/680730" target="_blank">📅 23:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680729">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucz1sWEw_cyJNfKFlRw0o_G92zKbtpvcsYqvgo2nUv6KQgRMXtiXvAZsOOPw1KbCtz7_av4rNotd5rTKX3Ff9rm7i9iewRRLEN15wgdx9XUxJdmeDVrz27hDkX5eqfoYeH5oAmJeDLvq1ToY7SA2S8ih-k1J7FO5ZYKpJ4v5XlX_AWsRNcbDy8EThcUXhkkmC1_SNPy-gqeVBVIIye-r1tsADhpFajVuMi0Ofsml8Je4iIzeRwlK5z2xiJ5buxT0ePnqulH8P73yShqetmmgw1Tz7jb6JKlMdqbycKgyFAw6EMuN6XUloIinCDjmI6JwXaRl9bpk2pykUXQVyBtBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده ترور فرمانده ارشد اطلاعاتی لیبی | فوزی المنصوری که بود؟
🔹
در رویدادی که بار دیگر زنگ خطر را برای ثبات شکننده در لیبی به صدا درآورد، شامگاه دوشنبه «فوزی المنصوری»، از فرماندهان ارشد و رئیس اطلاعات نظامی نیروهای مستقر در شرق لیبی، در جریان یک انفجار هدفمند در شهر بنغازی کشته شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3237239</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/680729" target="_blank">📅 23:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680728">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988dadeacf.mp4?token=Vi_x4aKs5WmJ0Rztp_xvXUe72HvM9WiStGmGs_rPHNJKUt4X8p9Kgxoby69W5oLjeaczn8uv27L9kGAULtigrWAfYRuMj2pmP7UiDpGj-CAybr0-7LBS7ZosFm6CXqD2eWuspZxY9W110T1Q4DVeK32P5hqQqlzIMvnl6-2VLwUuwo3IKRM_55Ik3ErdXuB0DsgSLlIr40GxTv1rzn4naQBXxcsvb2mg13ykgjGwzAvNS8yxfQ0y2RIlHrVUJ7pzAxNtg6Kx6tIdYa0NqvuRStWGP-JGnr1L8rJig7tFSCYESdOaYUFsxsT_VrhtRW4-VGwOyfI14zohlVRIyz2B2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988dadeacf.mp4?token=Vi_x4aKs5WmJ0Rztp_xvXUe72HvM9WiStGmGs_rPHNJKUt4X8p9Kgxoby69W5oLjeaczn8uv27L9kGAULtigrWAfYRuMj2pmP7UiDpGj-CAybr0-7LBS7ZosFm6CXqD2eWuspZxY9W110T1Q4DVeK32P5hqQqlzIMvnl6-2VLwUuwo3IKRM_55Ik3ErdXuB0DsgSLlIr40GxTv1rzn4naQBXxcsvb2mg13ykgjGwzAvNS8yxfQ0y2RIlHrVUJ7pzAxNtg6Kx6tIdYa0NqvuRStWGP-JGnr1L8rJig7tFSCYESdOaYUFsxsT_VrhtRW4-VGwOyfI14zohlVRIyz2B2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف ما یک‌کلام؛ انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/680728" target="_blank">📅 23:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1f17b87b.mp4?token=pYu-1wMKHP0wv51T6kJ5GHzleVrhUd7uK87MBTZqkjo8wLUgz9xm6toRfJO6NA13QzbOXrPBucFXXS02Et81D_EWd96MC9FYvGQvLlZQcZ2nOq5KUP4cD3yIJbw0PK6VApCDxlan4iOkil61wyLbja8S359W0uPDEMifAH4rncAVhQ-yJdr7Ssx23f84shvGkSSvKa3-bkMNodtTNGOrrWwIKeGfiOjV7b1cQaND5mDX_cBbvocPdR19l9S5WHBPOtCdIFypmQKac6lDuNa-oXaxv3fkSsJif2TH0gfi6x0IRQIbuQGwtvgBN3xfEfXzDFz0TKkUt_nWBut-laZgYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1f17b87b.mp4?token=pYu-1wMKHP0wv51T6kJ5GHzleVrhUd7uK87MBTZqkjo8wLUgz9xm6toRfJO6NA13QzbOXrPBucFXXS02Et81D_EWd96MC9FYvGQvLlZQcZ2nOq5KUP4cD3yIJbw0PK6VApCDxlan4iOkil61wyLbja8S359W0uPDEMifAH4rncAVhQ-yJdr7Ssx23f84shvGkSSvKa3-bkMNodtTNGOrrWwIKeGfiOjV7b1cQaND5mDX_cBbvocPdR19l9S5WHBPOtCdIFypmQKac6lDuNa-oXaxv3fkSsJif2TH0gfi6x0IRQIbuQGwtvgBN3xfEfXzDFz0TKkUt_nWBut-laZgYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش میوه خشک کردن به روش سنتی
🔹
برای تهیه میوه خشک باکیفیت، انتخاب میوه‌های تازه و سالم اهمیت زیادی دارد. میوه‌های مانده یا دارای زدگی، پس از خشک شدن کیفیت مطلوبی نخواهند داشت و ممکن است تغییر رنگ یا کپک‌زدگی ایجاد کنند.
🔹
ضخامت برش‌ها، نوع میوه و میزان آب میان‌بافتی آن، در زمان و کیفیت خشک شدن تأثیرگذار است. هر میوه شرایط خاص خود را دارد و رعایت این نکات باعث می‌شود محصول نهایی ظاهر و طعم بهتری داشته باشد.
🔹
در این روش، بدون افزودن شهد یا شکر اضافی، طعم طبیعی میوه حفظ می‌شود و یک خوراکی سالم و خوش‌طعم به دست می‌آید.
🔹
این یک نمونه از مهارت‌هایی است که می‌تواند از یک کار ساده خانگی، به یک مسیر جدید برای یادگیری و درآمدزایی تبدیل شود.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/680727" target="_blank">📅 23:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680726">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=n1I6PWW1LbI5IGzmZHVxU6TfljLJCB1ljcA06a20HbUtmuTC12ryx6nQU_15gN7PfCv5DTuTmfhd0yQCyME0LzHhawgxFpFj87mCLpXS1VAk3uhgbqSRWiYiakBQL0dIiBwD23DaG0OfQbzXIGnXBmws54BXoLB8oRm_Z1b8MEaObaP-ztAkSiMfOMDzxauARSCjXFPecSTHcYUDe6j5pOJIZoJo9HyGkErNnoNu036_WPRnTfO6wEThjL8TjCkmYSFm2B-mLeiT0wIrpK6khQOuDU6RvQs68GX82XuMV_CZuToEYamLWnFRexIZnkAl_LHb_O7M4ZbZqCUDtAGGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=n1I6PWW1LbI5IGzmZHVxU6TfljLJCB1ljcA06a20HbUtmuTC12ryx6nQU_15gN7PfCv5DTuTmfhd0yQCyME0LzHhawgxFpFj87mCLpXS1VAk3uhgbqSRWiYiakBQL0dIiBwD23DaG0OfQbzXIGnXBmws54BXoLB8oRm_Z1b8MEaObaP-ztAkSiMfOMDzxauARSCjXFPecSTHcYUDe6j5pOJIZoJo9HyGkErNnoNu036_WPRnTfO6wEThjL8TjCkmYSFm2B-mLeiT0wIrpK6khQOuDU6RvQs68GX82XuMV_CZuToEYamLWnFRexIZnkAl_LHb_O7M4ZbZqCUDtAGGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از حضور رهبر شهید در حرم امام رضا(ع) در سال ۱۳۷۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/680726" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680725">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون امنیت ملی: ادعای خروج ۸ میلیون بشکه نفت از خلیج فارس توسط آمریکا کذب است
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
ادعای خروج نفت از خلیج فارس توسط آمریکا کذب است و در راستای جنگ روانی آمریکا مطرح شده، هیچ خروج نفتی با اقدام یا اجازه آمریکا صورت نگرفته است.
🔹
تنگه هرمز در اختیار نیروهای مسلح جمهوری اسلامی ایران است و هرگونه عبور و مرور از این آبراه فقط با مجوز ایران انجام می‌شود و هیچ کشوری حق دخالت در آن را ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/680725" target="_blank">📅 23:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUPR_hoE5mTAsB2knycV7qLqIcfig6hjfbqt7a8gT0TQ2qQJaAKJIeFa-mJbYagkcuklTLIcs3qSPnWE7Z4nA3gax9Ydp7-dJeZeVkZGc0qpDdUjgR-vbrwWeeANQAfNz31UJXq4lGSNWkCtcZYHh6z8ueamx0DUHqS3PbO4zptdzPlUSpArQ8fqJgS55yIgR1SogLwtJcabMznLbNE9RZKYa-umS3AwwB-XxehHaUhuUFJPfWKFPDV4oupci801BO2JADYot_6vVCEFsdOMsiG-lC0HPNhPd2wX9U8BAxg9CEiLlcmSNm9rVt-bCo74DVJtg6N69Z45divLwJEmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f041e741.mp4?token=O2gQArPgbQez2sgzCzLgtxYcAAqJvhrgo8OQKVkmFH0EwZiw35GgLlrnqMP-mllIUTeWSyuDmlNhID8LrNcqBRT5mJGaN-IzC47pLzNEe1jWiX8_EKax_DihXYk_EJSjw6j188j_hf_rrwlLis5dcw49m-FRwUmnt5sHVm7Tm0ND2cA5DWf__Oo-JWiUyIJ_yb96CMYMGwf5PP5S6lV76ZepO-PYyM0jn339unEFKGNRfe5__8ZoXLJoJXH0ZTFLkv9lpZnwi1mnoj35e7LjP6ZFOyxO_X2DfPMq17x-xnoD0m6NoTmD1iancv6wJrJ5CcUfTbH2cTqP8SUFinzLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f041e741.mp4?token=O2gQArPgbQez2sgzCzLgtxYcAAqJvhrgo8OQKVkmFH0EwZiw35GgLlrnqMP-mllIUTeWSyuDmlNhID8LrNcqBRT5mJGaN-IzC47pLzNEe1jWiX8_EKax_DihXYk_EJSjw6j188j_hf_rrwlLis5dcw49m-FRwUmnt5sHVm7Tm0ND2cA5DWf__Oo-JWiUyIJ_yb96CMYMGwf5PP5S6lV76ZepO-PYyM0jn339unEFKGNRfe5__8ZoXLJoJXH0ZTFLkv9lpZnwi1mnoj35e7LjP6ZFOyxO_X2DfPMq17x-xnoD0m6NoTmD1iancv6wJrJ5CcUfTbH2cTqP8SUFinzLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشیدگرفتگی امشب در اسپانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/680723" target="_blank">📅 23:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بازار بورس ۶۰ درصد کوچکتر شد
🔹
ارزش دلاری بورس تهران از بیش از ۲۰۰ میلیارد دلار در ابتدای ۱۴۰۰ به کمتر از ۸۰ میلیارد دلار رسیده است.
🔹
سطحی که در زمره پایین‌ترین سطوح تاریخی بازار قرار دارد. بر همین اساس، کاهش ریسک‌های سیاسی می‌تواند جرقه‌ای برای رشد فراگیر بورس باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/680722" target="_blank">📅 23:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680720">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qho1zh9LUvJobzewBuvbJAMrpJ_HBnEt_oZwC2V6nQYUQhGwVwmA4F4wwxFv05eYDDCrZMY-E_KWT3FoBaDarpNgFT6xwGRnX218_1ZqHa81SbLKlbla0-f6NvzoynEkDGjiNF7JjnAZle9FXneNvRyKmawHywxT1clXCdEK_hBo7hpsXE9qVy-XMeyQBemaI-XEopu-pzWytCkEaXmNWCHv81tppuHwZfvndXSI_PWUBMMqCZYWWyN-Cv1RnYygLfMS5p1TlZLyA4eVKPU6qXelEUwA1PsnzX6PSZ4rVkCvCPKzT_P0Sr6vKjZiGsCZzSOyTUSWRWOQN5kpyJ9Tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/680720" target="_blank">📅 23:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680719">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skTeP4FE05Mzu8uKfCoC2xUh4aijdMgK2S6NzU3QgwQQ_Gr6Z8rVjM277P8svaDxnI50IWK_Pha7Ah0go_shnNLhpXKmdUZK2kXTNCYcHrge5dXHDYP096RPFFcy49QfsPloltLw3l0pHwqeGN1CSI6ID7FUVzvdmWM0vchKDTJrkW0lBfP-vq_DedAsF2u33jwhKs5YCEQ8yEh9hAG-Ofhp3N0qrerszXGbWeMBq-GMYUTGJaMcH4C0qgTyYXwTzxzMw9Y6t0WxNbikvKz6r8QyJIVUYDReRyC-kpNdzl0ipFbYBfU1rdGtsDgCrZxpDCdvwPCG8rzYu5FCEwTk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه کسب‌وکاری در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
عکس کسب‌وکارتان را برای ما ارسال کنید و در چند خط، تجربه شروع و نتیجه‌اش را برایمان بنویسید.
🔸
روایت شما می‌تواند چراغ راه کسانی باشد که می‌خواهند از صفر شروع کنند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680719" target="_blank">📅 23:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOPu8dmF1Cg__VRmsugxOJumbTEkK27GGIp51lFRwEm2aRKDDQlXQ4YiZwtjawWGZsTIuzNPamGYK40vgLMrlV4-NvNrIS3CIXpm9k4aNyIDv8vw9PcirNK1z4TFQw4h0eEvASEcel5jdm6s7IWkYy0_0_4AWHyWV_JPgErBOr1x5T9OnDcVln-0AQT2e3gvmz4oOLFKHb3YGd5UMba5_ZPmxw5jOqRnDh1fUDeTf6YfCcpNGGxgcadvSvuRgY-CUgtVt0GJQPQil8p6l8uGtDPlV2BFc2SkgY3CY6MI7qIgA_7KaHGd87iTQMw_34v8np4vnqNzCBSF6Qprju7TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتلانتیک: ترامپ درباره ایران وارد فاز «صبر و انتظار» شد
ادعای آتلانتیک:
🔹
دونالد ترامپ در قبال ایران به‌تدریج رویکرد «صبر و انتظار» را در پیش گرفته است. کاخ سفید اکنون بیش از گذشته روی تحریم‌های اقتصادی و محاصره دریایی حساب باز کرده تا تهران را به مذاکره وادار کند.
🔹
حملات نظامی اخیر، برخلاف انتظار، نتوانسته به درگیری پایان دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/680717" target="_blank">📅 23:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چه کسی تصمیم گرفت ما خاورمیانه باشیم
🔹
شاید تا به حال فکر نکرده باشید که چرا منطقه غرب آسیا را خاورمیانه می‌گویند.
دسیسه‌ای عجیب پشت این‌نام‌گذاری است.
و باز هم پای انگلیس در میان است.
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680716" target="_blank">📅 23:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680714">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
گاردین: با آتش‌بس هم میل ایران برای کشتن ترامپ کم نمی‌شود
ادعای گاردین:
🔹
تغییر پرواز مخفیانه ترامپ نشان دهنده شدت تهدید ترور از سوی ایران است. اقدامات غیرمعمول برای محافظت از رئیس جمهور در حالی که به طور بالقوه دیگران را در معرض خطر قرار می‌دهد، «ظاهر خوبی ندارد» و خطر «ضعیف» جلوه دادن او را به همراه دارد.
🔹
حتی یک آتش‌بس یا توافق صلح که به جنگ پایان دهد، «میل آنها برای کشتن ترامپ را از بین نمی‌برد»./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/680714" target="_blank">📅 22:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680712">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ای قوم حق‌شناس
حی علی القصاص
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/680712" target="_blank">📅 22:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680711">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
موتورسیکلت‌های ایران چینی شد
اصغر فرضی‌پور، رئیس اتحادیه موتورسیکلت فروشان در
#گفتگو
با خبرفوری:
🔹
بیش از ۹۰ درصد موتورسیکلت‌های موجود در بازار از چین وارد می‌شوند و با نامشخص شدن مبادی ورود کالا روند تأمین قطعات با دشواری بیشتری همراه شده و این عامل نیز به افزایش قیمت دامن زده است.
🔹
تولیدکنندگان داخلی با هزاران مانع اداری و تأمین مواد اولیه مواجه هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/680711" target="_blank">📅 22:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680710">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6dvtRfvXogB501PGMRYijOV0nUalce3ck9kTUXRqdMjZO6Y8TxOWDgzFk7ohcXyCLR-xQsgxpGTIPfbOkQXQEfv4UZiTnw9urIOxo-pTkKzDcwosm_aOgZgQTEr3e0fTYhMVILl7FCcR8Nxkwo1pPs58Xl7X3rbMG119dG-wNyKTRKfJnriVVjYJQU_OJPQYOfXHu-5FRHD1GaBtq2Ov5EegUz0y4hbVXCz1gnUsIXkcoSM1eDsnw__j2z1HNFbAUDJqbgwD91hkL9FsV7bqB_ztmkjjrgP-QX7DdrjvSbMvs0ajcsvp37aL8yDke9iDTI8UFZgZQ4BwW_iTaSitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز تا پذیرش شروط ایران از طرف آمریکایی همچنان بسته است
متن کامل پیام نهاد مدیریت آبراه خلیج‌فارس:
🔹
ادعاها و توییت‌های پیاپی مسئولان آمریکایی درباره رفع انسداد تنگه هرمز، واقعیت را تغییر نمی‌دهد؛ تنگه هرمز همچنان مسدود است و تا پذیرش شروط ایران بازگشایی نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/680710" target="_blank">📅 22:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680709">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f05b26e0.mp4?token=AVbw7HfE3wPaqJjzWEJdwZOzPjskVKzXrHqSjxnRqXmNdDYfIev5m-0t2bfsNl5J21HQ6kguC2kyVpa-O4fafKVFjFQlSDEQ4L1Rx6166CIaLLmFYugfTnDJTIxVZrnQtxthV8O7AXWcHyvSCG27FozR6qWCNBYL87ljlt3LD_cHDcVziL9RO5IWrS0cFkEc8pAZD1q0AnJzIejCCnDNPdB4lOIbiMZP7ZXKlIs_B0kScWLX8x3aCqRVcOpwhyWpkeRBVSlmm6X1E-Y0ogzZFapTjkHpXJf1LZ_143Ei-ddLSHczrmThwsQA-Fa81ePvTQlgqcv4N9pFmlDFSaMQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f05b26e0.mp4?token=AVbw7HfE3wPaqJjzWEJdwZOzPjskVKzXrHqSjxnRqXmNdDYfIev5m-0t2bfsNl5J21HQ6kguC2kyVpa-O4fafKVFjFQlSDEQ4L1Rx6166CIaLLmFYugfTnDJTIxVZrnQtxthV8O7AXWcHyvSCG27FozR6qWCNBYL87ljlt3LD_cHDcVziL9RO5IWrS0cFkEc8pAZD1q0AnJzIejCCnDNPdB4lOIbiMZP7ZXKlIs_B0kScWLX8x3aCqRVcOpwhyWpkeRBVSlmm6X1E-Y0ogzZFapTjkHpXJf1LZ_143Ei-ddLSHczrmThwsQA-Fa81ePvTQlgqcv4N9pFmlDFSaMQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امضای قانون سقط تا ماه نهم؛ جشن «حق انتخاب» در حالی برگزار شد که صدای نوزاد شنیده نمی شود
🔹
لحظه امضای قانون سقط جنین حتی تا ۹ ماهگی در ایالت ماساچوست و تشویق فمینیسم ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/680709" target="_blank">📅 22:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680708">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDGPCrLngFU8NS_Ex9DqBQpngK_upIt4a4aSILEiL8lFxAsSrgrkhtDxo2LbPdBfRDT5YFmQ5Q8E-pXN0FrIneLZOrMfgzypl4CBpvPwK2aYZPjhky86Z5nL_FDEgWGenVwKns2DaAYFpKK1Rgsi3ZgHESxBMjUG0cWZbgc8C1_RQRSiBoiIw3kEqez2sd6_DXkIp-HW-yAfC6OilQh_paIrYtXKxKjG8btXreIHoLG5h168ZTCIIVmUtlQR9GdCZPq20hIZXT9kOdNy-Z4LE1l4-e1zXBw4piJ94cNe3OJ4UpgngYEVqMEBQZhoXILUbFrvq1ZW2taseL-rorxb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای برخی منابع خبری: فرود یک هواپیمای دولتی امارات در ایران طی دو روز متوالی
🔹
یک فروند هواپیمای دولتی تشریفاتی امارات متحده عربی، از نوع بوئینگ ۷۳۷-۷۰۰ BBJ که توسط شرکت Royal Jet operated می‌شود، طی دو روز متوالی، برای مدت کوتاهی به ایران سفر کرده است.
🔹
این هواپیما در ۱۱ اوت از ابوظبی به سمت منطقه تهران پرواز کرد و حدود یک ساعت در آنجا ماند و سپس ایران را ترک کرد.
🔹
همین هواپیما در ۱۲ اوت بار دیگر وارد ایران شد و این بار در فرودگاه پیام کرج، در حدود ۴۰ کیلومتری غرب تهران، فرود آمد. هواپیما حدود ۳۰ دقیقه در فرودگاه ماند و سپس ایران را ترک کرد. /انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680708" target="_blank">📅 22:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680706">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ماجرای تغییر مدیریت تامین اجتماعی در روز تعطیل چه بود؟
ایلنا:
🔹
در اقدامی ناگهانی، احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، مصطفی سالاری را از مدیریت سازمان تأمین اجتماعی کنار گذاشت و غلامحسین محمدی، رئیس سازمان آموزش فنی‌وحرفه‌ای کشور، را جایگزین او کرد.
🔹
این جابه‌جایی در روز رحلت پیامبر اکرم (ص)، بدون اطلاع‌رسانی قبلی و در شرایطی انجام شد که هنوز توضیح رسمی و روشنی درباره دلایل برکناری مدیرعامل، ضرورت این تغییر و معیار انتخاب جانشین او منتشر نشده است.
🔹
گزارش‌های اولیه همچنین حاکی از آن است که سالاری نیز پیشاپیش در جریان این تصمیم نبوده؛ موضوعی که وزارت تعاون، کار و رفاه اجتماعی باید درباره آن شفاف‌سازی کند.
🔹
دولت باید درباره علت و فرایند این تغییر، رعایت تشریفات قانونی، معیار انتخاب مدیر جدید و برنامه او برای مواجهه با ناترازی مالی، پرداخت مستمری‌ها، بدهی‌های درمانی و مطالبات سازمان از دولت، توضیحی روشن و مسئولانه ارائه کنند.
جامعه تأمین اجتماعی حق دارد بداند چرا مدیریت مهم‌ترین نهاد بیمه‌ای کشور، آن‌هم در یکی از حساس‌ترین مقاطع مالی و اجتماعی، به این شکل تغییر کرده است.
📲
🇮🇷
✊
@AkhbareFori
| Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/680706" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680705">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a80aca92.mp4?token=WaDXrb8lrw9-a78VQGOqtRyguPFAvKmyywFQ4EA162lwQKHs_NkEfo-fO8e0jDw7_fP567NvoQOEVekjgtznmv4NzHTU5nR2O4DJAUW2GjPexT6qfjUbXb_49pYfy1zbVpnBQCKivtn1fPY4u20h_ifKQ7P9TOjG3aBuwa96ZWhJqXeCuPkYD2HYdrNX4A_DTfKB1nezHHHMbft0Dx6p5MvxMqQ0vaccBojCd7YGQfI2NxP7o_wBtgiDzqokBGGc2jxAOvdSPmpbWW0oDqzOgeUmfRtertnrmHXUTmmHFmcguwtAofgvJdkSGhTVCFfaj00ul99Mp2iT9JkGr73BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a80aca92.mp4?token=WaDXrb8lrw9-a78VQGOqtRyguPFAvKmyywFQ4EA162lwQKHs_NkEfo-fO8e0jDw7_fP567NvoQOEVekjgtznmv4NzHTU5nR2O4DJAUW2GjPexT6qfjUbXb_49pYfy1zbVpnBQCKivtn1fPY4u20h_ifKQ7P9TOjG3aBuwa96ZWhJqXeCuPkYD2HYdrNX4A_DTfKB1nezHHHMbft0Dx6p5MvxMqQ0vaccBojCd7YGQfI2NxP7o_wBtgiDzqokBGGc2jxAOvdSPmpbWW0oDqzOgeUmfRtertnrmHXUTmmHFmcguwtAofgvJdkSGhTVCFfaj00ul99Mp2iT9JkGr73BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
غریبانه آمد، غریبانه زیست و غریبانه به شهادت رسید؛ اما قرن‌هاست که میلیون‌ها دل، در پناه گنبد طلایی‌اش آرام می‌گیرند
🔹
سالروز شهادت امام رضا (ع)، امام مهربانی‌ها و پناه دل‌های بی‌قرار، تسلیت باد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/680705" target="_blank">📅 22:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ ممکن است بخواهد خاورمیانه را رها کند، اما خاورمیانه او را رها نخواهد کرد. ترامپ در آخر هفته گفت راهبرد جدیدش در قبال ایران این است که «کم‌سروصدا عمل کند»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/680703" target="_blank">📅 22:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f490de586.mp4?token=o5U_lCYVl45E_g4izwkRFEnUi1417Lc556zWthJtIjmrF2LgpHoMW2P_5ET1sX_o-fmqnYgjtZylc9crYMvgCCcwL8AmXRCDX8ZY6ECHHz9gmsp6sXgH1RAsqx5_CKDzcn5bxM_mkIYqFCU-Nj1YS4IB-hfPK818pAd_RdjUEV-ZjfyaNelOnHIUgQYCPvvvLCxXbtiryo97XJD1QT9zah9SVhqWCErQV8D36iMgs8AZJV_i8l3tHp-sfTlu9bOxzN38FrKLNzAPIjS1DCLDuZBQ0GU5S0GO9U-EpkziNa_i4P-5ih2_Me05zNJ6NPr4cxOHKkaFgkQ7s7mzYHMxFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f490de586.mp4?token=o5U_lCYVl45E_g4izwkRFEnUi1417Lc556zWthJtIjmrF2LgpHoMW2P_5ET1sX_o-fmqnYgjtZylc9crYMvgCCcwL8AmXRCDX8ZY6ECHHz9gmsp6sXgH1RAsqx5_CKDzcn5bxM_mkIYqFCU-Nj1YS4IB-hfPK818pAd_RdjUEV-ZjfyaNelOnHIUgQYCPvvvLCxXbtiryo97XJD1QT9zah9SVhqWCErQV8D36iMgs8AZJV_i8l3tHp-sfTlu9bOxzN38FrKLNzAPIjS1DCLDuZBQ0GU5S0GO9U-EpkziNa_i4P-5ih2_Me05zNJ6NPr4cxOHKkaFgkQ7s7mzYHMxFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
امام رضا(علیه السلام) ميفرمايند: "هرزائري كه مرادرغربت زيارت كند، در سه موقف هولناك به يادش هستم:
اول درهنگام سخت مرگ وجان دادن
دوم در زمان سنجش اعمال
سوم در لحظه ي عبور از  پل صراط."
@Heyate_gharar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/680702" target="_blank">📅 22:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ایران هشتم جهان در مالکیت رمزارز؛ ۱۵ میلیون ایرانی رمزارز دارند
🔹
بر اساس گزارش TechRasa Insight، حدود ۱۵ میلیون ایرانی در سال ۱۴۰۳ مالک رمزارز بوده‌اند. این داده بیانگر این است که  ۱۶.۷ درصد جمعیت کشور، رمزارز دارند.
🔹
این نرخ حدود ۲.۴ برابر میانگین جهانی است و ایران را در میان ۳۱ کشور بررسی‌شده، در رتبه هشتم جهان قرار داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680701" target="_blank">📅 22:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
گاردین: چند ملوان ناو آبراهام لینکلن قصد پریدن به دریا را داشتند
🔹
خانواده‌های نظامیان و اعضای کنگره در مورد تشدید بحران سلامت روان در ناو هواپیمابر آبراهام لینکلن هشدار می‌دهند، چرا که ۵۰۰۰ ملوان و تفنگدار دریایی این ناو، استقرار بی‌سابقه‌ای را در دریا که به جنگ با ایران مرتبط است، تجربه می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/680700" target="_blank">📅 22:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907149645f.mp4?token=reiQgtbaJz_pocSYU-Cg5FRQMxSZstC677YcXNUUfRGBUUresNEKUzP0HJkZUfWX1FkdICHTosgYKbUeWk8Sr6cbwHZqZ17jjpe8O6Igbb8gtqD1Gh4L52wnaZ7j058RyJDnGidKzk0yBLEskCkt7gXiVygljqaXG77JFkQNMRGRZWjwMCLfepH-3FixdY2JIP96hkR_yrD2mUy7-FOUXRQfCVztExreTqufrHepCKqxJRr4Jeks30Vw67_9rpMRCMatfZn5kukLMjgib9eomiNWnvZRgFlovbYSjWrMd3hS0o0SxcXEI4qS7XvXAyNXckLtrZgbgBgQ3ed4Aiwk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907149645f.mp4?token=reiQgtbaJz_pocSYU-Cg5FRQMxSZstC677YcXNUUfRGBUUresNEKUzP0HJkZUfWX1FkdICHTosgYKbUeWk8Sr6cbwHZqZ17jjpe8O6Igbb8gtqD1Gh4L52wnaZ7j058RyJDnGidKzk0yBLEskCkt7gXiVygljqaXG77JFkQNMRGRZWjwMCLfepH-3FixdY2JIP96hkR_yrD2mUy7-FOUXRQfCVztExreTqufrHepCKqxJRr4Jeks30Vw67_9rpMRCMatfZn5kukLMjgib9eomiNWnvZRgFlovbYSjWrMd3hS0o0SxcXEI4qS7XvXAyNXckLtrZgbgBgQ3ed4Aiwk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وندی شرمن: ترامپ برای بازگشایی تنگه هرمز ناگزیر از دادن امتیاز به ایران و لغو تحریم‌هاست
🔹
مذاکره‌کننده پیشین آمریکا در مذاکرات هسته‌ای: بعید است فشار اقتصادیِ بیشتر از سوی رئیس‌جمهور آمریکا باعث تسلیم ایران شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/680699" target="_blank">📅 22:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHqxMw8jr9pz07TaNhDt5qEUZSBoce76lKF5A0AokLQ9nmkZS3mgOdw479viUG-b_QIow0pNi42Sgn2jIJZwd9iLNH4vJ-OnwlaCd008sN5f3JG2sQ-mQhK8TpQaWwykhdzYjcUy1w4MOc-0QvsixfWjXl5mZ1JhL3dH-szSGTrAsuNrwSSr4YrO0zQXh7wkDZb-4rNpma3TwWxVbjYQk_UCmUBDZG4gylfoSjxXrzC5zhurp-IpzosQmZQXg5QjLVdUp9jy8I9Ll7L2ILOomHsHBw-F2siF7lKQGpkjzR3DeW2a6RnWKKOyecJY7rk7I5x19xN-qEh3srJiSoUItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEd1OZ1Mu74sQE5lMU_H5S1S4UEzQbZwSHoODT5L_vXnKjFNgmK-3BgSy_jry4aOwbEyc6GLMKk5b7GuXyRU367qsKcOVqiU0b4lzyK-iwZyLfhf5Lcs7Guowms0n936hnCAsORMKZQXL_ijN2UiP_kCROEpeDIJzxFAD24awgXRYiRZIryLRRp3_4DHkhWF8clG5pGJ9avU6xicQfu6Nl9GC3EGdN-UZQumKQ8cEwu_hhwImEttmQIbT3bzhn7EN_XnnhHbvbmnx7ijRPKq6M7b4aNLWYE0H51zcEySoiXQl9NhNeElnrXxuVrH7RYGVQoRYrUi6hoaNX-GzP8brA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل، آسمان ایسلند را تاریک کرد
🔹
سازمان رادیو و تلویزیون ملی ایسلند (RUV) تصاویر دیدنی و نادری از وقوع پدیده خورشیدگرفتگی کامل در آسمان این کشور منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/680697" target="_blank">📅 21:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4372b072f8.mp4?token=cN3DaMXdj4LNU21MgvXSdMfjO3PbY5fKMOjqEA6yZ9p0S7v79g_mDETdff1zjee5mKUuJmDLQHuxbTTlNPF-lum0k7aqiCGtemnvZbLrWvA1Jmdyt6ApJUT8c0FSk2sZTHoS7CFcqMb95CopPPdiBtINxnMcGSKuDEZ_Yts95U0umNGrCbkxSGRPboREefPsxDOzoB3621QxrGYIfY7FdaB-_rCAmlT7UNHwNqLMEiWi5tAkJFbuGeApyZxkpuFw567BKSm-7ezZJiIYoWaHBpvZhpzgfeVuZ1JBX6bNhGVn6_WDLfUzQTA4bUMT9O74tjvMFQBB7LjN2oSMdxCd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4372b072f8.mp4?token=cN3DaMXdj4LNU21MgvXSdMfjO3PbY5fKMOjqEA6yZ9p0S7v79g_mDETdff1zjee5mKUuJmDLQHuxbTTlNPF-lum0k7aqiCGtemnvZbLrWvA1Jmdyt6ApJUT8c0FSk2sZTHoS7CFcqMb95CopPPdiBtINxnMcGSKuDEZ_Yts95U0umNGrCbkxSGRPboREefPsxDOzoB3621QxrGYIfY7FdaB-_rCAmlT7UNHwNqLMEiWi5tAkJFbuGeApyZxkpuFw567BKSm-7ezZJiIYoWaHBpvZhpzgfeVuZ1JBX6bNhGVn6_WDLfUzQTA4bUMT9O74tjvMFQBB7LjN2oSMdxCd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنگره آمریکا: ترامپ بیش از حد بی‌کفایت است
جیک اوچینکلاس، نماینده کنگره آمریکا در شبکه فاکس نیوز:
🔹
می‌دانم که دونالد ترامپ برنامه شما را تماشا می‌کند، بنابراین مستقیماً خطاب به او می‌گویم: «آقای ترامپ، شما نخستین رئیس‌جمهور تاریخ آمریکا هستید که شخصاً جنگی را آغاز کرده و سپس در آن شکست خورده‌اید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/680696" target="_blank">📅 21:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تهدید یمن به حمله به میادین نفت، برق و فرودگاه‌های عربستان
🔹
«محمد البخیتی» از رهبران جنبش انصارالله، نسبت به هدف قرار دادن میادین نفتی، فرودگاه‌ها و زیرساخت‌های برق و آب عربستان در صورت وقوع حمله همه‌جانبه از سوی ریاض هشدار داد.
🔹
البخیتی با تاکید بر اینکه عربستان خسارت‌های خود، به‌ ویژه تعداد کشته‌ شدگان را پنهان می‌کند، به یمنی‌های حاضر در اردوگاه‌های نظامی عربستان، توصیه کرد برای حفظ جان خود از این اردوگاه‌ها خارج شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/680695" target="_blank">📅 21:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: دشمن قصد حمله زمینی از مسیرهای غرب کشور، خارک و قشم را داشت که با واکنش یگان‌های نظامی و نیروهای مردمی، این نقشه در نطفه خفه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/680694" target="_blank">📅 21:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680691">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5257bba3b9.mp4?token=I7LZYkka_RyKv3lO1p38Ym__IIdv0jzbBOBbxr-iiC_8AnEZHMRbefAbKp8iufFZWEcHobrOIThsN5rwXEhyNfUHLSjb5TWXCWcl3pSuwguqn45wA1VYHtCRSoiMiZ_wPc5CuHvH3b4a2Y7weryhK8Az4ttlhWFvgs5HAcE6byq29oWxXas2lCx7C5C0sWDKI-KkI6tejPSKif7tzfa9xlXSrbbzbRrkrClFs90nR5Lej38gpSSXXRiwuddGpOG2KqnyuZ1HeW0T-v5ISv3KW6Yo2lr357OrR-vK9gMZ8xjVJgtnA7tq7Ds7hVLt4G0rcoy9IfsCl1Me1r5sbWtksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5257bba3b9.mp4?token=I7LZYkka_RyKv3lO1p38Ym__IIdv0jzbBOBbxr-iiC_8AnEZHMRbefAbKp8iufFZWEcHobrOIThsN5rwXEhyNfUHLSjb5TWXCWcl3pSuwguqn45wA1VYHtCRSoiMiZ_wPc5CuHvH3b4a2Y7weryhK8Az4ttlhWFvgs5HAcE6byq29oWxXas2lCx7C5C0sWDKI-KkI6tejPSKif7tzfa9xlXSrbbzbRrkrClFs90nR5Lej38gpSSXXRiwuddGpOG2KqnyuZ1HeW0T-v5ISv3KW6Yo2lr357OrR-vK9gMZ8xjVJgtnA7tq7Ds7hVLt4G0rcoy9IfsCl1Me1r5sbWtksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر آخر ماه نمی‌دانید پولتان کجا خرج شده، این محتوا مخصوص شماست
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680691" target="_blank">📅 21:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccad136da2.mp4?token=r6_oJAhfZvq7mjTnGZCJh1iA57ZxE29P0mx0flw87AC6A6OkFDqLPVY6vaBs6HpZc4wQ1422BH32PAdbjoV4f2oX3WBlnWqjc5uDA9O28RxYf4m3d-SPi_SsrzIxZ0WXX7PMOdrsxRNiIo9_8WI17oOrldIoDZCJ3aHN1oeRvmOX47zjCgiil2jxTJs8Z0JbjelPlyI7rtyjXDQxF0K1oUlLeyB-pO0VK2-ZHk263Ynu79ewkb-1RU-OJCl5RWfNcdG2ea1zDFEEAGmbBd5xhaiKBLpzj0YrBqi8wAPaYw57kVuTCNl2FXGh7WwXWrT7i8v5r-agLmNa17P8pSL9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccad136da2.mp4?token=r6_oJAhfZvq7mjTnGZCJh1iA57ZxE29P0mx0flw87AC6A6OkFDqLPVY6vaBs6HpZc4wQ1422BH32PAdbjoV4f2oX3WBlnWqjc5uDA9O28RxYf4m3d-SPi_SsrzIxZ0WXX7PMOdrsxRNiIo9_8WI17oOrldIoDZCJ3aHN1oeRvmOX47zjCgiil2jxTJs8Z0JbjelPlyI7rtyjXDQxF0K1oUlLeyB-pO0VK2-ZHk263Ynu79ewkb-1RU-OJCl5RWfNcdG2ea1zDFEEAGmbBd5xhaiKBLpzj0YrBqi8wAPaYw57kVuTCNl2FXGh7WwXWrT7i8v5r-agLmNa17P8pSL9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از زیارت «آقای شهید ایران» در رواق دارالذکر حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/680689" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680688">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آقای ترامپ! ایران نه ژاپن است، نه ویتنام...
🔹
یک فرمول قدیمی در واشنگتن وجود دارد؛ بمباران کن، هزینه بساز، محاسبات طرف مقابل را تغییر بده و بعد پای میز مذاکره بنشین. آیا «مذاکره با بمب» در برابر ایران جواب می‌دهد؟
🔹
این ویدئو روایتی است که حالا سردمداران کاخ سفید به آن رسیده‌اند‌.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/680688" target="_blank">📅 21:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680687">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c4a0cde1.mp4?token=dQiJD2FJlpwOf8bMg0fYhoHGvzSSPjScZduh5t_HtfifsTuYVN4R3G_SxAe9vy8h67MKy1jwKFVWBgzgl-anLPcLVXzBPG7MMxw7r2XQ3x7k0LKSIRpdS_8cRswEdkltsOSv_sd4JHGlohmyHcgtFLMFZj-MVzCHRsaLiU74wjy5fhaUOvl6IEwyEnmHkDcxKPZY7JDPBU5rRPE8-fgGOxtzfOwZCWNYytisL-0AOjYL48zpgyb35Gsn6HPgKeslQEGdDD5qwU7wo4tmAoHoe5UG1SZGCb0u4n8iO1c2UVdm9C0SbMX3cAoD33TCSF0HZoLIUQa4t1TCYREPCEXq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c4a0cde1.mp4?token=dQiJD2FJlpwOf8bMg0fYhoHGvzSSPjScZduh5t_HtfifsTuYVN4R3G_SxAe9vy8h67MKy1jwKFVWBgzgl-anLPcLVXzBPG7MMxw7r2XQ3x7k0LKSIRpdS_8cRswEdkltsOSv_sd4JHGlohmyHcgtFLMFZj-MVzCHRsaLiU74wjy5fhaUOvl6IEwyEnmHkDcxKPZY7JDPBU5rRPE8-fgGOxtzfOwZCWNYytisL-0AOjYL48zpgyb35Gsn6HPgKeslQEGdDD5qwU7wo4tmAoHoe5UG1SZGCb0u4n8iO1c2UVdm9C0SbMX3cAoD33TCSF0HZoLIUQa4t1TCYREPCEXq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاصیت تفاله قهوه که ازش بی خبری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/680687" target="_blank">📅 21:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری‌ها از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
افرادی که صرفاً به…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/680685" target="_blank">📅 21:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26989930eb.mp4?token=hFsF73H9HfytnuAqfZOTBYEjc8E2UFAu0BxUGwvTTgIucvJ4jDL7iCVNcIxRGBiLMrWGo9BG6Qth8dZFk4VYk08hnie2xeg0qAm3vlj3DhOSdgNGFPvQS2Ibko0bI36OG2dTd9arM9F8Z3xfWYV2kYiAj1q8wpFeOHqp4lXjeFBzC58H_rQ1BlgpuvbxZgXIsj23Lczbl3lSSPtGxVLz1gDWTnqOVNLCq1bfdaiboPA1aOycGVpJY7g4Oi-ac6QRUOiasQyFDGF8rc-49ROq067dS5JIxCFlx0k-FU_Ghs1U2ihjAnEAfCtLVBLr83yfUFk4wBtiYWyNoNf9dlzTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26989930eb.mp4?token=hFsF73H9HfytnuAqfZOTBYEjc8E2UFAu0BxUGwvTTgIucvJ4jDL7iCVNcIxRGBiLMrWGo9BG6Qth8dZFk4VYk08hnie2xeg0qAm3vlj3DhOSdgNGFPvQS2Ibko0bI36OG2dTd9arM9F8Z3xfWYV2kYiAj1q8wpFeOHqp4lXjeFBzC58H_rQ1BlgpuvbxZgXIsj23Lczbl3lSSPtGxVLz1gDWTnqOVNLCq1bfdaiboPA1aOycGVpJY7g4Oi-ac6QRUOiasQyFDGF8rc-49ROq067dS5JIxCFlx0k-FU_Ghs1U2ihjAnEAfCtLVBLr83yfUFk4wBtiYWyNoNf9dlzTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دادستان قشم فرمان مهار فوری آلودگی نفتی سواحل جزیره را صادر کرد
🔹
دادستان عمومی و انقلاب شهرستان قشم با ورود فوری به موضوع آلودگی نفتی مشاهده‌شده در بخش‌هایی از سواحل این جزیره، دستگاه‌های مسئول را مکلف کرد ضمن شناسایی منشأ آلودگی، عملیات مهار، جمع‌آوری…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/680684" target="_blank">📅 20:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون اجرایی ارتش: بیش از ۷۵ درصد توان موشکی و پهپادی ایران دست‌نخورده است؛ ما نظامی‌ها پشت سر دیپلماسی حرکت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/680683" target="_blank">📅 20:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDy7b53z_vZ9PnEQCI8VFUH4nsE4GCAkYcbQq5CB5PhOkPBMGCIC3uGs9nEIIEVKQqcZeODksnOpt5lM3_Or5M2B1VPsQvpKno4aplbu5s5-poo9xWCNfHWrjj4DcBqNgc1BgXD39w9K4PYL9hzjzejuRS_LXG-77MJLiiLRK69pNpMfsONLLF9qtPeygTNaAhQz1yd25OqAITq9QvgZlR9W99tQ9LUYX_d29jnzTv8QWk6gNlfNDG3eB8UzzKaSRR1cO09nsmjInKJHaNLlCQEhH3YQN0eSU1t4a69ksNi45Zk-X8m7OQew9ql_6F0DKTVgatUQu9uK5_qGsUYeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران موشک‌های پیشرفته‌ای دارد که می‌تواند ناگهان تغییر مسیر دهد و سامانه‌های دفاعی آمریکا را در هم بکوبد
نیویورک‌تایمز:
🔹
آمریکایی‌ها با توان جدید ایران مجبور شدند تا ذخایر کمیاب رهگیرهای پاتریوت را بسوزانند. ایران در دور اخیر جنگ با استفاده از موشک‌های پیشرفته‌ای که می‌توانند ناگهان مسیر خود را تغییر دهند، سیستم‌های دفاعی پایگاه‌های آمریکا را در هم کوبید.
🔹
ایران با پیشرفت جنگ به دشمن ماهرتری تبدیل شده و یاد گرفته است که چگونه از پدافند هوایی ایالات متحده فرار کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/680681" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سفیر پاکستان در مسکو تاکید کرد اسلام‌آباد هیچ مخالفتی با پیوستن ایران و مصر به توافقنامه دفاعی مشترک با آنکارا و ریاض تحت عنوان توافق مکه ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680680" target="_blank">📅 20:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d16aec8d.mp4?token=JzNCaUt6oitbXKImkFecTIeOsfkRvp9MT9EwBIljgEdshcJM5QEyIGjvfPe_5_bf0zFT973YVHCqF33i6H_NronHfj7DII3UHYq49558-ACC6yuBY9bi0mnP7fKEXyKPXyid287WFYVS5gr-k9zkvhb16e93wVU7PBRj0MYWodNGiogu0AQ3ZikE5mFOZq6YWh_0bRL8r8ieteaY00xKefTPMuRoCJWee58_5miHTfM8vG8_xfEbwiaup2J9_mWkt8KSU1ISbS02x5exOLw0zPOaa2r2SqtqsEl1EVW2lefxA9JTjLZaF0nMcNB2GF14HdDeE30AtrHvuv2RDAAzvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d16aec8d.mp4?token=JzNCaUt6oitbXKImkFecTIeOsfkRvp9MT9EwBIljgEdshcJM5QEyIGjvfPe_5_bf0zFT973YVHCqF33i6H_NronHfj7DII3UHYq49558-ACC6yuBY9bi0mnP7fKEXyKPXyid287WFYVS5gr-k9zkvhb16e93wVU7PBRj0MYWodNGiogu0AQ3ZikE5mFOZq6YWh_0bRL8r8ieteaY00xKefTPMuRoCJWee58_5miHTfM8vG8_xfEbwiaup2J9_mWkt8KSU1ISbS02x5exOLw0zPOaa2r2SqtqsEl1EVW2lefxA9JTjLZaF0nMcNB2GF14HdDeE30AtrHvuv2RDAAzvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشتار در مهدکودک مینه‌سوتا؛ ۳ نفر از جمله یک کودک کشته شدند
🔹
پلیس آمریکا اعلام کرد در پی یک حمله چاقویی در یک مهدکودک در ایالت مینه‌سوتا، یک مرد، یک زن و یک کودک جان خود را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/680679" target="_blank">📅 20:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjlc9FeDTgT5yyeUdrBurzUroXgbwFNEa1LM7gj6lvsTKCtIg1ZqKifM1qpbA2-Yc1rql3ogn7jgNW4bkI4cf-A8MQ1fXWWSJ9tTdIwgbozNp9WKB42B1DF2f4s_GrUCNcU4G2-OZWqToDNKztJZBCMpAYEqjDVei4U8FIy_XTszhXPHvCcTl5bHYF92V_PSmmXRvME3vZd02WM7-ynSQgbNTcbxl0E5ZbeesDBnhcChi9Upec9WqDLH-NV8OYJE2FBGCzXozshnbdJLyAOHw22aiHB2GbPRA1s3FB1iVwl1aOGA4MAe9eQ7mmSL_RJbw1YZ1nxrxgs8JYOk1CTL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGdiKXY5ZAxFELoqWOC1lq8ENTKi-n-jqRkLLZJhfvIdaCUM5jaEQaYsQA55xgkyLkdEnWLVu46HKLSvMUCwoL8t1NP3EBZGe3IH1k9twXV3KWmnviDSlNScPDZ9sv9XTjZfsz2b89Miy9Be1QMAdO-DN9Zq-WujE1LhQDmHTCEMmcn9BJawsSv9VOlOpsatDmNqaPaJSSdcZxznBfxtuqf7pd8DIZ3wHCcBAss8jHFSSHK34j7uMUKMbO5GSgwD3T--etc-1EWZrKtfkjlo0z9krrMa6Wra3KfJ_RUmjijW4AIPJ6-HBGAEwP7DuZHPMPWpmt2THQiO1KoIFq823w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfuBGowukYEbYKIcYweKTVmEpiX_HYoejFLbL9Lmc7RGCC7MFjTyiUkrLLK5Sgc1kbsiGpAKbs8rxJQB8iVAyHYmq_CB41Yjv5BWdcehZtVC-lJYXzF4-SeY4r1JbXcxDKLM5KgAV1aLxI2bfulHGtmCRavcqevCeOanrTP7_egK_PuQl-as9k5YDz7S3lwcmtmom1_I0mVK4s_I2CbW9dwvQ06dEgNrXAXQH6I7rQln5vPZO3pDacpyLAIAYVd4e9eTzVYgLL2h9a59LCGaNNn2w4NBMdfaQ875cO3XCJ1xAPAGLlzu9iWcNxKQGQiaGWZBMOKj-539SU3Uwg0JZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXLJTyHkg6sVEqsGEd6klHUzGxkowI2BDMqxRHhHanpMybHgYLBUv8DVgb848UY2LbVfOIrGl2t3CRYD75WDQO7EAnpGGGPNK6_Sszf40tKV7QBV6xbXId4ECdtJC8ruh9m23HwUVTyTV9PSgzBGbdJGfx4LjZkNchVW4KFSarDMKiUOT_Bcx3xh_6avsJfeUbEavy63oKMKcxwhNr7R4FAmwMkjNJo9yBEObwGLaAy6km51B8cRnpM2dpGhLmeSwlZPBDBFNIhnKotaNlqgO-tCfcFSx61wakeXvJGgQ-hdcdwKhm74IecR51kcCDwRUr2tp8QHOnHs4p6BdJaDMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اوباش صهیونیست قرآن را پاره و به آن اهانت‌ کردند
🔹
شهرک‌نشینان صهیونیست عصر امروز حین حمله و تخریب یکی از خانه‌ها در منطقه «بیر قوزا»، در شهرک «بیتا»، واقع در جنوب نابلس، قرآن کریم را پاره کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/680675" target="_blank">📅 20:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ازدحام جمعیت درجوار آرامگاه آقای شهید ایران، رواق دارالذکر همزمان با شب شهادت امام رضا علیه السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680674" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVYu03ykvExcFGDBfFxQ3Zsk9HKbsWqVCRH64vYpAEuMUA1qLXe1xnq1fWwQO-op7JKLS8u6DMwshIxPJ5OJPbWu-4r06LDadiMGsmuoL2RHKI4S6hIiQlKcw_gQxoDUfybQiPsVx84JsBYNyWqugplYeLWw3ChEtjRtat4gF9HNTKg3KQHFNvPMg0CIjxclHQD46iQE6maKCWm1qRNXrlt3LnYHmxuEXPl852bv3GbMHw0sw_IKs8bhmnVmL8Y1dTz7eP60jQZ1ElyUkBSyz8iD_W_K4Nw5Wfjd5P0ppt0Kv4lq7epHnW_f-wCcUbn-6n1-PieyCbh9lXhSo5fuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
روضه خوانی مرحوم استاد ایرج خواجه امیری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/680673" target="_blank">📅 20:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAH2wl5kHKiKCykFv5gujiRQw7oxTVLmUkUBsM40wslqtyu1UpOvN07m39tIfTyItAB_MUZeRqNyaAJBxHEeZWc2i_VYiTIH3RHNM9ZsuCpSzCAdSV3yOnzAE0K3x-g7uhp0fOd3CfaOqATv6AilQA0gk-5DZ3vKbzZfhFvLa9o3YJRiij161zNPXHnGa9Tkc-NClkF8wDsrH9xe9axRxqG90P-lxF9R6cI1W0-oXPv7zZZlzrzaJB_9oczn3L74COoLUREV1OtL-aLeKa_GSTUIPR7vDCBRdgeRfBmt-HxMCX66IxZzPtmIxb84tiIna2XNF12RfBzQUfqG7Q_VxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: هرجا قانون در برابر قدرت سکوت کند، آنچه فرو می‌ریزد صرفاً یک پل یا نیروگاه نیست؛ بلکه اعتماد بشریت به امکان حاکمیت قانون در روابط بین‌الملل است
سخنگوی وزارت خارجه:
🔹
امروز، ۱۲ اوت، سالروز تصویب چهار کنوانسیون ژنو در سال ۱۹۴۹ است؛ کنوانسیون‌هایی که هسته اصلی معاهدات بین‌المللی مربوط به قواعد بنیادین حقوق مخاصمات مسلحانه را تشکیل می‌دهند؛ قواعدی همچون «انسانیت»، «تفکیک»، «ضرورت نظامی»، «تناسب» و ممنوعیت «رنج غیرضروری» که با هدف متمدن‌کردن بشریت و انسانی‌تر کردن جنگ وضع شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/680672" target="_blank">📅 20:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXAoZhyaaY1te26VpOzbte0bQ0vWFZTWrVYJzjhe2ZHKY2BeftirbkcxMddQDcLwkmjAUuVipOA3cTn89T6uYQUtfYBxCCgTuLurWIHl2w6VPduzbIaybNn4m_1ine2kv5GBglQLvgLGBnGZjVgxtrtoqncdhw_qhQxJVNXqtaA8lnRCR2j66nT5N2RNarQ2naLAuGnwQNa1RobHaT0zLsok6QnbLFAZ8lOFBBAcPZVts5ztOHmxsvBPZdu-hTtb03727Bu_lyV5VvTA5cF9ncLCrkJUcwc7AQHBWgX11xO6bCbrdb5b0oXToEv85PwiU2bEAgpNBu8dULqCkBYm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوپرمارکت‌ها چه می‌فروشند و سودشان کجاست؟
🔹
بر اساس گزارش سالانه بازارهای خرده فروشی، لبنیات با سهم ۲۰.۴ درصد، صدرنشین است. خواروبار و کالاهای اساسی با ۱۹.۴ درصد و شیرینی و تنقلات با ۱۶.۶ درصد در رتبه‌های بعدی قرار دارند.
🔹
نوشیدنی‌ها ۱۴.۱ درصد، شوینده و بهداشتی ۱۳.۶ درصد، دخانیات ۹.۳ درصد، یخچالی و انجمادی ۴.۲ درصد و لوازم مصرفی ۲.۴ درصد از بازار را به خود اختصاص داده‌اند. چهار گروه نخست روی‌هم‌رفته بیش از ۷۰ درصد بازار سوپرمارکتی را در اختیار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/680671" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بنزین ۸۷ هزار تومانی در کرمان عرضه می‌شود
🔹
معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی به مبلغ هر لیتر ۸۷ هزار و ۲۰۰ تومان از بامداد پنجشنبه (۲۱ مردادماه) در ۲۰۴ جایگاه سوخت استان خبر داد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/680669" target="_blank">📅 20:14 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
