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
<img src="https://cdn4.telesco.pe/file/RpR4JaSYs9wpQevFJYM07SrhxWbVTgyz9Pks-vcD1ZtZ2oBWduVIE93noecc2TFTDqTTB3h7-TdqKAh1LKEV1UAZixMSVklVZooeAZGrzv7N159Ikz12A7kmv79mIBJwgLTrCs_rSz0_76VHtR-P9TJb6uDcHqnchhGcqwsKtgm_pOMtN0txu_rbucEIP6wZIUpalWi29K14lOlVQt5VnGOD-L9Zvt1dqIKCNSFM-i0kF-eXPaN-q0-ts-zD7ZhaSq0qGlRvAeKwCt42VwTw7-I0gM20yvVBgtyjYmJptHKQRXF28kCmLMg518CpslA8pPkldvJkobjZcVBdbRq1Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=A801Jabc1P6Zl19kBHfzzKlSS9flU3Y4B-p_q5B5cWGxu2fQ-WWF9AUcCdRL7CCzvW58_yytmEpHdB6nkfgzRlkmmkPVM7yISsAkdTya3nPvhtBkJlL29pf885zRkRfdTeRCGkwKK7p_I2sfv4K_11FI6itnwh_ICfVM0xvhhbjuViT5GfsxQOGVCDPeOJVtqOZ_GExBlAre9zOlJ0PFXmcTUTJ4Az7HqQnchvGSy3ZqcbE9OQ2BzwiZ397l06WP6nyCW5nPbW8JfdNwlAPUPF3whQ4cnGws723AY52VP5lF2vzwVTRN1eJ6Sr9U2k6kbjVyVnN8DvTlis4idtugDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=A801Jabc1P6Zl19kBHfzzKlSS9flU3Y4B-p_q5B5cWGxu2fQ-WWF9AUcCdRL7CCzvW58_yytmEpHdB6nkfgzRlkmmkPVM7yISsAkdTya3nPvhtBkJlL29pf885zRkRfdTeRCGkwKK7p_I2sfv4K_11FI6itnwh_ICfVM0xvhhbjuViT5GfsxQOGVCDPeOJVtqOZ_GExBlAre9zOlJ0PFXmcTUTJ4Az7HqQnchvGSy3ZqcbE9OQ2BzwiZ397l06WP6nyCW5nPbW8JfdNwlAPUPF3whQ4cnGws723AY52VP5lF2vzwVTRN1eJ6Sr9U2k6kbjVyVnN8DvTlis4idtugDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QaU522qNNNk5a9j6N1NAh_vXpmB-KoMJgtCvVbLk8uR36sgFLys0-Sa7H9-faw65YQTfOuk1tuPOH_tdriqVW0roEdgXOFAQnIgBZHibfYWUkSY2C-74UYzoYLXRdIHjE-3jkllquYU8KTNiF-565VWud_EceoyQ3yZH0QpcOvk9HkhbDmUhKLN3lu5sXQpPQj3xv5FhboikuriIneyknBPZ1ikTaJ879FGgWl3taBNywi8mkMD2P-M1ayaD0MwNtf2-FmuV55wXNgO_Nu-pN_PGIBNV3yhr4AqtYFNGDBHzJh0_V96n7jFuiFONJhpgRUR2Mh3yFKq0gD2VwvANWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeJpz5aknrGc-wJ7yLxhaub6hFMUO1D6hU2UhBDxQdn0G0mGDIm9yYNdbcF1TeiNG_R4-fu_Ywa2XIF5Vw57In4rHNivTu6K7Sh2C2WkeS6NI1L8InbXCdtDpCxXiZAc_0p5h3Gn7DMpQcG2q_m-DqSKBAlJbDg-Czj8YVfDgKo9bPWY149_xTJ4aaF9qdo7Sk44EboWrIYZxl0t5xWnHJulkYMy_xavQJ_BwZkxi4NfRz5Vf9ejC6OFzuyDfVEx99_b0yHBw7q_ZUZijE6TjAXhdSJV8HffgukyyLRr8Sqt0SIuidLUig2C_VyQTYZ9ynCKFFw81s2G_I1Gj7D5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBlqXgLXwDG04YMzvhTKsL8cDMzhjLQ-5piGxVNX0jAxWzhdVmQdHJlQoPEGh6r5mE-quXGWY3yxKD3HxYy5NRz86OIDobUl-pnjJq0jIOgAsZSW2vbQ1DwH7JwUkQ1CXEwR89-ietuFmXcgoUhVWIRbU61n-eKVW3oseGTFeKvjkxXReCfsniocQnz586luYP-L7fhsdB6r_o6KA4MzdIAy0zl3RckuL_LqnZfWWytnDUAvD-Jwlzox4S_XG4B8mhcOFbkYNvotN7qBkClwuq0AGLS0HI_CcnDpRtMdysbb6HnloI5Z4v5qauykP49HPmYMTZX_kDbzXFA46pPhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M592XQDsZoZZp4UKAGTgF59kFjVRoIVgEiq0kX8rK44Am67e4nkMNvmKi0wW8m0SGDiw7kUC69XoAqOu5zIHmKg3v0zrFwfm0eaoYS-5nKXVKAUvjaFh2Wfc-cBKGQKz9VGedByjtW8jbofY3jZjYbReK9EEcJgk72ejSpqkqKv8rXiSeEr3DiFjLi38k-vQb91DNW4O6d6qxykueG5tlEPgzPnD39E46pKAFeOZOOiUePfY00JUgWXX9fkoRnLZV6MCNtspEd_QOD9UkE6MP7DdUHen3kG4ijDcCV7pTjY5OeInzy-YaUPJr_TqHHVTfhXLlfOtOdmTVG-xl94fSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exM4j0XS6wSrE442JzuVierrkPncziNc5puuwLvTviKQLkIZPf0EDN8PDVMHIW7CDBzsdqfe2TNdtY43rrg_2w6DHiKiRMY0zNzdmRfHSk-Ld9ljXSM1PJB4K1LwPf3iEo-Bv-bk-vKoqttueVLpz5pJ6MKB87VpzQ7KCNzxB9Tk8XXcIgLxoVaggaNTQRVJukOOtBaykOM3ekpc7q5evx35z2eUuOZwzL96Qpg0u5ANtyGj3PlqAkxQoHZjPA6eSB-QkSlK5n2wo0ZK3Dl6xS1qElcFQMYlj62kAZLXB4iwCAQIRBxIbIhAMFqpZqmHFdSiwvNJLjOkLH-a9Q-jZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=fNQ-BStKTluemc4d0cR7sbfIccF6GWvhyS0e2l6BROl8qwIYkrGxjT5xGBFXzMreu_OMOCZPYzMHv_zEgTu1tdAhX_nq_p2KIHYwaEs-s_VOihENa6QH8YyuN5-9-cdBtCYjLMsHrpM2nKfQMehkNMVgxUBAg5YfwJZ-4cqR_dIN_2O_bg_6GYach2HWc6XCF0jY4Szix98AUzuQsUTzF_f6RuQWnbQzA9b7VJJ9y2oEvOl7h3xeN5nDWf-xOgdjjNoqTrQkNqX8B_tAl5zMguLVH5v2dysmb0l4op9INDrJgn55ifu2MF9YaeRqOCaBnZCT56hm5scmC0wQ2jG-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=fNQ-BStKTluemc4d0cR7sbfIccF6GWvhyS0e2l6BROl8qwIYkrGxjT5xGBFXzMreu_OMOCZPYzMHv_zEgTu1tdAhX_nq_p2KIHYwaEs-s_VOihENa6QH8YyuN5-9-cdBtCYjLMsHrpM2nKfQMehkNMVgxUBAg5YfwJZ-4cqR_dIN_2O_bg_6GYach2HWc6XCF0jY4Szix98AUzuQsUTzF_f6RuQWnbQzA9b7VJJ9y2oEvOl7h3xeN5nDWf-xOgdjjNoqTrQkNqX8B_tAl5zMguLVH5v2dysmb0l4op9INDrJgn55ifu2MF9YaeRqOCaBnZCT56hm5scmC0wQ2jG-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMVwwwaLfgy6IRWGwKHD58jCW2ysJJ6yYtXeZxyI39lObZtmrIuZKZvn86xGi3vA8nkwUcoYnlLX8y3z_uXgZd1Vs0cDLe58b_MYG3P7fSlen64vWA1X9ztN4M930W535Yi7-JCHPuN750XL1nhMMP4wkpGrilPz-30cozA9jhnNi8FdW5pRoKitcB4rU2B8_XCTRsOBPAFCRg3sduO3xurAcKdVgEbPLli2VMxAWuG-ijwWbwOKvHi4RUda9V1Y1L8lYa5tpn7kJPMfJnT5JSCZoCFYsXsi3OqCXlrfneQ7oLHtYwWjNvi-lDW6DE_OkdEaD4TrLjlr9oVkaA3j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=cVJfHunkThbITH78LVoHz-rT_b7quWKhyavCtsXE_qZhFE687CZfrO_Bmvu7dEYwHQWXDGHCfXn9fLFATv0evdfrrE1Si27TjUTW1TxR9vxK4H_DgYYQRjR1W5H_NNwAE_RZkiDjr11BXWtXLVromsdIY7O51YGGra4e3Hlg-mvWJEqe3ZE2qKgjG7EK_v-TTKSQM8GQS8oXHfNAH_YCifxRmr33QUm0cHAsoS_Qrl-aJFRUqcKuiKDK1vHTnTJ6gdKt1KtrmmdPBK_PUdN7Esg3BFPM87OhzDyGd2QIUozVNYtrhkjFU83W0LhrvS5-OAxDmCgsh4GUNqCQfI5uPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=cVJfHunkThbITH78LVoHz-rT_b7quWKhyavCtsXE_qZhFE687CZfrO_Bmvu7dEYwHQWXDGHCfXn9fLFATv0evdfrrE1Si27TjUTW1TxR9vxK4H_DgYYQRjR1W5H_NNwAE_RZkiDjr11BXWtXLVromsdIY7O51YGGra4e3Hlg-mvWJEqe3ZE2qKgjG7EK_v-TTKSQM8GQS8oXHfNAH_YCifxRmr33QUm0cHAsoS_Qrl-aJFRUqcKuiKDK1vHTnTJ6gdKt1KtrmmdPBK_PUdN7Esg3BFPM87OhzDyGd2QIUozVNYtrhkjFU83W0LhrvS5-OAxDmCgsh4GUNqCQfI5uPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=IXUQHbNSCxY7lxqd4-V-F_kPvS-4YR7y-7EsVKjNVzmIh69Nru5SNNNjNnG-SP_y1x1F_3JE-xB5Be4Aqqpetx72m_fyzmDM5Gnd4sckYWVbMJvraGL8ubysfQu8LYFljAbllKtgP4qRZphgFthGS1mZDhjphxvnkJXo-P-i8QaWJuh4KZGe5n_mi7-b-sZsHedeRp5hCNoqXLuADMK3oJ8mUZhx9zykA_06sBPZb5HnKRUQR5ziI4Y9XST55bELPFdpqR_CgGPNiSeh_ZVb4Kpbiz3wVT695HilBu33yBbLdKOFaXnDkSK7t_CE6y6h1_qanfaY_yOE3MJMafB63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=IXUQHbNSCxY7lxqd4-V-F_kPvS-4YR7y-7EsVKjNVzmIh69Nru5SNNNjNnG-SP_y1x1F_3JE-xB5Be4Aqqpetx72m_fyzmDM5Gnd4sckYWVbMJvraGL8ubysfQu8LYFljAbllKtgP4qRZphgFthGS1mZDhjphxvnkJXo-P-i8QaWJuh4KZGe5n_mi7-b-sZsHedeRp5hCNoqXLuADMK3oJ8mUZhx9zykA_06sBPZb5HnKRUQR5ziI4Y9XST55bELPFdpqR_CgGPNiSeh_ZVb4Kpbiz3wVT695HilBu33yBbLdKOFaXnDkSK7t_CE6y6h1_qanfaY_yOE3MJMafB63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=dfA3_3w2oFliD53VnIVvRwoyPUO6GTCQAEn8g7GmpAtM4KSniOl-Hs9a--g6wdoMW77GCszOZiBSBlT6QKlrXEv9aaeImvqIZzaLrGIyi7Fd7eiFcdrovDikq1kZp4PIpMG_zPgb8pKYoAslawlj8I5Lnk25GQ2BB4k4kygVGh62bcZ0KJCunEd1wxVGekUYQx6ZUB7Hj7yyM7iSrw4QsP4ZrwyYHg8GrmNKZ3NngTTCAFJGQq0YCybfmpBOsIkcsqJNrw2iaU_sCgSeO99RXZPVXqHjIwRjqsdyaXyZBFS8_3ZUazMIObL0W6Br5k4w4hBWw84EfYcfwkZKf44Dwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=dfA3_3w2oFliD53VnIVvRwoyPUO6GTCQAEn8g7GmpAtM4KSniOl-Hs9a--g6wdoMW77GCszOZiBSBlT6QKlrXEv9aaeImvqIZzaLrGIyi7Fd7eiFcdrovDikq1kZp4PIpMG_zPgb8pKYoAslawlj8I5Lnk25GQ2BB4k4kygVGh62bcZ0KJCunEd1wxVGekUYQx6ZUB7Hj7yyM7iSrw4QsP4ZrwyYHg8GrmNKZ3NngTTCAFJGQq0YCybfmpBOsIkcsqJNrw2iaU_sCgSeO99RXZPVXqHjIwRjqsdyaXyZBFS8_3ZUazMIObL0W6Br5k4w4hBWw84EfYcfwkZKf44Dwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9MH0AtzBdScDv-jn_UQm9QGyhNIuXQ2gMYIYd9KgdhRjFQ1e3EOlRdKSU3Sm3grD3nqoXN1aIrrKzcuJZCVQZUCpGQYvT8vXpGkBP4-mdURauSVgDGuYxXEpWVph2JCXZ1apkbirk7B-Qle6EuIw-Hpfr6uyIrGNVwppxo-bODMgT4oCr3P6i4T9fCo5T8aH8_1QGNc1kQcn29hN5rVELcRZMpKGLgwO_GxtRMxz87O1wrA7C5W_jwDVg5sBkGa_aELgElpCsvDvQdU0W5lN43QabhSbk8HIPIt_1Qb7q8603SaoZjATYB7dy4aRXvaD7GeJl0I3clGMVaoT9JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Peu0lwctsQotAiI9QSZSpSns6HdTr1VFuaYDUNeiO1U7QcKX327jmmNdr4Y7ynJKGFoYpJZgiP2GMySFWM5DHEURL_U8P68Z1BS3x8dxkO1Yfyj494E3pjMfgRIlrkKxAC76Rl45BwT-FqlUAgtymEurJ8Gz3Jalbp3rRbuhoQFk0cBaj6oBAptUFOumngcHwHF0goBTpa80tvbuUyStR27LBuptuU5KVemmKteLPezsjxEi-b_AlCbpJ7w_69vzFrfkgY4Bmgn-06oap-U1M1KifITiZvnpDZVo7ZTi7dlg77zhEv1mi1SHI7NUGJtMbVN9y72slWQqMf9ftMUwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=iWQd06fs_xGfFEwv46rd4sXpPQmI78TMSGEvzpCedcn69b77q51TebedHx-BhzzoD_PV2Anu4x01R7_fmBc29YYH80cfWcSkQvk9_3g4AsCbI3jAviv9ViV_lrgpbvvJUnpNzDPGNx0v7DKnPaZJDdTl4V9HEPaCa5rL9JPirffcte8aNzhHyMsdVi8kLhSQORe5JD--W18HxEQ5Bu-lQ7iVkHf-zGeAav6VkLQiVIOQ8a2T_6MTARfYDYRjv1EMzvb0fM5oj3i2mvnLNmk00qRr98IPnNXSlU-ChOVEzM2dmGkNd3frFD7HP0b4OM52FAhuIDe7wTOXEVic7rnYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=iWQd06fs_xGfFEwv46rd4sXpPQmI78TMSGEvzpCedcn69b77q51TebedHx-BhzzoD_PV2Anu4x01R7_fmBc29YYH80cfWcSkQvk9_3g4AsCbI3jAviv9ViV_lrgpbvvJUnpNzDPGNx0v7DKnPaZJDdTl4V9HEPaCa5rL9JPirffcte8aNzhHyMsdVi8kLhSQORe5JD--W18HxEQ5Bu-lQ7iVkHf-zGeAav6VkLQiVIOQ8a2T_6MTARfYDYRjv1EMzvb0fM5oj3i2mvnLNmk00qRr98IPnNXSlU-ChOVEzM2dmGkNd3frFD7HP0b4OM52FAhuIDe7wTOXEVic7rnYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=k2Fxw3p8BSe16t4wFwZLWygrPLB23EI0H4MNC1clxYRrfnrs00LSkFrCyPkLJ-6fgImgoszl8wL090lhSMSBGc9sBbn3cnaBuLD2gEhR_f56-4Wb0OmvjfR2gHboSDMp2MYnzyLWGQAdUNnEvp6a4sKh8zq2WGKwlpvsCI7Jwa0Nqdu78ml6wGNC1OHGbSeBocyePSJLbXD_uBrvnrlOUgVGAkFMLxHlZTNcG690x4f8fPf6ekBpn48ylom3HUPXVMLH2rR3cxzXbqP6QxFZDYADn_W3XArMQpZAGiBhFnf0pc_bvr7nD9YAXIAzuI6dqxk-gp3au4TZWRKr0Ds5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=k2Fxw3p8BSe16t4wFwZLWygrPLB23EI0H4MNC1clxYRrfnrs00LSkFrCyPkLJ-6fgImgoszl8wL090lhSMSBGc9sBbn3cnaBuLD2gEhR_f56-4Wb0OmvjfR2gHboSDMp2MYnzyLWGQAdUNnEvp6a4sKh8zq2WGKwlpvsCI7Jwa0Nqdu78ml6wGNC1OHGbSeBocyePSJLbXD_uBrvnrlOUgVGAkFMLxHlZTNcG690x4f8fPf6ekBpn48ylom3HUPXVMLH2rR3cxzXbqP6QxFZDYADn_W3XArMQpZAGiBhFnf0pc_bvr7nD9YAXIAzuI6dqxk-gp3au4TZWRKr0Ds5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=n-hP-pTSXZS0KmjgfJDAhjFkMEa8aBOyISM-PxVe-72yOW7sJXt7FtevctddQTbKog2Q-RLZu0dkSho5sI9LG0SgMEKpSNAsJtKg1W-2V975SeigLI65zxSQEPwYUbrzg11N5fL2BeXDQ8sfsgo_vjDcfr0S-fR2my1dWHg9FKxbPni96sqCVA3P9VkYz24mElRero58A93FJvqWvT9FR1MzT4ridC2sOOtbbK2Mhvt2j_vyJYeFDgQ_UovCcQ5V3DY0KyJ2HQiaZrRMOKhcD7kUMRRxNorRecaEVspGinwOQIiMk4dPhKOR0np2Y2kuLfTjDYwcfHuMxVrv8xRVoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=KKJAMZnHHWWUU4jvYUNrbFpYlKMNicBTh4G8AD7K9eatQlRZDzqRiEOhSxSi_EDZS-78MrVsztggf8pkxR-iM1vxDZyaZp6ZmFuzMFd6DqfL7Mesz3rYOQqW6dHk0QGoIuSjqcERH2ZGYDbNVST9dnCwcfy6EWggYdNYpjPuhR9bp0xD5kHFj7YORmK3PazsvBR5rDT-GfBLekskKdgbFCdsoAttYMIPhpSmL0oQ0YyLm_xFjGNGXYcGqcTRBbkQDNwRKPnks3lA63nGdglbLJutDVLIbK611_7yCl9Oh7YTI60n9K4Y3D6-mhuCw3xTFR_xxYRFZQo8LaWGBdHFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=CR5jOmyiLlZ518y6qce0cojp2nxnQnNFIUXmsm3AqpLohfQ6buOm_RPg9EQd7xtKwx06oP2CJMAEMuYgzBddeBwKw1OsKk_y1XNnPwEK9EEVTpNm9cbD6yFJDnxjW5y0tW3Wlfe_NG79DoDSl0ubVKnQP9e3CiVxLbLqvdZnwy_Xlb46CiHxoAl-PUA_iK2ImQ7Trr9qy_AYvDFbb5SJxp7tbcTId2v0ZJY0grPz0Sh0k6YZNxyUNc70xt6AHpAZMXElT_RwWwTAmCvz9JMJlHuR14XPbEYRvZQnUQwlSDJUyMjgOoI-YcO0yKSqBkbcbg3YAJP28lTaOre6d2OBaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=V6PS5d8qKrIJif9qAHDs8hbdSUzfMe5gftgGK0LKSa52_AfYcLw5luy35WgPuH3RDIp5b464D3qxE315T_kv0obHPJx2p-lLCiYuljlpu3kn4GXsgVm-RNIVM-Pcm_y4Au7XFcoDnO6zEA7nIEPw58QUfyiNEfb7ZSv2Wk3V6-mhj5AMcHC0kiqaaR7Q2bSMUpQUorCfrtCv9ZnJ0y8Bi1cuRAlUqzmE4by8VUUaY0fwtRBV_vHP1UBaMQa6q5lAHMnW_wcT7sOVNkz7bsva0sw8yJpZshbXUZRJ24Byu2GxQD7gA5_uiFJR8S6VViiAaBj8hqlvcvqZ95taqoVu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=V6PS5d8qKrIJif9qAHDs8hbdSUzfMe5gftgGK0LKSa52_AfYcLw5luy35WgPuH3RDIp5b464D3qxE315T_kv0obHPJx2p-lLCiYuljlpu3kn4GXsgVm-RNIVM-Pcm_y4Au7XFcoDnO6zEA7nIEPw58QUfyiNEfb7ZSv2Wk3V6-mhj5AMcHC0kiqaaR7Q2bSMUpQUorCfrtCv9ZnJ0y8Bi1cuRAlUqzmE4by8VUUaY0fwtRBV_vHP1UBaMQa6q5lAHMnW_wcT7sOVNkz7bsva0sw8yJpZshbXUZRJ24Byu2GxQD7gA5_uiFJR8S6VViiAaBj8hqlvcvqZ95taqoVu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNejnkF-pFGWQZz6vcup8nrO6bov2KgLG23_fCE_ND3yEH6pDfoTJAQwPoTWI891F-hzhlXqZRa6w6BYi7KfAoBLwLG5goTGOVAPP4uu4gd-29Mn0bkDUztcje8IkjTvyz0egsMByEORD0_AgNexTcVdvINJSBNoRzyNLfBFiX6-S_ztV3-YRQSooHawhY5dyE0Z8fym3OXtlY5PnKxquHCHEOBmskgbEHwclJEHC8-5tsUp9cDhfddBi7C7RTZc-Qi_hJI6koVzheaqytjMrmSJSpWUi-KUkKOpVbg7Ml4qPWqBEvwK9vIPo4UqzAMHNu9bV5jaz0aT8IrAzJmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=a800_84XEzSKJbdDvboMpIvxU6_HJ1MWeGGhzuwEW-v4DYDz8xoSrNEkaJDXG_Io2iouqXBE8EPgkxcmFtFJFMew85Lvajs8iVinqV1mFjgJhh_Vo6Jq_j1LS6XGWsKO_27leI8F4GzJv3z3IkZJve0dBz93A1sFsiC63vRkyon74WHrwWRIidzzaBAJBv4OJGiKn52_eCywhI_VzlwuWsQoGoyEjGaaeirzsm5UyHgwaOqi-Xn0bpf3cgmnBUDlikwKP03Wr7kxxCaBz6lC1qTSv0ih8zpzhSc9W6esFYmSFP--p4x0k25pTT6KNTXakuYjUPOGMpZ6Ka1BZhY-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=a800_84XEzSKJbdDvboMpIvxU6_HJ1MWeGGhzuwEW-v4DYDz8xoSrNEkaJDXG_Io2iouqXBE8EPgkxcmFtFJFMew85Lvajs8iVinqV1mFjgJhh_Vo6Jq_j1LS6XGWsKO_27leI8F4GzJv3z3IkZJve0dBz93A1sFsiC63vRkyon74WHrwWRIidzzaBAJBv4OJGiKn52_eCywhI_VzlwuWsQoGoyEjGaaeirzsm5UyHgwaOqi-Xn0bpf3cgmnBUDlikwKP03Wr7kxxCaBz6lC1qTSv0ih8zpzhSc9W6esFYmSFP--p4x0k25pTT6KNTXakuYjUPOGMpZ6Ka1BZhY-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=LfjpL2PNlora-ZzOQDUBrIHFVXfBwwCoB30SJtg_kicp4h9Z5LOcpaBxriPsM9X9DV0HIf1InnY_tq8ZAGjKyUd28lj9g2GF-dQlOuW8_jHXHINJc0qGFcSgj02GujWGOGEFkJP_4fiWeMckaA47w1dBGSkodBuUAZIADvMWvRJkH_5p__Q_0K3twhYsVnVDWM34o2w98Ubeb0BWb1sYnwdPUWDKZ6dcmOWHiqnV4Oa0AbgCEQxp9RIFenjvNxOE6iej-xfgJ0vHLE1-FHjuSmynoGRAaqeCMdlwAl1Ge3iVz1G8gYrIgC2OZdx8tFwkD_wVtJRyOgMjky-3ajr5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=LfjpL2PNlora-ZzOQDUBrIHFVXfBwwCoB30SJtg_kicp4h9Z5LOcpaBxriPsM9X9DV0HIf1InnY_tq8ZAGjKyUd28lj9g2GF-dQlOuW8_jHXHINJc0qGFcSgj02GujWGOGEFkJP_4fiWeMckaA47w1dBGSkodBuUAZIADvMWvRJkH_5p__Q_0K3twhYsVnVDWM34o2w98Ubeb0BWb1sYnwdPUWDKZ6dcmOWHiqnV4Oa0AbgCEQxp9RIFenjvNxOE6iej-xfgJ0vHLE1-FHjuSmynoGRAaqeCMdlwAl1Ge3iVz1G8gYrIgC2OZdx8tFwkD_wVtJRyOgMjky-3ajr5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=Sj9Isy2G1KJuENUlMphUEBFHYatsHMV9qXSE219vT6GycpXJZXrlWlwZvrGhBO-vklW6lQzgWWTpq-ZGkq1oLRP7LF89hSiBaWmw-HKo0IR6iVefNJsa9XsykohtrMZS8sJGTtkuvSEGBcEUMQhg2CajpcqHa1Fknk4fY971zV-VyAUY9W3ZKSqPWUG3GyyPX4vg81fdIRHKuo8w7eSbzyv850byWgzQYkB9xISk7AkQ0KsKBvnBHP9nV6Pzb3wJzwEr2TybCPKYquZmbtJk7MlfN58xfl-dDL-W_FBZ6_sgFdlz-Xw9lCxkOtFs1FpoqbQ5BHePHQU77AIC3b2Opg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=Sj9Isy2G1KJuENUlMphUEBFHYatsHMV9qXSE219vT6GycpXJZXrlWlwZvrGhBO-vklW6lQzgWWTpq-ZGkq1oLRP7LF89hSiBaWmw-HKo0IR6iVefNJsa9XsykohtrMZS8sJGTtkuvSEGBcEUMQhg2CajpcqHa1Fknk4fY971zV-VyAUY9W3ZKSqPWUG3GyyPX4vg81fdIRHKuo8w7eSbzyv850byWgzQYkB9xISk7AkQ0KsKBvnBHP9nV6Pzb3wJzwEr2TybCPKYquZmbtJk7MlfN58xfl-dDL-W_FBZ6_sgFdlz-Xw9lCxkOtFs1FpoqbQ5BHePHQU77AIC3b2Opg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg-JZhoqUiLLb7yhYsn-f6pON3TBjtab7zKEruQpoLvdW77HcDjZVf1QmwVfqAG48gK3qrJFBb6beaqjZoiDuDGZS5jdAsDaDKMdpMAOf-d8JFbGovlvcJxuxF7CBPbt3JtbYFXFTqbUZmFZ4lmS0o7Uy6mN9SmG07-W1h1BW7QHMtRVIzEwaxIqyPcB-cGBLDIy_BFedhJAPMCpxHRjXAacAQm98NlKlp5AdNalU3rdhBncHr-q0i0G-xbudJ5AP4gfug7qJwKR2-0MlfUxQZptdGLMXiRxDJtjL45YLIWjJZ42D21k5yhp1TggkhVPlItGNXRoL8ez9nCBCSX3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=dsI305o5n0vU86l0COvHhWiyQOnfDuaMJmXVtvxBKe1XtNd4qzecRvtCkCQEtl24Vii_xUvpYL1Q71HhhsXjqyz7FNjN-tAuIAuG6TGSIPUk02Pdq4bVCGfbGsGrO5FgW8szAGzlWHpdtnTD3F_pdBQe0-Y4kV9wSTH-r68vpmjT6cm_7mxNJkylQ1TnV_lAYPyfNjaCbaFm7OnWSkskbHg5qHf9Hp1Pdb1XCGXG0kz816Th3jP9XvaW1Fo23a2GzS2wPh2xO07OGUqRnaistUZDYdcUGYwjITy0I2W8CSTrMYc_e3NaBqbaPJX-0WAaWSvqyktn_tt2bijn63Ir1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=dsI305o5n0vU86l0COvHhWiyQOnfDuaMJmXVtvxBKe1XtNd4qzecRvtCkCQEtl24Vii_xUvpYL1Q71HhhsXjqyz7FNjN-tAuIAuG6TGSIPUk02Pdq4bVCGfbGsGrO5FgW8szAGzlWHpdtnTD3F_pdBQe0-Y4kV9wSTH-r68vpmjT6cm_7mxNJkylQ1TnV_lAYPyfNjaCbaFm7OnWSkskbHg5qHf9Hp1Pdb1XCGXG0kz816Th3jP9XvaW1Fo23a2GzS2wPh2xO07OGUqRnaistUZDYdcUGYwjITy0I2W8CSTrMYc_e3NaBqbaPJX-0WAaWSvqyktn_tt2bijn63Ir1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=thKwt8ZEwsmwbUDjGKzdTx9mdZ_fj7gbGnxoHIMXFegIvqK7KZ7Lm64J3tHCDsfThRCtJ1Msex3tbShN_jRq_iiUqhKRuRVNVYgzDA5WjVqjOSGlJywvkTTcrnaMTAc3-Hv3njnoCyA7ms7Y7uQPp7FfLWKiSMTLDdogrRHUhwufERIPt8MjKPHT462dQRrP1Z13lmZG0mmQDKp0Xzayp-N5SxgCe9SCdEiZilNSO4eu9tr5n0KRJYaCb-1C4RUUe7fPVzFW9txQgKAV-JLNBxbA8UpVVUs-yov2VrGuKupU0p1GpkmWc0G6aSuRj6qSxfFWwxkiYL66HeO6FSNqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=thKwt8ZEwsmwbUDjGKzdTx9mdZ_fj7gbGnxoHIMXFegIvqK7KZ7Lm64J3tHCDsfThRCtJ1Msex3tbShN_jRq_iiUqhKRuRVNVYgzDA5WjVqjOSGlJywvkTTcrnaMTAc3-Hv3njnoCyA7ms7Y7uQPp7FfLWKiSMTLDdogrRHUhwufERIPt8MjKPHT462dQRrP1Z13lmZG0mmQDKp0Xzayp-N5SxgCe9SCdEiZilNSO4eu9tr5n0KRJYaCb-1C4RUUe7fPVzFW9txQgKAV-JLNBxbA8UpVVUs-yov2VrGuKupU0p1GpkmWc0G6aSuRj6qSxfFWwxkiYL66HeO6FSNqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGYxPa8laxFVvFJ5blN4MGREfTUKprdIckLN1QzxhS8OhnCY_F8iXJRHu7Bf-bIvmkV3rDJU_Sh1nTHW_H9ieZkyyqYMiEZjUEWb2aXTNlpYSSW-CJkOKBOvIr3LbI1ktsl5glnsXzWuSa4j1lKLDYpEY-_YFTZ3_rClu8cPq6hjp7p9bKVqwfmdecY4hqfmfZXkJu-0xXK7aPxUb9Vs7bZTb_EfLRYAiHwnFhnXRaPgajn2Gv_DJpTSR6QjZ53CPFukBOJXSgx8U-fP5YLsiDP29i9XqS-Tlj4bHY_DWCa9-dq6Qd1g_1mfciEVvcXs4ImOzUNueZOD05291f1kHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=JXUXGVw1Gdjogpfmo0tg5TLOzX_OFCqwrOWC0JdXjiYjxl3ZSk20t_Jom-kfyhLCrbCnvrjwbWXKzfEWmiC9lCwHYaxQLBcuh9iMaU3hNh89rGBxXKbYB4sBB5nb800YY3IKuVU4I0vq7zMlLZ5yyq6Qz4bKUNikGCZGILsI8D7r-_tVrILjhAEZaEVVInxkiD1JdbFT1Lfl6cmXmx4bxdOu2n9ri6IHC0O9Z4Y0AtysBl5yFG5G3_F6WnVX6EAZQ7ZCVr2-xC-WT3hG79JZPgGdtEUmBpeko2YR-N2Bv3kz1i66-jIRbBW9iexocrGBpqzgT5h8KG2SPM7BvpDkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=JXUXGVw1Gdjogpfmo0tg5TLOzX_OFCqwrOWC0JdXjiYjxl3ZSk20t_Jom-kfyhLCrbCnvrjwbWXKzfEWmiC9lCwHYaxQLBcuh9iMaU3hNh89rGBxXKbYB4sBB5nb800YY3IKuVU4I0vq7zMlLZ5yyq6Qz4bKUNikGCZGILsI8D7r-_tVrILjhAEZaEVVInxkiD1JdbFT1Lfl6cmXmx4bxdOu2n9ri6IHC0O9Z4Y0AtysBl5yFG5G3_F6WnVX6EAZQ7ZCVr2-xC-WT3hG79JZPgGdtEUmBpeko2YR-N2Bv3kz1i66-jIRbBW9iexocrGBpqzgT5h8KG2SPM7BvpDkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RmJhwxvI2MNAqIDrrAvQcoyIv94mrVJMV9HnQ477jTj_IFfFjseGikBudmZy9rDPVA5xcErYt-mehkP1o1snhvslgZk74g4UIx6X_MggD2g7y6jRSz2kx904g178ZicMAiRi2XIM7mlu8HC2IE-kp4tV-vSfBtThqSU3lBaPnIG8xfvYrGCtyjoluW2Or98QfAXbETa88LKrdb02LKIT-4pv2Ff8p2ho1-iP1-DpnBzF-Y2P1Mv57R8Wx10x7wTidF4Pgez41earydVduPUXyvRrQpZJ4WPRU5T7t4PVHoWsQX5fh0m9lkQcng1xrGVvNbRChp9zJYEu00t6BCx2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hkUMKFeAqs-qMwUOpBjQqWE8NNZqrqe5s19tep9RehWbLkUm-yDjYHdeqAZlAIeYtFaNk1neK5EDxf_C5HFhZ_vGeqXlNHdQ58k5rCn--y_i4OC7otcEIV61sBCXuB7SZefhZ6PgqtwA1cMbl1El9b1162jfnTjQirX65Y_wASTdYW1afYiDeSybwNZbCQAPrTpZpRaX_iIp-uHKaW7qvU3ecX9dfxEx8LsH4aF5IkeJ6d3h2K3CtnGDE4gZ44jZhYMR7xRxaPEY3lrhG8-BT9UnLazlUHrdd99p_UwKVNndjarocGnEXZZaTwUbPLE-lrk7gJ_9_xns0PZHbJOzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxGWES_C9lFkWZavngWUnOXl0T3qGkfx0ehNTJqyh9QArzSUf812ruarbLsILZyYcY2fEHjc5xXgJVczmFEkCnEFyX4-lfGCr0FHfsSZE46mc1mc8Bu1fKt08T5peceF5BHiTml0FYtuU9VptZFsNecGglLBBcxI39an_wTtk6T4euk_iaTSPjSutHCtwtkPSxBGqmGS1PWWX7Z7MT-UpCvgTL9S4rMuBUrS0XsP8V1tQ2NpH-PjRktSuaY-ZVGYFoDMn7c4f88wINU0lVQAGM3sQi7lQOjUKDcuNtdvZPBv267KNhC-NsqP5Ik1ko4rQ0j5UQYoo0JvJe9QLZkwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cnc77COpT0EfAakzXSDVmluOoCLTlKUCnGF_3r9R7zJxzTT5CfWnYt_ozR7_Hq3EGH9x3M8Fj3pRPym3Nnm2LchIaqBjwbz7vUodoy8JoYWYDQGMP7gJfYWYSiZrr5MXML4vZ2GrrGTdRLGMdiqcaqVOaA30GDrIcgsrVtQsjU_PJ9cHEZXTfNaE9UQH4DGbJyijgcZILvGxYkmCzAeqzrWRwULzA8F2Xh4kj9pTUNwG6rt36nNKrqJ8pNChNHwY6hQZQPsA1yjztOrtliN49MXsX5fIbX4GVUIyqxYBJw_62bOoCkpmD7inuyHiNSUBiAafSJZ6AtPqSKKvSozAug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVM8E9PscxK0q-oJZEoMTOkSNhKq1kjxlw9WtHUX42VTL5LADn6IMIcmRE4ObCQr0tawbLgPF0QlCJrrqQps8apacbeKiSaMOiTqLdCaapAhJ3cA2qfFD4mQwjfo2B8TkBfA62KaxwUEMm1Q7r2flmMncah7TzFbXtgqAPgz2ccahIHTYW1x906KPPvHdvFr6Wq5bbqd-eUvbKWhyhj2DplE_1p0W_mwc0cL7F66Ki66LRrOUo9R4TA7PmfFsX_0B_WrAW9q4eOMH5qkRYIAuloVkLOyjcKhzkgSVEaHd6GsPo8oZjo06Phh7Jtn8PBobS6UuXTfEzpsrZF_xeFajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU6ZyUKITSbfhSvlgHa-wbP9MB-1E25-xnxV5iDXifeAN_n9sUKrbo4X-wDZLsKn02ZcjRjmLzrx2GBb1exa9cIf0CHLHHp2MCYOq2nk_Gpl5hMhPHCned-qrMmoVYB1V8eAHb2hjSM8Vl2AW94KTfiXhPi9ohFxsss3ux_xlTJQuZj0Kf79aZVsjq9MSWi4niaPvnktojpssrz0aV3Pc3j5PBcn_9hNL8PfjLsvtz28M_BdE2ZvPn6Okilna4TcOP9aWc1nco1oZSDz0W-6vNIlHy8I6I_Vq0TIrYUejE01-ebHBUSJblqpO2UwqpzzXrKiZ8rOw-KiU3nAANEhwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPm8ntMCZvV5jko7GaBzgqAeC4y2K5ImmdAOJieJDcfIhayhIZ22FfF_VTb-Dkp7xm316EIM_B3scYBDBADfuMcJngP9RYtPGR8Gpr24i85gb2USH-TDOUB3F0wTyxG_fK79u_XlDVyWrouqnu0fANh3hmwTB3HlSVxd2dDRTX2P_wFPHo-oVgmKzZHGkKXhqrmT16l0JpEeSjHymI4_KOzUqgBeuvFmPkGFTCD5KaDWbqCLvnqBwBokW9-12KFuUQAcTBwLdS4gI6dubM9YFdApVqCAiMPyr_LdZTqYP8gkn4FC0_JjBytPHFKxQiGpbOr78y7cgemkYsRW73YYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=KXXx968UZUAzCYlfHCfNSvpOa2GuysHEXtUbnlrUDgTK2TU9eOqQGzZjWQI516Nbbgt3zfdt-lsbT1O6GsPxzniCAVLBuhjXQ_DkbkKUu7as3iVgZo7xtT-X1iO_MZ4KSbqs_bbuVxBkgnm8532cA7iewICXV7ec3PzxYwd-tbewqtF_A2rGYlD7qwoyUE7cstFGzyIhJRH7eeD4hQl6AjRykFzR6pU3nHdYV9HjMalTNmEbDm_kmUSqEEgKPbf5CCRX3uGirQZYER4HbQUvla5Szb5aQpyn_nAMt5Gus0mupxiYBv4_kyIyHDEnaxF7nSZoIWQn9yZaLX8EU7Dx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=KXXx968UZUAzCYlfHCfNSvpOa2GuysHEXtUbnlrUDgTK2TU9eOqQGzZjWQI516Nbbgt3zfdt-lsbT1O6GsPxzniCAVLBuhjXQ_DkbkKUu7as3iVgZo7xtT-X1iO_MZ4KSbqs_bbuVxBkgnm8532cA7iewICXV7ec3PzxYwd-tbewqtF_A2rGYlD7qwoyUE7cstFGzyIhJRH7eeD4hQl6AjRykFzR6pU3nHdYV9HjMalTNmEbDm_kmUSqEEgKPbf5CCRX3uGirQZYER4HbQUvla5Szb5aQpyn_nAMt5Gus0mupxiYBv4_kyIyHDEnaxF7nSZoIWQn9yZaLX8EU7Dx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=sHSmQuBrubbxtX3W2UJplyrk5yrxLjXeFX0dZkeW4qY-IJtoT7LxoGkKAVhGTk0yeZEz8-HyCIlYRyNm1b520j5wc1TOYzQ9yg9tFPeb6ll4UO58mm4PX2fVDaAgSGSzv8mtPC0dvvWQzrJ9oXNwQrqsE6-FjLNpM51olHLyr3QROwTvShW8wnPkkJ0h0oxPpFPscUdf7lhbfKgjEnTUfLTYrpiFpYZF2FKkXZLs9RVhq-TdWnaBXSNqvtsr4lhEBjsQBHF4g0F982A4A-7SbAdEMJEHYn_Qyop1y3N0mGtZX-coznYxFE_7yWroYYjzVtdPJEKPm_NN4FA5G-VqdYFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=sHSmQuBrubbxtX3W2UJplyrk5yrxLjXeFX0dZkeW4qY-IJtoT7LxoGkKAVhGTk0yeZEz8-HyCIlYRyNm1b520j5wc1TOYzQ9yg9tFPeb6ll4UO58mm4PX2fVDaAgSGSzv8mtPC0dvvWQzrJ9oXNwQrqsE6-FjLNpM51olHLyr3QROwTvShW8wnPkkJ0h0oxPpFPscUdf7lhbfKgjEnTUfLTYrpiFpYZF2FKkXZLs9RVhq-TdWnaBXSNqvtsr4lhEBjsQBHF4g0F982A4A-7SbAdEMJEHYn_Qyop1y3N0mGtZX-coznYxFE_7yWroYYjzVtdPJEKPm_NN4FA5G-VqdYFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=jpiYObBbHHgvrIsIBahwSNyx-PqMwsznEKLzuyAM9ZqsPe3th1BtGTg7B2QZNA-UfukHKHksKZhuBpWwnnS-3dyiDmoqFMNChAHiqEYWUiqatqUEvComKyFif4eggiSqDI3S_aKxKjWxmntc5XDWN3AUH1QWFwT-yzq7c2PiEc-mpDeZSKg025y9HMwbAUo1TK8tUH1Ji7p-xM4f9EEm7ZAQPChri1YNKIj7pZbUIOHPAiafY7cpq_74PQRp4E7C9TcWk6m9gJyimrvsChzsLbyHnSQSKZ_wNL7JpAcxTUOeU0r5iZ7zaot1-Pq5zvaTGjCP8e9ModB5otWMGMu8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=jpiYObBbHHgvrIsIBahwSNyx-PqMwsznEKLzuyAM9ZqsPe3th1BtGTg7B2QZNA-UfukHKHksKZhuBpWwnnS-3dyiDmoqFMNChAHiqEYWUiqatqUEvComKyFif4eggiSqDI3S_aKxKjWxmntc5XDWN3AUH1QWFwT-yzq7c2PiEc-mpDeZSKg025y9HMwbAUo1TK8tUH1Ji7p-xM4f9EEm7ZAQPChri1YNKIj7pZbUIOHPAiafY7cpq_74PQRp4E7C9TcWk6m9gJyimrvsChzsLbyHnSQSKZ_wNL7JpAcxTUOeU0r5iZ7zaot1-Pq5zvaTGjCP8e9ModB5otWMGMu8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOEkKkhfHevwzV4Ez4NheiV0pY99XmiGcOE672QfrFuGnbq_Kf1ejTv0m5X4pWelcsdM138YJTsZyLZgiAjxsfTUS7xKR6PmS9XKe4-xMoNDdplGpCPf_LDgkao6r-p64qJwzl2ahqxQdD2gqq5hBU1QAE5X7rm0isypsblgHQWLqpkYlFtjSLq8FkZBL3kvGgTx7UZVOOG4shngYibZWkiX1koDjtptMsU6gyJFDSpLSXn50lwV5fSujOyn2-g-f2V_kI_tPBu6R6fBt1ysQ6ChlmuFGu47gn705TKoUGBn4jdyzZVewyMKoT5JZSr4ijR6FHJSRcObkKG3CuWb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=M3BzZw25-1mRr31yKRQ6-Pa5c0iHq0FidFyyoRmcQNh9T0stvES2Y65xaJwj4snCIKR3gChxJ7KT4E-bKp39RRJJVRTALCW9SF4hkUnex0F8lDJhFk649aoFbfNYDa60OGf1LlPpp1HGN2_k2zdTu2xS09YY6OINyI-WlMBEScszOGOcVJYQTS5vAW3cxYVsTGPvESjph4Yh0wXosWlCsoIyWM7gr1qgq60ya43XiWWWaYSRJen17HtGeAkUPOoY1Pww2J2De5c1cKyv5QN6lx4WDUALmAMgxdYixZT-9ilGKD8u51qWkEhzHByTiKQbgE3j17mArIEvltSbXsgq6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=fMdcSaeowNrV5UPZMYA-CCMNRKRMO4SOxWQEAaLJrU0czCuSleS7TczKAltzcRZN4fxDc7T7HJ3Amt1StjndySOU3QCrt_fa5bxbVjvW2qZ6YkWwchdtpgoT1Q7LLQsTk_xBrQazR1vz86gCiZGJHCoPwS0mXbOEWTFGFmYylvW_ETW7gvVTGyLsgNWnfSNVJZkwy2VJ0cgzr4r6nc9j2YY_xbuPTLeG85aQwU_bG7NuSgnFRrM31-O_750G2cfZE1O6EGGk4qcCkQ9XYIU-VQWbE5Wg6aaY9hWoWiLze6aQ5lZj2OUcQx4O3q6pudApLoUF8XpYpWrcXNLMi7xsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=fMdcSaeowNrV5UPZMYA-CCMNRKRMO4SOxWQEAaLJrU0czCuSleS7TczKAltzcRZN4fxDc7T7HJ3Amt1StjndySOU3QCrt_fa5bxbVjvW2qZ6YkWwchdtpgoT1Q7LLQsTk_xBrQazR1vz86gCiZGJHCoPwS0mXbOEWTFGFmYylvW_ETW7gvVTGyLsgNWnfSNVJZkwy2VJ0cgzr4r6nc9j2YY_xbuPTLeG85aQwU_bG7NuSgnFRrM31-O_750G2cfZE1O6EGGk4qcCkQ9XYIU-VQWbE5Wg6aaY9hWoWiLze6aQ5lZj2OUcQx4O3q6pudApLoUF8XpYpWrcXNLMi7xsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV4P-oO_ri7MWVPHAq6YNY4UqhhrdueNQUL4M-j_-YE0-AnFAcYd4hehrqRoRwzBVhlOaOMyWldedgfcZcfhht7fj6bGTBzCbaa0uBv6S22YSLHEkum4M6A1j1EE37s-EOXVAN2jb7OWi6bDN-GFsrpiVJ1St6m35NTNN61SFzmyyEQ55g5Plw7VhUWxf9YM5jtyp-ONt-ru6LEydbU0umU0tv1qEd806AHbg37yK2scvUAVXUpn5yt1y6b1yOeS4ggeprQx_M__tfnaehejQy81QKyEgV4viNSp8c8Dur2cQxOpBYrgOpN4UdjHy88kH1cGvNUCWh-mgvVVZS-EFVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV4P-oO_ri7MWVPHAq6YNY4UqhhrdueNQUL4M-j_-YE0-AnFAcYd4hehrqRoRwzBVhlOaOMyWldedgfcZcfhht7fj6bGTBzCbaa0uBv6S22YSLHEkum4M6A1j1EE37s-EOXVAN2jb7OWi6bDN-GFsrpiVJ1St6m35NTNN61SFzmyyEQ55g5Plw7VhUWxf9YM5jtyp-ONt-ru6LEydbU0umU0tv1qEd806AHbg37yK2scvUAVXUpn5yt1y6b1yOeS4ggeprQx_M__tfnaehejQy81QKyEgV4viNSp8c8Dur2cQxOpBYrgOpN4UdjHy88kH1cGvNUCWh-mgvVVZS-EFVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=VvFlvR9eC1KxtmJ-XtXLYCMSyvoQdX26u9QSp8j5ABu6hZ8p91vUhAXZg0ZlHZmaPza5PHdN9-wD_L8TBYflhahfe6s016gfh0M2nZyC3I8KGB9hNp9miltiZ2fjjQl0LzuhTvQEytn7306h9tbQ5Hv3e7s8U-x7rHXllJmJDgHU3CCubXxnz71SZi_NidbMMYsk62FUqueldMU5z7FYgDnxeWCVlabo8mL7_jKdcgg014fLSwe27IAJ7i2sbG4e5W9koA2RMHzucP2eBohIYLIW9c2S-46i5CLlDA1TuJmL91qHcDk2jsYjyzQhDEJktlvqKmghutTCr2c5BtCGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=VvFlvR9eC1KxtmJ-XtXLYCMSyvoQdX26u9QSp8j5ABu6hZ8p91vUhAXZg0ZlHZmaPza5PHdN9-wD_L8TBYflhahfe6s016gfh0M2nZyC3I8KGB9hNp9miltiZ2fjjQl0LzuhTvQEytn7306h9tbQ5Hv3e7s8U-x7rHXllJmJDgHU3CCubXxnz71SZi_NidbMMYsk62FUqueldMU5z7FYgDnxeWCVlabo8mL7_jKdcgg014fLSwe27IAJ7i2sbG4e5W9koA2RMHzucP2eBohIYLIW9c2S-46i5CLlDA1TuJmL91qHcDk2jsYjyzQhDEJktlvqKmghutTCr2c5BtCGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=aTGzMQyZN3HM1Xvh3bLIjhg8fn07UZfqPDr7v4rFYHORAiFWHr-GZDTf1GpPTYm2_FHS7IrmOLZiRLy2zMnImxBULKBpMronq0txr3fU0v5FKzY4RfpSC-jbJz6QlB8qWDsVmFJbVgOo8BDWpGTcxHZ8k6vPqh5Cvz6XQgx1Jz-JzPV_l7RUdLvGkBlQM3-Ao2s5vtcoqvpMuL3SEetD8tS_OeI_HssUoC7ZhfrPUxbwy26omQeEjvENPRI5UxHBB_BCrsODDwkFDHyC78-OLWY_k1ot6ioPDiNpXagb4pNAfExuovOlzrCoUVkR8CjPUVszFF6T0xWwVt9F_N3S8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=aTGzMQyZN3HM1Xvh3bLIjhg8fn07UZfqPDr7v4rFYHORAiFWHr-GZDTf1GpPTYm2_FHS7IrmOLZiRLy2zMnImxBULKBpMronq0txr3fU0v5FKzY4RfpSC-jbJz6QlB8qWDsVmFJbVgOo8BDWpGTcxHZ8k6vPqh5Cvz6XQgx1Jz-JzPV_l7RUdLvGkBlQM3-Ao2s5vtcoqvpMuL3SEetD8tS_OeI_HssUoC7ZhfrPUxbwy26omQeEjvENPRI5UxHBB_BCrsODDwkFDHyC78-OLWY_k1ot6ioPDiNpXagb4pNAfExuovOlzrCoUVkR8CjPUVszFF6T0xWwVt9F_N3S8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=XbRqaY4HYnbaPgNNtMsmaio1vzbyEWK94lvzzoBYD18nh3hs8AM_HNOKv2CkKkL6LoeADC0Min9lY84kixwFKSQ-1G4R6IbRxgaboscKU_p5Gbz51VOSfxarFDMulHuyn7IP6IGHrRH0doneR7aS3IoLEYOHCUtardZWhUz8ZsACo8ALNBp-ADlsuBH9d8FbBNpP6aahOzVT5V4jU9nYMNkYg3mEGnw5NgvSek2JoUn9OqFdOQz6InA6sgsu2yhgQEKGtjz7nMTDHaLroTIGVAVj8EQ0MzYeZ7DEsThtQtWUs2eS5fF4qsTrTZjZLgA1zqBXPoJZ30fENiVXTIEjEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=XbRqaY4HYnbaPgNNtMsmaio1vzbyEWK94lvzzoBYD18nh3hs8AM_HNOKv2CkKkL6LoeADC0Min9lY84kixwFKSQ-1G4R6IbRxgaboscKU_p5Gbz51VOSfxarFDMulHuyn7IP6IGHrRH0doneR7aS3IoLEYOHCUtardZWhUz8ZsACo8ALNBp-ADlsuBH9d8FbBNpP6aahOzVT5V4jU9nYMNkYg3mEGnw5NgvSek2JoUn9OqFdOQz6InA6sgsu2yhgQEKGtjz7nMTDHaLroTIGVAVj8EQ0MzYeZ7DEsThtQtWUs2eS5fF4qsTrTZjZLgA1zqBXPoJZ30fENiVXTIEjEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=Z6kOBVSEemiT97_G663S2D1m-A151Bn6xrF7yqnnoDmdJx6eK2hgq5gF7jCPXNY-EnuFP6fBT4xPyt2I8hBzs2GpXqQYFsSweTNw1HREQcTktuNUjSE7-3dc1PGGM8-LBoilM1pwkMGTFz5u8Uha4E4J69VHGVki9IwDPtLsI3Gp2mJobgEc-XXf4n7ewg_20xYC8xEmkZXQ5ixdgQU8u_VsAfXA8PsCG0oMLvkl7IXurgRfVkd21dL7_gqlriKGE6g4_LFLJzy6WK8kmNUBmM9WLJWDmSzIgCiQsZ80oG_IQTEphZ4LdO3Ctv2olUPdGJM3l65JAAR9HSnwaKdfaVgk2evdPKjwigRUXzaMJNk7_DLchzGLkO6RwLate-UREb5UqVSUKIBIcZh8nwbfKAJ3IDtVf0c6eAcfQAyeKDA6SucmfioDh8UXO9nyUao0ucgsxW9f76-25Iy2OfVL_Isa2ODJ6YEJQ50cxoumy50i0mke49eWzOfUMcyyQ90bXAbLh9e0nd5hA2XMak2KPt24MWDqhX6uDdVHBnMGEsIdb9qsthoJm2xD-nOu4ej5MMqoUkrJ04t_5frjKNRsmrN4krkSk01hpCWKMEM7pcFb0iLrE154ORGkv3HJb4mAl4_P9ppmONSmvhuQqYlnPp5SfeVpXqdckYA4hXMz5b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=Z6kOBVSEemiT97_G663S2D1m-A151Bn6xrF7yqnnoDmdJx6eK2hgq5gF7jCPXNY-EnuFP6fBT4xPyt2I8hBzs2GpXqQYFsSweTNw1HREQcTktuNUjSE7-3dc1PGGM8-LBoilM1pwkMGTFz5u8Uha4E4J69VHGVki9IwDPtLsI3Gp2mJobgEc-XXf4n7ewg_20xYC8xEmkZXQ5ixdgQU8u_VsAfXA8PsCG0oMLvkl7IXurgRfVkd21dL7_gqlriKGE6g4_LFLJzy6WK8kmNUBmM9WLJWDmSzIgCiQsZ80oG_IQTEphZ4LdO3Ctv2olUPdGJM3l65JAAR9HSnwaKdfaVgk2evdPKjwigRUXzaMJNk7_DLchzGLkO6RwLate-UREb5UqVSUKIBIcZh8nwbfKAJ3IDtVf0c6eAcfQAyeKDA6SucmfioDh8UXO9nyUao0ucgsxW9f76-25Iy2OfVL_Isa2ODJ6YEJQ50cxoumy50i0mke49eWzOfUMcyyQ90bXAbLh9e0nd5hA2XMak2KPt24MWDqhX6uDdVHBnMGEsIdb9qsthoJm2xD-nOu4ej5MMqoUkrJ04t_5frjKNRsmrN4krkSk01hpCWKMEM7pcFb0iLrE154ORGkv3HJb4mAl4_P9ppmONSmvhuQqYlnPp5SfeVpXqdckYA4hXMz5b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=l3zXOTVKIP1RiaZW6qZk5VkrXvFmkGR4JAQNRue1TkVfWMMe_HGvT1PLfhTrymn9LFu2vFPInkC5MHF5jmAGFOP3nxmEFGig2k67i4EMTDa_8p0QrhXlHVTcDju0UgisGbFCe6K1AJjXm2u8PCyRHbyfQra7y4U1vfT_gpBc4Qrd5B1zZhXQ0gIT92OzrUlAZYhClWtf-ED60zjAb4TkBBKYrY3D1tvhdCd6knEtKJJ1i0DwvQggmzkSQj9gr9s-hWFt00IQcWfqGSxLjGFZAzCbQVbnDsVs73pnMpwlugPg55PRXjaF5PG0nkMPq_AS7B28eUYE52dtuO__ywCo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=l3zXOTVKIP1RiaZW6qZk5VkrXvFmkGR4JAQNRue1TkVfWMMe_HGvT1PLfhTrymn9LFu2vFPInkC5MHF5jmAGFOP3nxmEFGig2k67i4EMTDa_8p0QrhXlHVTcDju0UgisGbFCe6K1AJjXm2u8PCyRHbyfQra7y4U1vfT_gpBc4Qrd5B1zZhXQ0gIT92OzrUlAZYhClWtf-ED60zjAb4TkBBKYrY3D1tvhdCd6knEtKJJ1i0DwvQggmzkSQj9gr9s-hWFt00IQcWfqGSxLjGFZAzCbQVbnDsVs73pnMpwlugPg55PRXjaF5PG0nkMPq_AS7B28eUYE52dtuO__ywCo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=kPXD6LWxvxIx_KvtDkCdiw8qCf4BRWLbQW8-dHq0As20Lx_yB2oY5_YszRM_x3JfIrwigxLe2pazyUMNezCEvchG_FMo1PnlP9Zetz3qP846pFNDLQ88GymmbWZ-7RgQ2zpCSZmYW7ExM1suL0FWig-1mSc_GE1ZoP0DLABbWZq7q_olRZqjcB9mzA4x3gLjulBl6H0_jNTi9r4oAXH0G0XKbmna0rqvc-EacoHYkSljvW8XMgEHVM4IKEFqe9zzP4PltSmxP5G6-R20IXyW_3okNZkq0UvfcxQQcpwtqJePlxYmGUAGmmNq3wijM7kwyT1JMLKALnVew2LmSI6Y8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=kPXD6LWxvxIx_KvtDkCdiw8qCf4BRWLbQW8-dHq0As20Lx_yB2oY5_YszRM_x3JfIrwigxLe2pazyUMNezCEvchG_FMo1PnlP9Zetz3qP846pFNDLQ88GymmbWZ-7RgQ2zpCSZmYW7ExM1suL0FWig-1mSc_GE1ZoP0DLABbWZq7q_olRZqjcB9mzA4x3gLjulBl6H0_jNTi9r4oAXH0G0XKbmna0rqvc-EacoHYkSljvW8XMgEHVM4IKEFqe9zzP4PltSmxP5G6-R20IXyW_3okNZkq0UvfcxQQcpwtqJePlxYmGUAGmmNq3wijM7kwyT1JMLKALnVew2LmSI6Y8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=Zfe4CvT-7no1CCyFQOX0Q8xS23rjduO2ArCTqJGjzUhuWG3-FZc2z6Wnt6FVqlNh4cHbsK1XQSEVtS_ls5BC_1kS4f_7z1hQLcVVbdr-etGMryA7f-z7wz8np8MB67J4FfduD1qt4nwq6-M476VRf1f1PddJBqGQNKf_s_rCR7yQiGwScabuS0Iv--hH2F6lXp9ZY5vVXvzqICv2b6FvFfY6kRotUJvjw0nuaZl27JeH_zGvUmDoF7bhHclY7aNN685ArUEVlgMQMwheMKxC4sFAM-mGza3USaTeFCam0Pi76dK0YFqMXA_8e6t4wKir1pi5OmQnHdfTQ2ds0lfcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=Zfe4CvT-7no1CCyFQOX0Q8xS23rjduO2ArCTqJGjzUhuWG3-FZc2z6Wnt6FVqlNh4cHbsK1XQSEVtS_ls5BC_1kS4f_7z1hQLcVVbdr-etGMryA7f-z7wz8np8MB67J4FfduD1qt4nwq6-M476VRf1f1PddJBqGQNKf_s_rCR7yQiGwScabuS0Iv--hH2F6lXp9ZY5vVXvzqICv2b6FvFfY6kRotUJvjw0nuaZl27JeH_zGvUmDoF7bhHclY7aNN685ArUEVlgMQMwheMKxC4sFAM-mGza3USaTeFCam0Pi76dK0YFqMXA_8e6t4wKir1pi5OmQnHdfTQ2ds0lfcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=JjT1rJ_sYGAfIVFueDoFvMzMe8WGSMwc-Qr0vGpbMjwM8rGT_TRFb4yrBWbjqClGwvMy2Sab7ad1UVTIJ121pPCNzo_7nQBooej5-vXxk-GyXbmED7MfBynf6kwJXZg8b0xcye6GMMiP8eFwZbazocl35aqr5e4LT4YbYeVBk93MgovIFPhMa2YljfCj5sQOB14aTgtJ5WDZc7yVtVpcaywMcDa41zx9C-zRDObIe_NoH6aJg40RA8ZCG6jsyFfkKJCB5JPCjmgBSt9a3u1Ogr72su6Ol5ST1GmHITKmhYYKU9AhLBW-lQuD1mAXRBC_wqC8D7h4M03u6k0ww6V8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=JjT1rJ_sYGAfIVFueDoFvMzMe8WGSMwc-Qr0vGpbMjwM8rGT_TRFb4yrBWbjqClGwvMy2Sab7ad1UVTIJ121pPCNzo_7nQBooej5-vXxk-GyXbmED7MfBynf6kwJXZg8b0xcye6GMMiP8eFwZbazocl35aqr5e4LT4YbYeVBk93MgovIFPhMa2YljfCj5sQOB14aTgtJ5WDZc7yVtVpcaywMcDa41zx9C-zRDObIe_NoH6aJg40RA8ZCG6jsyFfkKJCB5JPCjmgBSt9a3u1Ogr72su6Ol5ST1GmHITKmhYYKU9AhLBW-lQuD1mAXRBC_wqC8D7h4M03u6k0ww6V8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQJ-zNjNxy1vAfaQv6RbvcDuCBWGr5mEx66iV8mgD-ZZZGC_9WmBWMOOM7qhcBPgvwLQ0GozwkgStIIo5sgug1Ja3j7IzF8o_MySHYI2pldvJEhKAfAqztF0ahe5dCk9qEMWjB2CgpFMYwT-c73SeponH5XWEQySRNcag2cQ3siBfNlGM-b7zrH1feCa6EpiPmx7ftdCXJ_uylznNgwUDBmjX8SeQMp_717wRai7wn5fqiyuyhd1UiBrSaOwd1Y8sAJqac4X5nxnIC9tjjGT9elg-E9dXIf_bA7m9vKi0DgrGzEiBSuNj4k89kBe9pCdvsPMqGVRsZllDofL_ZxEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=oGDX3Cq0dgumnM83FXYwv7wUZEaKs83nP3tD8SCnmsOTu9Y_5w0f9guAsioPbXGE7c3Cg0GhcKERzTYM9H2gSMF0K6LmjRnRNd6AuoG2FxQ-Il-MDj_Rm_btjm3tH6fbrnBbRS3q-9tABdW4u5od9hQl1NQmbuq5ZMpToAQTCnItCQJYvPmXU6kBBHSlCYhrQKbsg2oP_VUEQtM53H32XQnJamj7iCsEvvjwTDU_d8HefbOQ2ZLtWLR-W4MDVKbrotdplLMW_WOSlGnWVao-sHV64kJSEfAlKvHdt86twKSvEWCEKMSjbeYcvZTssRqLg_yiJkRVvqDncKgRdhvpuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=oGDX3Cq0dgumnM83FXYwv7wUZEaKs83nP3tD8SCnmsOTu9Y_5w0f9guAsioPbXGE7c3Cg0GhcKERzTYM9H2gSMF0K6LmjRnRNd6AuoG2FxQ-Il-MDj_Rm_btjm3tH6fbrnBbRS3q-9tABdW4u5od9hQl1NQmbuq5ZMpToAQTCnItCQJYvPmXU6kBBHSlCYhrQKbsg2oP_VUEQtM53H32XQnJamj7iCsEvvjwTDU_d8HefbOQ2ZLtWLR-W4MDVKbrotdplLMW_WOSlGnWVao-sHV64kJSEfAlKvHdt86twKSvEWCEKMSjbeYcvZTssRqLg_yiJkRVvqDncKgRdhvpuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=su7cpR93N-GumzUIm-vDsvX9Q0EAr1zDHqYH3P1faHfmLVvxu0-XNVXyPg5RriYFK7QQDTlPPL-Zx4U3U8r0maF0VRvTs8eRJTIb9F1ih5eF-yV04TsRzOyiaos3N1NRqgP57eafq_bSset4jKu9uz7Tph-lYEXaq2-jTv1hfjyvqVCocuQvsYf6NPkHtGjMS2KLqBWm3U-_D6MDe1NVyjALauzcIsHmWsWtw_iHswldKiDrR3QjRH-f_xwSlo6n9AM5KeB0T4melxkUJ_om5oFP9rLFgo_OP-j3uCPyGtG1vyXflEnAbV2g8SFFOCGjKTu_jIE7p44_1Tw3L_8iMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=su7cpR93N-GumzUIm-vDsvX9Q0EAr1zDHqYH3P1faHfmLVvxu0-XNVXyPg5RriYFK7QQDTlPPL-Zx4U3U8r0maF0VRvTs8eRJTIb9F1ih5eF-yV04TsRzOyiaos3N1NRqgP57eafq_bSset4jKu9uz7Tph-lYEXaq2-jTv1hfjyvqVCocuQvsYf6NPkHtGjMS2KLqBWm3U-_D6MDe1NVyjALauzcIsHmWsWtw_iHswldKiDrR3QjRH-f_xwSlo6n9AM5KeB0T4melxkUJ_om5oFP9rLFgo_OP-j3uCPyGtG1vyXflEnAbV2g8SFFOCGjKTu_jIE7p44_1Tw3L_8iMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=mL_eSYfOx-16Ci7ysGHAYfMRV8F73gJ_gJeLiddGOXelV7lt65nzNOqL9RMXtMFspEdZ3ypGxA0bjGoBilvzWf874_joOZY8uDMyYenxF-0rYhxa48HNkHy9V1OGI45K6D-QFYu7szbAw6_NhoyiddQtt-BORzAyQQ8qsWP3ek4dT5ZXw4Rqj8S6Y_wNhJXWzeeJ6Wj6IeqjCEn0CJWevN_ceI3Onq2FjBNBMkzZHZUHHfwhqYYVxxC6FPKYIKnm9h93akiviF_N6tzCA-l8yR43K_XuPmVvkyJeMbX_QB3SFgIIdHm3A3MX1048tc3bRpkH6kl1JAYrUoOWDm1Okw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=mL_eSYfOx-16Ci7ysGHAYfMRV8F73gJ_gJeLiddGOXelV7lt65nzNOqL9RMXtMFspEdZ3ypGxA0bjGoBilvzWf874_joOZY8uDMyYenxF-0rYhxa48HNkHy9V1OGI45K6D-QFYu7szbAw6_NhoyiddQtt-BORzAyQQ8qsWP3ek4dT5ZXw4Rqj8S6Y_wNhJXWzeeJ6Wj6IeqjCEn0CJWevN_ceI3Onq2FjBNBMkzZHZUHHfwhqYYVxxC6FPKYIKnm9h93akiviF_N6tzCA-l8yR43K_XuPmVvkyJeMbX_QB3SFgIIdHm3A3MX1048tc3bRpkH6kl1JAYrUoOWDm1Okw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=UxeZ1_1ngI2XPgGqFM_GVX0o2JjK4IhSYw2lB6EHSEhi0DRJIj2R7AClQ4ZasJpW_5U6t30TZ7Sz2ExYQhSvGaUO9AQP7ZSL3Aso9KKTUIYS9YJH06oaHgSiaX1ebaBtrndnySebOpA9VfgyzfQpGeuwmzg2dThviTnDVnqwrhoFGm4p6WaNjPJfpVEdtxKXt7n-QU4lwL7PJGOITdcS1LUc-EesqppdzNm7tZ3v3IpYX7dqLbk5qI-lBYKaPB9iqZbLr5ZDwmnGAjyNHAdHkEvnJ7pQtefV0RUMGmuGG2M85dz8w1pPZyvx857TXsxyRWbU3zh3bU4ofp99h4fbsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=UxeZ1_1ngI2XPgGqFM_GVX0o2JjK4IhSYw2lB6EHSEhi0DRJIj2R7AClQ4ZasJpW_5U6t30TZ7Sz2ExYQhSvGaUO9AQP7ZSL3Aso9KKTUIYS9YJH06oaHgSiaX1ebaBtrndnySebOpA9VfgyzfQpGeuwmzg2dThviTnDVnqwrhoFGm4p6WaNjPJfpVEdtxKXt7n-QU4lwL7PJGOITdcS1LUc-EesqppdzNm7tZ3v3IpYX7dqLbk5qI-lBYKaPB9iqZbLr5ZDwmnGAjyNHAdHkEvnJ7pQtefV0RUMGmuGG2M85dz8w1pPZyvx857TXsxyRWbU3zh3bU4ofp99h4fbsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=hqSCaI9dwn7c7Ffb975UAE79Rfyr3nCcs4Y6ljb4dDP7lCIHMyO2Lr8QqxcXg78O58-z4q6bdGttb6RD7i5K9expxB071TIyw13SHOR6VYdRDiDQANLOfxDFLgyORIAMWsLWHJuJSeVr3BVWOA1TzZBZVwzTH4e48GyYo0IK_ogBwbLPcWtxVRDWhhMid1rcS0ysmMF1Ij72yQ8dJ8LwhZWW864sWGy0zoK409eFME22cPKLIbki-xnxDWH-vJcd3fsQs-gEz5mc-u4RhXqwDncTkgmi77570XyfDc5skULf5AIhhSrn8r-ZiS3gzuU1L09cKEOurasQjurAoV1-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=hqSCaI9dwn7c7Ffb975UAE79Rfyr3nCcs4Y6ljb4dDP7lCIHMyO2Lr8QqxcXg78O58-z4q6bdGttb6RD7i5K9expxB071TIyw13SHOR6VYdRDiDQANLOfxDFLgyORIAMWsLWHJuJSeVr3BVWOA1TzZBZVwzTH4e48GyYo0IK_ogBwbLPcWtxVRDWhhMid1rcS0ysmMF1Ij72yQ8dJ8LwhZWW864sWGy0zoK409eFME22cPKLIbki-xnxDWH-vJcd3fsQs-gEz5mc-u4RhXqwDncTkgmi77570XyfDc5skULf5AIhhSrn8r-ZiS3gzuU1L09cKEOurasQjurAoV1-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u4xuZYYnvs7xaQfgWbaqn-VI4PWXz3JYGlKt0f0MvrEe0d7Um1wPrsH9ENaClUlWRGXE2_zVaqYOx6x_vwsN6umTdi2mWtDzwCDHuQXIyLXLYd479gsm57zudoUuNp7kzRtb1QmovLf1rm_Xz4NaCdjdSmHADTf-rjQ2gHLqqHUPkGBUWxH976q52pd_FKon09UtSGN_DCWZevjD2XosQwVUzB0skrc62xiIW-BxPsqAkIOkQfmQos0jLc-EMmaQJsLNpBkdBdMdxI-8UJehv8Wq1BlRkxK4INu3tZe_Gn4DcZUNXqLXfTVdzuD3t9d7kX7u-RxY4DHSNarKX_xMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u4xuZYYnvs7xaQfgWbaqn-VI4PWXz3JYGlKt0f0MvrEe0d7Um1wPrsH9ENaClUlWRGXE2_zVaqYOx6x_vwsN6umTdi2mWtDzwCDHuQXIyLXLYd479gsm57zudoUuNp7kzRtb1QmovLf1rm_Xz4NaCdjdSmHADTf-rjQ2gHLqqHUPkGBUWxH976q52pd_FKon09UtSGN_DCWZevjD2XosQwVUzB0skrc62xiIW-BxPsqAkIOkQfmQos0jLc-EMmaQJsLNpBkdBdMdxI-8UJehv8Wq1BlRkxK4INu3tZe_Gn4DcZUNXqLXfTVdzuD3t9d7kX7u-RxY4DHSNarKX_xMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJmyBgK1XHSH2XRBw5S_Pkd1zLmc3eBIWWWhGwzi3a3HLx16uPlCd4Lgx7e7rEYHvuP9aU-aJgcUh5WRr40oVrKgFXDQduCIMyeK17KmbFanHmmFYM91YfpBbYWJkZ816oTx5_gE8MhVvU5eE_lW8qFgenmdebyUe88eoAxJ8jtSuCyvmDALT_loVPb2x7Cj4g4SI_37FVYs9S2X1Ln7BTzY2qCNYMRDWEK-X_h-ydIAc7DFUy5xXgiITJlTKfWW2EPyH8w2fm-8D68JcXoIR888otNBxdnIIzAcu8FWNi0B3Ld0d6YAGwEJ51ZZqtWGNQSwCyNEUwnWzVhfAp9CD0hT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJmyBgK1XHSH2XRBw5S_Pkd1zLmc3eBIWWWhGwzi3a3HLx16uPlCd4Lgx7e7rEYHvuP9aU-aJgcUh5WRr40oVrKgFXDQduCIMyeK17KmbFanHmmFYM91YfpBbYWJkZ816oTx5_gE8MhVvU5eE_lW8qFgenmdebyUe88eoAxJ8jtSuCyvmDALT_loVPb2x7Cj4g4SI_37FVYs9S2X1Ln7BTzY2qCNYMRDWEK-X_h-ydIAc7DFUy5xXgiITJlTKfWW2EPyH8w2fm-8D68JcXoIR888otNBxdnIIzAcu8FWNi0B3Ld0d6YAGwEJ51ZZqtWGNQSwCyNEUwnWzVhfAp9CD0hT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
