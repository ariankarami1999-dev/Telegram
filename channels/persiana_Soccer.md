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
<img src="https://cdn4.telesco.pe/file/r6I4cdydSYO42GBGHRdQjjk7g1N8eAAqamNc-aGQSkFTe-1oAQ_nGMDQDCu9eXyGWiw04m5qGww-yBCcOwNjDsjCDLxmKDDL7eAWtj3q2fG2saNl0W5y6lziIfCnJJ03b6rG6jqImFdDLPzML_oUpH-JPLJHh268aAyHjfz8EWVgKFW12jfhdxr6OlMxhFiJhVKyzxdDUjR2ojH1QMMmjyOOtM3nZK2XUY7Zr48Sd78EilbQNZkC270__tXFqdhTXAufFQYrYtl3QgHYVWgUK9omHi8bO0UTtt7fIga1WdBbH-UC-qp0Q36oWdvTuXyHl00T8nl3VjZ6A_0fod38WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 173K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
<hr>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtB1zB68hpxpTBnZKUp5x-vIzcV16x-5mY0ZkcapYPDOAqPC3rkj17NI9WhOKupnFt2we3wSseISKmfQIgnUQ89u2MMvY94wYOFwSjMj0zMWc5YuQQ11mRzhpH975mI473nyZz1NbYx2I3dbDicPNO963_-zlxGjp1WcDmmBtdu7iO1qDmRcVK35Gl1u5VbD563aHPS8IXcXaoKkoLEWEhQiwXbtc8QtwftbPpjF65kNcjENzfa4Kg4sbPV_GrVXs28-qy-uZw0MJlrKkrLE9k7oJraNQGZyLK1s6u_MTxikNKl--TVDwii5hZeaolf7aipYKoe5pOC7bJHJhFtjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTp3zPjiS3VyQvtgOBj5NLyIZZ7QRA2dgmk2lakvx2HQuS484AnF-p43pBc3tlNZyrlAmyYmpm1jDByRmtj9ImxJ_KMH3uby33g659ZwxxNvrw4d9Hdv5fKC2s7Nxgn-AtsYV-ThyiI1zOEgb5oukzpINyuEof_FKscekM_tMhSkSnM-OvAjE8PYX9dDBStTair7ObE2NhbDpL0rczi3mFMLHLobqP3Ff79ArB-DYr_YIqqtWVJRy37gTGrEM-9yKL-xv_DFU6oTYUd1usp3cfFrQolh1j1_fPgMmA0zuxjaXJX4FVVKC4VoDlio7dJkgtgCZUBAghkGnWFw0xTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBfsvKoly6_bLn28_7FiU2WZCEzBKrRzr29k6HoMkNjQDUcrpsM_xG5kMFkCs55BrocHlF-BlGW5MQX4HmJn239q7nNWG82GGvrevsCpYeMz4leZgdZGepXnJhtGAbZUyvzqo9-Qg8B_5y1PuArYukdOEGK-vmzMTg3rHDH9PS09t1G7qpFyDm-KuFITNUJrIvwfnw8Ar8Nv3U3ybTk2RRitXWnWr2juG3M7PSDsdqRkdC975wiHItBEetgY3NaDcn9JyviKLHDpk6ULfpYOwY0qxSauzqVZB0rOiA6EzYK5S6Yr5ekH8caZuOUdLZk8F93_GvtENBZANtfjO9JYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7PQgrnq4H4LpvVi6UB4i3nHDdE3H0Fff2htHfgdngA8HpVi6C0zzMtwE35EM9nKLZA9q0RA6kF_FV4gatX4QMlDg4Rdgj6kCTEBnPKcGUI7_kkOleClRCWaZSGPCbrdGhCYbqMxHnyqGMAxf_mIZsxolRNP_n5cYmUs0hKXFpTZZ2V0en9FEazpJ1C7RI4WUrQC1NObH3sZoQdVxIbh408i5zPHLgIXzxo_-WYCBS7PQVyvEoihTW2r5YODe3tx5wrOAYl6edpotJqGHaUxuaiFyZigxwqdaKuI09tTRJTijxQqzOBa5urdFHDYAXmjizLX3NMoLC-gHdCMqWMmzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSAeiqmRDWubKHCtpghixLQIz_veQ4FEuccDxi4Y8rfgiCXcsJvrd07LrQkC1BdowBN4Ube28re3Rlc7ddRml4gCBb3Y1zomIH4e_0PrDk68A--yi3Fk5ABmb-VjlyxdZ_MTHhKun291k6uoKs-EMvKtA9aQVCh1EMxLXNXKfZHAqhqlsJU6HRw6x_5IvzD9GxYCDkpz1szYNO2enrbbczSI2mbFS8JbcpxY_0lDXbiwKomscqp_1A_2UFCyNzEf1Ey5atQGJ-hnPsG3Up772wFj3Cwdh81CirJQAwRqeXv33SncwnJ0Om_7G-dQ3h4e51PetYTrfa2m2Tnn06i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjEtjTflPuTBoFKo6EBeWO7_TDG5NDKK8kglSccSpxIfoU6OsQXHrC5roEPlFK8kNmUOYvAulwQTO9mRdnO-R59_JG9DT_GZMPlyXEu_nXPG4skK-a9aZ3rgGqumnUaCpbgeos4P8-vbDbPu2RlAIRTy8qekdM0t-G3EaEh6QCkiOxJQWCCAQuDrQ05-ukdOi-_fydUymF7wk0dIgOc78SUlhdTHp8OlyXJnxdBQUcONUzBTgB429GwgIQuoOw1SVCmHFR2_W4URRZvlorkqu_HzW46qK8d_p0t7wda65ZKAgVh4VKDJnhWtHVM3dfjTXbxwnwqP85LT9OvKp6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22896">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf6OgrGAcmvvPWlJQ9e9F5BQBwRnMAD9FCqjle_2fWKFfc466KZtBmn8HmACbLWTKsD_yD9hpWYP-3LzwonXPVpmo5D10PvBfykAj2xHfYBJYk0xcjccX-inEmDW85s9edWeYWZSmh44ATjuhWkj2DrG6IdTIuyvOWbaCxx1Cb46OdbiJcXZdP8AMECdzdA3UOYnsEgpwxNcgV3TQWC1DH4UDgVKA26NVqU3wXinWjA2q9ilw27WML5SpBb-_qy0HGlMge_EcuNI-lZfX7QxSTK8AfVn6NbfORb3woPlXPCJD8yktGGI38o9vBm9cETiwUtWTwAb-R1p3tX_kX-DTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید باکارت‌بانکی ایران انواع ووچر و همچین‌انواع‌ارزهای‌رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22896" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=rZJtu3SmfnjKL4U6qf8tUic1A4txOYsOTwMWZLAgW9IqI2GjV1tWSOQY8S5nnGQqQJtiR1bJq5ySNEAwfk6WzaQWXTV0KU1wt6WdpvYTeqWltxU6QDBaf7elAVpqqnivACmZQ0rqpx7V-WWjKlpWMPk6xyXX0RKyyJcMDhyMuSbVs2ZbOhuhVot46IviSg5Xaw70Q3U-5YqYta9399m4bSW3OhXzdFz6TYJGS4n4ntLR8aFOFDOHTlaMcnTZpbIPe_pqNDZ6eAuWhm-SZ4H1X7rSDCAFEasFwLcWe4q5kQBPLjATv6CAwhWftG0QWTEG54eREublTeWX2vmWldbCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=rZJtu3SmfnjKL4U6qf8tUic1A4txOYsOTwMWZLAgW9IqI2GjV1tWSOQY8S5nnGQqQJtiR1bJq5ySNEAwfk6WzaQWXTV0KU1wt6WdpvYTeqWltxU6QDBaf7elAVpqqnivACmZQ0rqpx7V-WWjKlpWMPk6xyXX0RKyyJcMDhyMuSbVs2ZbOhuhVot46IviSg5Xaw70Q3U-5YqYta9399m4bSW3OhXzdFz6TYJGS4n4ntLR8aFOFDOHTlaMcnTZpbIPe_pqNDZ6eAuWhm-SZ4H1X7rSDCAFEasFwLcWe4q5kQBPLjATv6CAwhWftG0QWTEG54eREublTeWX2vmWldbCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnJd1XxBkjbgBWIDQn3PZRrwELIEvv-cRgmq5hGXqWJhjKn0xjYM4qqXJ16kjKZ8Feim5rISj9kDClowpXr8BWaO0danU_yR_tBOb-URd-5jLPX0Y93w6MnTANGwATn8sin03adfKJEDGtcjU-GsjTT8BU7Xk-jY24j86XMWDq3vZU4-y11zRHaAxpvCQ-GteH-0OMIGrgj9HUWrGwLtOIcBvS4b1IGPNi8-a78VFEAuGJziPj4oQBbTWQD14nmlPG6aCvwafGMlrOCtYt4miwAOQD4xBlTEaEAqWjiD-jBn3dSgTie7fHclgnXPL2m2d1Bg9ObQ-CQDU-rS-3uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWI7V8WeD7DC9AdWdUP6dmqmWHoLjzWmInLDkRsXAf8Sd4PoHdBVlmwLcwmeE6JDxiB8cS24gcrpFeXdJCYAHz9S4ooyLIdw4QOukDswfunui_ilZJlBuYyUfckKtktkoveTcSexMn67MqihqdW56qIZzh6NjHmzh39GcA6roataLzpmhbWPddbCbnBvWLk72FkctfFI0g51mybUZ6q4M50pnUXUWcjFQequbeBQ7ZeFGogI4g5u15hbBSzFmSdiC1llkgoDEi9CAO69ApfaIXyrwTtdW-KAV1MPVB0kewIqYrd_aa3JaZjuyGpX1kmNqdQER_O5FmBYSyNbm544GdS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWI7V8WeD7DC9AdWdUP6dmqmWHoLjzWmInLDkRsXAf8Sd4PoHdBVlmwLcwmeE6JDxiB8cS24gcrpFeXdJCYAHz9S4ooyLIdw4QOukDswfunui_ilZJlBuYyUfckKtktkoveTcSexMn67MqihqdW56qIZzh6NjHmzh39GcA6roataLzpmhbWPddbCbnBvWLk72FkctfFI0g51mybUZ6q4M50pnUXUWcjFQequbeBQ7ZeFGogI4g5u15hbBSzFmSdiC1llkgoDEi9CAO69ApfaIXyrwTtdW-KAV1MPVB0kewIqYrd_aa3JaZjuyGpX1kmNqdQER_O5FmBYSyNbm544GdS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=QEyF4kLAVgiv6yAezq7ZZCHpikZifGtSG6TFw7r34U3pQFBcEdgTlbXbInOF5UwTkBLzbsqjHebCkGmOEZDC0_r1cpA_HOMqBiUegc4udMal45_cCUeLKcs1uS-Bfe6sP0Clgoowd8IAp2zlYvw9JOq0d4TtUfX41n_WqRcH0OfHD7d4CB6qnmzJnrstNhz5BYTAeHl_49CDMu9kepSW3r_DBY3kuS7hiDYy0hAwZVVf2rmRbcf85-uclNvdRmA8mBijuDpPXdGoFZJE7ekpxkBSCN335IYe-NUaKU95ue5JFs96X26n649SSBW61M9PQ1OW_Hi4L4bkhXvyOMIh8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=QEyF4kLAVgiv6yAezq7ZZCHpikZifGtSG6TFw7r34U3pQFBcEdgTlbXbInOF5UwTkBLzbsqjHebCkGmOEZDC0_r1cpA_HOMqBiUegc4udMal45_cCUeLKcs1uS-Bfe6sP0Clgoowd8IAp2zlYvw9JOq0d4TtUfX41n_WqRcH0OfHD7d4CB6qnmzJnrstNhz5BYTAeHl_49CDMu9kepSW3r_DBY3kuS7hiDYy0hAwZVVf2rmRbcf85-uclNvdRmA8mBijuDpPXdGoFZJE7ekpxkBSCN335IYe-NUaKU95ue5JFs96X26n649SSBW61M9PQ1OW_Hi4L4bkhXvyOMIh8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxBc5c8LFD-ePtu9Tfi2cevbXyupuo3B44WRIGrYAi6jfdmEABzbk1uc326a30sSn3JQZ0OnBA93YzAWJVld31_3J3XUCMrTSZhZ5qURObM1y3VYuLOX8Ej7s4SrmosPUSuUqsD0qa1-FPB-IpDRgn84dhHY5hKio2wx4xv2ht7_FmUqax5d29J5IhQCEHr4ISRSwJTM_k7LMczGUHnOqvJSS8vtvHCuu8iMWbkPIFWKL2Uyqx1D3VM2W9NkVAo4PadSPo0B9IIJCV1EfMoKl21csTebnMmeVA7u-mWSOs_ocpfuJqilJBNQh56B3-Iu8d9zsRKx9EnJ8dgN7jBSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIJNc8a048mD7p3humb_joYe2xRn5h92uD5UPLEeLuGBajCABYhLrhW0l9Cej9kZ0E7xsj_eM3nJ7McJ7eSUbWMcuz1gyHZk2bvCsk8Yqg3Qb3JvqknANOBHUYqzABo1hLUFyCEeBUQbAs04fvhO8V0pFKkFHFn5jCOrGLcUYIHDqbVOyoBQ9_rETtHzGQrcyAANq--aX88bGS6uWmvfoXRg5Wue2aiV9k1-NNeIidjVt5FDvKzDcdyInNNJFVDSPq6YNf4qxi0NnY4CwcBhRRPPvfpztBl_rGvBkwfV9T7nJhelI52PH4hiB0Ev2iY3IbhId4VQbt9G75wbVSE4QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppw1-dwa8BnUPI8hu0Fp0MjfOMYrAGaqp2EahWKPJSuSV1g2_TwRjmwOIOIwq0mjvbIcuaOuNWT6VjyZ95sMrFSgafquxCzkaMHb7yZbqHsO1oeajRWLWGCQ_cgBOg7v6nPOvJRp0hiWemN3kkYY00wgnifSi-F1L_MK24KBNSyrKuu2LcJqDjEMmVUQ_UEd55UnpSl191l1RlsEFUOtflXBV6GTllIndjqCFtHIP5vIjDgu_Aqj425Zvn24XprKtRNuONwqZFvUM1ORQEgIOpoQdN0ctb99E1oZPTQD5S-Cx-ckuOF8niKAfFk9Q04tWEO2U8xhx3JpUhhZXoq7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWqmfCdKwWGPZWTR8AuUo6i8m_F4x7yMcT79_eGVpw4cgABoAPDTBHcUNi22wRp63kvtxjRqPlTZemcux0NO1SLcEEkZGF5zlazM0vNl_wkSyGP-s6XLUEJQK6Oq4yxPjsxvZIWhH6vgjfB1pNzXBwgkWqx0eYbYLq4571T96BJ6RV4PKSrNFBFTIiWVhHBp7rpRjnNXwQVftGaOTiuJlLvg9olu_YzdwCQGsHtUMSYZFjxySw9__KG5nGwVAR5QSnmYqAOZbuAxCW8MFzZMiWq3nSigbxzecdCd9BIdN2FAaCxErMH8g2p-GJDGTnhFxfhjEp6v_KkVv4TjjCHRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGTjOfanlhHfVtJDPcJbTAvDy6bL4IUZC_P_WQpFqZJ6XGdOl3pkiBASliqCCX-w7csuO5uBc4xcVABttdux8ddRmm1ccFMRpu7JVUc4QEUmXrKLKi7-ea73AN4CfDM_38VVeefLJhQY6lROdnQNeo7zqNNcFLUhffFCUPueA3qJOAqN9ManCyZDTlEqecBplCH6umEQKZhRFaOaKyARqRRVqdtUBd5ZXJycZK5Bh8nmiN3ddB673wtEAGnpL0g28hjh8EtDQI9VcTPxXPbD6s-pCy8fd1AsNiChFzN__-RfkeN1wH4XH608cXa0SpYOvOIGJZ1uhe7C_AwMIc_1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrIN9ZVK9AwokoLxOyBMLsuDwkB9BeIrA-hbDUilNSDCIMa7GC8oFgZj-PaIfaAqibGtTVB0PRL5iR5rqbw50iEPpgnFDt_S0d9mgdk-7ZDkoe-n8HaRJBayGIXduobCFLZ9MkVRLpjLj59H8fe20WE2ydgWc_WIHCZS3GoSFk9tl0HKk67Kh7MqDyG_wFMWDtrmAYmjFTnNWuOEbKmtkqVZdJaphWKhP2Fg3caA9vPYjSwrGArbvkDMVEoYl937xTm8whsrYVDsJ3nIuIB81h9t57jOKVUm1ItA1XpjlbZl1ORnnW1tlvTl3IjAmjKCkBPQOwnv_dOt7HgoHjgMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWDdlnckZnX6Sljw1MstpowOBiQjtI6_SXr7hSjxNiBdjDg-boKASjFISokP9gNmhVWahOgCkqLyuik3jhHKqK3FH3viStJoNGbfnUr1F5wVs64O79X_Epgnn0zMpGXP0-84cu1dpaKNgpKSbPDLgyfntcDdVf7GUa2DTFQAtG8QHnKqbvpT0k17y7aQszNOL3cgtS4lF5ZVBq0eICcfXMs1D_MV5d1Py9x78tjT5JidThhOoFDZHgyhjmP0ZndcidpjdJitdpaMWO27ZrZpSzRfXb9v6SC6F3e85y8yQawqAckUtmRG6gh4GGoRsT4YJ_7R5lkoWQn_LF0hf2aK2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXLOSTyaBMtT9-1Q0zT48AezUCAIo5vrFGzAp3QL8NtmDubo3m5UvNNbbZuLcomedxIo1VWpKVp-4tR4iZ70YFvIf-MDHwP_9wSuwMBqPT0_xw-7Nn1TQeYwppr2JWF2xgdyQIZ8iOIyrtlA9DlzGRDKXuqFPmRjMugwwliy2kQBLmFPY5ngAV4ZtdmrNe9bbV0W6nfvxp0feN_momQfBeklOgTXJbzc1pBf_hLR_zG-M_PDEVGGH82Z5ZPkjlvrfWDuZo1enZyXBLggsF5ydAmCqWeKOY9aw9BYO7dcwSoAcsXrPN6BwM5gz44CnRqNM6Ps-Wd8dNHmDSSgPQBoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL_i4RD707ElmgVTadn0fbhnWe_bkY64SHQjg0vQf0tfcSz_3-F-otgAEh76iEYcBNwRhhmie20WPjEjssiWr3m6dADmO6DfDSrm7bUjPc4QFPOL67QafVpy_4aWVWJrWgbGdaraWXXP6VhMyJe-Un9_YpTVTMTlSl5nOJB08gQUGaLU-WkZkDZP_UCK-p_ha-NSxBRlbhs0nFDqbmdkwvHId6-48uOGcG7JCr8I93Svix5CUnaTdoihuDgtLN0D7c1RAlzUhKCN2f9hymFXCeDnCvvj16HV1e5OfHApZIxJqK3RU9hgxOyiHZuk5viDbMUrQ8JjMe1X-29uxHPZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT6IVNNoiWPAoIzrQ7aSlJie2xbKa8icixq2-EKUb-FDtxX7TsmIPSmKeTzwW-N3gcvLPB1A3kqRS7zX5sZX8ZHtutEvsEcMit4dYEvDIv_ed3LZY_Z1wvwW9IA4uUFtBWmcGn9ndriwXbVor2y5nvHXWgPZWZttGKBKlSNU285BDyyjMqPem9mcKfPx_-nj3Hgf765ZXAWNAweAfdPOhGqBaTVx7Hhu0I3ILuXXewBEHAbyUGPU-1_fFNUVDV2qhuPDceMo1HLNAxuN5krA1Yubnhr5b7eBMvohzxGhIZEz10-1fgxDethZ5zXbmL6MgGAE1jnzSmDco98OwANzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEefsTY_07aX9QrLVQfx_SLwM3cBWqIDFuQ1RkN9hkrxqY9nn8XXaJguAdzweHMBv2fTA1IwWErtPUkmgGpVTcj87RJBLtibMj8Sh1Id2tdDRHEW_L1WhUauNjWC-T59roj7s3bcvLvJrAaFDSF0UGCznQmfsyv8HC2l6UzNYEGftQnnuBypFJzQiovuRUASdnIO4AkWagK4Ft5ibw5-cvbSJbxbva5fiPLBnZMlspb7XY_qN8W8qSehRMgNOtTvjO00uCDQ6n7XIwcySmEXmfk7F76cTMOtTRDEq2ygikx83U6mqGMSOxySbbtcBLkcQWbuYvcpDI_JWEqsfGivuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjfpbMmFsbNcAhSwclbNMYnPz8Q5rGW6S7lR-93ULQb_JA7qQmUkj_xQ9CtrMhclTKsHb0PiECf2DbPg6UfgkM69AkEdzai8oC1c2yhc9_q8lGK-zgv4eB8F8yg-ZKUNZ4LZ1-K_dZeZuBWq5Il20--KDNGJ0sBdPCoXsa5oHDkb-S7bnxVc-DbL-paY1WYiU4-phrN7q3r1EX6jlfJ-IZWuZ58YoVkbi9e5X64BpeP58PUALo99UWfMRJCFJAScJfqb5RhPMLVgHlHfpuiMxEmdQ4QJjp1SJ49DBzZYuoPT1maApAnQmc-pTFBl2aIrorI94Jgr1iB5E5PaayJlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y594wbONAN5c2xLp91DG_sDr9YI_VbYCqLYLiwujyxizOnpjur4rdrFDfdeE-Pg8HzxHLGUeXjcJy0fQngke3pxbExg7wxljh7CpDvbvXCs_gy7Ft7vMd7DdP5H2xzJw96aK0K3VmiM0ksQ1YDD_G26Y6z6J4PKvzqH1IntNcoIkKrZD137u_n-d5AjK6DmRoeMT2g-ncUuxF_8pPO3JxhF52ovuYa2pHrARgSB-PTYhLVn2nyA9KOIrUmQ4VcD6uXg2-lIHKU8fqWLFt0iRyJFpB8eAzDN19nWjfzTVL7G6Juhnv5Enl1VccKlhXyOS3z2GT7MuBAGhWNFdTls41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22869" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqjepSpcevt_l0Pb2OOWHxk301yJLdkv1YBXNhVhqX6Nu2_-Cn_CwPaSXobn9n8LvlToyzcJjen9XiBE3zxpAb-3U_e5BGGqh7VV0oMjxk4Bup2oQCN_Joite3n4W3ZJgaeyWbO5yrRDK3L8pWcMHgj9s2oC4SceVejqjeib752SfDDPQDJqcsrOSWm0Se4Ov3Rqi0HZCbjWZYApQqYZ1U5DUCjUVZhvgCyeclSaGvynH4-pQC3t8zGKGm0F95uO8n1MksPg4C198TV1EsCWUkaQ-gS7MpeFjQEaAli7xlLzNG2zTSYfA5O4LsKb9ek7OHnCVkiBz5R6yJCJi8SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwqvX3O5Zzx4_YhUUyCf5yWhNQX7R_6jiZJng0KzKkz111bovYG9yh6JbaRPx8JRir5FT5uxiqBWxlV5G8d2wPqT2IWADK8bkPBC2zam9Qd5fUy2Fm4Q0aeWbO5mPmXlUasUpXktBuPKuucWlnDZpKwFr6TJAu3TO9hMtNeJEeT7nxADC_ipLylZh_Jw9VMKTMz9USG7S2s7g_2YGsfWmC4J6xF-PWUneGi7zLmdlehYfr3Kssvvnm3M2lciXB7bLoYW1KE8zPYQylXz6CZZGTIv7SYHd_nqbQxvh_89RYZhbCnA3LBfL3ifCcy2nR6sEHaHflvmxXE_jGC_94UnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=L1ZLA_gjSpRSOe8HqoBKfykvpKsuj0xMXDDpxRJKe4Mlb0OCjjy42CIBCL98MJUtcSzkK5QgcCmnrd9TOYbJ6jU_tkYEEphWDc_yy_XZhiFCFbCqev1Pdz8KI5RHKJK-N6iowG9xhixU1XScco8_yh3_4vZEAwqzG1xGG5j5vVgJleRp6D_ZS8hqOKuaJrp3H-gHumvFRZddfKncU2S6EgjAGzCbmAAktIgVlmSY2LoIrM9leUze08eQYpk3ok4cVqC8HyyxtktsoJWR3YKIWte8a51Cc3SvaBLdChMPaZhDIteSjSoJm28M3Q41k8Wn5uSgDsMfKN7V-sylZoqFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=L1ZLA_gjSpRSOe8HqoBKfykvpKsuj0xMXDDpxRJKe4Mlb0OCjjy42CIBCL98MJUtcSzkK5QgcCmnrd9TOYbJ6jU_tkYEEphWDc_yy_XZhiFCFbCqev1Pdz8KI5RHKJK-N6iowG9xhixU1XScco8_yh3_4vZEAwqzG1xGG5j5vVgJleRp6D_ZS8hqOKuaJrp3H-gHumvFRZddfKncU2S6EgjAGzCbmAAktIgVlmSY2LoIrM9leUze08eQYpk3ok4cVqC8HyyxtktsoJWR3YKIWte8a51Cc3SvaBLdChMPaZhDIteSjSoJm28M3Q41k8Wn5uSgDsMfKN7V-sylZoqFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=ttzIflUfd5i-j8wu7IPOCzag-iAAlrAQeAn24KDf5yJJOIV7rGNPggDSZ9JPKdZ-cJqk8AtBWUrA0Eh42stIps08DmA0AEVckDh8EI-itdMlnhwR1Tlt5UQkW0D-l6fSvkCUkEFL8q9mokPjciOo5kYVq2LiLb8oI9DBBn8qHeu9fKOehey7hakGq451vQ9Zwdu1sF1PO5i1c59e3sNGpVcxomLf5RYCIo_WgWF-u6buL70N-BV1LBEf8--nR8bxVqJUo_txT6Qe9EE4RGjrr28AH9Mog-AgxlFmgVaJvxHxxRR4LcQgbOQOTqZTLSqDL27JweeyYjQ3iFD-7oOeIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=ttzIflUfd5i-j8wu7IPOCzag-iAAlrAQeAn24KDf5yJJOIV7rGNPggDSZ9JPKdZ-cJqk8AtBWUrA0Eh42stIps08DmA0AEVckDh8EI-itdMlnhwR1Tlt5UQkW0D-l6fSvkCUkEFL8q9mokPjciOo5kYVq2LiLb8oI9DBBn8qHeu9fKOehey7hakGq451vQ9Zwdu1sF1PO5i1c59e3sNGpVcxomLf5RYCIo_WgWF-u6buL70N-BV1LBEf8--nR8bxVqJUo_txT6Qe9EE4RGjrr28AH9Mog-AgxlFmgVaJvxHxxRR4LcQgbOQOTqZTLSqDL27JweeyYjQ3iFD-7oOeIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3KD3Dn_nYakEInwEvZLxrZ4thmZWAezRinF0o0mHT5vzyMRG4C4v2W-_ojTmpy0G4lHrZWUYFjkKV6yMvPELXlacJ7I96OJfug-levGz2znzZ6jCCXRynCCsRjBJ7E6ZnwDp1IrrjxZnzzM9lGj3Z6dlOMiRv30IGnhcBWQ_FspMyZz-xTOIk-WZw4nd4VmYpG4Ln-QMI3GtyZyy4N8vDS-YXrlHfGbTtU-6ZreJWFjnkO8xujkHYgcuOSTfDmCox2SsHHOr3s4IUv-om_fp_yUU2oZ-c0LHc0Ew0JM6q3BPdIXElI96mc829geLBzgzfU7gNP4iUJKAfcudrP4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvWXUl9u7LKfSNid6Bfjp5C7w3AWyWhgy2KEp6jHLwrjgEhPg3uQnFNlL_MkkPFPJ73cs00hiUoW5iNhTw8Mee4fuylwgmC8KsVSH-uptuH0-qxZiqBXuh0yfHIMbKEEI2HyKa7yheQU_k01CD46a1kxCCeAnszkIKIcpmdg1MQP6U6kgEcpBEfPVgx9X7H-brlqi6SDX9TAkwl5p6er5mBFy5xiPE_IOcjlMMlbrqJbdSdfKcy95SgN68dsgBQ2qvvsdIXh-UgWaYI_kG0frwum1D3CXsdzniNFgbwQ7VVasHrtPYMG-fnAjrVrLhBL5OPJTp7nkk3Qo2VkKkCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVj1Ro3fze3ZaRcQN9DHdnCXjjOhk_kUq0xupB1Fw-ESCAITZ_AincdHV7kZtBWLiWKSoaokNcOm7T_y7bMMLErhw84tCYNOOuslww7941btqN19yePUHDR37QNrYmKUMWVZ0C76iUXdaTFgGRhS8r45pS-WwiFnHtBfcvCqv8sSRoCGkyI_nkRpVzNrylxCS6TCN8rQbcKg7iimGhBbN_tyWfmdYcFaFcWYL26Kap_mexCt0prskaKcXZADn0WDO0YZdd2DDC7mSUvKP_P96beVsZn_BUXN176qmBtsAEHmrwfSLAGJNgODWqq8qt5sec7UIa03lTlkQNsD1ckm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzdICiESiVd9Ku2sbcvV48tiAEqLQ7bX34HF_xY7tH-BXpKIDm1MsWrtWB8aT2I5_2Q4EiC2mcjIa1Z-dJ_0Lc6Qk5M5m_gzM9-ECtNLkX7VXvqlO9VfumTc-oFNhY667Tvqcw_e2cyEvf0oSWkpUH2a6R6RVW7M01HbXstDGKzXibxiG4S1e9U5JkfAnmgPi5Fzc9_tpj3TmLTOHG84VjI_gwJVAxlI-TsxHrWNdfT19fmhdL6Cb0canEafmG4exo_slBuQTq2YFC1wCKsIwaDF8SaEswxggpjDs8XS7PbIqJL3yBBlyWuMSgZClpJUtHjescJEaIe6DPsSG34Ltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_SBiOPj9lu235MLi-kT3DkX8mBsiEkMvT8btOYi0dqLqQY9ir1F7--F3Q3H1JooHmP7uvEjjJFFPA0T9YkVU1-CHDfy6UwWmrgtvIELQxF-ERSoIrkxErEkCzUFa2VsTUDGkMFAmlLguCmzkZU5gE6Es97cIYVluiufBpQ5Rp0DDV00SoQxDUbPL2pSaWm__UY0jkGqgHUB9QrZTUaJoR1w43tJ9E_Wg7xS5AlL3v7VMiDiQrO64xn16IV4ThnV6b2JSms6cncKKz4HeDfIZVayn4fUo1vT9YKyADzAKqWFZ07tXJuifgpCwTrnvMlvwks1HlE7BGvCdaIQp5HACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7HPj3SrNy-rsK7VhQF_t6SUqUkss1tNyZmv7hPbMJYZeYnzxm4aX9qmJegBvpTqK1WYEb_OXod-xs_M8E1skYafFnj3WQ1XtROFBrT0TPpE3_isZLaWFcJVPbfdjglQcDWNa2ZahP1XWmNV4WV9C400d6PAudWp_lfc_LhbL9huNXL5TgGhgkisKWIEd3nG4-59gbydWWVulhYnyw7uP8sxkRlGJjA6Y-fD35IsmZM89mU04J2I33XQ89sFZujs9mzlK_PQXHnlAn9U68PFawb0S9ybzj0HJTVPRZVe3liwmxzPwfJfHnN-ibmzj4nmlnSWi-rbgQrlF7eK63POSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIX7gzWBIzD0IPcfb1whqFZfkQiaibxd4ShjShofnXas5t2FbCmHkF7Y0xEJb2TYe5ejhlfjhraj6iWDnJViiAeXROek8LsgACAsDRDQng7zHE2kE-uu0j8v-ypfuQ6Ccj-v6u6ckO_QMzcz8zVkYD2AT1R1gtwtLCWtOIApCSGQ0ijP5ZgvQkwRGp0cpt6bJ8Wo2aBrVX67IsE0xkKHZ3NcXoFUEY-x8FOhaxt2YeYenYwiJA3t_F4chgUGU-joP1b8iy82jvt7kbSy7JEgkYl6wAybt8fDuD0J_EIhXIouNdHJouqS5x8Kzyk4PnF8vkxeSl6LhTFWWVAysBLKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA-ALBBMtb4MZbWDoo4ahsUczMA6yhzvPQ5LHIKUCbpaSkhvmtXkzseDFwtOmO7hxY11IHBQLyA2rQODZk6HkccatzltJzNepMtuplnsVN838xwiQN-RFufbUFItpVPmoirGWtj-B6EejWaZ9Eofa1yMdpv-cEdSCv1KJVYVUYKy4inAFTsQqzKHZAywn1NgYwi8BcST_3ICtypd3Nc5heJtyEJ03_ayMCx9M1R-KY-gexjTih2GYo7HvaG4BncGEiNNSBOu0PGp220lsxfDMA4sAHxetyX38y4yCL68g07HoS1lMyHSeXfrJ2yK3dDCeMMfdccXktfE2lcnOibqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=D3gNbQWwKMhtDsaXVvpv6pifRwEEmIuWQJoet5J58DKkzjlk0ZxH160jX_Cu8WkE-ZHYEolz2rWut7IK9Wzh6w-WHf5UQJBy2Q3p64yF3MTHTCCEfdhSLdbr0f7fw_xX_ClZ_ltBXhiwmRC_H7AbNf8jAx5Kt1sFrYDs2mB6dgvu1PkiQ8BysRGFN46IrhBE1zwmGI02B3ZDCDteKBpCqIuj48X-BkMK-wco-sKBbfxkBYYfA27yoAVnP3OmN7-Utbnoi21cUMibjjpB0uVfRzm02m1J6z2w4ITJufYo-NbO8P26QG7s_IvO8EUyrNuaKTpKIQ1l3lqrYLudxfDH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=D3gNbQWwKMhtDsaXVvpv6pifRwEEmIuWQJoet5J58DKkzjlk0ZxH160jX_Cu8WkE-ZHYEolz2rWut7IK9Wzh6w-WHf5UQJBy2Q3p64yF3MTHTCCEfdhSLdbr0f7fw_xX_ClZ_ltBXhiwmRC_H7AbNf8jAx5Kt1sFrYDs2mB6dgvu1PkiQ8BysRGFN46IrhBE1zwmGI02B3ZDCDteKBpCqIuj48X-BkMK-wco-sKBbfxkBYYfA27yoAVnP3OmN7-Utbnoi21cUMibjjpB0uVfRzm02m1J6z2w4ITJufYo-NbO8P26QG7s_IvO8EUyrNuaKTpKIQ1l3lqrYLudxfDH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDKoMTM9TWvo79o5GEbxHtieFqAI1p9dNfqAxUm8sqIRWnKKKKCsFHO3Wh65n62B234lYZ_HHx3PfCINF3N36-G_GtvVQi5kjvUiOoRuykly5fg48IBOkI66B_fXdOBHs23rKkhw0WwDRk4YBcYTRw5OkAjySGfMFTjN1-sOzG0_yHmFH2sJWeYKqSQ9h7ZyMweKaywkevD8gfv6JELH-0xFeMuANY45p80LN9oHupanbjDvg7v9tvNm_Vx_S2NImxuk7BilxIrm99hB0hiGHKvXx0vQpawY7_m4XxhYYO-PchMPWgXQREwQtlFgsp25el49QjPWyaS8YgQg6FAnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPtYfB0EoHFvoK4txU-279Ag1YP1OQAttH6txCBW59QYGKs26_MvmdfSkUDaWNqWjQEjpx0EG0KLI9cD3u-ehzScy2W3B45Y_QPDML6VqI46Wq76Aj-VWSS4laqNp3AkPWrB0V1L0aqbLVTsJa9Cro5fTig5Z9yqOI7j18-SDXFzedoqKfOcbe-7WPlkCEc6QT5bErbber5iCaD5pRRL4scuBdcR2TRIC1T28vQEykLrEPEmoxU5SPK5uB6AhujWP-AfFgr1UzFBLFtSGGB7SpSOLEAnLGxWYxXUgy7ICTeKTeLjinNuRinzyMf6UnZPF3jJ90_ypKJzifk6-Kte8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=FS4Jj3Uw_GHMhfXuqbcikKW9tbxzNQADtu_gVfaKOy6gOSGoZr0AYJaGwVEriNtVyGnqchZfbN-mumq7pZ8Ku_SLlochugFdDIN-jpzx7U7NPZW0H_TSYsIdHybf81jIhGHPpc9Zo58BevdMF_OUfqn9Yh-Kqj9-7XAqFZGU7VUZEOhkw--FCQrxKcQsfUMIgKAufSO22Dbrn3aDOEe_AvFswLf61vtm1g-9mI9ZeWbAuChiFM-1cRcMQulqrYmAKIzE9u4OLsSFf1sYpe4IVL_ZIoWCWgjSCrgLQVvySCq2yy-VCqNnxp7MpmmMYTOmKRE-tQ8-6xGG3tzP-OU1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=FS4Jj3Uw_GHMhfXuqbcikKW9tbxzNQADtu_gVfaKOy6gOSGoZr0AYJaGwVEriNtVyGnqchZfbN-mumq7pZ8Ku_SLlochugFdDIN-jpzx7U7NPZW0H_TSYsIdHybf81jIhGHPpc9Zo58BevdMF_OUfqn9Yh-Kqj9-7XAqFZGU7VUZEOhkw--FCQrxKcQsfUMIgKAufSO22Dbrn3aDOEe_AvFswLf61vtm1g-9mI9ZeWbAuChiFM-1cRcMQulqrYmAKIzE9u4OLsSFf1sYpe4IVL_ZIoWCWgjSCrgLQVvySCq2yy-VCqNnxp7MpmmMYTOmKRE-tQ8-6xGG3tzP-OU1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=p2YdEygdmObp7iufDmggbmw0tUZyGzKJN39vHdPrunoH8kRdIhd2xxNrGZWlMpdjiC5GJV2bM9h_fDHKjeFZGrmkiprXbbU37tz6cQOnjh2pyqrJJ2RCCgwBvZF6-TiYgC5QpY8qn4hFfJwXQp0FA1sDa8MJpjySzW5kKWn0Tk-jKlrGRU-QchHFkWVJQurhv7cMTHMlV_PnDXMMgDNnFSGG_fcXQk0WOh3Aa17hetC957c_I71jIbXw6VpH5CItmbcEr2iht2uA3_5c_LyLZZsWrgSEM0Xab_QCSXqOklXzW4MxZHEEdZLvqGTP0PdejpOJIL5ysKtHeuXLVmHwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=p2YdEygdmObp7iufDmggbmw0tUZyGzKJN39vHdPrunoH8kRdIhd2xxNrGZWlMpdjiC5GJV2bM9h_fDHKjeFZGrmkiprXbbU37tz6cQOnjh2pyqrJJ2RCCgwBvZF6-TiYgC5QpY8qn4hFfJwXQp0FA1sDa8MJpjySzW5kKWn0Tk-jKlrGRU-QchHFkWVJQurhv7cMTHMlV_PnDXMMgDNnFSGG_fcXQk0WOh3Aa17hetC957c_I71jIbXw6VpH5CItmbcEr2iht2uA3_5c_LyLZZsWrgSEM0Xab_QCSXqOklXzW4MxZHEEdZLvqGTP0PdejpOJIL5ysKtHeuXLVmHwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDQeFrH2zKuMNyRp-LLBMqTy7JK9tBcIUh6vawxGsIeGCO-ZGwIT7wAfrXtOkR0LNFP_7zf4JmwaFm00-mQIyqfVG46ac1yEjR1Y0pENYIrxo5H9wMqYxKv9vGqq0u7m2eWUPrC-vNHJmvp-KfZptRfQFuLCAckNcVRO86TXnlR83aSZA9WLBvb5_KhjOPgmKe4UKEMpFbWukWuk1nrL8OIrIpy2rPGWEh6BVhyAoW0iThsfdb9XX_FsR2Nh5BU08yfNmi3J_BAxFIXxhgOYT9bIfmpDgf_YiInlDLgyts2wU1MweMjv8QTZUZcIydRTeXdFZQFjgTC7_ZJxyGf7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=G-rQUUEpwwy7RpiUWmmgEFbwi6eRrXao-jgHIKOWQydwe6DZC9KBdrS_lYScici9aGL96VzT5aaxOrBKy-7IAGyKfVaABwTWUnCWmXa12WcNkhnlvEfxFhJay6foogZEZrbmkdAuyza5bSnmuPRYr_VCMcbdVhSi8KwjKd9foHXje2xCF9v8CDK93hgAweE6A-dop_DFsTlMj_KoBSddNbeuPtW6b3Wja1De_GCGjwxiq86hS8c4Uj9DCNZiWJjWTD6_x3scZNdzyFikgouENFmoquY8SSz17Yr4-43gA2-R6SOs9lVDeFkuEz-wZ4LhekjoQfejKVG41RjiEmVMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=G-rQUUEpwwy7RpiUWmmgEFbwi6eRrXao-jgHIKOWQydwe6DZC9KBdrS_lYScici9aGL96VzT5aaxOrBKy-7IAGyKfVaABwTWUnCWmXa12WcNkhnlvEfxFhJay6foogZEZrbmkdAuyza5bSnmuPRYr_VCMcbdVhSi8KwjKd9foHXje2xCF9v8CDK93hgAweE6A-dop_DFsTlMj_KoBSddNbeuPtW6b3Wja1De_GCGjwxiq86hS8c4Uj9DCNZiWJjWTD6_x3scZNdzyFikgouENFmoquY8SSz17Yr4-43gA2-R6SOs9lVDeFkuEz-wZ4LhekjoQfejKVG41RjiEmVMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=ehUsh33UwzdoHPBw6Bjc4RComH7RjAWyHXdQHtef09P1GzP-bWWRxwxZQvFpiAS2lyEhacWy-Zbt5qhona-DE0k3HRvueq3Yd4YaEdI0vHmNNYBTTYcE2LzHhaUEC592fdKHcDdhfytumkIJPppbPhk5U_AdxZ8i5hur4sfeYKaGxBctZKIfDhsXJ8tobXOeHb2GBco28pR8v9kJOgtReRRyukDGd18B1BNxLq4sbERbsTvFpKfiFXmSrrdCu8wmZKOUqVnFPG4U6NUtekfvt8wvc7xCxJsIYfXea5VT6pmD_zR2Z7afXZPV7-l7adKBcv03clvT9l0W_k2Rht3Wlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=ehUsh33UwzdoHPBw6Bjc4RComH7RjAWyHXdQHtef09P1GzP-bWWRxwxZQvFpiAS2lyEhacWy-Zbt5qhona-DE0k3HRvueq3Yd4YaEdI0vHmNNYBTTYcE2LzHhaUEC592fdKHcDdhfytumkIJPppbPhk5U_AdxZ8i5hur4sfeYKaGxBctZKIfDhsXJ8tobXOeHb2GBco28pR8v9kJOgtReRRyukDGd18B1BNxLq4sbERbsTvFpKfiFXmSrrdCu8wmZKOUqVnFPG4U6NUtekfvt8wvc7xCxJsIYfXea5VT6pmD_zR2Z7afXZPV7-l7adKBcv03clvT9l0W_k2Rht3Wlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=N2E-WJ1D7rY355MQIekAMrD0vhS-8AwxUfjRaZ-L5Ty0nTfIMvaE4-G8DHiUbiTUmG3XwSbmnM3ISHKg6d_-yeUn3htFJqC0Ca_S9FFmd9pn-tZHDzJ1HeqLvDKt2zbmkdTUHzxwxpC21lUB5236xLEXCQ2cwijuQ1k9FQiP0Ta7dvTZNZUI_vfeVbDHqGF9k5eND3RFSePJoZj8EOo_XMsvOWd8gSLDNTqkaw7_Mon96uCJ11TaC1stcK8d-go2N8lpFKRheUgdNYKOEp9VXEbTZdb0ALuiyrCKZLCnCsrh3Dh99-B_E3kx6d9-70Xy8YFKoUu4LMfWed9R3jSvBSB8-JVH1l8sv9aiJPfthmi589PoUrHSl6uJPyLJluVm2cnWL3wlIsI0L_oSvaJmJmxPJNA0Syt1vs1g9tNAwhjCpDD8ZbZEwtHjcsc4RikZ30vqSXWesF3Gy4-sH-_lXTTthvhadyI-M9WQKy_98SVF-KJLPrImwSvCxyChRXnGJQW0JTzyZ_XrAHH6ayusHRgOmdhU7kRVw3Dgrz6DrOGTcXvglJHScJPODSoqOLxTnH-yIHyCWjKyJQ1TxSOd5PzIEBOIEGgjjLpSli1TW011-1kND1tbRnpv_Olxij3CeaQPC9qqmt_UNBtAasDmCxEyYLmWfo85BBudGqBCWOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=N2E-WJ1D7rY355MQIekAMrD0vhS-8AwxUfjRaZ-L5Ty0nTfIMvaE4-G8DHiUbiTUmG3XwSbmnM3ISHKg6d_-yeUn3htFJqC0Ca_S9FFmd9pn-tZHDzJ1HeqLvDKt2zbmkdTUHzxwxpC21lUB5236xLEXCQ2cwijuQ1k9FQiP0Ta7dvTZNZUI_vfeVbDHqGF9k5eND3RFSePJoZj8EOo_XMsvOWd8gSLDNTqkaw7_Mon96uCJ11TaC1stcK8d-go2N8lpFKRheUgdNYKOEp9VXEbTZdb0ALuiyrCKZLCnCsrh3Dh99-B_E3kx6d9-70Xy8YFKoUu4LMfWed9R3jSvBSB8-JVH1l8sv9aiJPfthmi589PoUrHSl6uJPyLJluVm2cnWL3wlIsI0L_oSvaJmJmxPJNA0Syt1vs1g9tNAwhjCpDD8ZbZEwtHjcsc4RikZ30vqSXWesF3Gy4-sH-_lXTTthvhadyI-M9WQKy_98SVF-KJLPrImwSvCxyChRXnGJQW0JTzyZ_XrAHH6ayusHRgOmdhU7kRVw3Dgrz6DrOGTcXvglJHScJPODSoqOLxTnH-yIHyCWjKyJQ1TxSOd5PzIEBOIEGgjjLpSli1TW011-1kND1tbRnpv_Olxij3CeaQPC9qqmt_UNBtAasDmCxEyYLmWfo85BBudGqBCWOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTY-uwG3O7m6MUlcPZY3ZhBkI2lKs3pYBuB4Q7y_N1IMdPCGe74dwzwDWPSkvrhaN-SvVnRicBuIbhT8sIAgSjgSCQar5XfNghTeTm7uQdoj4YM5sylFc87e-ECJem3E2kBsFZ1LB9mO0DUu2en9kkQKJTSI7lyJyySF76LzB-Y38rrPsNKOTnLH2g8ufYbt_qg5LPfB9bv5ACgZ--0BxLLJzT8YXaGMsiWn5kISDFK015JNgkTSbhfAI_jCdBHgPEoQFuZhoDXEuB4CpiZHNjH5vkuAHO3zPnFxW3brC6KxP2zv93Uh8Giw5Ff0YJcbc7BOTJhH5aHMd-ogAjuZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2MvIiyzPjmpHV0fNqkR3NubCfX71QrbbMCoMBblJOUTfdsn7mEMhnPhCqNNqMxqfD3v_YrtCb6uwiB97tFCPGdd0Dg1sjMuTtz1bo7EZw6MOwMR1kW364tv1WJD6oPl_SZLLgir-Bugx3uQb2CjOTKoQjD7titMyZFqr8sMZJfTMpZQexSwYtnvsCd1e8MSBbQD17cOTbTeKSzy4gBN4L-AZmNN7PwJzTN-ZgxKnDXEcE5tqA_4TgHyI0KBogETbECl4lGxBRmb0nqyNeebY7r6d4qu_IlTReB3xDCCPlZ5cb7TJrmKs4tDKNrjC2DhOEjUyxEl5DW8zlxDw8_Mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=AgLqPmszaT44dUIt1MFkII1LBsxlTuOlBxVR7r6BmlSsNPRW0qIPNsbdCke0lcIM8UB9ac_KW4Vi1W5Q5CGuxWio97JqTBU-vKaXVxm_O7kUKNGgPdr5oS3v1Q3A6z27mAx1u20mDW_eaw343LQg6KQMfI6YhuxmKeiIKJMuy55l_QS8l7qespO6-DaO8_cXGhwgkD3fkqj5PB6QnNWvLM_8RHvHm8o1lYwlEdAui8_himM884RU8cTC-tE8tQv8SyOofIHzwkma5B0YFnKq8EhTKCd6H2X0S4Ep78zcAUlhw2HuKvZLyktx60gR0VaCAM4AIc4Z5T6G2YGBeVBK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=AgLqPmszaT44dUIt1MFkII1LBsxlTuOlBxVR7r6BmlSsNPRW0qIPNsbdCke0lcIM8UB9ac_KW4Vi1W5Q5CGuxWio97JqTBU-vKaXVxm_O7kUKNGgPdr5oS3v1Q3A6z27mAx1u20mDW_eaw343LQg6KQMfI6YhuxmKeiIKJMuy55l_QS8l7qespO6-DaO8_cXGhwgkD3fkqj5PB6QnNWvLM_8RHvHm8o1lYwlEdAui8_himM884RU8cTC-tE8tQv8SyOofIHzwkma5B0YFnKq8EhTKCd6H2X0S4Ep78zcAUlhw2HuKvZLyktx60gR0VaCAM4AIc4Z5T6G2YGBeVBK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4KMQoIV29DKmUVeS2AXsBDCoUISmMQArlUh2X_238hmTLRUJj7APwm3Ohz9e-jONXzhH4GgWY47Vd2eBZm2geUZAjh6OtJfMKgVZMzFrfVgcOs-i1LvPfkZ4gks1CbCGhavE1hGMvKz87FNmy2vApMHYAbxV3SJfxRsqdEbAszebTrMyYuFNC_B8RsmluhfOqm1hQzxZS-dhhAcx__wGJTNF5nhb0dohqJwc4VGEy3ai8JB_KW1rGmSnZEEjTIPAmQPjxonvnoXEibor4Ban6LMfPTxFm_cMg2OIFWTi2ON9xXU6Lm-CCMrdA6h9XlqTlH34jWqVEcCwXJGerXX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebwqC7Ol-CDfh-WZWGYwIXz4WawfnyKgifDSQYZt7P6SYOHqNkVyJj1BxegUjaKrMaHbLzS0I7BtOAP_e8443URC-WtomK9AITStxk45wm0TiOboI1s0LI4GsIAvpF3vKWKemxte4SUxgCJgKjJJtqo3b1z_MaCf-IztV0-U54ohs8W5veybLBJKgIXIopxLVv5QzJdPYDsdbRiljnoXSTXNT_3WfvivOfiEfV88EKjtrRkoubkP8Vj22c_2VpGDmHO5HnPLKr9dqmLaVVNFXQfutB4RrDHfxtFpyGyXJ0Wdwk338iLty9HvUSDRFy2o4L6XILnM4zcIx_9LcQaqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npHMv7FK2LntVQIyKaj0JBTCs9hTUyRUQ5RY6WCmb_4ihvxPDRdPM2azmUI_MSZBcgo33KiZ1NQcB9iz_IayhusPldYiSuVu3hlHn7YvngHSFs4qG0oHcsHWmUQEcJgpmUjGVethHKqUghnANtec70kDapqhVEDOGfMvXye4CvlwZJgdrRKOKxm5d_hS82f2CYpailp114BCH3lZrcI2LN5Kd8vW3ZxfE2Y-G_gEDPVoeWQhub2NuWihaZGe5jUYNBBmYWBD5qwIKqR5ljjPcOU3gpPwmnXRIc9t1HWfbMaltIIu0O89MShMklRcMJWsqk648bAphW2QimcdBnsnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=AAvAjJE9IANaNO7VEe0jUCK6c29WBwqnhW6oho0MkVk58_lVY2qQgdRi4tCF5sj6hbnFyjjzP5etrPkzRoV6pXopQKXslaM4SbmPx_NWRx6-MXzhL9YX9xJe3fuz4BLg7e7u1QZuTs0LhmsspH7uke-U_YnMGJiIrEttZ41DFoC0XJNfyS43fzvfbvd1Rtwnw2Le2cJXb5cHGx35-EUm-fnlHLW-qjrbvjUwedXUrOKqH_iqwcX-Hv5lcOa2-UeI2TFvZ_H3kqHwucD1I7QgC3bwRSGRn_nyUZHzHzeFxNyg6Q69D7963rHUutl8trEHFRJA4NlD-Gwj561K-tq8lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=AAvAjJE9IANaNO7VEe0jUCK6c29WBwqnhW6oho0MkVk58_lVY2qQgdRi4tCF5sj6hbnFyjjzP5etrPkzRoV6pXopQKXslaM4SbmPx_NWRx6-MXzhL9YX9xJe3fuz4BLg7e7u1QZuTs0LhmsspH7uke-U_YnMGJiIrEttZ41DFoC0XJNfyS43fzvfbvd1Rtwnw2Le2cJXb5cHGx35-EUm-fnlHLW-qjrbvjUwedXUrOKqH_iqwcX-Hv5lcOa2-UeI2TFvZ_H3kqHwucD1I7QgC3bwRSGRn_nyUZHzHzeFxNyg6Q69D7963rHUutl8trEHFRJA4NlD-Gwj561K-tq8lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPi4Gv7SJPPQZPmiY9FmGj7mYl0SaM3Wc5BvTJRJFJNEcV6Cd7fwSbu9EXEz-2373iQ6BlKN1XQ4xU8W0Mv2j2fLXM_XN1tfgNtv5b44-D7Khourz6M8JU_c9sGHKWHAxtoG297BKmxWd2VOxS2ut0YLCETiD6zL5u9JSOgWOjxXTOK9c4HjMMQwsqx4RDB4hpvfq8t2IKuqClaXWaAuZBYtYyr2tsKoeQjqdc2bBPuwijrcqpJ-tp3AhX0q6Q82uDMSHxRm0pMiYIEfk0fcgJWd6bBvMfCWaiXRYR3kekFB5lrgZHQjO9R_0mgt5oRVZ3BVcx6W7XGLws7PVSPSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRkvqwp4FEUyQY7JHN_t0MtxGGpQPxQpThWS4HOfUh3eBXLXNN6RulbQrDJC-kU_-Gpe_e60cvkzsGTJuaWFXqOw_ejEVbui3i7ZhEDo79uFQ_HEhlpIiUP3tYubLhWAXCHMx-S3jxswijccijZNdKYzDN4RwJXwUFR7VW0yRKuPBB4cDYNj6ytby0-uNKTfjntUOgDdujt74oa4W2yOlgfYb7mAhxi3h4HK6aY7gmT6Ec40PrgbzwJhg0ziJDnYFxFdmLNjDOKo3ToIFep48aqfz2a0VZaERAyff0MesKT9AkMK2qOuRgACrRlX9GBmdjgcDZ_aeKyqdRgLtWAk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1-Hq4TkZYryikRGa0mDh3TX42QFJZfM4YwiDa7wPEbPw3n_VtWg0PftZNozyf--OaQTDpr8ymeH8ew2-KVuMSLALRtny7Fd7mTF4AY_2O4jRl7u323NHQxAHVr2wTIQyQj5124pfy8NIEeLkhxoNvILEWqw4_M3HI4mIpSHhfxhJKpHaIXmQWOUNCdXXUAt9RWxzIX2j5kFGXtNxS1ORqDijrWB8EvEDzE6bXIecKWelV_pBz1jnNtHuLCiOZsH6juV2F8_4JkrBwmZR3vS2nPRloaSdH_uwm8J7gd3iQfu57sWnouQAgcT-RjM8tORKXwP4sOt7az2bUKRzttXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klp17_7kGFpexbaxlygFwFjtcrEYDWutXok89SBER2rjfGXNtaTM5NISq-BtirM0gedmmhCgTA7-UYXWwzpKueuzP7Jb9dZbNVocn96zxiWyqTl1zUKQBJf34Uy5kwfxATBVgn8xla4XUniAP338x1RITKdy_Kr26kU9U5YdGfMt79AcCevj3KykUne0X2AIJHcRw-1PZtk5uMNrUYeH-qdeRjwrEsmjtm9YRVdG0D7ifyutKCcWp1Fd6wgPD-gGDaeswYs9pdW23e5CuitiTcb3LRnjdvlQRM2mqrBV7Rvph-4vvp0Wcz2jvmUcYZM0H1RC-hvpeSfI0eNo-orr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8sRsbWdLNpUr66bJ5ER_a9i5s1Qj4XPvorqvaiKndHqqm2Jku_uJ-B4S5wj0BrudLmXlXDREtbzmrVqoA8oRJUpnRAFVf6eFRk2LFe7_2q9y-GG8yP2B4lI3EfNpZbMiQdZdRmEc0i3soe5vPBgKOUmmANIKjfRPqoBwhMff-4ZOI-Z9gcc910xU2QXG6kD-vq2Q0VOeO5CjrvIceeddomUvjVafzFTBz32s2lRSPVNH4gPvnwZKzEzs8lqU7LWMWVB_iYLe77qbYBHcCuvtDOfu3orYZM9SQMae1NiAmKbD1ZvWiSyZ0LD_mTIoqOM2ZLrEWTczXx6aSGOBOotHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=XILCxnx55fItEmhoA7r8ra0NbnbA9YuhovnTEKSqzaqM_Fypatvm4azQA14KrCbWUKwk5EBmY0RiTpUnkZmRQDnwE_OORaunYzur2fQrhcFf2L-ujh47WgtAyG1EC6-X0qLehzsXZsg-d-9v9SA3MRjteQMJojmOrm2x2ue2-3usqQfIIKWEpUF0ShZmSGbPkik6uZpyI54DP4AcPCpvYXOolzhAvXUEz9FhJRVp5mgRD_nFEeoAbj_uxm7-YZQmIMC6HWxCsGMVsC6G1s1VuL-FfRTXHmfTnEGz8Asi3OLeEf_2NJ3hO4R0-mvIFNR_rM55TM8PxgToVLrOEvekQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=XILCxnx55fItEmhoA7r8ra0NbnbA9YuhovnTEKSqzaqM_Fypatvm4azQA14KrCbWUKwk5EBmY0RiTpUnkZmRQDnwE_OORaunYzur2fQrhcFf2L-ujh47WgtAyG1EC6-X0qLehzsXZsg-d-9v9SA3MRjteQMJojmOrm2x2ue2-3usqQfIIKWEpUF0ShZmSGbPkik6uZpyI54DP4AcPCpvYXOolzhAvXUEz9FhJRVp5mgRD_nFEeoAbj_uxm7-YZQmIMC6HWxCsGMVsC6G1s1VuL-FfRTXHmfTnEGz8Asi3OLeEf_2NJ3hO4R0-mvIFNR_rM55TM8PxgToVLrOEvekQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXX3NMzBDYy9xgfCDhgnhgFCW3ljABY3R1iIjx8anfRkeo2XuwJtw1Dic0k-u4Z0_201zGZ7YlbMwi8HsJh9z2IpPKft-ZlU-wVp5i_aULElaWSh-8Txe91TFaAb7ft9LLvw0HaNVKqmd_XnuwZBmMJM-TnIw6YbP3daqUg57wPDpcZpwPxUgZK1KH7vY2pBCHpgG66eBxOEKJuYU0vEJYoAwb-_olwB7FhUMSScGdN5w2T3Pa4R-8o24oPT3sTxuw-9BQnV989heoXq3wnhZo5TcfuVc3MjJVKf3ma255XjV8Nf6r5PEIhJw48rLo5344MZ8EqjA6g2J_pbgycupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2TFNj0mrbnKhFeQXIhDY5HUH9yYTxoExjBVLzjrBcvV3F88XYByORCKOa_gBKdS_X9bEm6qMSAp8y4IvEC4eElRyTSXhHqZmi3A0KLNsbEV8tafPGsU5uMu-vXEyqucv5zeB_VhhxW0_d17lYxVwMDxPJtn_hKzdzL1skpS_1gMtg5iZ2oRDuC7ASXbovl6iVL1m45LB5GUJuxBoC1CHpxgO3ZCsE3pPg1G6xJqpVhHDwsGD7-TDWpWK7QqsVgjYkNrvoVDla7XNOR-RZI2TV84AAZwz6yPX03kYXKS-0Ux5pMjt8N_x21fjM1DJmysyCJWXZ3zFa0ahNDZ8DY5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=QwjWpGd9uFFvjqdu1c3Dg29Qi5jFcssXR6z-HSt6_i_CXw4i6e8_1W45RP6HWi2JtSVPXnRxnVt322UoXU-CJ1HjWz-LKUhVhis9ttyKnVVEvzRLBEczxv6-HE4T4RGZHBE7y3IYTvXNhPXchQlvD5fbnkmpPJrj9jwLBA5uN8vzeG46RJAtFZGttgwz8VudFvboOdYoi6FK0gTJgRHnCiZLJf_2aeNpT2LCNjHMaDAFZoiZKDVg8g4Yd5CrMs6J31xbdyx8NX4MZk8RoDEi3_gsHGI6eyY0XlpbRL55V8bipGCsTcYORa8rGuSVxJBDuDIUisxBxCDVOY0HFQrh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=QwjWpGd9uFFvjqdu1c3Dg29Qi5jFcssXR6z-HSt6_i_CXw4i6e8_1W45RP6HWi2JtSVPXnRxnVt322UoXU-CJ1HjWz-LKUhVhis9ttyKnVVEvzRLBEczxv6-HE4T4RGZHBE7y3IYTvXNhPXchQlvD5fbnkmpPJrj9jwLBA5uN8vzeG46RJAtFZGttgwz8VudFvboOdYoi6FK0gTJgRHnCiZLJf_2aeNpT2LCNjHMaDAFZoiZKDVg8g4Yd5CrMs6J31xbdyx8NX4MZk8RoDEi3_gsHGI6eyY0XlpbRL55V8bipGCsTcYORa8rGuSVxJBDuDIUisxBxCDVOY0HFQrh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmyf4Ftg8M4X5MzrXeGWV7ljki0YYYIWt1IzeIsVdJntVlC0mktfJ-jn_uWDBNCnXZf9SYygdq27Er8sQjTBr97tHZBik43JOBE-4eVmJjvKLMT-i7K92tXMboJV9t1dQ08x8Y72Rav-S_TYnZz3ntwejY7-D9VbL1fzgxDAnYeRsdjYQXZtLrJAu6ZEnDS9XB-tPYREogP0RnD_OBwfZkGD3R1cDgQLbIKdZJhqwRiWR9gEjbef7yF5DC8-DwxdWoV5rVDu-Z0OgvIO9Tihy73Sws5RgKPB0K50D4gxVzH19jcTsTn3D9sPilPwmX0QhKadxWIC2efqSVjEXzxjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEsBOkom84dxwzXERtCO3lVD0rt-mq99pBssBb5_2KjvbgBvPelM5lugqdIJz-W8xPI-AisZzN2-gaarmUgRYIFq8lPCxbaVycZROozR_Lvdr2TfaICwaDvkqndDOjF-DNHyhZ1--dvA8PBYjnRpt72S86_4RlidBjITYm-vDvrHVnjqiilbbXhlQ6_KKq8cSn7IYhfqYOhUcfdSsZAPhBTddZOyEA8pRIpKTsKAc-ZIjMH9p_XI1nGYt4ozNM-pAih5gVC_kv93T6M7vIUY7MA5FeEPcpi1-cjDUI7I1ZUH5jPK1aiNmRbO-dC6Z0lP9z4Kc8zhtB9be0rjuFijBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTMp-6WpGbAOlY5EkdkRHrRRA11C1zhAVllYt69nfaUcQltWhKVvwJAumVCjXuY4VYtALCk6FABGarPWgEVNeenwWeoMM_AwQgJSsvHbs8Shj5w3JLHIimA-frjgAI5ptonLsVAUT1XYQOg5cfAZtBS1Lcnp10CsmS_GOBDrlcMapJ9s3JFNVmmAIlyPdNaHN_7o-7J6_DtlIaEKV7bRx5SxtmcndBhSM-ol7OBE9sV08jvG7Us73mC16lbU1jgamXnERWOA1mv4hDSrRH05Mx0v2Uwja-a-1PMe-fqHZONokbsASmhBuEH1kyhSZ9eDKGmw4omkm5BAGzLkeUnxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s47pjoFF-PZBczh77URTBekTKBLhz6ucAzgbtpuM31Tr2awBAn0aSOYOQXvYZM7OUUrBCmJtOxaXs0OuboiAs-uWZWSbvVFUplO4I9bpRv_SDEi-siZtT5O_WcebGrsdBfOT_-AVOAKzFlocGJ4CxEsAZ_qtywl5vfA7Q6xFoSS0EwdPlD3I4cK8cFSJ7YGppQnpDNW3X4CYfQcFWgnE0WXT5518YjQhHaH2EXQolohz9ZButN8f1NLabCIk_Q7_V9KLr34TII2MvQrdPownmg1LfSJkHkjsi7e5uE_aC-oe1o04yKZxJoGoB9Osx83xH_3hpuOTo_9XMBkeCu7jfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeCjd3vlFeOGrpmdQQL-4ZeUdpOgtHGk-bFOdwvv-GuBUgzWg6svcDIPiHM0QNFRZr890Erc0atpXoCZvIWhLSWxmt4aGuyEpnWOQydimsA3YIvrHsvqz8EKN9uXCzCUDd0bW5DO0H-xMhdqFdKU03TsKHa73u403mXlKRYPOxIH5P-VDgGMjQBAi_fXH9CdIN6Qixb5cOWz8eMhhRChB2vQy8koBfQzzeYJFN4sq9QDs4jig8YZe0sq7h9N-fcpQn4p-DO22LuaVZ2Ar5vNX3wsnx056UpYu-E-0ZMPMPgniEupGqZ7Q15AeoqAIxLxgwLk-TsPiJilIKhdj4ZTSvPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=KfiUD7p9NB5s8kHZ1I9t9Rk6zaTBzJXRzB9Hx2nZrRqnaJQfOWOmNdJJipWgXoD8yQsxkp54gxTgESMAzk1vzOUDI8ggtxTwIqbhqDoyqVpgSttfgo1vdJNkdSeKGfllacFvJTpPuGoDILrOR1UYIKuP9Z3-IMYbd3a4OIOSCrZ-Q7OfIy0Es9phyN_ZvpTzFW6634h6_vzlq0AjboxnXM7lT5J628tvb2cLYxoFPFlTwHL3i1Wr4pGy0uF3yCWF7YpEzF6JgN50sHJMrzEmSEHgbsYQnpAmJt_BuiJO-rb5IExyt_6Rjo40yvKl2jJT-8mPybeJVCZqtGV3z4QWeCjd3vlFeOGrpmdQQL-4ZeUdpOgtHGk-bFOdwvv-GuBUgzWg6svcDIPiHM0QNFRZr890Erc0atpXoCZvIWhLSWxmt4aGuyEpnWOQydimsA3YIvrHsvqz8EKN9uXCzCUDd0bW5DO0H-xMhdqFdKU03TsKHa73u403mXlKRYPOxIH5P-VDgGMjQBAi_fXH9CdIN6Qixb5cOWz8eMhhRChB2vQy8koBfQzzeYJFN4sq9QDs4jig8YZe0sq7h9N-fcpQn4p-DO22LuaVZ2Ar5vNX3wsnx056UpYu-E-0ZMPMPgniEupGqZ7Q15AeoqAIxLxgwLk-TsPiJilIKhdj4ZTSvPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhAdbbxP-6313fafv_nnY6iePvEhN0OPPJxzf91ueNShCjxvl4e6moKf3sVltMTouhzf_RQiKOYmqHX3S6gtXXjZ2PIGln5nlBAhz6VmUb0W5UY0sVlTqQPIVC_GOpDiykDY1ZG7Pr49fddqFgPZFjiOdkbydN0699jZM0k7oRK3iREgjdI16_I5IvqeVqzmrFOFV9aweQfOx67TF2sags7031_419K-6npE_owvAiN0BbJ-by8y-H1qoRDqeConCOCN7AQwunk3VZBonH1BcD-e1SaKO0Rl5CnLNB9E0dENZ2VtaEUGACpzqqB_UBkUDldGgcKS6roc6jB56t8j3nkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhAdbbxP-6313fafv_nnY6iePvEhN0OPPJxzf91ueNShCjxvl4e6moKf3sVltMTouhzf_RQiKOYmqHX3S6gtXXjZ2PIGln5nlBAhz6VmUb0W5UY0sVlTqQPIVC_GOpDiykDY1ZG7Pr49fddqFgPZFjiOdkbydN0699jZM0k7oRK3iREgjdI16_I5IvqeVqzmrFOFV9aweQfOx67TF2sags7031_419K-6npE_owvAiN0BbJ-by8y-H1qoRDqeConCOCN7AQwunk3VZBonH1BcD-e1SaKO0Rl5CnLNB9E0dENZ2VtaEUGACpzqqB_UBkUDldGgcKS6roc6jB56t8j3nkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1W1xnmfa8PfelV06kz5mfQgunSX47Ff_v1MV2MRq5LbBCDg1MN07CVqI8Xrb5IbYhoXRQ-OvAIsPoTP5ikH3M77JShv8cXzeYCwWE7UT5l6HG-W1IsHnOHdOhi_hNneYR9QDrne1lkupW6ESV780lWLzTR1rgy9R_zAN4paZRLqlyGUzmTWF13fZy7I2SRkppctfjx1m_h7rviHmiQJizXANXe1C9I1rxi5vga-bBJNrq42ckZZtv9xywHcSKXTx6De6UeTGOThiWZRD-UZP3lnotP4smcyNeZzG4hc0myvFMVF8y7zdtTEMpcTKPuc8SNIuuYayn0HnDloIU4AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqTgPsQHuaE3yeG7vjMKVXxXV-4XjD39ZIyO7Z84CLaIwlLEqoMYAHdc9WShQeL6MdrB1tbn2G8vD9AKSFIJHWbAitopGCc088KvAtIoa1xkLYlnUEHkpgjKLQ-YYlHUFtyNOnCgwIznCISmHpICUZD7QKJN29gVl8mYg4H9uaNi9MNl7hXZ5-XZuRvG-HVHeJaKg0MRk0dSKSdt-Mf6Asic0PIs7nqcepHhkRaZGZDw-40bmREwLNhucW7n_eMlGCBJdlU_PtCcv1kIMBW7SrdGcbKz2Pn6EeY8d0T3s90pTSDJ0WPlq6A9yNI3PphZbG3ae16-W3bXZNaRO3Cg7R_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqTgPsQHuaE3yeG7vjMKVXxXV-4XjD39ZIyO7Z84CLaIwlLEqoMYAHdc9WShQeL6MdrB1tbn2G8vD9AKSFIJHWbAitopGCc088KvAtIoa1xkLYlnUEHkpgjKLQ-YYlHUFtyNOnCgwIznCISmHpICUZD7QKJN29gVl8mYg4H9uaNi9MNl7hXZ5-XZuRvG-HVHeJaKg0MRk0dSKSdt-Mf6Asic0PIs7nqcepHhkRaZGZDw-40bmREwLNhucW7n_eMlGCBJdlU_PtCcv1kIMBW7SrdGcbKz2Pn6EeY8d0T3s90pTSDJ0WPlq6A9yNI3PphZbG3ae16-W3bXZNaRO3Cg7R_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeKw7WICgMD2L8I1njwcuywGc_aub0acXRGpmkZigDQfWL0gRn0MbhCLn252Eyx7NmPNUzZErvVIwss99UulB2rG_O7T_1419K09BdbDJU3dzzv21hp0NJavI0m_IbjU1ZXqivJEkCHKK4bIMs4qRf82Poq7Y7tz5Ex72aIkjxt2owaU2DUfTHE9F_D_yBx1BES46SfcIx8o2v3u6d3zrGZ5M6Ob3WUxIUCALHRmCdfFzZozehHyTZEcroricmNYnroKIjK3Rqbw_8GiewrK2e119PQHSLxZv17xWMZcq3ug51sSGs58tgX19GqNE71pJZaA3eOxBFxCl9mO3ELl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=aqr9buFhg8Gg9ir7xJdVuEsp04WUbYqHD9ivDmFwdBGVRwQtkZ87sLcsAprIDt07IoMIpzidEuszSlLXsnN3RzTw2NfBbycCsLlDD2dR6bww6ftFT97QWjJNUZckPaaXikrl03rKAcfObVkOAjZMo9tNhpX2y7UaErun05ddI1arwud2z3wy5bota4ap90_Du5k5il8mzvupKj_ZTG3KwTR1SUgUlcJHxGcMWu2tkxiC-UdTN7OgZs2lPP-2TTlA2Qxu8VcqrTj5hqvLowoOVAVGf-ppHZ8wy6qw5UV0Qwi_jG7bFN13oSKVCRfKltQNHJyiPvDpRkckkRnduabcC4xQs0iJ2OHMSpkINGk_bfFdXEHRFQ_Sw5jV9u0qTTh8nnn8HcXURASgzjOszGYhXtuDEpwmiCx6Ma3t_pzngta0ExEPJRY-kvNIUNyH2z6D4lyzCF6IiPx_OM5gnr3C-tF13CYo_PK1g2SjLuo3sM-liEZgLq6qkpZ2UnoKWz7R9Mo0GDTkpi6mTKrjVUlamkWZMcWnkXPnsnanFXDR5pmlZulyrJ3SvrWnRfpSDzVRsFpThqnbE3flnw3Y2pTk3CnhsFdnE3sstVj0C5sorhbYhtJG0t3VL1oabh2T-XSAKnWUqjATUIYJD5PojnSvHwkslnVXxEGi1YLRYS6rvw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=aqr9buFhg8Gg9ir7xJdVuEsp04WUbYqHD9ivDmFwdBGVRwQtkZ87sLcsAprIDt07IoMIpzidEuszSlLXsnN3RzTw2NfBbycCsLlDD2dR6bww6ftFT97QWjJNUZckPaaXikrl03rKAcfObVkOAjZMo9tNhpX2y7UaErun05ddI1arwud2z3wy5bota4ap90_Du5k5il8mzvupKj_ZTG3KwTR1SUgUlcJHxGcMWu2tkxiC-UdTN7OgZs2lPP-2TTlA2Qxu8VcqrTj5hqvLowoOVAVGf-ppHZ8wy6qw5UV0Qwi_jG7bFN13oSKVCRfKltQNHJyiPvDpRkckkRnduabcC4xQs0iJ2OHMSpkINGk_bfFdXEHRFQ_Sw5jV9u0qTTh8nnn8HcXURASgzjOszGYhXtuDEpwmiCx6Ma3t_pzngta0ExEPJRY-kvNIUNyH2z6D4lyzCF6IiPx_OM5gnr3C-tF13CYo_PK1g2SjLuo3sM-liEZgLq6qkpZ2UnoKWz7R9Mo0GDTkpi6mTKrjVUlamkWZMcWnkXPnsnanFXDR5pmlZulyrJ3SvrWnRfpSDzVRsFpThqnbE3flnw3Y2pTk3CnhsFdnE3sstVj0C5sorhbYhtJG0t3VL1oabh2T-XSAKnWUqjATUIYJD5PojnSvHwkslnVXxEGi1YLRYS6rvw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4ohDfl4yo26emzDMtRHqXYx_G3QwyJLr_9MgABquiTVvjmT9N9uh6KS-IMgfCYT8e_FvTr_oDs65tcOgtf4eVD_i-PNOTLaktQ4x4_q0rBNNufj3yHZ9Br-Wllp9h4wPB5TmHXI0dgLYujmLV145kx6kCkD61iMU7wxOxchMhZG_dRMGWQpyeHQI6sMzjAf5zkXkOEza1IFDjAYn9mFLceTQF7GMjJnegmbwE5EZxQMG2lZFX4E0XtLr64JsQWWHM-Wg2OBX1TgTc5k_OyPnXJMWCZbriwoNZ6cAUlx7hnvj-wXOfcLqeMjmTfj4Tctr2o1ZXBnXpmSD5U8QIuE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY8XIXuzl3X54OEaQEMZNdNiaTYxOF9YugdtCKvS9TYCmlESZ-HwwcLRHx-hRNHigeprBdxMHrTP7oXNys2Zg6fE1SXuF0v4GwIUT6RbModx_Ef9gExn7Fq2h5YHAr6FroUkyMJZQZWQX7dnMhpbwDrWMFxQRP23hupCE2GX2017jmcduu7HoA0is_TQqvWcPxOWZCLXRDSpkejkqnc3bHkKHXHxnJxNSTIJDGNnGdM6_K60dyy6DRrh68E5iX5mqdgBODTOWqYT5Y7u1eFoKF-wza55J_Q9Xvu1gTAqRQhEVKXGsCHtRB7rFMFor5lFkwI0Ot91FmP5fhCCDWWjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joTnv9JEKuL7bhgUbu94R4WaFZ-J49B8-o1i9GEYEU8AQ5rMqSHUA4j20I-uesF2JbRd-PyrGPLgyd8jiHa4AtU0HVYiCI68JmjlB5TvAt4EKQyj-HMovl5AOfeqBAcR8WSKMBztFGhVqZXQRIPgKab2XsWu614R3uN4kIXybuQTIz7f7FVrP4_XGbixmEw7JLFRw-Q6DXMsTmMo0zvqmEum9_puL_ZZ655SdV7o33tr55_oWbN7IAFwfQAikldtc8Bh3fiKtWAwnypg8pYOr6rsoL4zScmyhSPFGGHoQxnzhhKQ4DHHPGGdooGtYICH9rlif3GDZ_UqJw6VYXjb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKXZ39Q_TlHLMi43YtQqaeP9qsmfZKUOBv0-TLvBEy8hEKJSsttGBS_JxXckUhiOGdenlIT3DXCjxIK9fcq2G_Nf1_5WO8oKZ-FDPfJE0158cSVI9ftdoL5hP0a6-AJbyDsjkuJK-d4chwDpm7KlmVtURBYvynUpRVtVdOuYtzUb1YFeKKmSRFy-vgAUAXpVkJW1QJjdPl_gBjAxsWCtlVNflZhiQACNOTnSHCtCmDu9pQcskVI34Tv45PhJ2yFRVeADVE1Yx2W4LEKpDuraDw6SPLDP8Q9aPBd48inpK9MQ0mmCwg6l3Jx8dAo0QP6oA8jn70gg_3aV7qrOJxH-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocd1gum0IuKk85sumK-LHVOM2VenswI0oMfrp_c2qbRyuH7AoHWfqkqVWkyrSjasnilq7fHqMDPVfxGsv5ymIDs9pv7ZTGrO1M-gYCZAeJStGulfO5vaP_414x7i2WM2jtwtEuNfNE0HxOCCcnCXLN9yccqplPx01jJ-_tg-LmYWTe_ia_twkUarTi4xBgcCWcgVSzBfgf_GhEyPenREqbNiHyrgYau6XYNjizeNNXFIprpVH9zt8oDTiMmmApgZA8NylIB8VkMgF1rXAioSu7E2s8x0-waOG5xmFVlYWq15TxY1TJQO3Pd91VBufsWN4XEKjI4QFKAQUOrXGaTtZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE16HDDWhUa-Qi9tikQey1eXDVsREeU3KbFLFp37vAyjvYmBETa2HPxsdJkqjLOqzj0yFPu8VO9B6F6tcgToCEzgoVMP9VNrmcj6bIHshu4H1lb9QdPDQaZjg5_VGyKmajqDYG_8U0M1-7xJJDiB6VAumzUZBLh1zFKanRa2tTtRyWwqiDSqlStffLWpVYEFizh_Q3AIvQDOmwVfbBhw5A6I-ofIPrMJfMt7azM18tR-J-eapkZZs61sZiov99MSYy5Wh0AvpyZ4b8q6v416-QNbFyVMiP39lfbnIk4caaXZhYxfJIXnQRIIVfboalxvqWdyPEshqvAhBMowwSYlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtRxfxlIOYVLCL3ot41g01Qg-DK6cuTokQbiHzj5iY4B-VSGg22ZRIS4h8zc9GRIPnp8G4CICZyy0dQMR-xtIVszN972bA2pPBaSmraD3QXDDDo8hrPrFbXtzWsbELKGH6y52shp1JPu1lE344Zhlm_KhtHpREqR4rkvZYluS57lOM_L7Rmch_f-bc_apD3QmCeXnVeUY6w82P0iunUHmTzv-N6LKIn_1e_yRLP3jlOBT6XoZcXxvU2XK9vx1D0uJJ9_3P1WCLdb_CCRDWGa_gLWZoYyzsUOW3MmS3row_XzkUhVOvOvFSpGwMm2JMy1-eUYEng9jMXxFPFRKqYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE_EO7Jfv1MckO9yot_s9cm88AB9zb2f9exaw1wxVvOiynFPaouMasmH10n9VCvcEttLNncQ61VGNo0SbbdhYVlB7i3vmUgJL1SAZKYr_AXsPP0iE-tKHCVWEDukwBgFDRIiWqDvyw1yRDt-oaddmn6z8gMm7IT04bsm8wy359XrK5tQXprN5HWn3ByYX7VYY13c6TcvzqWAtWXOQvZggHBensctjHBZPFLZDt5_s2NIlDDKy6uZmcGz-b2BF_f92aiANCcEOsGuVRxbLkSSv5poccWKk34HQeH3v_iZH44ybOxV_DGcTXE2_Sxo3UO5wSx8nwH3BSC00lSHCVoNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECYNK7YeZZYsVwZM6y8RcO0vYUgAQNv-3bSkIvxcyZ3xmlDpLFbBoCmqH8w7sB8HA4swJ-8b6EusxGJvyuF5IaAxFi2VYXv0cnLKg089Eky6TJfEu06ThoukXW2yRCJKv_d-COtl7Mq90B3rLnZnM7QVRp8l1nZNsQoBoOk-X309yTC3Beek5TdtZLxevnSBOj_NYBOH43id2b50XWEkKW3DTriFG-dJ0wpDQNnhsDCoOgeB2JFO19aKKrloH_5QME4jOcPDKw3MycT9OFsqRk3lygU13LWfG5YYtF5Z5GEIKwxwfh1Gfz6WyxeNc0Y_BoTj5qYzSDIVkhoUZbeXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9yC8p1jam40cskZrQF5Qyx64mAlQtLbbU0BfGdxx6UpoJogvD18kjP-wufaFVAZkldkj7r1fGVpkfDYatRW1UUQMLKsrItMmiF17_qP2Dly_LHvixlVRNAtGoJQNocP6ETn0OzbvFMFk7mUhci48BWoGyiG9d0Qsxi8SiuZXyVYaROZelEtt7LCJCam0jb1-SUnBzHT_7QQ3a_kRxhRlqFr9B5d13ilcNOC5Q0DL-1mOEVN1yK2ZghIJ6uxw4u0ngoKNoJ1qeCFSZQl93o6aters0mlvnYa3n5ZGBswVXjG6om68I8rvUYlrTaKukQqErTcKmZUqzMubJBpVKsqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYbrRyKOo3ZjfVhSwvHbo2nchcWusI0FXP3PRTNh7-2A-uQO9DVX8TRL96QSf2lm1SJJ6p-X5N8T5QJ04iRlTlKJQPTJ7F4gu1XYfgZ3nF8j_58s2Q1g0YllVZXeNuV0bRAYHcG7V0MLN9dJmBYGX-9gejCeSwHK29d3MRupB_KzakV_sNZpHFK3DvGUJ_VwJFGeC_EdQTDZ2_gKmFLu037KE1xEtoJv4VhZtPRfcIvoCOkQorVmb8llDVxIw1ol8_JbE1oFC9y1BTLCetJ1aYTLmBAybMQcRTOBY2Nrvu2wbVQ8WcOvMv5Fq4p0JaW1JmG4e1ZCxq3n9RaVvKZBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGjKtuKmbOnix75iiJcnv3ZFbLZBjV5dsmWfvkuK1e-g0UZn08hClnfU93LsmPmhGQUz8GfcWKgqpAt8TNI4ABcH7eGm16m8saQT7HwOmrqwLvq5PpDh7YoKCUC5AeMxuV8hxAV_o4x2cnV2DDnx6jLcELfpBjYizgo5xjHhJ2wiIh1ZSVg2jHEX5Gnfc-Nw-LF_E4g9nVhgXyyBSY9D140AZhrxrTGX0XTLwx0UGb5Ou1ULXZYt-gtCbIAYLxRyRBxJaqbjOJ7ymQS0Ia-rEFMeI7LwtclAMV9wzR3MXEDy7oDlAcl1Z5frxnFEFZF8P-zSu-zSAgG7qzsBWTVmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=tntrKOzxkWJ45QP7FCveNGaIkSyDCFBMtRmGX4XCI-hgybvoIyiuyqrY7k0op6wLGGHtyMZWpEy_Nd3QuzNpnjO6xSwNuMW1eet4ytmczQnqRrG4ajqlIb4vhswdOwguFTQEj4a6JRbYyo0aUn7nMdUICoS33ZddsvzKxzmBRf2AE2o_ViH9rezhPr0V7KgB8XE5kWLBxBV7m4qfbjnTW2BygIsg70087q2juUotxAVy_1-dKUWYNN78ifVOAnNtOdN4XNEMNIp1tv4YOsBjR5m6iTFo88x9Pp7VexQf6D2pRcyYsF5xiHI0Tq2JF-wB4lnFTuqLq3Ya_SQncyqS7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=tntrKOzxkWJ45QP7FCveNGaIkSyDCFBMtRmGX4XCI-hgybvoIyiuyqrY7k0op6wLGGHtyMZWpEy_Nd3QuzNpnjO6xSwNuMW1eet4ytmczQnqRrG4ajqlIb4vhswdOwguFTQEj4a6JRbYyo0aUn7nMdUICoS33ZddsvzKxzmBRf2AE2o_ViH9rezhPr0V7KgB8XE5kWLBxBV7m4qfbjnTW2BygIsg70087q2juUotxAVy_1-dKUWYNN78ifVOAnNtOdN4XNEMNIp1tv4YOsBjR5m6iTFo88x9Pp7VexQf6D2pRcyYsF5xiHI0Tq2JF-wB4lnFTuqLq3Ya_SQncyqS7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgFubmiBBz5mV64ObfpwwnKf3CMJjDuGOdbdEVhluxGAeGmRYLjNrquKs7jWdHIBAt_YGShO0vogMrOoO2-tTwgBg5jfMOFBnry5RPApNqJrBj7mczHQuf0ajHJEXWozMhDv3k9yxNU8Z4sx-M3QW0-VuJaJcH9uc4HCouudNulb_8C0-pxHH7ug0Y5ym03rcOZainsSvviC46x6uAPZMoqlTcO3qXx8lWSQLaYXomTdCfCKJW0BXtBjDaCbuFr0H1Wxof7pDx37vOQ2Z8mlvmXlXgzhcJqdiuqdbO6M_-djpY92KZke2nwGhHAVy9Blb1jcZIijQi-HGAMBbeFv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dEhMMAE0feYbeveExjY4WYsUFw1aH2RETEoxUZsOhi-fALZzpl_VTpf-NX_Zksesjn-20Htbpjlwk7_5KUH-gjlYxjguHJqQlJrO7gwXALBaJoJsQlOfVoCIhRjyVQb340IkMRgIFOJXFNvDEcTVo4xxtVaDNJPee7pypflo-ME3Y8zsaJLelZOs0S6NxhtFm8mO-N2mmMJbm9p3Dp8uzy4hsGHQkNMwxt7CHJfGSn4ckakT9g-EUL6DXsK7GVNYl9XENP0auWOUi83P0jLAercL_spA9ndX1gIHUJuiFSXHwZmk9UD8yQq1GH_Dg6tFdzWtMph9teF_E1MRUcJyGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dEhMMAE0feYbeveExjY4WYsUFw1aH2RETEoxUZsOhi-fALZzpl_VTpf-NX_Zksesjn-20Htbpjlwk7_5KUH-gjlYxjguHJqQlJrO7gwXALBaJoJsQlOfVoCIhRjyVQb340IkMRgIFOJXFNvDEcTVo4xxtVaDNJPee7pypflo-ME3Y8zsaJLelZOs0S6NxhtFm8mO-N2mmMJbm9p3Dp8uzy4hsGHQkNMwxt7CHJfGSn4ckakT9g-EUL6DXsK7GVNYl9XENP0auWOUi83P0jLAercL_spA9ndX1gIHUJuiFSXHwZmk9UD8yQq1GH_Dg6tFdzWtMph9teF_E1MRUcJyGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwzuKvSbM0Ls-RdbrVWB2582QASPN1kdu4psiWtAoTDcV-D9Te5Q_MEVWWzdvS_tMUmRTpsgYne7PrsmsqsINHW0H8wlKP4fK2xcuJlqvnDNnSPG3vD2jKidmGRkPIUQAPG6wiP0oPM8OzhfnCrZRFqelSQV7cfG1G9CWvYUSfRJXXKuGv5hVZnhZGyzzZ9YNvTuF2GnBkHG0xJEUd_FwQhGqE6qOQBJYCfriHy_3647wxcW5GFWKrWnlaABag9efS1MnQ5ob3hxZufMlVxBrZ2MdHISjDIuiI98ZxmVimw3RLUwiF5pPC2b7CpfcdKEeNPh0VJU3PEcCuk6wVqE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiiBdKFEehM5autn9hWaAWDIonDoTFrx7zmZpkTgxDvkK_SwzEMIklH_jIpm_fvt_ISTYpWb3v57jlpSUA21-1e-PbtHTnav0Zj8RmLMbBXa1TcLIfk_kugjJNX9H9q_QSoVqu5gnHlp5YPYnAvVL2UUBcaFRqcQ81uDnZfhelSdtKXCnft0VDXhcz5ksZsSNQ8LvOjoBr9k1vrMp6LJWwwwhD72ynF8UNqU3DpBzvqi7GkQZ7_dbmuQpUTxF14LFK8ZNyfSE9b8-CYEhr8dshhs3S83GHYtTH3JvLy0mziR1cLyc3KKPy8ai53QsUhQUFMTMXWRQ2j1qJz9YRQkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
