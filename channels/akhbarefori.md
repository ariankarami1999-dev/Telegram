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
<img src="https://cdn4.telesco.pe/file/TOn3M6IjdpmkKHQ0QjtKns5ZMTMuCx2PponC68cHUk_vsqGpCYCiHB5BMvpH7pWxysMaHCbybOfYYK5yFBUSogP8-LoeUIuH_nxYdUvZfW3yg7x_IMowagBGDHqP2FnQ2Od5RE5wxObDOSdalcyCarG-xsh7J1iCBmhYoH5lMqXLJdGTKNGTZm8D68YUAHTrKoNC-RyyURgXIoRB-YiCpWYRhktO4DWRqOWujyYuwK1QF_Z3ZxUcCXeoOp5LLBuZoJkpccDcL8XOS89XsendHetu3OftIeeBigA20WfhgvHz-DyHs7MqfXDvFjaT_F3r61Vea7QPiCFVlcZbkDUYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-665686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت رفاه: واریز ماهانه ۲ میلیون تومان برای متولدین ۱۴۰۵ از فردا آغاز می‌شود.
🔹
رئیس مجلس سنای پاکستان: رهبری آیت الله شهید خامنه‌ای برای جهان اسلام همیشه به یاد خواهد ماند.
🔹
حزب‌الله: دولت لبنان فرصت ایجاد شده توسط ایران را غنیمت بداند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 712 · <a href="https://t.me/akhbarefori/665686" target="_blank">📅 20:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81adfe9f60.mp4?token=SCRog0JFZ44JaMeyENWhD6X8J5rmJOpQccR8QqWfctZlfTBumlfXRHieHlfzSRqp9rGMPZq6nQTco78T7wpdkoT7wrMIhcKhpmPDvaOwCVWnS2_K_egJ7NaJm-Xr1yHS7jpH4eU6ntjEmDLWaziDJSgYH9IoA8Cw5xNWFGAV6K-YWQ1ruQ_xlMGyPAoIC87pidIRqj_HqnfKfXV-a92Bs-bhT2uCGdveC5ZrGQ_Zm3y2VhaqL_alJmnkpMQuqMETohysnJgPaWTQ4BPa3FwztHk2C_z09OVFvhVbox5ehbEV6y28MY66hCpTmMTYhe7Gc2fhNX47CVDVYQ4-xbBiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب آشپز سابق صداوسیما؛
وقتی کودک بودم لباس‌های دخترانه می‌پوشیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/akhbarefori/665685" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0539c154ff.mp4?token=rwlfdRo-UQe_yByaZ6ZV55Tt1siD34BxI7huMQYA5h36X2ju8rvN0g7-Z8KKZcE0oatAK239edEDSR6t44tO9OLBxxfk4IuMNug4FjjfHAEK-Nj4fcNR7cIglkaqG2Bs0iRQXMWSUCmGxAXt1iaUu0lfZ0a0B2T-qNZUbMY6tSrGB6wc9ql2qU7gSEngVjzA2YyhRe2gCQz7iWhfFJ_zW3nW7DVeXmzUUWpgGKGwqTgdv8VsmVcNb5GP_9naUIjv5QoZuOrRuVerR5PkWNNfwFKqvP0XIXmH0aTRklMVMyIjMW2bAUueutXWeLWnWG7Ua8KPEgFCD1MfSaW6hW0LV0loklyf9acaMR9FctkpP4XWw_1fgzPq5WFGCwbd874QhNPQw75EzIPcTHr4s7HhPPVtlIFa7MFwkKilmHUoL-Je1ajPH3iv7PND-O96BaB3OnUQfdzGvkczVp3ExFY03Q7XxVyDsAfNEvefeKURUPCqpnxmJh7g-AEVrQZVUQpJc3EoqaRoiLU8fCRYzHtFgzd1Xv9WWwe_kBFp3Si8I_E-Ks6i8JlnOWV5XV-TkmUrI3qdJbEtt6bOmwTc8U-yRCrVuxG66927Uj58H9DC80oVBFSyZ3kwyceBhvTr0cHh-U0hP-PQwjmwZqLhF_78F1T60uUyixFsPp5sdvv5hCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ تدریجی امپراتوری آمریکا از زبان تحلیلگر امنیت ملی آمریکا!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/akhbarefori/665684" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محکم در آغوشم بگیر.pdf</div>
  <div class="tg-doc-extra">39 MB</div>
