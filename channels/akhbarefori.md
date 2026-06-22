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
<img src="https://cdn4.telesco.pe/file/jEVfE9TVkbI1P9uPkkDDb1LS0R0JVmcuABZnqPSmMbGaGrPZDYWye6DlkKmSAvTTonTPUTiHyjd2QnyR6y7ilTC_OZt8TFRPTKzOk6f0a3Kpk6hn4R5YYkaLA2z10YUq34Fdht9M01ByMduqwVtWacInfYt0h3OK7oCCZ24yc3X8Iaaik1K5oho41tN9Mxaoe32JAP6jjsiVYbVFmt-pZfHdpEwQ5eXbgJRmUYuP8j7pV899kHn4QBDvj1o7qqeOYvk_QuZxQAZ9opAvCfcclKoW5Yq5U9mrbmsKmrMeAfCzo6T7nyvLCpvdjYd0-K8Lp5hiZR0ED1RTUrgL7gEwxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-662380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
عارف: هیچ اعتمادی به دشمن نداریم
معاون اول رئیس‌جمهور:
🔹
هیچ اعتمادی به دشمن نداریم.
🔹
حتی در صورت توافق با آمریکا نیز حفظ آمادگی کشور و افزایش قدرت بازدارندگی از مسیر توسعه علم و فناوری، یک ضرورت دائمی برای جمهوری اسلامی ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/662380" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjj7rFj6lUKjksxEIzkBLiBH1bqJNO4D-l3VmMMFItGXTvcbj_mWwwM_A3MvCUpS5f4X63lFyR0Ag-kc4tEiRZKX4sxDWsAm9z1OMbpSEABAdmWL_LK7XJcHGOtqmGWlOh1VC2b7z8QMQ8G31SFae1zf-J5WZFTUr4LmfYScW8m44jRcocJUAcE9v1QRRWnng1I31tnVTJanwNRVmKvMdqAR4xIQTq_KWkV4I6oJf33VeB96oU3MMKhVmMON8bb4BryoMSTJQ71S-ETEs0iuzz8yAtMxfg5V3srLmmZzEbzLA_rpxlMXLPxmn6SIbEkweRVbljMfLefa3Lu_shEBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معنی بعضی از نمادها در زیورآلات که دانستنش جالبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/akhbarefori/662379" target="_blank">📅 21:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تحریم‌های نفتی ایران به‌طور موقت لغو شد  وزارت خزانه‌داری آمریکا:
🔹
مجوزی صادر کرده که بر اساس آن ایران می‌تواند تا ۲۱ اوت ۲۰۲۶ نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی خود را به فروش برساند.
🔹
طبق این بیانیه، واردات این اقلام از ایران به آمریکا نیز در…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/662378" target="_blank">📅 21:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
محدودیت‌های پروازی تهران، قم و مشهد در زمان تشییع پیکر رهبر شهید
🔹
سازمان هواپیمایی کشوری از اعمال محدودیت‌های پروازی در برخی فرودگاه‌های کشور طی روزهای ۱۳ تا ۱۸ تیرماه ۱۴۰۵ خبر داد.
🔹
فرودگاه‌های مهرآباد و امام خمینی(ره) در روزهای ۱۳ و ۱۴ تیر با ظرفیت و پذیرش محدود مسافر فعالیت می‌کنند.
🔹
۱۵ تیر محدودیت‌های پروازی در پایانه هوایی تهران تشدید شده و هیچ جابه‌جایی مسافری انجام نخواهد شد.
🔹
طی روزهای ۱۶ و ۱۷ تیر نیز پذیرش و جابه‌جایی مسافران در فرودگاه‌های تهران با محدودیت همراه خواهد بود.
🔹
محدودیت پروازهای هوانوردی عمومی در استان قم در روزهای ۱۶ و ۱۷ تیر اعمال می‌شود.
🔹
فرودگاه مشهد نیز در روزهای ۱۷ و ۱۸ تیر با محدودیت عملیاتی مواجه خواهد بود و در روز ۱۸ تیر هیچ جابه‌جایی مسافری در این فرودگاه انجام نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/662377" target="_blank">📅 21:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آغاز ثبت‌نام ایجاد و ترمیم معدل برای کنکور از دوم تیرماه
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش:
🔹
ثبت‌نام متقاضیان شرکت در آزمون‌های نهایی برای ایجاد یا ترمیم سابقه تحصیلی از روز دوم تیرماه ۱۴۰۵ آغاز می‌شود و به مدت ۶ روز ادامه خواهد داشت. متقاضیان باید در بازه زمانی اعلام‌شده نسبت به ثبت‌نام و انتخاب دروس مورد نظر اقدام کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/662376" target="_blank">📅 21:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782bf9bb54.mp4?token=ifXVIotpP_UsbiL0lKkE1t-mzL7GX3d-SrR9xl1mz-3fWlhGFdMpK9LaVX5YYoVvUtSVZIJYR_KoOvjUw2JxsS7R7vipE9GIDPjJ1XJ4tfCbn2y8ONCPpaCmMndQ4BU4yFlR5GexzKBgsqP7nKikekiggAahgN6AZE8enWlck10OKNrT9PlOFoirfLwbtz7vJQ6bE3r2GD-uay3xSbWKByRbwP9LpZfafuknfi8wQffVZMebQWtskO1-IvY6HcsbFyzHpw-Jthpoq9myhR1se5Ky4wt0INa2jnWUG69PUeqx1ORnNrrpzKQMsmKBXK_kYSNHg1ygdvY9gIuLcixlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782bf9bb54.mp4?token=ifXVIotpP_UsbiL0lKkE1t-mzL7GX3d-SrR9xl1mz-3fWlhGFdMpK9LaVX5YYoVvUtSVZIJYR_KoOvjUw2JxsS7R7vipE9GIDPjJ1XJ4tfCbn2y8ONCPpaCmMndQ4BU4yFlR5GexzKBgsqP7nKikekiggAahgN6AZE8enWlck10OKNrT9PlOFoirfLwbtz7vJQ6bE3r2GD-uay3xSbWKByRbwP9LpZfafuknfi8wQffVZMebQWtskO1-IvY6HcsbFyzHpw-Jthpoq9myhR1se5Ky4wt0INa2jnWUG69PUeqx1ORnNrrpzKQMsmKBXK_kYSNHg1ygdvY9gIuLcixlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: مذاکره، یک روش مبارزه است و ادامه آن است و آن‌هایی که می‌خواهند دوگانه درست کنند، که تو طرفدار این میدانی یا آن میدان، این موضوع در جاده خاکی صحبت کردن است و یک بحث انحرافی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/662375" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b9cf5d2.mp4?token=DpfV7JM3FJfMJq1BCTLraoetpslmI3na1rkN87LlUAJDg8VrGYJk2oGPmHp1WNhmautHCCY0LSKXre4pmZxEssvCvjXd1urBEonVxath35gusk7b6SlLopSBEQnVeyGUcdzPF3X_e70ZYpdoi1G3PnPt0kdT7Q87H3dJHW5PUpQ9JSeYTKfQTr9jbpujgccQ888vdHPkuaIynFBheMQ0RfNgx9ra03sXY0W_mqwgWHdxc1T09xdgL6vPW0aDX8iHUPfWTkoaURRmYBN39PY8E22KjxIaubqaUTtfxXTaO7CYXOlxUeOwXn8EnGnHlmnaQUvuFTUL2Jrn9GbItRwqR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b9cf5d2.mp4?token=DpfV7JM3FJfMJq1BCTLraoetpslmI3na1rkN87LlUAJDg8VrGYJk2oGPmHp1WNhmautHCCY0LSKXre4pmZxEssvCvjXd1urBEonVxath35gusk7b6SlLopSBEQnVeyGUcdzPF3X_e70ZYpdoi1G3PnPt0kdT7Q87H3dJHW5PUpQ9JSeYTKfQTr9jbpujgccQ888vdHPkuaIynFBheMQ0RfNgx9ra03sXY0W_mqwgWHdxc1T09xdgL6vPW0aDX8iHUPfWTkoaURRmYBN39PY8E22KjxIaubqaUTtfxXTaO7CYXOlxUeOwXn8EnGnHlmnaQUvuFTUL2Jrn9GbItRwqR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به اتریش توسط لیونل مسی ۳۸
⬛️
🇦🇹
0️⃣
🏆
1️⃣
🇦🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/662374" target="_blank">📅 21:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رئیس‌جمهور: آمادگی داریم دیپلماسی را در راستای حقوق بین‌المللی ادامه دهیم
پزشکیان در گفت‌وگوی تلفنی با رئیس‌جمهور ترکیه، ضمن تاکید بر تداوم ادامه روند دیپلماتیک برای استقرار صلح در منطقه:
🔹
ما کاملا آمادگی داریم دیپلماسی را در راستای حقوق بین المللی ادامه دهیم، ایران به دنبال جنگ نبوده و نیست و این آمریکا و اسراییل بودند که تجاوز غیر قانونی را رقم زدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/662373" target="_blank">📅 21:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: همه به خوبی آگاهند که ایران موافقت خواهد کرد که بازرسی‌های تسلیحاتی گسترده‌ای را بپذیرد تا «صداقت هسته‌ای» را برای مدتی طولانی در آینده تضمین کن
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/662372" target="_blank">📅 21:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: توافق ایران و آمریکا، به معنای پایان سیاسی نتانیاهو است
خواجه محمد آصف:
🔹
رژیم صهیونیستی در پی شکست توافق صلح میان ایالات متحده و ایران است.
🔹
دستیابی به این توافق می‌تواند به پایان سیاسی نتانیاهو و حتی بازداشت او منجر شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662370" target="_blank">📅 20:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662369">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeMzbBG_j4bZFlffLLgbnZH0iIP67W99FWBiUdga9k0-aHUMq0PHjKIvHB19r58JELtsg7TezOEdUBwGkZfZwDzc0yYu5oquh8iRXQKSF-90g8K0rnS5RpMdTwEK7XCTTwj7VV0FCPi4A9EAbUf2xh9_Jlxk_tIPtlvm0OLdhalhj8gGsjkc0O4KvbUaSClRabNC09QMebCr-6vsiwLCfmGB4n7gVbWFi73lVXv_uOpRJUfJtAvy9TxVhpAOb8zXTcs6AdDgm0rK3MlPLXIb5jzNjR4Pi7jk-9RHtHoJYuAFyjme7iCVqpaIjvSdp1pkWZJ0x6A6NNYxK9LpSYqLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد  یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662369" target="_blank">📅 20:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662368">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاالله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/662368" target="_blank">📅 20:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820e1e95a2.mp4?token=bsliiWf-mWfxY6-P45BWxCDo2vn9D_JvUfUsZsZ4i94xxB0yzuDTb57582mFw35Fe8QQChBY07bWm43nDlXpJjOSTMUVkZAwwOHIOn1JnZVm4uPa5XRFxqzbRmbSs7kAzWfbxYTQM0zhbcn080LzceEG299C_1vRdR6WFc17r9OZywFQ1GsSrvCdxed2-_ymjcpIqTS5BtdVM6iHTE7y4euAVeq7jHZiE8pio9AGiE6-h0SQF33qPkFu6r28KydVArru-D6bAW5WWULryzbspFlN13IOWSgjyvmp9vO2pI8Z9H52XlNyraPdGJpSX-BGkTsA1W9htUTTBtBvsDIWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820e1e95a2.mp4?token=bsliiWf-mWfxY6-P45BWxCDo2vn9D_JvUfUsZsZ4i94xxB0yzuDTb57582mFw35Fe8QQChBY07bWm43nDlXpJjOSTMUVkZAwwOHIOn1JnZVm4uPa5XRFxqzbRmbSs7kAzWfbxYTQM0zhbcn080LzceEG299C_1vRdR6WFc17r9OZywFQ1GsSrvCdxed2-_ymjcpIqTS5BtdVM6iHTE7y4euAVeq7jHZiE8pio9AGiE6-h0SQF33qPkFu6r28KydVArru-D6bAW5WWULryzbspFlN13IOWSgjyvmp9vO2pI8Z9H52XlNyraPdGJpSX-BGkTsA1W9htUTTBtBvsDIWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاالله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/662367" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSVIB7v6DIrunud08IJIP6pD5usFr5-LcGbZeCyDxj1q7_NoJyFcyalvPLjiswDIWtO2Hu0yf59th3Z9Pr86Rl-OjqPObSME513uOKdcTAz3uWkaMqVe7wWlEX0h2kW58d4ewEQ_uKV-i_GCodqj_cbDpMd979H0F1-tIE3Ok-biwMA3Cy-532U-nu5FDTLx-4QPOOBeFz2lipCqySW7EjSvc36xsbu8st0gEtFLP2dXxyAMZVeEeZ1bu5_tolyh6hrMW_iStJMWbN19XmO4jUFtJJm0OlhrzzeYAFnzcRNOWgz1FuMhwyQvb6k9BFkwNvF1NRbC9G5Wskj4nFDcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: ایران با بازرسی‌های عمده موافقت خواهد کرد
ترامپ در تروث‌سوشال:
🔹
همه کاملاً مطلع هستند که ایران با «بازرسی‌های عمده تسلیحاتی» جهت تضمین «صداقت هسته‌ای» در آینده‌ای طولانی موافقت خواهد کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662366" target="_blank">📅 20:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662359">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac354b107.mp4?token=lgT90WG8r6Ki5rz0UN8tAA4Gwshg4EP_kHqf0kfvUMV6tGH3lBwcQufTGyG9Ne_y5sNs_Xj74u8OSdjc-iWl8_XkcxkvmrG02uB2y0_hPcnCR-Jc9xz2lKeCP6EzvBVUsM8yet1jRc9aprUTiCAiOOcdpUIyXcVn7jaIVOMLEc7ZqXl3A7milIc3IAbxJW--LBtMHTH8YqONHStou1IEIK5XOVcbupBNS5g31BpzRc-OMN4-zjS_e9IwD98-Z9-9Fd-E8VRxTIJTX6NsgcDA4Bd8i_YtMo0w9rfCnhtftRoDunzP62IhCZvqlBkv7SBgVS23e7gt2QrodUfH_Z-8XE3HPlokb5K9gMgeWGv03DD-nhcEmbonaVXxcWk5-j5-YKYe9a2b9t89pSHcjnOXeB_BUSYJVw4t3XFiHQVy3pPOEcbq1yat-tJGtuMZ_Htk7QELZ5NWEirJoHOQHpv7FtDommLErCJNsjGPUFEvHaMe1comcTLKl735l4mp6VuATLK-6Ltv11xzQLPN2ZE9UtzlCxWPoCYJvTa3ApevQeDsddbInxuuYV69BavYbIK2eRKO7MVkW68UO_3FCcikpqxNKqF3ISlhTgPXMacbO5rQaYYgcnQLkxbzA3N1X_7ziwbvNueC3c5k8_0Br0XDCNYw6FVJvDtRYFwtaONw1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac354b107.mp4?token=lgT90WG8r6Ki5rz0UN8tAA4Gwshg4EP_kHqf0kfvUMV6tGH3lBwcQufTGyG9Ne_y5sNs_Xj74u8OSdjc-iWl8_XkcxkvmrG02uB2y0_hPcnCR-Jc9xz2lKeCP6EzvBVUsM8yet1jRc9aprUTiCAiOOcdpUIyXcVn7jaIVOMLEc7ZqXl3A7milIc3IAbxJW--LBtMHTH8YqONHStou1IEIK5XOVcbupBNS5g31BpzRc-OMN4-zjS_e9IwD98-Z9-9Fd-E8VRxTIJTX6NsgcDA4Bd8i_YtMo0w9rfCnhtftRoDunzP62IhCZvqlBkv7SBgVS23e7gt2QrodUfH_Z-8XE3HPlokb5K9gMgeWGv03DD-nhcEmbonaVXxcWk5-j5-YKYe9a2b9t89pSHcjnOXeB_BUSYJVw4t3XFiHQVy3pPOEcbq1yat-tJGtuMZ_Htk7QELZ5NWEirJoHOQHpv7FtDommLErCJNsjGPUFEvHaMe1comcTLKl735l4mp6VuATLK-6Ltv11xzQLPN2ZE9UtzlCxWPoCYJvTa3ApevQeDsddbInxuuYV69BavYbIK2eRKO7MVkW68UO_3FCcikpqxNKqF3ISlhTgPXMacbO5rQaYYgcnQLkxbzA3N1X_7ziwbvNueC3c5k8_0Br0XDCNYw6FVJvDtRYFwtaONw1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ شب هشتم محرم حضرت علی اکبر (ع)
🥀
کار تشییع تنت دست عبا افتاده
تار و پود تو ز هم سخت جدا افتاده
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662359" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662358">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14951272bd.mp4?token=VoZJoWxKXP0EM9rKrAkchthKw8_r2PTGoQnvoH45TaFz78PiIyxknd_PKFfLhivfidcpih8SAcg5r08M5WjxBZ8swAZFaA5tH2-Ch4JZXlu25UmOwjO42R2kwi8OBG4hWnfXJW0lvVtRsI_1uYW9iir3lhzAnKKa27Tfh0MkWqho52IIxy6Uzge5upIMr2Jqfu2DczQgZlbPp5vKX1dxixt82TcuvEI2DZYK3QJgVQhutmp3LnfQwWlOqyYlbtyx5HzisAkYWTTVMjDoIJW1HXRB47ffEnJLcxyTHJnW0A4Q4XjCxq8Kbgo9_TpL5XTNBMCxIxbddHfSgraJWI6Edw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14951272bd.mp4?token=VoZJoWxKXP0EM9rKrAkchthKw8_r2PTGoQnvoH45TaFz78PiIyxknd_PKFfLhivfidcpih8SAcg5r08M5WjxBZ8swAZFaA5tH2-Ch4JZXlu25UmOwjO42R2kwi8OBG4hWnfXJW0lvVtRsI_1uYW9iir3lhzAnKKa27Tfh0MkWqho52IIxy6Uzge5upIMr2Jqfu2DczQgZlbPp5vKX1dxixt82TcuvEI2DZYK3QJgVQhutmp3LnfQwWlOqyYlbtyx5HzisAkYWTTVMjDoIJW1HXRB47ffEnJLcxyTHJnW0A4Q4XjCxq8Kbgo9_TpL5XTNBMCxIxbddHfSgraJWI6Edw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنالتی که مسی به این شکل مقابل اتریش از دست داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/662358" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLQAiPL78LEGdg4wZGtBVJ8O9u1sAFGegt5aYNBgJm8WV1QVutCRMDRrc09TtwoFdzvt2w6VOBGSu-2hVWAJCm8L_Er1r85JVTX2PZ-08yO5HPvD0ieY7zjCSuPs5HOQy-kEmx5_-kek1WSWK7ewquKnswziQpVKI0QWYHdziAPPNhTwVC2uMIkbKJO0kWpDNI2lQdKRljPIEwrvluUEGaTMBBS1am6_AL5CXDOGoAFqQ9ptaLvdn4_83DguXBcncdUHBSpznN6Sp8RIfNgb7qNAmiLPmZ-icSsTAGxnLRXnrPBHCYF1HE3JO4JlyOwQvVmf8PGkfLQIXFzsO8kBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sb5wflrvoH7u0kyhuT3nIwXpHVFBPv2YlU4cBsRb2yW-MurgDWRTUJXcmErmJ0AE8sFqmOjs1nSP5FfiM21TB1i6nE5PgSEWMy72Rhg58xQ7RS53m2qp150Ol98SAzpaQ9MU2Hfg08DGSnXSrUeX3N6Xak9flxB8PyEXnvHAAvEjtI46DK5lgorqRuhmHSe4pC_GIYH4A_IMRiqUZ89MqA7_DU9GhjN9Zq12oSTSG_wvAeo_r2O8d_AThgn5PMf-V-PKBZohi5oesXdtC46r1EoBoTpT5SWlip7PYGR9V38LTlj1H-oOHQQl5SXhmwLrz3iqRgGPDAcvCSVimLPJ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر دختر نوجوانتان می‌گوید «هیچ‌کس من را نمی‌فهمد» این کتاب را به او هدیه دهید
🔹
احساسات دخترانه فقط یک کتاب نیست؛ دوست صمیمی برای روزهایی است که نمی‌دانی دقیقا چه احساسی داری. با تمرین‌ها و پرسش‌های جذاب به دختران کمک می‌کند احساساتشان را بهتر بشناسند،…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662356" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c5d75e64.mp4?token=u3ijYDkV4IbBnNVpW2XO_cXpXCYnlYqgXgHJtfwT9iXdDKTT1DsVWb90uF-9VVB8If2jPUYUFysTD7nlEj3mbYMLEFeaoGPGX5Qxt5p9754yQaI3q8a0EiJ0QoBX3uqD_faQ7oTQSYHwnM4BP-KzABVT5jXKfdfv1BWsN6TimsoNDMKzlr0RnszkyxT9-mWbBx8HIzGAFaw-xoZVu-scdpejxpZEFuXar7LHKISi2uqVVZKCtQ2ei8YdZppGWoHSh5-t2ujJWJ7wa42NnWW8-GX-YsiFvB8vcwuHHYQPKe46nGgYJ-K9cZjN6v-4YsHwc_vbU81Oa1-PbhAEjI8gWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c5d75e64.mp4?token=u3ijYDkV4IbBnNVpW2XO_cXpXCYnlYqgXgHJtfwT9iXdDKTT1DsVWb90uF-9VVB8If2jPUYUFysTD7nlEj3mbYMLEFeaoGPGX5Qxt5p9754yQaI3q8a0EiJ0QoBX3uqD_faQ7oTQSYHwnM4BP-KzABVT5jXKfdfv1BWsN6TimsoNDMKzlr0RnszkyxT9-mWbBx8HIzGAFaw-xoZVu-scdpejxpZEFuXar7LHKISi2uqVVZKCtQ2ei8YdZppGWoHSh5-t2ujJWJ7wa42NnWW8-GX-YsiFvB8vcwuHHYQPKe46nGgYJ-K9cZjN6v-4YsHwc_vbU81Oa1-PbhAEjI8gWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه تیراندازی در مونترال کانادا
‌
🔹
رسانه‌ها از وقوع یک حادثه تیراندازی در شهر مونترال کانادا خبر دادند که بر اساس گزارش‌های اولیه چندین کشته و زخمی برجای گذاشته است.
‌
🔹
در پی حادثه تیراندازی در شهر مونترال کانادا، پلیس از ساکنان اطراف محل حادثه خواست در محل‌های امن پناه بگیرند و گزارش‌ها از زخمی شدن یک افسر پلیس خبر می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/662348" target="_blank">📅 20:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
«
مسگون
»
سه‌شنبه ۲ تیر
در تمام کارگزاری‎‌ها
«مسگون» صندوق بخشی در صنعت «فلزات اساسی» با تمرکز بر مس و نماد
#مسگون
در روز سه‌شنبه ۲ تیرماه ۱۴۰۵ پذیره‌نویسی خواهد شد.
تحولات قیمتی صنعت «فلزات اساسی»
در کنار آینده ممتاز «مس» این صندوق بخشی جدید گروه فیروزه را به یکی از گزینه‌های جذاب بازار سرمایه تبدیل کرده است.
💎
تخفیف ویژه معاملات و خدمات اعتباری اختصاصی در کارگزاری فیروزه آسیا:
https://in.firouzeh.com/kargozari
https://in.firouzeh.com/kargozari
🔙
👨‍💻
واحد پذیرش و پشتیبانی کارگزاری فیروزه آسیا: ‍
🔜
+982152461000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/662347" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تمدید خودکار قراردادهای اجاره با سقف ۲۵ درصد
وزیر راه و شهرسازی:
🔹
بر اساس مصوبه سران قوا، قراردادهای اجارهٔ مسکن که تا پایان سال ۱۴۰۵ منقضی می‌شوند، در صورت درخواست مستأجر، به مدت یک سال و با حداکثر افزایش ۲۵ درصدی اجاره‌بها و ودیعه تمدید خواهند شد.
🔹
مراجع قضایی نیز صرفاً به دلیل پایان مدت قرارداد، از صدور حکم تخلیه به درخواست موجر خودداری خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/662346" target="_blank">📅 20:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8lNaop5PP7uMGW29kq-OBxvPGR4f0f026aftoHph5ljvDaREYAxQz6Uc-rHPzOrzEwowWD4XGok9Ewd04dmz9O9vHLINHaCHoCD-pyOf50N5cJ47uvUBtMNuhxArVQ3sf5uBnGoOLqfft7GtPASUpxA0u9EMYOi5mDlefW7A7cwao7yJ5-ufqL32k1W73GWrU0NVeXqCbow_vYZ9N0kMt3C871D0g7LUk1-bTTJShINVvhaVkSFQiGJ4Ohs2-TzGuRw7exhxW9pNDzNfYyXG5Zt5G-G98KIAThgkBW4rEx7wZK39-sE-YT9-0pSCljOMwGZdN3gW4sw1xJ79sMcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIVkFiXt8vbh4VIqGazHun6lVu9G6I7WOcaFrBUihAXzxHcdkmrci-V7wR-FlJWbo1-cFN-7Mixp-LlWVo4khzU7dVBEt-efNwWBc9ySU82I5644KA1XvDFQY1Dk57K7QmkKBHICEInK5WtZZc9U6i4iTUF5PgNulNAbohfH3DFf8FNrt6b7auiNqpu0UfAneYXzTWkkyRSNbcFSGMz5OMb__Ztputyt-hocv351H4V3N4t45hXxV_9ftcv2XkemChse2ykfL5vpCEUU6_NOunAXT-lmXRqjdFLgkbGtSp7lvWVQeKJLt_vYeJ6hTP5RkhJlqYQ5_Uigd_f15s2jZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سن ازدواج در کشورهای جهان چقدر است؟
مردان و زنان نروژی با ثبت میانگین سن ۳۹.۷ و ۳۷.۱ سال در صدر جدول دیرترین زمان برای شروع زندگی مشترک در جهان قرار گرفته‌اند.
این شاخص آماری در جامعه ما برای مردان ایرانی روی عدد ۲۸.۳ سال و برای زنان روی رقم ۲۴.۱ سال ایستاده است.
کمترین میزان سن ثبت‌نشده در این بررسی‌ها متعلق به کشور اندونزی است که ارقام ۲۳.۸ سال برای مردان و ۱۹.۸ سال برای زنان را نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662344" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662343">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد  یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662343" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
یک منبع آگاه: صرف شدن پول‌های بلوکه شده برای خرید غلات واقعیت ندارد
یک منبع نزدیک به مذاکرات:
🔹
صرف شدن پول های بلوکه شده ایران برای خرید غلات واقعیت ندارد و در هیچ تفاهمی ذکر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662342" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGUGp9OKvLdcU0mRSMkAq4sKo7ZptabrYbsdgCiQ3SNFKqxQrk7-IxHf1S6TAJ3WKTodSAkRa5pWiBSmYmn0PvFyjgVvM5GpKVBO32YvTJuEsl1u9Cbe2qoi1jd1JFZLrOpr7vP5LQQkMcHFFl9ACEmGWe64plXqOuX2Dek3VnXqjJ52RITv_Kqq6VhZRvsFi2YryW94YUH-G_QUihHs6Hi0wus6V9fNULI39m6vl3xUYqwNaOxG3gIRfhgjdN46oplxa7GHf9lloCLSarb1V6EeQKOnUBDZwNbuZl_8Cw4oILC23YFbeCCsjLEGiIKEMrpaggHCh-iWt5Q0A8smzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه جنگی یمن منتشر کرد؛ آماده مقابله با هرگونه تشدید تنش یا تحولی در وضعیت جاری هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662341" target="_blank">📅 20:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
اعلام
هزینهٔ سفر اتوبوسی تهران-کربلا
رئیس اتحادیهٔ تعاونی‌های مسافری:
🔹
قیمت بلیت اتوبوس در مسیر تهران–کربلا بر اساس نرخ مصوب، ۴ میلیون و ۲۰۰ هزار تومان تعیین شده است.
🔹
همچنین نرخ بلیت اتوبوس از تهران تا مرز مهران نیز یک میلیون و ۲۷۰ هزار تومان خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662340" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نیویورک تایمز به نقل از مقامات اسرائیلی: فرماندهان میدانی روز شنبه دستوراتی دریافت کردند مبنی بر اینکه عملیات آن‌ها در لبنان تنها به دفاع محدود شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662339" target="_blank">📅 19:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ea230cc81.mp4?token=er12aeHBV0TgnMqs49YA2onnLurd9eeXxaavtFHtiIw9bNNq0HTGg2A84TdeuY-6WVP3A8z-rfHpQQKdHwyIFlppARNs0TLhpUuc_-6Xh7Nsycyr05ZkdWofd9WYeVY-d6VfkUlpwLx-aIrAstURMk3O5SBW_dD-R2u0tcGwEj2T-I_3aERuEMr08RFAhWfGVotaViEhsqQO9dAjBpCt7WZK7JaZXTRL9iA2yQ-t4qsULCYUpLO93b3Mrm7wTT0t5uDQR-7ICudHiy3WfrowUsiIvV8aKfHwSd4KYqU2vmdCZV-Pj-59s0ol7FMGpkyTpgCdLhoGadMGV7IeL2-w5p-DBsBbo6GlQg_Ma2FsLWm48428_oLo0lbvvP5ScMfehySQC9QwwH7zCVew3n3xOj3BdNrgHy8WWfxQ6Ml9kdGXqtONHebPb5UYR4S7ewDnACyIoNoPh79Z6BUR9EdmztQh99F45mSWspGxXO8zWX-TwtToimrgEDNUDSyeihkuCuNsp-7XiWh5vCPs3o2btqJwO0CvA1L8Nr8aatrsoUCeD8fTzLbuERDKqCpb5CBkQciijBcg-Qfjx0hjFBrj3aNYlGS8OuF7LozxBtzUIto3N4uKVSLRu0ABBQi6r5RR5KBmFQ-0MFwXV5Zid_do2FvYawWr2npc56KgSLQokT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ea230cc81.mp4?token=er12aeHBV0TgnMqs49YA2onnLurd9eeXxaavtFHtiIw9bNNq0HTGg2A84TdeuY-6WVP3A8z-rfHpQQKdHwyIFlppARNs0TLhpUuc_-6Xh7Nsycyr05ZkdWofd9WYeVY-d6VfkUlpwLx-aIrAstURMk3O5SBW_dD-R2u0tcGwEj2T-I_3aERuEMr08RFAhWfGVotaViEhsqQO9dAjBpCt7WZK7JaZXTRL9iA2yQ-t4qsULCYUpLO93b3Mrm7wTT0t5uDQR-7ICudHiy3WfrowUsiIvV8aKfHwSd4KYqU2vmdCZV-Pj-59s0ol7FMGpkyTpgCdLhoGadMGV7IeL2-w5p-DBsBbo6GlQg_Ma2FsLWm48428_oLo0lbvvP5ScMfehySQC9QwwH7zCVew3n3xOj3BdNrgHy8WWfxQ6Ml9kdGXqtONHebPb5UYR4S7ewDnACyIoNoPh79Z6BUR9EdmztQh99F45mSWspGxXO8zWX-TwtToimrgEDNUDSyeihkuCuNsp-7XiWh5vCPs3o2btqJwO0CvA1L8Nr8aatrsoUCeD8fTzLbuERDKqCpb5CBkQciijBcg-Qfjx0hjFBrj3aNYlGS8OuF7LozxBtzUIto3N4uKVSLRu0ABBQi6r5RR5KBmFQ-0MFwXV5Zid_do2FvYawWr2npc56KgSLQokT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662338" target="_blank">📅 19:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W23SsaIkUuSiyEkoI73mWVBvGPUNhdHK0byrOJAGysZx34KUhFhzJ1m1Vif4XXOF_jHDjGQkBshtkDwoAsZ38MruszpqfsxKEfMx8Yt3qVbVlvfywWt81CpFLYqCSc95tkOnyDIom-vsN2N7UQ1ZEDNe9PhsyADnCCyypi8xrPz4TeG7JaNNoxYcP3U_htWG0kX1sRgMKh2TO5fuZRP3fMzTdqQnxoVJGRwXNaF9QGUxZrrEpQDwrgEUE-552mv6whJiNuwRQUT146Pd0fC82wy6cgJTqEvKevb2eQQG_ytP0clOh4LOrWqBYGl5LujLpz0eaylgp94fstDWAJHusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منابع بانک صادرات ایران از مرز ۱۸۰۰ همت گذشت/ تحقق ۹۹ درصدی هدف منابع
🔹
منابع بانک صادرات ایران با حفظ شیب صعودی از مرز ۱۸۰۰ همت در سال جاری گذشت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662336" target="_blank">📅 19:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662335">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
احتمال افزایش اعتبار کالابرگ در تیرماه  وزیر اقتصاد:
🔹
جمع‌بندی وزارت اقتصاد درباره میزان افزایش اعتبار کالابرگ انجام شده و به دولت ارائه شده است، اما سازمان برنامه و بودجه هنوز تأمین منابع لازم برای اجرای آن را نهایی نکرده است.
🔹
به گفته او، پیشنهادهای مربوط…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662335" target="_blank">📅 19:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662334">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رایزنی امنیتی هند و ایران در دهلی‌نو
🔹
مشاور امنیت ملی هند در دیدار با معاون دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران در دهلی‌نو درباره تحولات خاورمیانه و روابط دوجانبه گفت‌وگو کرد.
🔹
دو طرف در این دیدار درباره تحولات خاورمیانه تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662334" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662333">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نحوۀ انتخاب نمایندۀ سوم ایران در آسیا مشخص شد
‌
🔹
دو تیم اول لیگ برتر مستقیماً راهی لیگ نخبگان آسیا شده‌اند، اما تکلیف سومین نمایندۀ ایران برای حضور در لیگ قهرمانان آسیا ۲ هنوز مشخص نیست.
‌
🔹
۵ تیر، پرسپولیس و چادرملو اردکان به مصاف هم می‌روند و برنده این دیدار ۸ تیر برای کسب سهمیۀ آسیایی مقابل گل‌گهر قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662333" target="_blank">📅 19:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662332">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c88ee546.mp4?token=cO8ekIIcUfoV6PRBPeThB7Hqo3sXKnmzQ1KdL-7cnjpsE0UlJGYtCDvk_LH0jxnLbELaOzDxrAUdJAuI5-GcLKD_NSS9ZGyT5ciIlZS9vy3OvhXcdv4KLloSdLDOJgOzKfukztkJMOPsP_ptFDo5cEXCkGCk2DVb41FGGVg-lz4DQCQl3lb2NXAYtNvf7wi-BIo9-KBXWxKsC3J0zTphYPJYwa3JX8JR81sHWwSptVhpDnABJ9pv0g5Aq-3sZ5WcObPAoGRCNwBGMOGvGj7vNqYO0op_1XF57ROv5qD8Xhd44X5w9b6xkpOBgGXhs_amsfdLsxBTFljyz1Mq-81hwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c88ee546.mp4?token=cO8ekIIcUfoV6PRBPeThB7Hqo3sXKnmzQ1KdL-7cnjpsE0UlJGYtCDvk_LH0jxnLbELaOzDxrAUdJAuI5-GcLKD_NSS9ZGyT5ciIlZS9vy3OvhXcdv4KLloSdLDOJgOzKfukztkJMOPsP_ptFDo5cEXCkGCk2DVb41FGGVg-lz4DQCQl3lb2NXAYtNvf7wi-BIo9-KBXWxKsC3J0zTphYPJYwa3JX8JR81sHWwSptVhpDnABJ9pv0g5Aq-3sZ5WcObPAoGRCNwBGMOGvGj7vNqYO0op_1XF57ROv5qD8Xhd44X5w9b6xkpOBgGXhs_amsfdLsxBTFljyz1Mq-81hwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان خطاب به بازیکنان تیم ملی فوتبال ایران: دمتان‌گرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662332" target="_blank">📅 19:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662330">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjInGmwUvN41JZ5GsFsSmWNwXHG26tdVvUBr58cT2oqrqxU7vAr7eRA1DXIo_EYUGeFcaDZGbAQie_wBRsNfHD47JuSQ8xbGSXL94GCfFqpyGFJu8D1Qb7yaHjweTJW27vBpt2USEl-edSFJExmnH0tdwltfdoRBPo6CELZyn4MF-_SwyCUq18b9FpPUFrZ3-vQqrF29a4abiTqsfTyhiSvbZAgio5rzHG_Wcy3Wcr6TbAt97p8eNWJ7T9rCiLYhJSUYS7crwKYPriyoguY2QUrevscd4D5wHELMZnpG41NJOHJfFgl_mkb9hM3lDUla3tpojwLQXGX---lK22zwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین خلق موقعیت در تاریخ جام جهانی؛ لیونل مسی در صدر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662330" target="_blank">📅 19:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662329">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8DPDwnvVWRtBdpgCK8fAIGPVIqoCY-IROOHfjpNP8GfWuixkov_dCB758UA_OpiI838qK91OLN3fLPxobKJFntTuTbvPGp4GYiTdK3UwM_5Ir4A5Tw3IA_NbAr9VoqIlq3w2RilhY87t4wPMZJ1BOa9eknnALE5hAjxH6QHJnwJ8Q-LePyhLYiPXysso2Hj7Sj91UfNXH8q4ufAaAFKz9KxmNJ-YsKR0vLWO0PWPE5Md5zh8uNhOm_Rc7tVkxz_7ybQRTCYrsmyRue-XGuI4qrmTQOptW_ROVoq6EQX-CyFbkLlWRQxWu7Aj62-rfS6M3HUuX96UWgr74JTBQzASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نام گراد در میان برگزیدگان روز ملی اصناف
🔹
در مراسم روز ملی اصناف که امروز (اول تیر) با حضور مسعود پزشکیان، رئیس‌جمهور، سید محمد اتابک، وزیر صمت و جمعی از فعالان اقتصادی در سالن اجلاس سران برگزار شد، از چهره‌های برگزیده و تأثیرگذار حوزه‌های صنفی تقدیر شد.
🔹
در این مراسم، محسن اصفهانیان، بنیان‌گذار برند پوشاک «گراد» و رئیس انجمن برندهای پوشاک ایران، به‌عنوان یکی از چهره‌های برگزیده صنعت پوشاک کشور توسط رئیس جمهور مورد تقدیر قرار گرفت.
🔹
این تقدیر به پاس نقش‌آفرینی او در توسعه برندهای ایرانی، حمایت از تولید ملی، ارتقای استانداردهای صنعت پوشاک و تلاش برای هم‌افزایی میان فعالان این حوزه صورت گرفت.
🔹
برند «گراد» نیز طی سال‌های اخیر با تمرکز بر کیفیت، برندسازی حرفه‌ای و توسعه شبکه فروش، به یکی از برندهای شناخته‌شده و اثرگذار بازار پوشاک ایران تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662329" target="_blank">📅 19:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662328">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف عازم عمان شد
🔹
رئیس مجلس برای دیدار با سلطان عمان عازم مسقط، پایتخت این کشور شد.
🔹
سیدعباس عراقچی، وزیر امور خارجه، در این سفر او را همراهی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662328" target="_blank">📅 19:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662327">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
آغاز مهلت ۶ روزه برای ایجاد یا ترمیم سوابق تحصیلی
وزارت آموزش و پرورش:
🔹
ثبت‌نام متقاضیان آزمون‌های نهایی جهت ایجاد یا ترمیم سوابق تحصیلی از ۲ تیرماه به مدت ۶ روز انجام خواهد شد.
🔹
داوطلبان می‌توانند برای انتخاب دروس به سامانه
my.sanjesh.org
مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662327" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c489455039.mp4?token=bIUQXPTVK-jaX5X5KpIupSXlFtKklUILqkRBziWqUV5t6GNN_5FvZD5tt_A8VEaEVyxpWDirVzcqw7N2ICx9qLmyBu62u_dJ9J3Yi354hJ2JJdgdm5wVbx9blr3U2Zwf4bWQKe5vYRyxi2Y9cjRU9HL91ofpIeVJUXa1uGf6rOHjlg-r8CrYCaHT0mGyEo-OT0xlpBJER6Uax2dLux5igPDX7sqbmlq8SF3d_UWeJXqDvcOBR62Jad6LQi-lawn3IUv25cdkMZJ9NslVHDYkFtbPZEYObEW3qyCr3G8oBfbE5dAn1KzcdeOUFaia4VZLkVivYqvELcy4_WDE_w5Sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c489455039.mp4?token=bIUQXPTVK-jaX5X5KpIupSXlFtKklUILqkRBziWqUV5t6GNN_5FvZD5tt_A8VEaEVyxpWDirVzcqw7N2ICx9qLmyBu62u_dJ9J3Yi354hJ2JJdgdm5wVbx9blr3U2Zwf4bWQKe5vYRyxi2Y9cjRU9HL91ofpIeVJUXa1uGf6rOHjlg-r8CrYCaHT0mGyEo-OT0xlpBJER6Uax2dLux5igPDX7sqbmlq8SF3d_UWeJXqDvcOBR62Jad6LQi-lawn3IUv25cdkMZJ9NslVHDYkFtbPZEYObEW3qyCr3G8oBfbE5dAn1KzcdeOUFaia4VZLkVivYqvELcy4_WDE_w5Sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
ایرانی باغیرت
🇮🇷
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662326" target="_blank">📅 19:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSx3Q3OgbSbEDDhU-YAekT4c5xXMMmVp7tGrmwjj42iYq2dYt9TJzMRbAHmfaDNLCQGASYn-M-6VOi-QmImQiapDlvedd44_QOO7unjj5YH3y-2wrUo-7aMYwnhTY2QmWZyWQ4L1hb19Tv7TGPgtgjo4eS9fevlmiulv6ew_YIwsS-KuDiGA9XjxXY3tyuCchn5wmvyqIaR2UdIkGRbEWkUlkJHYod8ky6lHJ0reHZ-bYiHvvrskNgdljgFbqx5l0JlekN_4FYiq1L_WzxuH0H2kmpG5yI3wu3T_STfd8UcdkpSHphJEFWIqOrC5RG7fGofEQwd73WLMleloh5Ivng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662325" target="_blank">📅 19:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مقام آمریکایی به الجزیره: جی‌دی ونس، معاون رئیس‌جمهور آمریکا همچنان در سوئیس حضور داشته و مذاکرات ادامه دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662324" target="_blank">📅 18:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662323">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8ll40q10LDAdBEzq9rDWBBhJgzIWXbZqkHvSdmp8dBpMH7YU5x35-ipxD5Z02W-5Rhzu_3CVFgXlSW_6VuNys-GUjm4oabq839U2p-phWf9PYMepNyCDrKMDXfqJ2rdLfEr8ZfIn3Bg4AQB4x8Y6tRcvPFKoCYbfsUhgdf74ieosjz2pYNd5jU2-7AKDENearayGTPeLK9nv6uP7OFOiOLhcvtt2WAKfg6qen5cHF37vWOCRSainvEZuwX3utX8Q14llvQOxrZXIdOmNU_F5nTHDZy0HYazt6ZGvYwKKR6vnKluVkv3amJ6vWjV8_ZOAjqui35wgD6-7BxgtQQCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آمریکا: تعهد ایران به ورود بازرسان آژانس در ازای فروش نفت  وزیر خزانه‌داری آمریکا:
🔹
ایران در جریان مذاکرات سوئیس، با «ترانزیت آزاد در تنگه هرمز» و «پذیرش بازرسان آژانس» موافقت کرده و در مقابل، آمریکا مجوز ۶۰ روزه برای فروش نفت ایران صادر کرده است.…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662323" target="_blank">📅 18:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662322">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
آغاز مذاکرات فنی ایران و آمریکا در سوئیس  سخنگوی وزارت خارجه:
🔹
مذاکرات فنی ایران و آمریکا در چارچوب یادداشت تفاهم اسلام‌آباد از امروز در سوئیس آغاز شده و ریاست هیأت ایران بر عهده کاظم غریب‌آبادی است.
🔹
این گفت‌وگوها با تمرکز بر موضوعات هسته‌ای، تحریم‌ها،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662322" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662321">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سفر وزیر امور خارجه آمریکا به سه کشور عربی حاشیه خلیج فارس
سی‌ان‌ان:
🔹
مارکو روبیو این هفته با سفر به امارات، کویت و بحرین، پیرامون اولویت‌های منطقه‌ای از جمله یادداشت تفاهم با ایران، تضمین عبور امن از تنگه هرمز و ثبات منطقه گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662321" target="_blank">📅 18:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662320">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نخست‌وزیر قطر: نشست امنیتی ایران و کشورهای خلیج فارس در راه است
محمد بن عبدالرحمن آل ثانی:
🔹
در مرحله بعدی مذاکرات ایران و آمریکا، نشستی با حضور کشورهای عرب حاشیه خلیج فارس برای بررسی «امنیت منطقه» برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662320" target="_blank">📅 18:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662319">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcPYoVu12d0ojIL1ziaTdAnNhgOA6f_gT5yfyNXhsS9MRVc1M1IX6q__3iheW_rQuCr5y0v5LJXudky2pq8SJuF7cCXA0EaYYjk4BOhEYc0szn6jmBn0w8hA-ozcFJ0yTn8csTWWeZbviNzzo0IV7n71hOTONkFWrl5tZ8lmPstacAtOUDDdCXt4CaSSwXNtRdzsCZeuD8Fo1Tn7KKlsQZhEBbDMYqson7Ae_9DhDeTdlmVi9B1F9HuOQEUkzNwc3bKnmKQ7RiGB5J70D7EmpK59O5LwXNI-8ujpJLC39BRiqglFg3Im1_9Y7TAlZtMMJXLvMzvd8iAaTebesZm_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از کت‌و‌شلوار دیروز همتی در مذاکرات سوئیس که سوژه رسانه‌ها شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662319" target="_blank">📅 18:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662318">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvVOI2CxfzsEcKNgRuf_EsvRmatoljfQsNR0ygJ3PP0ZKaQ9fYY7EBkepUOLSlIhUNrShlVOGwcNTCT8HuMObHCSVkgH8Xw0cSTUb-hjbg58dXjGMkLOYw48wopvFX0SPzZZ0rJke23jmshjUIX09P_SXBu3XIjdzuRwaLzZIxw7-LAh1Wsxj559sLoHmb4skrBqHgjRgoXYgtgYZVzfaX7aVqoqcvM-ct4-j9zEqpJDwFyO8mgOyoYQroJOwowCs0N9J-DrmtSiWFamlAU5dR6eZR--IeMuQmQMos2481asS4j9wjFiaUnLg_aamQIyQuDwHCGOH9POym4yj3i5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت تشکر تیم ملی ایران پس از مسابقه با بلژیک در رختکن
🔹
از ایران باستان هزاران سال پیش تا ایوان متمدن امروز. روح ایران زنده و استوار است.
🔹
ما با غرور به لس‌آنجلس آمدیم، با افتخار رقابت کردیم و با عزت آنجا را ترک کردیم.
🔹
لس‌آنجلس، از مهمان‌نوازی شما متشکریم؛ و از تک تک ایرانیانی که در طول این ۱۸۰ دقیقه قلب، صدا و روح خود را برای ما فدا کردند، متشکریم.
باشد که صلح، احترام و دوستی در میان همه ملت‌ها برقرار باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662318" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662317">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: بازیکنان تیم ملی با همه وجود تلاش کردند
رئیس‌جمهور:
🔹
شاهد بودید که چه صحنه‌های زیبایی خلق شد. بازیکنان با تمام وجود تلاش کردند و سرود ملی جمهوری اسلامی ایران را با افتخار خواندند.
🔹
امروز ایران در صدر اخبار جهان قرار گرفته و از ایران و ایرانی با عزت و نیکی یاد می‌شود و این دستاورد چیزی جز نتیجه وحدت و همدلی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662317" target="_blank">📅 18:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662316">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=Lv8Zalhp4KW8l9sczFa1vGbAwXEVU-3TvHX8fzw0v6VXxIGqmDBrf9aBsyj5lDK3UcKxVIM5mUNDuy9tNDb8yQbyDU85XTQAd8OqapYDChhHsJQtIobUldxIOKXYUtJpzPjJzzJdqtR36PJlUxBfX_VyZbLRNiI2xC9SNj40Sv2CADax7zJmqZpBr1zh5hudpg6GYC1FxfTWKQ8NGuJY0FXVd03IGLAEqaM3tgnyTon46akL40lWRgw7CsXjQs6IAXX8aJPHfvYAEf_9kO6qL4AnmPnAXc011NEUw4xf-xmx5pQaOF8c8V3MLNCWYSQNhgMZ7DxDvxsRjwyMBiDx3IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4e5db99c.mp4?token=Lv8Zalhp4KW8l9sczFa1vGbAwXEVU-3TvHX8fzw0v6VXxIGqmDBrf9aBsyj5lDK3UcKxVIM5mUNDuy9tNDb8yQbyDU85XTQAd8OqapYDChhHsJQtIobUldxIOKXYUtJpzPjJzzJdqtR36PJlUxBfX_VyZbLRNiI2xC9SNj40Sv2CADax7zJmqZpBr1zh5hudpg6GYC1FxfTWKQ8NGuJY0FXVd03IGLAEqaM3tgnyTon46akL40lWRgw7CsXjQs6IAXX8aJPHfvYAEf_9kO6qL4AnmPnAXc011NEUw4xf-xmx5pQaOF8c8V3MLNCWYSQNhgMZ7DxDvxsRjwyMBiDx3IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، کارشناس صداوسیما: آمریکا ۱۰۰ آب‌نبات جلوی تیم مذاکره کننده ایرانی انداخته است تا مروارید ایران که تنگه هرمز است را از آن‌ها بگیرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662316" target="_blank">📅 18:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662315">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d05ad146d.mp4?token=XSGEVBijbw1VZ8Ot20IHMZrOR5Cze4dYtIr4RsXwI6MC4yDunaz0xfX_ugg7LqXfK7yFldCncPtVRAb3G9Apu_D7MgsSTnqZCl_SJX9Uzli54WwqHwK6bKWoWeaP4p4MXrWmlA2Fksc2nm7NYM3X9tx31uQDkhawKV3FhTWahb2k2Ickuv6_YCzw6taByvP_l-OzO6B3EoSKlyvJ8o0loI_spVJ7EXbfVyjJiFTd5-4gxpPe9gBZ6CIu5D0HKHZIwm1KPwNxKqNCbIJP1KFt5UKRlg-D_unkGERJ3hKJoQXTo3GQ8yNDgwT80MgRl7parq_r8_KeUQaWPpcdv8LBiFtbrCuQb8zX-aTH2ZzE-HqADcPFGY9zHvJ3U2diCJt6aJsJFacZ8X782Tq7UiwU8aFOv8GnhEMMogeVKd_r3EXE7xEV2XsN6UOzRG-jplTbJg0_3dM2L1SBnVI7vr07bVQ1uH37gJNHuKMd9Ua6To0lVj_YJ2fqMT6OOoHzS-TDNEHAd_cKOU4GsbX0XWHmfg37G77Zhjil4E_Tl60zdsVz-D9aqearaikOykrZbYDrCfc6cTpIqWOb3xPxtZVvUQ0V5KYdbV89AMWSgrrQZrY1_r90zX_39By5S5f54Mrm7yGLhklRcKyIM4Gu27lJXCbQd4KDjt_LeQYsKMh2HZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d05ad146d.mp4?token=XSGEVBijbw1VZ8Ot20IHMZrOR5Cze4dYtIr4RsXwI6MC4yDunaz0xfX_ugg7LqXfK7yFldCncPtVRAb3G9Apu_D7MgsSTnqZCl_SJX9Uzli54WwqHwK6bKWoWeaP4p4MXrWmlA2Fksc2nm7NYM3X9tx31uQDkhawKV3FhTWahb2k2Ickuv6_YCzw6taByvP_l-OzO6B3EoSKlyvJ8o0loI_spVJ7EXbfVyjJiFTd5-4gxpPe9gBZ6CIu5D0HKHZIwm1KPwNxKqNCbIJP1KFt5UKRlg-D_unkGERJ3hKJoQXTo3GQ8yNDgwT80MgRl7parq_r8_KeUQaWPpcdv8LBiFtbrCuQb8zX-aTH2ZzE-HqADcPFGY9zHvJ3U2diCJt6aJsJFacZ8X782Tq7UiwU8aFOv8GnhEMMogeVKd_r3EXE7xEV2XsN6UOzRG-jplTbJg0_3dM2L1SBnVI7vr07bVQ1uH37gJNHuKMd9Ua6To0lVj_YJ2fqMT6OOoHzS-TDNEHAd_cKOU4GsbX0XWHmfg37G77Zhjil4E_Tl60zdsVz-D9aqearaikOykrZbYDrCfc6cTpIqWOb3xPxtZVvUQ0V5KYdbV89AMWSgrrQZrY1_r90zX_39By5S5f54Mrm7yGLhklRcKyIM4Gu27lJXCbQd4KDjt_LeQYsKMh2HZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دردناک و باورنکردنی/ روستایی در سیریک که پس از جنگ فقط ۸ ساعت در ماه آب دارد
🔹
بعد از حمله آمریکا به منابع آب ایران، حالا مردم روستای کنارجو سیریک فقط هر ماه روز چند ساعت آب دارند!
🔹
در این ویدئو شما شاهد روایت تلخ ساکنان کنارجو هستید از روزهایی که آب، به کالایی کمیاب تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/662315" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662314">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6D5IFD-5qS7Smw4Ii5P_2S11EM-p-m6HZrVQgQ5_edlMXjsGtH-mKSPswDfN5jc6jXVE1aOIMLdosmPew2I2H8jSKgiC2APO5OT1NiQuB-CIPmL258Jziyp34mLXWfyg1abPCcCwcAZquv3bgWZbwSkfrVKM7IoDb5rA4hw4-Pe1MEWfMsHAgAq8CbZQUTSfg3VRaJcvCrd0Kjerb0hyNO2tt87Z2KzAt8OznOy0QEJl6gv4ZgNT0Xh_8RJCjgRmMHlZ0EDdducw_jt34SpyBaKNCzf9eT1A-bc_r8kxzJFEcfuVtjH3U8l6FaeqYc4tXXiEHQ36A6YwS3U5iaSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از برکلی تا دهلاویه؛ داستان شگفت‌انگیز مصطفی چمران
🔹
مصطفی چمران؛ فیزیکدان برجسته‌ای که در آمریکا دکترای پلاسما گرفت؛ اما آزمایشگاه را رها کرد و به مبارزه در لبنان و ایران پیوست. کمتر کسی می‌داند او نقاش، عارف و نویسنده‌ای توانا بود. چمران ترکیبی نادر از…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662314" target="_blank">📅 18:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662313">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا: وزارت خزانه داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662313" target="_blank">📅 18:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662312">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8Y6PHM9tyLK4fuOTZymGUh9unJnlxp4UaOV9KQqN6zCus8_HUSvaEOGnPwmp3s0nW-eRMNbnxH-t-ReVFHBD70l8tMxoqmjKfbv_ZvASzzSdW4ZazvFoBh-R6lfdbOvBLiEhw9F7n4FeEPnInMDngCBR6nR_6M82Me1A9g067lflTFCbApKcVc5O-2Vyok9n8q49wmYT3KmOjrjwz-Mdn4o1GF1vdVnHXYAbtDuyFjA-_GV-4kSdqAMvhm-JBc_cyD2ldplfrKZ-b8sehp-qfpq3KGO3bjMkSsngUVNC8wceLqitHIVMuBunOyg7ma93WFm6XI10vCXoD0NEqhJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ امتیاز برای صعود کافی است
🔹
برخی نتایج غیرمنتظره تا امروز باعث شده حداقل امتیاز لازم برای صعود به مرحله یک‌شانزدهم نهایی به‌عنوان تیم سوم کاهش پیدا کند.
🔹
در حال حاضر، کسب ۳ امتیاز و تفاضل گل منفی ۱ با احتمال ۹۶٪ برای صعود کافی است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662312" target="_blank">📅 17:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662311">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای کانال ۱۴ عبری: در ۴۸ ساعت گذشته هیچ حمله‌ای در جنوب لبنان رخ نداده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662311" target="_blank">📅 17:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662310">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ایران در برابر یک انتخاب تاریخی؛ تضمین واقعی یا تکرار تجربه برجام؟
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
«هیچ تضمینی وجود ندارد که آمریکا به تعهداتش عمل کند.» حتی قطعنامه شورای امنیت هم تضمین نیست؛ همان‌طور که آمریکا قطعنامه ۲۲۳۱ را نقض کرد، اگر توافقی حاصل شود، ایران باید موافقت کنگره و سنای آمریکا را بگیرد و به وعده‌ها اکتفا نکند.
🔹
ایران امروز در برابر یک انتخاب بزرگ تاریخی قرار دارد؛ یا در چرخه بحران، فشار و تحریم باقی بماند، یا دستاوردهای کنونی را به پایه‌ای برای ساختن آینده‌ای قدرتمندتر تبدیل کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662310" target="_blank">📅 17:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662309">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30287af157.mp4?token=nN15V0XctFLV0ho8s9OEwVlwzLcJRkHmvMQ3GatWS3WsxgcLgv7p8XO0KEgW202-s8ZSv3w3vopfmg8gM2L6z1mD61oWPP-2cGUkFoVVWNXGtUF97pJPcWrSC6JKI-E1k-peSjj3qmTREF9zwyS-CClUn0Sdn2NxCzZ3EYqf_vNGxoZZuSOymMZv8xw4BB_70UjI0XLi7pWP5Joi90Xb13LPMEKykrkyWcycYdaKh_skRXWKDLG5g6QcCDtVPzpthN9MTUUbDuRc-rIqAuZzcwGi86JpghIs3xmfazkb1064P3JogmzTtA6-_4ngFrvFCAG7so4w7Di27ueMNxyEIlP1Wyhnt6G3OJ8enoNp3rW5sxOwCQI7fJaWT6wHkS_tiaXRdfN9n4JI3krXnIVzl7NuCCsm8V5MH4D1wDfy02HQUSdzu7PTRz0Rj1I9tACEpcAOH98qIssIHgTmrfIjipGTKb0cuMACudxMMbjocriCSfsfR4yJz5jf4w5AOX8bdEgUQBeqXvyWre0KWrooFxqV5c9UzQABYlzwmz6izICUXxabdrw_agT4ubO5w1zLqvz0TnHoeXxfk6l8ef-JEMu-BJzDC7lK7oagvcghkdcSna_RQbFxUPhXcNZ1AVWc33msN3FTP4DM5FDveVpNULIYmG8vAv-lYYiNHhrK8Pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30287af157.mp4?token=nN15V0XctFLV0ho8s9OEwVlwzLcJRkHmvMQ3GatWS3WsxgcLgv7p8XO0KEgW202-s8ZSv3w3vopfmg8gM2L6z1mD61oWPP-2cGUkFoVVWNXGtUF97pJPcWrSC6JKI-E1k-peSjj3qmTREF9zwyS-CClUn0Sdn2NxCzZ3EYqf_vNGxoZZuSOymMZv8xw4BB_70UjI0XLi7pWP5Joi90Xb13LPMEKykrkyWcycYdaKh_skRXWKDLG5g6QcCDtVPzpthN9MTUUbDuRc-rIqAuZzcwGi86JpghIs3xmfazkb1064P3JogmzTtA6-_4ngFrvFCAG7so4w7Di27ueMNxyEIlP1Wyhnt6G3OJ8enoNp3rW5sxOwCQI7fJaWT6wHkS_tiaXRdfN9n4JI3krXnIVzl7NuCCsm8V5MH4D1wDfy02HQUSdzu7PTRz0Rj1I9tACEpcAOH98qIssIHgTmrfIjipGTKb0cuMACudxMMbjocriCSfsfR4yJz5jf4w5AOX8bdEgUQBeqXvyWre0KWrooFxqV5c9UzQABYlzwmz6izICUXxabdrw_agT4ubO5w1zLqvz0TnHoeXxfk6l8ef-JEMu-BJzDC7lK7oagvcghkdcSna_RQbFxUPhXcNZ1AVWc33msN3FTP4DM5FDveVpNULIYmG8vAv-lYYiNHhrK8Pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فینال تاریخی جام جهانی ۱۹۷۸ با کیفیت 4K
🔹
این بازی بین آرژانتین و هلند که با نتیجۀ ۳ بر ۱ به قهرمانی آرژانتین انجامید و یکی از خشن‌ترین فینال‌های جام جهانی تاریخ شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662309" target="_blank">📅 17:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
هیئت مذاکره کننده کشورمان به تهران بازگشت
🔹
هیئت مذاکره‌کننده کشورمان به ریاست قالیباف، پس از سفری ۲روزه به سوئیس، دقایقی قبل وارد تهران شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662308" target="_blank">📅 17:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
بزرگترین رویداد قرآنی مردمی کشور در جوار امام سلطان
🔸
حفظ رایگان ۲ ساله قرآن کریم
🔸
سفر یک ماهه به کربلا و نجف
🔸
سفر به قشم و شمال و کرمان
🔸
استفاده از خوابگاه شبانه روزی
🔸
دریافت مدرک لیسانس قرآن
🔸
بورسیه تحصیلی در مقطع ارشد
🔸
زیارت و حفظ روزانه در حرم
🔸
استفاده از اساتید مجرب حفظ
🔻
۱۴ تا ۲۲ ساله های عزیز جا نمونید.
🌱
اعتکاف با قرآن در جوار عترت
🔸
جزئیات این تجربه بی‌نظیر در عمرتون را در این کانال مطالعه کنید
👇
👇
https://eitaa.com/samenalhojajj
🔻
جهت ثبت نام در سایت
👇
http://Samenoon.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662307" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
هنوز مسیر نهایی تشییع در تهران اعلام نشده است
فرمانده سپاه تهران:
🔹
مسیر نهایی مراسم تشییع هنوز قطعی نشده و طی روزهای آینده اطلاع‌رسانی می‌شود؛ روز اول مراسم در تهران تعطیل خواهد بود و درباره تعطیلی دو روز دیگر نیز در حال بررسی تصمیم‌گیری هستند.
🔹
او همچنین گفت مصلی تهران از صبح ۱۳ تیر تا نماز مغرب و عشای ۱۴ تیر به‌صورت شبانه‌روزی آماده پذیرایی است و نماز بر پیکر، روز ۱۴ تیر در مصلی اقامه می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662306" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سفر پزشکیان به پاکستان تایید شد/ رئیس‌جمهور فردا در سفری یک‌روزه به اسلام‌آباد می‌رود؛ توسعه روابط اقتصادی و پیگیری مصوبات گذشته از محورهای این سفر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662305" target="_blank">📅 17:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662304">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1e7KQxyKfWnloKxzaCuMfiuVC0ONbU0mTALbgpMsCLU5V_jvAhKfmgUbeNXxzUdDj0mZ6okRrzO0qeM98BVkv4F5wg8NcWOOJ1NoasXbvLSZVIIREsrR1aKbZ2PZfm_WGSsm3u0ji5QG2Xlz_nWgNrZinfzmLFbeUG3z4ZsO3UlDXH7RL15ck3cFtoPZLSDcOWx0PSYU8__qm4RlfVih8yYcBERzs--Wll4V9fNLCVxWazkyUet3KJocb0SJ7mDmKlbeaQkgu0lBaOamZ03u-W9ec_DxXNftb-zy4ZOfN5I6jJppDQv8I8Y5h5lQJfOijiCecXSxjxW2HhdZdJAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کنتورِ زمین، رویِ دورِ تند!
🔹
هر «کیلووات ساعت» مصرفِ غیرضروری، یک پله گرم‌تر کردنِ زمین است.
🔹
صرفه‌جویی در مصرف برق، امروز دیگر یک انتخاب نیست، یک ضرورت برای بقاست.
#مدیریت_مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662304" target="_blank">📅 17:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662303">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbac53cfe3.mp4?token=JaNPMHJMq7RWNndYQvo7LonxJ6GDKE0G9nyLysZQ2uM9Qc7i019MmLgqW6RrhUe9bD7kRs_iWjD7L9rp5KBMg91Q1NF0hRBbQl1Tr-7zc14WcGW6axk_e2LBsHZPfA2v4vIE-KsjkO1HJS_pBxBi90ZvweXdPTAqz2XRRTWvE76Jk--_F6LKcDBfnUFAW6EWLmys5_463oQL_9tZU4M7ECeBqh5cIDTbrNB2UDvS3ITnA8gkyTLEzC7o8aNgxTc1R-Ps1sG5JZ060DF9oFTlNhzMGv9OAToztOLAcBOKLXEw_ryc5Iu4_4ZgU66eVN8N5tqNKYlKN2xylCA9EotYLllSlsiYKnMySpfOWyJjcebKtJ_WHJWtN8PBuLK_22qsus997JXO-h9-UhOBiNq4xhGt_HWRZ952wxtCPlnSKHEnGYdZR5LbeWNA0BoQ9pUH-ec6kcJlDyK6KGs29LtG0jKLlmGiprcEmDKBSBvhvyCdgk_SgfCVIiFds4c7YACAKOoiwZ92ddoy6mpdz5gY78EC9DrO9Us0OjBCXsoGSt_Uc7v9bRE1Es2y_gfrWJYiRGc87YmabLHIT2nwrgftHeqoVVtgC3_maIuAj6x7cx2-7chX4FXZaU-dKobD4uSdAQ6F0j7bcuYZp-edC0T6NU9g2_fj27wBIBeirpFpd20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbac53cfe3.mp4?token=JaNPMHJMq7RWNndYQvo7LonxJ6GDKE0G9nyLysZQ2uM9Qc7i019MmLgqW6RrhUe9bD7kRs_iWjD7L9rp5KBMg91Q1NF0hRBbQl1Tr-7zc14WcGW6axk_e2LBsHZPfA2v4vIE-KsjkO1HJS_pBxBi90ZvweXdPTAqz2XRRTWvE76Jk--_F6LKcDBfnUFAW6EWLmys5_463oQL_9tZU4M7ECeBqh5cIDTbrNB2UDvS3ITnA8gkyTLEzC7o8aNgxTc1R-Ps1sG5JZ060DF9oFTlNhzMGv9OAToztOLAcBOKLXEw_ryc5Iu4_4ZgU66eVN8N5tqNKYlKN2xylCA9EotYLllSlsiYKnMySpfOWyJjcebKtJ_WHJWtN8PBuLK_22qsus997JXO-h9-UhOBiNq4xhGt_HWRZ952wxtCPlnSKHEnGYdZR5LbeWNA0BoQ9pUH-ec6kcJlDyK6KGs29LtG0jKLlmGiprcEmDKBSBvhvyCdgk_SgfCVIiFds4c7YACAKOoiwZ92ddoy6mpdz5gY78EC9DrO9Us0OjBCXsoGSt_Uc7v9bRE1Es2y_gfrWJYiRGc87YmabLHIT2nwrgftHeqoVVtgC3_maIuAj6x7cx2-7chX4FXZaU-dKobD4uSdAQ6F0j7bcuYZp-edC0T6NU9g2_fj27wBIBeirpFpd20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به شعار «حی علی االاصول»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662303" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662301">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/980b0543dd.mp4?token=ksMtqOTQZlVbB788cTCP3Ej5hqoQG37H1eKSZIriMDkALoM-qI-IYk44Oh3Z5xc3p8lLgDPnf5iRkIfa7EQirSARJp1UuSBFAwWilHZDeEs7jTU_lYIq4j64o6xQiQv4jOubs-8MKdThXbnP_VAASTVa4U7LMstWFhdCHwOKH_vnYtJnwZFi0sI29NcKgzrvbf6oTyCOq7DNljOHAmKjYOUk8CxVNOIB5pF8OiSv62T28vXbymWqzXSjmtc_3m6g-fuKpiXKJZWXO2FV3jncmMTbZmXYwZ1xbPMLrUnIOr2XgUOpe-BCJPEUYOUUsCVG_fSmXXaimQYHUf8G8tUkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/980b0543dd.mp4?token=ksMtqOTQZlVbB788cTCP3Ej5hqoQG37H1eKSZIriMDkALoM-qI-IYk44Oh3Z5xc3p8lLgDPnf5iRkIfa7EQirSARJp1UuSBFAwWilHZDeEs7jTU_lYIq4j64o6xQiQv4jOubs-8MKdThXbnP_VAASTVa4U7LMstWFhdCHwOKH_vnYtJnwZFi0sI29NcKgzrvbf6oTyCOq7DNljOHAmKjYOUk8CxVNOIB5pF8OiSv62T28vXbymWqzXSjmtc_3m6g-fuKpiXKJZWXO2FV3jncmMTbZmXYwZ1xbPMLrUnIOr2XgUOpe-BCJPEUYOUUsCVG_fSmXXaimQYHUf8G8tUkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرش تماشایی مارلین‌ها در اقیانوس
🔹
مارلین‌ها با جهش‌های قدرتمند و آکروباتیک از آب بیرون می‌پرند؛ رفتاری که هم برای رهایی از انگل‌های پوستی انجام می‌شود و هم برای گیج کردن طعمه‌ها یا فرار از شکارچیان بزرگ‌تر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662301" target="_blank">📅 17:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMR1xRJE7SAofBgvNi1Ccd3BbvvrkMlk_R9Uxho2Sf76NRq7U_RdumD23EMd0PMnvOu_7R0ZqRwgA8ES-wInUgSOs6VObrjlsOF0CDdBURraYrk5zphClMdCtFge2rn-1iNZAUJ1BPdzHjvFROnMxmkNlrZDjcCAc-1er0_i5cIp_nno9gqCvtU5SDD3oLt_tWm9o37dQXVDw4K6j4z4oxysEYQalnt1LMsibMTNiBngHDfk0NIiBsaM4UU1i3Be5rc0zEuzE4kNl-uoO9ZU75ntVosKAHjXFLPsLkGAt2Le2YZQM28KwKvKreyVb2f5bh1tWopkFI-lqLFzztg1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحریم‌های نفتی ایران به‌طور موقت لغو شد  وزارت خزانه‌داری آمریکا:
🔹
مجوزی صادر کرده که بر اساس آن ایران می‌تواند تا ۲۱ اوت ۲۰۲۶ نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی خود را به فروش برساند.
🔹
طبق این بیانیه، واردات این اقلام از ایران به آمریکا نیز در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662298" target="_blank">📅 17:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b57Z5VUiEtRDdIfdrUkjS35gs6KJN-ehnd7UybfjZct49EQNss62zy8q-uzDt5qUwujNX9wXeJ20QZewIehy3M2ya3BUGhMWv8ybCMUusT7OQ_9yVXNh8uV_PCZN0NK3byxXe4xd34fH_Eu4XUSmcq4gvFROL3a6HW_HpkxaomdpplGP01avkviaE0_w65fJGPDI_B9OsHeiHHepq3rbNS1ZNUcVX39J-35m0zL5fEoO9SOmlShuUDWCiaNbeVq8cE5gE3be52r9AF2OiBEbfheNVCgSebxH8Gbaeu4521xfQQm-8aG0RaJ5qZhgBfVBGz95LD4lfpShPR5PX9qRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحریم‌های نفتی ایران به‌طور موقت لغو شد
وزارت خزانه‌داری آمریکا:
🔹
مجوزی صادر کرده که بر اساس آن ایران می‌تواند تا ۲۱ اوت ۲۰۲۶ نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی خود را به فروش برساند.
🔹
طبق این بیانیه، واردات این اقلام از ایران به آمریکا نیز در چارچوب همین مجوز مجاز خواهد بود.
وزارت خزانه‌داری ایالات متحده آمریکا
واشنگتن، دی.سی.
دفتر کنترل دارایی‌های خارجی (OFAC)
مقررات معاملات و تحریم‌های ایران، بخش ۵۶۰ از عنوان ۳۱ مقررات فدرال (CFR)؛
مقررات تحریم‌های مرتبط با فعالیت‌های زیان‌بار خارجی روسیه، بخش ۵۸۷ از عنوان ۳۱ CFR؛
مقررات تحریم‌های مرتبط با اوکراین/روسیه، بخش ۵۸۹ از عنوان ۳۱ CFR؛
مقررات تحریم‌های اشاعه‌دهندگان سلاح‌های کشتار جمعی، بخش ۵۴۴ از عنوان ۳۱ CFR؛
مقررات تحریم‌های مالی ایران، بخش ۵۶۱ از عنوان ۳۱ CFR؛
مقررات تحریم‌های بخش‌های اقتصادی ایران و نقض حقوق بشر، بخش ۵۶۲ از عنوان ۳۱ CFR؛
مقررات تحریم‌های جهانی تروریسم، بخش ۵۹۴ از عنوان ۳۱ CFR؛
فرمان اجرایی ۱۳۸۴۶ مورخ ۶ اوت ۲۰۱۸
(«بازاعمال برخی تحریم‌ها علیه ایران»)؛
فرمان اجرایی ۱۳۸۷۶ مورخ ۲۴ ژوئن ۲۰۱۹
(«اعمال تحریم‌ها علیه ایران»)؛
فرمان اجرایی ۱۳۹۰۲ مورخ ۱۰ ژانویه ۲۰۲۰
(«اعمال تحریم‌ها علیه بخش‌های اضافی اقتصاد ایران»)؛
فرمان اجرایی ۱۳۹۴۹ مورخ ۲۱ سپتامبر ۲۰۲۰
(«مسدود کردن دارایی‌های برخی اشخاص در ارتباط با فعالیت‌های تسلیحات متعارف ایران»)
مجوز عمومی شماره X
صدور مجوز برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشأ ایرانی تا ۲۱ اوت ۲۰۲۶
الف- به استثنای موارد پیش‌بینی‌شده در بندهای (ب) و (ج)، تمامی معاملاتی که بر اساس مراجع و مقررات فوق‌الذکر ممنوع بوده‌اند اما به طور معمول برای تولید، فروش، تحویل یا تخلیه نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی با منشأ ایرانی ضروری و مرتبط محسوب می‌شوند، از جمله معاملاتی که کشتی‌های مسدودشده تحت مقررات فوق را در بر می‌گیرند، تا ساعت ۱۲:۰۱ بامداد به وقت تابستانی شرق آمریکا در تاریخ ۲۱ اوت ۲۰۲۶ مجاز شناخته می‌شوند.
یادداشت ۱ مربوط به بند (الف)
معاملاتی که به طور معمول برای تولید، فروش، تحویل یا تخلیه چنین نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی ضروری و مرتبط محسوب می‌شوند، شامل موارد زیر هستند:
معاملات لازم برای پهلوگیری و لنگر انداختن ایمن کشتی‌های حامل این نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی؛
حفظ سلامت یا ایمنی خدمه چنین کشتی‌هایی؛
تعمیرات اضطراری؛
اقدامات کاهش آثار زیست‌محیطی یا فعالیت‌های حفاظتی مربوط به چنین کشتی‌هایی یا مربوط به نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی مذکور که در انبار نگهداری می‌شوند؛
خدماتی نظیر مدیریت کشتی، تأمین خدمه، سوخت‌رسانی دریایی (Bunkering)، راهنمایی دریایی (Piloting)، ثبت کشتی، تعیین پرچم، بیمه، رده‌بندی فنی و عملیات نجات دریایی.
نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشأ ایرانی که مشمول این مجوز عمومی هستند، شامل محصولاتی نیز می‌شوند که توسط نهادهای تحریم‌شده تحت «مقررات معاملات و تحریم‌های ایران» (۳۱ CFR بخش ۵۶۰)، «مقررات تحریم‌های مالی ایران» (۳۱ CFR بخش ۵۶۱) یا «مقررات تحریم‌های جهانی تروریسم» (۳۱ CFR بخش ۵۹۴) تولید شده‌اند.
یادداشت ۲ مربوط به بند (الف)
معاملات مجازشده تحت این مجوز عمومی شامل واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشأ ایرانی به ایالات متحده نیز می‌شود، مشروط بر آنکه چنین وارداتی به طور معمول برای فروش، تحویل یا تخلیه این نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی که به موجب این مجوز عمومی مجاز شده‌اند، ضروری و مرتبط باشد.
(ب) هرگونه پرداخت وجوهی که بابت خرید نفت خام، محصولات پتروشیمی یا فرآورده‌های نفتی با منشأ ایرانی و مطابق بند (الف) به ایران، دولت ایران یا هر شخص مسدودشده بدهکار باشد، می‌تواند به صورت وجوه دلاریِ مبتنی بر دلار آمریکا انجام شود.
(ج) این مجوز عمومی موارد زیر را مجاز نمی‌داند:
۱. هرگونه معامله‌ای که شامل شخصی باشد که در جمهوری دموکراتیک خلق کره (کره شمالی)، جمهوری کوبا، مناطق مشمول اوکراین مطابق تعریف فرمان اجرایی ۱۴۰۶۵، منطقه کریمه اوکراین مطابق تعریف فرمان اجرایی ۱۳۶۸۵ مستقر باشد یا تحت قوانین آن مناطق سازمان‌دهی شده باشد؛ همچنین هر نهادی که در مالکیت یا کنترل چنین اشخاصی باشد یا با آنان مشارکت تجاری (Joint Venture) داشته باشد.
۲. هرگونه معامله یا فعالیت دیگری که به موجب هر فرمان اجرایی دیگر یا هر بخش دیگری از فصل پنجم عنوان ۳۱ مقررات فدرال (31 CFR Chapter V) که در این مجوز عمومی به آن اشاره نشده است، ممنوع باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/662296" target="_blank">📅 16:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گزارش ها حاکی از آن است که انفجار در صنایع گاز در قطر رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662294" target="_blank">📅 16:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662292">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrofi5zXVDBPmKEeTIGQkGGPL0cUvOTGRkXYR1ZlRYKlBYcG0SfJMa3mKcRQPNI1nS25hP3HR_ZzXjvCZ-tCDWTnFu0Cn3e9F_01vc9Oj7wftqQWK4HM4KKEx1OF4ahW62zgo5im4pfxS0W07AV-PLotu-vWo2LJBzgKMj07ayOPiSWYxdogjHucKbmBF9yOxKiExeVoRUUc0MLezol6_-CuMY9uRtV57xtyMNEDFbpy4X5RuZkGtZnQ3XxSRi0A5wrYFBgL8uodHil9jiowe9YMNsh5Kgp04xYE5HEbtRn_HDj4Dv_xM3IwTSNALiO6WE9UDpV4oKlz5RoAGmNgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشان حسینی
🔹
همراهان عزیز خبرفوری ؛ اگرجایی از خانه یا محل کارتان به نام امام حسین (ع) سیاه پوش شده است یا نشانی از عزای سید الشهدا برپاست  از آن عکس بگیرید و با ما به اشتراک بگذارید.
🔸
تصاویر خود را از طریق پیام‌رسان برای ما ارسال کنید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662292" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
چرخش مواضع دولت عراق در قبال ایران
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
دولت عراق که با حمایت جریان‌های همسو با ایران در «چارچوب هماهنگی» و با ائتلاف شیعیان، سنی‌ها و کردها تشکیل شد، در رویکردی قابل‌تأمل حق دفاع مشروع ایران در برابر حملات را محکوم کرد؛ تغییری که نشان‌دهنده تقابل سیاسی و امنیتی جدید میان این دولت و تهران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662286" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245b4e3f13.mp4?token=ErD1vAovFFtDhHAOOCNQFtSZKl_XjklGTr0w1isOjpS42L77JNhQMfSRBN84bHGAiLb17QV5SXhH082RlT6C9hnPzVbAge3Fa8rlWshVHZ771g5W55YXuWHsQgdYaWWobAzW2dDmBFO7dGSf8lo7lnwlM3OnK6f0_chhFdIgdy6I3I3y2-UZe2XKuCCclEeyUFXXQhkeU3kCQUjDSEm3LGdTAr8n03vP83PZl8qAUbdisvWGZUy8giHaemmahIkhhOTHmwLxJ_nkgyLNu4YyV_BjgMTY1rNiyFJLPW-BgMuHa1U-2savlHreAr_KKCS_Na31d7_qauQznw6wVHEHPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245b4e3f13.mp4?token=ErD1vAovFFtDhHAOOCNQFtSZKl_XjklGTr0w1isOjpS42L77JNhQMfSRBN84bHGAiLb17QV5SXhH082RlT6C9hnPzVbAge3Fa8rlWshVHZ771g5W55YXuWHsQgdYaWWobAzW2dDmBFO7dGSf8lo7lnwlM3OnK6f0_chhFdIgdy6I3I3y2-UZe2XKuCCclEeyUFXXQhkeU3kCQUjDSEm3LGdTAr8n03vP83PZl8qAUbdisvWGZUy8giHaemmahIkhhOTHmwLxJ_nkgyLNu4YyV_BjgMTY1rNiyFJLPW-BgMuHa1U-2savlHreAr_KKCS_Na31d7_qauQznw6wVHEHPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش قدیمی‌‌ترین لکه‌های خون رو هم می‌تونی پاک کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662285" target="_blank">📅 16:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8EB7RB3j2Egccii7hlHWdBsyLkXN0QpM1hrCIW402nlnXh3mHTMWLn244PfrgNih8TjrnXwYb7Q4fWXtZJI0fDqpwvVH_wCARs_P9hb3Lj83m_spHiTN2hL4W1lVlhLpN-psD_br8yYR_F5kEofcJqg7URhPmI5VLtOdneekwSj2QZwSQDDnD3Y_oXkwVI10d-OGpkZaHgDueIE5WFmuVKJbp1hiAL8HpHLxJ6Jc1eKakpClsY0-FVX1FDOebubhvAnhHOvHUcioMzs95L8L5KbNtFSKkomSYFlbb78WuUBwScRAWRH_NryKpezl8JEwL1W9hnHLjohvJ6tw3XnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سوم ظرفیت مخازن سدهای کشور پر شد
🔸
ورودی آب سدهای کشور از ابتدای سال آبی تا ۳۰ خرداد به ۴۳.۹۴ میلیارد مترمکعب رسید که نسبت به ۲۴.۴۰ میلیارد مترمکعب سال قبل، ۸۰٪ افزایش داشته است.
🔸
حجم آب موجود در مخازن سدها به ۳۴.۳۶ میلیارد مترمکعب رسیده که با ۳۵٪ رشد سالانه، موجب شده ۶۶٪ ظرفیت مخازن سدهای کشور پر باشد.
@amarfact</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662283" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c82edd02.mp4?token=Wj2kjOpezzU4lZlTRqDScIFzZ7vB9IgQsuW20A5dNC14dT79wwBpFK5nNVLoYr6D2YJ9U3tczGx1PXIwonjLWwraw9G6vNDr2QAtF5kPc9NryL_ZLF2vnbiTX3gX2Va-e83Y0PA7z5m7Lz8PVupSzd29RwhVn69aAHDIeDVxVfnxPBOfaqLTPpSzGELO2YhTVdkB3T3QAq-hJ-cYSs9fTpvJCChxt4SazaI55Z8PZ4XUrHM0-jMibNa46Boga34CJjOya-qTvxmDWZvnMTMEFPTcBxpYHs3iCEv5T7sOAqeXYeX5xcGwHCjE4Uvx75T8IQcDDp84O_3UpkkHzFPieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c82edd02.mp4?token=Wj2kjOpezzU4lZlTRqDScIFzZ7vB9IgQsuW20A5dNC14dT79wwBpFK5nNVLoYr6D2YJ9U3tczGx1PXIwonjLWwraw9G6vNDr2QAtF5kPc9NryL_ZLF2vnbiTX3gX2Va-e83Y0PA7z5m7Lz8PVupSzd29RwhVn69aAHDIeDVxVfnxPBOfaqLTPpSzGELO2YhTVdkB3T3QAq-hJ-cYSs9fTpvJCChxt4SazaI55Z8PZ4XUrHM0-jMibNa46Boga34CJjOya-qTvxmDWZvnMTMEFPTcBxpYHs3iCEv5T7sOAqeXYeX5xcGwHCjE4Uvx75T8IQcDDp84O_3UpkkHzFPieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش فرزندان‌تون رو‌ به میلیونر تبدیل کنید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662282" target="_blank">📅 16:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: تنگه هرمز باز است
شبکه سی‌ان‌ان به نقل از منبعی دیپلماتیک:
🔹
«اجرای یادداشت تفاهم آتش‌بس میان تهران و واشنگتن به مسیر درست خود بازگشته و تنگه هرمز برای کشتیرانی باز است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662279" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662278">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpgr_kIjFiu1yIZG4-dDxn9EF-LTec8bTeK19fSR62hdKNcT-x6pwqcthakzzxNwIQsVFJ2bucLnUURoFQtPrDojvAbmllYiURsv92zvnyxKiFNLibCvyNaKuDfgkHfXCRDljtMGjMG2eJYu1QQu_jcwDncgSI9ZvJUhtKkLdr66wZ3QXTbMwi1iJlp-j93yXxVL7jJKMhO_AZQXB46D1pVNxFk3YrIjIMyrHJEh6phPTRYphfdKYZzjimDLuP-TVnd4STNhIlPLHDyrWCe4paNa4wnfYwgOEKiaTyVPKZO5sQZeOlbGao0fToT11u5QCw3IAWL8Fx8Us6HSOoueKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در هر کشور توان دو عددهای دو رقمی رو چه‌طور حساب می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662278" target="_blank">📅 15:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662274">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXSGZNLxn-aHffxbEmVz2SlPy8DyEI0tcIHcW9y1GfxOPz5XlTRNflA9ysLd-t_k_yuspJmKL4Ty01fsZC7GGnd65_nc1FYEcN1WzyhNzemRAFcrVnujsWCYJIolk8VS4PEi1dTntF4DTB033wyPjxWjYY6Y-NI0n8l8hKzuCJZCx-K23yB2ys9RaaqZ7qHcMvJWWCysd8JM0yQBR93s_xoN0PZ3EKorTVIfOn3GcgurSR7R8aXZoV9VtKLhvnwNWySWI8vW7Bxuzq5rigI7PmzEVKMULy5Ezrs2318Y64BZIxJHRQiXyXDpimDdLmGiGUBbBkyqSrnJ4Rg3si4Vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJiBQx9OryY4KTnJAX2V7X-IppLFHgpmWJVDItfz648Bln7MIpH6GhyGsmyM0IDb1Uo67FfP3wVX0bIvolv3H99WDdN_TMwhU55P0uSjaLIPToA0qoOBgAeJIVimwI9elX4j2yiPhGMhJxwtBJxZc8jt-UXkUumyiKEISZtqJ0G0kTV900XAVWHmrS_eJ0B7MDm4N1Cp2Hq2niPk9RDC0fJfrQBWn9UV5t2Har45fa1vCnEZr6rO3pU0uMqLISPjYAFuMNlUI-CE6LFpiG1yJfU1ibAr0wgLU1UjGG_HAU_nAxJAlhWh5gBnVC5ot6Z41hCiphfFO7dWwhj-bSng_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGeI4eKUP8lUOdMgd_2wde_j9KQNju9qJ7DhWlPolNrAQcWAKsklN84n-G-6iLilbdIPoBuInI9v4ElWegnT7UTFstshOceMpGvwJZJ-1vorPdGP3C7L7CBu9VGjx1kvq71HAocou1QrDV4RODvE-DbWYNgXstDWHsNpypbEu2nH8G6IYgFuN5jLeSCKkzJf9CBr92Y1QtwJj5hH5XZHNPJ_pMwZvutwPEX3Bf7S8E7n-PMy2hIqU4vSoiw1ZKwDRYTkwTMmAUDH2Adko_OVRe1ZcvQwrUWR0cI5rTxYIMaY7UwsOCzFsFWVhe0VWpAfsevgo4OEYJMpZdNxxriJmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf3c22adf.mp4?token=jRs_v__ZLb-u9TyJg5eLD3tTDTMBigz6p4cjffKKvKCVqtCQ9iOYj9KHYYgqJ1B8G4wBryb2wTngsVCpC7Pr7Hq1RFAVTSODCdz_jxDDA4szFBE7qJl0sV4KxwehTur3k2MDkHSE2Modx0VgzeMVB5lF-VeKTE5GUdjfCg0DKV0BefIYUxmNAit65NoXQ2L4STulMEXzhqYPt3WbsUcFUVtURxFayVVK_iHLUJIsvH3csqa9WWC_TVrnpYKMnM9YfujUr80U02zZjWoPPlmww-wkx1eabhDLc0iQz0RJyadKQOxqkomfa6N_HoXOVZXKByEBo0nivT-5p_SjCJyq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf3c22adf.mp4?token=jRs_v__ZLb-u9TyJg5eLD3tTDTMBigz6p4cjffKKvKCVqtCQ9iOYj9KHYYgqJ1B8G4wBryb2wTngsVCpC7Pr7Hq1RFAVTSODCdz_jxDDA4szFBE7qJl0sV4KxwehTur3k2MDkHSE2Modx0VgzeMVB5lF-VeKTE5GUdjfCg0DKV0BefIYUxmNAit65NoXQ2L4STulMEXzhqYPt3WbsUcFUVtURxFayVVK_iHLUJIsvH3csqa9WWC_TVrnpYKMnM9YfujUr80U02zZjWoPPlmww-wkx1eabhDLc0iQz0RJyadKQOxqkomfa6N_HoXOVZXKByEBo0nivT-5p_SjCJyq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعی گسترده در پی آتش‌سوزی یک پست برق منطقه‌ای در شهر کارمیل فلسطین اشغالی
رسانه‌های عبری:
🔹
چندین ساعت قطع برق در مناطق وسیعی از کارمیل در پی انفجار و آتش‌سوزی یک پست برق منطقه‌ای به علت افزایش ولتاژ ناگهانی و اختلال در تجهیزات برق فشارقوی، رخ‌ داده است.
🔹
یک کاربر ذیل این خبر نوشت: «وحشت ما را فراگرفته، صدای انفجار، آتش‌سوزی و قطع برق بیش از پنج‌ساعته.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662274" target="_blank">📅 15:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662270">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6oTNkyS1755uJ4Mu87JvAoA4sVsCHFa2teCl13TGGDK4Sjy1gAbPYuVysGTvqL3OGa63UtgD0jgDYU1h4OwXSGEtBDBTt67IxjetJV5iMbr81eQRdbq-T4ZjTuxMu09Cfn_dkclVcgHDra5Ljerf_vHr_v48HcUoyCWuqSegUlAS2izf0iPn_gGAo61fgUTCCZ4lERv_Pvv4Rzwtghh7D0s-yw9YAm51GaTCi4bpj8wkn4iiWEtHxXv1LwvxCTFb69AHdEMXQOOeWjii25l-qAYa1rvPWwohwyQ-XJ3h_WQqIVjp6Hin5l2dMxrP5Jym_0DSD8G41CfX-7mvqMzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCNFPn597CMbAoqMOLOkSrypDE5GyJ5f8KpCBxf2R5rCga3UvmMtBKmXxrfk0uTuUzBzwikvE2BPDVl1fNEKEKHHatyKxrZbCC3KTaenioVTnGUkBQhWdtcVaog6Sob2kap9cUYPtP9O36NauHvlox1GDo4o45kyRw_ul8gTZJQ3znN_YVqP4z3bshzxQ7zkZcYr0bH2xYOQmiTo4zxAGkX0Aade9zN1lytKtZi9ItX6xJC5chjOCJ89SRX14Si9WmGGiFhiso_OJh5wbytaNp8QI2TSF1Vnz0LqcthPWahKqWUS9Hgo7op5ciM7sTsGaikj9gdND9gSPEzPY_q-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSV2v6hPTv6nAUEzn9OF4dYLx0qmBAtgDLasqpxDEc295bbfWXXIs1R0dMXX3zEFSI6g9guRXV6fbM4TpkXwFB1RjwofOUS77mZPGyaknjnHJ2FO8Z4vtO6Pf31dYS3Enw9_i69CTpjshG8eyHWKDx1vjCijmEOFPDRNAqB0tw2kOBjQBxMr-uDCDBPfmwy8D36yuwEzxBlEf_d9_VJkgJ9yBjna9ef2MigVZP5Wv7kQpjDWXQEdIwQuhez6zH1aOhlJUznHLSM1-jYqZnQm0_-zxTUFc706r_XCW9YvK3aR5y_n-JSlve3NkYOV0QMVrdUDPF20BSQZSDCJ_3OSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSjWHo_mNQH-RIiRtlaqeszZZ06_BGo4pU52X4tH04_5y4Zz9iRxnQFXW-Fl09pRMFm8K87nBCB_kVn5JtPNiwjgVfc_O7l86Ui-bd_8yufua9wjAMKr9xa75hHLaYFqsOaFovQCJvb57CciTarqr4d1nymwQS2Z-VknviU05xENCE8JvzbzmFWO1lF66ekkIdrDfFKLmfoR-INXuZQd4kITzt5Hq8nIt-ugQBR_bZjLxM6oa4XhDZi1iWQk-KbLQLX_9QMULiCh2YavWqyjoZWUy3O84sU5kDJ-jDtYBPOgFoPekp20B0YuvwdLFW2Ke5nYp6sVNhpvxStnIu9Zjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«
صورتی جیغ» رنگ جدید فوتبال جهان
🔹
استفاده گسترده از کفش‌ها و لباس‌های صورتی جیغ در جام جهانی توجه زیادی را جلب کرده است. کارشناسان دلیل محبوبیت این رنگ را دیده‌شدن بهتر در تلویزیون و تضاد آن با چمن سبز می‌دانند.
🔹
رواج این رنگ در فوتبال، نشان‌دهنده تأثیر مد بر دنیای ورزش و کمرنگ شدن نگاه‌های سنتی به رنگ صورتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662270" target="_blank">📅 15:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662268">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfMWHHBmZGE3-QboRMWY6jU2g1KmV4dvyw2wRfWzjZsf5FKY4NWsa6qTH3pgT3Tg07gloRywhBwHWBEMm-nlIXr5qw-zggFeF2RnCUi7gzzZylyftykxOxcSZi6njPaIcWEh6wvHp7mUGQNXHJYvAgyo2889n78EAAFG1kaHu6BaXsrGnjBSoqrqL1Wp9gPfefHOR7J_X2HuPGxLy0gLgPIOrmfZNYLrw9DfhKxzvX-Up2uF3bOZU1v0eXDje08i0dUcf21xtYilfGAw48OpDsDyqltKxuKLNhWTxMDS_oG2au2eZcmmHhkkNeEhWZBebsv5-hMhk-LR1667_axshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نام‌هایی جالب برای یکی از شایع‌ترین لک‌های مادرزادی
🔹
آیا می‌دانستید؟ «ماه‌گرفتگی» نوزادان در برخی کشورها «بوسه فرشته» و «گاز لک‌لک» نامیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662268" target="_blank">📅 15:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662267">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قطعی موقت سروش‌پلاس‌به دلیل قطع برق در دیتاسنتر شرکت زیرساخت
🔹
پیام‌رسان سروش‌پلاس در حال حاضر به صورت موقت با اختلال و قطعی مواجه شده است.
🔹
علت این اختلال، قطع برق در یکی از دیتاسنترهای شرکت زیرساخت است که منجر به از دسترس خارج شدن خدمات سروش‌پلاس شده است.…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662267" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662266">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c540cd4c0f.mp4?token=cFtB0fmZbLAORjnq7wLCfUG56kGhJtZivyJkIQ5NXc3jT-RTRIFPSuj8388ZhB7VR_7HQ7dDcmSzX-BgBeQwHB6ZQhTt_rICPs_egx6NUS0taq3edXKBBg98Q1qCsJerhVYI8N9K_-8hqAVLj8R7L-h_TyKmx5yI3rkn97Qkl2LmnDjF6SJdEjnvMVhy_enWsoPYP3Cylm29IavzcBLF4uUDTOv-9JTRcOXEawxiYlWOBfewhI1gROKmlURl9Ch0w_KjYqVeegG3Tq7wVF9eh6T_Q41n3k68fR3c84oeo6lA6AriinLf4r6seyG9LTYTCwInYxOsodiPFP7Ah3kv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c540cd4c0f.mp4?token=cFtB0fmZbLAORjnq7wLCfUG56kGhJtZivyJkIQ5NXc3jT-RTRIFPSuj8388ZhB7VR_7HQ7dDcmSzX-BgBeQwHB6ZQhTt_rICPs_egx6NUS0taq3edXKBBg98Q1qCsJerhVYI8N9K_-8hqAVLj8R7L-h_TyKmx5yI3rkn97Qkl2LmnDjF6SJdEjnvMVhy_enWsoPYP3Cylm29IavzcBLF4uUDTOv-9JTRcOXEawxiYlWOBfewhI1gROKmlURl9Ch0w_KjYqVeegG3Tq7wVF9eh6T_Q41n3k68fR3c84oeo6lA6AriinLf4r6seyG9LTYTCwInYxOsodiPFP7Ah3kv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: دیروز به ایرانی‌ها گفتیم وقتی شما کُری‌خوانی می‌کنید، نباید انتظار داشته باشید که ترامپ به آن پاسخ ندهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662266" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748789f2e4.mp4?token=LOt-lQdyy27hYVcnLRE2Fh4WYssb77xrwdZKuKG0Wq4w0js5SpyvMBIMTd1lwfIMph66Z2-8tId1Uo2pN7ie-svCDGK0nVXsPFH7qsJitWwXhEc0jq1lpW0UVFBRg5lkdPG9mXO7qsp3cHTDd2sGm7OnFkiQrO4wI-WOOWIDPiYofAIUeGXpN-YZ-G7E1zkx2kOFFIZAM73o4MA41ksvep4eiKfvNf-_t_YoaqC0RJN0_U8yYBVOh83iVQXtsLjgH1dvsk_cK1J5u_gZX4grzz3zvgVXLyDkgLZK055OT_UaxT5RdNmz6ElqqeiLrqX7gC-1FP9eHSImc30fV4e9Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748789f2e4.mp4?token=LOt-lQdyy27hYVcnLRE2Fh4WYssb77xrwdZKuKG0Wq4w0js5SpyvMBIMTd1lwfIMph66Z2-8tId1Uo2pN7ie-svCDGK0nVXsPFH7qsJitWwXhEc0jq1lpW0UVFBRg5lkdPG9mXO7qsp3cHTDd2sGm7OnFkiQrO4wI-WOOWIDPiYofAIUeGXpN-YZ-G7E1zkx2kOFFIZAM73o4MA41ksvep4eiKfvNf-_t_YoaqC0RJN0_U8yYBVOh83iVQXtsLjgH1dvsk_cK1J5u_gZX4grzz3zvgVXLyDkgLZK055OT_UaxT5RdNmz6ElqqeiLrqX7gC-1FP9eHSImc30fV4e9Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اسرائیلی‌ها بسیار واضح گفته‌اند که قصد سرزمینی در جنوب لبنان ندارند
🔹
دلیل اینکه احساس می‌کنند باید آنجا باشند این است که نگران مبارزان حزب‌الله در جنوب لبنان هستند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662264" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQWHCZ9fixE44rNIRaRpyCMwimU-zHnQAapbupg9Fiw9KjhHnwvl2UMpei4uIWy6-oUa4tJOyDnT582sywyWUhkMlBZdscvSY4G8t1LRIriH9xB7gHfcYTk2c1AYlJ77hPMwuaqRxuXLVTIGZOJW_-P0LlLi3GsAoq7_xeuyG8DYmMBHkNw2rCG2Mw2pRFsDiXos_txSGH3WgCurYquVElE_gfVxEM3FM_klktY9Vdcoq8MsTgeLtqYMI7YnrS0E88a-NsL4id0-EK3epB3UmHdjPBxLA6zEdf8c-9Tm6wrXyUpxcU3pMcUf3o2_iFVCXa-K0ib15nodFXQc2XEJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e49c6c7a.mp4?token=D_uNkUg_hGOSx_f7BHrLpjPE1pdcmiyBxDglSfvpUu6Bmb5afqxAJ1EClLM8rIx-eRs_AzoK1JLsELqNL9Z7YOiKEynNALha1qzT8xVVL0-OWVmnCt765DxXeJ45Ri_SKaeBR6XLT5Fs2JCN7J7sxFWNAHpUH9snbBeAeC0whvklGDELkzch9ChwTG6So2clKpogfmq2yOq6AGUuiCgE1IxuGPsUXsEcTc9vwGWt_d1wCRHUY11kbYiVm7Yrrgq_Y8gCIkb-5KHRoE7PY-O6CGg1nAQWoGmZVMv2JjRIu8UipOhizc-w-17tCtJaZ_wTYVO0hfFL_tfgSn857vn1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e49c6c7a.mp4?token=D_uNkUg_hGOSx_f7BHrLpjPE1pdcmiyBxDglSfvpUu6Bmb5afqxAJ1EClLM8rIx-eRs_AzoK1JLsELqNL9Z7YOiKEynNALha1qzT8xVVL0-OWVmnCt765DxXeJ45Ri_SKaeBR6XLT5Fs2JCN7J7sxFWNAHpUH9snbBeAeC0whvklGDELkzch9ChwTG6So2clKpogfmq2yOq6AGUuiCgE1IxuGPsUXsEcTc9vwGWt_d1wCRHUY11kbYiVm7Yrrgq_Y8gCIkb-5KHRoE7PY-O6CGg1nAQWoGmZVMv2JjRIu8UipOhizc-w-17tCtJaZ_wTYVO0hfFL_tfgSn857vn1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستاره سریال مشهور بریکینگ بد مسلمان شد
🔹
خیلی‌ها او را با چهره سرد و مرموز «گاس فرینگ» که امپراتوری مخفی مواد را می‌گرداند، می‌شناختند؛ اما امروز نام جیانکارلو اسپوزیتو به خاطر خبری متفاوت بر سر زبان‌هاست: ادعای اسلام آوردن او در عربستان، جنجال‌های بسیاری برانگیخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662262" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662261">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba4494eb9.mp4?token=WkeomS2EprdaBk3lLujvRX0wCceSXRHCFhYbhqeWNvs2te1T6vZXOBuZ9yJyGDl-q7czbtTYYlw8AgegKKF-xnKIAJnb8bPezBzQfK269aXLywMouZTNPVC1aC3-qRRt5AN4F1gwHKYdyX_Nq4rFzhTNTxsdznv1RVPXrmePUAgpivbdGRz7K_kNsTxYz-VjVlTIVBeo3PzI8XNEAyb3ORy65LxyO7ds9DWb01mu79gcpZCxVIPEf_ImUQrOEN-KRNKPbdBzQ5s2X3jGa6uoW1dcRdY4oYFMzPaUlsXKEqsIFzfPeemtA_RwSGca7gelrfpUAZy4qeWTGkFGzeNNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba4494eb9.mp4?token=WkeomS2EprdaBk3lLujvRX0wCceSXRHCFhYbhqeWNvs2te1T6vZXOBuZ9yJyGDl-q7czbtTYYlw8AgegKKF-xnKIAJnb8bPezBzQfK269aXLywMouZTNPVC1aC3-qRRt5AN4F1gwHKYdyX_Nq4rFzhTNTxsdznv1RVPXrmePUAgpivbdGRz7K_kNsTxYz-VjVlTIVBeo3PzI8XNEAyb3ORy65LxyO7ds9DWb01mu79gcpZCxVIPEf_ImUQrOEN-KRNKPbdBzQ5s2X3jGa6uoW1dcRdY4oYFMzPaUlsXKEqsIFzfPeemtA_RwSGca7gelrfpUAZy4qeWTGkFGzeNNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هموطن همیشه همراه! میدانی و میدانم ...
صنعت برق، تمام قد و با تمام توان، شبانه‌روز پای کار ایستاده تا شبکه پایدار بماند.
🤗
با همین یک اقدام ساده، قرار دادن درجه کولر گازی روی ۲۵ درجه، سهم خود را در پایداری جریان برق ادا کنیم.
«همیار ما باشید "
ba25.ir
"»
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662261" target="_blank">📅 15:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=YCbkqhxXuZoM0dPZsVss2FOa5sieZT9DAWMM_aqVqubp05MHNkH9bsv_BlFfu9reJk4d78oKH-YZPb7leAp-4ufTnhlF5dtun8Po2BI3c2KPPRkgPdx5TEusCoR-RJY6V35nm_UPH6eLIwfMt5HIjfqJGQafEjcYBA2JzQuKqm7Kevx2InpXI-RMqFSTDZ6nsScXdx7NbnM37zOnbcwe-H9tEq5QxnqM_c0WB8ep4p6j3lEzcYMqWIv07vJuwcEjx5RswOm9FI_nh5V0K3-IRFfHgmFc37swdiGO4od--xhd3FDyCMCHVIaRbtpm0SzE215PUNu825RjiSBhS8mWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=YCbkqhxXuZoM0dPZsVss2FOa5sieZT9DAWMM_aqVqubp05MHNkH9bsv_BlFfu9reJk4d78oKH-YZPb7leAp-4ufTnhlF5dtun8Po2BI3c2KPPRkgPdx5TEusCoR-RJY6V35nm_UPH6eLIwfMt5HIjfqJGQafEjcYBA2JzQuKqm7Kevx2InpXI-RMqFSTDZ6nsScXdx7NbnM37zOnbcwe-H9tEq5QxnqM_c0WB8ep4p6j3lEzcYMqWIv07vJuwcEjx5RswOm9FI_nh5V0K3-IRFfHgmFc37swdiGO4od--xhd3FDyCMCHVIaRbtpm0SzE215PUNu825RjiSBhS8mWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اسرائیلی‌ها بسیار واضح گفته‌اند که قصد سرزمینی در جنوب لبنان ندارند
🔹
دلیل اینکه احساس می‌کنند باید آنجا باشند این است که نگران مبارزان حزب‌الله در جنوب لبنان هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662260" target="_blank">📅 14:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662259">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
همتی: پیشرفت در آزادسازی منابع و معافیت نفتی  رئیس کل بانک مرکزی:
🔹
مذاکرات سوئیس با وجود پیچیدگی‌ها مطابق اهداف هیئت ایرانی پیش رفت و یادداشت‌های لازم برای آزادسازی تدریجی منابع مسدودشده ایران امضا شده است.
🔹
به گفته همتی، همچنین قرار است بر اساس تفاهم ایران…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662259" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=rH72tvZZo9ZpdhnZ7qtbYhDXmWmHiYkvYOroLQNqis3Vmv5FWu4GOn_nBJMhYYruTkhts8s7EuHYkl5UUuUI_77OOAYUqWd9IqZGeB7MnibaYI_IMjs030IzrCXlRRpxB-5qFZEQiz-XTPSv3vrYaz4b8LPdpn8yrpmTI8ONtuyme59iRJuTQ_kMXygLnJk9UUgl_qR8YHyv_NTQvpNpX56e0aOVnoSMXk7xvqcWq5s5JXqe1fK4V5bHBvKf01vh88TN161ZOLQbKbyHAPuMIzyJcB5LbWAY8xFdz1gVIR_GE4CQp8A9qY_iGWS9C0R2Rk908qT01yCRwNBf52NCQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=rH72tvZZo9ZpdhnZ7qtbYhDXmWmHiYkvYOroLQNqis3Vmv5FWu4GOn_nBJMhYYruTkhts8s7EuHYkl5UUuUI_77OOAYUqWd9IqZGeB7MnibaYI_IMjs030IzrCXlRRpxB-5qFZEQiz-XTPSv3vrYaz4b8LPdpn8yrpmTI8ONtuyme59iRJuTQ_kMXygLnJk9UUgl_qR8YHyv_NTQvpNpX56e0aOVnoSMXk7xvqcWq5s5JXqe1fK4V5bHBvKf01vh88TN161ZOLQbKbyHAPuMIzyJcB5LbWAY8xFdz1gVIR_GE4CQp8A9qY_iGWS9C0R2Rk908qT01yCRwNBf52NCQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس:ایرانی‌ها تهدید کردند که جلسه را ترک خواهند کرد، یا حداقل در شبکه‌های اجتماعی تهدیداتی مبنی بر ترک جلسه مطرح شد؛ اما آن‌ها جلسه را ترک نکردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/662258" target="_blank">📅 14:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae95a0257.mp4?token=TUjBRUDKM9eifwxUXl5n0KCdSsGwHdSZICAoc9xPZlwm8F3mTy85b9S_I2hqt8HTfjb1AfSMNyGy3RgGruVbKnmzTNc3ogcIzXXBzLcS6O5eM1T3ORCi-PNDCC7LCDBF0AvVRlsZ_xq5OfMBTJw2rVh1F-MTBSPmoSFrM7_LETvJY8BICXrvFaJFXy7jyxswTqu0WrlNOHSCPO7Qb4t3yfQc7YZ9nnoQDAMrKS22g1x4g1a4H0vn0-jYHfLRd4ZodIHrQVLjXZqxak4PH_RGLQv8O27Y6Moe-sVknMk-lTs1vZsL6XmIS7Yyz9cQPsmUnRnoaBqQKouEyA4wLlUPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae95a0257.mp4?token=TUjBRUDKM9eifwxUXl5n0KCdSsGwHdSZICAoc9xPZlwm8F3mTy85b9S_I2hqt8HTfjb1AfSMNyGy3RgGruVbKnmzTNc3ogcIzXXBzLcS6O5eM1T3ORCi-PNDCC7LCDBF0AvVRlsZ_xq5OfMBTJw2rVh1F-MTBSPmoSFrM7_LETvJY8BICXrvFaJFXy7jyxswTqu0WrlNOHSCPO7Qb4t3yfQc7YZ9nnoQDAMrKS22g1x4g1a4H0vn0-jYHfLRd4ZodIHrQVLjXZqxak4PH_RGLQv8O27Y6Moe-sVknMk-lTs1vZsL6XmIS7Yyz9cQPsmUnRnoaBqQKouEyA4wLlUPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره به کشورشان دعوت کنند
🔹
معامله نهایی خانه است. ما پایه را گذاشتیم. هنوز خانه را نساخته‌ایم، اما پایه‌ای موفقیت‌آمیز بنا کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/662257" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bd59db4e.mp4?token=XTfb4SXG_Y5QTEubwpFo_xyJqFNmFmZxPx-ixIIHWdDsZ29a6hyeNa0LHHYUgsuZn9hSg4y8S_C7Rx_4Af2yI6kSKSdg0Zp333tPW1Yjf0lu5CI3zD3z1MZlPz6QKou3oRR0r0LJph_SshKBNPVw2gq72GBxSaGSS1fQuxjVN9dTFsuDcomDHtaGBzxFYnPh5HaUscr_gMilQF7dGPFK32NCOOxoTCYrrgznYXyY_WSxZfVlLhc94agtio65zJDnv29FITfrMJAOMRSPuns2Rh4cw79TL31BcI--zlrLpRbCqvvg1X4bJCnsgSvzXFV8_QwbfogeZMcW3egIZR1W-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bd59db4e.mp4?token=XTfb4SXG_Y5QTEubwpFo_xyJqFNmFmZxPx-ixIIHWdDsZ29a6hyeNa0LHHYUgsuZn9hSg4y8S_C7Rx_4Af2yI6kSKSdg0Zp333tPW1Yjf0lu5CI3zD3z1MZlPz6QKou3oRR0r0LJph_SshKBNPVw2gq72GBxSaGSS1fQuxjVN9dTFsuDcomDHtaGBzxFYnPh5HaUscr_gMilQF7dGPFK32NCOOxoTCYrrgznYXyY_WSxZfVlLhc94agtio65zJDnv29FITfrMJAOMRSPuns2Rh4cw79TL31BcI--zlrLpRbCqvvg1X4bJCnsgSvzXFV8_QwbfogeZMcW3egIZR1W-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ما می‌خواستیم مکانیزمی برای باز نگه داشتن تنگه هرمز بسازیم، این تنگه باز است
🔹
ما می‌خواستیم مطمئن شویم که مکانیزمی را راه‌اندازی کنیم تا وقتی که تعارضاتی که ناگزیر پیش می‌آیند، بتوانیم آن‌ها را حل کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662256" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366085b82a.mp4?token=N_0YUoe2cqh_w3QqK5eHG_z_NPxCVWA-u182d2O2A98g206b_PSNQEtfdJdsdUJLST2PZXFSQ0Pavo1I8u0BP-zn1cgGVdRozcpeh-y2iA77IsJK3P4TMKYmc9rPKX402PaQDSsYUc_IZn_B8Sz35RxUOrRb3mBeA1xaj-I170MEkObSEnOnLqJRfgECz2QzY1w8FC35aSdgfOekYfp34NfiZJFzvSOSXSctN_ipTJlHob90XdhHCP3t6HuuJQ6wnria-ARiIqVitOpSEVbLONSQIgV1CNFtGp5ChAkGRQAAgkDjAeP0aRl8w-1SdJS0sKpCoeoRjIwQIxPYWkoIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366085b82a.mp4?token=N_0YUoe2cqh_w3QqK5eHG_z_NPxCVWA-u182d2O2A98g206b_PSNQEtfdJdsdUJLST2PZXFSQ0Pavo1I8u0BP-zn1cgGVdRozcpeh-y2iA77IsJK3P4TMKYmc9rPKX402PaQDSsYUc_IZn_B8Sz35RxUOrRb3mBeA1xaj-I170MEkObSEnOnLqJRfgECz2QzY1w8FC35aSdgfOekYfp34NfiZJFzvSOSXSctN_ipTJlHob90XdhHCP3t6HuuJQ6wnria-ARiIqVitOpSEVbLONSQIgV1CNFtGp5ChAkGRQAAgkDjAeP0aRl8w-1SdJS0sKpCoeoRjIwQIxPYWkoIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: دیروز روز بسیار بسیار خوبی بود
🔹
ما پیشرفت‌های زیادی داشتیم و دقیقا همان کاری را انجام دادیم که می‌خواستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662255" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662254">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اختلال ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662254" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اختلال ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662252" target="_blank">📅 14:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2j7AGSvG6kVjU0XeMb1WziCWQS93sh5T3DfRIFu8Sp2vSjhehcrAnEoc2FBLYBBSHMJYH2oImHsTgkqUF3_TamFYcV8CIrC-PUq4-cgqUqfSvHZicLwd0BIhB5Pdzj0XOsV9XOot7LEyUdXkst9UzX9JGnIcHFZkZZzWwdr55HSxPIzdCpNJwgWndmXnN942DpE1LRKF6L-07cxD4_m0Vf4QXiw3sMiu5TB1GhOOz5JJ5K7j_lQv5i02T-8d3FdK1QIabGRRk3F_VLpzYDM3jmQv3RyQetY_Cmlybq6QCO1EAF5va7EPC_gTQweRpFzCbFDHF196gqoTKjMjXEQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به نقل از رادیو مونت کارلو، بازی عراق و فرانسه که قرار است امشب برگزار شود پیش بینی می شود با تاخیر حدود ۳ ساعته آغاز شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662251" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riVk2GjVvCbCw0wz9uy3xYSGoF3LBQProEI9WoYA_OawrVD6Zo2AnvqmsNY2d13NyorPIN4ekQkF68UeYvFmhpFYa_IzyzrbpmD2U2xanwb0qTQisIy2gwwWUQAJH1y4Nz_VawlA_pNaoz530_ud3zdMTipQ5mad4FZBVAvIKQs8QOnNY9ceL9wWgzlyHNW56-3u19Yq_Z3yyldt48Z7l2MrKHtzZvCYhoKAQX0E8tDbJ6zOFXluYi4LmyaQ3XzUWFPRe_JuZmsHqNIj8QoitKY2WJ78cQm0Eq-T_UI_ABqBJAlBepJdxJHEVNL7rkYh_oBnAYx4zYiXcOXEtfi0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایتی کوتاه از وقایع روز هفتم کربلا
#به_وقت_حسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662249" target="_blank">📅 14:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF9NGdW0DaatWjALrxTjxyONSQX44VCa79lHyEUPt_qnWobXBcJXfGqdlJfnaqkdhzGykATAuQXm2zUW8XLySelOeeqaKq30BEYDfXyvpH_tjHOmYb8I_qzzdvO390YF6alsKyme10A5OFX7H4SYY54C_Y_0YFglxtcJBcp2OqHqO2tS4mrBahPsJ4eUoeOO3mXby5QuoCMM1rDvdBJMVwGuWkF7HRq3Gakc_rCq2hsDN-1eQN2oDMeA8__5Jrtn92wqxRmp42ccm3hE2vR9TtSs70hzBNvmn0iWLzDaTFpnmqEIhf9_KzfVJCH2waifiDfIb3MEziLpJsG2l8a4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضاییان و عزت‌اللهی در جمع بهترین‌های دیدار ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662248" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtf6dMS2x6C6OhnZ8_6pvcMSQJksBD2eqM44Zwtp78ynOhkj7AHdAHFzcr8vD2jv-6FFSm0m0PBwU5VOD7tN3XctJmoNf-aK7q4qXE7pHuyyXZoi7zlEd9phxHvLXTK39r27YIrgbjkSTzYVOUKVVlZFavcNjWsPKhy5iz-V0672F3j-eVCL1bmiSZGz9xl5l86_EnKvjCNxrJ8arMRbrAbeQ8Etp7MUJ2dkgaW6EAvmhjh-rMZ6zXzXaIXksL6slQRZUxMHt5UJ_LGriv3uZLzmZRnIwaHHqjwm2L7Z2hIp4jml5ZXqtBwTyWBfLye-pIr-fBEQS1VTGMuh_d13JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان یک فصل سیاسی؛ کی‌یر استارمر چرا استعفا داد؟ | رقابت برای تصاحب قدرت آغاز شد؛ جانشین او کیست؟
🔹
در تحول مهمی در سیاست بریتانیا، کی‌یر استارمر اعلام کرد که از رهبری حزب کارگر کناره‌گیری خواهد کرد و تصمیم حزب درباره آینده رهبری را «با روی گشاده و احترام» پذیرفته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224943</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662247" target="_blank">📅 14:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سفر پزشکیان به پاکستان تایید شد/ رئیس‌جمهور فردا در سفری یک‌روزه به اسلام‌آباد می‌رود؛ توسعه روابط اقتصادی و پیگیری مصوبات گذشته از محورهای این سفر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662246" target="_blank">📅 14:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb9NFqEE9vgBZKbnEhUZ-H2esbjKFMOJp9Ep6m-uHRk9ZSI-NuLSHvzhCgPvP3PxZkWdCRXtFqpLStUUMq9iVuc31gNzk6EjBhsAlpkbG9QS6D65S6pIKqGPM-h7zdP-Kwb41us9ejxoZmcBpP7cCGyYd4RmUHXPVh3ihtV44HrZVXXMb7PY8AOqg5QPEM_Zm6RKbN8swbB_o4mAkWgW3VWkzEoE3DN14P8iQRO3whymm7Nq4gy4dgZMr3qNwakOgZCN-KpHuK1ZVz-yJL6YyUE8aRoBOZyy5LXbuelkBWpdE2XBTtUxKoBO3IXUjraovxS-WBANsw3QX15SsmNLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پتروشیمی امیرکبیر برای نخستین بار تندیس تعالی صنعت پتروشیمی را کسب کرد
🔹
شرکت پتروشیمی امیرکبیر موفق شد در دوازدهمین دوره جایزه تعالی صنعت پتروشیمی، برای نخستین بار تندیس بلورین این رویداد معتبر را کسب کند.
🔹
این دستاورد در شرایطی حاصل شده است که پتروشیمی امیرکبیر طی سال‌های اخیر با تمرکز بر توسعه سرمایه انسانی، بهبود فرآیندهای عملیاتی، افزایش بهره‌وری، ارتقای کیفیت محصولات و تقویت نظام‌های مدیریتی، برنامه‌ای منسجم برای دستیابی به سطوح بالاتر تعالی سازمانی را دنبال کرده است.
🔹
علی حیاتی مدیرعامل شرکت ضمن قدردانی از تلاش‌های مستمر کارکنان، متخصصان و مدیران مجموعه بویژه کمیته‌های تعالی، این موفقیت را حاصل همدلی، تعهد، تخصص و روحیه تحول‌گرای خانواده بزرگ پتروشیمی امیرکبیر دانست و بر استمرار مسیر بهبود و توسعه تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662245" target="_blank">📅 14:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85463a0a3.mp4?token=pn1h2abpHeoX4Y5jJ-FyFBwrEnpwdxpCFcW_m7U-Og976VQhlKrPlWKRUwRGkS4mRUgC26OIZ5QbMCQ0LvItQZEf2o2Y1rhj2FmtavHTloRvwt_sAdV2oGEqIwH_IAvnqiNsRGSxjOaS69e3a2ch2AfbeLJXVqipqxvUZmnnx7hANqY2Jof497dz_pzlblmD3PXsbP3x9dhj-KsGrnMLE1JjnWLgtvuJ7rw9WndXi9t4N_I9lPrYeK3CzPt0VaaNwgCYkZIloxQP3K2zD747njMjIxVatmhI3cGbYgCMVmc03vU9zly8ersKlUnEsxMFcPIzkXH0947umqFVW0py6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85463a0a3.mp4?token=pn1h2abpHeoX4Y5jJ-FyFBwrEnpwdxpCFcW_m7U-Og976VQhlKrPlWKRUwRGkS4mRUgC26OIZ5QbMCQ0LvItQZEf2o2Y1rhj2FmtavHTloRvwt_sAdV2oGEqIwH_IAvnqiNsRGSxjOaS69e3a2ch2AfbeLJXVqipqxvUZmnnx7hANqY2Jof497dz_pzlblmD3PXsbP3x9dhj-KsGrnMLE1JjnWLgtvuJ7rw9WndXi9t4N_I9lPrYeK3CzPt0VaaNwgCYkZIloxQP3K2zD747njMjIxVatmhI3cGbYgCMVmc03vU9zly8ersKlUnEsxMFcPIzkXH0947umqFVW0py6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تلخ برای سعودی‌ها؛ واکنش هوادار عربستانی پس از گل چهارم اسپانیا که در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662243" target="_blank">📅 14:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQlWXipMb0f6JBD1x8JQYYfRC8dMI_kRvrrN3lHUq4nkan_bYKq2sKGDCsIeCLyAD_ZEzUdlwCtAl9mZJUnf7t4vozL7M4kdrTv8c02Ybw8_IcnMgi2zbWFrOyDk_SyStHZqwS2-Inow3AdYkPIf6KnqLBN4C7i1Y-tnd3IG5CP_gEWuGvsR0mQ0NxsgwGczsLj1_2pfrYF7ttTdt0zrp7QXpDT_LXxNb0eG_XCkh4I9acKIMemLmIEFeVpVtSy3vsOt8W_k-EXA7nM8UIqlU7Db0C3eZDSxerwbaaI31VKfzlTF5vof_-s_XtQ1e1gOkpaZn9i-kHlSQUB1n9cXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن تنابنده با انتشار تصویری از بچه‌های تیم ملی نوشت: دفاع به خشت جان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662242" target="_blank">📅 14:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662238">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhoN23XIgdVnB3eWDr65A1b4CE6doDqLkRHIBJnLMHiyYE6oK9rv5MO88nWO_8r4x_o-9Pcal7qw5GCMpp8hQURG-i0w7CPLXtp1whVovYhmxshjUOi5FI67GFvxzTN_7kTlq7N_OwRb62TUlivARYtYa7fOQk0e_nOiIjBjRd4JxwvaZvZnpEWPWw4j18pRmFBggPi7Q1X4I8D_jRBiRGNsR5Kcf9eINElXSbKYiOTu4m25Edn0S3xZv4P68RgQh8fZoM4KJIzuigVM2yQi82dcsPXE7YK_GZSlpEj7dLE1wCYrhBTulud8JCpW8_RwJ9P_Hy2vsvJ_dYAKVF-ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pu3HPKhIhHKkr2PFoOkilUP5maq1lHARKxCU6gJauT7ZbG5kscStJqCBUJ0jafKLxqdG2sFytmbo87cu0DJlQvrzj1R0NyF7ubiUmZpMR3Y0kt7dcbZ1MY0kl91yFbQ23fM6Lk6fmzDSrEXnekTMvKkj63t0WiaIHDHMq5E0wxE9brbPGhbkH28BQ3ffC2N5OUslf5bPxV8ijLN6CKF02X_JLkwijEjVaRkkqaUqnWYHWxj653pLMUCVg7tgvRmkEEKkKTgr6vRNVAtsG44wKK7maqCWZTzEw-Ftp85KLGo5dgJdghG2hF7Jjh3yEqnWuGnHHwigF2HUsARRIRj0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT9hG4qWZX2NLQbFaI6Ew69szEOskfMhr4CN5JXv5Bd8f9l9couOZezA5dWHi29Wx4GD5NHi618QnQ3CGkyOIkIOnF4AUGCSxN6Ggt0q4bQfHspQ1VTlmr4hAlKrMvYQfSq54YxC16LUuVJv0shZkG_Xlw3_mvhJBHu5_MTWWhXbLK7dTdw-KdbcLpA7AVmtz3HXd5fUtibWjASeFAxESaLCl-AgIWgBmt5wVVZ_Nj1MqJrrNUJsrbG487JwC4nrcCewD7AEE1czAb1mFgKj49HCTZ1Q6fNlswqEHUuFaazZq5OZstMtGc8K1z6Z-RAoodvAuAWlMuGE6Ox7KOfwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wgec08ApYSDIlCn5RQVsMBYbrAFBCbz9wPkeu_TBmOlTnGqTLnHm7L7G_pMQdvR4vNanAIzKcqcQ0g3jOQH61XxbdCRN8lXPITA2z-S3peO6CADpL3mQhP2G8cWkyNwXnpMdqYb9OQz5MnVjQx9XKioZ2s9UzjmpBQa3-xidj0TNIDr38LvGHy7j647f0zrYQEEvxUItI8eoxVAeW_QbwpDR-7r9yUwrkFeW4wJ7qYA6VlLX-ePUXYYZ0q7VQjIIpNAtmR1I1LwiXe5M3ZsdD13hhoJo-BC7YN9xQj6PVAARrh-yiYYHmo2Cr24lKtt4uXxM5UqZ88eQWxL9rtju_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کویر و کوه‌های ایران
#ایران_زیبا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662238" target="_blank">📅 14:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8751d8a85.mp4?token=kERZTVJL3b2BjiQIqp8x9W6tZDVYFfWz-P7Vu60Poee5DxAJYx2cQCx0MR2cJ3dbks7Gt8WhC-dMqik3Lum-e1cQMdp4ff9T22cJ-vRlrm1kW3VliHvq2xhDUxgghNyjV-Jju-iFqluvC0BgEJUuoUg3hWqyPYdGDKfWC5Te652BV2iY2EDNdAKo-WaHcIuWG6mCz32XfVBlWhSqKq7MBv-j4zczHTudjALNP1ixkvlEnZWQDwuRhQLLJcbEUPJNOzd9-tYzesX3ErgpdqbFp7-b6w2BZ4fGTMO6CIGSWbuCbgrBgD419HtBiTi_IzkZFVdk12UuWKVztaZ6FQ1IGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8751d8a85.mp4?token=kERZTVJL3b2BjiQIqp8x9W6tZDVYFfWz-P7Vu60Poee5DxAJYx2cQCx0MR2cJ3dbks7Gt8WhC-dMqik3Lum-e1cQMdp4ff9T22cJ-vRlrm1kW3VliHvq2xhDUxgghNyjV-Jju-iFqluvC0BgEJUuoUg3hWqyPYdGDKfWC5Te652BV2iY2EDNdAKo-WaHcIuWG6mCz32XfVBlWhSqKq7MBv-j4zczHTudjALNP1ixkvlEnZWQDwuRhQLLJcbEUPJNOzd9-tYzesX3ErgpdqbFp7-b6w2BZ4fGTMO6CIGSWbuCbgrBgD419HtBiTi_IzkZFVdk12UuWKVztaZ6FQ1IGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استوری نوید محمدزاده برای بچه‌های تیم ملی
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662237" target="_blank">📅 14:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGjoqlSgr-IrZLmTuMprq4RKffJZdlecRJLK46wUCxLz6f5efxEi3mmm7WXsOc-uJNjfGCvsgihll35R22I_Y7-diU7FBTsNi8Lzlh_gy0JUioJQbSmBZc9k-19v4xeBZc5otoi7Bi2RNChlVGSz689Yq9iyT0aexvMpSy3sIf3zhxc3tEiqeqDt8VWS4Y4hHVrluicFTq4F4mi4DHGbgMewAz0ZrMM3vJsgz-GE20jNlEv0JvyHcRN0I-hiIQ1HzwP5smXbmuxOsuConKRVWanE00-4sx1BNwMomNwbCDqBHg3oabMed77GywKjngOmBJPMQMpbixeoqhZnGUcuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با کیف ۵۰۰ میلیونی در لس‌آنجلس
🔹
رامین رضاییان، ستاره تیم ملی در بازی اول با یک کیف لاکچری و گران‌قیمت وارد ورزشگاه شده که مورد توجه قرار گرفته است.
🔹
کیف رامین رضاییان از برند Christian Louboutin است که ۱۱۲۰۰ درهم قیمت دارد که به پول ایران نزدیک به ۵۰۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662235" target="_blank">📅 14:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTf6_0FSKzh7_-AFE9Ju1PCEcTXLw_BotPQbQVI7jDccV84dcmXrzknpfAWy5cDIKR5mKbHSqE0eiPLJGNOn1wpCv02V2h4yNwvSkY6zIMcDxOjz50AoJyXNJYusd84nFhRGEqHeScUMvaaMkESlpDaUl-gxanZXT_CxIwTyUHQ9CLQR98_C_pL49P4QZvF6sF3lR4CmEfwwAc5YkvzHUHELKyNTDxkwAp1YnzxojbmV9yWaWgHcweMNqhjiqLzpOglZh9fvQTbGpbHjLbGxulu0PK3U-XTUOzSDdAewyyL0FeYq-X1GpEtMQKwui2EHdv092dcslCqRNpouLUOFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امتحان نیست، ولی بد نیست معنی کلمه «اظهارنامه» رو بلد باشی
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662234" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه: براساس آمار پزشکی قانونی، در جنگ تحمیلی اخیر، ۳۵۱۹ نفر به شهادت رسیده‌اند که از این تعداد ۳۰۰۲ نفر مرد و ۵۱۷ نفر زن هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662233" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
