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
<img src="https://cdn4.telesco.pe/file/GCnh-bCLnt0Wqg2N7c1X17BohsVdYaVSj7or_mjxLFuS6ZBRCd9pEM-yeb5lwZupsLKjS2Fm_IbVhY8xylyHe5TZVFgPsr7ijObyMjsMHtUFRTZa2QD20b4IqWC4ACrBj0X5AO15Ag38Nt1M9VALkCIJTUulDTN4OiTQAtfCEJ3NjyNxka_Nx8YXTYAFsTxolJzpgtWXdmxqzHAsk8e7pnsBtg53kQKTv1T36oSzirGAo40cUBOh1FV6o58Lc3Ck_Fgd-rrRnkF4liJv1Ig767xZ1IafbLqOzJDi1C9HSTJdXn9hdN87cOdMca9X_ozUl4yX01RknuhowxrEoyIB5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-690577">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وزارت خارجه سوئد در راستای اعلام حمایت خود از اسرائیل، یکی از کارمندان سفارت ایران در استکهلم را اخراج کرده و سفیر ایران را نیز به وزارت خارجه احضار کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/690577" target="_blank">📅 13:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58fb01550.mp4?token=bqXaBjUIGSozjMYZHbG3bo-vKZ4vR3o0n4_HENrOZPme9GtY44eGdyR8DJBol1s8_OPZTyCFAXXB3f2nJ5QSyQvPRwK_tjkjrWqDF1MHvEAEhkCcFE3orQkeZI_feDzcJimvvNy6lAVpSrqeRGgkcy5hQY86RZuZg8bEUqVRUdXMXPRE84kpJWEpNTxq91JROdc3qXoIhNum4GjJa33i5fSUQaLXRZS-qkXurQ4pTSjR3enZBH-o5T5e7V1VQcygszjljqkJANnD92CxwADxa6oUDF27i4HqmY1IiCl78EdnHQSSQBFTmcTAEMtbku7AJa0yHsk76fMkaRcSyNgagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58fb01550.mp4?token=bqXaBjUIGSozjMYZHbG3bo-vKZ4vR3o0n4_HENrOZPme9GtY44eGdyR8DJBol1s8_OPZTyCFAXXB3f2nJ5QSyQvPRwK_tjkjrWqDF1MHvEAEhkCcFE3orQkeZI_feDzcJimvvNy6lAVpSrqeRGgkcy5hQY86RZuZg8bEUqVRUdXMXPRE84kpJWEpNTxq91JROdc3qXoIhNum4GjJa33i5fSUQaLXRZS-qkXurQ4pTSjR3enZBH-o5T5e7V1VQcygszjljqkJANnD92CxwADxa6oUDF27i4HqmY1IiCl78EdnHQSSQBFTmcTAEMtbku7AJa0yHsk76fMkaRcSyNgagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپی‌برداری از پهپاد شاهد ایرانی به مکزیک رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/690576" target="_blank">📅 13:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690575">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbff5dc1db.mp4?token=iVVJafNLG_PoS_Fn9CPZDM_DYBQXRDYSrKOzDz9ZHAe-hluWvB5Hi4a0s2bazX3pKnuBLDcE1hcw6I6yKfuSMb1t7J-UJd9zd93n0TotKM9DT3kApblld21kA2soi-kNAAAwXvwhoBAz0AwOR1uPEa7LTqenpSWFAC_oI8y2sZKRc-liVh5YPPLVAlRmO2LXR5uCF8zUm3w2-gyDdIUgIXgPMqVmLA-wIsybaywoy1CTDJCqmjo_Fq1b5Sk1x1D3z4ouj3DJ7UmKZeWNcOGnr7XIED2Gw6ajGrJJvlvYCzztBRyi2wiB3mjjNK3cr0Opo_XvLMebx2iFa2rcNUjxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbff5dc1db.mp4?token=iVVJafNLG_PoS_Fn9CPZDM_DYBQXRDYSrKOzDz9ZHAe-hluWvB5Hi4a0s2bazX3pKnuBLDcE1hcw6I6yKfuSMb1t7J-UJd9zd93n0TotKM9DT3kApblld21kA2soi-kNAAAwXvwhoBAz0AwOR1uPEa7LTqenpSWFAC_oI8y2sZKRc-liVh5YPPLVAlRmO2LXR5uCF8zUm3w2-gyDdIUgIXgPMqVmLA-wIsybaywoy1CTDJCqmjo_Fq1b5Sk1x1D3z4ouj3DJ7UmKZeWNcOGnr7XIED2Gw6ajGrJJvlvYCzztBRyi2wiB3mjjNK3cr0Opo_XvLMebx2iFa2rcNUjxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطمئنم نمیدونستید با این ترفند میتونید سرعت موبایلتان را چند برابر کنید
#ترفند_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/akhbarefori/690575" target="_blank">📅 12:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690574">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa946db76.mp4?token=DtukdcOQLQMJNPrucMkcd8M5SwfrTIRqFfLnzQt-JqbahrAfJaLVJrw566GSRjU_g0RSHb76SOXrggYnca1xb34bbX5IGHSaNP5L_O8yakHVHR4UPelJX5SMlt0gK_4bfAuqTSLaegtFufvMR2OFqQWh_SVKtInge1ljTLFT7K26E0hE6m8hjJ6Z3LoyO1nvkmsEH-Z2d4hzLmh69ob6bL-iDDYfmdRoBFFoGDud2_BgAJkTF40Ow5FO-IND--E0OIDPyIwpnMweHNeuoBVqMMUxqaqZrAH6NgGD66aeyHuKr3cYUqozDBChCAKoW9YZXZ8VEA0OgOWYAL0HDKOOdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa946db76.mp4?token=DtukdcOQLQMJNPrucMkcd8M5SwfrTIRqFfLnzQt-JqbahrAfJaLVJrw566GSRjU_g0RSHb76SOXrggYnca1xb34bbX5IGHSaNP5L_O8yakHVHR4UPelJX5SMlt0gK_4bfAuqTSLaegtFufvMR2OFqQWh_SVKtInge1ljTLFT7K26E0hE6m8hjJ6Z3LoyO1nvkmsEH-Z2d4hzLmh69ob6bL-iDDYfmdRoBFFoGDud2_BgAJkTF40Ow5FO-IND--E0OIDPyIwpnMweHNeuoBVqMMUxqaqZrAH6NgGD66aeyHuKr3cYUqozDBChCAKoW9YZXZ8VEA0OgOWYAL0HDKOOdYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهای خوش شریعتمداری به سهامداران در مجمع فارس
🔹
از رشد ۴۸ درصدی سود خالص فارس تا تکمیل پروژه‌های نیمه تمام و افزایش سرمایه ۷۵ همتی در آینده نزدیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/690574" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690573">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ‌جنایتکار: اگر پیروز شویم، به هر یک از شما ۵۰۰۰ دلار خواهیم داد. این تمام ماجراست، خیلی ساده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/690573" target="_blank">📅 12:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf87199f71.mp4?token=A15KQnd6LNZIdrjC5X5M1dszNJPpJ39zGD-NQ4JiCLMq2g3BrDjvjvkZTtwbo4BMY1gOTvOiNAGwqmyRB-FnAKNY1SwfMVuHvO2_PefT38vheKbOUElz19Ci7quVupymXvd7csYY8s-A_Wmyv57Ahwsfyg3yyxcmX5nXC8tBfYw6onuPElPf4YlO6bVxrwuZJiPaEBpEWC7w4cAn7CPRcYxXHdQCogMzcacgztNDj4rl3CoBNbF8dCgfWvrJIDN_DLVgq3LcmP43zvgZsyDasc-BOZtGR7tonY7sjsO-mLls_PPveVQAoRyJAVDUShygyv2JfLvheEpBBqqFEwvhng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf87199f71.mp4?token=A15KQnd6LNZIdrjC5X5M1dszNJPpJ39zGD-NQ4JiCLMq2g3BrDjvjvkZTtwbo4BMY1gOTvOiNAGwqmyRB-FnAKNY1SwfMVuHvO2_PefT38vheKbOUElz19Ci7quVupymXvd7csYY8s-A_Wmyv57Ahwsfyg3yyxcmX5nXC8tBfYw6onuPElPf4YlO6bVxrwuZJiPaEBpEWC7w4cAn7CPRcYxXHdQCogMzcacgztNDj4rl3CoBNbF8dCgfWvrJIDN_DLVgq3LcmP43zvgZsyDasc-BOZtGR7tonY7sjsO-mLls_PPveVQAoRyJAVDUShygyv2JfLvheEpBBqqFEwvhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی متفاوت از تهران که در فضای مجازی وایرال شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/690572" target="_blank">📅 12:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca85298042.mp4?token=dpsXgegqhbWOvoykqC--jkRi7iuwPoaLAeR2zCJmKhzxo0dyNqPZpWOYx0VBL4sTwD4il9KT0W7_QjNmnA-ZQT7yTZMFAHZCRwYDg_uze1Rcva5AAeq3swkTJOdW5DM-YDyb0pCB6TtMNeicGMZlmgKGeMjvLDZRDT6e0Y-fxUC7-kMBp0Gj8CX7QUUmbCiNsJ6IbZTy6QXTLVeH-1ZMHNDUlxNefU9uN8soq0d4OwNP5rFr_ALBXMIqGbGPJqeAFpc2ygLE9gHcMwX5aU4ZOJ4BYQFSI23_X25pa4-Yqg0uM7XIS2MvzKvMlXLRs4AF-yHgSqbil5qE_PoHu5mrUHMUHhTLX2baB2sZTUqEiw636C_p72gTz0wKRL4Hn512F3TXgl0iVnEcivsd_uVl4kxHwPaynYMuV3_8cDXGWSje-cIvJycqIML24i448SvDG-Fuvxnxy_jMDmA-PIYZ2ixSXi4vqvm4xLhSpr-okYYKfcKvR280eqwnh_sjj-gN5xlfxY68RR3nnOKh_x5s7cQKWE7_SkGSlqFa-6Y3bYzS8hqbtg-loOvfC57ikNlfNuLvPtm1mjNpGOd0GFgdlzE_tGgbdI7eVFx6dD8yO0nEcZd8i5eeddo8fVvrYRLyyETcGEdQcezYkQhYJlKnUyMT-AAlqx-B2JZyjx_nU90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca85298042.mp4?token=dpsXgegqhbWOvoykqC--jkRi7iuwPoaLAeR2zCJmKhzxo0dyNqPZpWOYx0VBL4sTwD4il9KT0W7_QjNmnA-ZQT7yTZMFAHZCRwYDg_uze1Rcva5AAeq3swkTJOdW5DM-YDyb0pCB6TtMNeicGMZlmgKGeMjvLDZRDT6e0Y-fxUC7-kMBp0Gj8CX7QUUmbCiNsJ6IbZTy6QXTLVeH-1ZMHNDUlxNefU9uN8soq0d4OwNP5rFr_ALBXMIqGbGPJqeAFpc2ygLE9gHcMwX5aU4ZOJ4BYQFSI23_X25pa4-Yqg0uM7XIS2MvzKvMlXLRs4AF-yHgSqbil5qE_PoHu5mrUHMUHhTLX2baB2sZTUqEiw636C_p72gTz0wKRL4Hn512F3TXgl0iVnEcivsd_uVl4kxHwPaynYMuV3_8cDXGWSje-cIvJycqIML24i448SvDG-Fuvxnxy_jMDmA-PIYZ2ixSXi4vqvm4xLhSpr-okYYKfcKvR280eqwnh_sjj-gN5xlfxY68RR3nnOKh_x5s7cQKWE7_SkGSlqFa-6Y3bYzS8hqbtg-loOvfC57ikNlfNuLvPtm1mjNpGOd0GFgdlzE_tGgbdI7eVFx6dD8yO0nEcZd8i5eeddo8fVvrYRLyyETcGEdQcezYkQhYJlKnUyMT-AAlqx-B2JZyjx_nU90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا کشور با بحران کمبود پزشک و پرستار مواجه است؟
دکتر محمدرضا ظفرقندی در
#گفتگو
با خبرنگار خبرفوری:
🔹
موضوع کمبود کادر درمان و توزیع نامناسب ، دو بحث کاملاً مجزا هستند.
🔹
واقعیت این است که ما در حال حاضر به‌ویژه در زمینه پزشک و پرستار، بیش از آنکه با کمبود مواجه باشیم، با چالش «توزیع نامناسب» روبه‌رو هستیم.
🔹
برای حل این معضل، باید سیستمی برقرار شود که با تأمین معیشت مناسب در شهرهای دورافتاده و مناطق محروم، انگیزه لازم را برای کادر درمان جهت فعالیت در این مناطق ایجاد کند.
🔹
درباره «نقش مهاجرت در کمبود پزشک و پرستار» از وزیر بهداشت پرسیده شد، اما این سؤال بی‌پاسخ ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/690571" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690570">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
تصاویر جدید از شکست عملیات نظامی آمریکا در اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/690570" target="_blank">📅 12:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690569">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hidxqx0ciyP517ChikzAbYvePw3I_ZCXsEdx9LZ-YvyI84krLbED0OmyJsZ3yAeDqWcduNH6f1_Fdyt4KeYycc37geKKKwnXe86HBmz-BdoHwl8yj0n1Ae3z-OK7bRblimrComoxnd4g6MpYXTdWrwIdO8P9-ebVuBvMorJlGM-zi786cGpBJaMdYqMOGvZLErLltDe_uDWhHmYrRVLiQYuboznRHC2DgG-ZtAm99plP332qYcxgLUHQPHHnNwm8jqx6V010p4ZxymB1AEcvbvpfRIlS9IzY3D92VKJiXkxA-mtYD0j1ggm82MPC9xli6nkmX162FFExmCkfBiXIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر دو کودک زیر ۵ سال، یک نفر موبایل هوشمند استفاده می‌کند
🔹
۵۱ درصد کودکان زیر ۵ سال از تلفن همراه هوشمند خود یا والدینشان استفاده می‌کنند.
🔹
۲۳ درصد کودکان زیر ۵ سال هنگام استفاده از تلفن همراه به اینترنت بین‌الملل دسترسی دارند.
@amarfact</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/690569" target="_blank">📅 12:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690568">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aec07825f.mp4?token=WlsqR1uw_08cmgo-MMG3YkHmANdNEkA3kMZS6MZI-Tds8XENHslI0ofET_cqiPM39ba9nkLcNI-qgH8Om8Z86ZufDBAEO0_c1xCMAgshFBMsakmeDDmxloSa8nkLzRDCrPTEQ_gMcpMH5-VfN2IH4Bbeu_rJ9Oewwukk6QZRRr7cUFxyUQGMuHD7AegyjQiy6DwE6MPwYvM8aXmutGK3lSZ4Iuxf3rNNa6jHtBgt5OOKBjNBGmYmwb1aK9kb6veaNwMCQ6xYF7_ID3HfH8CL8-JVx2k9eUQOMylYiaUH1TeCLMbBF18_wdrBKIYS7NH8AJc0zHQSjkvKs5lsb48SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aec07825f.mp4?token=WlsqR1uw_08cmgo-MMG3YkHmANdNEkA3kMZS6MZI-Tds8XENHslI0ofET_cqiPM39ba9nkLcNI-qgH8Om8Z86ZufDBAEO0_c1xCMAgshFBMsakmeDDmxloSa8nkLzRDCrPTEQ_gMcpMH5-VfN2IH4Bbeu_rJ9Oewwukk6QZRRr7cUFxyUQGMuHD7AegyjQiy6DwE6MPwYvM8aXmutGK3lSZ4Iuxf3rNNa6jHtBgt5OOKBjNBGmYmwb1aK9kb6veaNwMCQ6xYF7_ID3HfH8CL8-JVx2k9eUQOMylYiaUH1TeCLMbBF18_wdrBKIYS7NH8AJc0zHQSjkvKs5lsb48SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به تازگی دعواهاتون با همسرتون زیاد شده، سخت نگیرید؛ شاید فقط دلتون برای هم تنگ شده #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/690568" target="_blank">📅 12:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
وزارت اطلاعات از انهدام ۳ هسته عملیاتی گروه تروریستی - تکفیری با دستگیری ۹ تروریست و به هلاکت رسیدن ۳ تن از آنان در جنوب شرق کشور خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690566" target="_blank">📅 12:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ماجرای تلخ مرگ کودک ۴ ساله تبریزی به علت گازگرفتگی سگ ولگرد؛ کلینیک واکسن نداشت
🔹
امیرحسام پس از حمله سگ به چند بیمارستان منتقل شد، اما به‌گفته خانواده، نبود واکسن هاری در نخستین مراکز درمانی باعث تأخیر در درمان شد. این کودک پس از چهار هفته درمان، جان باخت./ هم‌میهن
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/690565" target="_blank">📅 12:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وزارت بهداشت: واردات واکسن آنفلوآنزا هنوز قطعی نشده؛ شرایط، جنگی و دشوار است
🔹
نکته جالب اینجاست که در همین شرایط، برخی به دنبال تامین ارز برای واردات لوازم خانگی هستند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/690564" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fb03d7c.mp4?token=LzGW5geyDjs1x4_V277fkKc30ycxIAiCoPxuxby3vbKK_fuZgb0ZT5gTfXtwmYYChyMufeL9xKZyH5PtCJb6n5c2ibfhT1hdLMEM0QQ4V0BqulZ6N_bsUKAAaWWyb9YZfy_mjhxwn0ygN2eXxf8fsHE5uRXZj-RVcoqoPbm3Q2d7jFCp1Wl6r-TSaUZ80Ta1qoInsyaowFwRUzyllnFb_jxQc889W6FCKxsAo_Z5sAyf9PKw_y93fpUoKyFYsToiQip8oqyyDBiRUSf5Xf5nWX2mGMFNa4LRee0r-r9dynVhuDEJfn0hyrt1YybgNyErsJwZyJNq6gIJMx44Syq83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fb03d7c.mp4?token=LzGW5geyDjs1x4_V277fkKc30ycxIAiCoPxuxby3vbKK_fuZgb0ZT5gTfXtwmYYChyMufeL9xKZyH5PtCJb6n5c2ibfhT1hdLMEM0QQ4V0BqulZ6N_bsUKAAaWWyb9YZfy_mjhxwn0ygN2eXxf8fsHE5uRXZj-RVcoqoPbm3Q2d7jFCp1Wl6r-TSaUZ80Ta1qoInsyaowFwRUzyllnFb_jxQc889W6FCKxsAo_Z5sAyf9PKw_y93fpUoKyFYsToiQip8oqyyDBiRUSf5Xf5nWX2mGMFNa4LRee0r-r9dynVhuDEJfn0hyrt1YybgNyErsJwZyJNq6gIJMx44Syq83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک قیمت‌ها به شهروندان آمریکایی؛ وقتی بنزین گران، چهره واقعی ترامپ را برملا می‌کند
🔹
یک شهروند آمریکایی کنار پمپ بنزینی با مشاهده قیمت‌های سرسام‌آور بنزین، با خنده‌ای تلخ و تمسخرآمیز ترامپ را دیکتاتور خطاب می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/690563" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
لاکچری‌بازی در شرایط فشار اقتصادی / کشور در محاصره است، اما برخی عطش برند خارجی دارند!
🔹
قیمت یک دست مبل مینیمال در ابتدای سال ۱۴۰۳، ۲۵ میلیون تومان بود. امسال قیمت آن به ۱۵۰ میلیون تومان رسیده است. ما نسبت له قبل فقیرتر شدیم اما در کمال شگفتی تمایل به زندگی لوکس رو به افزایش است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245847</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/690562" target="_blank">📅 11:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEF9O3oQ2Yogh-TrinauzjrMvtOvXaybzNPiqzESWoJsiI2PyhJgzV75xCC2wuWZsG3JeTUchMigpfS39Uga6-XP74_V3fKLWppyTiuLgccL1qd0DDNTkPgTkSQyhOiVct__0RFIXR6fc1IQSq0zlIURzgm1iPEWOobmFB4405Rq08rt9qa4OFVfJGY3uxnfSTKsGoY02GdtspngUDD-OsuNETQ2iCOhfD8bkULUS1JxScCspK1POYeABrAVIBOR9QYSPU-EX2zyC_PX4XjBMhKAo-q7CJOzQuKrH0qEJ84QvPgejMNaNQisGPGP864q4CIlFGUSFJWqSE6or1ByPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ غذای دانشجویی سال تحصیلی جدید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/690561" target="_blank">📅 11:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129b6ba29c.mp4?token=gaACiM6WkZ3AL_EpIKR_BUDAkw9W9Guy8EUebaw3CcfJK9b5fnGfn7w3158phsVsRZVOduDuZGj_7fI8lc1IvtcrDxG1SWXjbk7UB7TiYiHfK9ngV7qa2-ODriv7zfLtCZ5uBJygTv0pCELFkavJGITblHW4CJ5oyA9B583BKKfSibBW7NOG4e35n4onku7so5rhXzocfbETvRhKadSrGgLpSh7DrTHTJ20zDuvnHelM8yRjAEeqhgE3Di0NlkOIb1dvaYQzA6DUDi-YUcbfsgOszTYF5jXKrHEmvViuJfwX0uFr20iBajO2Oj9m2XmbqyY7gUtJFQRX9Z8nRWDQEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129b6ba29c.mp4?token=gaACiM6WkZ3AL_EpIKR_BUDAkw9W9Guy8EUebaw3CcfJK9b5fnGfn7w3158phsVsRZVOduDuZGj_7fI8lc1IvtcrDxG1SWXjbk7UB7TiYiHfK9ngV7qa2-ODriv7zfLtCZ5uBJygTv0pCELFkavJGITblHW4CJ5oyA9B583BKKfSibBW7NOG4e35n4onku7so5rhXzocfbETvRhKadSrGgLpSh7DrTHTJ20zDuvnHelM8yRjAEeqhgE3Di0NlkOIb1dvaYQzA6DUDi-YUcbfsgOszTYF5jXKrHEmvViuJfwX0uFr20iBajO2Oj9m2XmbqyY7gUtJFQRX9Z8nRWDQEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشایی تنگه هرمز باعث کاهش قیمت‌ها می‌شود
مایک جانسون، رئیس مجلس نمایندگان:
🔹
ما در حال پایان‌دادن به این درگیری هستیم، بازگشایی تنگه هرمز باعث کاهش قیمت سوخت و مواد غذایی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/690560" target="_blank">📅 11:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رئیس سازمان خصوصی‌سازی: واگذاری سهام عدالت به جاماندگان فعلاً ممکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/690559" target="_blank">📅 11:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2BGZHejrmmhIKlgPzrLBX1V1TzT-qikbBBPS2t-8VyzHss5v3C9P-ZH6PzfqgzNc4d_T2tHIElWNxurjTkei9SdsYz4uRuUclB6d6Rd4yqn3wlEkjsdv1pUr5d0mkl1pCeddvsnw1tZjEJ6Gf9QNxT3mci40AGmdsKtyHfjZw9jVSTXtv4RAeGe5cbi6jUWuyDOfyYQHj_oo6-YlfXMK4r7JpfuDIJYNxtkHfkGJT6Dc-YAMw7k0PRmAnyG1e4prrdK6zx2L0DQOVN_GsBf-Rn62Mt3knZvU5YWTB3L4hkHLl2-7unKUAP9Gm9MpVdQzjmiE1ioT0Seq21JrpTscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار شرکت توسعه منابع آب و نیروی ایران: ال‌نینو عامل ۷۰ درصد سیلاب‌های بزرگ ایران
🔹
مدیرعامل شرکت توسعه منابع آب و نیروی ایران: نتایج بررسی‌های این شرکت نشان می‌دهد ۷ مورد از ۱۰ سیلاب بزرگ کشور در سال‌های تحت تأثیر پدیده ال‌نینو رخ داده است.
🔹
کامگار: بر اساس یافته‌های این پژوهش، ۲۹ درصد سیلاب‌های رخ‌ داده در دوره‌های ال‌نینو در ماه فروردین و ۲۱ درصد آنها در ماه آذر اتفاق افتاده است؛ از این رو پایش مستمر شرایط جوی و نیز افزایش آمادگی در این مقاطع زمانی از جمله مدیریت بهینه و‌ هوشمند مخازن سدها به منظور فراهم کردن امکان تسکین و‌ ذخیره‌سازی حداکثری سیلاب در این مخازن و استفاده بعدی از آب ذخیره شده جهت تولید انرژی پاک برقابی، از اهمیت ویژه و‌ دوچندانی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/690558" target="_blank">📅 11:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc014bdc8.mp4?token=t1_Ro7WLEy6v4E93V-cD9NgimQ7wJWVOw9w4sNjYsrjbbtm3dwS3-ze_CWoenJlh5Oezu-u8zhOG1R-OEe8uKpdsACFawZUqWZD0R9O1cdxWzUtfYpnJdoURK-JmdBP2c16ZMS0ikibbgQ0xxGjXvvRcJBDNlMu_sQJAo0XKouCrD2DDFIrZZmIdq_R9JboAeyMUlIrAdDlRkei73K0V8zhiIjwAsG3NVSUgQkl4k59Sfvkpyi0FCYQcZx1K-7iIXBVfhawgm42jUFHpw4NbwdM362kH4itPbZ4WIDCnmSo3m3-N76m1nXkJBRe8gBrxljT4Ab0B5WmLkW7pSXa-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc014bdc8.mp4?token=t1_Ro7WLEy6v4E93V-cD9NgimQ7wJWVOw9w4sNjYsrjbbtm3dwS3-ze_CWoenJlh5Oezu-u8zhOG1R-OEe8uKpdsACFawZUqWZD0R9O1cdxWzUtfYpnJdoURK-JmdBP2c16ZMS0ikibbgQ0xxGjXvvRcJBDNlMu_sQJAo0XKouCrD2DDFIrZZmIdq_R9JboAeyMUlIrAdDlRkei73K0V8zhiIjwAsG3NVSUgQkl4k59Sfvkpyi0FCYQcZx1K-7iIXBVfhawgm42jUFHpw4NbwdM362kH4itPbZ4WIDCnmSo3m3-N76m1nXkJBRe8gBrxljT4Ab0B5WmLkW7pSXa-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کی گفته که آمریکا می‌تواند برای همه دنیا تصمیم بگیرد و بقیه باید اطاعت کنند؟
🔹
ما این را نمی‌پذیریم و سر خم نمی‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/690557" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm5uJsp4eK_aBxm_oWW37HKzsGBwg5KVvdVMPAFS5hM-Tx3x-r5oy2f6LvvbqBj6JVEMIhgw34TlDpC1SBv89XTla58ZiGsOpqZtJ8Odmmt0QJvpMJ_7Oz71cmrE9BNTYhd3lvvWgAY6d6MQcfRtdu9EDJLbIYExfiDyve_G3yDTevxJ376uOQkriqZvGiDOpDCmKENEpTkYn15jGPuCDzRZuOmDZ_8RwBNPSVdQRMCOstIT6EXexx9SjE-J_L3Kx0efsY_LH4244uQpvWZkcnQpyiHu2eqmFd_iBkQJwChdYSfE_XLMWzScxTeCtBsMaps_WQfO_Q7F72zKcoH6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست ۱۸ بازیکن داخلی دعوت شده به اردوی تیم ملی فوتبال ایران اعلام شد
🔹
چهره‌های سرشناس غایب در لیست تیم ملی
روزبه چشمی، محمدحسین کنعانی‌زادگان، علی علیپور و شهریار مغانلو چهره‌های حاضر در لیگ برتر هستند که در فهرست آخر تیم ملی برای جام جهانی حضور داشتند اما در لیست جدید جایی ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/690556" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd9a6d7d5.mp4?token=NAP1aeBTZ3Af6KoVkOb_y4iqw2F2GDPYjHzu8_AZcMnerYz7zmrr7FrocgjaVJnWIzl2qK-QGVQVxQB1Zakh6z6nv_htQgqoG6FSNq-4PrYXiDXRtWDZ-tT1LtEmLviMWivNorFMbBBzP9-0ieZgC70fArEx7uGwgLodX1UIeOFsjKnf9fkhZoCSiZcbW-KVa8gzWpNpZN0hANgMfM_iaVM6Z9xvFhUp1H7xT7DSrkKz3_DKCICR6g1CddQUrVL7BF4uG6i2Ywhvy8XhUYoY8oIsWrijil4d9x76VJRMJ5gsmp4F3pvr1PqI6Exbtn651SoAfm-j_NSo_b0d0nrTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd9a6d7d5.mp4?token=NAP1aeBTZ3Af6KoVkOb_y4iqw2F2GDPYjHzu8_AZcMnerYz7zmrr7FrocgjaVJnWIzl2qK-QGVQVxQB1Zakh6z6nv_htQgqoG6FSNq-4PrYXiDXRtWDZ-tT1LtEmLviMWivNorFMbBBzP9-0ieZgC70fArEx7uGwgLodX1UIeOFsjKnf9fkhZoCSiZcbW-KVa8gzWpNpZN0hANgMfM_iaVM6Z9xvFhUp1H7xT7DSrkKz3_DKCICR6g1CddQUrVL7BF4uG6i2Ywhvy8XhUYoY8oIsWrijil4d9x76VJRMJ5gsmp4F3pvr1PqI6Exbtn651SoAfm-j_NSo_b0d0nrTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر رهبر شهید به شهید رئیسی درباره امیر تتلو به روایت استاد رائفی پور: چرا به تتلو نزدیک‌تر نشدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/690555" target="_blank">📅 11:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
کشف اجساد ۵ نفر در تهران
🔹
اجساد ۵ زن و مرد که گفته می‌شود قربانی قتل خانوادگی شده‌اند، در گور دسته‌جمعی داخل چاهی در بلوار سیمون بولیوار تهران کشف شد.
🔹
عامل جنایت دستگیر شده و تحقیقات درباره انگیزه و نحوه وقوع حادثه ادامه دارد.  #اخبار_تهران در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/690554" target="_blank">📅 11:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تصویب طرح تحریم روسیه و ایران در مجلس نمایندگان آمریکا
🔹
مجلس نمایندگان آمریکا طرح تشدید تحریم‌ها علیه روسیه و ایران را تصویب و برای اجرایی‌شدن به کاخ سفید فرستاد.
🔹
این طرح موسوم به «قانون تحریم روسیه و ایران ۲۰۲۶ لیندسی گراهام» با ۲۶۲ رأی موافق و ۱۵۹ رأی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/690553" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
کشف اجساد ۵ نفر در تهران
🔹
اجساد ۵ زن و مرد که گفته می‌شود قربانی قتل خانوادگی شده‌اند، در گور دسته‌جمعی داخل چاهی در بلوار سیمون بولیوار تهران کشف شد.
🔹
عامل جنایت دستگیر شده و تحقیقات درباره انگیزه و نحوه وقوع حادثه ادامه دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690551" target="_blank">📅 11:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA13a1NNOSd4I0XniIdtw4KJ0n8-4nG7N59Eyos8XIAWBJ1NgpNwKOWVHhHzuKjrFyf7MCG-1yy0B8HDY6rQSjJaxRKkoHu_kF1SS2tSa7ISiZlFpMuCcvkmYJ2GHyVk70dxQuexi8N1Zhk7aXq2gXxD8DPkSsoVvpvoDrJH7IJpTWS2NB3x0FVnGt2VL97Ny1H7LO0Qrf5MkXOiWn--nmxH3vJL2QtKF7hjFcfIwjom53HbhnHBeGKsTtJnkaySosAl1XvmgVvtr_p4IITBVFaStLli219Sye5UTE9Pxnd1M3ZdOTsGzLuSd2edhayQa8BJK-hKM_i3GPkz1jWz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج سفرهای جاده‌ای در روزهای پایانی تابستان؛ پیش‌فروش ۸۰ درصد بلیت ناوگان حمل‌ونقل عمومی
🔹
معاون حمل‌ونقل سازمان راهداری و حمل‌ونقل جاده‌ای گفت: با توجه به موج سفرهای پایان فصل تابستان و افزایش تقاضای استفاده از ناوگان حمل‌ونقل عمومی، بیش از ۸۰ درصد ظرفیت ناوگان به‌منظور تسهیل سفرها به‌صورت پیش‌فروش عرضه می‌شود.
🔹
مهدی خضری اظهار کرد: در این راستا، هماهنگی با تشکل‌های صنفی به‌منظور افزایش بهره‌وری ناوگان حمل‌ونقل مسافری، برقراری سرویس‌های فوق‌العاده و تنظیم برنامه زمان‌بندی حرکت ناوگان صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690549" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای
الجزیره: گزارش‌های مربوط به اینکه عربستان نفت خود را از طریق عمان عرضه می‌کند، قیمت نفت را کاهش داد
🔹
نرخ هر بشکه نفت با ۱.۲ درصد سقوط، به ۱۰۴.۵۹ دلار رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/690548" target="_blank">📅 11:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_QxRokRBC8pNChndVsIc2n1brPx2w9F02jkf-1IbVml7nal-VQs6yRshe14HhAddtdT72jvVY00-OXJRnWmlMLl5rqsoFTVjmaJLKcEovnCUEOyJgNsruID3GC2M-NpEoroVmCnRdhh9JdyOlvU9XZw5NCpIj-gYWTnl2GXtHJAQgbv3ADuHZ9NdebRCigGHmvq610hAjeFPQ969wrhFs8WwedLPXk3onSUFhCv9kLhtnQVPt9Hkblm3sCgNQXNxlYVd2Q6E3yrTF2En-9kKzdS5bWa4enMnAFRvciBKBhMl9jIqwt7rb4tVPvM4ezCACuOjEliGo66F1wbFucz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HspCp-KSoUe3VjydTcnbJ79PugoEJ-lLGYcd7b4Hi1vLUOk4_RQOP0nRp5Rd5YCOI7DY_VptMF3CdW7VpaZmpkggz8nVyGvp0VCvZPFnnzecSVZeQnXBwUvvicibwNB56iGVFgEQGsPFt0S_jfFqX_hqHE0MWDfkCuxJhCg-zOIiiyp2APkmd04E-T8P_6FZoxnfFkU1aPIr3VbgCFR0ljA9Pby8pO1eu2x2DMRoFPcXm9oWXx-TqJise-proAj2YzIQLswR9DdUXDA6iSYaSACiYD0C-TjLq6nYrzqEBtDQBtmgw8c0wYCDTUsSrTNTZY8NPurnz2Rtef_iNOS0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت آواکس آمریکایی با فرسودگی شدید
🔹
یک آواکس E-3 آمریکا پس از ۷ ماه مأموریت در خاورمیانه با آثار فرسودگی شدید بازگشت؛ این آسیب‌ها به گفته گزارش، ناشی از استفاده سنگین و مداوم بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/690546" target="_blank">📅 10:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyxdz4LL9eFP1uZ3k0-ijhX0z2v_Jl-FDSDOtzEdm-qYiMwHrDzybmlOacITp1Xo_Ttu-fdzHitZMh0dpLqwRn5Husk50gzsSlyCznpbVzpwB8IHEKNQOWpc66wXSjFMvEg5vMv5EUaVpLovU8c0EyshO4BnnBTexngjphKLySQp2h5mf-Zl_3eKsWTfIH_mpS6JJdBuwOLKw8262r7IPX9AcjlTw3m-ontHzYicOLvbvXyH2axbTktaXDI9U3wzppKWV1dZXg8o9aiSg7ATuscQvUK5LD_VEaB0ForSrKkARY6YFRmMnHmcf4YhYdj2LXRvl-57V65QrLLbXjNvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویق استیضاح پیت هگست
🔹
مایک جانسون با تعطیلی زودهنگام مجلس نمایندگان آمریکا برای هفت هفته، رأی‌گیری درباره استیضاح پیت هگست را تا بعد از انتخابات میان‌دوره‌ای به تعویق انداخت.
🔹
جانسون دلیل این اقدام را بازگشت نمایندگان به حوزه‌های انتخابیه اعلام کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/690545" target="_blank">📅 10:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgfI9sIr-FedWGBwh-9KL7uIkWGRxpTJX7toulGMy0RJQffqpLI3K35ir30tTcTW2ZamRUcSF1mvLcfcK4TblYalW5meB0G5PfCWvOBH7FLD0Gds0Sp5g3LPHoFC9QnxavMbru15P02h2xngkhFjC8-GO6uH6gVYRY9mGgUnxvGIxOZfVwnAQkUN65XYnQe3MHu2GDn29ayf_LufJJ1bOB4Q971xLK9nrQEH6w1HqOgMi_-WrpKb0EsEwnEAutfYGw30zr0kZQ_4XymEQ6YBsHH4qWKT9-eBXxxB5TO1vcWnvwSQFGtX3wPTB2lt3KKpLe0c5n_kNL85kZmw4HvyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهریه چه زمانی معتبر است؟
🔹
۶ شرط مهمی که باید بدانید
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/690544" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe5662b69.mp4?token=Hyyd_MwOnidc5KVGOKdLcSzE3Wt9NRk1cWeL2YjyBkypgwbUzpiHDvbHGZCVKQQMLZpV21Zlhl2oZWCUc1M-P1n3qt-jdYs3rht7fSV3lmS1mFF59eVfIAphGsaYSa1jD_VrYrwGB4VcdtBd7K_NVxh4LIqU0DheU08XLBlyVAg_M417kUFUgmRQRFy8wVr2qEezyB7wTgtdsGW2s1qgDuoSkxNJvwlGqOdW8yuTR4CG7gyRJVMJrahiIBXO54lhKV99sLCGbuZH1e5_KFhX6rO2sTFm3SiQEoO_ZV383aRcJfbBpwKb0uKjIbInINErPtqk3dMnHdpv6EUbb-5kuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe5662b69.mp4?token=Hyyd_MwOnidc5KVGOKdLcSzE3Wt9NRk1cWeL2YjyBkypgwbUzpiHDvbHGZCVKQQMLZpV21Zlhl2oZWCUc1M-P1n3qt-jdYs3rht7fSV3lmS1mFF59eVfIAphGsaYSa1jD_VrYrwGB4VcdtBd7K_NVxh4LIqU0DheU08XLBlyVAg_M417kUFUgmRQRFy8wVr2qEezyB7wTgtdsGW2s1qgDuoSkxNJvwlGqOdW8yuTR4CG7gyRJVMJrahiIBXO54lhKV99sLCGbuZH1e5_KFhX6rO2sTFm3SiQEoO_ZV383aRcJfbBpwKb0uKjIbInINErPtqk3dMnHdpv6EUbb-5kuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف، معاون اول رئیس جمهور: از مردم عذرخواهی می‌کنیم و  شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690543" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_a8FTod6XC0SKCAkNJwkRxrhWkHdHVHI6qtVUW_bnX7N7IinnIn-FCUb0ScuRI6H6C8GHc9QXvCwvSdKc9rxd4lguYhRCuIqx5A2nzm7YMGm7WCl7vtdOOs-4kt7EJQuCZ_iJt9oGBZCOQoYvDL0CSKHMhFGwKuBbifFz-BlvQ6zxXd7pujnUMTV4lSq9gh6vIKy4Hp3gV1Oy6WZCtchgHu6A3suReyfUfIRr4v4dUwT9ZvNKGB7m-5NE5A3uxCH_vIdXJF67UygFmWDnFEJbGVU73-UO9wjQRa_kzJkEiLZBVkTUqNj4I67SNsLSRE3UyahqGCc1TTO_rNdNL0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام دانشگاه‌ها سال تحصیلی را مجازی آغاز می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/690542" target="_blank">📅 10:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اوت ۲۰۲۶؛ گرم‌ترین ماه ثبت‌شده جهان
کوپرنیکوس:
🔹
اوت ۲۰۲۶ با دمای ۱.۶۵ درجه بالاتر از سطح پیشاصنعتی، مشترکاً گرم‌ترین ماه تاریخ ثبت‌شده بوده است.
🔹
همزمان، یخ‌های دریایی قطب‌ها کاهش یافته و بخش‌هایی از اروپا با خشکسالی شدید مواجه شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/690541" target="_blank">📅 10:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHDEAfS1cjvW2-H2f6zEQpbqghHXLG2ffLN4wqoxDRulJ-0OKyZ8yLSR9BcrD1j40Lx6xz8laSJlv5hKLW337jErp76T93ThOYAZPJ6dlPNhVsr_pt_7b6_YYEvKZSD0ueapzM9oQe4y2GIFmjqieLqmqSmvB8kRgCaiIAimAzJF6B-tZAlKeFH4Vu9oLHZHXYHtvuMgCyQ9PqagO60A5U9eWMNC3iNu_dLJ8nhH0Z67mwlfjubFGzz1aUbReMxaCB4QW6P3CpSFXKIINm8Ee2-WB6yWFRhFgQp3wfTkKVNGFm6rWryxjdD4x5m-GWAJ191VnzhugAG7-nrOZrZTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
📚
سال تحصیلی جدید رو با حامین شروع کن!
✨
از
لوازم‌التحریر
،
دفتر
و کتاب تا کوله‌پشتی‌های
جذاب
؛ هرچی برای یک شروع دوست‌داشتنی لازمه، اینجاست!
😍
🛍️
🎁
تخفیف ویژه سازمانی برای خریدهای سازمانی و تعداد بالا
🛍️
حامین، نزدیک شماست!
۶
شعبه در تهران برای یک خرید راحت و لذت‌بخش
👇
📍
شعب حامین در سراسر تهران
🌐
خرید اینترنتی:
Haminstore.com
🎧
پشتیبانی و مشاوره خرید:
📞
۰۹۲۰۶۹۶۸۰۰۱
🔵
کانال بله حامین
برای دیدن محصولات و اطلاع از تخفیف‌ها
:
👇
🔗
http://ble.ir/join/DYPXxvTLNv
صفحه اینستاگرام حامین
https://instagram.com/hamin.store</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/690540" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqq_U2MqK6fcCZQeBPjL0w4MhHoiJrAg9XqUjo4SbcvJNrgRQ7-jO7Zhs42VAGntuwqMzmz7cVOob6nPWY1d2XZHOGgW0LZJ5ko1gPDE_6YVCuLHQWGWlymw__29Rs04FNGTLWks_hDnuWxHYHsL794ZXSdKoYl9P6Cc2Qp7BKTARN4BjZ3f2RSImTfDouiF2wUU_29FOTH7nIBAmGbfzZSfOOdQkBe2hvHbiSWpcSJpPmWvDbnxS8l-D21RtYDLBHzNjBoLQWUZGLQnreq1nlR5FGYhVvKi74a2ss5ySoWJ3k-gN_hqe9fn4kMPZT7Hj7vqbL6Zgp_Y3n_yRq-4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیک دوماهه آنفولانزا در کشور!
🔸
حدود ۳۰٪ از نمونه‌های بیماران دچار عفونت تنفسی شدید در کشور آنفلوانزا است و کرونا تنها حدود ۲٪ موارد را تشکیل می‌دهد.
🔸
موارد فوت در بزرگسالان و کودکان گزارش شده و احتمال پیک طی دو ماه آینده وجود دارد؛ رعایت احتیاط برای سالمندان…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/690539" target="_blank">📅 09:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
آسوشیتدپرس: عربستان سعودی به دلیل ادامه حملات حوثی‌ها در یمن، با کمبود موشک‌های رهگیر مواجه شده است و از فرانسه، بریتانیا، پاکستان و مصر درخواست کمک در زمینه دفاع هوایی کرده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690538" target="_blank">📅 09:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoqxhutHYxGTS7idmW7SgSBLxkC5pg13jOu4_UTbuJfAPv8Yx_HdEKeRTtSv8rVs7BrnJVpdapuHJOHHoQc07DeiWPiplAVezoV2KS_p-KK__ZN7Pbf-eHrYTZZ6-tlCAJKdAKvF9zqMSmGR68q04HRnWSdm6mDVv_541R28iozwn0zPzsCGNTctI0QQuD2oAQnlyupHhXI8D_OV3rLGP-n6wy5GFR53kwAJWbrKLFymw-Fha9Y0Ai73_pZ0yFtvTE_-CmgM7TvQn3lIi_c2mScNO09LZh7Gg_bfJc__K6b_dRSm160tBbj5mbJCAlsj-kzcouufgxYucuVy9kFYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهداد اقبالی میلیاردر ایرانی، باشگاه ورزشی چلسی را خریداری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690537" target="_blank">📅 09:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
آمریکا رسما بالا بودن تورم را تایید کرد   رئیس فدرال رزرو (بانک مرکزی ایالات متحده):
🔹
واقعیت این است که تورم بیش از حد بالا است و مدت زیادی است که این وضعیت ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690536" target="_blank">📅 09:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690535" target="_blank">📅 09:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
رویترز: وضعیت خطوط لولۀ نفت عربستان همچنان نامعلوم است/ زمان تعمیر ایستگاه‌های پمپاژ ۸ و ۹ خط شرق به غرب نفت عربستان هنوز مشخص نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/690533" target="_blank">📅 09:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a700e501c.mp4?token=UDO0QZfSapaMUodpHZyOJv5BirIzJW245RiJ33Id8MS0jFWVO5e6CVTqlbKl8p39fhnR647HWLABWc7iP4I1W834KR9oQ3NIZ99F9B7tamok0ScfNfdJxJxdwW8bTBXP3v4Zrcme_aqeZ3F_2RWyEMJFt0ibIFthxXowohBWgJ1WngoKwCeHQGEyaDUM4alEgqJFHs_4ce-hJBleNDmLWy7LKGqGM940_iYl6-MpIhg5mD1lPyiKop6uM5SNht7j3qRE1WOTdoZW897XGUi6B3wy4wqP2IX0nqKR1URyKaZJRp-oWuXIzD5MqSZ93f6m1MIZi-wgVXx9ZbTPD-CxmHvTvZ3VuXhRiqxw-Thu537pxEqbcjjGR0zPIeIgX3_qbQ2U_wauvKV_-R3H85YZdHbCas8Vy0HQ2DNb9ebVHNuaYv8FsPs8oT-wiRL4IdskYgACCFhz54HrxLUKiAFJ4bPUS03QSiaqg2bnkrJEMzg5C6s1ib8jE2BVuDWfXRor5nZ7Xj39Kk07hjqXzgRGWdd_kU3IsS6mIo53T6_i24gMFFFWR7F05r9Ss0SnGN4qlqwPdFUeGDR4CA7LFh5AYRVawFQWUqQlWB2gJpxZJMHJ5WZjvVFMEnbnSSsQjZ4wIOFmxS-2csNHKkONzVPV7lq7tSB9vmZ1IJ-o9hyX6Go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a700e501c.mp4?token=UDO0QZfSapaMUodpHZyOJv5BirIzJW245RiJ33Id8MS0jFWVO5e6CVTqlbKl8p39fhnR647HWLABWc7iP4I1W834KR9oQ3NIZ99F9B7tamok0ScfNfdJxJxdwW8bTBXP3v4Zrcme_aqeZ3F_2RWyEMJFt0ibIFthxXowohBWgJ1WngoKwCeHQGEyaDUM4alEgqJFHs_4ce-hJBleNDmLWy7LKGqGM940_iYl6-MpIhg5mD1lPyiKop6uM5SNht7j3qRE1WOTdoZW897XGUi6B3wy4wqP2IX0nqKR1URyKaZJRp-oWuXIzD5MqSZ93f6m1MIZi-wgVXx9ZbTPD-CxmHvTvZ3VuXhRiqxw-Thu537pxEqbcjjGR0zPIeIgX3_qbQ2U_wauvKV_-R3H85YZdHbCas8Vy0HQ2DNb9ebVHNuaYv8FsPs8oT-wiRL4IdskYgACCFhz54HrxLUKiAFJ4bPUS03QSiaqg2bnkrJEMzg5C6s1ib8jE2BVuDWfXRor5nZ7Xj39Kk07hjqXzgRGWdd_kU3IsS6mIo53T6_i24gMFFFWR7F05r9Ss0SnGN4qlqwPdFUeGDR4CA7LFh5AYRVawFQWUqQlWB2gJpxZJMHJ5WZjvVFMEnbnSSsQjZ4wIOFmxS-2csNHKkONzVPV7lq7tSB9vmZ1IJ-o9hyX6Go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه‌ای کامل برای درگیر کردن تمام عضلات بدن در خونه بدون نیاز به هیچ وسیله‌ای #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690531" target="_blank">📅 09:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ba280b8e.mp4?token=bx2Pn08BDzWT1qgPbdfaLpbyigHpBACLy1KEpLlRz-g2GgL_75cafXD-UGxXp6YubSB0LVeGXxGFq6cpRQhJk2RMUteKzywq_PnvywxfoCrCxBj9Mna9ASySG67461ODACKxl5X8VN0woiya2u51fsqktJAqMZ4ZNm2xJ6Yxx9s71T3Gw5d8AFxKhx2NSYcjD6O3n_wwoIN4S9AwRbiGDPqBq5IPNpaPXX1VNnUERYDTiaZ3gRF11QmQh0cRFKIeJSRS8xuX64uyZMB3ko4tWiaALpB1VNM5tcgglBw3V4aXV99utIX_ExnYdAm7ISJ9IfeNfmYNVA6ps7VHiO8R0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ba280b8e.mp4?token=bx2Pn08BDzWT1qgPbdfaLpbyigHpBACLy1KEpLlRz-g2GgL_75cafXD-UGxXp6YubSB0LVeGXxGFq6cpRQhJk2RMUteKzywq_PnvywxfoCrCxBj9Mna9ASySG67461ODACKxl5X8VN0woiya2u51fsqktJAqMZ4ZNm2xJ6Yxx9s71T3Gw5d8AFxKhx2NSYcjD6O3n_wwoIN4S9AwRbiGDPqBq5IPNpaPXX1VNnUERYDTiaZ3gRF11QmQh0cRFKIeJSRS8xuX64uyZMB3ko4tWiaALpB1VNM5tcgglBw3V4aXV99utIX_ExnYdAm7ISJ9IfeNfmYNVA6ps7VHiO8R0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری کامل از لحظه رهگیری و سقوط جنگنده عربستانی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/690530" target="_blank">📅 09:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ترامپ با وزرای خارجه عرب درباره جنگ ایران دیدار می‌کند
اکسیوس:
🔹
ترامپ سه‌شنبه آینده با وزرای خارجه عربستان، امارات، کویت، بحرین و عمان درباره گام‌های بعدی جنگ با ایران و راهبرد پس از درگیری گفت‌وگو خواهد کرد.
🔹
نتانیاهو نیز خواستار دیدار با ترامپ در نیویورک شده، اما هنوز این دیدار برنامه‌ریزی نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690529" target="_blank">📅 09:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
کرونا از آستانه هشدار بالا گذشت
🔹
مرکز مدیریت بیماری‌های واگیر وزارت بهداشت از افزایش درصد مثبت کووید-۱۹ نسبت به هفته قبل خبر داد.
🔹
درصد مثبت‌شدن آزمایش‌های کرونا به ۱۱.۷ درصد رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690528" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b902c0fb66.mp4?token=X6Cq8WPcav8SbhbbCZ2DO3qycd1QG9uz6hYB-sNEHlM1k01vjNidITB2DMKMztEm_iTtH6c8bTlmDIpTo0-_VBwCF14mOPCB0gTOR1Lh4wJU_v5m2X0BltaLNWb-EpjiSijHeH8o0gsak3EJwnGc3fYPJ2b8HPVX1AfPN2LzT46ukjzAc2pHoGw2swZAPvdVwMdYR2Raa2N04wYgOFMlmigdkhg7r1fBwd3Lva_M5gH1UooH_v3PNjGCEsZljtpahjxG3iF0e25X7n2D1CSqcFmXcvMHxAxQVP3IaDlsx_pMBAt1HI_t61O_27dUgGKt7yy_h7k5cNAQiQ4_MMY1PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b902c0fb66.mp4?token=X6Cq8WPcav8SbhbbCZ2DO3qycd1QG9uz6hYB-sNEHlM1k01vjNidITB2DMKMztEm_iTtH6c8bTlmDIpTo0-_VBwCF14mOPCB0gTOR1Lh4wJU_v5m2X0BltaLNWb-EpjiSijHeH8o0gsak3EJwnGc3fYPJ2b8HPVX1AfPN2LzT46ukjzAc2pHoGw2swZAPvdVwMdYR2Raa2N04wYgOFMlmigdkhg7r1fBwd3Lva_M5gH1UooH_v3PNjGCEsZljtpahjxG3iF0e25X7n2D1CSqcFmXcvMHxAxQVP3IaDlsx_pMBAt1HI_t61O_27dUgGKt7yy_h7k5cNAQiQ4_MMY1PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی رباتیک در چین
🇨🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690527" target="_blank">📅 08:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ba5cb331.mp4?token=VGoeK44mQ7scDRjl6XwESmQGKcQ4-sfYbX7SGiyL5E1ojt12GMkAdNPaa7Sgg-bbJGpcnAhgvWbaTloPhdlTvQ2EQnbMjN9JCijUu6O9TKK_vxlTbX4BF0G8wpJfqAB1TGJuYiUvNSgBySM9YNWMVPPHeXdtX-gSR-CWfFfXG1FnNpVGIIZWkzbU1fvwj7kExXeTVfPvoga2UFe4kCC77KbsTrMA7Bo-XwnJ7vbUrVDhOyTAvBtd7aFHRHFcENItmb5oX2HEndAMKoYoacpu-HriMRL6HsvxI0wjHDtBWEVh_Lxfk09nH4j3-HlbSYqO3L_DNiLwxN5E4LR8t8yLla-X_bZ3aHQKXruMl7H4enkDkuH7p34FQzMPvmCytYkucxpm6BhMBNd5OIPtZP3ti3rCSRzEgSbmVDhozSr43ov9Lw-cuh4LNjHMDmFFWzd_zxRd9SjsVB5yZSDMT4BOmS_i3PjpYK9t-OwqtL7uIH6r9amAGyHpMDN7WKKXmBmTD5Bx9Hnk1687xELCsdNWPOQXS90l7uMZDXzA7eot0PCFhOYn2_ZJrp9FuyccPEaWMtWJNX68oxWmYwtOT8A4UXvtlaL0IIb8gDKyFF-4qtZjbBYrfO4kRzRiqKx5319PLhHMvhfSOUx4zgC7uNZz_qvfLuzY3G_l40ywY365W1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ba5cb331.mp4?token=VGoeK44mQ7scDRjl6XwESmQGKcQ4-sfYbX7SGiyL5E1ojt12GMkAdNPaa7Sgg-bbJGpcnAhgvWbaTloPhdlTvQ2EQnbMjN9JCijUu6O9TKK_vxlTbX4BF0G8wpJfqAB1TGJuYiUvNSgBySM9YNWMVPPHeXdtX-gSR-CWfFfXG1FnNpVGIIZWkzbU1fvwj7kExXeTVfPvoga2UFe4kCC77KbsTrMA7Bo-XwnJ7vbUrVDhOyTAvBtd7aFHRHFcENItmb5oX2HEndAMKoYoacpu-HriMRL6HsvxI0wjHDtBWEVh_Lxfk09nH4j3-HlbSYqO3L_DNiLwxN5E4LR8t8yLla-X_bZ3aHQKXruMl7H4enkDkuH7p34FQzMPvmCytYkucxpm6BhMBNd5OIPtZP3ti3rCSRzEgSbmVDhozSr43ov9Lw-cuh4LNjHMDmFFWzd_zxRd9SjsVB5yZSDMT4BOmS_i3PjpYK9t-OwqtL7uIH6r9amAGyHpMDN7WKKXmBmTD5Bx9Hnk1687xELCsdNWPOQXS90l7uMZDXzA7eot0PCFhOYn2_ZJrp9FuyccPEaWMtWJNX68oxWmYwtOT8A4UXvtlaL0IIb8gDKyFF-4qtZjbBYrfO4kRzRiqKx5319PLhHMvhfSOUx4zgC7uNZz_qvfLuzY3G_l40ywY365W1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده با عنوان "وضعیت بنزین و گازوئیل ایران در مرز های شرقی کشور"
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/690525" target="_blank">📅 08:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حملات موشکی گسترده روسیه به کی‌یف
🔹
رسانه‌های اوکراینی از اصابت ده‌ها موشک روسی به کی‌یف و زاپروژیا و فعال نشدن پاتریوت‌ها خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/690524" target="_blank">📅 08:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6bb48a54.mp4?token=gVuYIUqX0ovy5Plg3uTqgvNELvcP2hHOCvAEo4Img4yjmjE06pJUGO30upoYm0voO0gs319RatVW6A_OLQhq1s2DPvNUCg0yAT8m9Yh1_6C860R0cTu_nioCUmy0nfij_73SBiF2CcxDa0gMZIW0sEN-OyLm4YQ5ne5NxVN3MpVC1e0hEd-xv7zeXwX8Nv12S7_EnSgsL4NSbLNWOTcldUR_wmkbAClipx1KUdCeS2uH2gncAkJ8lyw164i4uwDSPsZzNHdnsY9GpBwfFNLkt9nEDBYrA80-0qvv2eLhToyv-ZVPz2I7LSU5E-c_O3nosnXY15e5xHO2xz4RTkr9MoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6bb48a54.mp4?token=gVuYIUqX0ovy5Plg3uTqgvNELvcP2hHOCvAEo4Img4yjmjE06pJUGO30upoYm0voO0gs319RatVW6A_OLQhq1s2DPvNUCg0yAT8m9Yh1_6C860R0cTu_nioCUmy0nfij_73SBiF2CcxDa0gMZIW0sEN-OyLm4YQ5ne5NxVN3MpVC1e0hEd-xv7zeXwX8Nv12S7_EnSgsL4NSbLNWOTcldUR_wmkbAClipx1KUdCeS2uH2gncAkJ8lyw164i4uwDSPsZzNHdnsY9GpBwfFNLkt9nEDBYrA80-0qvv2eLhToyv-ZVPz2I7LSU5E-c_O3nosnXY15e5xHO2xz4RTkr9MoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690523" target="_blank">📅 08:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpNw4-ebTevakXZI-cRFVKPz67IQzn0ymVbVtOYAp3uRhYCOAyUaCqZXsUTtgOro4N_ZBLwibsN2X6TG7WVMgRPE-E2fhMyM_YN87KoyNJQfAeLFclGs3PUcliO1nKJyiv-C3lEgvp1-8SkS8oBjqQ2et7GEFDvaj541DT682t_1U3pGdfJGe5eqCzFVQ48o6pT_hsRZvpSUQ8nzz9CXFBjJpcqE8rrJ5AW_nJMc3yynVYWjpdIympMH-sMPyVv8y4e85ZGTA6tXuKceKyUZBQ9eSQWt-tou8Cjc5uXWTf47cfuH7lHDEBdrbPys7jDZqJ4nVU6FC_4RqBkHh4DbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
علی ضیا ازدواج کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690522" target="_blank">📅 08:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزیر امور خارجه چین در دیدار با عراقچی: چین آماده است ضمن تقویت گفت‌وگو و همکاری با ایران، از حقوق و منافع مشروع جمهوری اسلامی ایران دفاع کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/690521" target="_blank">📅 08:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
دادگاهی در فلسطین اشغالی الکساندر گرانوفسکی ۳۱ ساله را پس از محکومیت به جرایم امنیتی در ارتباط با یک نهاد مرتبط با ایران، به ۳۱ سال و نیم زندان محکوم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/690520" target="_blank">📅 08:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56039af995.mp4?token=OTbZvdNyWbRdddseKEBSWBBM3xH1SU1ACsYt68vweRG_VNpB3jXcc5FuKVIM5ZM-mrI5Fe46PxwK2uZ_X62jvEb4HCeQAxc0fsYvOVlnS-nvcquvsKs2zg3zrPPhqiO3RfxhOaRsm5TdnfB_ELua7HK5LmOv6cUWxjW9vD-2kWrp-JCx1TLKAW4RVWgbpUcvNwyAH1r8qEnjG5hujJfifISJJ1SYfUpmXaav9vtB1hHzrb6GjNNtLWWQXtuHujd30uVL5pApebtFFCmeKNJ1ckbVY8CRuWDfFc30IQkx0qpLRvhAqlKdB2g5YyiKgJvzM-SVdaOIeikCVc-HLlQ-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56039af995.mp4?token=OTbZvdNyWbRdddseKEBSWBBM3xH1SU1ACsYt68vweRG_VNpB3jXcc5FuKVIM5ZM-mrI5Fe46PxwK2uZ_X62jvEb4HCeQAxc0fsYvOVlnS-nvcquvsKs2zg3zrPPhqiO3RfxhOaRsm5TdnfB_ELua7HK5LmOv6cUWxjW9vD-2kWrp-JCx1TLKAW4RVWgbpUcvNwyAH1r8qEnjG5hujJfifISJJ1SYfUpmXaav9vtB1hHzrb6GjNNtLWWQXtuHujd30uVL5pApebtFFCmeKNJ1ckbVY8CRuWDfFc30IQkx0qpLRvhAqlKdB2g5YyiKgJvzM-SVdaOIeikCVc-HLlQ-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: به پایان جنگ ایران نزدیک می‌شویم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/690519" target="_blank">📅 08:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690518">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeGodohv9_tt4LXACBxH5b0x6Hd_aTwLDo43OQYSxGQ4vL1Jm67DhDjlgdeJAfZRetrq_ZXrTLkulPbMnC7Djhp7Lm_dSZ2t25T_VkjlAnTF7NUbCDEs6emf06W8xNEl8nPHJWjpBG7LIQyFgWJB6i4Y7Pk9_rh1kRJEaIXf6Yj4R7NAvoh5XdCWl2UQIEh8r3oM_vQ2SWzXLdLdBwDEa2p0QTXmzB1_pTRDQL-Nq2alf-EwMMQWijxIe6ogaRCHuey-yQzyIlUnRsw4lpU4SzW1eY-xWujTmVA40LAOmR-YCW0b1kiOKA52v-NqvV_IcglpxtH6IzQJBOlWOGO3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت امور خارجه چین امروز اعلام کرد که سید عباس عراقچی، وزیر امور خارجه ایران، ۱۶ سپتامبر (فردا ۲۵ شهریور) به چین سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/690518" target="_blank">📅 08:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690517">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تصویب طرح تحریم روسیه و ایران در مجلس نمایندگان آمریکا
🔹
مجلس نمایندگان آمریکا طرح تشدید تحریم‌ها علیه روسیه و ایران را تصویب و برای اجرایی‌شدن به کاخ سفید فرستاد.
🔹
این طرح موسوم به «قانون تحریم روسیه و ایران ۲۰۲۶ لیندسی گراهام» با ۲۶۲ رأی موافق و ۱۵۹ رأی مخالف در این نهاد به تصویب رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/690517" target="_blank">📅 08:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv8wUlGzVnA5a5JMcvZBUATfySTMtu5rmJ2HpYl23LrR1-Y4uWREKn4CuMV9O95CZHrqqoI3Icc6fGtLhu1ILkWi4tkCtmKQDNziMizP6FMGdOYUVSrugNlQWVGAjGzMq_pjl3v2F3AXfXKgqQDfyA7s8gN4qKM4VKBgMOo25fZmrjM9bHMM2GQiTW3Nv4j7i2gy85fKhryPEcJoOwSmEja1TNsct7piGQXMeIbuVOJSKDS1GEhf41WrgkrwxhqEK2whB86yYPtYaiZonqk_TEt1SEqcVBADcbVpGd5bZhXBFyCceNECPLhdPNfGUmQSjMTVGjKQpY58bH-MhllY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۶ شهریور ماه
۵ ربیع‌الثانی ۱۴۴۸
۱۷ سپتامبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690516" target="_blank">📅 08:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به پادگان گروهک‌های تروریستی در «سلیمانیه»
🔹
رسانه «صابرین نیوز» بامداد پنجشنبه گزارش داد که صدای انفجار در منطقه کردستان عراق ناشی از هدف قرار گرفتن مخفیگاه تروریست‌های جدایی‌طلب در منطقه «هه‌لشو» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/690515" target="_blank">📅 01:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGFFOa8bvzWp1MyoGKRqQ3yQv-KchPoV9iuov8TmDN3sSp7OqGpgfZNoICe3Fu7YjJ6woe21ZjHV1hM3Y36gN92eEHOY7GXxkPbDZYgNGJQ5swtUPdeGOBEdt2kmAgkOJhYLHKCsd07XPMI40YBvu8ChtjYyRdbaOVBUbr1wa-nvIn3rYUe7yIyvxN3pDqJmDI39SuHxNtpCidgd58nJxlGUOCCrffJy00YEP5UNXAQlIOZlr-LpGBJc7RQPn1fD6ujFK9Cp2cUmhWfYDMvGkggMlnU-Xonn-Uyybyz54yOwlXhff2DzEeslhh-QwCBzmtT658zJzqSIhV_qrscdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
📚
سال تحصیلی جدید رو با حامین شروع کن!
✨
از
لوازم‌التحریر
،
دفتر
و کتاب تا کوله‌پشتی‌های
جذاب
؛ هرچی برای یک شروع دوست‌داشتنی لازمه، اینجاست!
😍
🛍️
🎁
تخفیف ویژه سازمانی برای خریدهای سازمانی و تعداد بالا
🛍️
حامین، نزدیک شماست!
۶
شعبه در تهران برای یک خرید راحت و لذت‌بخش
👇
📍
شعب حامین در سراسر تهران
🌐
خرید اینترنتی:
Haminstore.com
🎧
پشتیبانی و مشاوره خرید:
📞
۰۹۲۰۶۹۶۸۰۰۱
🔵
کانال بله حامین
برای دیدن محصولات و اطلاع از تخفیف‌ها
:
👇
🔗
http://ble.ir/join/DYPXxvTLNv
صفحه اینستاگرام حامین
https://instagram.com/hamin.store</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/akhbarefori/690514" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu5Qe4ZD1CxE0g42cKD6G7qqPwbcNPV5Bzsw_3EMvL9Ty2gSr03kr3bsDRtEeFzj8_BVvoGyl60O752inWuGJhf4xMqfHWVSSA7LUBScdRuUHlR_rWN9JUBEOCgFlbH1kMc4y7odRnbQPZ64Umk7tmK0xfJio_32BV6aBU0BlpFyNjtiQAaSYhZBGR-JhpvVCqIR6jC87ytk8AJwz7zsTqtpQDb5cWYa6yleV0vufmIEMAlkxY-JBS-XquQhrUUpSfCMTwyhllOCBRbhai8fpUwcYwf74E71cL9i6vhXOMrDklPllLbBXYxhHissvfXAJgKsoQ_t-cW2UX9NtXGDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دنبال یه گوشی دوم، سبک و جمع‌وجوری، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت/ منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM/ صفحه‌نمایش رنگی ۱.۷۷ اینچی/
ریجستر شده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/690513" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orGRKXWYD7MFBAjDuakhm8Pv0ZnfcxT-lOPI35JZ7d0ebc332hhBPjH-TBMhyOfFvVp0rqHv5oj4RYXBsPeQl-kF3_j-D0dPt_YMoJTb42Z7li3BBqZoVEvkVGmJjWku3u0OQcxgRPjc2zz5Mg8pRqu9JZDFesXbNx5dCQSPp5FGDFsNizdH-iVW_aczWBmTioK5rllGgXTjpJ3vtLKIxOK0HUELClDVGu_fgxWtUeaAbbGkjz2RkMuLlAeYKzn_9hH-l6trEGPY9SX4-DgXpKfrNeB4Qq2dZYFeb3MedAnRlE93j8n8NAJfbj-Wc-ZlUzE1P5OU7OLvuFFNzU8hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواص زنجبیل برای روماتیسم مفصلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/690512" target="_blank">📅 00:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای شبکه اسرائیلی: عوامل ایران به موسسه وایزمن هم نفوذ کردند
🔹
شبکه ۱۴ اسرائیل مدعی شد دادگاهی در قدس، چهار ساکن محله بیت‌صفافا را به اتهام همکاری با سرویس اطلاعاتی ایران و انجام اقدامات امنیتی علیه اسرائیل محکوم کرده است.
🔹
طبق این گزارش، متهمان در چارچوب توافق اقرار به جرم، به انجام مأموریت‌هایی از جمله جمع‌آوری اطلاعات برای آسیب‌زدن به یک دانشمند هسته‌ای اسرائیلی، تلاش برای تهیه سلاح و نارنجک و طراحی اقداماتی برای ایجاد خسارت اعتراف کرده‌اند.
🔹
این رسانه همچنین مدعی شده یک مقام ایرانی از طریق ارتباط با یکی از متهمان، او را برای تشکیل یک هسته عملیاتی و انجام این مأموریت‌ها به خدمت گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/690511" target="_blank">📅 00:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فایننشال تایمز: قوانین حمل‌ونقل جهانی و دریایی در حال فروپاشی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/690510" target="_blank">📅 00:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRekNYUBesP40CJOO6DKbyDLt9h4ZUIj5DNPV2pJVn4_FEz6QFputRvnngcG8SI32ktYXIwrfAeQGBHUXN5CBLT8Cu3TzFdcJAYsiubcZZYQ6RtP-g452ZusTY9iNtOL-wlx47VanG34tX4Wg2f7mvBqjWbOkwA9EUHVrUYnsesq6N9cMxgPzDDAbw9sF1p2G1andvgaLW-31jKSbCKNAn25vvspLoB9iFgLrgAXH4qukwksncnSeTl4JGqpC3Qi1AsTqyDL53PQIcIUvLc5rSluAlbQ2c9Ekxnw63aYJMnhRU6poFqWpFijd8bgATG5p4rwTCj8ZjvK5ETbT-cnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690509" target="_blank">📅 00:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
گزارش لحظه به لحظه از رویارویی امروز نظامی ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3245535
🔹
موج جدید تلاش مافیای لوازم خانگی برای آزادسازی واردات
👇
khabarfoori.com/fa/tiny/news-3245759
🔹
حقوق در ترازوی طلا | پس‌انداز «گرمی»، سقوط «کیلویی» | با یک ماه حقوق ۲۰ سال پیش چند گرم طلا می‌شد خرید؟
👇
khabarfoori.com/fa/tiny/news-3245634
🔹
جی‌دی‌ونس: جنگ ایران طی چند ماه وارد «مرحله‌ای بسیار متفاوت» می‌شود! | فاز جدید جنگ چیست؟
👇
khabarfoori.com/fa/tiny/news-3245604
🔹
جنجال در پرواز؛ مسافر زن برهنه شد، هواپیما فرود اضطراری کرد!
👇
khabarfoori.com/fa/tiny/news-3245446
🔹
خبرهای منتخب هر روز را اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/690508" target="_blank">📅 23:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbqnnV-LDifMsi3NZAshPaT6KSNiiMnNA5RxY8vLieAnM2q2XWWG4fdt4ugi5CIpgDWmJGnmVXfQAyw0GHFmEjALQrU6oiTJru-G-vJvuz5y4mWucKY3ujpBqmq0nk7omrmW7WeULFo_p43iIiUf0oWQQHQhaA7tWijTXytdc8ZRMpbUe4WFzDncSDA5O36nw9hBsYGTxbwFxWHiY7A9imQSjnn4t5kxDwgCPVeixKhRAwvFXW6QIGGaBLpfi087xLjWXbAZVzQDsRcRTY4VcmS36shvvaaad_KxfkvPMaNnG2lMk_-ulkpbp3qOwWt9j8CfYB4Gx8SOemDhzcvYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی امریکایی: جی‌دی ونس می‌گوید که در حال التماس کردن به رأی‌دهندگان است تا در انتخابات میان‌دوره‌ای به جمهوری‌خواهان رأی دهند: «به ما یک شانس دیگر بدهید. به ما چند سال دیگر فرصت بدهید.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/690507" target="_blank">📅 23:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=OhBqnMajqDAQo0YI-2gbViy5wBZnYLqrT3upDGbIsHZ1Tlvp-qpZMjD9BJYDJQjYCm0xkJhBYjjJMd885WOO_RM1T6PVUjpLGiNL-90AlR_T_ChtFdTeMxUaKX-54HTEgZY9_8FmMksmfS1WvUlRnviQgUuyvrZ-8Hs_U7ifIEed5-Zs9x0NVUXr8VkoXX3mGGHuDxDPtSZQiDWs9_2T37J_mMJ8Y6AgblSsfaXVvex00MVennALvZmk3IaKJmgAp4YH31utw3FFbA9cyNnGvpQr61wY2WoZgEAYfIlp2EvnVd8JR_FaOWsPFdCEiJKVhEg84JAdzyF12h0fIFkp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=OhBqnMajqDAQo0YI-2gbViy5wBZnYLqrT3upDGbIsHZ1Tlvp-qpZMjD9BJYDJQjYCm0xkJhBYjjJMd885WOO_RM1T6PVUjpLGiNL-90AlR_T_ChtFdTeMxUaKX-54HTEgZY9_8FmMksmfS1WvUlRnviQgUuyvrZ-8Hs_U7ifIEed5-Zs9x0NVUXr8VkoXX3mGGHuDxDPtSZQiDWs9_2T37J_mMJ8Y6AgblSsfaXVvex00MVennALvZmk3IaKJmgAp4YH31utw3FFbA9cyNnGvpQr61wY2WoZgEAYfIlp2EvnVd8JR_FaOWsPFdCEiJKVhEg84JAdzyF12h0fIFkp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آژانس بین‌المللی انرژی اتمی چه گذشت؟
🔹
روایت رضا نجفی، نماینده دائم ایران، از رقابت ایران و آمریکا در آژانس و اتفاقی که معادلات رأی‌گیری را تغییر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/690506" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: یک پهپاد RQ-۲۰ سعودی را در منطقه حَرَض در استان حَجّه، نزدیک مرز عربستان، سرنگون کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/690505" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3kNlMLnIpKijpSj5kPcHj1I-Oybd9soahkIUxIyuTndRbBd0yDC5WQfoUnOzEcnsNS9jX9HLf7B-sY9uYIXk30EPFBIyp6TtXuiB52f4qpD5Z5bYBuSf8WqTJuvsLuQWjUo_j6RjJnZU1W3AuOJ1FmT47IEd-4YjCac5rGMxR_C_OhReGPlbY-RO-N4WzPoBydRvSAXckOlcV_df-doEmOybEy8LurrvUmgbEV2m3k89LBE1aWIJbd4lKrgnbVuEAV2kZNLvtYur9vM5-w2jnHpsJXPNXCzT6Hz7fzXPWDvd8cj8W20sX5bIZzXAtNbcsXw0LMaEwW7gemis781Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکارگاه
🔹
سپاه اعلام کرد بامداد امروز، پنجاه‌ودومین فروند پهپاد MQ-9 آمریکا در آسمان جزیره قشم رهگیری و منهدم شده است؛ اتفاقی که تنها یک روز پس از اعلام انهدام سه فروند پهپاد MQ-1 آمریکا در یک روز رخ داده است. توالی این موارد در روزهای اخیر، توجه‌ها را بار دیگر به توان پدافندی ایران در شناسایی و رهگیری پهپادهای آمریکایی جلب کرده است؛ به‌ویژه آنکه MQ-9 یکی از پهپادهای پیشرفته و دوربرد ارتش آمریکاست. تکرار چنین رهگیری‌هایی می‌تواند بیانگر افزایش کارایی شبکه پدافندی ایران در مقابله با پرنده‌های بدون سرنشین آمریکا باشد.
🔹
هشتصدوشصت‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/690504" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaclsMG72nOc_c_XsjSQsDIV0-p5EH3l9od5DiDFuI-xbvJQgwywF5TDOk3d5GOTGTu6eldPeBa3zyNR0Tly2JXpvAlD0tB1p6sygbPcxkCEiqVyZdrTXQUFGULJLy5V1ZBK-JVVocgeQA9CEZMaqbLfJYeRP3Ldhrgu2aR8-3iUE0FoD9G4rJllCKvxMU1XXLeBgHqCX9gshVoyXs_SVmpayxJkXsWcDSRXVcR5kaPJAHKqOC1SU3ZkHSg6WkvSfmAMbA1gXSv1o1rqHcPpBRxSZHngdUM4aaLXJNFe_vdHIXtbBgBw3wVgSAPWSoHeIveI21TmEwy-rwzC0IdVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری هادی چوپان: پاینده باد وطن
زنده باد جمهوری اسلامی
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/690503" target="_blank">📅 23:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6527a4f926.mp4?token=twn_piyDLK-YT8778u-T0eWUkNHtn1PXM0qK-Cthx2A9IneAiN0NQdX2bsweHGRKDQBS1PbnDh7LC4oCSi0Uc-PKXQGuOYrzf7QZhkt4IgfHtS8yTHL0LMISf7HnK-X5_NmyralTHWNEK-uhz1ZCq7JVQKkJub7pQwQIBa8sT1a-L3msoNJKfR_Kes0CvZgPEc97p-Z3J-Ni6OOw7-qqN9kxjgXeJDeT2_w0f-P-sOQQGUCFMfvIfmMtdHJVy0hc636XFwGlBsMXMYxAiHHlTuHAcKZzx-7tih4S5s-WlQZyLHGzIkd-VuP8oRFZFLRpN2Yuj4Np7Hylv305p7s0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6527a4f926.mp4?token=twn_piyDLK-YT8778u-T0eWUkNHtn1PXM0qK-Cthx2A9IneAiN0NQdX2bsweHGRKDQBS1PbnDh7LC4oCSi0Uc-PKXQGuOYrzf7QZhkt4IgfHtS8yTHL0LMISf7HnK-X5_NmyralTHWNEK-uhz1ZCq7JVQKkJub7pQwQIBa8sT1a-L3msoNJKfR_Kes0CvZgPEc97p-Z3J-Ni6OOw7-qqN9kxjgXeJDeT2_w0f-P-sOQQGUCFMfvIfmMtdHJVy0hc636XFwGlBsMXMYxAiHHlTuHAcKZzx-7tih4S5s-WlQZyLHGzIkd-VuP8oRFZFLRpN2Yuj4Np7Hylv305p7s0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توییت کاربر یمنی: جنیفر لوپز در حال رقص در استان مکه در ۱۹ آوریل ۲۰۲۵. ظاهراً تقدس مکه در آن زمان نقض نشده بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/690502" target="_blank">📅 23:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a954fa76a.mp4?token=U4avpNARZFivAzj3NO5RpKva0OgnrQUWBoW5VWUv2J0yKxrz1sJgA9gIubcazarLr89MNPdvRgYP5WSeYINDiMmFirQ9FFWS7axp5kBrRcvomv6E43mneZHMjzvZVjyaB0sx1AjL4lHs1v06AsBjYZyPpTJjeuTiwO-9z4vTzFG25MEWAm7zNqwNtzzTcuo6o9lg2xOotrsbB9AgVd9Audx4fRYVQ5odviV1RFdEd5Scwe47vfXRupLlGH9E1R8fwM-bfgjVt039zL2Cpf2kXib71TwmbGoaO5pc_RJkVe6tP1v2ddHontRYzZzB5CVdziDVr5TKaIy5NUb53SkBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a954fa76a.mp4?token=U4avpNARZFivAzj3NO5RpKva0OgnrQUWBoW5VWUv2J0yKxrz1sJgA9gIubcazarLr89MNPdvRgYP5WSeYINDiMmFirQ9FFWS7axp5kBrRcvomv6E43mneZHMjzvZVjyaB0sx1AjL4lHs1v06AsBjYZyPpTJjeuTiwO-9z4vTzFG25MEWAm7zNqwNtzzTcuo6o9lg2xOotrsbB9AgVd9Audx4fRYVQ5odviV1RFdEd5Scwe47vfXRupLlGH9E1R8fwM-bfgjVt039zL2Cpf2kXib71TwmbGoaO5pc_RJkVe6tP1v2ddHontRYzZzB5CVdziDVr5TKaIy5NUb53SkBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجید شاکری: استفاده آمریکا از بمب اتمی تاکتیکی علیه ایران، قفل استفاده از این سلاح را برای روس‌ها و چینی‌ها باز می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/690501" target="_blank">📅 23:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690499">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=I5wa30zWy4f7xFmhYLYXkxqjNjErTMwwwBk225Za2ddnU1naaXBkYyfnVtLvLv_YYCm7q1Sp_EvaB99M2qwnPxfg2vIK5DbBHN0mZngp4H3Nn66NnTfoSdoP_sV2Oy-wJkp8ka5kpQPbONfTo1WqeuVM_LKbNjJVBY6-isDlNo8QiFgSfy8WH0Ecg-HzyvKUl2VOkDziCU6ApPjdV1cSp3n1jlfonZ4pHCg9RYSZzDZiPqCGavjG2GVzEiwopaPqmf5pj440KpdGfYlCm7QXzfrmkVLDOIi9joM_Hxg_KUnUBQtuZg7rWRKCGMRsKroLfNPJBT3hDpZXQIrKe0rLvGKQ6YRmA7UTeGHXx5XTVkwBW8noNkUzbJSGDqxVUucVMIXMnkcjRG4bcryDBQa7Qrj7XERUkDrRPAzyoNs5D9J47vB7sJzl6PJB61t7NWkGHBWHzYsU-tZmrVjFR9hcKCWrgfwVZre4PgqiP_nJ-xrMwmnD0c3iKQuGIHFjjX2aRVKjmB9RO1Vp1MLrAB1u4a5bJ4OBWuUgz6eaQvDsCIpf_AZyOILU3Wkw3Lz6hip8uxHyMiyPMwc577Zo1DXIzcm9GcfTuZe0xDP-1yTuvE7P7d83Y1v7RE7fkcBTRUIXOd9KvHAKDiQXcOLIlGeDLUI73HXTiDRAGBnrEIOC9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=I5wa30zWy4f7xFmhYLYXkxqjNjErTMwwwBk225Za2ddnU1naaXBkYyfnVtLvLv_YYCm7q1Sp_EvaB99M2qwnPxfg2vIK5DbBHN0mZngp4H3Nn66NnTfoSdoP_sV2Oy-wJkp8ka5kpQPbONfTo1WqeuVM_LKbNjJVBY6-isDlNo8QiFgSfy8WH0Ecg-HzyvKUl2VOkDziCU6ApPjdV1cSp3n1jlfonZ4pHCg9RYSZzDZiPqCGavjG2GVzEiwopaPqmf5pj440KpdGfYlCm7QXzfrmkVLDOIi9joM_Hxg_KUnUBQtuZg7rWRKCGMRsKroLfNPJBT3hDpZXQIrKe0rLvGKQ6YRmA7UTeGHXx5XTVkwBW8noNkUzbJSGDqxVUucVMIXMnkcjRG4bcryDBQa7Qrj7XERUkDrRPAzyoNs5D9J47vB7sJzl6PJB61t7NWkGHBWHzYsU-tZmrVjFR9hcKCWrgfwVZre4PgqiP_nJ-xrMwmnD0c3iKQuGIHFjjX2aRVKjmB9RO1Vp1MLrAB1u4a5bJ4OBWuUgz6eaQvDsCIpf_AZyOILU3Wkw3Lz6hip8uxHyMiyPMwc577Zo1DXIzcm9GcfTuZe0xDP-1yTuvE7P7d83Y1v7RE7fkcBTRUIXOd9KvHAKDiQXcOLIlGeDLUI73HXTiDRAGBnrEIOC9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
این
طاق،
جاودان
است
مرمت
میراث
فرهنگی
، ادامه‌دادن مسیری است برای حفظ بنایی که سال‌ها بخشی از هویت این سرزمین بوده است.
پروژه
مسئولیت
اجتماعی
بیمه‌بازار برای مرمت
مسجد جامع عباسی اصفهان
، حالا وارد مراحل بعدی شده و عملیات بازسازی در بخش‌های مختلف بنا ادامه دارد. کاشی‌های آسیب‌دیده، سنگ‌ها و بخش‌هایی که بیشتر در معرض آسیب بوده‌اند، به‌تدریج در حال مرمت و استحکام‌بخشی هستند.
بیمه‌بازار
؛ در ادامه پروژه مسئولیت اجتماعی
«
طاق
جاودان
»
، همچنان همراه این مسیر است تا سهمی در حفظ و ماندگاری یکی از ارزشمندترین آثار تاریخی ایران داشته باشد
#مسئولیت_اجتماعی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/690499" target="_blank">📅 23:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690498">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b90e4877.mp4?token=RaL8GtqYC49wGDNcGQleG7bUm4nhdByoLDqVTFAulHf_bhpUm2PRbSjBHp7Sgw0U8juD_awqy_qcngkX31UKTD3cQ4u1WflY9hmHclwaGIhIjLLYVHVF0K3q7PKNNk4ZDQxjEU7TRXg5I2jN281A9GJnokUaO0Qw6bhY4uRfH0uj4PUd9DjOogw3TjYdnq_h6drNm-3qz732h_RnQiN-55gs55XDLpefbcoOth1tX4VUfjxz00gGotFgoV8IKOvK0s0gI8uxAgoGGJttgzkdmn084sC66twPR7CDM7h9481EuuiYNEInKL57Hl3V_UF3liKviIJTkUND9JL-ePIBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b90e4877.mp4?token=RaL8GtqYC49wGDNcGQleG7bUm4nhdByoLDqVTFAulHf_bhpUm2PRbSjBHp7Sgw0U8juD_awqy_qcngkX31UKTD3cQ4u1WflY9hmHclwaGIhIjLLYVHVF0K3q7PKNNk4ZDQxjEU7TRXg5I2jN281A9GJnokUaO0Qw6bhY4uRfH0uj4PUd9DjOogw3TjYdnq_h6drNm-3qz732h_RnQiN-55gs55XDLpefbcoOth1tX4VUfjxz00gGotFgoV8IKOvK0s0gI8uxAgoGGJttgzkdmn084sC66twPR7CDM7h9481EuuiYNEInKL57Hl3V_UF3liKviIJTkUND9JL-ePIBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی پویش ملی جانفدا: در پویش ملی جانفدا تقریبا همه مسئولان تراز اول کشور با هر گرایش سیاسی ثبت نام کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/690498" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690497">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd3db3e8f.mp4?token=czgPKmvK4JQz4JdapGeIPE8TRaPN5-EOsCW3TTwBjo2Lzge5muYcrrnKIg0qOqc0wMuzzNoKuklEGM9VdrhHOFB4FzOj789EHyacmhd_Em4basdO6GW71_1ddnSgZWfBKR2kYOY3xIs9vCZHeIDRrE5FwnpXRt7xY_HiuYrl5Sc7IUKaQS6DVdH6YXUSf29__eEcrhbKkfenBCRYRJSMOQI4OLgkK7_TJchaUPJXJdfLJwHNWWJRaGgEJqzG8yJaY0LTtK3QZXC7FZKcQJCED7VCcRrWP2NVyG7GBWl5ThsfR3K8-8CG8zg8VoJrkHvErM1Zw62jlLzIO_ol6YOlykA1sZJMt_8W7xR3sqw7cOaWrJJ6BSqBf4yvQawmj0pLP19RWH279jp8vbdO8GDsA7DyAU3TG3nawBss0SCU9Y_KZUdy5kwQgiTHcA-P77uglVyyq2jh4gkqsA0HiO6vRcsPRES66s_4zHzqxHMkN9Q1iYXAo_FX0WCSYIx2mv_Rmk7-PyYXpe9duadI-nfZtl2tPr_KzGR-Z35QwqGvjbHA6EJvi8XujVkrzZfk_GZWHadfObDTHV-LBjprXoWe4aoNayFmJ-s-oXOUES9sRX0bcleWBzpM-sfYGr-DkabcCYtnq4klZguOD6-HORlo0Wfu1fMYe6Un5c9qJwFnvDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd3db3e8f.mp4?token=czgPKmvK4JQz4JdapGeIPE8TRaPN5-EOsCW3TTwBjo2Lzge5muYcrrnKIg0qOqc0wMuzzNoKuklEGM9VdrhHOFB4FzOj789EHyacmhd_Em4basdO6GW71_1ddnSgZWfBKR2kYOY3xIs9vCZHeIDRrE5FwnpXRt7xY_HiuYrl5Sc7IUKaQS6DVdH6YXUSf29__eEcrhbKkfenBCRYRJSMOQI4OLgkK7_TJchaUPJXJdfLJwHNWWJRaGgEJqzG8yJaY0LTtK3QZXC7FZKcQJCED7VCcRrWP2NVyG7GBWl5ThsfR3K8-8CG8zg8VoJrkHvErM1Zw62jlLzIO_ol6YOlykA1sZJMt_8W7xR3sqw7cOaWrJJ6BSqBf4yvQawmj0pLP19RWH279jp8vbdO8GDsA7DyAU3TG3nawBss0SCU9Y_KZUdy5kwQgiTHcA-P77uglVyyq2jh4gkqsA0HiO6vRcsPRES66s_4zHzqxHMkN9Q1iYXAo_FX0WCSYIx2mv_Rmk7-PyYXpe9duadI-nfZtl2tPr_KzGR-Z35QwqGvjbHA6EJvi8XujVkrzZfk_GZWHadfObDTHV-LBjprXoWe4aoNayFmJ-s-oXOUES9sRX0bcleWBzpM-sfYGr-DkabcCYtnq4klZguOD6-HORlo0Wfu1fMYe6Un5c9qJwFnvDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از اصرار مادرزن تا دلهره‌های پیش از ازدواج؛ گزارش خبرفوری از جشن ازدواج ۱۱۰ زوج جوان
🔹
۱۱۰ زوج جوان تهرانی در جشن ازدواج جمعی گردهم آمدند؛ هرکدام با یک قصه متفاوت، از روزهای آشنایی و تردیدهای قبل از ازدواج تا تصمیمی که در نهایت آنها را پای سفره عقد نشاند.
🔹
از ماجرای دامادی که با اصرار مادرزن‌ در جشن حاضر شد، تا  دلهره‌های شروع زندگی مشترک و زوجی دیگر که با وجود همه سختی‌ها، تصمیم گرفتند برای ساختن آینده دل به دریا بزنند تا دامادی که تعداد سکه های مهریه را فراموش کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/690497" target="_blank">📅 23:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690496">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
معاون پزشکیان: حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷ میلیون یارانه به هر نفر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/690496" target="_blank">📅 23:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690495">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14519dfcfa.mp4?token=PE8_BntYbeXp7d6-mkonJLTo-8_NWgCl4Sc94GZaoPWWYevsxf6YEzOkcP6YjhqdUzOBmkBUlAx5-nYaE4H1nRyuH6SUr4zD7yPH8ftjsaRC5K5fr_Vq2hWjKKGiklgDej_lXLLj9roytxZ8_pDMTO9YgDlKzt8RbJ1TfZFpeyNLlQ_ZWt7v28P2TmlXW-Am-0axOT4BmwNH2htRDimMCviUunilMjLs88mZYR6odJFAZ-LMH0GhTokyAA664ye-KFOQxcvVfCjleV3gcbs2S8fzGp0DlKSORKXYfPJCIlAde3IXpYs2WAaDjAdv2AlRD5Z-ZYAn85p_creAvJQo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14519dfcfa.mp4?token=PE8_BntYbeXp7d6-mkonJLTo-8_NWgCl4Sc94GZaoPWWYevsxf6YEzOkcP6YjhqdUzOBmkBUlAx5-nYaE4H1nRyuH6SUr4zD7yPH8ftjsaRC5K5fr_Vq2hWjKKGiklgDej_lXLLj9roytxZ8_pDMTO9YgDlKzt8RbJ1TfZFpeyNLlQ_ZWt7v28P2TmlXW-Am-0axOT4BmwNH2htRDimMCviUunilMjLs88mZYR6odJFAZ-LMH0GhTokyAA664ye-KFOQxcvVfCjleV3gcbs2S8fzGp0DlKSORKXYfPJCIlAde3IXpYs2WAaDjAdv2AlRD5Z-ZYAn85p_creAvJQo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته‌شدنِ دو نفر به‌خاطر یک آینه بغل
🔹
در پی درگیری یک راننده خودرو با موتورسوار بر سر شکستن آینه بغل، موتورسوار پس از تعقیب و ضرب‌وشتم جان باخت. راننده خودرو نیز پس از صدور حکم قصاص، امروز اعدام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/690495" target="_blank">📅 23:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690494">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx5WzG0CPGSwRU3rxdh2E1tiWlw0tZJFMWGZPNB0GiDtt4Hkrgo6VNsbC74MkYSY6MyE6v-O4Kh1aAC9_b0MAbkL6ZyS57NInDsqUJd9vY-dF8X0AUuuY7hHV0EEmxhO30ZTAcZ8oWTCh3wQEGf22AUi_i42TTSTdXp7Fn5ngvgT92pFNQwQ2fnYnedPVDuO70sSd-ggUo_qVMmpYb0vfTjF8w5UIOCROM1xfSPUiJtqA50D5D80eSwgmNChkKrkDSMyKqk8fuMrrHQqvswv5eJOQBjV18S3jsgBz63r9Wi6aSOO-a0SEANv8L2ynuMpHPAqyT04Rb2Qjb9uTwzvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار لوازم خانگی و جولان برندهای کره ای؛ جنگ ایران و کره در قلب "امین حضور"/ سلاح خطرناکی که علیه ایران به کارگرفته شد
🔹
ممکن است بازار لوازم خانگی ایران نیز تبدیل به همان سلاحی شود که «چی» خواست از طریق آن، چو را شکست دهد. در واقع، وابستگی بازار لوازم خانگی به برندهای کره ای می تواند همان «گوزن خطرناک» باشد یا مانند اسب تروا عمل کند و مخفیانه اقتصاد ما را فلج کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3245776</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/690494" target="_blank">📅 23:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690493">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf0d19b22.mp4?token=LfMC8igxToL_itlaS-AzEED_uFgukgJ1_o5A8SpLeiaastS6uvu4Rgg4Ceo7EU8VP0vAgPBaZlosmZu10odHXdVgHn_BBdnXoGVayybPasp3pmEmJi6oYn9T1IiKkTiezDmL0xT8Y09Pw2mtKMH5CnJSIKqphIHlNoYSXgUnInUIUIA2ETaMscVgLbUiT7BF3-A6lC8d1t6tiHHh_he9d3tzNWHPfKBIxU2XTjz7We47QgjYiyIXbfMMPEzCpOFrN3FcEROs7jZ1jgxD1NhmtPMGRoNE_Nso2WSaVpbZtr71iOn1zlac-C6z1_JE8iHyoVaKctkEfG_SIx-ks7eNVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf0d19b22.mp4?token=LfMC8igxToL_itlaS-AzEED_uFgukgJ1_o5A8SpLeiaastS6uvu4Rgg4Ceo7EU8VP0vAgPBaZlosmZu10odHXdVgHn_BBdnXoGVayybPasp3pmEmJi6oYn9T1IiKkTiezDmL0xT8Y09Pw2mtKMH5CnJSIKqphIHlNoYSXgUnInUIUIA2ETaMscVgLbUiT7BF3-A6lC8d1t6tiHHh_he9d3tzNWHPfKBIxU2XTjz7We47QgjYiyIXbfMMPEzCpOFrN3FcEROs7jZ1jgxD1NhmtPMGRoNE_Nso2WSaVpbZtr71iOn1zlac-C6z1_JE8iHyoVaKctkEfG_SIx-ks7eNVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با کمی خلاقیت، توی خونه هم می‌تونی خیلی راحت این‌جوری فیلم‌برداری کنی!
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/690493" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMy5p_3t0e7JevOVn5FU4taFJum3-xY1hGOJBPE7OsUhJ8tMu9AQQGDXYB7PhriASt500XRYHx2e13KYS1pSpJmoYqBEtUgzHl2ve9GOiJixLDztDg-dKUE3rSxTZ3wNe7kkm17xuk7WpWRsTlesnYPI8h8hIEl6eHNywyEiL0vJjURDoNxEz8SYtQ3NPOnnkz8VzEpY45RnqBaSP3oVx4p_GMYRP7RR9Wvf9ktMKCE-XFWkr8N3LxymS8bWJn6eAX4VskjlPSJVHEpQS8d_r-whKydAg9fkjX8C2RupUZrQChi69jwi_YBKuREjKyq9tYqq-HAxeBxjibVQylsbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اینستاگرامی ایران ۱۰۰ برابر شد!
🔹
بازار فروشگاه‌های اینستاگرامی ایران طی سال‌های ۱۳۹۷ تا ۱۴۰۳ جهشی خیره‌کننده را تجربه کرده است؛ به‌طوری‌که ارزش اسمی این بازار از حدود ۰.۹ همت به ۸۸.۷ همت رسیده است.
🔹
بنا بر گزارش مرکز تجارت الکترونیک، بررسی ارزش حقیقی بازار با حذف اثر افزایش قیمت‌ها نشان می‌دهد که حتی پس از تعدیل تورمی، بازار اینستاگرامی در سناریوی کمینه بیش از ۹ برابر بزرگ‌تر شده است.
🔹
در این میان، چهار حوزه مد و پوشاک، خانه و آشپزخانه، هنری و فانتزی و آرایشی و بهداشتی با حدود ۵۸.۸ همت فروش، ۶۵.۴ درصد کل بازار را در اختیار دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/690492" target="_blank">📅 23:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi6JgxIW0D0V-mbdo0zcU4H7W1_QRMmb6L3gRmg5Yyw6DyK0Qy3VUvPQWBQz5cSqARdM-G93CjHmkga8vozt15g11LZWE3buZP3bmuTEujMjL5Ezf1F5wPpC41ZNQPfpjeAX7x501KYlZT411h5F783yMh7f4E5JV-GKcaS252aewYc6yHUW9FNuQSXpWS2lrrmdU0a-L_XpXTPlSGre8nb6c8lX97cbhwPYyeKdQyjJawrBkRqnQf6S-8uqddy0MqUIe1sjSCmaodgXZ9a1XHmD3aV1WMIgDSgFqd0AjM2eSHf8A29_JG35-8448LAvgMDuSTRjbrDzKfP5mno0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۵۰٪ تخفیف برای تبلیغات حرفه‌ای!
یک پکیج، حضور در ۵ پیام‌رسان و دسترسی به بیش از ۲.۴ میلیون مخاطب
🚀
@Titretejarat
📱
روبیکا | ایتا | بله | سروش | تلگرام
اگر می‌خوای کسب‌وکارت بیشتر دیده بشه، این فرصت رو از دست نده
👀
🎁
۵۰٪ تخفیف ویژه برای حمایت از کسب‌وکارها
برای اطلاع از جزئیات و قیمت کلمه‌ی تیتر تجارت رو بفرستید.
@ads_ghimat</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/690491" target="_blank">📅 23:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VefXz03x0Ha7gy4DqMRLZ94t2x4OjFghHjZuT1lTgNjDMA0T1RqhDFG-pL4Z9FwXkDvSSfRZ24dBO2xgLUcTq2TQBEINfWmV1-iLuLwmfJblLasNqKls1gLPeGl6hRRSY00VZ12GslEJDXRyit_wI0FgF1tuAS8a2DFErQ4AVkoHV47IP4-MsFdkpAXDxSPqW5SWL4alF4IFR0BI6tl6WZd2t2trfIDXNGBttEGgtahqY0Z8Qhp5O_4o3QvER7wKFfi-TMFOUQZV0P5mRLSEH4SdaNC0dBLEqFC407UlZlqEm2EnYFCqoPD8IuaTRlLum5K77zAxgpG39FDFd8jbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/690490" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFTgRxbYu0BAkuOkHFJHGu5RXr31bGET2W1O1BcYFovD3eizHxDnxxCDuCXt7Q-LAXpZEAzoDewelHZy-6a1MXAuGy7vXrltMl9IF2nH50eElrxETyHLZKVCyUfI3fDZL-378FtmkyCDg_5PV2emGlDNATPJ3RtLPEp5CA9wXHETKd1b5cztgSfZ40KdD6LNSX-0KAv-1RoCYNmJaOiH8-4jyYKVo2YGQ1cIZUA577EF8iKsRfUty4uGhP2GGWeScZobYSB5DWqOFIrANBUVkLUwAMhXw2ekwL9H5FM3pMyXU0k4z4chekAVvRaHv-Pd_a_3Y1u9I9edI-k_SkzuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی آکسیوس، رسانه همسو با صهیونیست‌ها: اکثریت افراد ترامپ را فردی خطرناک و فاسد می‌دانند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/690489" target="_blank">📅 22:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5L75oKA4x1wg6z4ptUwN4xZ6d41twlfmWJoEz1oFPMZmUaNqZzNJTmWyj-KKsWMQCI0XokiZ_8JWlUJp6LSfCTZiAY-KceQIBvy8-vQmDl9zOqDMXBAX_FpD8HeLZ1Ai2nGN4IvQ9gtm81XuGrcoxPnIn0eUVlQqtqf_EIRuwL-WvIMklnqkySQvleddTANRZhiosIYieBueholEdDNSDyrrFas0odxHe2O_jLjFksVull7anLiEXd9WT3uXmee2e9BiJ3IX0ONQaUFqqw1kde-uPr3lneB0HRazfiYwHsSc2kq3fJOUt2z6ImabYXsYfKaOEuMRfsVHBT5Pl3xwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوانه های پر خاصیت برای بدن
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/690488" target="_blank">📅 22:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvrfCp8LwGLA827rTZgG2awYlKAqbhL8z2LLxqX-4zTF7HH03D9wgYXZvVNByzua7jPSHqrhtyMk--cVTC4f7uSRocYxIl4G3E64eH7uY3etqTChUZ2x1PsbnZg-CFZqQSt2nvb9kBmJkXnz8iuO8JPHhgaN5QkNQLKxVQw8bEFvEecjM16a16nIYc17ymvBSZ8wRIAq56oD0PuVaOzp82gD_yx0pdPaCe1l6vNCdGoTopP9Wgdz-lYVoNyFortx0w9TECKhMqQD8z824sJsCYN69ul9JNSi2QbZ5T20CXbQQtwveQn1XwZB94yB3LH8sx4Dq2sEZvISLGXFiYP3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vN-vnHph6FoSdVzGGq5by6XQ_6gVFu1Dg_Iiw66iGqhZm6AMNZ_LnKiMRemk9LpeX80kxkb57tnDCcfm7DeBwgvdsSN4iaFQeVObicJkA_MkOwpB6aLchy3XCE8KRsrCB6V4ZcxRDkZqkevWk1KShumB07QB-IEJZ8bT_YyNS2t4qBQE4SvOc72m9w865oYjQQFRD3i-ywH8kS3A60px5OLxEiN5YrztQBowwCLGf0e159NN_2D2HAXWGjz0wvMDBUTL-z0UhoQ6YeWt-Zn9jUPEhjfLB1KDv2fgsYKtb5noq3DfwQCSeiZGQ8Y3q1nBd4Lxj2jXTh9wQ9Peq5VRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ji0Gz0_V34cxIniyWEPZATVhZWKfeRjJChBp1iNp3bITeUfuLjWgM1B1hW8eKLUqAwNMq1GT-5kPPusnSrwMoiuSD4eUrJ4Y959eiZsrO2_Ays0AEb82VLkg1rCC-QQEI_8lzWpi7JkkjJX6734_neqC8PaIMRrj6jenINapjfuS7p4mGVufgvNBqtgxCRaK66FWDJpzPxWGXyxoeTKT-7MlbXKNSNlmO3shMohfebODluHwU8SHZcrLb8dA7RXae4JjVLEbzpkMcu2NgfmGAI03W3mTtLFXM4Yn87lUxok6KaWN8zOPyUQphozfiiZr2-PDwB6W5QBxE5Wn1s3W8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qunl32VWU9hb5pfE75Q3bdoWIvwlTrMpWoMX6vSH3Pq4ib3YQZpWOIjeeYwKI6dTm3zCci_jDtLzCX7slZMoRHE4pgb_soq93uYhszXKg9LPc3Y5gvxTl8ZoiMETybBQ2yhVhPy7tNmUwZhC2qvRrZySdfCeNR9xWAkcmrdq8opsWIQ9mDihL-7OGuU55rt07lCe_apZ5h6_E01qlYjeoc2GuuHnNrjVdmxpKtZgPY771oFk6wyuBy5QjidpP8Q5tryrzUgNyaAJWF3zPRDIIOgOvEigAHu00GXprBqhP8At1OCGGWexw_b90rYA34y3qESU4IVpvgzosC7wDHvnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e72jRaLq8b7SsO-YJLwkq9ImDpZBx-QGh1mHg95b2b8EFpf6Ih32ODO5hhKMUM9p09_d8Eh__oI0HzMf1M1l-pwCjaJO8eOEA_VCvVNPtigtInE8yF2V1zjLOcjge2J53Z8T95uCaRXuT80hlTFFKXlAlq40p1JWFC3Pc7hkIrVHacnfDdfV-MVSE9a1qI_TjMHgXlcRPY_JaokmPi0R1SaDaHEPh91eYcE6EcwicA9_IP5lflB3Cl780gZnCOp1LS0YqjljjBa9W6RP84yxWJA54D0wubc7x5R4g85hy2QpM6A9Oi2krCkJef0KCLzmBGkpMe2jNHqzjDY21V393Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7fbqXUo5UXsh9HVy14XG9e3rosst76l3NqKROl90ADz5w3wMBR-nszVOcbbD-Yu913HlF8iEVhSn4e5Cf-fRI9oVwRbqEcJ_tNZqlqino2d34FpcydCfylPdmG7vx2QrIkMn0qllcmJSRmo7hp1zsvgmNi9Kep5i-rG6JPOlG1gTzKYewxHpj1r8AN_ACgKaLr6zzb4cv721hZEgJvoch2NPulS92T5UQMaBCtrLWpP7glw5B_upiMneZxi8UatHScbYHicFmQ2YOZSaUuTnko8Qz6NlK-f6OukCjkHwMs1pQhJgkdrfcweD6Ju21RDrn9ee9MwjVf6DNcIUmwQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvupzSUYvD5NMcTc1coa-WFc8gLZU9ydgys2Nmqel8nx7MoGyYsGI8HECRBFioI6gn7sxmhf0SbwhvlgVTkYpGLmihXNSWPd6oUzEzcjFUW8dw0VvXDRPgF9X7upboGwNZaM1p202ahfa3iX6jupIxMLQq4t5NVj-EzARfSU9Yc_D25pdgActrsQcd2DDgqLUZ6q7knmbYkMWRYL1uGgtRhUVBddYlzFk8Eib0EaIKMu8QhXyUtslekEm4mXKaYk6v1ILSUtwu1GjYyEaX1_aWe54yC32IcOysBzAo-4sDoWhwj7oEZT3l8wEDqs0Zn428pd6jTkLhyp1bJnZJiWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnj0N2yzE204C7iBvdFa91LhVuZUEKZrVsef1uFFfjwiH4IZdrIKTCvt1dm7vL-H2FAZUKGMGJ95iMHi7fl41E8WdGVsFO6hP-i6_2hZz5G1UtWowXn9glL6Ff1hBsEasdhcQ7xaKTcnU6tHV48Z7WUrzeE3a8uVBat-FE11W101ltqoNmoGz-xcdMhjdFKFTU_nWO87uIcLGbGfHgRu9pZg9YdIP60kzO4-XlOeKeUFI4BQrUL0z4uNglh3QILACSxb8l7z12-svJlzRjkpsjvwf_UpEi9y5AStJs_r7k6kAfWfOA6DexumcH6a8RNyA6dbPs-4i47vqTWrYjwztA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس پیام‌ها و مشکلات مخاطبین الوفوری در آستانه بازگشایی مدارس.
🔸
روایت خود را در قالب متن کوتاه ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/690480" target="_blank">📅 22:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آمریکا رسما بالا بودن تورم را تایید کرد
رئیس فدرال رزرو (بانک مرکزی ایالات متحده):
🔹
واقعیت این است که تورم بیش از حد بالا است و مدت زیادی است که این وضعیت ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/690479" target="_blank">📅 22:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkz7wpQ-Ltd19HpDRPrVSN1WivisIhw4gp9bzc6Jj0ClwsK0XjgP2jx8xkwoDZdmCMYa6Ge0TEdGPBWUFXuuMVNOJSOitEHZTNhZJnsMf0HQ8f_U4jgZMnILlB5YvKCwDbYj8Ltcq4zfYgG-yhPdU0OUMXKFB4gsRNkJitPp2ad8xYE4ZNAQYg_xPXIQQWfm3zqqYij6YLplWiXWRdJo39AZWmTGSFoV50Ec037ZqTpZ4KOjRbsj0zUko4cZX7Fac8Qo__vrC3nbPhMbFZKbDtQAaN_NWQYRxXUzAv2fV6ZVopxTK9IZ_cseLQ5m1A1DKqusKYQT5v0VG2FbmoJicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/690477" target="_blank">📅 22:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بانک‌های مرکزی عربستان، قطر، عمان، بحرین و امارات متحده عربی، نرخ بهره را به میزان ۲۵ واحد درصد افزایش دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/690476" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش ۷.۹ درصدی حیوان‌گزیدگی در کشور
قباد مرادی، رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
در پنج‌ماهه نخست سال ۱۴۰۵، تعداد موارد حیوان‌گزیدگی در کشور ۱۸۰ هزار و ۹۲۲ مورد بوده که نسبت به مدت مشابه در سال گذشته ۷.۹ درصد کاهش داشته است.
🔹
در این مدت استان‌های تهران با ۲۷ هزار و ۲۳۰ مورد، فارس با ۱۴ هزار و ۸۷۱ مورد و اصفهان با ۱۳ هزار و ۷۷۸ مورد، بیشترین موارد حیوان‌گزیدگی را به خود اختصاص داده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/690474" target="_blank">📅 22:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
واشنگتن پست: آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔹
این اقدام بزرگ‌ترین فروش از  این نوع مهمات در سال‌های اخیر خواهد بود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/690473" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فعالیت تجاری در مرز چذابه روز پنجشنبه از سر گرفته می‌شود/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/690472" target="_blank">📅 22:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای مضحک ونس: تا زمانی که ایران به هدف قرار دادن کشتی‌ها ادامه می‌دهد، خروج آمریکا از منطقه ناگزیر به معنای بحران انرژی جهانی خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/690471" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUs8N_CtCXKEOm1t56bkZ9qxIAbJ1_6Yj__tM_8kqF1gFgIh86UlOaBftnlDeVS0Bi-HxptMxF3WCuk8ihAY48UiJ7mtAAaucRjjP3JZ0ztR70JbQN5cnhn_pr2Nf6lGSA861ZGLWWNxr1Lqpy0m2FRgPgQyElixJ03OIwiAMRkX_kbDTdN4Rg7zGAZf5_g0OSrlKLSDF6zJV3omjdX5ktmH6i5Tx9lGUwnv5fvwX_-NTqW6YTrUZdDv8KnfP8vHdISA1lbnEY9msnAWZHg8PYdOPf5Sgqw1GhdcF-jyLDJf0K5Z48jWHqrnsQ2zrrPoJobhbHcuMy2g9czPzPoEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرس چطور در بدن ما ظاهر میشه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/690470" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» آغاز به کار کرد
یکی از چالش‌های اقتصاد ایران، نبود ابزارهای شفاف برای سرمایه‌گذاری و به‌کارگیری منابع ارزی است.
در همین راستا، آیین آغاز پذیره‌نویسی نخستین صندوق سرمایه‌گذاری ارزی کشور با نام «مانا ملت» در ساختمان مرکزی سازمان بورس برگزار شد. صندوقی با ضمانت نقدشوندگی بانک ملت که تحت نظارت بانک مرکزی و سازمان بورس فعالیت می‌کند.
در این مراسم، وزیر اقتصاد، رئیس سازمان بورس، مدیرعامل بانک ملت و جمعی از مدیران و مسئولان اقتصادی حضور داشتند و درباره اهداف و سازوکار این صندوق توضیح دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/690469" target="_blank">📅 22:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA8LqHUHgcXSipCmxs798Y21hQ0xvuMPbMVVPXCJUFD0G6fCBcponCPz43wHu6SOqJHTjfIMfhjW-hE-KvraWDoEJCfYT6rxcYKjba96vEtOSjHyzFeGEUKwzV4GdXgwJ94lsBw4Dr0NjGatQybAld1SlDmZV3Mc9bfATWFgByPDwm5AS21kFfAZcnQgGg5IbzP0jsEBdvyFvyzoxDEUIQ0ZQKpNhP-Qv-D8JTf-W5nYvA5xarA86qB_cjCf_OCsVObJWjWUp73W2CU_9uE-YoAHdJB-DxiLDo0-l7gS4Hp9YEgJlKzMYgjj9NbMd4B2w6QOYyvMWQVroFJE5zH8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧥
کاپشن مردانه مدل Ferrari
🏎
🔥
مشکی طوسی | مشکی زرد
✔️
رویه سه‌لایه مموری
✔️
داخل پشم‌شیشه
✔️
فری‌سایز، مناسب
L و XL
✔️
قد کاپشن ۷۸ سانتی‌متر
✔️
ضمانت تعویض و بازگشت تا ۷۲ ساعت
🔴
قیمت: 2,380,000 تومان
رنگ مشکی زرد
https://memarket24.ir/product/brief/63704/180124/
رنگ مشکی طوسی
https://memarket24.ir/product/brief/63705/180124/</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/690468" target="_blank">📅 22:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA5RJU96dHIZK6GduFfLmFB17yzR2hIBrZ1NTwdfcbm7oV_6t3yUX12REn1c3wSP5zl1T8AfsZiQO0ULQu_Crws6vlA5O6u72qlFqGtvQDa3G_Z5wQ393TA633K-p6Ffl5lDz255wIbqKpv0GTcV0MCi-0TLkNKTV1x9UL-qiqUJkleO3BkLvXy38SmNcEgumWEhSSfNuNIrl8WcYBPrILj_rU09y0xJ7vuG96cC1uwOjBjyoMHaySnADRwxdcZHoWeTbot2D1lAy-uxt8QsQIgzTMtFXACi_xRLdN43LAl2z0bcjN_ZpyqKCVyZWJRtIw8tk_WlQ0cxF3KvWon8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: دفاع مقدّس، ملّت ایران را عزیز کرد، روح معنوی را در کشور ترویج کرد. ۱۴۰۳/۰۷/۰۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/690467" target="_blank">📅 21:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای سخنگوی‌سنتکام: ما بیش از ۱۰۰ کشتی را که سعی در شکستن محاصره تنگه هرمز داشتند، تغییر مسیر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/690466" target="_blank">📅 21:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انجمن صنایع آرایشی و بهداشتی: میزان تقاضای محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است
علیرضا کیانی، رئیس انجمن صنایع شوینده، بهداشتی و آرایشی در
#گفتگو
با خبرفوری:
🔹
امسال صادرات محصولات شوینده با محدودیت‌های زیادی مواجه شده و سیاست‌های تصفیه ارزی، رفع تعهد ارزی و سایر قوانین صادراتی کشور از جمله موانع موجود در این مسیر هستند.
🔹
با وجود این محدودیت‌ها، احتمال جبران کاهش صادرات محصولات شوینده تا پایان سال وجود دارد.
🔹
تقاضا نسبت به سال گذشته تغییر چندانی نداشته، اما میزان تقاضا در محصولات آرایشی و بهداشتی، نسبت به سال‌های گذشته اندکی کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/690465" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b0e77466.mp4?token=upFyIVbKIKVBris5R4C1ylEF5A7IWT23wHIVM_8wzuTJHWpL9jM3Fwk8DUKidr6gozbeFgCEcuItSl3APVbzLvri8A5oawtzfamDEX67f2knKdKaysrYFI-KQmRHeqZcr0KlKS7ncwSPDL2bcH3jXCx7aBZ7BbEyh21oWLW1v3BJb103cYLCJ1Y9dZhxFoN6zGwVr9nlJmnXoS6uz7tn1fCmTSTp8xVZKoWvJ-XTHnPqdCuH0esB0UYuaW1g2qhrClcbJKnfBp69rIDiyXLnKZ2V9V2c0Li8Yd-ym9zuEvcyRPMte9Rg0ZYMUnBidERzZe7vUQsFLtO_1jhTZo3H2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع، سخنگوی ستاد مردمی «جان‌فدای ایران»: ورود جان‌فداها به پرونده ناترازی انرژی؛ عملیات ملی در راه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/690464" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNVG2BCagJdEb7A6gZKKKwrMAn00J7qgkEttj2CHDwG6EY-0mKwuns5oZKsOTaNbqYxalNb_byi7uv7KcQ5uuJa0y4BauQjcZqL9qTYsNntFw7hHIs7h69ij7PTkjk13YCxtP_beBTnrG2syaZWY5Z1Fj5glCx8s97RHY1HWmW7QwDk61MEIat_XGAubcU2x-cvmRKuUj75_UzdQcTbuOKIdBKqylk2jVi_s3Q2ZONJkJiw43Ksaq6auvRLP0s7oAmAAKuv3DVkT2TKi3vdqoHlHdIhQOsVBm8sy_qtKj5YnByE9WSW25QTEQPaTcAGDF6NLhoD-iJZvLNAJo_MF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت کاربر یمنی: جنیفر لوپز در حال رقص در استان مکه در ۱۹ آوریل ۲۰۲۵. ظاهراً تقدس مکه در آن زمان نقض نشده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/690463" target="_blank">📅 21:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qm57s9pIRHicC5_-nyb4rqwEDAklOqC6QVJQjnw8Lariu6GtsIGURzfYDTSDCPzU-8_us0PW-zz64z79TucHszEjmyEIUeLecI1MKE2lp5DeTJgFVwjjJYWQjp1PK77W9I_Kh65GdeHK5SKAa2eB0nURXlHPvwcsTxFn-_0QP1dBTRd-pvbobUQqcX8GV8OpE1jQsThZenHNY2ehVHTyqMsYYon0_GIKd9gJXQ4iu4fr57K4cPJWJPC6T26FqSQjNcYzZIfvzJyQWU_aB8d9QUtyHUsA4JnnHXZDK6yiS7TgvBJRmXwe5tj78E5GlndZen3Qeud9GzmBbBbclunwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQRN1lWFH7wrOLMVopWpHSEDv90Ksm2QuuHUHBBPV5Tm9pyJGpfgXMqaeOUeoz6TBPPT7akOrbbr8TZeziYlo1kJIAV25yG2DbcG6dV9cf5B8uEXmwTo0xczfx_lK-aJFlR_vq6F6MLF0TWz7-UXydy8y3xk5277cX-g1ukfkDBNQKQJQ9MUMrQyd10SfFl7k4Ue6q2Cpv9zGTfMFHDfanmgL1KDNnStz0lwBsfg5xVJwbuZwiT7Sn8uJGJJXB0rfVDt_GFfnHCXEH9XWiBsEeBExBcGmP8j_p_Hi-Ck-UxOoaWA5gUiq2e9CmyPTAiUQkkfrE0HF-BIV6F3vgo3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXhYWPXGMZzy7f6xuJqQSI87R73Ikg5wf6eWm4HWe_UPfnNpIQOPbaoIOPvIg-VBHS3nBNJvkfW5ld54vzeCopJyclSY13imAND5hRwZ2rDlbXSF9R1eFkb0GvncYDlLxa8p6GH5-QCAw1XacJD2p_3K-zS91ROCsALODysBy1zTTgZm-XB-trt7sCEL2v7_duhK_dSGQmigMUGWphAcDsnvQKzWBCG-gAzAvQ1MUykMyIxgIYCjti_aXdJ5Fn0pd2EVW3tofDkiobb2h8gIObYUWyUJ052WDoaJStVP4zaNIns9T4FJO8waeFJEk1jqL3kG1NMzI1QxKUuiNcLi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOHfF9r4clL4HvVG8P718vte4TC7rGWlZ4l0cYkJ2xcilKW6Dn1EPTHeZxly0AX5rshmV06VDIVBDkbrTywtk9NvvCgMCdpNJDpGAu5Ok0fNkmUHG5G0fasIufR1fFEIOBzoqT9fpZNAwxD7O1lCDEPVcncD7qM5oansq-bXp87sWgkNFBFn6a9zay7EIh0Rqrr6X3Shnlj5pyeM7Xrz9aPYIW-p4MwJUe-OV40dP-6iZKiaSZpeTD42r7EMPu7c1baDKng5BnSJXB-gPNy-A8M7uGXJm_Clg66jlR6m5qw76lA34dG8YKvknHZNsQpw8j2z2hPZ1fzhgKA5TjChng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRmwwe38auteoLHyN370qzvBhRMp24d46ySYJZBsHsxcydgEvc_PNvVN--YodM3woP2PNn-qPl5cyhNaPBg1Dll1JAoaHxmDWVab0h8wyyfSZ1uAO3aet7nTS1ZwbgFHVtIFuEo_TxcOS89SmkHP7eEaPsG_R55zOYsWtVLNbMWXHNmss6GCEzKmlFVwKvpz-fjoDTpAW2DwUyKDjwffn6lWK55nr_yrMoIP0GydKVAmXgOJHS9K962UB6L8s8eV9IDJf-vF0JdiLlUA9NSNsJsqQpmE7AjsCBa3V_yNBX3QE7iCpZ2DLJKvTmnYYHx2VyTUa4XE7t-PRXx9S90pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ijy7VNwgVnBZk3O4sE4zU2zg84WVYHQk0-JARtUSsHph0azRjHhP_d4E78HEpuBI9m-9U2xMyWF_xqwEAFF9oT3MW4zpwRitXqhbHewdemu6yePrjIh3qIqNmvK7f816wjmibAhQLUdqh1FAJKL6Ir37w0R5TSVTTrwp8s9QBnILpLB-32FF1ISqS0n3LVN_qPpa3IuO_srMo-CUQIFHk19SvD2WFDf570B55EK3gcm-V1ly4F8kmpJ0KzoViOdSdIPVF3pZNFevMP6u0a-W1frnhHzV__9x97iOF1V2wfARqkrMWeKILo1DIiTraKPY83YyaGTCF4V-DxmpHqtjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrxyDjGUlZZtNjJw2Qkz3wE-H2lKP_ziFGtFCS64Dr67Q9S-3W3GnC8QKZK7isRJWt4kX1TdvYLLpJPqO-kbeAzIVZXTZVw7EW5f0MEXMurLvmLLq0KMpc6e-eOQ1FOkm85UEiRMQnkajcvVr8waGNC2uBweXsjHbYMFigo7wtiVCBFCtSwvIRSjCpHAGUhROe_TD1u8QXqpad4USqHe9I1APymnEqD82hKzfblbLGPxuZRHg_qvffYZ5mOBeb_YKvX_deYUhDxWy-v1CQZJ436IWcyMRhN5aFZZGSvkV0XtE35VWoNMwT4BhfU8_GfGMeLeHuLuZs4fxCOrctla2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REn7AKq3BM0W1XBvJBtxdLbUlDE3QYTDlhPLxPY632hPnDI8slNppSHIVpT6qyTQDIdOhH6bDAJg6NbcM6bdlHhDYoHPLjSZtfBiOyoacDvx6_kVGAPSKEErgqmxQWhApjA7wgcIy7yX5ub4lcdA5p6QImk54P-L0peGuzBiWCM_-Tj1w3Jsowd1tuHnqygrRDixuFQxdukpSERuw4nwmGV1hRDuzDJfwwL9qx4MeSSv9kE-Xi5UrKCdghAOH-Nm9Dgsg0x-pLc0zwBHBM5BHt64z4dILfn15WQhO8KOad7ma1Vgzwi1-N8HmG7vTPS6rfHtjIbvjanDD99QabMkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzOGZ6Tt0QNeP8OLIsgfs3Fp5zn7hfH_W5q19WZr79I8Qi3RRl4aQiFMeqyDZyWwLgqQrTW-ce6S7CXHxn5163ZM1ypl9Y0NSHTgN8-x-2MnDRvnGBMe0jngq3EUcvGjTeNuKMWSYYMgDKeFURiqsrWAMQWkrsigumVAvshM8djG0JgDgEajnXgCSXa45uGJ0cI16oEE9fIKYEfDEM4ejEQML4248e5WPIv4oujQokkVTHzic4u-NF1K3_Pf_G4qmG8K9CgAd-FP-gNsilP5iwgkiTmqGj0XWW9fY0dra0PV5ubCVUC50IX7Zv00K09vDquIdU5ZUSZ-FHhwptO8bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
سال‌ها همراهی، سال‌ها صبر، و سرانجام شهادت
💫
⚡️
در پنجاهمین  قرار با خانواده‌های آسمانی، میهمان جانباز شهید مهدی سورچی بودیم.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/690453" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
هیئت اعزامی دفتر حضرت آیت‌الله سیستانی در سفر به ایران، از اختصاص و توزیع ۱۱ میلیون دلار کمک مالی میان ۳۶۰۰ خانواده آسیب‌دیده از «جنگ رمضان» خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/690452" target="_blank">📅 21:25 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