</div>
<a href="https://t.me/akhbarefori/665683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل کتاب محکم در آغوشم بگیر
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/665683" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiKQROxgQymi4eTRkl_wS-FHZ0TSA1s92GlThO4asVkw0pMc3XW21XnhQ9Q2JlMRmmIIARcprULK3A6nCLuZcr9rSOSU8h1vAAcBpr4TjnMh17-hNjrLTdwwBNIkk0gzjmtkvPHpqEQbnCWepnIMoKwBE1s5TrQTRiVvNpUPJ3OyMwZA57Yw0i2ZstqIpFJ1BnR17UcMmUYdtce3CrFVyxrhnPE7QK-aTwQIhDk8RnjZkMeVUNxmU20arxiaVxrdD51-4w3hi-ezGoQTxMUr2y6ouCYNX6nRqRX6I8mGiDmN__UIP3j-7veqimXCAQxwMW1pID_1SOPEPPu1Koz90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y892wUHbzrfFxYp6b7sbPA3B0WDIXL5VxotEl3dYKL-DZ7A0gDO0fM5EefQk-n4egCxuYhrNS1juMCo4LKhX0SHxwaveba2Fv_pNWxi1cubNDWFrZ4IEinfaxVJlXSRvU1RcFV2WtsD1BulfbM-61-xWFuF8GR_ZH5juIxuU1aSCLuqudRPaJf_uY0HOZo4aBnI-ljYoSh1iLsFJMpYYJ_0ryZPulB-bZvzGgrZ_wcUap8JGSrBgDFLQBwRvqVc2jPtYl_JIxPHVZ7hpL9eE_fqYEYmgYHQ3tUm0LNyNKCpd5kx-0A_asL3eQx62QMdXtq38sNEYWZRZqqZtDlaknA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر رابطه‌ات سرد شده و نمی‌دانی چرا، این کتاب جواب خیلی از سؤال‌هایت را می‌دهد!
🔹
«محکم در آغوشم بگیر» اثر سو جانسون، یکی از تأثیرگذارترین کتاب‌های روان‌شناسی روابط عاطفی است. نویسنده نشان می‌دهد ریشه بیشتر اختلاف‌های زوج‌ها، کمبود دلبستگی و احساس امنیت است نه نداشتن عشق. کتاب با مثال‌های واقعی و راهکارهای عملی، مسیر بازسازی اعتماد، صمیمیت و رابطه‌ای عمیق‌تر را آموزش می‌دهد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/665681" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نشست شورای امنیت و تکرار اتهامات آمریکا و بحرین علیه ایران
🔹
نمایندگان آمریکا و بحرین در شورای امنیت، بدون اشاره به تجاوزات علیه ایران، تهران را به حملات «بدخواهانه» و «ایجاد ترس» متهم کردند.
🔹
این در حالی است که ایران پیش‌تر پایگاه‌های آمریکایی در بحرین…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/akhbarefori/665680" target="_blank">📅 19:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Ud5qP0_uF4t4FZrof5_axMbjlU9Q-PB__hkzMikMYVsrhAKpWEEt76hmuQf2KQHljxj6GNQ2vwmYh3GxKzcABJdObkB6a6fBzZCde6qqzFhPS4OHrL_ybTayarWZjQIpgVc6fg667wK3l_a31U9TfACWwpwZabKuZcqM7my3PAgCBx6GY__KScehpFnUOqGatTL65UfLGMO_KKuoF0_-vpWcv5gXfC28sfgmOPoeAURSZrD_6jkJXDjbjNAHV1eiaHVQj3vvT9wdzTumj2QkCeVR3S4PO3uUKiYB4qVdkj2c2SfU8Ukrbo9C0zrSekSVP__-Ie95_lQ8IVusmm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنایت تازه در جنوب لبنان
🔹
نیروهای اسرائیلی خانه‌هایی را در «بیت یاحون» به آتش کشیدند و یک پهپاد این رژیم «النبطیة الفوقا» را هدف حمله قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/665679" target="_blank">📅 19:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEqAGXXTZOmYsHu3suroRe4qV-ieaZmN5opPXahCOXkpy51MpHl9028KFNIa955wq6JLuV7UsuWlJleS5OkGLoxwvUOq_H7Zbminj4KlKUnbPnMkTquLtJUuzKWPIU_JEe1RCKkIbu-BNJIIlfj9DgF_iviTeIdzqtRqB9w7-BTvG_9GT3G8z4_a87qQc9GXtEFxvtCOJqIaCUtoROUE26sjbLTBBDa55AW96MdCqjgWDcUWCi--Wfg5Kb8wsfsKJEcsfme3dR4vtrssT69Xa80Wb2vwuvR3hc1QBQ5W6KKzDMq8nJ5atA5W-Rhxvf0fnkk_p26-y6BoiU7wQ1kJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور سردار وحیدی در مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/665678" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تلاش آمریکا برای جلوگیری از کنترل ایران بر تنگه هرمز
وال‌استریت‌ژورنال:
🔹
آمریکا و عمان در تلاش‌اند ایران را از دریافت عوارض و اعمال کنترل بر تنگه هرمز منصرف کنند و از وعده آزادسازی بخشی از دارایی‌های بلوکه‌شده به‌عنوان اهرم فشار استفاده می‌کنند.
🔹
تهران به این پیشنهادها پاسخ مثبت نداده و تأکید کرده هرمز «تحت فرماندهی ایران» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/665677" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نشست شورای امنیت و تکرار اتهامات آمریکا و بحرین علیه ایران
🔹
نمایندگان آمریکا و بحرین در شورای امنیت، بدون اشاره به تجاوزات علیه ایران، تهران را به حملات «بدخواهانه» و «ایجاد ترس» متهم کردند.
🔹
این در حالی است که ایران پیش‌تر پایگاه‌های آمریکایی در بحرین را در پاسخ به حملات صورت‌گرفته از آن‌ها، هدف قرار داده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/665676" target="_blank">📅 19:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZA6ZcwPK1KhbxkvfznfwIhMjjaEGyMXFWh0mLpXHQIo4sfjVFFvHw1ZXjDZ27jzvARX0wHoILWx_971F9eGSg6jIrbcH530lXYrR8NroKnrqXa9NZ4yIJzIib4e5Pis-aWxjpcHHCWnfmtJe3lre6N9PFA0ecopAmygbaxct3OZ03B7IHP6_REyPHzmXwwXa51CAL113Os3nNIdBNkXCyqp-gwL0r3xwuQ0ATJYhQkM1UgOVOOUQP7x6mFJrTUmpT9hC_leaoihKe905asb2wz2xeF2Nqe1DdYEsRx5WmTq5NWOM6o56hVwox5kTN01ZhD1WRioHl1Lhmr5Pa5Xag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع‌ پیکر امام خمینی(ره)، ۱۴ خرداد ۱۳۶۸
🔹
عکس از علی فریدونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/665675" target="_blank">📅 19:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7f19774de.mp4?token=ZC6LOBnET0_DWiMe6iHXU-7Nd0_VrQOR4D2SQsGb-QfY9UzzwTE_hKTnRAif5-5UNd2zJi0NMzWsMVqsUo4JSXC5hRg2xJueJ-Dh-Jl2oKKpxre1Dff3dlhmdLiDOZT15bjKy8mqUHfYrXqMhtlp2iMOw13X9JmWwkZ99jkENElX3uftyCK9IWbzCngwsvX0ln_7Nh4AhL77w6jMo1GqmJTlz32kP2B8culzP2aDcRXCizAEFZOF8L-u_vjwsk_7kTiv-zQ5jb3n5QSZoHnlBoKKezXIeJOmXuyWmezx8i-GQbY94omVjg17zPk0ZNAuOowEhP8Q06DL_cTKsxv2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7f19774de.mp4?token=ZC6LOBnET0_DWiMe6iHXU-7Nd0_VrQOR4D2SQsGb-QfY9UzzwTE_hKTnRAif5-5UNd2zJi0NMzWsMVqsUo4JSXC5hRg2xJueJ-Dh-Jl2oKKpxre1Dff3dlhmdLiDOZT15bjKy8mqUHfYrXqMhtlp2iMOw13X9JmWwkZ99jkENElX3uftyCK9IWbzCngwsvX0ln_7Nh4AhL77w6jMo1GqmJTlz32kP2B8culzP2aDcRXCizAEFZOF8L-u_vjwsk_7kTiv-zQ5jb3n5QSZoHnlBoKKezXIeJOmXuyWmezx8i-GQbY94omVjg17zPk0ZNAuOowEhP8Q06DL_cTKsxv2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا استفاده از داروهای روانپزشکی اعتیادآور است؟
/ تلویزیون اینترنتی مدار
این گفت‌وگو را اینجا ببینید
👇
https://aparat.com/v/jjy2nnk
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665674" target="_blank">📅 19:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCi23Zulef5Ui9m9rGi6AsPM27yQcgBjLno194v15WwG-SIqXIiXMgV68UtC_OI8CGvJ0VjiOaWcBW19MyHEBeLskWrhn0V_44WPdEMc0gGSE1ScDTcXRGyUewVTGHT0n1I25mPxtZV2wHtEEmBY7GET_oKQ8g3t_qUlUcGVg6avMtGhYa7bNV2lJMgydfUl_hy-2Trx5Eg5RdyFTGUnRg9usefkASxo1F-Z4Dg20fx3wIQqwGaecXwAn8rpIUbHttPltPx07jiri3nHpKyCb5977RWblIZ8HRQwqcj1v-x6BAaSH-gCMobbQh2HdjleCprWg2PO3bM7LVPqNAdKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبل از خرید آپارتمان، این ۳ مورد را در پارکینگ چک کن
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/665673" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeM9lTgRZqoiBYJ9gJfwgDkhLvoOFu_ccVTvTLahVqdu7m2srmWKct_di-wkDCjrogHCIQ7zzQGI6NMYV61HicBMNcllXftU29963WqVHnqenzPijBIRzgboJzAGj-GWcbCyv1PskPIhkeaadfX4VhnIQvU_PagYD7lrS-WTeBKo6eEo6ZDBWS0ezV40BPdrms3VcftDS6skyGW-ulKiWS2h--X_rYD3S4nT9XJspN-xvlmxBlUAsYUgbH3_Azq_PkLliLcwX3m6aQ_0RVuNrNq_BSA9ja_b11nqED54kNQGV5QvkDAdt0FvXr1eeb_zXiXj66B7leR7y5rN8BZzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه عواملی جان کودکان خردسال زیر ۵ سال را تهدید می‌کند؟
🔹
عفونت‌ها با حدود ۱۴٪ و تولد زودرس با ۱۳٪ از مهم‌ترین عوامل مرگ کودکان زیر ۵ سال در جهان هستند.
🔹
سوءتغذیه و بیماری‌های قابل پیشگیری همچنان سهم قابل توجهی در مرگ‌ومیر کودکان دارند.
@amarfact</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/665671" target="_blank">📅 19:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هلاکت ۲ نفر از عاملان شهادت کارکنان فراجا در نوک‌آباد تفتان
🔹
در عملیاتی هماهنگ و منسجم یگان‌های عملیاتی فراجا با همکاری نهادهای امنیتی استان، ۲ نفر از عوامل اصلی به شهادت رساندن کارکنان پلیس استان سیستان و بلوچستان در نوک‌آباد شهرستان تفتان به هلاکت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/665670" target="_blank">📅 19:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7gkmBBRtDYnd2Ypz0vcsKs0aogVVQNqnaBfLWXiCyJo67RprqkApHT_LN9Eq3-Yzd7_0iwdqZG_MgbqEztkuo2d7I7CJcIFdX6fLRAMwK3PzHj0sl5_-eiGQTptFfeS1qjvV_SHesPyABcFL2V_Zp_UA1tDYxR50C-C6sdPJHZazBoKiRBbaLX6hOyTwyx0_mWvoqm-UJD9dHxFmIQ3xn6SH6MINupLEUukh2Sim4hKi-RckFhtf5M65XE4xJ184yOtyG1kosIlGqH4IR1k4woWC6nGzWr6E0L_WdTRPe6bDX9rxJxNnaw4HckoYAOxK4OZRGdnDoeWkC-gGeivrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۲)
🔹
به عنوان یک کاربر فضای مجازی نقش شما در بدرقه رهبر شهید انقلاب بسیار مهم است اگر از آن تصاویر و ویدیوهای امیدوارانه منتشر کنید. امید پایان‌بندی این روایت است. امید یعنی خون شهید به ثمر نشسته است و فردا از آنِ کسانی است که امروز ایستاده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/665669" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت اتریش در تهران فعالیت خود را از سر گرفت.
🔹
سازمان هواپیمایی: پروازهای داخلی و خارجی شنبه و یکشنبه برقرار است.
🔹
تیپ «گیواتی» ارتش تروریستی اسرائیل از جنوب لبنان عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/665668" target="_blank">📅 19:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9KYjFySi7HTce-hU7P1xGK9l5FmC7fspfMBlmmoOIn8jYCirz_VZ_kzqwjjUqZYveCR1cge_II9H40exZfXXRQVQisX2fYTeei5rv9OVWO1lCWOdNfQJSvIGqnUN1Zk9dlemOPRc2_H4EhqIT7lpC1Lx4xaQt8DcaZHTibU_J3IMXAqal76q2mFvKrrCk1UkxbgAtbEBkjFdNmCELFwPqmEvbRqqRgJjc-xjE2fzibLfO_DbZpe1eN1x9KHIEKP0uxA6nsYohB27hGHY3tuiRPiU4dpAC6NMh_xpUPAf6MzgwcjTBVdaEDfHFPN-rfBwgtiCEJT_GoQ1zGGFsFRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665667" target="_blank">📅 19:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbRN5XNJSPIYT5LdMKxfjgoF54KKniU2hBIk-5KDKmH91nhMh52OUDNS6y1ZjFdkqXFSfuFZrr-wbb9Dupx9U7Cz3KwNnAmk41ArA-fHZtNxW6grtND2N4zEFBioCXzrXPpcZrmeIZ7u4X0xn-KO8_UUdsasOhe7v_AfWUqe9rBaEvKu4f9G5HITDxmwU57U3ZyzfFrPkPCCcHxQll-ewybzpe5_6byCzE1_s_JJCaQBhvECAvllpQJBxG60FP_MRjZP4oBGnAxhOqL5CqDRj1CXd1ivRsvu0BZ7l9ex5jcn8DtWpd1KIalIsKknKNsgDeHoik7-ulk-GIdkfVEgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال تغییر زمان برگزاری جام جهانی از تابستان به زمستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/665666" target="_blank">📅 18:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آیین نامه سوگواره بدرقه یار.pdf</div>
  <div class="tg-doc-extra">260.6 KB</div>
