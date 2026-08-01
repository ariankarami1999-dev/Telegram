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
<img src="https://cdn4.telesco.pe/file/SO-jp_AnMUkUBJiEIUtyrPBL3SICCV6L8EjpuJG5g9JpdV0paAhdXoek4AS8c8VUIZsY-lli-xqShMGmJK8o6JAbRi5IVn_rKW-vYeHLJe9qETyDVqEBI6ppUq2mO3KE1v2_R2CKn85b3xH6t-LsTHrP9bxpe4LlrN3GTExkZGE7iqOzk_eNbxEgeNmY5OLsldXOd3VjVG_sklmCLEeVtQp3hs6MFAIiPv_sssfavcUVZ-0D868d5Yek5wQAsimK5JzlB0WoK-O4ihd2NuQ93Zz1R7Xa9SymPcPu9x1QRAF5Dc5WdCzFDYRfmq7_X0vnhlrZWUZQDZGRy_HmqmcXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.09M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 23:36:25</div>
<hr>

<div class="tg-post" id="msg-677514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
یک مقام آمریکایی به خبرگزاری آکسیوس گفت که ایران در روزهای اخیر بسیار تهاجمی عمل کرده است و برخی از مقامات آمریکایی از میزان آمادگی تهران برای تشدید جنگ شگفت‌زده شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/677514" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شنیدن صدای هواپیماهای بدون سرنشین در آسمان سلیمانیه در شمال عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/677513" target="_blank">📅 23:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی دولت به تامین اجتماعی ۱۲۰۰ همت شد
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دولت حدود ۱۲۰۰ همت به سازمان تامین اجتماعی بدهکار است. در بودجه ۱۴۰۵، پرداخت ۲۷۵ همت از این بدهی در قالب اوراق پیش‌بینی شده که دولت تاکنون آن را پرداخت نکرده است.
🔹
بهانه‌ای برای عدم پرداخت بیمه بیکاری وجود ندارد و سازمان تامین اجتماعی باید از هر طریق ممکن و از طریق خط اعتباری دولت و بانک مرکزی، بیمه بیکاری را پرداخت کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677512" target="_blank">📅 23:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تماس تلفنی عراقچی با فرمانده ارتش پاکستان و وزیر خارجه ترکیه
🔹
عراقچی در تماس های تلفنی جداگانه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان و هاکان فیدان وزیر امور خارجه ترکیه، ضمن بررسی آخرین تحولات منطقه‌ای، درباره پیامدهای اقدامات تجاوزکارانه و بی‌ثبات‌کننده ایالات متحده آمریکا و خطر تشدید تنش‌ها و ناامنی در منطقه گفت‌وگو و تبادل نظر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/677511" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب شدید در هند
🔹
بارش شدید باران امروز در شهر ایدار، واقع در منطقه سابارکانتا در ایالت گجرات هند، موجب جاری شدن سیلابی قدرتمند شد و خسارت‌های فراوانی به اموال مردم وارد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/677510" target="_blank">📅 23:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در جنوب لبنان
🔹
منابع خبری گزارش دادند این انفجار در «شهرک کونین» رخ داده است، و هنوز علت این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/677509" target="_blank">📅 23:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: یکی از استراتژی‌های آمریکایی‌ها این است که ما را تا آبان یا به مذاکره، یا این واسطه و آن واسطه، یا به حملات محدود و غیرمحدود، مشغول کنند تا به آنجا برسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/677508" target="_blank">📅 23:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6WRgsqtZPsopiQ5I99oQGkrZzgx5zNOxjw4vp4o9dKRACk3bRcDjUxyhHgGwIVBXWpfh1moMtMifhxi1oK_xR5mBv9jaOek4lrb0H9MiooSp0O02qwXBPdNWvLRREZtVj0cHHm3IdTgtlpazGKUcvTXTztLn3qFbNgmDUepmwHphw3I645RBfx2-w7SVsTKgkNmHYJBpef3AS42uTkBLa7JzI6HMAeai3vR8uUogf1rk7FcBjE686PwJQPS7qi4N-RcBw7noK2YG2cOXKVmuOR3JyyDpjF5JBIUTm8fBGOqIhU1VSQn1ZYIUFEHMtumcQSxzDSkhcYLeTgydtq7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8A4zgwoNy2KHtAvgh89UedTvRRuZtH6AifW5-reGXoevI2bGJJImeO8aAhG1xYvOUvnbtIN-rdkOoxLJbUWaC9ddv6Lq9Ni998kQ-tPAa3Dp4dOxoKbbSwrrhxoWZ2n1WhulepzweYBxMJv3vKet24GgO1QwhdMNm7IGT0Gcx3VYVaPxS_EpvKa5bZ0t4XJbm5XQg1FYrcmi4D-Z4s6ejyLwlNAqHLUuGfbsIFxiij8KGZcG31zIRJRHYmd8DReLWpqVjRQC3b2my0BMVZaT4UhDH9lTfyYuL5NQtLY-scT3gYiqRJ1RAeC1Q2g0SFPQNAvXxm17cQQjh7jBi6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgcfB7_ImMl-c8kHd2pO4eXNLsfLGTRaXqBDrYpzwMrcC851aAFpoKVdKG8PBtCIxpAPb4faO1wIWRkTM-ELWXxvDUz2v1OSRNFXQ4PHnAQSTVqGEe7i14TBNrpIMHHyB_GXIZF97z2ZMhgoDRLXrbti_bpgLQPQZfhYtSask8AD2i24mXcq5pV2TaiaHwKBI9pJKlYSje8myO4cJtsib8QHyau-PjQ8Py4tt0O8SUJ32bGXAWuD_dGW-C2AVd9VSMYX3XQ79z5lmQlbgPG0yR4DNRFHCubGEhHnyUkWWNxmJBxGoVmcWkni1P2pj401bL562sP_rOdFMLUjEExFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFeNnqT-fPBtX_i22H0_EQ_-DxQWmMk02AFRERNaDQs8-pR3FvYhw81rF5IX5dx3_PsrfkY2jQkZJVNEvf4kVgCaM80EHMe-rpMLT4CKlUsIeLvNlyzM0nSJcbKwOaYjdARoxQ7_Ux6x_5ZIgKM8jxnTGQtHnjZOGKOfpmOsySoGqt5BP1halfKtQENIzU471fBL4vWXJXGGf0p5bVEDlnh1g-6o_LZEfnVUo3MxUO_cODlUPPJwhqnQrC4VSzelwHVczaTTxJ7suX1UHKdvjy2Yy8XaQHy8wbyRiEL86n36slSceU9c7fI6c9Fpv4xg7y-MVljSwDD1A3KIvCpSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu8NSYiYfJgOj8M1meDaoHZRdoO6KgvgyAJI9XVW_GVhc_VmdZOsx6WqrW21zJE2lFkFbYIhuSSu3HEHvLWfY36cXhIikKRWQjDUERmlj_fvmwLf6Rymi1yADlPl2Omjehicw1AdIbqEYUjoiwekVuES8FEgshugjCYIQzE8JVWawX_fs_-kk_btO8IV71zchlFo5W6ff1Z6aF61ugpmSoHUfTaOkKfMS470fH1Q4vXlWmxOyBRUL40zR1UEk6wC9Jn_g9OASvVhoEHTZyQn02PplRpDlTDaFiEm1BzzsSobysrW__kNECc0q5C3gI6xWCH7aQYzlAYHrh6Zo8tz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONO9OikgMi3sPDugqT-BbyLOfZML-jhvc16RY_Uohy5BnyXtQzT8aVLfUF84aAchfZjQjSE7ZU8yGngOYh5MZLOlS1bjIpVpnekuPgoatAXr9XKzNGdAkhue8D0Trurp6hRssi2tZliXMwf8bYtY8uOCqRfLkHGkvAn6YCKMauBZr4ShHvDAdZg-8rNIVi26fZnURDGKzwkA6jEndxvkqhN2bs5LaKgPPhjJhb2_oAKhh5YNWN3zMfE1rHBbtu0eSHqHGLHfopkyh6q0jeV4uIaIiLmCryRKhVMO2N6R7RQfkcaJvNbkOFTs0lk5u23PHs1L4mEkWNaxpwDcv16taQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این آمار اسرائیل را نگران کرد
🔹
اسرائیل برای ترمیم وجهه خود دست به کار شد و ۵۰ میلیون دلار بودجه رسانه‌ای در نظر گرفت. چون داده‌ها در آمریکا روایتی ترسناک را برای آنها ترسیم می‌کند.
🔹
اما چه شد اسرائیل تا این حد نگران شده؟ در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/677502" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331b6210f7.mp4?token=px-rRlBLFz6fHj1y2EIAGp0Tq2ZiuW_jaSLLcUFdbuWvsXBNTMB91XHM9zuxEsnvj6HoT1frC9dI53irIuqKTdGlKxWf4_90NxEj8-z2qHZmn7xQLcnZtfNPSQTch4LTYHaDqNSFxgXM1u4Y2o0WO3Dmix4fPWi4fyPgh1EEH2dKwPvHg9LcORPcMvZJSgZMIAwoh9mDx7c1zBUFGeuYFuLxSPGBP7eiRpG2p1ab-AWVlEZ_9VK_NB2R5T4tGuBo3LEuo7NrGRWGpgOB3HgFVIz6bNOodunMR1MZzrYnayskSmFUv2YjpZgUKGjUTHQoPrdNc3VZKlug-W3fc7y5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331b6210f7.mp4?token=px-rRlBLFz6fHj1y2EIAGp0Tq2ZiuW_jaSLLcUFdbuWvsXBNTMB91XHM9zuxEsnvj6HoT1frC9dI53irIuqKTdGlKxWf4_90NxEj8-z2qHZmn7xQLcnZtfNPSQTch4LTYHaDqNSFxgXM1u4Y2o0WO3Dmix4fPWi4fyPgh1EEH2dKwPvHg9LcORPcMvZJSgZMIAwoh9mDx7c1zBUFGeuYFuLxSPGBP7eiRpG2p1ab-AWVlEZ_9VK_NB2R5T4tGuBo3LEuo7NrGRWGpgOB3HgFVIz6bNOodunMR1MZzrYnayskSmFUv2YjpZgUKGjUTHQoPrdNc3VZKlug-W3fc7y5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد عجیب محبوبیت این پست در اینستاگرام طی ۲۴ ساعت اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/677501" target="_blank">📅 23:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f55f6c3.mp4?token=mGwe9GrFAd_5pfQ0NHCxKbRQ9l5elNiRi3srezxaRYhqk8Nky4bu6QkD8OiRih61QfRQ_rtOOsH0SjORCj6o1_zqtnLa9NoVvt4pfBKBhMJRMsevTgojE2cM9o7wtYb1RQNRAIC1z150PetwVYRcOLhNaKPYXZmS0GTLT9_AD9vwYvuf368s_GgxrZ_x2UWroCyvgvXlNJDp3uGqmErQ9exzs6hm0V9n7Nh71xNKMGnhQjpX8YlCiN0y-TP6QfVcblxqyEhHJ8ct0DUZzr9NO_pGeGvCcWespuK7eY-wC5wC_qrc3ljJaQHiTKAuT18CvQarE0SA6z-tFuPGRF8BYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f55f6c3.mp4?token=mGwe9GrFAd_5pfQ0NHCxKbRQ9l5elNiRi3srezxaRYhqk8Nky4bu6QkD8OiRih61QfRQ_rtOOsH0SjORCj6o1_zqtnLa9NoVvt4pfBKBhMJRMsevTgojE2cM9o7wtYb1RQNRAIC1z150PetwVYRcOLhNaKPYXZmS0GTLT9_AD9vwYvuf368s_GgxrZ_x2UWroCyvgvXlNJDp3uGqmErQ9exzs6hm0V9n7Nh71xNKMGnhQjpX8YlCiN0y-TP6QfVcblxqyEhHJ8ct0DUZzr9NO_pGeGvCcWespuK7eY-wC5wC_qrc3ljJaQHiTKAuT18CvQarE0SA6z-tFuPGRF8BYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم سرخ یالثارات الحسین در طریق العلما به یاد آقای شهید و طلب انتقام در مشایه اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/677500" target="_blank">📅 23:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d35fedd0.mp4?token=rLcI9mNvAmyA012thl27BYSmaF6Ljz9DbC3k7n8P6a2z8h_mLXUocV-WUFv9oxiFYCGX6KsONVM3VaBe3TMyIYdhXx1GVqhfWLRJBToJSe8FpIvBNZ4xSA0AxlHnAZDdouOMHO9klJuAraoF8TBm41HL8tr2Nb5eaxDAbrpbIrmrSqa5VwkTCYNLh3exOuWuIEcZPudYnHhz8jJ2wGNtsEXbrtJqrIhEfYiNkMLCUMTkLIArE2KO64NSyv_O47X3gtKkSLrqUFTYZVkd9HICvjQTmMY8eLEefaeFNiDb_o860YXGGTc055JpjNfm2Wr6S1zjWgNbDmIhUHNyHJufcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d35fedd0.mp4?token=rLcI9mNvAmyA012thl27BYSmaF6Ljz9DbC3k7n8P6a2z8h_mLXUocV-WUFv9oxiFYCGX6KsONVM3VaBe3TMyIYdhXx1GVqhfWLRJBToJSe8FpIvBNZ4xSA0AxlHnAZDdouOMHO9klJuAraoF8TBm41HL8tr2Nb5eaxDAbrpbIrmrSqa5VwkTCYNLh3exOuWuIEcZPudYnHhz8jJ2wGNtsEXbrtJqrIhEfYiNkMLCUMTkLIArE2KO64NSyv_O47X3gtKkSLrqUFTYZVkd9HICvjQTmMY8eLEefaeFNiDb_o860YXGGTc055JpjNfm2Wr6S1zjWgNbDmIhUHNyHJufcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس عراقی: انتقال تسلیحات از سوریه به عراق توسط آمریکا و با هدف حمایت از گروه‌های تجزیه‌طلب در اقلیم کردستان عراق انجام گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677498" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بازنده و برنده بازارها بعد از جنگ؛ کدام بازار در معرض ریزش است؟
🔹
بررسی روند بازارها نشان می‌دهد مسکن، بورس و سپس دلار پس از جنگ بیشترین رشد را تجربه کرده‌اند. طلا به دلیل افت قیمت‌های جهانی از این رقابت عقب مانده است. مسکن اکنون بیشترین ریسک اصلاح قیمت را دارد، زیرا رشد آن از تورم پیشی گرفته است.
🔹
بورس با وجود جهش اخیر، هنوز از تورم عقب‌تر است و کمترین ریسک تعدیل انتظارات تورمی را دارد. همچنین دلار و طلا در بلندمدت تقریباً همگام با تورم حرکت کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/677497" target="_blank">📅 22:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c39243dd5.mp4?token=ZrVxzNj2b8UBKbModyJ9r88a_8YFdexzHfbbqKugaMFh6l7evkkv71VAWY5ziITbJTOayq7bsz1OIj6PwBsFFTYWMvVvDSVbjNF-keefL2QU7sJRHurm5EAnz8FErRw3Tma5A7XN3E2LEoVHKoWz30bNP6F6FlokWCa8fXsljwjZtJfsPsceh2XmfiM0Ho5zskXVeptjLBQGwLidggEXb2SkZRPpXCdshbao35pGJGDX8Dg7Fhgdh95uopJlOldmhVnXs7aDnpNjCEAZFMtnvtUCe5ri41RrTWgl2lVPDTtQ67NZMbgSxg0Iapus2eQO27O9kUv1ZrklPmVUTaRM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c39243dd5.mp4?token=ZrVxzNj2b8UBKbModyJ9r88a_8YFdexzHfbbqKugaMFh6l7evkkv71VAWY5ziITbJTOayq7bsz1OIj6PwBsFFTYWMvVvDSVbjNF-keefL2QU7sJRHurm5EAnz8FErRw3Tma5A7XN3E2LEoVHKoWz30bNP6F6FlokWCa8fXsljwjZtJfsPsceh2XmfiM0Ho5zskXVeptjLBQGwLidggEXb2SkZRPpXCdshbao35pGJGDX8Dg7Fhgdh95uopJlOldmhVnXs7aDnpNjCEAZFMtnvtUCe5ri41RrTWgl2lVPDTtQ67NZMbgSxg0Iapus2eQO27O9kUv1ZrklPmVUTaRM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفتگوی عربی رهبر شهید انقلاب با پسر شهید اسماعیل هنیه: بلِّغوا تعزيتي إلى جميعِ عائلته (تسلیت من را به همه خانواده ابلاغ کنید)...
🔹
پس از پایان اقامه نماز بر پیکر رهبر شجاع فلسطینی شهید اسماعیل هنیه در دانشگاه تهران. ۱۴۰۳/۵/۱۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/677496" target="_blank">📅 22:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54dc382f4d.mp4?token=RDUlkibWZx7HHTVIoevzyPUKM7uxoe_Z3ckPTnFFl0BVOxT_5oXpNFIZOOjSuIw2KsPJg_dbkDtUMnmIMVylAbxhIBi_NQgfxl1RfWXTkrlxs0m_iRrceUQL1gLmeFgtLt-mWrce6gBID_a7hM5nrYZaLqY09UtcM03g0RUwZ3mclF7tTpUw2g6QhKZw8eM4rlX0hvaQRqpEd9qFN5y-oA0A98QnjMK4-O_v-Ah9eS2cnfQTC22aJUkctSrcGgGhncwPcjEL8iSgqy_9jJ9KlcoWgfQ2w6aJ7lhu4sZaYucJoA9lstCHvLJVOKblg0QXxRxuck5QJEcj3FNwK_NVtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54dc382f4d.mp4?token=RDUlkibWZx7HHTVIoevzyPUKM7uxoe_Z3ckPTnFFl0BVOxT_5oXpNFIZOOjSuIw2KsPJg_dbkDtUMnmIMVylAbxhIBi_NQgfxl1RfWXTkrlxs0m_iRrceUQL1gLmeFgtLt-mWrce6gBID_a7hM5nrYZaLqY09UtcM03g0RUwZ3mclF7tTpUw2g6QhKZw8eM4rlX0hvaQRqpEd9qFN5y-oA0A98QnjMK4-O_v-Ah9eS2cnfQTC22aJUkctSrcGgGhncwPcjEL8iSgqy_9jJ9KlcoWgfQ2w6aJ7lhu4sZaYucJoA9lstCHvLJVOKblg0QXxRxuck5QJEcj3FNwK_NVtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز اجرای آزمایشی استفاده از کارت بانکی برای سوختگیری
معاون سیاست‌گذاری اقتصادی وزارت اقتصاد:
🔹
طرح انتقال یارانه سوخت به کارت بانکی، وارد مرحله اجرا شده و به تدریج در سراسر کشور گسترش می‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/677495" target="_blank">📅 22:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6ae2e69.mp4?token=X4_dhEhzn0LA0TGFhYdX1vso-zaWE5eYfcLq-49pL7LkqrugGbSx62m1lBHXZX6TdCWAIuls7NE40BkCSiv9hAl-dJ1OrhLcLLREn7d0KZXccPPGsbc_j5kbYPzYudIhwPhplQIl4NOcjrdnT3Vq8kdEPAXIzw294z0eWaoEN3dFhwqZS85fdwHb3O0QAavr_mMidNkJshUZPcLG4Sw6AmTV13jM4F6Mk_ViYyLbD2A3nJeHEUj9GN8TuybRl8Cy0hzxtbonipRGXVnQQgnfDJZNSlZfJLDMspL84F08hHtSSK1kobcp1X96_7nTJuY1G4op-nUWd3cJhLLz6xS4Wxb6t4hbSc3LJv9DCelvtJ1I_K9HbMaiX7Kay7GwL96TzVD4-mstpkQS0B6SjbEwFFw5qlz8wAH-KmSSY3ZdOfCFSDUbNBruyIxDlflS4P79OI4FYL-NLezIKIXPqwNb5o3zfdOaLgSVgb4EcuK1_yUwrAKlE2NumHAr8E8M1ittu_XG15EwzNJkDWOPcgz97utS0qw-IdVzBXNzOfJNYKAqHIKU5fRppDfocNBZ-EVfNtvFATKUU6hS_N7XZeA0HMilGJvMYdy_pNzkP0Tva8TOu1Ho8-pMJcYiiDfDNFuQRJBfcsatJ5f-vBL58tnOBukTpXb-vl1zN2PzzAgXJr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6ae2e69.mp4?token=X4_dhEhzn0LA0TGFhYdX1vso-zaWE5eYfcLq-49pL7LkqrugGbSx62m1lBHXZX6TdCWAIuls7NE40BkCSiv9hAl-dJ1OrhLcLLREn7d0KZXccPPGsbc_j5kbYPzYudIhwPhplQIl4NOcjrdnT3Vq8kdEPAXIzw294z0eWaoEN3dFhwqZS85fdwHb3O0QAavr_mMidNkJshUZPcLG4Sw6AmTV13jM4F6Mk_ViYyLbD2A3nJeHEUj9GN8TuybRl8Cy0hzxtbonipRGXVnQQgnfDJZNSlZfJLDMspL84F08hHtSSK1kobcp1X96_7nTJuY1G4op-nUWd3cJhLLz6xS4Wxb6t4hbSc3LJv9DCelvtJ1I_K9HbMaiX7Kay7GwL96TzVD4-mstpkQS0B6SjbEwFFw5qlz8wAH-KmSSY3ZdOfCFSDUbNBruyIxDlflS4P79OI4FYL-NLezIKIXPqwNb5o3zfdOaLgSVgb4EcuK1_yUwrAKlE2NumHAr8E8M1ittu_XG15EwzNJkDWOPcgz97utS0qw-IdVzBXNzOfJNYKAqHIKU5fRppDfocNBZ-EVfNtvFATKUU6hS_N7XZeA0HMilGJvMYdy_pNzkP0Tva8TOu1Ho8-pMJcYiiDfDNFuQRJBfcsatJ5f-vBL58tnOBukTpXb-vl1zN2PzzAgXJr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: هیچ مذاکره‌ای تاکنون صورت نگرفته است، مگر اینکه اذن ولی در آن باشد
🔹
ما باید مذاکره با آمریکا را مشروط کنیم به اینکه ۴ گام عملی را بردارد، پیغام‌ها کارساز نیست و شبهه طرف مقابل را بیشتر می‌کند.
🔹
قطر باید خود را بدهکار حس کند.
🔹
آمریکا بدنبال ایجاد بازی‌ها متفاوت است تا ما مشغول آن شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/677494" target="_blank">📅 22:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حمله پهپادی به اطراف منطقه دوکان در سلیمانیه
یک منبع محلی:
🔹
دو فروند پهپاد اطراف روستای گیچینه در توابع شهرستان دوکان در استان سلیمانیه عراق را هدف قرار دادند. این حمله منجر به وقوع آتش سوزی گسترده در منطقه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/677493" target="_blank">📅 22:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677492">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG297vyHFpIzN6fXqTzjtZaY0TxE5xlqamJ_kD6hC1DbdhCoQnWRXNV5MOK2nFNig-zO7bkXASo8EVCFyx29KSgsup1RBAJxG-haQE-4jbeeyZSjv8hO4RDs9KZaueK-6291Zs4m3L8SVZZ_geas4V9P4oF2Zvxb0bIO0z40T7YbltLyHbHr_1rdt5PQVa0zLSl5PK0cCzlgMfy7SLtyEUpgpuA6Zc3uGjJm8lVmxE0jutf0KVzK48wyr-OzMB36EFcXby8gl09du71u3MWeFXgTIIwtvnBM3-qNuhlNI6rfQ93XAqeFccbau-r7yMtz6dxBHgcJVHykeh95bbUdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واتساپ قابلیت تماس صوتی و تصویری را به نسخه وب اضافه کرد
🔹
از این پس کاربران می‌توانند مستقیماً از طریق مرورگر و بدون نصب برنامه، تماس‌های فردی و گروهی برقرار کنند.
🔹
متا همچنین امکاناتی مانند انتقال تماس بین دستگاه‌ها، اتاق انتظار، حذف نویز پس‌زمینه، کیفیت بالاتر ویدئو (QuickHD)، اشتراک‌گذاری صفحه و واکنش حین تماس را نیز ارائه کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/677492" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677491">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=I1l4Fdye8id-H9hrKNTeu6ZXp8Hg0s0-KVCs68yZVL9Utj6_VQtA0EqPQJbyN1WUMwRtbk0xcMaJwzd0ytRzyof8C2FOIsp-_PAM2cUmsdd0ujI621cUDAr_6fCAf4GW7iKa6QO1fBNKxCQkma52BL6VDDAj6wyAFt6-5pRq72wsksV31FSICg-KxdHvS72c7-TWcJOzu4KpKKvnBXOMxa-DpJXxCy3olNZlt6wBo8xVFC_AMmHRY7_HUKOROX-KIeIj5cYC-k1aorHPaDhkvnva5Ry0j_eIDj0ADAnU_T4VimF7PSJPYlVIULlDajX-KP0rQxIDp1Vy3tTsoo-fpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d147c1534.mp4?token=I1l4Fdye8id-H9hrKNTeu6ZXp8Hg0s0-KVCs68yZVL9Utj6_VQtA0EqPQJbyN1WUMwRtbk0xcMaJwzd0ytRzyof8C2FOIsp-_PAM2cUmsdd0ujI621cUDAr_6fCAf4GW7iKa6QO1fBNKxCQkma52BL6VDDAj6wyAFt6-5pRq72wsksV31FSICg-KxdHvS72c7-TWcJOzu4KpKKvnBXOMxa-DpJXxCy3olNZlt6wBo8xVFC_AMmHRY7_HUKOROX-KIeIj5cYC-k1aorHPaDhkvnva5Ry0j_eIDj0ADAnU_T4VimF7PSJPYlVIULlDajX-KP0rQxIDp1Vy3tTsoo-fpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «مرگ بر آمریکا» در مسیر کربلا هم از زبان مردم نمی‌افتد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/677491" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677490">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
♦️
وزارت خارجه: دولت‌های منطقه وظیفۀ قانونی، دینی و اخلاقی دارند که از استفاده آمریکا و رژیم صهیونیستی از قلمرو و امکانات خود برای حمله به ایران جلوگیری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/677490" target="_blank">📅 22:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677489">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hylnnnebjOr807EKgJDyWTu2Issf3fZtgNx6trO7B417qCwbc2wkVr_BD6Eq1w7w5pC8BQ75X25kgppk7enOzoq7hrozPfHz14PJxff6QL6BXuwrZCVOq4Ulp6szovwBZDvarJA9Q9EKcL2tuvRucNoIGeLPHCf-pGyOv3KYgqDJ1SLd5yS_XqtZV1ZsoS-2nSJ9coZzYW_SwD68JoYtmt-Sqqyve46N_LQOP_DQKdPwV4FPvVIXnjlSx9FboWHKXlEmy_itUTe5HZS695gNV_SCvFw0emNob_auMb1Od0VB1AZ1dj4Hk-CPcBQQFUyAhoBTKroKlL5j9JA4U-iRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف از حملات احتمالی آمریکا به ایران چیست؟ / مدل جنگ عراق تکرار می‌شود؟
🔹
رسانه‌های غربی درحالی خبر از حمله قریب‌الوقوع الوقوع آمریکا به ایران می‌دهند که درباره اهداف حمله احتمالی اختلاف نظرهایی وجود دارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234815</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/677489" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
♦️
وزارت خارجه: ضربات دفاعی ایران به مبدأ حملات غیرقانونی آمریکا، به‌هیچ‌عنوان حمله به کشورهای منطقه محسوب نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/677488" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJvPuh1a_iDxqPIlYYTwRSXwzYtHpm6HXNJ2lFvJCqe4X0zwpJeopHlBfAdf1rAzXJksb-VogwtGrPua3V_5ZgiAfucwaOMbQOu3acIc2iJOphL7vw_BeAyybrefKNCMnxI3uv3w54M3L6A80PxGInGoQ1JAIobCUF0Ge1NYt0eaRowY73qXz_63Q7kjRj0BKZ-Ca7q4sBrPwGMVXTNAS1_s9LeeO2IQ3Yr8I9y3f_c3yUwnjbFDu405YQwVF5O3y4tRPWnt4tPGTCBXGAQOtOTCNKcScEev86izvMxpIynVjcIahPVAYvtdevgMjxy2hebZ59zCN_U9zAmgAUPaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/677487" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
♦️
وزارت خارجه: ضربات دفاعی ایران به مبدأ حملات غیرقانونی آمریکا، به‌هیچ‌عنوان حمله به کشورهای منطقه محسوب نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/677486" target="_blank">📅 22:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=Pfk75FCXW-OZfEvU815qZWRA_eas6FntaK4b7DyWu0o2p-SejmJs9G08GPdAd6sk1zMxiUponXNfgBshpZf_rYF-jrTZKFEc8o7YfSd17c_47yYIX5Kq3hLC5TfS9XnGIRwJZo1KZlFDFUx7xMUU1wIxOPvt5380TEKje2lHxnPq9UDot9tvUNSY0a72dsUuXL2hZdWw4XWlO7b9X5pvaqIs2fjthcwGL1mLhDpESWAtzOhX3zQJheXJIzubKWBttcEQcQ1M4H4S47mLmxwj3qdscjwQadw92fcO9S5ClBI-__hHkFnmg0j_-unpRH-FEwjVjSi3efqRnXkVgs6QLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a52f306e.mp4?token=Pfk75FCXW-OZfEvU815qZWRA_eas6FntaK4b7DyWu0o2p-SejmJs9G08GPdAd6sk1zMxiUponXNfgBshpZf_rYF-jrTZKFEc8o7YfSd17c_47yYIX5Kq3hLC5TfS9XnGIRwJZo1KZlFDFUx7xMUU1wIxOPvt5380TEKje2lHxnPq9UDot9tvUNSY0a72dsUuXL2hZdWw4XWlO7b9X5pvaqIs2fjthcwGL1mLhDpESWAtzOhX3zQJheXJIzubKWBttcEQcQ1M4H4S47mLmxwj3qdscjwQadw92fcO9S5ClBI-__hHkFnmg0j_-unpRH-FEwjVjSi3efqRnXkVgs6QLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی از آتش‌سوزی گسترده در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677484" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMIPH0gtmT1x55Jl5Xk4QPDNz7F4t1h0OuMzJ74hSOOKF5YzYqRwr9hfnAnUqM-MYOHJd3AlVYpZkN-RqRxI6HTPj5OUdlgZ4gkRJurSVUELVOpXqXvZhHVlVKaqKHDYOLpx9Vw3guKrrJdWK4aoOpr7v-VyZ_6cbUwrqJqQY24eO5A1XPKwTR_mF6ArU3oDh-BgYWBBvPjZca8CPN0g8cUi2gtSaAXRNvYvgMjTVqLyEq39BSMVKqjQmaTlQvrSCFLe1NI2GHlBRmLrYTMuZlwZGrO8UHzWnuv-scQgqmtKabID7HTwPm6lZC_AG02tMjUY8Qnyl2lUDlHJq8827w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵
نشانه هشداردهنده کمبود اکسیژن در خون
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677483" target="_blank">📅 22:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تصادف، یک کما و ادعایی متفاوت از آنچه پس از مرگ دیده شد
🔹
00:07:20 ناشکری کردن و راضی شدن به مرگ در هنگام داشتن یک زندگی خوب
🔹
00:20:00 خوشحالی شدید و عجیب با جدایی روح از جسم
🔹
00:34:20 صحت‌سنجی بی سابقه‌ترین رؤیت، در تجربه نزدیک به مرگ از داخل سقف بیمارستان
🔹
00:58:57 کشیده شدن به سمت پایین و بسته شدن روی یک تخته سنگ
🔹
01:08:25 پاسخ خداوند به شکوه و شکایت من در مورد دوره آفرینش‌ام
🔹
01:12:50 درک شرایط زندگی در دوران حضرت بنیامین
🔹
01:21:40 تجربه درک بالاترین عذاب الهی
🔹
قسمت هجدهم (درون سقف‌ها)، فصل پنجم
🔹
#تجربه‌گر
: حامد البرزیان
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/677482" target="_blank">📅 22:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPS2IkctXlxqVgMeJEpHfxYKKG2ps-nMlYWv4mWoY3oVjSpGakUNK6oDmH-xDBvg42JausU23Qw_5XOkM3OmkhhyxpMAzjIFgaxlp2_mI38nlGt53Y0fDe1xhi3M_f4qnUCURlYW-7SXvbCZHi1Uxv6jtXskwFRxn4YVfxgVVi9j_FLGbeFQ55UURCh9-KjdU29J17tGUuEYwnDBXpXMW_09SiP3uV63X7Dbu3XU2Dm-WKbgHbzWIBGhYKRtlwC_NWAZbu-pvlUCKdddaZo0jqh56hwWUoRISwlXzMo3nh1G65RtHVL_FNbvv0LuoOSuV4MVc6StJZDQBf0Mjkn3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه توئیت‌های عجیب خوک زرد؛ این بار در لباس الویس پریسلی!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677481" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cODH2uXFUa85qn9mgwtqK78LcmKd8FjhKBH3Mm5QtHI064Cr2PJdkJtQJHxoL8DE-WyZTFQQALWoBFczftIcq8OTZfCWqySFcmm-g-yN8-d9kUIjo8iaipU8xji2Ve_XCMsB31UtaOhVFTG0RTGVeAwizjsJn8ED_3e7mGD6etN6p7YFgDJ4AuX57L_hMMGxyd_OfMWGVeYZmzZQP5L2CniYaf9Jb4_XpjWJZO9qbvn8P93nd2fM4GL2w8DIYnKFE1iCM8VuRMrwla_zxCNU6Qv2aZxSlj4N4V5MfFoOiMrnhGhAcNxbyMTvbMy3b7jYsciBOXnREYQ0yJAnuhOOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی عضو کمیسیون امنیت ملی مجلس: پاسخ به حمله احتمالی دشمن محدود به منطقه خلیج فارس نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/677479" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2Dx9tmcor6A3paLN-b_UfcHySc5dsxJvlb3UooxheO-srYxOTK6TsEQlue8_1rKiuM6-ZPTbiPL3r7v8xtuNOyq52xzlCZzaPsBsYT3GLq8l4ph0DsIW7Lvy8VQlEyLp5Xrdqwp9bBs0JuOsgR1H3Hyi9yyGdyfif5URR97qxwJRvkeAchATNIh4wdnh8gX-7oKmG8_XgQXFss9vbSCVlGGtb_19NOMZYTsFq0hvLTRlntqNjc_srYiW0G2BxIBRvvw0Wm7ahKHGFruvZW59-wLp_M-OcCONHglk2_TWjKHLYWv3mpAbFwEmqK79KVRXxyWADZ4NTxuAzTbrh5IuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش جنجالی رونالدو به لقب «مشهورترین ورزشکار تاریخ»: فقط یک کلمه، «ساده‌ست»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/677478" target="_blank">📅 22:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❇️
کمک فوری/حال این 2 پسر نوجوان، زجر کشیده خوب نیست
🔹
پسری ست نوجوان، به دلیل بیماری شریان ریوی تحت درمان قرار دارد، تاکنون خانواده اش هر چه در توان داشته اند برای پیوند ریه پسرشان هزینه کرده اند، و چند سال است به کمک شما عزیزان داروهای ایشان تهیه میشود در حال حاضر ماهانه بیش از6 میلیون برای دارو نیاز دارد..حالش خوب نیست وچندماه است که نتوانسته اند دارو هارا تهیه کنند..
✍
متاسفانه پدر ایشان نیز به دلیل شکستگی پا نیاز به جراحی دارد که هزینه آن نیز بیش از 8 میلیون تومان است، شغل ایشان مسافر کشی بایک پیکان قدیمی است ولی با توجه به شرایط جسمانی توان کارکردن ندارد ،وضعیت مالی خوبی ندارند و به کمک احتیاج دارد.
🔹
مورد بعدی پسری ست نوجوان، به دلیل بیماری دیابت تحت درمان قرار دارد و ماهانه دارو مصرف می‌کند و نیاز به کمک مالی دارد.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677477" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677476">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4bvfyNH_VOzM7wlOJ_TAtPvNMSYw9n8DI0UiKD-mEaiLA7nYwBzbjUf6tPYIe56K2ZDZgKKre19W2wQXMjnI2RmYVLRC5oVA_1hb1E7GjMYDkqs7SCRb-b09ZGWSdCkwQNB39LRyXFGv1Bp0PKUOi8sVkax5z-Q66pZRYyZQ68HnkicRCXgxL6cE_VtOvF6Ps_7NI0JFDyB1dOzYEWeELOxW1ey6mIJxymMau438M1z1Mn2h9U7QjYoeJ-1ZrFrP_TbcPx92Ib13HIgFzy7uQOtH6yHdX7btfvPikMvvGLzMalUdWUrN3sO22Q7RTbuxm18sa2E-tSNsMg4wPlQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
خادمی فقط در موکب نیست…
گاهی جمع کردن یک لیوان، مرتب کردن یک جای استراحت یا حفظ پاکیزگی مسیر، خودش یک قدم در راه خدمت به زائران است
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677476" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TctE_hKiTba70PP-Uy0p_RMQ38upoR8kxpRrKOrUOTtuHG13VTdhE9H_nRqzydFwRvEa8QvuDaulFDS0DmSFBKzv38vd_kXQv7M17GzDhT411eJxuP8gnE1N4anZ1OcrZdEX0ABz9JHltxrMvz1zlA8Z0kPLc8TvoD_OKlQbE9qAPAJXlHMZ7WSpKdQd2XcvPhEqiCQnxGr1JZ6f27zIEBAqBbKblDZ_oSvxKo6HgFr7IE5iyoHdER6PMl3eMYNMw7__h8GlrS0Ha6RN9gT8D9u7snGZVejNvMx8FBQBwE3ytIW3gIeLGzbxQZ5-JHVZyBo9C0dvrbi6YrcCZNWCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyBLBpcVUtYwyC5PMnCiwrgqzuAFEAzPNRNLP7qYWg2Rh8OzKJ2X2QIw7wQxWG4efQ6Vtk0zSWzHupE7q0Gh4nl4wDpbJNT45lh5nqiK6NulIYASfKPi5ouVpJupWp_W69AY_vl34ktoN2MGBarOQMG4RPYpvfNK2SjOSA5rIO3oZnBkXQsoEiC_q9rIsSi6hVSeiw-lVxteZLbNhT4raMOAcTGatekimut0PhgMSN3tKKGOC6YhWwzAHl9PlR2MR0xmKlJwRrtXGLEMUuEOvhXMOy076oD6dJK3IhDJr9MOpU_IAKqcrvp1fAkvhw6eZe1Cwct-v57ZzyU--MdW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7X1TKagMJQWAT1u3c0UyjmFNJDOuW4fpivsiiPkS36Kv8cXe9gvnK3yGO183U4yKv4zRzAibkgTj7LIxea_oQbCawwphiv3zzKS-FcELCrbFnItWYKwF6Oa617PW7o3ISPm1b14N613QdWIufnxmEIJhquqYIuBccsU9QLi5noqSgu_2kgJBQHXlL0L4Z3l4zbkBqCLt8RkJzgZRIZYcBOZmz6xbDbKZdPsxacziz7Twxbn0uzMmz_6VfTG-Dfy02ss5M5xUKuyRqRia9yacek_TU3ci3YnZtAW0KGaVL1DkA92W9hQyxFbkxvJZUZePYIxngOuh171srMiLpujpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNPyo8gAsbTU6iQMOgk0QHLPyyIXcSxYruFrEwrjfNZ-Xu55xMDggl81in3N85mbh8taR16D5_4EUBUNGvxfu80BCDChfjVGyHt8MEQp8T0mTXjdtP8NRhCEJ6iCsoQC5oJHvvhEFXPYV7ZE_eol2QEQtDiPEytN5yTugG4HLL9NtPkTBUstyz179h11GJHmnEg0vPwUwnojHoSTsh2yxOMc7nABV5UDcLwobhaJF9gM13XEd2B939o9CdElLcPwuaOVgTAzBq-zH4oinEAgXQNPHLAIi6H-qjqcuBUN2CjW-_acA5IXQw4Eue5vUMVU153Wu4j2w4e9DN3_I-eKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taob1a14AG-k9SVKyPUGdQq61iGN2KdR38YwNttXqrmyWcjlBaJrjCfpBobkg1yZhic6GnqoT5FWzp7QCpt4IdG8F2OiiNA-8utiIDTm_VO-oVsdS_Kknh9875DVngZXqjWMaPXniJCCmC_0jHXvLqwlnm4rLBHffLHqZEAMzK2xmL2A0oFyi9ZVC87S8PIViGEJatFP3oEnsy90sQOkZgrLu7kYAIze1RWZ5PRO_lQ09Dv-twJk_GcUMnEPbscxTBXwqRgqiBW7D8HoPgeK9MyH9tj4wDitJdBPo12hBGnh0bpEhyYrZeRyFejYS9yiJJBZWqDzbCq-d_7n-ly09A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیطان زرد در حال نشر جفنگیات
🔹
سگ زرد ظاهرا رد داده!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677471" target="_blank">📅 22:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نیمی از خبرنگاران امنیت شغلی خود را «کم» می‌دانند
🔹
بر اساس گزارشی که مرکز پژوهش‌های مجلس به آن استناد کرده، بیش از ۵۶ درصد خبرنگاران امنیت شغلی خود را در سطح «کم» یا «خیلی کم» ارزیابی کرده‌اند.
🔹
حدود ۵۴ درصد از فعالان این حوزه، احتمال ترک شغل خبرنگاری را «زیاد» یا «بسیار زیاد» اعلام کرده‌اند و تنها ۳۳ درصد از آنها در صورت بازگشت به گذشته، با قطعیت دوباره این مسیر شغلی را انتخاب می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/677470" target="_blank">📅 22:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وکیل اسبق ترامپ: ترامپ می‌خواست به‌دلیل ایران، «جی‌دی‌ونس» را اخراج کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/677469" target="_blank">📅 22:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuP4F4KXC-kMWVPTQLcyaQJGitqslfUKN-hrdqSpnYEaZPxu6eUSr2beCSb-DjYpI7Kksnbzdcai7wDknaqcMGGMxen4gpHZm4kKdVD1cugKEvq1k5AeQ2jwi75eDTgD8RVqYornI9akq4CRSMdEMFL3JNVrz-LaGrgpyUKw9u767gfn8oqJy2z5if6A7aCWxGR0uIM9-6cPwmyDzDCd_cT8w5U_TaJpm4N3eGmK8KoWuFekOHucMcPDSBIyzc8dd2d32iKbWkh7popFE50V4J7yzWxyLL84SSvo2_vV3PEJv7fdc7gW6kl5mKZtWn7EL6PDlbkC1Mg0_Ef9FmDluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توهم تکراری خوک زرد: ونزوئلا ایالت پنجاه و یکم آمریکا
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/677468" target="_blank">📅 22:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
کوچک‌زاده: با لایحۀ جدید مجلس، مجازات نتانیاهو و ترامپ حبس و جزای نقدی می‌شود
🔹
در لایحۀ جدیدی که با عنوان «لایحه جنایات بین‌المللی» در مجلس تدوین شده، به قوانین مجازات اسلامی ازجمله حکم قصاص دربارۀ جنایتکاران بی‌توجهی شده است.
🔹
تصویب این لایحه بدون اصلاحات اساسی هیچ کمکی به ما در جهت رسیدگی به جنایات رژیم صهیونیستی و آمریکا نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/677467" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/setm6t2zVoSHQ6holBNh6gYlc-mhAcam9-iMvELwftbCm4NZm2_81AAyUmKr01N5UgRNZTXq3WavXQSgN0XyJjHysCzw6C50milDMt0rYR4EfzEALyaGfvxXMjFH6Wic4ZR8G7INfUOPcg5IU414EuaG2Oti4dYZXia5IkiPDq1uKkmAlyI-AMi2upA3DsziEjIXwfOCWPKq3YV7ZzuDGFF4oEfXMpmfzyspGXQHKAQ2pq6ETs5cDicWY59qTUSBlEUTMRz6qXZLVK-g9SJ56hVrivty1q-jabvI3--68-bebkOgowNc98a_lsRINX-OU5KNtDXVmjJrIOOLqZwUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی قلهکی: زیرساخت در برابر زیرساخت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677466" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c57ff11e.mp4?token=ilbk1Lwh5mcLV-JCRkxw-0LSv3lx9hOcoGdbEW3O757OTZfwJ0ssZwXFrguTvpxDzbf69sdeMV8Ck9bc1ciC-w1rqVTJFAhOQqE9v84SdeTqAsLIJBjuiKfW6TXQmLbliN2Pr_qSIhubQTp8i--MmAA98VymcL9fUG4ZzQJx7LZ0IaH9kVX-hbN3bQWJgbghJ3yF5YFBgOB-I-YYKI2BKKqHv9ONlZdfjRYFM1GD9hzJmDknKzNB0aofoONFWzR7s8jCHFdPNR-JZgzop3CrPYZUhOsktqAa7t3R-AH1fgV2ZubQI0UVeQEFC89v5IrPc1-OVsLTCuFWE7fD64oS-JAIxFhF8Ipqm7pnjy26mZsnEsv3TQu4oSMlnLzRr-hTvzrzWXmz4wR9u_JmilLCQHFP98rhbRNrDU7zXuRECmPnmnfbJ7qYcOEeyQ4W_nA5Q_rYgT0gifLz1eOUkebS3SSYq0rvpEqo7R1KE5zeTVNkMGjPF0bZw7NUZj3o4MIbvzUujiACYyE73G9wMmi6CWySWOWxBcY5xc_mOQes1b3Go7Y0rfgXL79t9p8RnfwYy_nkkO8k9WFyqXvJn7zBNJzIc75Ok3bx_q_WArSpjK5AFvTLp4MwC5SH0t5X9h16jE0lB2lRfIbmbHGLbjv5zciiLt-2noR1R__1eT8ISuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c57ff11e.mp4?token=ilbk1Lwh5mcLV-JCRkxw-0LSv3lx9hOcoGdbEW3O757OTZfwJ0ssZwXFrguTvpxDzbf69sdeMV8Ck9bc1ciC-w1rqVTJFAhOQqE9v84SdeTqAsLIJBjuiKfW6TXQmLbliN2Pr_qSIhubQTp8i--MmAA98VymcL9fUG4ZzQJx7LZ0IaH9kVX-hbN3bQWJgbghJ3yF5YFBgOB-I-YYKI2BKKqHv9ONlZdfjRYFM1GD9hzJmDknKzNB0aofoONFWzR7s8jCHFdPNR-JZgzop3CrPYZUhOsktqAa7t3R-AH1fgV2ZubQI0UVeQEFC89v5IrPc1-OVsLTCuFWE7fD64oS-JAIxFhF8Ipqm7pnjy26mZsnEsv3TQu4oSMlnLzRr-hTvzrzWXmz4wR9u_JmilLCQHFP98rhbRNrDU7zXuRECmPnmnfbJ7qYcOEeyQ4W_nA5Q_rYgT0gifLz1eOUkebS3SSYq0rvpEqo7R1KE5zeTVNkMGjPF0bZw7NUZj3o4MIbvzUujiACYyE73G9wMmi6CWySWOWxBcY5xc_mOQes1b3Go7Y0rfgXL79t9p8RnfwYy_nkkO8k9WFyqXvJn7zBNJzIc75Ok3bx_q_WArSpjK5AFvTLp4MwC5SH0t5X9h16jE0lB2lRfIbmbHGLbjv5zciiLt-2noR1R__1eT8ISuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاردریل، سپر نجات؛ پایان خوش یک تصادف هولناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/677465" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6553e33e7.mp4?token=nxyuQ1OXf2_hu1gd92WdOFpFHrHqJKLD0JTl1Gxh4Jsmsw_pBrQOJqrcJvkP4v3QweVQjznSJGh8h6BwO47NIUi3w_Eb_TKU75u7K0IZkUj_B6X90FBcBk2YJP-mEZfu1GY0n5SfxSlcNZHrtGnEpWuf4iFb6QdiWsKrKzeXXvliHkmFFoulX87SOjRvDW4TPQLgGlHIAnmVCM1uWx2bt0Gk3vaJTzymmKiVz6mM0IQVwv0GrHwA4_ZPCO97Kb0b-atCiQZKKifCrG2kpdw7dcXdeuoxQwZEmabbJ3bbUN3fDF0e6zq9dtH6T-shGuHv0iQYRjq8kbioInPhzVyIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6553e33e7.mp4?token=nxyuQ1OXf2_hu1gd92WdOFpFHrHqJKLD0JTl1Gxh4Jsmsw_pBrQOJqrcJvkP4v3QweVQjznSJGh8h6BwO47NIUi3w_Eb_TKU75u7K0IZkUj_B6X90FBcBk2YJP-mEZfu1GY0n5SfxSlcNZHrtGnEpWuf4iFb6QdiWsKrKzeXXvliHkmFFoulX87SOjRvDW4TPQLgGlHIAnmVCM1uWx2bt0Gk3vaJTzymmKiVz6mM0IQVwv0GrHwA4_ZPCO97Kb0b-atCiQZKKifCrG2kpdw7dcXdeuoxQwZEmabbJ3bbUN3fDF0e6zq9dtH6T-shGuHv0iQYRjq8kbioInPhzVyIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غم‌انگیزترین تصویر از دنیای حیوانات
💔
🔹
مادری که مرگ فرزندش را باور ندارد. دلفینی در استرالیا، هفته‌هاست پیکر بی‌جان فرزندش را رها نمی‌کند. پژوهشگران می‌گویند این دلفین در حال سوگواری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/677463" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: تصمیم ترامپ برای حمله گسترده هنوز قطعی نیست
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/677462" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6nNbnAjwtDAohVPq38nefOcMmBahLI44cJXX-XyTAycPsWz3-7bAqW83TQj3N95JnNgbaFjntJ3UH7vuKHZ5yJTZOvodr19obZt-KV5AAKpDAM4pIoPARg-jKHM0iLyK8bON_cwG8DCLMQC2fAua4A8j9HPgSQAh4U8PrEzX3oeRF03qGa7K2LxBfHGniGKF6paKhSGvUZUdZ-H6y1ecS926Jf6klJQ2YRnoR2Y2vuCfmK25L1DStg_elHnD6nVjvZW_1exy_Kvz5KPDaZkXcJ-Bnf-aDI3hANB6qAlz0DAtqwTn-hWK8HYF9VQq6_0HQo8Ip1sjxWNPzRuy5ytVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عدالت از نگاه امام علی (ع) فقط اجرای قانون نیست
🔹
در نهج‌البلاغه، عدالت با چهار ویژگی تعریف می‌شود: فهم عمیق، دانش، داوری درست و بردباری. از نگاه امام علی (ع)، کسی که حقیقت را نشناسد یا در برابر سختی‌ها آرامش خود را از دست بدهد، نمی‌تواند عادل باشد. #نه…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/677458" target="_blank">📅 22:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010ea8b9ca.mp4?token=ILzCIokExCoBvZcjRHFLA2zp3_KBxurxshM_TEO65ONq9y7sHpDdkA_cGIxGu3HF80DSG5OU6wbhGvSQWVKlMWAoTErcm2iZe9gb87rwD6Auxqi7JA7sI8qzM_ZT0btpQBStP1zP2vLZRu-Cg-iyTigMHCTgqOLtu_9ftKqlH5UqYGTjGoVxSpiJSeARApTiVMpSmKbsLnsxWPsVaaOUJbUYm7UfU0Iim6JzCw5dyLCuTZW1db3-Vzvz37p0v584SedfHaf4XpBH5tTi3vACSVRtSMmsaamljYkVuWhWFytMLWdOz0r4qLMX9G_MJzKMO8KhsEKT29gddRCrDtuugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010ea8b9ca.mp4?token=ILzCIokExCoBvZcjRHFLA2zp3_KBxurxshM_TEO65ONq9y7sHpDdkA_cGIxGu3HF80DSG5OU6wbhGvSQWVKlMWAoTErcm2iZe9gb87rwD6Auxqi7JA7sI8qzM_ZT0btpQBStP1zP2vLZRu-Cg-iyTigMHCTgqOLtu_9ftKqlH5UqYGTjGoVxSpiJSeARApTiVMpSmKbsLnsxWPsVaaOUJbUYm7UfU0Iim6JzCw5dyLCuTZW1db3-Vzvz37p0v584SedfHaf4XpBH5tTi3vACSVRtSMmsaamljYkVuWhWFytMLWdOz0r4qLMX9G_MJzKMO8KhsEKT29gddRCrDtuugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در یک کافه در مسکو
🔹
خبرگزاری فرانسه به نقل از پلیس روسیه از وقوع یک انفجار در کافه‌ای در شهر مسکو خبر داد که منجر به کشته و زخمی شدن شماری از شهروندان شد.
🇮🇷
✊
@AkhbareFori
|
Linkظ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/677456" target="_blank">📅 22:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: اسرائیل به زودی به همراه آمریکا دروازه‌های جهنم را برای آنها باز خواهد کرد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/677455" target="_blank">📅 22:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77975f3da.mp4?token=cKPFUmQOIvdaDVQ5Td589Ukj-tNqzIZi3jOaGpYT86mkxf5pmD4Q0pXbFal-3ydFP9iXsbLwg77oCVMAZlZqbXnTTbXOKyuQLgTVBmTk64qNQItZhDDxj2ZhRt5GZT3dcQCztSgFauD9ngTf7WMBHtd4LlKr8qXEir44nB8j38wxQEAJ9-XXuX2gS6ZY35xYirrKG7GAXdw-GGpcRs2H9S1DL53wdiglAfgLfbcOO4pCQpCzFQ8VoPfebnbeN3RGXdCz-5izy72AZ6Tni9o6xofTj8e-wJKqgfs8hnLxiXGcFYKKy13dTsSck-oxOzPN0u4MXdN_Vy5bZC95KoI-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77975f3da.mp4?token=cKPFUmQOIvdaDVQ5Td589Ukj-tNqzIZi3jOaGpYT86mkxf5pmD4Q0pXbFal-3ydFP9iXsbLwg77oCVMAZlZqbXnTTbXOKyuQLgTVBmTk64qNQItZhDDxj2ZhRt5GZT3dcQCztSgFauD9ngTf7WMBHtd4LlKr8qXEir44nB8j38wxQEAJ9-XXuX2gS6ZY35xYirrKG7GAXdw-GGpcRs2H9S1DL53wdiglAfgLfbcOO4pCQpCzFQ8VoPfebnbeN3RGXdCz-5izy72AZ6Tni9o6xofTj8e-wJKqgfs8hnLxiXGcFYKKy13dTsSck-oxOzPN0u4MXdN_Vy5bZC95KoI-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقادات نوید کرمانی نویسنده ایرانی- آلمانی در مقابل وزیر دفاع آلمان: حق حمله به تمدن ایرانی را ندارید، یکبار برای همیشه به اقدامات غیرانسانی ترامپ نه بگویید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/677454" target="_blank">📅 21:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مردم ایران روزی ۲۰ هزار تن میوه می‌خورند
اکبر یاوری، رئیس اتحادیه صنف بارفروشان تهران در
#گفتگو
با خبرفوری:
🔹
روزانه حدود ۲۰ هزار تن از محصولات کشاورزی داخل میدان میوه و تره‌بار توزیع می‌شود و نزدیک به ۱۵۰۰ تن از محصولاتی که ضروری نیست، دپو می‌شود.
🔹
به دلیل افزایش هزینه‌های تولید، میوه از سفره بخشی از مردم در حال حذف شدن است و دیگر مردم توان خرید میوه را ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/677451" target="_blank">📅 21:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQnCxz1z5kU21LPW1PWhxXQFbvDs28UYRr3SEtYhyn6iJCZ5098dbd8cfknzMJk2Z6G6RUfhPQYPxHavkWIb8t-dtsr_3v5V8bDDI5Ku65BBNli8J_1dhKat3ifa_-gWe7lEBAP3VE-bBso3mlGrrd7ZdFCbMQscSbl7PK08T9Q7kQpUE1WB4-J7123Jd47KUIh3_MCblVSO7kDqIyiQZAHWXDnkdNNEHoHeD6zJoPMQkGhkCQz1XkfLzXymKuuJvNjA-hdzFp4RTgVsppEsiwrfbLb1hxWSMGh1fA7BDYdu7Fy7A8SsJOcWMS96bl0NKgDOjpjsXYOZi_EiY7LWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVJKURMmCJ9TMWKeT6fyiFEU742r8bBURN4W8RwTHb60wyLjNkuf92Hs6WgSchkE6DQ8BIPYKZa1k_Pr8hKbP6wjzYj_uc5TVxfkPcMlnv87kOCW8nt-NcXgZFdplrf68SGmXaF3FCcrjOJm5vupR4iXxh9GSH9FJcfQ4jBA3mE0LuQvUIn_qIq-i1ZrdaNPsok10Aq0UfLddNgU-_Ho9tCfcjfcDcsqot0qjWFr3WQVtoXuiYFTcNQW4S5OwizPwVIhgiGc30Wh6OzRX4j3_QwTrShhUw5CpZvcXYSGgyUD3qrVu-8pBv_dd0FwlqTxIMsd6R31G6917VYJXCVoKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست های بی مفهوم دوباره خوک کثیف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/677448" target="_blank">📅 21:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=Bc22BUa1iVR_m-Rzkg50C6jLOwdNSf05HBCxok_5FZNxkKXQpTcKv4019dS9OIfx1wLVr0TiktYOA_WIL_a6actLkm75aygamflpOuAfpqYPusw_QSkxTKfT2ZAQpcq119z4zMgVv0RvX2-huh8aOuvh0o7h5SSqatO59WcnQ1w9POf3BtUcXkhIR6773gS-aSI4q49Pdv_zqexyzcdWwKhKXzng2uNjJ2sPC-SSQMDpbqG1lXcYM3t0c-A5zau5KKdaTiZm91f3XdLBQvhkvdkMWuCIzlt-zD_8PTZB40Krjg-TsiqGuh-Ti_0keVf95-nXSs7FnMK14tbaj2zUwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d52c5baf.mp4?token=Bc22BUa1iVR_m-Rzkg50C6jLOwdNSf05HBCxok_5FZNxkKXQpTcKv4019dS9OIfx1wLVr0TiktYOA_WIL_a6actLkm75aygamflpOuAfpqYPusw_QSkxTKfT2ZAQpcq119z4zMgVv0RvX2-huh8aOuvh0o7h5SSqatO59WcnQ1w9POf3BtUcXkhIR6773gS-aSI4q49Pdv_zqexyzcdWwKhKXzng2uNjJ2sPC-SSQMDpbqG1lXcYM3t0c-A5zau5KKdaTiZm91f3XdLBQvhkvdkMWuCIzlt-zD_8PTZB40Krjg-TsiqGuh-Ti_0keVf95-nXSs7FnMK14tbaj2zUwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شهادت جنین ۶ ماهه در حمله به مدرسه میناب در برنامه پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/677447" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677446">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ba950ab5a.mp4?token=pG3O7VEECN2zXeZbuj6ghF4AAR1hqeGNlhgauaDfcMD2OIUkulQPDx_MR4QRxF9uocPHj8zvUj50amvsaHlgxAdAptCeV2PIIaYN9C0d74daFPa1PVuPEGuisJLifj_hSlQoT_PnTLmyoRl5DB-JqZqi34L7xAthyDr9EK-PwDH_8DVDEF3HRRbxzT-TKwMmnsa_EgO8zfm7KbibGP-kJ06AAtVI5XVRFt-z1Z6QPsuOSdnLQ32llM1JSvXOzJoFH_F0Zr3OCcmBVvvyFUqiZt7lbc3cVsQ9ONMj49p2YcwlAIIUiNSd5cRP21ZwDDZXdl8MPkoa3K3ACfDk3rzrrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ba950ab5a.mp4?token=pG3O7VEECN2zXeZbuj6ghF4AAR1hqeGNlhgauaDfcMD2OIUkulQPDx_MR4QRxF9uocPHj8zvUj50amvsaHlgxAdAptCeV2PIIaYN9C0d74daFPa1PVuPEGuisJLifj_hSlQoT_PnTLmyoRl5DB-JqZqi34L7xAthyDr9EK-PwDH_8DVDEF3HRRbxzT-TKwMmnsa_EgO8zfm7KbibGP-kJ06AAtVI5XVRFt-z1Z6QPsuOSdnLQ32llM1JSvXOzJoFH_F0Zr3OCcmBVvvyFUqiZt7lbc3cVsQ9ONMj49p2YcwlAIIUiNSd5cRP21ZwDDZXdl8MPkoa3K3ACfDk3rzrrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند جدید چینی‌ها؛ سفر با خودروهای برقی و اقامت در همان ماشین!
🚗
🔹
با امکانات رفاهی کامل، حالا ماشین‌ها به اتاق خواب‌های سیار تبدیل شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/677446" target="_blank">📅 21:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ac090018.mp4?token=BwHBn59k2_o8VidGjb0Y0zq_f1bK7EDg2pEdpXikvtaUAczQFhZUUt0ELQHOLngt2y7BOHqIpQyPuLyE0J9eqtzVC8aSgYY6W4YAB_Nz0k43aByfNdXlD1SpePM-W3dYB_6n_KvK-awl3DSaLVlMHP_l6G9XL1TjgQcbqGNjcRDmhcHwZbdtkO9azgoIgHH2HU581HpUZ__xemAfRFiT1iq7dtfFgQYe2RbpJY51vLpZWz3BFQVOpJIH7JP9UzfyiMis7Ufz-EzJkybmqs3-tFyEwMnThGJNqUPhoCFbXGtnsoGgIM5s9Do24nx7GnUiydV-YSOauji3-r2jRlClRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ac090018.mp4?token=BwHBn59k2_o8VidGjb0Y0zq_f1bK7EDg2pEdpXikvtaUAczQFhZUUt0ELQHOLngt2y7BOHqIpQyPuLyE0J9eqtzVC8aSgYY6W4YAB_Nz0k43aByfNdXlD1SpePM-W3dYB_6n_KvK-awl3DSaLVlMHP_l6G9XL1TjgQcbqGNjcRDmhcHwZbdtkO9azgoIgHH2HU581HpUZ__xemAfRFiT1iq7dtfFgQYe2RbpJY51vLpZWz3BFQVOpJIH7JP9UzfyiMis7Ufz-EzJkybmqs3-tFyEwMnThGJNqUPhoCFbXGtnsoGgIM5s9Do24nx7GnUiydV-YSOauji3-r2jRlClRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفتالی بنت، نخست‌وزیر اسبق اسرائیل: قطر امروز برای ما خطرناک‌تر از ایران است، چرا؟
🔹
چون حداقل ایران آشکارا می‌گوید که می‌خواهد اسرائیل را نابود کند.
🔹
قطر به کانون‌های نفوذ دست یافته است - دانشگاه‌های آمریکا، و حتی مقدس‌ترین مکان برای امنیت اسرائیل: دفتر نخست‌وزیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677444" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
۸۸ حمله موشکی و پهپادی به مواضع کُردهای مخالف ایران در اقلیم کردستان عراق
🔹
استان اربیل هدف ۶۶ حمله پهپادی و دو حمله موشکی و استان سلیمانیه هدف ۱۰ حمله موشکی و ۹ حمله پهپادی قرار گرفتند و بخشی از یک موشک نیز در استان حلبچه سقوط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677443" target="_blank">📅 21:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هاآرتص: ارتش اسرائیل سطح آماده‌باش خود را به حداکثر درجه رسانده است تا در صورت حمله احتمالی آمریکا به ایران، آماده باشد. / انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677442" target="_blank">📅 21:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677441">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWQsgkV3P5YYtIRmk08Ofxx5ZZeH2xMJUYK7umxlZJBMLZGMGUhi2e82XCb3U4f950WNh7lADE-QYSfExA7VlwpMwFWUxE2n5U1EkYB-aByRRb2BpXGXRhIgiHFogORmI1GHmuTGOQX1w4iNPJq6WRbeR6V16o12et73-fp1Y-bvE7tgTZ6DPM2qkoZFFgsHaNhWCH2K-riordOUWgdPJpPZadvVeSuHzd79e1eRbBRGUQ_CrnOLeGSv0MgDuVxYzoFdrB6SqBkPULUd-WSjeDFpO9SJO83ZX-zbXqwr4HSSKDgSXeE8EO6uiBS_RCqV9D6JSduqHxiT6Ye4o5SJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
الوعده وفا؛ گام بلند فولاد خوزستان برای جبران ناترازی انرژی
♦️
فاز اول نیروگاه خورشیدی بهبهان فولاد خوزستان در آستانه بهره‌برداری
🔹
در شرایطی که توسعه نیروگاه‌های خودتأمین به یکی از مهم‌ترین راهکارهای عبور صنعت از چالش ناترازی انرژی تبدیل شده، فولاد خوزستان با اجرای پروژه نیروگاه خورشیدی بهبهان، گامی مؤثر در مسیر تأمین پایدار انرژی برداشته است.
🔹
این پروژه افزون بر افزایش تاب‌آوری تولید، با کاهش وابستگی به شبکه سراسری برق در زمان اوج مصرف، به حفظ پایداری شبکه برق برای سایر بخش‌های مصرف کمک خواهد کرد؛ رویکردی که منافع صنعت و منافع ملی را در یک مسیر مشترک قرار می‌دهد.
👇
👇
akharinkhabar.ir/local/10964275/</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/677441" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677440">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaJT46Ka8pMOzYXKApUabC9HhxeelAPKwyBvE1Hb22siqvSNIUkLHEDH3ejao79P0nIrMBjvRrr5YOE7oZmNexJ5diqrMmVf7a0PJy1DHAX6pqlJVjueOf9hYJFJaNNQMorUT_ae4llHASPTa_NR79tRCVKjYP9MiCJBuGZ7YPOf_-hbayrPKvC_0zLCpW-EV9xkujm2hMsfAe2XOo8NcgD8NFgTv9iynoJodiKyAibO01kfr_aJe6ZWBal-4ml5rHX9NEchRGpN7VgxzYtlLcZbnFZDtcb6MrH0YI1Ikcyg6ryLdMVR-StMij1hyMT3cXoOfSLIeFS4zodUIA8Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی‌نیوز: روسیه در حال ارائه اطلاعات الکترونیکی به ایران است
ان‌بی‌سی‌نیوز:
🔹
نظارت ماهواره‌ای و اطلاعات سیگنال‌های روسیه احتمالاً به ایران اجازه می‌دهد تا بهتر از خود در برابر حملات هوایی ایالات متحده دفاع کند و حملات هوایی خود را بهبود بخشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677440" target="_blank">📅 21:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677439">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Fz7ZESP1_6PyX_s3cuqDjAZ0It87CNrobiOzeOmfG6h1LmdQgn7S40xv0sBBLmEpz8DyAbn558oypatSFqvUkPxzxTYmAuIMgJ2eqATjlt40qzSgtQE_bazyuiSy1Px0Km6Z2X1xm8JsyhIKb1Xbx5vTJVmccy3xgdcBN_WzMXmbZfNa2n4-Y3_tTMuB9U2Wl4VqJ9b9ubThbja35SRLU3jVAeZheGnxteUog20b4vnRJS0b3ng1hHqDtfmI-RZu7xjCKMjJWJERDp22ACtHlJv7ktRpFIOKX3uboo3A3U1bMVy2rc1w9QqusRk8VNbOaOGew6yJ9V7b5efpiaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای ناشناس آمریکایی که احتمالا جنگنده است از پایگاه هوایی الظفره به پرواز در آمد تا بر فراز خلیج فارس عملیات کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/677439" target="_blank">📅 21:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
الجزیره از حمله پهپادی به سلیمانیه در شمال عراق خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/677438" target="_blank">📅 21:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80bf386d9.mp4?token=WdkDjjvQDXhoGILBJWeUTDDaMZNoZcNPq_W4m6SlWs2PnN4l_BVIflKp7UBi5E44daqsLiX6AH0WFTxCaNcMKJmYDMPB9Ln-Cj9YNgHw2-zjSESWiJz53yabT9JNnZzgMgpqB4D84Ko-zUTdwxaGtNQAw50lXFblf6eU7ZT0k7m7cIQh-fgcv0JVkT-ldWSpT7NC1Ch0GR9gxpD08gAA-WbW4SQORRHDqgJwPTd6FlF41KBcT8OmjgqP6toId-QEOkcf7wkT_nPCfoYgPF_F7UxEWx2V3BYHpsSZd0OaWiDSx0WXmdwi2XNj4K0JLX_48EJ62-LydMfqzMoodfs-aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80bf386d9.mp4?token=WdkDjjvQDXhoGILBJWeUTDDaMZNoZcNPq_W4m6SlWs2PnN4l_BVIflKp7UBi5E44daqsLiX6AH0WFTxCaNcMKJmYDMPB9Ln-Cj9YNgHw2-zjSESWiJz53yabT9JNnZzgMgpqB4D84Ko-zUTdwxaGtNQAw50lXFblf6eU7ZT0k7m7cIQh-fgcv0JVkT-ldWSpT7NC1Ch0GR9gxpD08gAA-WbW4SQORRHDqgJwPTd6FlF41KBcT8OmjgqP6toId-QEOkcf7wkT_nPCfoYgPF_F7UxEWx2V3BYHpsSZd0OaWiDSx0WXmdwi2XNj4K0JLX_48EJ62-LydMfqzMoodfs-aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید تلخ‌ترین اتفاقی که میشه با دیدن این تصویر کاملا متوجهش شد
🔹
این نوزاد ۴ ماهه از همون روزی که به دنیا آمد در یه بیمارستان در اکوادور زندگی می‌کند چون، مادرش بعد از تولد رهاش کرده و دیگه هیچ‌وقت برنگشته
🔹
پرستارها می‌گن هر بار کسی از کنار تختش رد میشه، سرش رو بالا میاره و با دقت نگاه می‌کنه؛ انگار هنوز منتظره یه نفر بیاد، بغلش کنه و ببرش خونه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677437" target="_blank">📅 21:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bda2e364.mp4?token=HOjbBvYodLMS1JUiSqIbM6N6S5rvBUtf5A8dDkh1Ir-o2fkc_Q_XJiGH2XTZyIKphnrPFeGjMo2IjLY5XB370U0I86kTByUzJVPIdEvblHNtky8h-_B17vk4jqBry_siGcP-YdrqMk7X4hR2DitOKOTIePTfiz63tnzrmYPwHmmJayyJ6pj68I-B55Pzcc75-JKgyL0NxJUFCYEktN-cym9YH41E1psXX5cbr4xjqFzcClIgyis08LMsQ9Ao84UEJynzrIJdJXAbVkxwBP-D6iEjN6Hw6IJxFwDwylwHNDePCVMGKfXSnBmFw07Hqb9-FjZGPGhyP8NHjsR_jWi7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bda2e364.mp4?token=HOjbBvYodLMS1JUiSqIbM6N6S5rvBUtf5A8dDkh1Ir-o2fkc_Q_XJiGH2XTZyIKphnrPFeGjMo2IjLY5XB370U0I86kTByUzJVPIdEvblHNtky8h-_B17vk4jqBry_siGcP-YdrqMk7X4hR2DitOKOTIePTfiz63tnzrmYPwHmmJayyJ6pj68I-B55Pzcc75-JKgyL0NxJUFCYEktN-cym9YH41E1psXX5cbr4xjqFzcClIgyis08LMsQ9Ao84UEJynzrIJdJXAbVkxwBP-D6iEjN6Hw6IJxFwDwylwHNDePCVMGKfXSnBmFw07Hqb9-FjZGPGhyP8NHjsR_jWi7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: شنای پروانه
🔹
ژانر: اجتماعی، درام، جنایی
🔹
فیلمی که با انتشار یک ویدئوی جنجالی شروع می‌شود و در مسیری پرالتهاب به پایان می‌رسد. این اثر اجتماعی که با نقش‌آفرینی بازیگرانی چون جواد عزتی، امیر آقایی و مه‌لقا باقری همراه است، یکی از جدی‌ترین تجربه‌های…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677436" target="_blank">📅 21:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVzzi_rr90FPW46iI2tGJyUvJuNcS7VdgdqDuCvqg-tUBA3yazpuY-D0OslmGlnN4u6Y3X0W5-22-BKbZ0szBTabfDgrW2DuZ5yEibhwDkXPzV3rUzQnqU-9BCKnt1-fmjzsOYPDtkcOOoumEMSjwepezc_X9BZxZHS9oG9rf2bHS-C_ciEsW6OytiuPpNTnpcLfeYnC3Tpy4fWLr4zBOBzoOF2LS27FuxH7g7cbxW80AmLBi1L6r-l0mJKK0bdzz47fX0LnMSuBs3d8_pPUjYmrLh6CWlMqz2JFK-iy0j1pNywk4F7X0K7KeLIdiPBIj0pdAOki0cCj0boOV093MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
مشتری راحت‌تر می‌خره، تو بیشتر می‌فروشی!
اسنپ‌بارکد رو که داشته باشی
🛒
هم مدیریت فروشگاهت راحت‌تر می‌شه
💳
هم با فعال کردن خرید قسطی از طریق اسنپ‌پی، مشتری‌های بیشتری رو به خرید ترغیب می‌کنی و فروشت رو افزایش می‌دی.
🚀
همین الان ثبت نام کن
https://snappbarcode.com/snapppay-register</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677435" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a10bb1e850.mp4?token=v3qZK6ji6jUWYiUKZlABu9WgqUJ3yfS3TxE7PT_gG_b-tKNzYtmv6d5ZBqdQtkfUSmpk30wjKX_kZe7gYFBoLGHYAM15W9o2LL23ZZU1u9QbgAlzhBoQSbKvCqWCWabI9WNFOHqGm6PubnbMV6A437ZViyDQ58v_xBJ1IEeyOP2ig86syO8maMLTZ7SXa8fP_XRKhFZIPVhWYyTjdM1QkoMssOLsguOOLfv6JhnxgXp6dSeCuGWaD3iWtbiw5MCuLWUMB1WcHRfA6r8aGEQ2gFFM1yjbWrgtOv3CBryAJIsGZhZT8EBS1FuGSQQ5enA96lnESjRo0jR01g5AkP7xQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a10bb1e850.mp4?token=v3qZK6ji6jUWYiUKZlABu9WgqUJ3yfS3TxE7PT_gG_b-tKNzYtmv6d5ZBqdQtkfUSmpk30wjKX_kZe7gYFBoLGHYAM15W9o2LL23ZZU1u9QbgAlzhBoQSbKvCqWCWabI9WNFOHqGm6PubnbMV6A437ZViyDQ58v_xBJ1IEeyOP2ig86syO8maMLTZ7SXa8fP_XRKhFZIPVhWYyTjdM1QkoMssOLsguOOLfv6JhnxgXp6dSeCuGWaD3iWtbiw5MCuLWUMB1WcHRfA6r8aGEQ2gFFM1yjbWrgtOv3CBryAJIsGZhZT8EBS1FuGSQQ5enA96lnESjRo0jR01g5AkP7xQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۳ عبری به نقل از مقامات ارشد:
آنها انتظار دارند ترامپ دستور از سرگیری درگیری ها را صادر کند و ساعات آینده را بسیار سخت توصیف می کنند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677434" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
‏رسانه‌های سعودی: اردن به عراق اطلاع داده که حشدالشعبی قصد حمله به خاک اردن را دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677433" target="_blank">📅 20:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677432">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
لو رفتنِ ادامه داستان سریال بامداد خمار؟! درگیری‌ها بر سر فیلمنامه سریال بالا گرفت!
🔹
سریال «بامداد خمار» به کارگردانی نرگس آبیار در روزهای اخیر با حاشیه‌هایی درباره اتهام سرقت ادبی مواجه شده و گروهی از نویسندگان ادعا کردند که نسخه اصلی و اولیه سریال توسط آن‌ها نوشته شده است.
🔹
همه این‌ها درحالی‌ است که تیم فعلی سازندگان در مصاحبه‌ها اعلام کردند فیلم‌نامه اولیه کنار گذاشته شده و سریال بر اساس متنی جدید ساخته شده. این تیم همچنین نام تیم نویسندگان اولیه را از تیتراژ سریال حذف کرده است.
🔹
مهدی آگاه‌منش، یکی از نویسندگان اولیه سریال در مصاحبه اخیرش با تبسم کشاورز در رسانه برنا گفته که حقوق معنوی نویسندگان اولیه مورد توجه قرار نگرفته است. این نویسنده برای اثبات صحت ادعای خود مدعی شده است که در ادامه سریال اتفاقاتی مانند مرگ برخی شخصیت‌های مهم خانواده، خودسوزی خجسته، حمله اصلان با قزاق‌ها به خانواده بصیر و همچنین بخش‌های زیادی از قصه‌ها که در ادامه سریال رخ می‌دهد نیز در فیلمنامه گروه نویسندگان اولیه طراحی شده بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677432" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677431">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/326aeee761.mp4?token=IMGRj7IOhBPWxGtyJXOFBC9mpRJghlAVDla5dPFUmrdz8MNPQZIho89aRdYrMGZGP2ZgNDb09GO1bcFXgzcEC61XBov5xFOEGbsIu1Q690YFlmaMsX3XPV9eEeMjx1lv3DEWtFI_jKnhJAZpAqMbrBMOIXQVbgVEo3ttC3qKWBduCOvg0CQ2XVaQwnw_NHx-5qbHlcD_-nxNeiumMVzoVZRHc5M7MKkzDfWXwTx1GF7omhcuElHn7lNid2F4YgH79m_-56qMjWflKzQCBonEc8kdKIB6m0gfEJ-7P_mIr6Lk067q6iW90apC3mspuNcMWau-2RmnVNv_qy6xI8e9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/326aeee761.mp4?token=IMGRj7IOhBPWxGtyJXOFBC9mpRJghlAVDla5dPFUmrdz8MNPQZIho89aRdYrMGZGP2ZgNDb09GO1bcFXgzcEC61XBov5xFOEGbsIu1Q690YFlmaMsX3XPV9eEeMjx1lv3DEWtFI_jKnhJAZpAqMbrBMOIXQVbgVEo3ttC3qKWBduCOvg0CQ2XVaQwnw_NHx-5qbHlcD_-nxNeiumMVzoVZRHc5M7MKkzDfWXwTx1GF7omhcuElHn7lNid2F4YgH79m_-56qMjWflKzQCBonEc8kdKIB6m0gfEJ-7P_mIr6Lk067q6iW90apC3mspuNcMWau-2RmnVNv_qy6xI8e9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلتنگی خواهر شهید آرین زارعی برای برادر شهیدش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677431" target="_blank">📅 20:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677430">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQvcZAeYaDP65lgZdQNWSOQBUmQTxxjMDwJ3Zb1trLIKXPYlobkjznHIUhx6PlX687ALIZFZqFAZH61eo6PfFrS4Np9LwQhNOGutFy-uJ3sugMdda5hoVxr26vDm0-Gd3pwKy5B9eHwrkl8dezs5XFL_sdFtvL2GxY3rxoyBP1Uw-BYtxNbl1VDwyGdefmMjoCNpyEETYp3mQS1g5LaSPdxJlgYC6e0VrRzWWIrUR5A6XLLOOjZJmHFVVqvhsynxftr27vg68ncUFWsE46tPYjomTlKZCkwmNASAaUk_oasJUJZ7G-T8_bfZmfj6w-JhjBHy7J1hn8B0zgP96ZaKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سروش صحت و پسرش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677430" target="_blank">📅 20:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4LSMzTam9gGreHxXKo1vS2yqD5k0FPpsOyFoHyjO3UOh5-q6LGJRhk-bUb1dKjcoOMFh9My_lhbNoA2czbt66Sx7f_eqjycC-qpI8VQdibsakr3_RLrbKTXiS_HJX9f7xAFZbnF8fSumYXtHlyF5e7cU7Y-8gt1LU1tT67GeLFLBXy6Db_ulrslk7ZUB2lxcZBavm0fxx-yqzuRyme_456R-dg9MYXd25t58cYyZlruD-ZwxC_1-SR0qLI_89MkAcFCDuLNMV5vHCGuPJSM_fb6y9uMdlNqnHYyyrv_Qw3w59pZvjBzfsT8SeUo5egoh_iOFa35Omh8Sji4xJDB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9MWOiJLKEJ3LFItQ7fTZZ84rwLH0CVFlbDbePoim1zUH_wQ6ILZ3Rsfxn3aaQJeHwrG9r5SfFK1ACMBd5uU9u5zHBz4u7kUxa5SmOXtTDoJ1c5t81bEEt7J06qz75Bm1gTyttxX8oC30BmEr4-3zj6qWykgFDCEJRG37FXhPRXpFo6-vcR6TTtMAjXIL0g3qsy3vFPZIm3i7LJ4mgqrXpIrDlNU9LFIc7Md1JU2JEl7lf0-C3-rqPPhTY60VOYBby_YQwGRc1iguN5yHbHOPt3y2IvWB6tN_XRDZEkDaIeQoTRGV0HnI1sOZd5wyT_5IH-RBOUBkdqjiqMtJIopyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کیف عجیب شرکت Coperni که با استفاده از کپک پرورش‌ و ساخته شده
!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/677428" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ماجرایی تلخ؛ جنگل‌های جنوب کشور در معرض نابودی قرار گرفت
نادرقلی‌ ابراهیمی، عضو کمیسیون کشاورزی و محیط‌زیست مجلس در
#گفتگو
با خبرفوری:
🔹
نفتکش‌ها معمولا بعد از بارگیری نفت در خلیج‌فارس و رساندن آن به مقصد، برای ایجاد توازن در حرکت کشتی به جای نفت، آب بارگیری می‌کنند و مجددا این آب آلوده را در خلیج‌فارس تخلیه می‌کنند.
🔹
جنگل‌های حرا که ارزشمندترین جنگل‌های ساحلی ایران در جنوب ایران محسوب می‌شوند، به همین علت در معرض تخریب و نابودی قرار گرفته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677427" target="_blank">📅 20:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb333777ee.mp4?token=PTjADOXvr6OKIEw38mu4Bucx38dMirbXsxXGG75VlldZyHCDUcZjE2iQSMGC0RIdp2S9sgZd-wBIdMKBN-CfpoY4Df2Wg-M-e8WlWTwY6KZ6sUfVtBAx1QLy_GKF3kGf5SP7yAmG049Gd3cF4xCrb9H3eMwlHTMvnbNAB-fKNH9bmV0HPJ6n_AU_rCmPiPV2GEXAn8k7b4Kj94aw8Zg2de5gcuasn4x1POiOrMxxhhOEG3JxzX0A2d_iM7lPE-5NMxMPl6SRWLMY_lPLvLftbKRGpMv9R_YksvmjG0UkQ5m1-CCWM0wEhubEGtpebAieAlXTg3sW2nLXk1Nq4UmikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb333777ee.mp4?token=PTjADOXvr6OKIEw38mu4Bucx38dMirbXsxXGG75VlldZyHCDUcZjE2iQSMGC0RIdp2S9sgZd-wBIdMKBN-CfpoY4Df2Wg-M-e8WlWTwY6KZ6sUfVtBAx1QLy_GKF3kGf5SP7yAmG049Gd3cF4xCrb9H3eMwlHTMvnbNAB-fKNH9bmV0HPJ6n_AU_rCmPiPV2GEXAn8k7b4Kj94aw8Zg2de5gcuasn4x1POiOrMxxhhOEG3JxzX0A2d_iM7lPE-5NMxMPl6SRWLMY_lPLvLftbKRGpMv9R_YksvmjG0UkQ5m1-CCWM0wEhubEGtpebAieAlXTg3sW2nLXk1Nq4UmikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگنده های آمریکایی به حریم هوایی استان نینوا در عراق نفوذ کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677426" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6JDjEOvEuRq3HropVWzQ0FHpjSR5p9Z3sVJf3oTYjoBQyXQIH4h6vZsAhPzt13uYGrVimQ3Xz0DkXGC6G5w1D7mWaTqpoTbu9pL21NUwdfITUn-8AMVQCyhQN91G81R6Y2JBIK1dbNHeYPgqfAzcidmHzGCnM7E7LXoknjsEFK9yvcoIk3wp38UI6yogunReageLL1SxKKE18zob5nxxfLhenR49YJnxj-bhz3Dcb1abtVGEch_vAKrer_ZBCZRZXJGFofGm6TU1JEhhWekjL_yUGni7FhVop3lPhrmsQFPT0PeQvm_vDl9eZ4Dx47KJdDTgZjIVbJOlBVbtDYtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
گاهی احترام به نذری، یعنی فقط به اندازه نیاز برداریم؛
شاید سهم اضافه‌ای که رد می‌کنیم، چند قدم بعد به دست زائری خسته برسد.
نعمت را هدر ندهیم؛ پشت هر وعده، نیت خیر و زحمت زیادی است.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/677425" target="_blank">📅 20:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb54cd03b6.mp4?token=YZFLhG__O7QyJgpk0va9twrIBsa3ffU7bKwxMKh6GcL98CuhKo1dpHdHMwlSzvnZFKResNl7zxrHS4TewOQvjDU2NJGd40gQrj3rp4ivokOP1K80djqgDIzUo1bPbaqlEkN8SfWjciDuKLljtdCvYL5b55WnEHMBjI35ouU01Wz4bQ5e8GkYHJJ7x3Q9HSVduuExwKB8u8ZuMRFMxIf50nVzUL2QuVIxj-bO590jDVJ5ROCEhu_tJz9NqOVIYQFXzCYQ85mAQ1w3IQpTL3N--VLihtKAYLx3aLKLbdWok9i5z8G8-_z3LP9FFw7weO3bZ1y3VwXIG4Vtk86IspA6-IT3lXXU6EhI_kM5VRXtKfRAUZtbgzzQYaZWiuFT_UEgZLVb690D3zCc3uIWoid06PRCAFAjyfWwAsUUc2Ug81aBx1WeeweGWz0HofNVkmLZTj1hRAwkZWqan9rtr2xrzP2NRZKCHeUEY0mdchYCk2plpCy243QIl02avgea-7PPviUzaosv4zWTd7yPfz4Q_9JI2GCV7iea_atPEHfLpYrn6eKLYq7m0r_MCAjNCuszY8d-KPDwaERPYqxPccI1aIfG97LHITxh1Ss0Wcju0WEIVtWC32A2EyHthYuV1tegeJ2r5PIgNCQrzrdjlpJWZsE1Zvt02tOFqf91wQX6ifE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb54cd03b6.mp4?token=YZFLhG__O7QyJgpk0va9twrIBsa3ffU7bKwxMKh6GcL98CuhKo1dpHdHMwlSzvnZFKResNl7zxrHS4TewOQvjDU2NJGd40gQrj3rp4ivokOP1K80djqgDIzUo1bPbaqlEkN8SfWjciDuKLljtdCvYL5b55WnEHMBjI35ouU01Wz4bQ5e8GkYHJJ7x3Q9HSVduuExwKB8u8ZuMRFMxIf50nVzUL2QuVIxj-bO590jDVJ5ROCEhu_tJz9NqOVIYQFXzCYQ85mAQ1w3IQpTL3N--VLihtKAYLx3aLKLbdWok9i5z8G8-_z3LP9FFw7weO3bZ1y3VwXIG4Vtk86IspA6-IT3lXXU6EhI_kM5VRXtKfRAUZtbgzzQYaZWiuFT_UEgZLVb690D3zCc3uIWoid06PRCAFAjyfWwAsUUc2Ug81aBx1WeeweGWz0HofNVkmLZTj1hRAwkZWqan9rtr2xrzP2NRZKCHeUEY0mdchYCk2plpCy243QIl02avgea-7PPviUzaosv4zWTd7yPfz4Q_9JI2GCV7iea_atPEHfLpYrn6eKLYq7m0r_MCAjNCuszY8d-KPDwaERPYqxPccI1aIfG97LHITxh1Ss0Wcju0WEIVtWC32A2EyHthYuV1tegeJ2r5PIgNCQrzrdjlpJWZsE1Zvt02tOFqf91wQX6ifE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتباطات اربعین از پشت میز بررسی نشد
🔹
این‌بار کیفیت ارتباطات اربعین نه با نمودار و گزارش، بلکه در دل جاده‌ها و میان زائران سنجیده شد... از مسیرهای منتهی به مرزهای خسروی و مهران تا جاده نجف به کربلا.
🔹
تماس‌ها برقرار می‌ماند؟ اینترنت در شلوغ‌ترین نقاط پاسخ می‌دهد؟ شبکه در لحظه‌های اوج تردد پایدار است؟ پاسخ این پرسش‌ها از همان جایی جست‌وجو شد که مردم آن را تجربه می‌کنند.
🔹
با حضور وزیر ارتباطات ۲۸۴ پروژه ارتباطی در کرمانشاه و ایلام با بیش از ۳ هزار میلیارد تومان سرمایه‌گذاری به بهره‌برداری رسید. این پروژه‌ها برای تقویت پوشش، توسعه ارتباطات روستایی، گسترش فیبر نوری و افزایش پایداری شبکه در مسیر زائران بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677424" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
‏
رسانه‌های سعودی: اردن به عراق اطلاع داده که حشدالشعبی قصد حمله به خاک اردن را دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677423" target="_blank">📅 20:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677421">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f3be03e3.mp4?token=IB6kMolEfeB0JVgQ5Hs6MGK_qNRSdJnLvRlaGXeEjv-UFCfW_5UGgqq1My99XVyxl8CHhtl7wb6EnhKiWQAmecE4CUNlaJ0qXG6NOBe6LKATZaxAyt4VcmkzTYKgCHt26y8WVt6OMwXacMUlLX7XHzZLliJCexuQJ2bdLVoQy9eJSpUurEECbk6_j_NYwljYqUdB1AkqwqZS3FPCiYpfkjLGX1bGOdhtd6f9JxYbf_bt6jSSWu0QOlWE6NNoeRTFYsPZVoy34xtxlR4a16ATfYjW3G-Oi6hWZIK-viGdu5GM1gmIAZnymm3Q-lzGxj4dnY_DAHAciLhgKY7gVsovRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f3be03e3.mp4?token=IB6kMolEfeB0JVgQ5Hs6MGK_qNRSdJnLvRlaGXeEjv-UFCfW_5UGgqq1My99XVyxl8CHhtl7wb6EnhKiWQAmecE4CUNlaJ0qXG6NOBe6LKATZaxAyt4VcmkzTYKgCHt26y8WVt6OMwXacMUlLX7XHzZLliJCexuQJ2bdLVoQy9eJSpUurEECbk6_j_NYwljYqUdB1AkqwqZS3FPCiYpfkjLGX1bGOdhtd6f9JxYbf_bt6jSSWu0QOlWE6NNoeRTFYsPZVoy34xtxlR4a16ATfYjW3G-Oi6hWZIK-viGdu5GM1gmIAZnymm3Q-lzGxj4dnY_DAHAciLhgKY7gVsovRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمامی موکب‌ها در مرز شلمچه تا یک هفته بعد از اربعین آماده خدمت‌رسانی به زوار هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677421" target="_blank">📅 20:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677420">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df190636af.mp4?token=fPYS_pOrHknXiNU3wX2O6H0gwMsjZsAiX3Kn5Fnqjk2SQfSQkB2k6VHopsq60BrW0HOKlGgw80PZZHEBodRJ-uvzqdnor9RN04EvKHZGDro-Z5YrV9W5QJZHqSRtlMh_Z1phRqKSsEK3-krAMcbKz5qJ2maPmgQuunrOstWv3aA_aR3VQKeWqFG6BfJcU_mAF2Eh0CbSSXjEMB-FKdo_gwD9w0rOSnQTlDjxbeVj-WJeZg0NCZi1REDwfVtf_cyP7BQjTlM7Oa_4KnxWO0PEL62kjqRaBwaWHRYibnEkQxMwFLEYCXndwhtKQUoZ1NEcw-gaiQ7-3Le5JTt4DIc6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df190636af.mp4?token=fPYS_pOrHknXiNU3wX2O6H0gwMsjZsAiX3Kn5Fnqjk2SQfSQkB2k6VHopsq60BrW0HOKlGgw80PZZHEBodRJ-uvzqdnor9RN04EvKHZGDro-Z5YrV9W5QJZHqSRtlMh_Z1phRqKSsEK3-krAMcbKz5qJ2maPmgQuunrOstWv3aA_aR3VQKeWqFG6BfJcU_mAF2Eh0CbSSXjEMB-FKdo_gwD9w0rOSnQTlDjxbeVj-WJeZg0NCZi1REDwfVtf_cyP7BQjTlM7Oa_4KnxWO0PEL62kjqRaBwaWHRYibnEkQxMwFLEYCXndwhtKQUoZ1NEcw-gaiQ7-3Le5JTt4DIc6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جالبه بدونین ۱۰۰ کالری از هر ماده غذایی چقدر میشه
؟
🔹
رژیم گرفتن راحته فقط کافیه کالری هر مواد غذایی و خوراکی رو بدونید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/677420" target="_blank">📅 20:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677419">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هر ۱۰۰ درصد رشدِ دلار، ۱۲۱ درصد خودرو را گران می‌کند
🔹
نتایج یک پژوهش با استفاده از مدل ARDL نشان می‌دهد در بازه زمانی ۱۳۹۲ تا ۱۴۰۳، نرخ ارز مهم‌ترین عامل اثرگذار بر قیمت خودروهای داخلی در بازار بوده است.
🔹
بر اساس این تحقیق، ضریب اثرگذاری نرخ ارز بر قیمت بازار خودرو ۱.۲۱ برآورد شده است. یعنی به ازای هر ۱۰۰ درصد افزایش نرخ ارز، قیمت خودرو در بازار به طور میانگین ۱۲۱ درصد افزایش پیدا کرده است.
🔹
افزایش ۱۰۰ درصدی قیمت مصوب خودرو هم تنها حدود ۳۲ درصد قیمت بازار خودرو را افزایش داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/677419" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677418">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=f8LyPd5ytM3FO_yXncLRXFcMWKNpBSRkEuU7zCNKsSVncfIRdNOC_xGb0YVJWWgoFcidA507eOwmKsM3QobB8rWfIqQYNBl0sy6YJFXeEzgTEHBBBDiqsdqj4aVwA0jnJQzZkkIEkdtS48EdBPGDTqhx-w8mmA6TQ3p1lXQ2w36pYiGpL7W5XLwLXmD56Mn8UTkttrCYMLAR_1CM6hLUWdABotSRFKRU7_BRa81CFJQ-rMINL22M16neGFzzbgY-mBKhbYlldOHoHIofpBS5SXhBAqdbVCgLObTjMtVm6gRzUbDgXnG3zYMw1vFzCGxJQ87idCkmc4p2DI_8yGbQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=f8LyPd5ytM3FO_yXncLRXFcMWKNpBSRkEuU7zCNKsSVncfIRdNOC_xGb0YVJWWgoFcidA507eOwmKsM3QobB8rWfIqQYNBl0sy6YJFXeEzgTEHBBBDiqsdqj4aVwA0jnJQzZkkIEkdtS48EdBPGDTqhx-w8mmA6TQ3p1lXQ2w36pYiGpL7W5XLwLXmD56Mn8UTkttrCYMLAR_1CM6hLUWdABotSRFKRU7_BRa81CFJQ-rMINL22M16neGFzzbgY-mBKhbYlldOHoHIofpBS5SXhBAqdbVCgLObTjMtVm6gRzUbDgXnG3zYMw1vFzCGxJQ87idCkmc4p2DI_8yGbQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز ژاپن و آمریکا بالاترین سطح والیبال جهان رو بازی کردن
🔹
این وسط در ست پنجم یکی از عجیب‌ترین رالی‌های تاریخ والیبال هم رقم خورد
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/677418" target="_blank">📅 20:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677417">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAr5LSwvpCBTEjAEA3uxnA-5mCuq8raIKjv8rx1oKccfU9rKbIjyq48_iXT_mnzS3Z7BX5mH95eDNU3ZEAA9eHyaS2oSnr4LL4D6m2HkssQO-9M6BxjXv5CMqFXIWxMj8fgAGFnniKvHgBc6AeKXhkUe7h2Ah0m7_STAuBWF7PxiBNS8LmQD6o2kRS8Ki-GRMecDdBda3sqGDQdIZkbyJa6jGNpocJQuRNacb1NxNUQDgURB6BMx6TCTv0QdfBKJeJ0g0Z75SJINOIJ7Gw1De8PMsAjstLg4V-MaNp6kiUvvdVkQF9hhbpCHTH18wV6PVhIeq3QUqFTqhjCocPRJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فضه سادات حسینی، مجری تلویزیون پس از سفر به کربلا: داشتن ایران قوی هم مصداق خون‌خواهی رهبر شهید است؛ زمینه‌ساز ظهور شویم
🔹
حسینی درباره سفر زیارتی اربعین همراه با کاروان اهالی هنر و رسانه: این فضایی که عده‌ای از فیلمسازان، مجریان و برنامه‌سازان در کنار هم قرار گرفته‌اند، می‌تواند خروجی‌های بسیار خوبی برای اربعین داشته باشد. من چند بار دیگر هم توفیق داشتم که با بچه‌های رسانه به اربعین بیایم.
🔹
شاید در شرایط عادی در تهران نتوانم این تعداد مدیر فرهنگی، مدیر سینمایی و افراد مختلف را یکجا ببینم، اما اینجا می‌شود ارتباطات زیادی برقرار کرد. اگر کسی طرح، ایده یا نکته‌ای داشته باشد، می‌تواند از این طریق مسائلش را پیش ببرد، کار کند و نکاتش را بگوید. مثلاً بگوید من ایده برنامه‌سازی دارم یا ایده فلان کار را دارم.
🔹
حضور در چنین کاروانی موجب هم‌افزایی، همبستگی و ارتباط است. غیر از اینکه خودمان می‌توانیم تولید محتوای شخصی انجام دهیم، می‌شود با افراد مختلف، مدیران، خبرنگاران و برنامه‌سازان ارتباط گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/677417" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPlU-SDlsS2S210Qzuqk2STllryqZsBT5-njddhXa4-xxhi6ziszu4TOVZVKSa746nmFOOtaQu8FS5m1GeyALZVZ8GFrEVpTS-6b9KUvcjMJuIISV5Hkl9k2i5Pf1Jpu3KScMHsBGK5NzqDL75EobnL7f-4sizKZn6MKNZAsLC4KG-nhNxLDQf5qd3Jnl9k1aKbZCZfpUMZ42zV9AR6cR1nSEx5mVLT8f_ZpFMp0S_59YGgwmwInthBIfYDR_2u6t482AbyhV4D7wmeWjcvpgvt6U8nStPqXFJbruAuDfpKIZNuK9ZuGcfCSKS7MmFzafGn_5XX1ensLcuFQNdSxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت عجیب کاخ سفید: خداوند سربازان ما را حفظ کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/677416" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303ffade53.mp4?token=v2gO57Mqixhd3eZOlQxr3TRfniVwcw0njYIs3_7EZmJ_nx-iISW9JV72gKttIZ77rlGXrsdPksI1UQcMXCK8OsmsagIGIDOcj0zrA2qv7G-PQz23NF-RZ2VcytZCPDHwpMwW6_PvnfFMe9C0o_DhNlS6SiE2cBYXVcMGKxvrYT-btKom1-3PjSQfE4-W86vlkUx508ZDN0lvdg5a475iOLYiL0tO2v-PtvrZG0r9aL3oW85Y5gMrG3ezq-pb-9HO-l0zaw3L2fVt_p22r5jHtx5DlzwdI8rrKQxuYdFuwvXfyx4-6txBnhrQ2XPmaD7Axaj9pJIdUwSXNMTBEmcJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303ffade53.mp4?token=v2gO57Mqixhd3eZOlQxr3TRfniVwcw0njYIs3_7EZmJ_nx-iISW9JV72gKttIZ77rlGXrsdPksI1UQcMXCK8OsmsagIGIDOcj0zrA2qv7G-PQz23NF-RZ2VcytZCPDHwpMwW6_PvnfFMe9C0o_DhNlS6SiE2cBYXVcMGKxvrYT-btKom1-3PjSQfE4-W86vlkUx508ZDN0lvdg5a475iOLYiL0tO2v-PtvrZG0r9aL3oW85Y5gMrG3ezq-pb-9HO-l0zaw3L2fVt_p22r5jHtx5DlzwdI8rrKQxuYdFuwvXfyx4-6txBnhrQ2XPmaD7Axaj9pJIdUwSXNMTBEmcJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتی قبل در پی آتش سوزی گسترده در یک پالایشگاه نفت در اربیل، فعالیت این پالایشگاه متوقف شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677415" target="_blank">📅 20:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbD_qEpumLkSdCdS4gUECY2-jzKPs3Sr-DtujQjZVpadj3fdOittH-x7kOlwN3K686rB6iGn2NPAkWF9GvrGf5Mt40Y7UBnxeGB1MdqC51KfCQAqVDFjIOlKl7QzdUB4yGcfWLhtGVVHvshYffBSB-vQ9xrqNmTto-fF-HeDVchR6qb_JJImzULzpjKe3in_LItlpfkk38zNp5LlB_sMqKV8PzMnGsOxEqr1JjmrvlAvMuOsXxHMgeJwIAde_1cjRmLnql1-CXiqhsB-vsdsZnJPQ2BdpQiV-DtxJBmVIk3gJX6tfOOdBKl2ECP90M3757fgqRCAXT38mr-pMI5BPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/677414" target="_blank">📅 20:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9177878898.mp4?token=q9kl9syR4ebzfNU-D8Znw0PFYB5x7k_FHow0Xt_70235WAwsW3SNMuCBtiL0Ow3gVv9NCXDttZgOEjOM6VIfqS52ITmNT8fBogyHBHK0c77SF2UJtH7LYCIsFEQKAs6-M0PHT5lyN3bMZjjayGqdb4a_mitBg3ZcSpLALdCTSUFxUW6j0zhA296pQPFUJ4MCg5kjheUYwUsWSt8ebRJwuPkI1YGpXNZLLa_sbZknDXeGFDYUn_Y7wIUICixQvPr0UatsoWtWrPBpMXN7kDMWnKYYf10I2RV5WIEcQyuFkpiUwThwXT8MPPDXa7ZDtHRYmkKcC6FPfXU67eqRmc2WMpfNhmX5UeSfZFY9HZd7CQzwIyy0p7hqs1rI2toZGSQwW6b5kFIMU77zfArKfh75JSzj03XykTa6dyRYRiAitMnl18gGvbxf7sdCNyoNqt1Ti-BWcm_ExHmNnlp2jSxqYefny4zW_Drj7bVKgRqqfez21IwP2iSxAt0k87KZ-B4gK07-nvMoR4Kxc8rlmCfGLfa3bEaUwWo3Yr6dtNdRA_p4V3gXUJYdNPPPg-kJLrdO1rq8ZS0SKbp9AaPnNck7IJtQsVi6_SJ994OmUAHO_anezJAH2MkoeqOJgkWeW4bKMJUA3_lWMKxvKMgam2hrdZd_OXOHvm2THLH5I_aiWFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9177878898.mp4?token=q9kl9syR4ebzfNU-D8Znw0PFYB5x7k_FHow0Xt_70235WAwsW3SNMuCBtiL0Ow3gVv9NCXDttZgOEjOM6VIfqS52ITmNT8fBogyHBHK0c77SF2UJtH7LYCIsFEQKAs6-M0PHT5lyN3bMZjjayGqdb4a_mitBg3ZcSpLALdCTSUFxUW6j0zhA296pQPFUJ4MCg5kjheUYwUsWSt8ebRJwuPkI1YGpXNZLLa_sbZknDXeGFDYUn_Y7wIUICixQvPr0UatsoWtWrPBpMXN7kDMWnKYYf10I2RV5WIEcQyuFkpiUwThwXT8MPPDXa7ZDtHRYmkKcC6FPfXU67eqRmc2WMpfNhmX5UeSfZFY9HZd7CQzwIyy0p7hqs1rI2toZGSQwW6b5kFIMU77zfArKfh75JSzj03XykTa6dyRYRiAitMnl18gGvbxf7sdCNyoNqt1Ti-BWcm_ExHmNnlp2jSxqYefny4zW_Drj7bVKgRqqfez21IwP2iSxAt0k87KZ-B4gK07-nvMoR4Kxc8rlmCfGLfa3bEaUwWo3Yr6dtNdRA_p4V3gXUJYdNPPPg-kJLrdO1rq8ZS0SKbp9AaPnNck7IJtQsVi6_SJ994OmUAHO_anezJAH2MkoeqOJgkWeW4bKMJUA3_lWMKxvKMgam2hrdZd_OXOHvm2THLH5I_aiWFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که خوک هار دقایقی قبل از حضور در یک پایگاه نظامی در نیوجرسی منتشر کرد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677413" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677411">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4WnQdJho5tuh8QvAS0OYa38FbhC4E1nvH4JV9P4qg7UdQPgTjEbQg4O0xvbMDCNxIGhcquiAB8zja5YdrWLlFgxZUtRJsPyeIAf0V9bIoB_Az_8fz3z4kicNTBAeIXe1QH6RQREa1gy8-TNo3ciFWYF0FX3hcE8yV9TEWtFAlcK0nz-EVuVtcpEl-TYl8aLkdYzinF_oD57klztkn3KbAoxESKTKjqXajL17d_RG6Luyn8juuLwyOk4NlfuKLnak4crVAGEO3fLmK6VXa6hZMumUUnzUFg4ZJ1g9f1JoAJK0anOjzEwIQu-DIWWuieQDFqFOyc7ePyoby37QsejZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoTXfOL3DJ1Qx3pLxPylQgmZfZLvvZoRRgGtp5eQjMF0_JVXNI9y9ctsaZrdvA8OKEKyFbYCfYvfaiaXKxqUw7N8I-7gwhsUkR7UHflO_ETNX28DXul7r_pAIIfvZUHDN4eRpny5K761b8ZBuFEKvy2CgFXsYAYQJjEO4rbLBACIV71aTjgc7V6RGydv-mx32DGtKKUw7-_anIZdTTcD2A5tI2hIacra58aWcnJ1K2dPpXDAWovOECxXtV1y5axnFpfS3_2eJ5SSoqFmic1dyQWFrMOkjaG5OWv7dNoMJjJj8vz7g9jcpJN1MXzrfKggwkErmzZpn8vYXyXIGDAu5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بعضی خانواده‌ها گذشته‌شان را زندگی نمی‌کنند؛ بارها و بارها تکرارش می‌کنند
🔹
«صد سال تنهایی» داستان خاندان بوئندیاست؛ نسلی گرفتار عشق، قدرت، جنگ، فراموشی و تنهایی در شهر افسانه‌ای ماکوندو.مارکز در این رمان، واقعیت و خیال را چنان درهم می‌آمیزد که عجیب‌ترین اتفاق‌ها کاملاً طبیعی به نظر می‌رسند.
🔹
کتابی برای کسانی که دوست دارند در یک جهان جادویی گم شوند و بعد از تمام‌شدنش، مدت‌ها به سرنوشت آدم‌هایش فکر کنند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677411" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677410">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7c9bf91d.mp4?token=YSPAu9l5kR8TvD6PNMiMwWY2rNC6dj9sOWMbniaFAvmXULHX9rO6vy606Vb9uZXSQUBKMvS4iOyf6ZROsrMvabskmNQU_Fy8hXZyRlDiEQaAbm8TjZo0O36XjCoA82ac5gyYGcBE6JnKgKte2XQSzX1osFT1A60RFlrZPcsGt-iwKHdyhdOUGa96yk9LyMac38vznD4ULuiVDShI19WUeKonkz6ye1ago1NeaVkI4CWiZ715fSLWjy2ewf2Nf0kVpfgR7g4gS6VL-byT1nCc1U9J87sf-Q9TK2oa63oF6QrlLKBaKqg5i3wg1vJ5BRoSfsFkjPYcIMwF6SydGRqb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7c9bf91d.mp4?token=YSPAu9l5kR8TvD6PNMiMwWY2rNC6dj9sOWMbniaFAvmXULHX9rO6vy606Vb9uZXSQUBKMvS4iOyf6ZROsrMvabskmNQU_Fy8hXZyRlDiEQaAbm8TjZo0O36XjCoA82ac5gyYGcBE6JnKgKte2XQSzX1osFT1A60RFlrZPcsGt-iwKHdyhdOUGa96yk9LyMac38vznD4ULuiVDShI19WUeKonkz6ye1ago1NeaVkI4CWiZ715fSLWjy2ewf2Nf0kVpfgR7g4gS6VL-byT1nCc1U9J87sf-Q9TK2oa63oF6QrlLKBaKqg5i3wg1vJ5BRoSfsFkjPYcIMwF6SydGRqb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها: این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677410" target="_blank">📅 20:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677409">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f18f8b8e2.mp4?token=o2RZogi2nl1JgzJRAQ48JON8S0S0Kv2JyAHxlY_3bp2VXPXbVUF6RPoTDA-MJeeVUvh-WolATXDosW_XdejJts5eKGrfn37Qjj_fRg2kcYCqSuMt2cACkqiXxa3TzqCBlpUKTFUt5jO1O8p8eRLhZRvIHVaJsRgPsQoxDEvtCvmZey0rL1lKIe2TDqWePTcGpW48hC5ZKdS8yYikUZPGyIws1R1kD4OTcS43ML5B40ijWXpQ4o7-wCaQDDEETEpOWtmNNzOU755RrrkyLKLDTM54xAK9r772IeYuXUIbqp7m5RmM84us7zXgLhyd4wPWvKR5LIn7pKqEsi3I4mEQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f18f8b8e2.mp4?token=o2RZogi2nl1JgzJRAQ48JON8S0S0Kv2JyAHxlY_3bp2VXPXbVUF6RPoTDA-MJeeVUvh-WolATXDosW_XdejJts5eKGrfn37Qjj_fRg2kcYCqSuMt2cACkqiXxa3TzqCBlpUKTFUt5jO1O8p8eRLhZRvIHVaJsRgPsQoxDEvtCvmZey0rL1lKIe2TDqWePTcGpW48hC5ZKdS8yYikUZPGyIws1R1kD4OTcS43ML5B40ijWXpQ4o7-wCaQDDEETEpOWtmNNzOU755RrrkyLKLDTM54xAK9r772IeYuXUIbqp7m5RmM84us7zXgLhyd4wPWvKR5LIn7pKqEsi3I4mEQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس نظامی عرب‌زبان: رادارهای اسرائیل توانایی مقابله با همه موشک‌ها و پهپادهای ایران را ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677409" target="_blank">📅 19:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd2Ldkd_eoEO-JJE5opZff0SItmS9b4ApLMP4WqR-8r2jm13JNE2n2i--Uw36A-LfQsgAAI9WCEipMG-w6hFoaPsDnzGLdIMVKlfrVSOKTw1m9MKlDKw9Amn7nT52ix4IlqMXbTHzKDwcFUmiHaR1QZnRHOrJOG7YkmUnazGe7qbivoMQBlh3urNaeMBOihiAfQrpA1PJE1JNnx4a2A1w1NWC7y99qqCt5LgltDSwDyhRKG0LHNm443Fcw3ROanA88uGPSe2PCjvv_rU3KP-40j9qeJi4vG8WAsRftuKNdDQUI7gXzprEDd-54jLmTpK_v-RnfhMb4rdq2PuWKln8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از رهبر شهید در مسیر اربعین
🔹
اگر در مسیر اربعین هستید و یادی از رهبر شهید در دل دارید، یک پیام صوتی حداکثر ۱۵ ثانیه ای برای خبرفوری ارسال کنید تا صدای ارادت شما نیز در این مسیر ماندگار شود.
🔹
در پیام صوتی خود این جمله را بیان کنید:
«من ... هستم از ... و در این مسیر به نیابت از رهبر شهید قدم برمی‌دارم.»
🔹
منتخبی از پیام های صوتی شما در خبرفوری منتشر خواهد شد.
🔸
پیام صوتی  خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/677406" target="_blank">📅 19:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677405">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=gAAWxPuIrxyL5Rn9p9c1kXDkL3x8207P1sdfcKF4wDSpz6yG4UgnRAd7U9sIo8A7eVif6Msbud7kD2GRmMg0CxQLmDL1FFOMm68-RwmnZAAboxnNN0zSZ6kFqGQ5cmqnpzR7FWZZDm8RkU4VHCzVllx9i0CbGEkXJHUOtDSsP5hsVQN0uFWZKbV1RsyNtLJ-Ve1E60sUrGVUJQN5IVnavVSr3fDVqSD4LL6avaUBLSTRpxePd0LbSvblwYIfBgDqff2rWewiF4jvgJDbZHFzb4ohszhq_47MQOdsbCUu3tu2yfH2BQ0DwPkntamng2IPy7Gn0eldoKdkUDbJ0gHzng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6e2dece.mp4?token=gAAWxPuIrxyL5Rn9p9c1kXDkL3x8207P1sdfcKF4wDSpz6yG4UgnRAd7U9sIo8A7eVif6Msbud7kD2GRmMg0CxQLmDL1FFOMm68-RwmnZAAboxnNN0zSZ6kFqGQ5cmqnpzR7FWZZDm8RkU4VHCzVllx9i0CbGEkXJHUOtDSsP5hsVQN0uFWZKbV1RsyNtLJ-Ve1E60sUrGVUJQN5IVnavVSr3fDVqSD4LL6avaUBLSTRpxePd0LbSvblwYIfBgDqff2rWewiF4jvgJDbZHFzb4ohszhq_47MQOdsbCUu3tu2yfH2BQ0DwPkntamng2IPy7Gn0eldoKdkUDbJ0gHzng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آتش‌سوزی در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/677405" target="_blank">📅 19:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677404">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4318LgV6mmqxwsc0VA3XWJaBUBaJhLotHVz3abfxFdCpXEN7wnmupaklWrTqzFNcMoLE_Dx8xf-7fHi058Lu1IjrB3c2-0JAm9J3wrOlv-FMQEpvJt0yo-2aVQQ7RSfzTAaUAgtJN1HD9PiNlSI1e8ozyqmk721bG291XSuRSRRzIlkBjHd86EqFTCgWth4gwMRHIVL0MJOHadLZpT-NvHd2cYzFC4l6q6zGBz5Po0W4VSOHJAPGCo6hAITr-_WaG5dw__t-oO7odPvCgyNE0j3AXQaD8PQKzrKZlQ_nPfDhcBlDiLEbCiNP7aexhl68_BlQhc_o5pOJvrWq10zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاکس‌نیوز هم کم کم علیه ترامپ شد
گاردین:
🔹
کانال خبری کابلی مورد علاقه ترامپ در حال مقابله با جنگ او علیه ایران است. مجریان برجسته فاکس نیوز نگرانی، سردرگمی و ناامیدی خود را در مورد اهداف ایالات متحده در ایران ابراز کرده‌اند.
🔹
این موضوع نشان می‌دهد ترامپ در دنیای رسانه‌های محافظه‌کاری که به حمایت آنها متکی است، به طور فزاینده‌ای در موقعیت خطرناکی قرار دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677404" target="_blank">📅 19:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677403">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
محمد مرندی در مناظره با وکیل آمریکایی در برنامه پیرس مورگان: ده‌ها میلیون نفر از مردم ایران برای تشییع رهبر شهید به خیابان‌ها آمدند؛ خبرنگاران بین‌المللی آنجا بودند؛ نه فقط در ایران، بلکه در عراق هم همینطور. مردم ایران نشان داده‌اند در کنار چه کسی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/677403" target="_blank">📅 19:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_9r_VJEht4_3hzwBKZIthvj9IBfxEhqUnoWJqqYGI5pUXXzaiRRyYFxTXm7JP740BGtHc1nbemkPkEuESy2duCQZISz33E_IWzaVpTa0yJaGnkvNuOPE-inbBlJzclI4htAQRQc9h6243CJ2i1pCPK6cHnkqznJ_OWpVkkmbVjcRblhPTQ6ASgF0VC_Ruvje03XISCDm8jq4ze-TaXe4G4ypplQayy6OI7PPUdA4neRbbqFt3hiStt1cdHcwWQJV2E4gnWVw569bdIXkaXGnOYqWvIItqa4AhpvQZvqUBvV-8Kbu_JfSFXrEIzha-hwTv671xEl6w2iDny9F1EmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
همین الان راهی کربلا شو
‼️
▫️
همین حالا با ارسال عدد «۲» به
۳۰۰۰۱۱۵۲
در پویش «زیارت به نیابت» ثبت نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677400" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA8i4kZz7DmH9jh4VPMiHJwwEx052Ts9hTeB8prRQFb1_FD5UEhb9tMIPie1sZL8_o4DizQVaHs8aP1htaKth5qvT3Kf650nEbbfSTM5BO5uRrPTsz-RGiF3AXnWhgrVFG80bIBzapE4ZmaUw8-33PWvwJOnxTXC1boIQPVt8mI87jPAhsonSQomjciQY2cO09XP7GRNJkSsLhN8ew0znELl6egxEf_qNnKukanIRkdW41WEpJWWwCMNlECPbBipy-aoaS7hOf2dppoAI2lT4_2J1bPfEOf5UOXcxZqodMdldm4qrg9bXC7AT4i8iUWHu2RJ0IvzMQQiXug3A-XMdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنان بیش از مردان زمان خود را در رسانه‌های اجتماعی صرف می‌کنند
🔹
برآورد افکارسنجی بین‌المللی سازمان همکاری و توسعه اقتصادی نشان می‌دهد میانگین ساعات هفتگی استفاده از رسانه‌های اجتماعی توسط دانش‌آموزان دختر ۱۵ ساله بیش از دانش‌آموزان پسر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677399" target="_blank">📅 19:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a17e0d29.mp4?token=cvxkOz-h4Ja-QzbTbwTqJ6pTJr07XUiI6oBCk1QhJZNKWiYo-CbNfCEkZgRQ216o9N6Z5KscpZ07W0ntCs1FLhacnPE0jx1dIM3ycjP9_gb6LjF8VpDEvZohX-PLNX8awII7ROCABHXROcHKx96nXWy6gSnKCe6jOn1npgZX12JXLrmIZlklhKyBPzdBweqwzhEL0o0i_6jgggOK7i-8-CPhxaXoV3rCnTWNk1L18j6RQqvkaZNGnXObwmK7FAMOxlVvM6ObOSKeUE8v2L5JkQTfGYv6EqtklChAZpWM0Z75ElKx8zgHVwbLznoNdVvkRYQ7mDHbV9bVmW-DbIVk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a17e0d29.mp4?token=cvxkOz-h4Ja-QzbTbwTqJ6pTJr07XUiI6oBCk1QhJZNKWiYo-CbNfCEkZgRQ216o9N6Z5KscpZ07W0ntCs1FLhacnPE0jx1dIM3ycjP9_gb6LjF8VpDEvZohX-PLNX8awII7ROCABHXROcHKx96nXWy6gSnKCe6jOn1npgZX12JXLrmIZlklhKyBPzdBweqwzhEL0o0i_6jgggOK7i-8-CPhxaXoV3rCnTWNk1L18j6RQqvkaZNGnXObwmK7FAMOxlVvM6ObOSKeUE8v2L5JkQTfGYv6EqtklChAZpWM0Z75ElKx8zgHVwbLznoNdVvkRYQ7mDHbV9bVmW-DbIVk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام علی(ع):
شجاع باشید!
مرگ یکــبـار
به سراغتان می‌آید./</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/677398" target="_blank">📅 19:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec6418750.mp4?token=qPkjlVBTVFGI2MbrF21UQjbKyUEeVjfhl25X0V-SmIIg_kvxvSoTvyhZALF4h6pYqlrZpY3pkeQ_u3tb-4UUqKCOkWnt1Y5Qjx1ShaChnMaWzOdcfyoh6zKoNI5Ss_OsXRJkpLzQOJIC-V8gUM5KWr4TvwKlC8WoatR0y5E9WHd5N6wRwQs5pFSBHjqjHJ50nzq_bxZv87j7h_Bn0fWwwyiQHVpYMXRdbjLcSZ4e_Oo15hj5CLChFXQfQn7Qwic8N79si7cawIK5Pq04d2EUmooHBSU4k13ybZEHXWc2xZnBOpV9oMY7puwcoqanYBBtYxZG08IM6zgY5EmHBAZw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec6418750.mp4?token=qPkjlVBTVFGI2MbrF21UQjbKyUEeVjfhl25X0V-SmIIg_kvxvSoTvyhZALF4h6pYqlrZpY3pkeQ_u3tb-4UUqKCOkWnt1Y5Qjx1ShaChnMaWzOdcfyoh6zKoNI5Ss_OsXRJkpLzQOJIC-V8gUM5KWr4TvwKlC8WoatR0y5E9WHd5N6wRwQs5pFSBHjqjHJ50nzq_bxZv87j7h_Bn0fWwwyiQHVpYMXRdbjLcSZ4e_Oo15hj5CLChFXQfQn7Qwic8N79si7cawIK5Pq04d2EUmooHBSU4k13ybZEHXWc2xZnBOpV9oMY7puwcoqanYBBtYxZG08IM6zgY5EmHBAZw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پذیرایی متفاوت از مردم چین در تابستان
🔹
ایستگاه‌های مترو در چین، کولر گازی‌ها را روشن کردند و در گرمای تابستان از مردم به این شیوه پذیرایی می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/677396" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677395">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفردای اقتصاد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc021471e1.mp4?token=Zc0nG3NvZtmtD-KV9dJ4cR90Z1ZBf5roC1sbP4S_yM6sJCRqWEcnOVskoUpwo3wLVrPjEl4PyMqpdtE-v248D25etOtHXd-EFNj2pd-C570olg0kJSgqydzJajofvenN1Wceca6nypbhH7XmH4BGadd1PvmG447-ycp8L-cUoeJhDcoETPtoNO4Bnspz1bjuH9bfRZ54ryVkcTblCE7jD4twtTRBJikv9ciCJlsSBhb83264DJoB1iOlmNtnFzJw_9cTWRUgg9ZOyk_3VfVNbIAG49heKtPSWSnQUPCwaWjFAwSZT2dhkmfBYkzZG8y1cCl3WcJ4WJhNDuDbAaBzIUjwIb38q_oU0doITIuAkOZ-ZUqEOLLQrSsUAh--_ArMcE2Asxo66tqbmRIn4OPAXz2Lsu5S8YSeNXaeTfPEF726KTwdoyTak3hGmzwZyh4dJ8AZAVQEpCWJ7n4ooFb4LYNQ_FfqvEeCk3x7xASMvF63PgZnhRcANnqT2XjLyM2HFqeoM9rlwwf0s4EAqvRs332daroUF-KTT21GB9D7iQ0cMjqNOEtGaPMljr2fEKI1HCdGGrYI4vmiOI7vQxhui8cgg1O5OxU8UtQoa3Q6NnBmyMaALF7_LNNWPcTjo9ftUBY433rOE4qYf73gidm6OiFTLY9IPa-kkuuFxXSpqt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc021471e1.mp4?token=Zc0nG3NvZtmtD-KV9dJ4cR90Z1ZBf5roC1sbP4S_yM6sJCRqWEcnOVskoUpwo3wLVrPjEl4PyMqpdtE-v248D25etOtHXd-EFNj2pd-C570olg0kJSgqydzJajofvenN1Wceca6nypbhH7XmH4BGadd1PvmG447-ycp8L-cUoeJhDcoETPtoNO4Bnspz1bjuH9bfRZ54ryVkcTblCE7jD4twtTRBJikv9ciCJlsSBhb83264DJoB1iOlmNtnFzJw_9cTWRUgg9ZOyk_3VfVNbIAG49heKtPSWSnQUPCwaWjFAwSZT2dhkmfBYkzZG8y1cCl3WcJ4WJhNDuDbAaBzIUjwIb38q_oU0doITIuAkOZ-ZUqEOLLQrSsUAh--_ArMcE2Asxo66tqbmRIn4OPAXz2Lsu5S8YSeNXaeTfPEF726KTwdoyTak3hGmzwZyh4dJ8AZAVQEpCWJ7n4ooFb4LYNQ_FfqvEeCk3x7xASMvF63PgZnhRcANnqT2XjLyM2HFqeoM9rlwwf0s4EAqvRs332daroUF-KTT21GB9D7iQ0cMjqNOEtGaPMljr2fEKI1HCdGGrYI4vmiOI7vQxhui8cgg1O5OxU8UtQoa3Q6NnBmyMaALF7_LNNWPcTjo9ftUBY433rOE4qYf73gidm6OiFTLY9IPa-kkuuFxXSpqt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز و فردای رمزارزها در ایران با علی خویی، مدیرعامل نوبیتکس
◽️
بازار رمزارز ایران چه وضعیتی دارد؟
◽️
بزرگ‌ترین بحران امنیتی صنعت رمزارز ایران چگونه مدیریت شد؟
◽️
تحریم‌ پلتفرم‌های رمزارزی چقدر دارایی کاربران ایرانی‌ را در معرض خطر قرار داده است؟
◽️
چرا رگولاتوری همچنان بزرگ‌ترین مانع رشد کریپتو در ایران است؟
◽️
درس‌های  ETFهای بیت‌کوین برای اقتصاد ایران
◽️
نوبیتکس؛ چگونه به  زیرساخت مدیریت دارایی‌های دیجیتال تبدیل می‌شود؟⁨
🔗
مشاهده برنامه کامل در وبسایت
🔗
مشاهده برنامه در آپارات
🔗
مشاهده برنامه در یوتیوب
#فردای‌_کریپتو
◻️
رسانه تصویری فردای اقتصاد
⬇️
@Feghtesad</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677395" target="_blank">📅 19:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677394">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSmzBAT8k3jwZrzD3S14RCe5tQt3_WQFSzYsxZRa9slOEGkHWvwCBEwZnh-J0c_lSMRlpYFn3AiOCSHGWrsK4vBXFCWUrbkFIWqdU_mFKmTRWMBhoJL4IocPgIX9w6bR4NC9JKDI6uHiOCIErUTef5ijGPiZuE3OR-wozgrbkm9RYmhbCnl4CuA1THQD8sVtBNMpVFH0hW9OxvNyNWmoN4XMAia_nE08lE_HYiKTJ_nvqtqc2QM1gmIaynxFFJvAc_MMMJeju1lYgCRW3ClBYNCutQDc4IvedZyr6QmKsjLnt87vV_isUmhQLTpVoTk3oEd_AduV-iUd7Qfp_4cRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف کتیبه سنگی در دبیرستان انوشیروان دادگر تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677394" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a6164b25.mp4?token=e2wJeQOVaY5VFTK8oppt0tqgzYpxUuvS9fiQmByqC7cuaU-OHmRfcR1RxzB-Qtq7BOSjGeSDjYUR7vqAfWFRgvNTo74NQEjtkpb2zankwGCFvdirAJeg8XkqmWVyIPpIaY72W8J2UaaVmyWVwqa3OBl8ow8ycNvTyYPYYafCh0v-jWstUI4VjudnwlQ46oEXhL56Ds_03wZWwwC6_LbABEv_AztEptNNkcQoPE2jLUBfIrHyuo0JXLQmOSZBmDf3g-ObGVjFCY2iXUKNRYUHtB1I6RNwSQ84SoN_Gu756v105BDEpAFB_FBVgqSFBbkwq8iBj0U3RXk2aYYaGDu5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a6164b25.mp4?token=e2wJeQOVaY5VFTK8oppt0tqgzYpxUuvS9fiQmByqC7cuaU-OHmRfcR1RxzB-Qtq7BOSjGeSDjYUR7vqAfWFRgvNTo74NQEjtkpb2zankwGCFvdirAJeg8XkqmWVyIPpIaY72W8J2UaaVmyWVwqa3OBl8ow8ycNvTyYPYYafCh0v-jWstUI4VjudnwlQ46oEXhL56Ds_03wZWwwC6_LbABEv_AztEptNNkcQoPE2jLUBfIrHyuo0JXLQmOSZBmDf3g-ObGVjFCY2iXUKNRYUHtB1I6RNwSQ84SoN_Gu756v105BDEpAFB_FBVgqSFBbkwq8iBj0U3RXk2aYYaGDu5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاشیدن اسپری فلفل بر صورت کارگران فلسطینی از سوی صهیونیست‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677393" target="_blank">📅 19:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حاکم بحرین خطاب به ایران: حضرت محمد(ص) پس‌از قرن‌ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگر به بحرین حمله نکنید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677392" target="_blank">📅 19:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تولید صنعت طلای کشور در یک سال ۴۵ درصد کم شد
نادر بذرافشان، رئیس اتحادیه فروشندگان و سازندگان طلا و جواهر تهران در
#گفتگو
با خبرفوری:
🔹
رواج خرید و فروش طلای دست دوم و طلای آب شده، در کنار افزایش قیمت جهانی و داخلی طلا باعث شده تولید صنعت طلا در کشور طی یک سال گذشته ۴۵ درصد کاهش پیدا کند.
🔹
ادامه این روند باعث شده برخی واحدهای تولیدی با یک سوم ظرفیت فعالیت کنند و تعدادی نیز به دلیل افزایش هزینه‌های جاری و کاهش تقاضا تعطیل شوند. فروش طلای دست دوم و طلای آب شده به بحرانی برای صنعت طلا تبدیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677391" target="_blank">📅 19:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJsZ52TskB6aNsE4UsyrQrwu_IFl5LAnhpASb_juE51PZzj8HGpBlPDHm4TkWr2JF_1AWQ1Rpmuq_3EFEeHDhklqaojjcf_3Kg9Xm3iA7GHd4rybmZpJkyojGpqbSl7AIxXkJUEvNujhojhU7Czch8GRcdRfKx5cZzO9b7YJAe1Q6k21y4cdwYuhQB-pfuq9zNgMMgCS8T0cu8qj07pouOlAhF5-u7W92Km_FhqBGWvvP6ObKHl3bMqW0iGXYlCYJbMk-dZr7VCPPrq8QfBDI0PrHDP6WCsyTL9K2VY6s0RZA8y3wnDBLU568yRk4ocVsphK101eVFH5vx_npz2HEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
لبخند سفیدتر، اعتمادبه‌نفس بیشتر!
🔥
سرم سفیدکننده دندان LANBENA
✔️
کمک به کاهش لکه‌های ناشی از چای، قهوه و سیگار
✔️
استفاده آسان در منزل
✔️
کمک به تمیزتر و درخشان‌تر دیده شدن دندان‌ها
✅
روش استفاده:
بعد از مسواک، دندان‌ها رو خشک کن؛ ۱–۲ قطره روی گوش‌پاک‌کن/برس بزن و فقط روی سطح دندان بمال (با لثه تماس نداشته باشه).
⏱️
۱۰–۱۵ دقیقه بمونه، بعد با آب ولرم آبکشی کن.
🗓
روزی ۱ بار (ترجیحاً شب‌ها) | دوره ۷ تا ۱۴ روز
برای دندان حساس: یک روز در میان
⚠️
روی دندان آسیب‌دیده یا لثه ملتهب استفاده نشه.
🍵
تا ۱ ساعت بعد، مواد رنگی نخورید.
📦
حجم: ۱۰ میل
💰
فقط ۸۹۸,۰۰۰ تومان
۱,۲۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
📦
پرداخت در محل (در اکثر شهرها)
👇
برای سفارش همین حالا اقدام کنید.
https://memarket24.ir/product/brief/56228/180124/</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677388" target="_blank">📅 19:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCRsGAcejaUf02BP0RmeMvzfqkPyxqDI3LZ62AEa4jOMiKMvrUsJEtvOTwgvD2v2XyEU-wAHKAK1G9vNCFC7Nce1WGHB8R5t9eCURr-iAsWLznRlvvi3n3FLVvMYrEYmf8jPk35CCA0uF8TvhDX5BlSm6OeGa1a-nwxZQWdHGu7zN5l-iEEQkkvVTxSvHhaACUN1ZplS0PWnCilCvF4dbCjbpLAWsdugiAJ5IXclPzMgqY_Yqd5bil5gfz_HhRELcQ0aKfR25noy_LK9HxXD-KYZcyoPV3hG1Gg245xV9XVR7N-tQYGxyLmheGW0Jfkt9UAEoDVPKSHrl-XJ846_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای سریع مسکن‌های پرمصرف و موارد استفاده آن‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677385" target="_blank">📅 18:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677384">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRs6auJeoQ_aG5uXXRcPBCfIXv3sb7U7kiWIVSwegO9a3OVl37poHNYa2Xg1719_ULI0nmL942CBxIx6mw7KANlKTTB_h21Fhvpo_eXG7fPWp0S-phjurjH05zl78MTtSVV-h79GNPpyvMr2A-hC4LpMh_wf7F83an9KKFkBD6LnMcnCYLX-vB-00gjjNb5LmCOfIv-cOcRMS9WketwasDdEobR8AK7d0tirEfjHbam5nxNhd3gcB3EeZHMqMynByhPWL_RIEhvrIKdAW-JGfh71RHv8QwXx2vyHAfna8vQk_gf03E2WFYdBu4EXLDEzm_KvC2ve3pRrQJU2LwzJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
اینجا مهمان و میزبان معنا ندارد؛ هرکس می‌تواند خادم باشد.
▫️
اگر راهی اربعینی، سهمت را از خدمت بردار؛ حتی اگر فقط جمع‌کردن یک سینی باشد.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677384" target="_blank">📅 18:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8ihLOEaWIBsEH4b1RDfXUJ0vVgN29SfTES-oKy2VVfRH8CEJwykhdxpaoc27CZo_CTrDAMrLZN6nVoqKSpQXWoHGio1ehzy1zPLYlqoBZPIxybJYpV4H0wadcEn1c1Chat3cDrfRzKdqXNI7t0Av3Gzj6pJFUzPt-FRdLzmZ0YPBdyCSYkeRsEW_6Op9iORtWMfE80iSWoCIc8coSvMxngvBVkHsvraRx2_-BnVK70l2f68UjRZ6KhfLi-mhx7JNxd_3LtbsTOdp1-066FErbXOC2atYipSoXCsLrr7nu_83JM4CYy3wtt4QY6NjTGwfGwjMfGMCBOwPfrgeU5Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: زیرساخت‌های ایران خط قرمز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677383" target="_blank">📅 18:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677381">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای آماده‌باش دیتاسنترها برای قطع اینترنت صحت ندارد
مدیرعامل شرکت آسیاتک:
🔹
اخبار منتشرشده درباره صدور آماده‌باش به دیتاسنترها برای قطع اینترنت صحت ندارد. اگر مشکلی وجود داشته باشد، بهترین راه، استعلام و پیگیری از درگاه‌های رسمی شرکت ارائه‌دهنده سرویس است، نه دامن زدن به شایعات./ سیتنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/677381" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWo3Gv1X3kicy_tRcgnu0qyzqIfwuTmyrxvrub_kpKQdCNFXmzulYVSisaDssFxdCRxfXwYMiJ4LUWHLQm4RRTpZNJ5b65_182x1MAdw7CXS6n8J2PXZsZoBvuPhGOB2X3PTK5dxGk4E9VVnYoy_4M10FxzNxxxuwM9XzGDBjZ6Emc43vd1jLv2VhoXve_UaHoTrR1OPgXsJvOvA9tyPTX_XOVlsYrvpA1KWolsy3LzfjWULqG7uu5jqAmWLc3nm-5U0qBCOkVX3Z5HHcVzwxSxm_Y2nmGK5nTSZXqhO5grn2n0_bzZhGxU8DTHhtefl39NN33OXrpUzU2RDVHxO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fehj6OR-5e_MFazo0iwpS4C2CXeR69V4CsWrlkM1SaWh4ZXMawdJqVBFt3nAEH1xU1FCjZkuBKrs4_bucZoNbeiXx3M_A3k_PtiN-1_2QrHcOF7TglKCWr3HdolnN-jS6ohf0-m3qieC50-IKA2GtkP5SmqnIHvMKNBvRTmFJzv0tXEt-Impd0gOElefeF36pt10xEKUEGnuHsURi3GayATSuZPP7I-X0G7xCr_TdP-gzF9pBMEjHHHjyUj3RB1L_abSf20PWNul-nR_oS5rJln-dsHx1ZEA3_vObLivjAiAlZb56pu9Izr5oy7mLiG9ZXQCZ32j9cSUCj9fgXL1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyhqr6PvBdQCf1RG87GlJQf13gUUpZ79rr7gBIWC6dr2-ol6Xi7RK7cQhulB8vLYh6JaRzUnzyziRHfB1atEEZ2B6WN5jARlSXb11ZvIqjzD8RN049vSJvElEWIIEdUsBRMZg65V5PaQ4PjzodT12_QItmmSIylzO1_58czhi1k8K0w5VAl3J65QBmecrRtmUP7NwCnnv115XgbgjZTDYbeFUj_P-RAUKRHQdpNTO8mH_ze0Kxr7W7vUNwsKakNoar-2Uen-PlMAVs58rCLE6vwMnKHt-IEF-nblCyXm3wIAx6YcxrA7OglJqzyEQZqq-J6VHnUeBZA1PQRcQ2jxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZShaqfxXKvOisxROipetoZC1wmZQZTx6_5nVbbd_bg23qKUdHfk4hFfPvcaa41wT9W8jpz-wsJ_8uEsyboYAA6fVM_-p8tQ5qEZXQvh-VoMYib9ec4m_19nMYZcmVexZFl31EFq0FEFguEARw_e3UYhBb6GPFMuL48GOAmABunUO5pZ3biHuLdfTIjEKzSIWBxgOJJ90lYmGuhdpw6ki483O8ul40IAUZcULYSMZI-xGCgiCLKJ1GI0lJTyOr9HuIeMM1slkIQfZ0kBF0qtl7EQyjEkALWFbSrDePpMeRAaS0zI4o1Zy3U72txRRzzchi0xizwakUzvpANyp12SYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM1qHKocrhIUOgiURIqZ6VJmKMy4n3skUmDICJM6Ww4vtAg5kFteOSAK1HArsV-LZElfPz1Oq2gjNeTG28OE5XZxvquYxQXvbef-BwyBt2SlyGh24iANnWctJ9bhI-9AmQP-nlYqb4JORBgspXO5GmN0KZ4hHAcS30pnHBl0E27wBt0MufVmj8prYQa40snM2bT2bI1dU1L9j-_xt33Y2CSebfrlxm4Q16cFfjI0kg3mt1O0min_MY83POXyWH7EfAwkkgvFOj5lh1OvIsQpBG2nYol_Q_f5EoWtxrqjmneG1BKtmBkVFnE2R16TAFOWgaGAQeqDBpzohLWhTAib7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_s2lK7mBHr87iEPIYcksC3CIAN3JQcQOySw9c8pSnMMQrMKxEPXTAz_IwPux_-zeIqaogBx4R0vevShET4OK-aOFUyOK2I4ZKsdlm28n5UQveu_ViKwRs3_By2pdiQ4bQVrL4etnVdvG3np-Ni-5ZrszTXojR3q7Fmnd0PUvw3V4PU4SVmMKXz8n--2GwOzHhWzqjpT584QtY1V9Z1NSpCvq8-DfkQ4Dx06dHcW8AwvdIlwvSYqVoTBOBp0WRcVa5caZrPZ7V7W8qIaVcP-6uC5tNP7rEeDgcHZxSvfLlm8tP5PY1yH-61bZoDW3_GzYIe7zCJN7G64ix5TIKV6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6TBvTENVtfF-tK9fuKixk5qJKy0DvOMJiEtoKQk6NRoOcZeULM1fo7xsGqerXhyreHeE0rN7S3lM_aLTBbDY92Ba8fBUttBwKPpwAD52h0RBWgIUDorShEZNn7X9g_03oebAQSgQ4KgCwsPQFd3JuKozoK6C1U908TQtXp4ewIHhmTd0I0RHb-vPuiknUTGg62kCyWd88DaumbKAe7dRjrneYaRgc_BphFUxT6n4c50kWn2BqGhqxZoQXaFY7x5XpKD_uNTg7D7Rfn-okD0Qh0luytspdvR8g3mkc0JGydb5Q8HYj7yB3-oVNB6z1Df6mw2NX5qChKaicDmZfJVVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدافع سابق پرسپولیس راهی کربلا شد/ محمد انصاری و جمعی از چهره‌های ورزشی کشور در قالب کاروانی راهی زیارت کربلا شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/677374" target="_blank">📅 18:43 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