</div>
<a href="https://t.me/akhbarefori/665665" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">◼️
آغاز ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای «بدرقه یار»
ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای بین‌المللی «بدرقه یار» آغاز شد. این رویداد با هدف ثبت، بازنمایی و ماندگارسازی روایت‌های رسانه‌ای و هنری از مراسم تشییع رهبر شهید انقلاب اسلامی برگزار می‌شود و پذیرای آثار فعالان رسانه‌ای و هنرمندان از داخل و خارج از کشور است.
علاقه‌مندان می‌توانند پس از مطالعه آیین‌نامه، از طریق لینک زیر نسبت به ثبت و ارسال آثار خود در بخش‌های مختلف سوگواره اقدام کنند. همچنین در صورت عدم امکان ثبت از طریق سامانه، امکان ارسال آثار از طریق شناسه رسمی دبیرخانه نیز فراهم است.
#بدرقه_یار
◾️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
◾️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665665" target="_blank">📅 18:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad90dc443f.mp4?token=V7aGcdcMOGZfV6s9RVVpyZ7azaoWQcm-nwFqn5RQaBla3r6s9eiy03pcssDmtRxg-L4ZTeuL-gm5mqcFTsEqjtm8UMFEVeeMDQPeXrJpwvMBrpMmFC_TH6QIlvn4mqtbhiW7ZSgVcXo2YPdOgmM922egrKIshdCeAMHnKxcQS5YLSaPRycre6gJP_ANg96mCHpoZoauIRcXVHFAj2uQQ5cj78PRV5oK98gn-zPcivdsJeWRCKKXD966WH7QBKsKOwySArH1OilFY0KIcE2o9K57vzt8DKlEtGKidMyKrSUdt_ZSMoP56eCVtM8eyLlZWhUN7BZBYYk5m-Bkfdmhvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad90dc443f.mp4?token=V7aGcdcMOGZfV6s9RVVpyZ7azaoWQcm-nwFqn5RQaBla3r6s9eiy03pcssDmtRxg-L4ZTeuL-gm5mqcFTsEqjtm8UMFEVeeMDQPeXrJpwvMBrpMmFC_TH6QIlvn4mqtbhiW7ZSgVcXo2YPdOgmM922egrKIshdCeAMHnKxcQS5YLSaPRycre6gJP_ANg96mCHpoZoauIRcXVHFAj2uQQ5cj78PRV5oK98gn-zPcivdsJeWRCKKXD966WH7QBKsKOwySArH1OilFY0KIcE2o9K57vzt8DKlEtGKidMyKrSUdt_ZSMoP56eCVtM8eyLlZWhUN7BZBYYk5m-Bkfdmhvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش کارت‌های جایگاه‌ها برای مراسم تشییع
سخنگوی اتحادیه جایگاه‌داران سوخت:
🔹
مردم در صورت امکان از ظرفیت کامل خودروها و وسایل حمل‌ونقل عمومی برای جابجایی در مراسم تشییع استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/665663" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آغاز واریز ماهانه ۲ میلیون تومان برای متولدین ۱۴۰۵ از فردا
وزارت کار:
🔹
اعتبار ۲ میلیون تومانی
«کارت امید مادر»
برای بیش از ۱۹۰ هزار کودک تازه متولد شده از فردا(۱۲ تیر ماه) واریز می‌شود.
🔹
این اعتبار در روزهای هفتم هر ماه واریز می‌شود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/665662" target="_blank">📅 18:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0yFTnTG0i-bveTIcKCoHyeerdFWqzzNfGTKbJ06RXNo3dZ9kcQFXDD5WLagR2XAhCwvexH0YEhqlYwo-yTEFfqwtUAY9YbPKbj7wzESrayGH3iRKcqUIl9f2X8zq9XW_drCVIsQK9QWD-3MzVgmkci_Iiw6FKrqdXau0_U2rmfrDQhcErx-7lJtZ9yVF9XxQQJZqI0IPT3p-ezwzeZhOeE0o7WOH8G_hUz1_hGpAuRHx2omDNg2H4Nn3bdVxvJRY2eG1GQWocC5W6MNgAiPA4xoiU_9l0hMtir3CvRDyq5JTHdKCETqUn7uFujgPXFeTzEJroWqgPXzZWTSAUk8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشته‌های گرمایی در اروپا از ۲۱۲۹ نفر گذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/665661" target="_blank">📅 18:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
بلومبرگ: توافق کشورهای اروپایی برای پرداخت عوارض عبور از تنگه هرمز به ایران و عمان
🔹
خبرگزاری بلومبرگ گزارش داد که چندین کشور اروپایی با تغییر رویکرد خود، موافقت کرده‌اند که کشتی‌های تجاری آن‌ها برای تردد از تنگه هرمز، عوارض تعیین‌شده را به ایران و عمان پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/665660" target="_blank">📅 18:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بقایی: از هر کشوری که موضع ناشایستی در قبال تجاوز آمریکا و اسرائیل به ایران داشتند، دعوت نکردیم
🔹
شهادت ۱۰۰ نیروی الحشد الشعبی براثر حملات آمریکا و اسرائیل در جنگ رمضان
🔹
جاسوس و عامل شهادت فرمانده کل قسام در غزه اعدام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/665659" target="_blank">📅 18:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16jXr9-NpDUmTK8NlOVXd2iDIDlenFW8GieL3IdPUefDaK-gNmo-HVE6fsO7pQ6AGIQgJBbzJxqAAT4TOvZWesl29ccaCjumBAWKwCl2dPs4HgOJcbK2cS3ktrBwG8muSgzM0X06w22Xrc-XCOVXC4czt-oBwsRdPmnLSztGeJaN62em4R6yME7P8YCAXV92zwr00zhFCU3GB8A2coN1X4pXRbzUhSxNt2ZLBZ62KvGQlrIAfEEIIam5j6sBZZa2udBT9fr4bG1_3LyTTlEGOdEnT0MHbWaVRcplz7rtgpAogcG-ZH5er2fx_z8_OezH9CrZhZ8J-w1ECyGQ7fwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک خرمدین؛ ایرانی که بیش از ۲۰ سال با قدرتمندترین حکومت زمانه‌اش جنگید
🔹
۱۰ تیر؛ سالروز تولد بابک خرمدین از نامدارترین رهبران جنبش خرمدینان، سال‌ها در برابر خلافت عباسی مقاومت کرد و نام خود را به‌عنوان نماد ایستادگی در تاریخ ثبت کرد. روایت مشهور لحظهٔ…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665658" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیرهای ورودی پایتخت برای وداع و تشییع پیکر رهبر شهید | هم‌وطنانی که از شمال تهران وارد می‌شوند از کدام مسیرها استفاده کنند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/665657" target="_blank">📅 17:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJeQ4TgDa5ExyEMvVIXGBuKtqpWdxQHP5SkX_m5mcX9RGX5wDZtCOMv_bCoQa2udT4dAGAF6BWBogKaZ-jdC-H7RAsIHE5y4LIQJp9y3rU-FRKjQYrmqPvwTbxu8NrdoytemrBxx90Zj7EqsOwj-OLFMSbUcoHAhJKePkpHsTPcMZFqPq84gCoerubq4a6NIw6STVycZRhr4nwfOFRCC27qjUKYfNRpT8nYgmI8UGQe0ywVwpXMICwm3BpYy432igEIWFvUh4DhavGeRyWs0iCk365GKGVKCLM7pFohAwVGN_JPAJc8fFYvzgOpCOSiBuT9sDf82mZ5Z_Fl9YZZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: برگزاری نشست امنیتی با کشورهای منطقه، تلاش برای سرپوش‌گذاشتن بر سیاست‌های مخرب آمریکا علیه صلح و امنیت منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/665656" target="_blank">📅 17:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات خانگی که برای انجام روتین‌ترین کارهای خانه طراحی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665655" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز سیب‌زمینی کریسپی رستورانی
🍟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665653" target="_blank">📅 17:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تجمعات شبانه: ما با آمریکا پدرکشتگی نداریم، امام کشتگی داریم؛ شما اگه پدرت رو کشته باشن خیلی راحت کنار میای دیه میگیری ولی ما امام‌مون رو کشتن کنار نمیایم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/665651" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
درگیری عوامل انتظامی با تیم سارق مسلح در زاهدان
فرماندهی انتظامی سیستان‌وبلوچستان:
🔹
لحظاتی قبل، عوامل انتظامی با یک تیم سارق مسلح در خیابان بزرگمهر وجانبازان زاهدان درگیر شدند.
🔹
در این درگیری مسلحانه ۳ سارق مسلح به هلاکت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665650" target="_blank">📅 17:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان با تو؛ رسانه با ما
🔹
راوی بزرگترین بدرقه جهان باشید. توصیه‌هایی راجع به قالب و سوژه به حاضران وداع و تشییع
🔹
از هیچ قاب و صحنه‌ای، راحت نگذرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/665649" target="_blank">📅 17:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پردهٔ عجیبِ تعطیلی مدرن‌ترین کتابخانهٔ قم؛ تغییر کاربری از کتاب‌خانه به لباس فروشی!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/665648" target="_blank">📅 17:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف مرگبار در تایلند
🔹
رانندگی یک پسربچه ۱۱ ساله با خودروی وانت والدینش در استان «موک‌داهان» تایلند، به فاجعه‌ای انسانی منجر شد و جان ۹ راهب بودایی را گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665647" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
امتحانات نهایی روز شنبه ۲۰ تیرماه در سراسر کشور لغو شد
سلطانی، مدیرکل آموزش و پرورش خراسان رضوی:
🔹
با توجه به تداخل آزمون نهایی با تشییع و تدفین رهبر شهید در مشهد و اینکه اولین آزمون نهایی مربوط به پایه یازدهم است، طبق آخرین ابلاغیه آموزش و پرورش، روز شنبه ۲۰ تیرماه آزمون نهایی در سراسر کشور برگزار نخواهد شد./ اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
🇮🇷
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665646" target="_blank">📅 17:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت آموزش و پرورش: مهر ۱۴۰۵ بدون کمبود معلم آغاز می‌شود.
🔹
وزارت بهداشت سوریه از افزایش تعداد قربانیان انفجار دمشق به ۵ کشته و ۱۶ زخمی خبر داد.
🔹
والیبال انتخابی آسیا؛ دختران زیر ۱۸ سال ایران مغلوب اندونزی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665645" target="_blank">📅 17:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et-iA67UTW4g5iJ2y-m2wpX4f77KpOUuKX24nuu1H_zGkDhm2mVaJaQjTE1ct5gLwPt1Ivd3LbdkvnXkTaQ8pPetQczjyaCAb3fZrv0szxs5JCkxYAhGf6m8ph-6mvUbyCTvgwRjfhyQG3AG4vt8OECVrrxLhUXUgGvActGVXXh5afxCsDbRLUAazxlVpKmWPB4_1_1KqfQEGlPoxQboqM9WI7RpR4E6iG5stQ_utxuXPYR7-cIRcsOqDOg02iFQoH05_vmYY0OrkkZQLqkxAgUZnqYQNwzQdkSDYZw5-3PpupfTkKAf00bCLN2ZwtJEbZoENN0HhzGPNMMkrVGobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ایالات متحده تاکنون بیش از هر کشور دیگری برای محافظت از ناتو هزینه کرده است، بدون اینکه هیچ سودی از این کار ببرد!
🔹
ایالات متحده ۹۹۹ میلیارد دلار، بریتانیا ۹۰.۵ میلیارد دلار، فرانسه ۶۶.۵ میلیارد دلار، ایتالیا ۴۸.۸ میلیارد دلار، لهستان ۴۴.۳ میلیارد دلار.
🔹
دیگر کشورها، از جمله آلمان، بسیار کمتر از این هستند. (۲۰۱۴-۲۰۲۵) مسخره است!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665644" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwNs1gMCu59vmQjutxZ-ppJ8BZB6bMvcfjlsycVGK8AffhLmSFmrq1ThFkmUJ_Ly4r323yhXWtDFybOTvnSyrZQrIbkQxfubmM_2KW_WZNVtZb-QuioO1VrjjiNxK3WWEdYhNEt1Jkey-ms7x35LGzb5rwKT2irRcyzOzAOCO8JRINwB-ArcXubGh7XceMTispy1XhyyOZEc4_mW0RqOOJSTMH5GKWQVQDWWrmEX-Grzs5kohv6KFKG5YWHdmx052qrGe2jfb43R57PJv94xRRvFtH2PD1u1jMmDyduWqG-UcpVpfpkoJKgjpBnh3bt1mMjVeMmoIoEjdPOM5bNxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها تاب‌آوری قابل‌قبولی در حملات سایبری داشتند
محمدصالح جوکار، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در شرایط فعلی، دشمن تلاش می‌کند با ایجاد نارضایتی عمومی، وحدت و انسجام داخلی را خدشه‌دار کند و در این زمینه دست به بزرگ‌نمایی مشکلات می‌زند و یکی از این موارد مانور تبلیغاتی بر حملات سایبری به بانک‌هاست.
🔹
مجلس موضوع دولت الکترونیک را مورد توجه قرار داده و بر توسعه زیرساخت‌های فناوری اطلاعات و ارتباطات در کشور به‌گونه‌ای که از ایمنی و پایداری لازم برخوردار باشند، تاکید کرده است.
🔹
برخی از بانک‌ها تاب‌آوری خوبی در حملات سایبری اخیر از خود نشان دادند. ارزیابی‌ها نشان می‌دهد که برخی از این سامانه‌ها همچنان نیازمند تقویت و به‌روزرسانی هستند که به زودی مرتفع خواهد شد‌.
🔹
در کنار مسئولیت بانک‌ها برای مدیریت چالش، حاکمیت نیز باید نظارت و راهبری موثر خود را در این حوزه اعمال کند زیرا این موضوع مستقیما با زندگی روزمره مردم، اقتصاد و نظام پرداخت کشور در ارتباط است.
🔹
اقدامات موثری در زمینه ارتقای امنیت سایبری در حال انجام است و این روند باید به‌صورت مستمر ادامه یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665643" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در مشهد ‌قطعی شد/ مبدا شروع مراسم بلوار فرودگاه تعیین شد
سخنگوی ستاد تشییع رهبر شهید انقلاب در خراسان‌رضوی:
🔹
‌پیکر مطهر رهبر شهید انقلاب و اعضای خانواده ایشان پس از برگزاری آیین‌های وداع و تشییع در شهرهای مقدس نجف و کربلا وارد مشهد خواهد شد و مراسم اصلی تشییع، بدرقه و وداع با آقای شهید ایران روز پنجشنبه هجدهم تیرماه برگزار می‌شود.
🔹
مبدا مراسم بلوار فرودگاه خواهد بود؛ مسیر تشییع تا حرم مطهر رضوی امتداد خواهد داشت و تمامی خیابان‌های اصلی منتهی به حرم نیز جزو مسیرهای رسمی مراسم هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/665642" target="_blank">📅 16:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/665641" target="_blank">📅 16:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار:
🔹
آزمون‌های نهایی طبق برنامه برگزار می‌شود. امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان سنجش اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665639" target="_blank">📅 16:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665637">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSsngudjH0HX4SFjHKVJvK0Z6veA_y27RDasbzRXSmCpMaIyIHLnrolCNFngNEm4gJgkl0AdYkJu5SKK-GtpKgZOdclr0SKhZjzYlnFhuGlGcLlgCkOIyeL8Y7zPCv_6maF8V9DaVpggWj-0nTVD_mBbWi9G5SWdjNCZ3IDt_aNqKqLz9I2z6N7jECX_WUFxXkAV8lybf3rpZqiGW4tEqnmJmfl6m4NfyXB8SexoMh_dxLZ4VL11WsZoNJpSz7A1x1uokacdwU-Xt7eAn00hRjeHHerjHzOHFlJBrIyV6pQLG9-6432i4QSu2j49Ee0DIoT-JhXxCYfEMLqsfHQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها در خط مقدم جنگ سایبری
جعفر قادری، نایب رییس کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
بانک‌ها اکنون در خط مقدم جنگ سایبری قرار دارند و این نشان می‌دهد که مراقبت ویژه‌ای باید از نظام بانکی صورت بگیرد.
🔹
اگر لازم باشد بانک‌ها باید برای بهبود وضعیت دفاعی و تاب‌آوری هر چه بهتر، مجوزهای لازم را برای استفاده از نیروهای متخصص دریافت کنند.
🔹
در ابتدای جنگ پدافندهای نظامی ما دچار مخاطرات شدند ولی با تقویت سامانه‌ها، چالش‌ها رفع شد و همان‌طور که چالش‌ها در این زمینه برطرف شد، در نظام بانکی هم با این چالش‌ها دارد به خوبی مقابله می‌شود تا به طور کامل برطرف شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665637" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665636">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
جنجال جدید در خانواده نتانیاهو؛ سارا نتانیاهو همسرش را در حضور اطرافیان تحقیر کرد
🔹
انتشار ویدئویی از برخورد تند سارا با بنیامین نتانیاهو، در استادیوم «تدی» قدس اشغالی، حاشیه‌ساز شد و بازخورد گسترده‌ای در شبکه‌های اجتماعی صهیونیست‌ها داشته است.
🔹
همسر نتانیاهو در این ویدئو با لحنی خشمگین به او می‌گوید: به خاطر تو مجبور شدم با دیگران بحث کنم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/665636" target="_blank">📅 16:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvQqzqRylVYXIyHolcBGKKJrGKkEjTrZqWjvy3TK3x8w4Nf5nrnB0qb2scBA-yhtKuCpP94j3fNckse8owaWMpPA3-LLzjqR6IQwOd6dxjBKW_qjWDjiLMrtW2DdVguF4PrwZjucQfQVQA9K7e9lK1xyou1WI0voDvd4ExBX2RrLd1WnbI6U3m2GU3hz5ll668F9xXtmH730m1k-vOddTCsznKTGGJDNM3FTsFoMKUFhiQFjSHxWmSJmp8KIH16NJbK8feFBnphbVPM4KpYjNpjZib9V4w-RmTB3y8JUVnHD8SCLUDQ80JUHScvV36G_4rwb8njO1CMA73DWkj204g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Qg0FWSeX_YOY_TWw5wkgLAnNFL16F2hngjl0mefn3OVSZZmsTk_nO0rZKne_RnH6M5-osukqdJUSU1kRgJrWlNQIw8PjQ9EiPpML45kVYHVPmnjoO92rnfF2XSIRzd4QCAz5ra-oho1ess7Zu56bb-lS8tmPrSVsfntx8T10lrk9uB8chp5_oqqH_emD4cGCanVr_3-RDKamKAGJoXrP-LoXRs6y7ihhU1byziSvW1iGMO8UIMXj66lbOkf4sDKO6WBfiACHDIjANxWtpJwybkltDmkrr2RhkS_72JYzYH0rsHz9iqVNw1zGbK6M0V7D9z1pPXdwbqlnEWtxjseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy5h5juBhgH3qMnMseeP0VRb_DXCIJ21DLioOo4LzgmcXRqXR4r8EzqT4WhrrlgIRBWHqF1PLIFn0176qkX8YrWIBdalgQv3nfSfV13WtcvtKilELPATPPJVBYQEGURPTRZIQXDcmEltTlXIaPHttsgKLMLzjs7tTzeVWrt1B46yPGx_yBDPtGd4EYYLtaRMhjymK8KiSKGarbln0LCkJFHrB1_UY9QTv4kQl33cr5lLSOFtGCXO-9iqYyhzxnyDOdh-tc0MtGyKhsXQym2KzuzXpDcBTqbtP5CtGC-I6dN99zdTTs1Pk0J084o1M5zNkHtsdbDj9UcfjustvvdgoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه چیز‌هایی از پول به کودکان‌مون در هر مرحله سنی یاد بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665633" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g24WmQl5kUVHBaYEWO6OtMybSMx3VDfIHU-YtKJnxu-YwBAFO1JGx4Et3kZPNGrMWn7MjcVT_45QBQs3VImkgyZerojyK9iQOj8iIaqbF7hFktoWfF7rVasLsb8zx0C9ItqbOqVU9WlLT1nlJjQYAmn7nT2KiQhRN0m0mLGfJrK9pBc43KWkSC1ntsogFmD_hrWKJbtq4KFdemEfs2qAkbVsKhKubSS7Z4kjRJsZMHJe6hnCKcTRaSHYhBofEOcCa_5nq1qpbfyzth6QYaUAj1dXeRr7Q-HwizjN4fOoJlZLcQNHh_2zdjmH15bqJ4OH1u_RER4FF-_Kho2e11YI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: در صورت تامین نشدن شروطمان توسط آمریکا، خریدها از مبادی دیگر انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665632" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECt97H-amaolhUBMt_vWAXKE1BTxdJDvgcttQ2g_yBCPjm2lIcvX4q4qevrM01kWFMHre8NYh6Pf49yy2v9rgiGjrVcqk9KGGQnrdB3XsWMLhx6DrWsNSuCje4qF087JvLHwlB6SF3VLJ25B2Ip8rLquiBrarz-pwnmeXRryjQSzGZySd82vhr7FSkObik4v2-6MzZ-kEZhJaaP94qbYVwgySbRS7Qz1nXPJ0-IPQuk7K4mdIZPzogMXKytgt1JgsOduZL-T3ih-bc_SI8sWiNr_e_F_YqpycrDPzr3cgDm62s_st3gheeYTAYMdWeQ-Aoab6-ez62RddwWZsw1gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از شباهت مزارع برنج به تابلوی آینه‌کاری در اثر انعکاس نور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665630" target="_blank">📅 16:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrwuwLaOVrx86h_5JuCmKjfDzZJlu0Ok6ofQMir7293IrOAgkKSWJ0YUpUcUG7f-EPHxhy8LhyN8ru0y-7zc-LFyKmZu1XQmjsZ63JgOaqXmVWrUJceSZCkk0cRl9EeFPHDyu23YWNhIz8DLOEyw6fJXgt-vCLT7VlelGv0wc8zQWUjtH8BCEihQf_V7b6kBEdClshDPCOBZoPDuAaMannDWgCqkwU8OmSXn15CjdVF0dvbl3g_LXtEG9CUfrhZ7oV3ZLXJLxO2u6E7zDV16jBtGFFx9s9SjBQypamvqPzjol40cJr0rzTvzKTHVmneErYGZYOUV5buvdxCRjk-MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل معروف به «بین دو بهشت»؛ پل ارتباطی دو استان کرمانشاه و کردستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/665626" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیس لاته انبه، نوشیدنی جذاب این فصل
🍹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665625" target="_blank">📅 16:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دقایقی پیش ٢ عضو گروهک تروریستی جیش‌العدل در زاهدان دستگیر شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665624" target="_blank">📅 16:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9uFb0R4WUbkty1ynTxTnJ7P-ztjm6W_kE9nG59FDPuwdyAzzqGXsI0RJEg3kz8I9vG2-QrdJjkbEaTHpOvb5crt6xAyEiNjQ6OxfrcKe-d-ru1Om_sgxORHNiaQ2LZWy5FG7Gw67GAbIyNIaWIHBUfLw-rk5rB-Jy0JM4PKOzHZPtZyAdtvhmgWFKXBrBnxshCx7mmPaguUYVVticRKCtEYABEGW7wMw9tp6XbI5HUPnAfATAo0XcyTbLD97l1qmI5bI67M2fkzTeDH15REoUCgBBdxJvOwGN62kOi8If1gsMVOh1tZ3mSP1Nf7NcAtqZ8PjQKwrel8XVLaVghohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راهنمای زائرشهر چهل‌سرا در جنوب مصلا
برای مراسم وداع با رهبر شهید انقلاب
🔹
استقرار مواکب پذیرایی، بیمارستان و آزمایشگاه سیار برکت در زائرشهر چهل‌سرا در ضلع جنوبی مصلا و خیابان بهشتی
🔹
تماس با سامانه تلفنی ۴۰۳۰ برای راهنمای مسیر، مراکز اسکان، درمان، ستاد گمشدگان و مشاوره روانشناسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665623" target="_blank">📅 15:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjGZqDUvS448HJjZzpjC51v0gbG4JquIPM7id3-590JpMSE54E9cq-q8tf0b5gy8r5gLIha3t46ceEvru9d8TQCW7suGhX3GRLjlWb_8PIXVXm9nDhj4Lv8RKV7e1RliV48vfbKutn6o-N2aAhf2E1miiabV65_OQ7RGz-V55NVXAViatRcKmFb3QDmZ_r1G8iPmIMueU7JQTRAv0a690iQ94yMWUAZlCHa39jRttJFJpFX4NIMGOg8yHZe45RyT5H8FVT0cSdlZnS4AOlZcg0BzqLhV2nsAxLtGvZJrN8V9ys8peaIr_Lp8dAhAdRd1KCH9bKi2yQ6M4mtHW6FKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رشدی ۱۵۳ درصدی سود خالص واسطه‌گری بانک اقتصادنوین
🔹
بانک اقتصاد نوین از ابتدای سال جاری تا پایان خرداد ماه موفق به کسب درآمدی معادل ۲۷۲.۱۵۷ میلیارد ریال از محل عملیات واسطه‌گری پولی شد.
🔻
اطلاعات بیشتر:
🔗
https://www.enbank.ir/s/mfa8De
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665622" target="_blank">📅 15:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسل جدید سینماها؛ تجربه‌ای خیره‌کننده که مرزهای تماشا را جابه‌جا می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665621" target="_blank">📅 15:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665620" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
صدور کارت سوخت‌المثنی ظرف ۲۴ ساعت
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران:
🔹
شرایط دریافت کارت سوخت المثنی به صورت یک روزه وجود دارد. اگر هموطنی کارت ندارد و درخواست دهد تا ۲۴ ساعت بعد کارت را میتواند دریافت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665619" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید ترامپ؛ دکتر ترامپ
🔹
ترامپ در شیرین‌کاری جدید خود با هوش مصنوعی، این بار در نقش پزشکی ظاهر شد که منتقدان سرشناسش را درمان می‌کند.
🔹
ویدئو با تصویری از ترامپ آغاز می‌شود که با لباس پزشک از مخاطبان می‌پرسد «آیا شما یا یکی از اطرافیانتان به سندرم ترامپ‌هراسی مبتلا شده‌اید؟» سپس می‌گوید «علائم این بیماری می‌تواند بی‌وقفه ادامه داشته باشد. خوشبختانه، من دکتر ترامپ هستم و برای آن یک برنامه درمانی دارم».
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665618" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود  صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665617" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲ قرارگاه برگزاری آیین وداع و تشییع قائد عظیم‌الشأن شهید امت (تهران)
🔹
هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند
🔹
مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچگونه منعی برای ورود وجود ندارد
🔹
زائران گرامی اخبار و اطلاعیه‌ها را از مراجع رسمی پیگیری کنند و به ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665615" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665614">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ClRF-hEi_gt82dWu7KZ8ESRszrR7eNInkmfTwkLe1gFJa6J5TwBjYgUfUNGvk3idkwJKPpvOv0bOZutpvC8bAiY2JecfY6mhAkM3LTOwCTx_Y6LLwWfvPVfEJb9QYYhA091eToDkAXFeSBvZprM-GfVe1GteKO7F5eNkWXavZP4WjCtJFG4KO4Wfl57ZCaSSTWBg83F93Uy0MG2tk-VmyWloC1OFhYj5kCOLoELGrB1j0KCVhvI6gDN6lf0gq4w5_OhhSOEF1dxgtZNM34rsJgG-48gxRTeeqgaZzh0pby9139OMfhebsvp-t80X3zpqsxMiB88EsejO5WKtziHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نفتکش‌ها از کریدور عمانی- آمریکایی با سامانه شناسایی روشن
موسسه تحقیقاتی HFI:
🔹
اسکورت آشکار کشتی‌ها تحت حفاظت آمریکا در حال انجام است. در این مدت، ۴ نفتکش غول‌پیکر (VLCC) با سامانه شناسایی خودکار روشن وارد تنگه شدند.
🔹
در سمت ایران، ورود نفتکش‌ها به مقصد بنادر ایران همچنان محدود است. تاکنون هیچ‌گونه تشدید تنشی از سوی سپاه پاسداران انقلاب اسلامی رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665614" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم فرانسوی‌ها بر تهیه پنکه و دستگاه‌های تهویه
🔹
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/665611" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl7JhEYsXGedy1mKQkD6MC_sm2tvYwdgFuWCt_6azQxgy1SOGmvmpi4HkQQK3_PV18IPrS3VxRhur4kGImlzjgzW7Jx3YPNw5_6F-ITZsPk5qbG-ooPdlaxYelhYMdwkVgt73siHRykUuQRWTu1DGOo0ANPkiP-CIRDASbN_CBCWDRlaHoeDpvN95oLh1FCWOtrO01qlQn71fnpa8br8VRVNrk8b8HUDSMkiNfpp8D1fprFa91d_s5aJcXtHdQB4Bvg0QBRjpUvQrOaB-xhZvG1PEB5S3Chvm3YH0qI-0Z32jNlajCOyB2_kvdX9LEF-RNQkQDZ7khgUwsYbGxqG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفکیک زباله از مبدأ؛ اولین گام برای ساختن شهری پاک  شما هم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665610" target="_blank">📅 15:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665609">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfpH6oy_dHKcZuis4vjyXVvctfGNNJxp2CtIEc-RvxmJdVzI0hWaoYo7_rcEBFVowx9I463jOstPGsBqBjpv5zXU4-NydKP6Lk2b3J4-U42JP1Mm640XnzYMlZ7HCJaLeU8WQAVqs9myFDh3SujArRWmf--f0IgkEc0Dql54bgilKoqE2CehbK_7yKJ8ZYy0Bd_MRi9AJ0S8LKT5zK1Q3xo_mBf4wv7y_foaWyvbgLl5NJDi9S1VA8LekAvQQ-mzIVVnbXa71GvJpwlLmDqRxrv6zZrWmchgCjpU-XCe532PZYzQgJ2bW3YpYIVcqfo-VRa6P1Bs40_rFZi_oP04Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست مهدی طارمی در واکنش به حذف ایران از جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665609" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665608">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONagQjOwUWsd_rd5gKS2wFnmgvp5mZK1unyWu-VJ9hKJS2GBfD_ob0tJlJRxvQjbSZOq2Je4XJ7cJAN4kSxowXozuJlCU1uKQWe0KHIiKUvVdGeasfU48TZJ4_mjNqtkYMKgLIIiVrdMHHomhWzvktrngvl7Nuz2bAZn9dGsbBNosqUmdUyiCIPpBkLmEp6dk1-jM4nrwQnXSwYFCh5tANZdR2A3sNU1fyDVVBDtPuitq4n0xdRP68rRbNZplvQ_wsa-rdsMtz7vYeKjGLxdZ3jt-OokV0EzRDrDrWe2Q73YJyjlXhDL3EBYpu3VZpmPryUmRAOZ3m5GtiTx4VbXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
با حضور متخصصان اکوسیستم نوآوری و به همت بانک مهر ایران
🔰
نخستین رویداد کیوتاک با موضوع تجارت اجتماعی برگزار می‌شود
🔸
سلسله نشست‌های کیوتاک به همت بانک قرض‌الحسنه مهر ایران آغاز شد و نخستین رویداد، روز پنجشنبه ۲۵ تیر ماه از ساعت ۹ تا ۱۵ با حضور متخصصان اکوسیستم نوآوری و بانکی برگزار می‌شود.
🔸
موضوع نشست نخست، تجارت اجتماعی و شبکه بانکی است و در این نشست راهکارهای نوین بانکی در توسعه اکوسیستم تجارت اجتماعی بررسی می‌شود.
🔸
بررسی وضعیت تجارت اجتماعی در ایران، ابزارهای پرداخت نوین در تجارت اجتماعی، تجربیات جهانی و مطالعات موردی و چالش‌های پذیرش ابزارهای پرداخت از جمله محورهای این رویداد است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665608" target="_blank">📅 14:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665607">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خون شهدا با پول شسته نمی‌شود/ ایستاده‌ایم هم برای قصاص، هم برای انتقام
دکتر محسن خاکی، استاد حوزه و دانشگاه:
🔹
ایرانی شیعه‌ قدرتمند امروز خون رهبر شهید را فراموش نخواهد کرد. خون ماکان نصیری و سعید زارعی افسر ناو گروه دنا و خون رهبر قیمت ندارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665607" target="_blank">📅 14:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665606">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdtQnjoq--7nPbyZ9j42XAiwkQf1mdOr8HCmecOawe8oAXFU4UaSasTOHOACupl2tF7P00sPWYZzC_TU6ImCjg6oR14ksLmfB7tMkri82_fileHq7RcV0SQx3g9mlkxUPfqWAkL0v5fTCMLUXdU7nvsxQFjB2tjaa8ouNQMHT5WVIK0PP7Wzb5TUiQIn-QbSGljjNRiVlPcn2FOMr9Zog8_FU285EDCGqHkWLhgVSFIIh0VrfegJKo74OL4r_uk22iIKmoJI2KqgWHzGCamdvfkLX3TB9-zZiCDtHQnaWs51N8qls9dVWyKzKzQe42G1Jm6OP5Dx6K-6W9IGPzrqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
عکس
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665606" target="_blank">📅 14:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665605">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDuvOJsjiZMa2RUtkN9h4BWHpID8zl4wkMpwUpSFcIJWTOWkb2Udm17W7iWbUiN7CiTdOy7LEShgBRFkyMUz9KnGtZP0HTmeEkcfAaO2kZEgkvaO8alohPS8UXiGXDgDG5nCP1NebBPCq0VKqPOURlflKs4fqMTrO7114qsjFUz2LapXW0xuq9k9JIaSDz3KAOoYLZBEcTyOceWfopFzeZ1Y81A6id5ecRl0rHRRC9VnOaGK3-kl6dNvBUszeutsT74LscOaENQs_uFGIEJ1Pnrk3_oU6l6B8Y-fMwCMBhi6TByN0LbJAI-G6b3Y8BWPJny_6p4u7qXH6w9t1eIMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بلاگر معروف کره‌ای به مراسم بدرقه رهبر شهید انقلاب
قهرمان هرگز نمی‌میرد
🔹
«داود کیم» (جیهان)، بلاگر شناخته‌ شده کره‌ای، استوری ادیورز ویژه‌ای را به مناسبت مراسم تشییع رهبر انقلاب منتشر کرد.
🔹
این چهره بین‌المللی که سال گذشته با انتشار ادیورز پربازدید «قهرمان» (HERO) در ایام عاشورا توجه جهانیان را جلب کرده بود، حالا در جریان این مراسم تاریخی، بار دیگر با اقدامی رسانه‌ای ادای احترام خود را به نمایش گذاشت.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665605" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665604">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
جزئیات تشییع پیکر رهبر شهید در نجف و کربلا
اباذری ، رایزن فرهنگی ایران در عراق:
🔹
پیکر مطهر رهبر شهید شامگاه سه‌شنبه ۱۶ تیر وارد فرودگاه نجف خواهد شد و پس از مراسم استقبال رسمی با حضور مقامات عراق، صبح چهارشنبه ۱۷ تیر از ساعت ۶ صبح در نجف (از مسیر کوفه به‌سمت میدان ثورة‌العشرین) و عصر همان‌روز از ساعت ۱۶ در کربلا (از خیابان ابومهدی المهندس به‌سمت بین‌الحرمین) تشییع می‌شود.
🔹
طواف پیکر مطهر در حرم‌های امیرالمؤمنین(ع)، امام حسین(ع) و حضرت عباس(ع) و برگزاری آیین‌های معنوی نیز پیش‌بینی‌شده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665604" target="_blank">📅 14:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665603">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-text">📹
محمدمتین تنها ۱۸ ماه دارد.
خشونت، سلامتی او را گرفت و امروز برای ادامه درمان و توانبخشی، به همراهی ما نیاز دارد. مهرآفرین تاکنون در کنار او بوده، اما مسیر درمانش هنوز ادامه دارد.
❤️
پنجشنبه مهرورزی این هفته، برای درمان کودکانی است که قربانی خشونت و کودک‌آزاری شده‌اند.
🌿
نگذاریم فقر، فرصت درمانشان را هم بگیرد.
💳
6104337737614782
💳
6037707000289144
💳
6037707000426027
🔖
IR 180120000000001264298063
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
🤍
عزیزانی که مایل‌اند به‌صورت مستقیم به محمدمتین کمک کنند، در واتساپ یا تلگرام به شماره زیر پیام بگذارند:
📲
+989101785282
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665603" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iURQGwXXqTxYguNTkJX27bkB-RMTlTG6iq2Tx6-RGYRvySH5EwP0XL_xFxGZUp2gNi-PM0fdjgwp08N3QHDjvJqP31ZIELPkFViqdxi-lRpw3FHFLCdL94R9mkPs1X1E9JLvwxaDs3LDUVofMdJuwk0bUDjIvpjI049F2hwuAwk-Dq3IaW1A1JHV_OHfEW13FLQN7mPx8El7HjJLHsmOS9-tygDijHfhXXPlZIKAZGvLOyKDQAhc9YU1duujTlS9qLWt_7eyBFb4muq5PWV2rlTDdH3QNFWYvM2fCEQt_-9t3b3IcgOdm08GmZIRKwyN0nCYNMU7y7_vMUbpcz6P9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای جامع مسیرهای ورودی، پارکینگ‌ها و دسترسی به مراسم وداع در مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665601" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
استاندار تهران: ورود خودرو و موتورسیکلت تا شعاع ۱.۵ کیلومتری مصلی ممنوع است/ خارج از این رینگ، تردد خودرو آزاد است اما توقف ممنوع است
🔹
برای تردد خودروها در مبادی ورودی تهران، با توجه به اقتضائات و شرایط موجود، تصمیم‌گیری خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/665600" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود
صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665599" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyDd61n3oNWC3fYvD3_W-xUx691slzmPXm2BxO9nq5oKko8rJWEEc4A84PQp7OuSD2H13F7hUzS_scYw0r8B73vitwJ6eLmkB0wCyWUInIUEAmZdKOgXQfqg6yxoOzZDPu2fi_9-rldYjzXTm2BflvhL70zFTiiIjvzjjaGb5GxbM5KpCLalSB9iQ33QgnBK-os4ZgYOricesNILI1fL7042qiGU0M9SDnbsfwgClrzNxuEhlazI-91rkfZU48Pm734WJFONrQv2WcM-dteBkwacHN0msfkHGU1Vo0KcZKSG0pfBkEQb6BScwUkJF1QeR4USV4imNuziHBzgv_LSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعی برق؛ هزینه ای که مردم می‌پردازند  #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665598" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGWAJKVFCIW1RopgjHOWCvxhiB2eb1Hm6KO61kWzLKGSbPzTem2FNQZzUjipIhEqqZ3w8TIPalX_JLCkQQlPHBAxQaATZ9z9J4R0woKeXuxmR6lhycWpKL0iVtI3VPpYT8Sx3c1N4LfwTRXzgnlCuP6Dzq5O7BCqn_qSGvJFR9PBtP-ah6Rk3rbhtfsRxRL1rbWUrJsc_46_5rAdr3bD-E5_oM4S-KSYyCR0U3ZUN95dgy5T1COKgWJhNa8BHHQp6bOrRGYIFrTkOowL4G9GocdSK8jwN8JUbE3SiBdrQJqU_5rlNKS_YQX1soUf6HSN8493ZHSfN_PURwBfzed8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/665597" target="_blank">📅 14:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAQ56V3znDLlP2yrHqn1zQCqf0AAWW8eGX9flGhWoQlwDB_m3He4ldV__y-9YTgn5F3kjt4eUYpsvA7wDp2JV_FXLKC6fnYRVPCKqerpk8jZzUqxqd864Tk2wLdC_CwB7G-7LBkjyZfwW0Xf_1KdFLag2z5aarAPIGvXYq9aUeuWn1s2HWDcw3nE4agUvxHGjjC82uexXceaFvrsZYcxNsk5SyUi2lwpTkwK1JRi-MkD21gLNM9Xl1cliEvCG1efjAn50B-OUO4VBdgGeyXKjYEPX3FZFA72qqnAA36MqGAjuxDYfOJo3YAXt2M4FZZ0z-pJDQ_RWIlMQvq2CkpDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین گزینه‌ها برای یک سفر ۳ روزه در ایران
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665596" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل چهارم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ خانم زهره ابراهیمی را که بعد از ورود به برزخ و دیدار و درک جایگاه خویشاوندان و حتی جنینی که خواهر ایشان محسوب می‌شد؛ به دلیل داشتن فرزند از خداوند بازگشت به دنیا را طلب می‌کنند و با عبور از میان اجرام آسمانی و درک زیبایی‌های بی‌نظیر آنها به جسم باز می‌گردد ولی از بازگشت پشیمان و دلگیر می‌شوند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زهره ابراهیمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665595" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665594">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXVE49f5lmNiL2MbGzoeWt8R6myWq4g3a0zfz6DZ2A877sh5-JzCvg2xmdEPxAOKtRiiStOQBOJwVUCw0Qj_8GiwlMOgVTCDk8PZlf2aEqGrS5lg-PWwkDIYY8wP0h7EIQQcCQIATfAUrKhtwV575lJUWdeo6Ln6n8y1Lz6AwbjTokcHMuRJi9-HLRS9LPa6FUEvI0pmkBTdChcMmKjsA9eNEh3iDxxKurpAni_HQNhY82ypRk0tLdCIZ-SrxVmyRk1i3FQKxgcr6W-h2FqUkpJB1Qpm1WAg2X47Od1JRIAZffl1X-cWT0Rf6k0oV2QJ4d7V3ekaJxtShUq3XOwZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت ۳۰۰ میلیون دلاری به شرکت‌های دانش‌بنیان
🔹
برآورد اولیه خسارت واردشده به شرکت‌های دانش‌بنیان حدود ۳۰۰ میلیون دلار اعلام شد.
🔹
بازسازی شرکت‌های آسیب‌دیده در ۳ مرحله و با تأمین تسهیلات دولتی انجام خواهد شد.
@amarfact</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/665594" target="_blank">📅 13:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک منبع عالی‌رتبه به العربیة: دور بعدی مذاکرات ایران و آمریکا در ۱۸ جولای (۲۷ تیر) برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/665592" target="_blank">📅 13:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان چفیه‌ رهبری
🔹
خانمی‌ که رهبری را قبول نداشت اما حالا میزبان و خادم زائران و وداع کنندگان با رهبر شهید است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/665591" target="_blank">📅 13:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محله به محله خود را آماده میزبانی از مهمانان رهبر شهید می‌کنند
🔹
سهم ما در میزبانی از زائران و وداع کنندگان با رهبر شهید چیست؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/665589" target="_blank">📅 13:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyENBaQkUf5z1LROTBFPLF7UmLS9Q5qbiDl4ciQf557gEZLgv_bkv2FrzIhnjTmmwtqw9JpTsFWp7GcuJiLtY3jlDiwqdefncgyC2iYlsrUnrqeZr8kEhjosY0fwTEKYqxY3c2st6m4N_kxY_u5CxucbbzJ7nwFsVrd3Aupxp9XiB4HjI7zTyypt5mTd8xk-_jRAz4KQZYC1rsqnzj4wcT97IzkmQnEAE5_OeW5uk_jnRImttOc3xpRy47RTHr2Pmu2bFmS4VFsNatss7VFv6sVIGBzxCfGG2iOtC8NW-U78Hmsz5Jd0sD4Z3kOqLnnSsUCe8UW-hCZzCnDfQIP8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قتل دختر شایسته ایران در ۷۲ سالگی/ قاتل ریتا جبلی در ارومیه کارمند بانک است
🔹
پس از انتشار خبر قتل یک زن ۷۳ ساله در ارومیه و اعلام دستگیری قاتل از سوی پلیس، اکنون جزئیات تازه‌ای درباره هویت مقتول و انگیزه این جنایت منتشر شده است.
🔹
هرچند بخشی از این اطلاعات در صفحات غیررسمی شبکه‌های اجتماعی منتشر شده و هنوز به تأیید رسمی نرسیده است.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/665587" target="_blank">📅 13:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از شنبه در تهران
استاندار تهران:
🔹
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از روز شنبه در تهران آغاز می‌شود و پایتخت میزبان زائران از سراسر کشور خواهد بود.
🔹
مراسم اصلی در روز دوشنبه ۱۵ تیر برگزار خواهد شد. تمهیدات گسترده برای ساماندهی حضور جمعیت انجام شده است.
🔹
امنیت کامل مراسم با مشارکت نیروهای نظامی، انتظامی و امنیتی تأمین شده و زیرساخت‌های تهران تقویت شده است.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665586" target="_blank">📅 13:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیوارهای تهران هم این روزها داغدار هستند
باید برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/665584" target="_blank">📅 13:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665581">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB62ds73BPlRcjZkFjYlhhFGoNqX-nKfAzdwcdzUBCpcMi1QzAWDZ9nzd5iiV3L-0VsySGDodeZDZFojmj0eFoeBETNVHn2d5frUgJqQjIXWt6G3-UwUm2bp-eOYFWVDyH1B3wFKLTC5KqtMoRiOBH8H-5j8JV5Tbt9xIfqPqekGZ4brRAE0prCRDT17f1pry9PMQogHbI28xiychUK17F0TebBMSdlo3Kv0BBJU9xu7qRFnDZj9x-2q4ghdC77MSBItxvq5eFgg1-_f9LIGXfEJM2k2fnx9k7is8fo8mSs_3Uj1J0GZWIUqnOa3e8vIQVaP6bn0f2MAViC5h98lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لیوان نوشابه؛ ۱۳ دقیقه از عمر شما کم می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/665581" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونالدو از پنجره هتل محل اقامت تیم پرتغال، طرفدارانش را غافلگیر کرد و برای آن‌ها دست تکان داد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/665578" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دیشب جام جهانی ثابت کرد تا سوت آخر، هیچ نتیجه‌ای قطعی نیست!
▪️
قسمت یازدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/665577" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا Svalbard نروژه؛ جاییکه خورشید هیچ وقت طلوع نمی‌کنه
🌘
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/665575" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc47TjaU9JWAQOdL6OZBv1tmTo55U0nBlRLG629-RZ1dt6WoZ6mR7no0fSWyXpnRpV1V9nHGN-yn9EzIlCAok2JUiCQ3ICDFn-g2ucqarl8Sl_XXwnDE6mXyAjtmws0qj3wo-BY2irRXi4I43ynPP_Qb2jzPNjQXhQKRv39BEtIobtz5N4xh3QvzDRmjMMop_7hsfdJi-rZ4NyCtUOE73eki3et9jZ9rXbfuyz70QnXE_dE3pMt8T9BRMP3SxrMbhvPK6A5fIXUzmaCDII3hDLvnVcEQqp8IirB4-kkRSwb_koxvyKfFjZTKO4UpooRTdo3GxEfOpjA1O4L_jyccnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه در صدر رقابت کفش طلای جام جهانی ۲۰۲۶
🔹
کیلیان امباپه با شش گل و دو پاس گل در صدر جدول گلزنان جام جهانی ۲۰۲۶ قرار گرفت و در رقابت برای کسب کفش طلا از لیونل مسی پیشی گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/665574" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665571">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/665571" target="_blank">📅 12:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665570">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsOFwYL9lBJxN_h79m24IcDiOjGm5nhnhZAlC3RxH-VZpilLp2sljbl1OIoF4Hhy8t3v5N6cOLMOMcqOdW8bCibVHR6Hsx8rPui-HobPs_14J3eytIHfwb1jSf-_4FFFlWX0BrzOFtcw-KwPyR_2GBu05Y6ayOz9zRwHZhQza49CChM4LwxeJkFy7NS3oN7geRSDI8koqYfuf5PaGTXgCorObDl1-mDtjhtxMy33H5sP2XgUV16zGOZvAClAqsC7MA4M1SMkDfI81HqqPyAim_mIWHcnjJmd-RiBnxup0AlmwbEOaXFvzHv6RTX5WD7knIP7JeA82aDOp1poYvqrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه رسانه‌ها ذهن ما را تحت تأثیر قرار می‌دهند؟ با این مهارت، قربانی اخبار جعلی نشوید #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/665570" target="_blank">📅 12:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌شود نروید؟
🔹
۱۳، ۱۴ و ۱۵ تیرماه، آخرین دیدار مردم پایتخت با آقای شهید ایران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/665567" target="_blank">📅 11:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر درباره کولر ماشین سوال دارید، این ویدیو رو از دست ندین!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665566" target="_blank">📅 11:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKXcS9tdKGYrlEJI8SMmzRMk-aVV9_Pogis_Jru07UYNMczwk0PmgHAInlrS6OHYYHil1rX9TUTkwPKRF6fEAnj4lr1T38h8CjmH41So6eINiMpAOXIVT531UfXrdvO0IQmMk-NDDVbcn3K6kadg4SmU71HmwoJiMwhI-mU8JzIG69qChqQBV-VKepHmcgwoLgsHjIWfPzWS-A_uii5Ek-3M0ajPeq6hv1KujnMjF0Yxsv9farAeOslWCeyMWjZ0PhP1Y4M-o_6iTGZNJWr_vblQINB-sAb1w9PYA53ofO6iPPHFM4EAA5ogsTDCxYJhZIjokgFeIZQS1UBA8tp0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی وضعیت جوی مراسم تشییع رهبر شهید در تهران، قم و مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665565" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpswb5snk_zGM7_6rbZEddzVGFMlnQLDj1CPffpCwBN7WYMWOcx1q2_1LvVxTPuqrLMTnJtq4tZQ8_FvoOtbSkkYOag9n6ETmOhB_Dkv6t_m0g6Ip2PkqcAcU0R1GKFJDmR8PcqJ2-AqqWQD90P8shb4IsrsR-Bg7213-GUJnX5XhLp18_sbLP0Wr84y6lKXIJgKqKIw1tAe6qvdm_Rir3pen30K1XkplOEMgA08Uyt7XeyTRawWjxNq9ZvrPPChP9WHgGak8wxhgO3LfMbFYRkI1drseZ5KTPNRHHFYJur8ZecpW4Bu70xYrJPDseVwnvZ4LI1SkmFM8whFznSMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز ۱۱ نوع چنگال که نمی‌دانستید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/665563" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
مجموعه «چهارباغ» به فضای جدید وداع زائران در شمال مصلای تهران تبدیل شد
گودرزی, معاون خدمات شهری و محیط‌زیست شهرداری تهران:
🔹
این مجموعه که قرار بود به‌عنوان بوستانی متصل به مصلی برای نمازهای جمعه و عید فطر مورد استفاده قرار گیرد، اکنون با تلاش جهادی به فضایی برای وداع مردم با پیکر مطهر رهبر شهید انقلاب اسلامی تبدیل شده است.
🔹
با توجه به پیش‌بینی حضور گسترده مردم، مجموعه چهارباغ به گونه‌ای آماده شده که زائران بتوانند بدون ورود به صحن اصلی مصلی نیز مراسم وداع را انجام دهند.
🔹
همچنین مسیرهای دسترسی از بزرگراه شهید همت، پل روی بزرگراه شهید سلیمانی و ورودی‌های شمالی مصلی برای تسهیل تردد و کاهش ازدحام جمعیت پیش‌بینی و آماده‌سازی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665562" target="_blank">📅 11:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱٠٠ کیلو طلا؛
جایزه ورامینی‌ها برای قتل ترامپ و نتانیاهو
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665561" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازرسی بدنی «لیونل مسی» توسط آمریکایی‌ها روی باند فرودگاه و خنده‌های ستاره آرژانتینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/665560" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665559">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/665559" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpcJU30JW9TcyPaKTVXs7SGT9jtO_ajdGwp7sCjCjCuNN9lhbmmSI-YJG8E6LMkgJ-sjh06kQR7THczMiS7YB3bMp9vMRhCk8uXdlKXsI9p_N_xY_6m2AQCw6ZfWQOnCg5LT-CrrqHcIMKpQeunwkDRiK_112V_JtZkPhKl-byb2SYXLxPH46UerNHvSe5zX25wmd-pkihgmi6B3oX5vZp0N_b7dsez0JnZEHREO6CppXJ3OzYC0vArXijd1m7g6ZnRHfFenSPiOqH91zCD-vu89b2rQCk1lB7qccd4Hf6s30JVqBG-B4mNgochVrOJsb_ySWycF-Qsc7896-v9hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی دیدار ایران و مصر در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/665558" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665557">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مهلت بهره‌مندی از معافیت سه فرزندی و بیشتر تا پایان سال ۱۴۰۷ تمدید شد
فراجا:
🔹
همه مشمولان دارای سه فرزند و بیشتر که تا پایان سال ۱۴۰۷ واجد شرایط معافیت هستند می‌توانند با مراجعه به دفاتر پلیس+۱۰ ازاین معافیت بهره مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665557" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JblaX62A-76SkeHAB991yXlHZ7kimX9TE6YgT4kwSqbOocGDV0B2VMCaU3inIvmqDczaU7nHTUhzfgUwmc36uSAUzWPnpAESkvJHfja4ecbXNC0SUxCBdjx1mg8GqoPztMREf6M5-3FrYnMKT-Wi6fsYTd1q5cRY4T8OfCYna19LfdMkI0n_T41OPBpyrG13OTS_qhZugH4G_QGeRq2FEIeawRk6u5ziQv-sdLkXms74SMAUaoDV1oXemMerFpay8FbMCfOwZoEEagMBhk0AfR0-I0w47oYyhtyGPlWqcWhwNcFWAyeOHJgTVO0ALUApk86UL7L1ViglOdnUKqrqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCoDsJnbe2lYEZupsiXaKUwZKx5RZBFhPikXOgmBZQLtdvWI-BwL8JnMGcXQyII63ya6A-xu14y9Mp-ii454qMAlEynw6PMgiSGnI2_TSFqk02aBL7-vobjVUnl8oip15CiOmkpf__nGm4zKOCp30Q_1KKsysUTHUBDSms5Hj-I4tB31rSdCsiPmzsbu6FaqgDUrKnqHnHii6pOm2baRkMRCU5Q1zUj2tNsDIB5Z3InmJljUc6gXyqmg30VHzinLy2o6UaQ1WDMc3Tl6dkBJq6a2XehTKMMu_7uAXaD9XDCnUnoD59xdW0RnkrZjh3YP2GDvWR0djY256QTNkjoItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۹ درصد خانوارهای ایران مستأجرند
🔹
حدود ۵.۳ میلیون خانوار (نزدیک به ۱۷.۵ میلیون نفر) در کشور مستأجر هستند.
🔹
تهران (۳۱٪)، قم (۲۸٪) و البرز (۲۷٪) بیشترین و هرمزگان (۸٪)، آذربایجان شرقی (۱۰٪) و گلستان (۱۱٪) کمترین نرخ اجاره‌نشینی را دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/665555" target="_blank">📅 10:45 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
