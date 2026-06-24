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
<img src="https://cdn4.telesco.pe/file/tSP6EFCatCb_T-cGtttEHt-aqJYScKiSYgTsXPhkrJKdzSJ55zxbuUvRX4jf1PdTKonG6SjJtcNgBVL7dnppdT-2qAarvLOoniM_-zc4oFzU8NS8KbANE7p9IKfZaof7E6JWEOat19BMEhQE8eowe-PtU4I4nAV7REtEgNfZAm2DqRmVLl3m4w7zF05d3M0R9Kgl-Z2dUZAKSF6AmhuZTo1_nzVpNewgcr_lxVVviovSwhJZDvfBbsJLS5qJm75JfsHFa4gxZXx598g3JDJCW27xNe3kzTK-zGnDxOhi35DMuRWkDATVcR5xUGT9EZ07M3oAy-nXpKoEOtFPEO3PqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-662910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a801a95cd0.mp4?token=kOyqeApGcK5B77EY7ggWcfxjBq9nFZFTiLGyzbNri0xfhQQ9BaFtgbXfRQQxmlso8XGznS5_8euxIjj5CLdHspEX6eb6FElZZXxYINmBTxeRumAJhO8aX6O56qcIxjw-Vhs-S6PR3v5k9H1_EDySC_HCI34OeNCSefBxnqirHZtBF8DHfTiSWGCsE_xEUpvBwd_0-JVlKI1HBk6MfBewJtEMTiSEXzPPZ6YnLb-7BV-rjCWy0oulDZlX5zAT04W7eNcHDLnRO7Bh_B_dCZgteVzY_UmKKOUvi1M8n60MypMe117YU22bp1icCYvjcszZiy64egXw9dLwi36ADv5rTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a801a95cd0.mp4?token=kOyqeApGcK5B77EY7ggWcfxjBq9nFZFTiLGyzbNri0xfhQQ9BaFtgbXfRQQxmlso8XGznS5_8euxIjj5CLdHspEX6eb6FElZZXxYINmBTxeRumAJhO8aX6O56qcIxjw-Vhs-S6PR3v5k9H1_EDySC_HCI34OeNCSefBxnqirHZtBF8DHfTiSWGCsE_xEUpvBwd_0-JVlKI1HBk6MfBewJtEMTiSEXzPPZ6YnLb-7BV-rjCWy0oulDZlX5zAT04W7eNcHDLnRO7Bh_B_dCZgteVzY_UmKKOUvi1M8n60MypMe117YU22bp1icCYvjcszZiy64egXw9dLwi36ADv5rTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مراسم نوحه خوانی امام حسین(ع) در شهرداری نیویورک و نزد ممدانی شهردار نیویورک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/662910" target="_blank">📅 15:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWCZWjdd9ZrisAZdKmxpJM0MVWmv-pRFbfLMEaaN14LoLDkoNW31Hh191hoQfCFksEBgBoqc1v7_YgCxjWCtluBYRuvmMMiNDI0__u27PjUDCI8ZJIQthiWNC6V5J5qFTi5pnP1U-sfrD281wHb7tnXwWT9onHN5w0s9NPQ6iqY9sYpur76-bWmx9nmXZqCHc-shPmXWjdln0jvfx40yUM5caSUfnSXaVqardx91BgIcSXw_yaba-atc1-eiSQcZ18m7Njsx-gcXL3h2vv_kTq3oIq6jGm_6BzsUF-iqvu_rzc7By4KQPyZzqBF6CFsx_roMkkapyJs131nnad2jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رسانه‌های صهیونیستی گزارش دادند که در جلسه مذاکرات اسرائیل و لبنان در واشنگتن، افسران لبنانی از گرفتن عکس با هیأت اسرائیلی خودداری کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/662909" target="_blank">📅 15:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svls6kn_fPx462rchYJtAnAfxCi42Yn4UpKfHv_bWcC4f_p_C_HBZq2eT7188fK9Mwt4kpdGduoN4yesQyL4l2i9MB08FY4gHsA_wRUolTsbDFO_Ilz_rpd-gUCw4OsCYk5HvzzUUlMP3vuVQ6g0u1By3_wksThGJjxchG7dbUgVYEpkNGHfgQKj51MIXWoyLxeXn1wR84iwVw0Sle6YAKgqE1aKoB8IksXWqF_2XmXP9Cs-xu1QvJeNBNNGd9DFJmGHjDDf6FX-7fb7TT7l7MXFm_VZbIuB0qskrY6-nDWRctoK2jHyhsuJBtEnfMyEdzLYJcAY6UNaHYNExM7OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پزشکیان: ایران و پاکستان در آرمان‌ها و امیدهای خود اشتراکات عمیقی دارند. تلاش بی‌دریغ پاکستان برای گسترش صلح در منطقه ریشه در فرهنگ غنی این کشور دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/662908" target="_blank">📅 15:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662907">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814c129e45.mp4?token=J--uxMW46nNowW66TCMbVY7nGQUkGy4tynivODDrC5SGx3PWFGXJBdrRWnaOkaWxOI8Mt7qCa1S0usqrwLc0zhHTt6vyu2gYtY6nSwsLwfXdL-VuwVzAtyobvXAFbp_YnMVine_Kz6KkZvLDFU_D3jlCoUP0kDhAQn12CEG-6xqZB7A7sQptwDeol-YoDSA03rCCpvC7AhG0APdy0XVjvt6hngfntpALuXxwCC3EjR7I3rcmEa-I2LF4ws3xWuU4Hw_LR5_qaJwcxf4Atf32-eqbVDdNOCkd4iKgVJC3TVgf5AaZn73olHiBiaefXkkPs3GIoKau18c1mYvyL9HHRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814c129e45.mp4?token=J--uxMW46nNowW66TCMbVY7nGQUkGy4tynivODDrC5SGx3PWFGXJBdrRWnaOkaWxOI8Mt7qCa1S0usqrwLc0zhHTt6vyu2gYtY6nSwsLwfXdL-VuwVzAtyobvXAFbp_YnMVine_Kz6KkZvLDFU_D3jlCoUP0kDhAQn12CEG-6xqZB7A7sQptwDeol-YoDSA03rCCpvC7AhG0APdy0XVjvt6hngfntpALuXxwCC3EjR7I3rcmEa-I2LF4ws3xWuU4Hw_LR5_qaJwcxf4Atf32-eqbVDdNOCkd4iKgVJC3TVgf5AaZn73olHiBiaefXkkPs3GIoKau18c1mYvyL9HHRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
آتش‌سوزی‌ها در آمریکا از کنترل خارج شدند
🔹
۷۷ آتش‌سوزی جدید در طی ۲۴ ساعت گذشته رخ داده است و در حال حاضر آتش‌سوزی‌ها در ۱۱ ایالت ادامه دارد. حدود ۵۹۰۰  پرسنل برای مقابله با آتش‌سوزی‌ها مستقر شده‌اند، اما ۳۱ مورد هنوز مهار نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/662907" target="_blank">📅 15:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662904">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFplrEhnaCaddp4LyI508mzMHrmHIJ9KVhgly98oUGt-f9JSgOSmjwmIMWKT5aCId-fHh2HaLNMUH3sgahgOpnpQhxLWWn0LJ1IPfzqUC5KVw_BFShzvI7dLN78f9FAEQxyzmWOQeXx36eu_jfI-n2QKdAGIZVUeLGdRz3ntNt8wXFAxysWap-gWfRvyJ9Ek7lDC84SfVxwvRxnnn32pO309T-y-MnGRqsRpf8rtmMXot1EvdJkKybVnmW9W_wb4qPRe3uuMTwZ6w0cE4SaKcKSxq0Fqxa0zgi8eX-GwMZX5icRQ47HXvWmuRXkY72bbMQbEA-ZD6yIIKPximsu7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne65JMYnt0NqJROJWhmoo4tbs-tFyurC9Aj3Wu-qm8qdSqJQg9dyY8KAwhpFUBNhrPPUDwM9TNqIFA-uFq6FprP8kqqDlUtYT1UKG_SLLjCalFX7IHgD6fE_BTWI3gDvHNwdUy1xfNu38AHDs9GmWvIizOFO-8mM83hXfHe6BfNpB0BxF8fQ96Q4xCZoOhp8WhGxZwB78hHNglVQZw7kD11bXZDEWIDMGdv6UoXYdxO8O9MzG4fCH5ehNGxxvzpm9eLYh_G8zD5KHoXMHC_JJl0WXZUyj1DnLjlisYxO-yZkQCoEVpI3KosOD_E7mDrxL-5GqQVHEJV_F9GLEbGtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvOYXGxDYPf38ft2H1-t66hWg__f5QTknp0lWfxqXrupWoIR3wy6uMlX9lPksgFF6B93VEOi8jZSnfhCMEMRJyUGW4NogdVic-OpFxUe4lYNbGIcIpXhgmC-51wKNDXe2KnW84cHxi3zxMd_nckkKMctIoidneBz6IaanVJDAwuFhwJuG0umj4UFGW0ri7YLK7q-kYHrzU1Z9JvcPHm9KUMXQuuG70zkrrK9ocWjQPNkICB2V7q4w3FWMIRWXPpl4fwzp7aQv12vGHwdkWP8LBYHtPmV9XBpivyCnnaHoCyd5y4_qY6uwNY17YefUwnBkPdwWp7bWLqvzE6k6FLACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
عاشورا به روایت شعر و نقش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/662904" target="_blank">📅 15:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662903">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmYKHV6n-VlGP3eaeSKOLSbKnp6JcFGh7JvfI2GIsh8TTrMfugIj0H7lDjgfeO6BeGjIvKCZwT8tBaVtRqsGYyrOK3ksNDfnrbdNhGNh3-DJ9yHYa-Cha5RoGJYz1_IfsLnYUfUAz492MZQ5KQAvAfuD7b4QulIu3Zz-aBMWM7MGV7jb_TT5BdH6_eoqCxzV_P1KIiOg2-C5na_Db5H8gIbSx1wrRtAOjaDzqJfobVGky5rC3hxBh5vdfxB7yu9xh6B_NGc6ND87hvLpEybAi9hKXvAdY40gP0Z9fEu-et_O4xlG8mdT1t0QPwcemj9afVQwAb_QAZlFF_zMW8VVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دیدار قالیباف، رئيس مجلس شورای اسلامی و الهام علی‌اف رئیس جمهور آذربایجان در باکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/662903" target="_blank">📅 15:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKIAn6VjByTuM_BO24UDdggxaBEwAutEzBdPHs3gddBGXP_eYQ6hwkYsu5zhXuWDHUfT_xwOIm71R0KkC4vPnM9EizD7Cgtkj-b3M8nRrp5We_aroVNmzK_Ygwf0x511BoFomtIc2JB_CuUUalX0mMvlSsVYOy8eNFwnbo0IPHbcgHUS4j0WTSLSe3l3OXwIDIeWvv_oyx_dFQOqzUGIsW81JF-uAsBkZUTgrH2x1iWLPd42r4_uHEmHw7IQQJb5iLKzcohzMM_j-qB7tkpkV7SqHj1P-vsM15F01YvcZ0o1DtUAOTHrfKE1lF1tn1LX6ZXABEVOeD_vUVnllwlQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EC8m1Abr4XccD23Exvg1BgrZJDmQXfsUTzDVsS2GhmPLLF_2xbJ9-1ccBM7ysb25dNeYvY10lH7x900YdHLRekliatANFy06H_KbWiLbv4LIvSAM3LOBAelkeO2p8jb-ThP5R7ZuRltDHXooAfkFKp2Vz25VreeXl17hQdAwUGjztaSUdp5OR72vtc4_O-j3IzlQK1_xJ2VCrMP1HkecJNAPB4MapSRwC5P4t0TeoPEHsE8avni6b7qswkk5C1AJ3-wgJ_Opw5kLMHwBGJEenWXto-NDLCFZv709x2PBDxMfmLzivfkqqo8mhDY6Vo-_911Wvi73ZqxhySUB0TVnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پس از پیروزی پرگل ۵ بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی ۲۰۲۶، پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در ۸ دقیقه ۲ میلیون لایک گرفت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/662901" target="_blank">📅 15:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHn2jmBQD0y8yYu9X3rc6V97ifPZiU_MwQHrATnqdwn6vqXbjWr6LvAa8NoMyZVjKKrnpVVd0ebDdpwqF34gbM5UmBmV7ucDctgJLrfKgLIQ77VnzvBOuq4WJ4DaijfiuqggvGPDzU5PJ6PuWBvB4MqhrOygGEIrEtdGGs0glKSUvP9LonFfuXZik5SQZ_XRrZOEZd84p2GS_V1j1BbrlbiaWnrEDwdeO-sDbKjyO1FX8gtR0quNkQi-k-gt_NUGMXHftkJF-KsrZnLpoWh2Fmd3YzO0Xgzj4IoYAZKsovBAYMVnImSmiWo-zlA7a2rlhqQ8qHrm9XYv6YSqjtxmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز هشتم محرم؛ اوج تشنگی و استقامت در کربلا
🔹
هشتم محرم در تاریخ عاشورا، روز تشدید عطش در خیمه‌های امام حسین(ع) و افزایش فشار محاصره دشمن است. در این شرایط دشوار، یاران امام بر عهد و پیمان خود استوار ماندند و با پایداری در برابر سختی‌ها، جلوه‌ای ماندگار…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/662900" target="_blank">📅 15:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOwEjl2Y_qmUP2Aai09_yNGoGl9o-qDAuWpEXM_4Tm1xllbNqJhkGfXNf76LI2iaysYeNwRMWEhf3tjkuL8k1jlEe0YAwtfURWf1U6eTsH-QOsLGmSSCDcG-IkHHmo-oXVDpj1ja4n0A6ECcHKmPghGd1fnBtxLG3RVEnfVO77n5f7oF0Hq3CJBZr13iTmKm1qVYcoKqEhsjMvbVQKTYCZiJtMUzdKhLTMJkahRk7QOcI-brVc7M6hm5PBwoPD3Xfo54WexfFCIIJXaldhY58Si9poE6J1kUi-coFMkr-sDYueVOG3bAqJJIMi-07LEolxzPSi4A1zJEekBNilRTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ادعای ترامپ قمارباز: ایران به آمریکا اطلاع داده است که برای عبور از تنگه هرمز نیازی به پرداخت هزینه نیست
🔹
هیچ پولی به ایران منتقل نشده و از منابع مالی آن‌ها برای خرید محصولات کشاورزی آمریکا جهت ارسال به ایران استفاده خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/662899" target="_blank">📅 15:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/662898" target="_blank">📅 15:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4c6U_PkWLNM6PLESQAryTiuE-G78p998QxGHzXMMUY980CVMoKGdlAfPlnxgCcD1sMqKD--BrKAei9WIU09EjLTlaZIBk5h7qzWHF77Rl0ZfzRRmzygVc2OJGbEvZa3Kpx5hqJVRijQFkbOB63UZ1tt4uADXAzrRfkraLazix-zGo9Zz1zBil0yT-G8ncoboosaG7HN-SU4C8iTewxP_Ny8CKNcZUe9K-icQZHWwK20b5XLBSGXejGRxCcs2XpH_stXfH51BAUoKMoZZ-GU9y3x183NngbxAIijm_QDQrj-il_Vj1IQUfla6IGPgDkV8YhOmjW3zTjk1V4EPZhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر پربازدید وزیر میراث فرهنگی در مصاحبه با خبرنگار روزنامه اسپانیایی روزنامه  Diario AS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/662897" target="_blank">📅 15:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgFoljY4Yd5ZbH7428NDs4R4Ux9wWolbH8c-5lp3zi8MD2uZ7_Sli3oAk6yi-RkbMk3n_fjBCGvLTGL0ZvFxA3YSV3W1OtbTgdvUMsHvqwVEQvj5OhT7OOeT99IruqqLwUB3xTAVQJUtbi9E97X9PNPtaR4tevGsAMToUU-IqPMGBtCPq3OmaHtaVwcuAcPjAk7FI4IfeCjSgoTJK4r_jivhGo58O5dqjQuJoUdYQZVQohe1tNeIPLjmoLjvTzj34FKyvoLXbjOaYZnzwB_JEtVtmmFyqyfuvLeK0yYuIKD0GksZvk38rgWbNTXQKjaeu0eULL-Ob5ehXvZ-iNxuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر تحول مناسک محرم در طول تاریخ
🔸
رسمیت یافتن و گسترش آیین‌های شیعی به دوره صفویه برمی‌گردد، در حالی که تثبیت هنرهایی مثل تعزیه در دوره قاجار رخ داده است.
🔸
در دوره پس از انقلاب ۱۳۵۷، آیین‌های محرم با گسترش چشمگیر در فضاهای شهری و بسترهای رسانه‌ای و دیجیتال همراه شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/662896" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iULYiy0AzCInBbt6dWhymo6s8KFms9iTP0WygbGyuh_5fnqJ23dqptdMsY_5ydoww2ko2WJuTN4WJZoUO1DxylfqNZkF2GeEJ2pq-9PuSy9ftkjwey_oy-4PchwodVUl4o0ZbLhLFjSWX1U_rMozMYeuawJRcVYnIlCkYZXwuel1SdjNXbTHgePtAkJA5wPRqMQb1o6k6fTP0v8Bpz6WEA9zbrAleBhUn3mW9eSDD4RLGLMEbmZX7Ujvjl98eN9ZD7NHMFG9hcoaLh5brwihXYx8LmMvvyaWnxM7Da3kaMXqwxRBaKzvTeq2Vaclvs4ptMRfSdG3q5tAR1hSpd50ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
بلند مرتبه سقا ز صدر زین افتاد
برای آن یلِ بالا بلند، گریه کنید
غم برادرِ اربابمان کمرشکن است
کمک کنید به آقا، بلند گریه کنید .
@Heyate_gharar</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/akhbarefori/662895" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
گزارش‌های تازه از وضعیت تردد کشتی‌ها در تنگه هرمز
🔹
بر اساس داده‌های مانیتورینگ دریایی، دیروز (سه‌شنبه) ۲۵ کشتی از تنگه هرمز عبور کردند؛ همچنین خبرگزاری رویترز اعلام کرد که در ۱۲ ساعت گذشته ۲ کشتی باری از این مسیر عبور کرده‌اند و هم‌اکنون ۳۵ کشتی تجاری دیگر در حال آماده‌سازی برای عبور از تنگه هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/662894" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffB2H6sJFfEJtfAqxhcSqm8dFgvbq1C5oZAWoQDn7QaEN3AND1YLjig8B0nk-F9uNYkobcCNL2LZ0rTRHRHT_jrTouxC5g_pbVWqkQlpudI9j-ip7GlPJ_I_5qLw1seZbVuZElK5fa48EPanIc5tqF_Pf-hxokMPWRPKQxzq2STnB3WrmP8spqMhYmE-fn8n2RS3ZPN_LcpRa1Y4cNdy51e0x0NTOf2wrEqbvwGYt48fm7PsIpw94bCHdBEXQ8hho1FvR6aBCm4M-YHNA3vLnCqIJtN_6FizooPEgfQhPlRHA0rtIlSefWNEA5kQ44iPuDncfEvM8-gciEDtqHYQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رفع اختلال اکثر بانک‌ها؛ استمرار مشکل جزئی در بانک ملی
🔹
داده‌های اتاق مانیتورینگ شبکه بانکی حاکی از بازگشت اکثر بانک‌ها به چرخه خدمات‌دهی و پایداری وضعیت از صبح امروز است؛ با این حال، بررسی نمودارها نشان می‌دهد که اختلال در خدمات بانک ملی هنوز به‌طور کامل برطرف نشده و همچنان با مشکل جزئی مواجه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/662893" target="_blank">📅 14:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
وزیر جنگ رژیم صهیونیستی: از جنوب لبنان عقب‌نشینی نمی‌کنیم
یسرائیل کاتس:
🔹
ارتش اسرائیل حتی در صورت فشار یا درخواست آمریکا، از «منطقه امنیتی» جنوب لبنان عقب‌نشینی نخواهد کرد؛ وی همچنین مدعی شد که اهالی جنوب لبنان اجازه بازگشت به منازلشان را نخواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/662892" target="_blank">📅 14:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔹
صعود هندبال ساحلی ایران به دور دوم قهرمانی جهان با شکست آمریکا
🔹
تیم ملی هندبال ساحلی ایران با شکست آمریکا به مرحله بعدی مسابقات قهرمانی جهان ۲۰۲۶ کرواسی، صعود کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/662891" target="_blank">📅 14:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
همتی: تخصیص ارز برای واردات از شنبه افزایش می‌یابد
رئیس‌کل بانک مرکزی:
🔹
با بهبود دسترسی به منابع ارزی ناشی از رفع محدودیت‌های صادرات نفت، از شنبه آینده تخصیص و تأمین ارز به‌طور محسوسی افزایش خواهد یافت.
🔹
در اولین گام، ۲ میلیارد دلار برای تأمین نیازهای تولید و کالاهای اساسی تخصیص می‌یابد تا با کاهش فشار وارداتی، به کنترل قیمت‌ها و تورم کمک شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/662890" target="_blank">📅 14:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662887">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d794686604.mp4?token=cDEbrYOvzRWty_zHzmNQQHyoygItK8O7SNIbE3qV5Kjn7bhX9nRrl58fJE5Xp0L0G3PkCMeijvIgNnTULtTxKtDy0R8sLr7eoeUHFKDUQxO5mBLRaCSNieCuQ69mb7rXRGzsxhzfSLgmg-OCSYR_Vg8xsA0D4NDhMVMvmUIWEC3_ROfXSXHwYKoz904QzoNxvRXvxYcl_H7SUUklb3-zKhA1vdC1ykXJw_yEogno5I8-ytPaLqzAMXaHrfJC5zKFNtqYZWofvPp5k5FkOT_wkdxBRheEkdWJvI1y90u2LU2nEWxeqv8svEkaZPUHIOxs-bbePfdavcaM_iB2LTmnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d794686604.mp4?token=cDEbrYOvzRWty_zHzmNQQHyoygItK8O7SNIbE3qV5Kjn7bhX9nRrl58fJE5Xp0L0G3PkCMeijvIgNnTULtTxKtDy0R8sLr7eoeUHFKDUQxO5mBLRaCSNieCuQ69mb7rXRGzsxhzfSLgmg-OCSYR_Vg8xsA0D4NDhMVMvmUIWEC3_ROfXSXHwYKoz904QzoNxvRXvxYcl_H7SUUklb3-zKhA1vdC1ykXJw_yEogno5I8-ytPaLqzAMXaHrfJC5zKFNtqYZWofvPp5k5FkOT_wkdxBRheEkdWJvI1y90u2LU2nEWxeqv8svEkaZPUHIOxs-bbePfdavcaM_iB2LTmnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازداشت ۲۵ نفر در پی تنش میان زائران در کربلا
🔹
در پی بروز درگیری لفظی میان گروهی از زائران ایرانی و کاروان اسماعیلیه(شیعیان شش امامی) در کربلا، پلیس عراق با مداخله برای جلوگیری از نزاع فیزیکی، ۲۵ تبعه خارجی را به اتهام ایجاد این درگیری بازداشت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/662887" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662886">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9482fe2fd.mp4?token=mWfOasXF7YvztF4R0xeEyw-cZvMZ2PIpv7WlyMBV-CH1FfH9D8L3qMUW8ST3RbbYDRYzgeazGu4P2sj8Ir4NjX2tN-imErDbMcisllFbmY-8jmKg2CUSRjhhXJdnIELL25WqO6SCVAZuVacj6gRLQ90uC_KDByt9yVtj7DiIbcfREHRpUJ76KxA0Si2AGVvOOIGb0UUurNlWaWJ4dW38lLBVu2CXwWObjGcQW3dbVfbqnpplpv962PxoA8eThSsIuooV5y7-4-6kachUUEAl2qboaM-rNMf_jheZjFM7PJiNU5Of_vF57CATdZUr-VefA3qIOmfTthwC4TidU58tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9482fe2fd.mp4?token=mWfOasXF7YvztF4R0xeEyw-cZvMZ2PIpv7WlyMBV-CH1FfH9D8L3qMUW8ST3RbbYDRYzgeazGu4P2sj8Ir4NjX2tN-imErDbMcisllFbmY-8jmKg2CUSRjhhXJdnIELL25WqO6SCVAZuVacj6gRLQ90uC_KDByt9yVtj7DiIbcfREHRpUJ76KxA0Si2AGVvOOIGb0UUurNlWaWJ4dW38lLBVu2CXwWObjGcQW3dbVfbqnpplpv962PxoA8eThSsIuooV5y7-4-6kachUUEAl2qboaM-rNMf_jheZjFM7PJiNU5Of_vF57CATdZUr-VefA3qIOmfTthwC4TidU58tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اهدای دکترای افتخاری جراحی قلب به پزشکیان توسط پاکستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662886" target="_blank">📅 14:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662885">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
گلباران ازبکستان توسط رونالدو و پرتغال؛ تاریخ‌سازی کریس در شب درخشان
⬛️
🇵🇹
5️⃣
🏆
0️⃣
🇺🇿
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/662885" target="_blank">📅 14:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662884">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfP0_clcFsdGeQiHDfrDDzxf2-MEFAdfOvJcQSwgD_-x2ZtvFberBxJ_tj_85bVF1qcHQV5PlsFV6DVG7GwxpRZlaaOEOYSNo8RZpidVY6-dhvkRoOMvzI-o1UxEFVsFOgZjRtM_rqf_oI7N7B09qiZV_Z_v2IDrgsmCTP-jepHvDLYuWXM7Ez7JA1mrE9gqsR8IIHd0hAnKbXvpDdaWTHW5qwZBpJvcMAEW5_uaz5FZG5WcZaE4JVix4QX4j2YU-RSUPljRk0YV0XZCJZQ_0AvcKWnMx2EjS7Ol-646_7mXrKtFmjb_Ql65vM2U9r0qP-mHH6LreaZWLt83J8Idew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حضور شجاع خلیل‌زاده در تیم منتخب دور دوم مرحله گروهی جام‌جهانی ۲۰۲۶ از نگاه سوفا‌اسکور
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662884" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662883">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6fab5a33.mp4?token=PLByW1VF-KwF-0h7j7LhGWQVycXWKCqTbrWPLDlG3dUKim9KX-lBInpCG0fwgonsJbMqEc_xCEBQ0_0hcULpuaWqcP0N1hJuil_dvWC4uDwZTD4o0rHGbYBdin-NqD4CC_t04enDubqEXVpeFf0Tnn0P-Nr8rqquwTIRic1hGDjIsCwX_U80IRlbFDRlfOkBcHsAvOfUL6eTUSz0SKAnhY0BM9d2rkqKL62wWwW9SmMYivqrAsmIGbJuZXftjFz7_yXgYXsHfJn4vOOwl5JWW64rPoOOAgNzlbbvCy8hKJMKlscOhGDNoj3ibzJQZAptgtibniO4upk46Tgil-KZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6fab5a33.mp4?token=PLByW1VF-KwF-0h7j7LhGWQVycXWKCqTbrWPLDlG3dUKim9KX-lBInpCG0fwgonsJbMqEc_xCEBQ0_0hcULpuaWqcP0N1hJuil_dvWC4uDwZTD4o0rHGbYBdin-NqD4CC_t04enDubqEXVpeFf0Tnn0P-Nr8rqquwTIRic1hGDjIsCwX_U80IRlbFDRlfOkBcHsAvOfUL6eTUSz0SKAnhY0BM9d2rkqKL62wWwW9SmMYivqrAsmIGbJuZXftjFz7_yXgYXsHfJn4vOOwl5JWW64rPoOOAgNzlbbvCy8hKJMKlscOhGDNoj3ibzJQZAptgtibniO4upk46Tgil-KZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
السَّلامُ عَلَیْکَ یا اَبَاالْفَضْلِ الْعَبّاسَ بْنَ اَمیرِالْمُؤْمِنینَ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/662883" target="_blank">📅 14:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662882">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
غنا سد راه سه‌شیرها شد؛ تساوی بدون گل در بازی حساس
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/662882" target="_blank">📅 13:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662881">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APRLPracuA236RzkmszpSpB0qNUH979kKtwEBq35GYKpD2fALb465IEF1LpSI9-sazkV_T1L5Z6E1hq-QfDIwYrvsMS3lhxJbBARehMsfrvWIUU7fRhdZB6yeFxvdstI496MNJ4fGH3IV7_eWH81Jxl2lgpgYG_iNv5XJzhKGlNC89lFxLzHjJUGUHHRoNKjxlf8Wam-JolE92ZDOQj-1N_-H8eAyPJOgiI06boVFc7lHPvkYfLXijuZgsUXFNgo5lF7mtsil-k514zPsyuY_YZ-PqlsRdrzLScqQh2HQP2cNt3mtp_BQhN9eluS_mQcGojPcnxfGQlzVO4JmBzLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
قطر به دنبال مذاکرات منطقه‌ای درباره تنگه هرمز
رویترز به نقل از منابع منطقه‌ای:
🔹
نخست‌وزیر قطر در مسقط در حال رایزنی برای برگزاری گفت‌وگوهایی میان ایران، کشورهای عضو شورای همکاری خلیج فارس و عراق درباره وضعیت تنگه هرمز است؛ همچنین تأکید شده که این مذاکرات منطقه‌ای از مذاکرات ایران و آمریکا کاملاً مجزا است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/662881" target="_blank">📅 13:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662880">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLu09d3yV0Zr3Rv7Q9CykuUX6gT9c0Bb6RtTGcDccUtn4tPq-0U7c1QpP800XTCrD6BKDm8tTwSiFxVNVV4x1v1rR_H7zrzGmeGTRAHrpPiaYPOpAttKUC6tNAtSg2SEQSWcJcZEuU0vL86wc3vXQNAQxy4t1_dCkC0j4uA4wKvt9IIDjr7EaKuY3fVF9PFmrG6Wb19Sq583IHazgY2M_F-QJbycVdrDO2Ev1V1ETYGG7KyKcwlNE2OzCLGbRDi_G-2CTycdJH2PGzQOIWr8IEIOv3bsMGEWrl-6380_OAZ_yFEyeWvgWlJB5y3p5QjmR81-x-q1dlEOkSsaSUfyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غریب آبادی: برنامه‌ای برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد‏
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/662880" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662879">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca3d8385.mp4?token=tIRuLZQXQENK1i-EhXGk1DqGb_sOT5FABJ4TB5FQKNDVdGWMKGcGXRIEunH3Vt6LYcOKsyKBpTIlbOZbv_iGjNoR9Dhp5FGIanAmdKuSpO103UNbrcgXPJnAUedcOTnRPj3cS1zrdbagswuGRqY_JsiveBS-EV75HkSQHPWFeHCGG_Ry7QykePYG0SNdgF9y-ILyiRUj43OORRChiBTk8hePgGGm3sPcnLce9w_uCU02-8a050NLEjPdqocP6z6y5dhBU7bTlFond8SsxZDW3D_xzHmeCXSycuUDndI50BLAbjcxLx1DUIqPT9uK6dqG288vHOWjT3AVQ-oC-bvt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca3d8385.mp4?token=tIRuLZQXQENK1i-EhXGk1DqGb_sOT5FABJ4TB5FQKNDVdGWMKGcGXRIEunH3Vt6LYcOKsyKBpTIlbOZbv_iGjNoR9Dhp5FGIanAmdKuSpO103UNbrcgXPJnAUedcOTnRPj3cS1zrdbagswuGRqY_JsiveBS-EV75HkSQHPWFeHCGG_Ry7QykePYG0SNdgF9y-ILyiRUj43OORRChiBTk8hePgGGm3sPcnLce9w_uCU02-8a050NLEjPdqocP6z6y5dhBU7bTlFond8SsxZDW3D_xzHmeCXSycuUDndI50BLAbjcxLx1DUIqPT9uK6dqG288vHOWjT3AVQ-oC-bvt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کیم: ناوهای ۱۰ هزار تنی با سلاح هسته‌ای به آب می‌اندازیم
🔹
رئیس کره شمالی، از برنامه خود برای تجهیز نیروی دریایی این کشور به سلاح‌های هسته‌ای و ساخت ناوهای جنگی ۱۰ هزار تنی، رونمایی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/662879" target="_blank">📅 13:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
پایان شهادت نتانیاهو در پرونده فساد مالی
🔹
بنیامین نتانیاهو پس از ۹۸ جلسه استماع در ۱۸ ماه گذشته، دفاعیات خود را در پرونده اتهامات فساد و رشوه به پایان رساند و با اشاره به شرایط سال‌های اخیر، مدعی شد که «۱۰ سال جهنمی» را تحمل کرده است.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/662878" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662877">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3616b819.mp4?token=YiNKSpT5KKU_E4RsA-h_0ndsM2g1MOXFLBPU3hq0u4-LEDrxarjBTCAvet9erwJmkyc4YnacFYOGPhvTFH2xywD7bdqhyV5HMCfGvtkQvIZyXnQf9-RPOmlQrrFAUZibgQyZvM7sAn1lP33EtOL34oQe0s_ONwCxMQf9hFU_3qxKwxjcqb_6wr9b6eWT15IqF3ChhALmGutFjC-2Rw4s1UULSzChO3eR7FDgdNpNWxVFkaCnDFS_O9_X6p4eTTskFqOjkwgKdEEnYJnNPVMbL-GT-mhj-qbsrRddshdgPdj4qJikhFjIUTHGq_ELBmk-673fYIOY-cc_PAtwZVkBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3616b819.mp4?token=YiNKSpT5KKU_E4RsA-h_0ndsM2g1MOXFLBPU3hq0u4-LEDrxarjBTCAvet9erwJmkyc4YnacFYOGPhvTFH2xywD7bdqhyV5HMCfGvtkQvIZyXnQf9-RPOmlQrrFAUZibgQyZvM7sAn1lP33EtOL34oQe0s_ONwCxMQf9hFU_3qxKwxjcqb_6wr9b6eWT15IqF3ChhALmGutFjC-2Rw4s1UULSzChO3eR7FDgdNpNWxVFkaCnDFS_O9_X6p4eTTskFqOjkwgKdEEnYJnNPVMbL-GT-mhj-qbsrRddshdgPdj4qJikhFjIUTHGq_ELBmk-673fYIOY-cc_PAtwZVkBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اظهارات تأمل‌برانگیز علی فروتن درباره کوچک‌تر شدن آرزوها و سنگین‌تر شدن بار زندگی، بازتاب گسترده‌ای در فضای مجازی داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/662877" target="_blank">📅 13:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662876">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
ادعای وزیر امور خارجه پاکستان: مذاکرات جاری میان واشنگتن و تهران بر سه موضوع اصلی شامل برنامه هسته‌ای، تعیین تکلیف دارایی‌های ایران و تحولات لبنان متمرکز است و تردد از تنگه هرمز بدون دریافت عوارض یا نیاز به مجوز انجام خواهد شد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/662876" target="_blank">📅 13:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662875">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
انیمیشن شکار در تنگه
هیچ‌گاه از شما غافل نیستیم...
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/662875" target="_blank">📅 13:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662874">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=vP_atT5M3Qqb3I_nceWDs_ilAP225KoJz8-h3Rt4INnV2tLj-xty7LGXUZdcnYcTCEN9-432JhC9vbE-WpfQvu3VNMmSBFntvdb3z0lz2LhN4xaU_jWHiB63ytKD8gnVNnCoyUg01IyHZcTDT9j3KzxqEUrm36Sqx6RfHJ6gjLwLvz64raffiRkji9TjaMNf7eBabUamhJldsZTG9GGYEixt8L51ZVoyKJX9tnfJyFZPU4Rc-tBzhkZ-oVglnxGVCwdXr6fP_bC8MgcBQjwvCk3AlENm9ktwJ9Vd5BNEibnR9mXujCds858d-z2Ao9lNWEoGVa_WIvpbzr7fktuLTxTFBjNAjM5WLnFApqGVR50AJvlM70_5vENLdOoLmdizi_Zql1-p1w0v8wUBd85GlcOzWdhi7kUSNQfb_4R1cIe7WsbGtPMWtaPhhSseGtFiroNTPXCgqG4m3JdX16pbn3YCssWbKNuzkD66CU5lObWvv7HiRh3BOPdwIM3PMPcHzG-7EBBo8Qk5K41hCR-YwaIHP8RW11OnwMP_czQHJjwX1jVE5HIFhsQek7nIIM0SScAyHiIU_U6RSoV8M-wSId_0TDvzmzJMyCcz8wJ_3Ov8t1vFWP4oyKBgavi01eGt_V_VnPfJdagl1FORP0GAZ1UAOPZxotyZ7a6EwAQVb3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=vP_atT5M3Qqb3I_nceWDs_ilAP225KoJz8-h3Rt4INnV2tLj-xty7LGXUZdcnYcTCEN9-432JhC9vbE-WpfQvu3VNMmSBFntvdb3z0lz2LhN4xaU_jWHiB63ytKD8gnVNnCoyUg01IyHZcTDT9j3KzxqEUrm36Sqx6RfHJ6gjLwLvz64raffiRkji9TjaMNf7eBabUamhJldsZTG9GGYEixt8L51ZVoyKJX9tnfJyFZPU4Rc-tBzhkZ-oVglnxGVCwdXr6fP_bC8MgcBQjwvCk3AlENm9ktwJ9Vd5BNEibnR9mXujCds858d-z2Ao9lNWEoGVa_WIvpbzr7fktuLTxTFBjNAjM5WLnFApqGVR50AJvlM70_5vENLdOoLmdizi_Zql1-p1w0v8wUBd85GlcOzWdhi7kUSNQfb_4R1cIe7WsbGtPMWtaPhhSseGtFiroNTPXCgqG4m3JdX16pbn3YCssWbKNuzkD66CU5lObWvv7HiRh3BOPdwIM3PMPcHzG-7EBBo8Qk5K41hCR-YwaIHP8RW11OnwMP_czQHJjwX1jVE5HIFhsQek7nIIM0SScAyHiIU_U6RSoV8M-wSId_0TDvzmzJMyCcz8wJ_3Ov8t1vFWP4oyKBgavi01eGt_V_VnPfJdagl1FORP0GAZ1UAOPZxotyZ7a6EwAQVb3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود؛ در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/662874" target="_blank">📅 13:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662873">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEYBB91Q_mU5bCEaUdZyBSorV660XB2qw7BIcHWOG0ISaAWo3Kcs3Aycmp36uV5qpHbeQzt7R5sXdPqnHQYfHHe_He_BR3jChmiYhrYlyqDYQPDB6j3E6QAeXxAfOf8ksGE1Lrpw0Pe_MiMNJFhj09E9LkYlAa-Nu--a4uscbKXbO5OjaliT_fnoFE_ZTVwCfuKzanr8aARyq8oTEDmeCu55_sd9zEM2OXPsDlMea-l7GuLvvj-1ny6ysUE33hRtoYOGSg5HrZmu-_KRLxUdZTRNb7gBi9lank2PDrAMZlgRGMjy6lVbXWM5LHTKauRMVdi57PuG_KMTmouWwuvgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عاشورا به روایت شعر و نقش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/662873" target="_blank">📅 13:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb_wPAYeog2YMuSfuxE8Bj8HoQ9KCQ95VPYZ-nhhWiXKOzDAegDt3Smc4ah0-f5THZpoTsgN-un4V7ODL1rI6ZE7jH2ZO_l_0aNyixbIsi_OUleulTf6z9sMC2Beh315_6SLHL5LfBmdjy_Tas-pJUam5sw7Gm4pl91FVzX4or_1gqM2TfFm1dSNDJIt12qbSAcgWLq9AtbBn1GEzlpxhVX_OK6sOJ3hZFB0IcDKgLRr6mSgsrG0HYgrOT2hpSKHQ74IcaEW_cAGB9i3FbJGk2Rf_tf-c6Aqe-Lha1myw2DDa6QamTvlLU8U1u8RQECa2v0JcQTN2qvtcwU50bX0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxMGGyXx8Umi3zywforysokfKwZtp7NP8Wj8o3trvulh7ioFLiCAPyu2ReMQfJpp1aRNrKk8T2i7zM_Jwe1ZQTtKpKALMkdRK8xwecjUKtisWyjVHi7mojzkC91SgSRodSn5Fbvrs2bDpoz-ABhlZeTF0MIBCy-KBN8lZ_Vlh9oB4oqF1RfZ-qCiolTBDPODLt3RDsqXi-p4Hmv8MunMMLJ2tq24su6azoPuxuU-pXQ1WG9WegiZcn1SUaZquPA6D7Hz-E1jV9MBUNC-0tmaVHCzPERb7CkBMD3ZYyQdwEbNizV9jwz23I5PFeKoiyrGh9E-GdFBEVArof4Cfm-Y-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHxbmTTjNDaEGPFe2nTE2ZOxqAGLwOrwz1moFbe9NCCan9ZXW9l234uO3deFqR056J07FOgVSRdOSkWM6X_1rg8ZTHBdYrTpSLJE_i3mR8kSyepZrhopBEW9RcEHKfOvgri7pmi-QWcV3WkwbwY5F8xQc1B2C0QTV2l-z5UOmm5iwPuCWQeIzEb3oPcqDkMhpa9v4C2C4z7RpbXNumY2567f-7YDpkOLF1es5ipf3PgPxl16es0biK2_9ZoJhfrZWtsEvXlUyyvGrF01AKXjim1XSFswa7RMryS8zXuDPIRfOHHtbNVdTkjw4jALN3LL2tyZPrGhE-L97W5GIvLBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhBiJhnSxAc-vsp2JRwXyyZX2HtBHGMP0icxZtsTGMZVTqFMe26cezj4jNPHas1sXCzzjiJyzg7KMb6RYlcXBengVp_5zY164KqUaNLV9AjhDV1XLQ0eZpXc_bl99CuTxism0qOtbKixhG2kOGh4ISAgo1CjLR2uw0CGmidRwK86As4eqOsIbJRQHx0tDgf6MlIzQcB7xvGTYFWuU4wZxCahV403xK4NjbgsVyOpH_zT5SSe6o0Z5QSBnftOBDvKksarVLdgkPZc1VbtxReb2MJ88ygIHcEFqk3AFHWQqfx28ZW9tmecdi1xN53ufjgVPIRXnp3v_jrDOhZMSQ1taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oytQj4AWp6xS9p3FVS7BC9qTSxTjRIkzJjryupLyzefmsLB0PQgE2EGKYFLrr25IDdtu5BeoNILxMPlD_3OHfzECg91QhcAsn2uHCb7kp97mu9sveVpxW-a-KOzfXw0O_JO--TjNYTpsTdtU6Rf-wOfswvEykEoaXZ-cGzslzUmtVHXXtvOuB88a_CKuwhDaqWafkaj9EFv0KC3llscIDlAKKQLfS0eE3I4R78HbBgkKMi0CZvFQ9PoEINkDsutZ8k_FZdOXgC6hrxQRV9x2Ctlw54LNJELFO--gIozkw_fxumI---unQcj2N8SX7wElHvF9OfGO5Ez-JZ-8wNpdgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖤
#تاسوعا
یعنی دلدادگی علمدار،
یعنی وفاداری تا پای جان،
حتی بدون امان‌نامه.
#محرم
#اباالفضل
علیه‌السلام
#پروفایل
#تصویر_زمینه
گرافیک های خاص مذهبی را در این کانال دنبال کنید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/662868" target="_blank">📅 12:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7nZEG9EqEQsZ5i0OcAi7JQgBwSGvwEoruxDz3cVG_zA7fq-3XlxhIFHbd9oiHspnk3o0maVWQp56qE0QtI_WCd2qCU0bB7TXG_sF7NCImR22v318nsMoEGm0pY1hb386L7vDQgmKo_mAcxhNFj__SzQRJ701kCrXE_LzX2mG5p-8_Ft4Pv-ucDEpwYXvYFWV6Sdcc3voK7IAbBdr5fZIHocQlO-DZzUnrT2_tzsni13oIH6L9EkWBEctbUQCcVE66EbdsumktUVeq4vtafXGy9JIBLVMRLw4ORQ487Ju7xTUiI3n8ULr7EDipwAv8fsiSJVoP7xc8xCpuXJa9E6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راز آبی که سر به زیر، گردِ عباس(ع) می‌چرخد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662865" target="_blank">📅 12:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSMJ6GjzWHkXs0AgYveVnFF-3AT-Zd38YoKUeHhFKldc-woa8Dgi0lhtwIudFZWDgCMn328_F42knZzyWIUdE6RpDM3Hb4tzlvx0P0X5KTuI6CenWevzXzP98Z-B05oRgwVkoAgM43fWKoC9P4vMF14fMeweGOrgAoXEzMcYoCyHmEEoU9Ig-_vnFuv42-h-tDEW9W0ufdmIQM52WCLnvVYlPiuqkMKpcMaWHyKyaND4FangCN5yncmx5PnPmWasf6nMToD4lx3tS72lI6PMR5JaORdsqZY_RRTukurak6L1GmDoP7N_MfsydVfoq7J45A84Glw_9lHS6fibZRn-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه حسینی
🔹
مخاطبین عزیز خبرفوری؛ هر قدمی به نیت سیدالشهدا (ع) ارزشمند است. با ارسال یک پیام صوتی حداکثر ۲۰ ثانیه ای به ما بگویید که امسال به عشق امام حسین (ع) چه کاری انجام می‌دهید.
🔸
لطفا در ابتدای ویس نام و نام شهرتون رو بگویید.
🔸
پیام های صوتی خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662864" target="_blank">📅 12:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiXReMSjJ-dXCYPHLHeEpCWAO663MEf9Uc2x9Y2RE60sh-onYm67kgPi7C0wKPrQvvU_6yK81wALiysSiYRI2eQo5QoOdHGtXz4CQQvXwwM_i8zHZbKUGHfelMDZ7TZ4G-P8o-k6pmQL0uW5uOQhogZnA8bQg7gPS35nxtUp6bGspOLjDJzM9yfHmmxIk9qQI1vlQ-SbGvnjFX73mXsN9I4EdR_TqybJNqlCTJG8aRW_eFaZK5EQuBmLcII_jgzr9JEvBu9-WdNpOaOx7202-hUL9NclWgxqIUCx3kk8stthqyatA0GPtzXuVb8KzbtW_BlHTeTuwzQR7c4v37nyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احتمال صعود‌ تیم‌ها در گروه G جام‌جهانی۲۰۲۶
🔹
شانس صعود ایران ۶۰ درصد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/662863" target="_blank">📅 12:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYwp-dnpJpap_gn8FLOs1CyPvasUKuGQ7bKjdUmbNt-5XIkGP78DLVwN_PfbCNdDSj9WPrU1l-ReutwLF5b-bAqlfIhkjLwQYyCJn3EavY5eLNnhlrf02swohw2Amn32YJ0gD1XcPbRzqx6Kq6cVbQSszZsaRISRVqxlCTBdao78z6mh1Lx3NWwXYG32g6FHVretlVWxZMPq2M5fh3aEbfcygt6OlIa7yVwshfsHpAqapDGP61-WDpmz-PVb-VkleU_jWAxzZ_iOl4oY1sdqJZrOoVk4PJUKMu0LY4KDq3mJqL2xD2FY-j6CHO-5Qs0fGtbzCQJfxXXcA1jNMhEcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نامه حمایتی و احساسی یک هوادار مکزیکی به تیم ملی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/662862" target="_blank">📅 12:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔹
اعمال محدودیت‌های گسترده پروازی در تهران و مشهد همزمان با مراسم تشییع
شرکت فرودگاه‌های کشور:
🔹
همزمان با مراسم تشییع پیکر رهبر شهید، پروازهای فرودگاه مهرآباد در روزهای ۱۲ و ۱۵ تیرماه متوقف و در سایر روزها تا ۱۷ تیرماه با محدودیت همراه خواهد بود؛ همچنین فرودگاه مشهد در ۱۸ تیرماه تعطیل و در ۱۷ تیرماه با محدودیت فعالیت می‌کند.
🔹
از مسافران خواسته شده پیش از حرکت، وضعیت پرواز خود را استعلام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/662861" target="_blank">📅 12:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
ماجرای شهادت حضرت عباس(علیه‌السلام) به روایت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/662860" target="_blank">📅 12:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080e5ecb9a.mp4?token=RT3OFHNCJe0OD45jG9FWiFVlCHE0tV0RR7t6ktFMHgLWPKoI5-gE5yO4ZihNX9nW8sEmRvm6laVk5Ph8cD-I2yzEvmWULXJdeUEVB8sVhYFkjE0WAnsvv6ygWPeH8bshS2RDyAR_UXFCkRWYDULgwNSok7x8Nxtqj5BZ4GHb_Howgt2_5Vs1ye2bbT4KxnmEbR-MnyWX7zeeTEHC5YbWSLwnWUwRxfMdGYxL1n2kb7T_zAcMHnIis_BT9ZBpabLlp1Jzmu93xXnyuYsmzYgduChxpZi2atb28sBYoq85AUYyLAm30fFI4kHBuocqYjCXc6bfX3xzNpYSmOobP47-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080e5ecb9a.mp4?token=RT3OFHNCJe0OD45jG9FWiFVlCHE0tV0RR7t6ktFMHgLWPKoI5-gE5yO4ZihNX9nW8sEmRvm6laVk5Ph8cD-I2yzEvmWULXJdeUEVB8sVhYFkjE0WAnsvv6ygWPeH8bshS2RDyAR_UXFCkRWYDULgwNSok7x8Nxtqj5BZ4GHb_Howgt2_5Vs1ye2bbT4KxnmEbR-MnyWX7zeeTEHC5YbWSLwnWUwRxfMdGYxL1n2kb7T_zAcMHnIis_BT9ZBpabLlp1Jzmu93xXnyuYsmzYgduChxpZi2atb28sBYoq85AUYyLAm30fFI4kHBuocqYjCXc6bfX3xzNpYSmOobP47-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدئو پربازدید در فضای مجازی از چپ کردن یک پراید در سرعت بسیار پایین در نیشابور
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/662859" target="_blank">📅 12:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
تصاویری از حال و هوای کربلای معلی همزمان با روز تاسوعای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/662858" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662856">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gks8EbHRDe35eH3Oru-J95TOCBA_sUeD3s0V76bC8KJtDJpKbC2I1gLpm7HiXTc5SILvMpMGgGKzrRsWbOO1pqgxuYg-arRITavN8V7pb-z4ZekU-lbLJDlTkok-VobK5GwQo3R1r0H6QKUp1jiauamJDuMbtNIH5q4qaPKmVuiFuti7W4XtCqIZPCvwgUZkRiyzdzppNL0BwMKHmoA74cQpxqoVYKTCA5W3aI7inShadmBhw2m5NCYtzAfTKMzR1M1QAGH5r0i0MX7fjeUAv2x481jUE4vTTiYoKnGhcYQndwXjTSxPGPYicZ2yjzzwM9Y7IdV2TCTbETYjH2NIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نتایج تیم‌های آسیایی بعد از پایان دور دوم مرحله گروهی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/662856" target="_blank">📅 11:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2df765cb.mp4?token=E0lb5XSTp6_ulqI8QbiMiwytrsFgUH7_ilGlca_Uv7TFWOTe2V53-3ZWITqN-3oKUyAcwXt4w2xNy5qzq5DQbgcqldLqx_BABqcUkTEHCtpKiLTX6v91tIGUMPNUrRyOb143I7-LEI7ff_CHIpKpfjxrhYg_D30qB-fINj5D3fvB91HpJzb2s3Bo4ep3RK6cLshGkQxOVpdeKpclVIiU7ptdD3Hr6C6Q91WlI8JRT6Eyf58hMCyk03_dm1rzL7yQ6jR2wBn-UBy4JTqmGIGOPs0m9WUnF4dOn_4CNaAaane_7ivaDNsIAMwejYn69A9BY17j1qfoD4bHHuOMv0a1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2df765cb.mp4?token=E0lb5XSTp6_ulqI8QbiMiwytrsFgUH7_ilGlca_Uv7TFWOTe2V53-3ZWITqN-3oKUyAcwXt4w2xNy5qzq5DQbgcqldLqx_BABqcUkTEHCtpKiLTX6v91tIGUMPNUrRyOb143I7-LEI7ff_CHIpKpfjxrhYg_D30qB-fINj5D3fvB91HpJzb2s3Bo4ep3RK6cLshGkQxOVpdeKpclVIiU7ptdD3Hr6C6Q91WlI8JRT6Eyf58hMCyk03_dm1rzL7yQ6jR2wBn-UBy4JTqmGIGOPs0m9WUnF4dOn_4CNaAaane_7ivaDNsIAMwejYn69A9BY17j1qfoD4bHHuOMv0a1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کل دادگستری هرمزگان: متاسفانه موشک دشمن جنایتکار آمریکایی - صهیونی مستقیما به پیکر شهید ماکان نصیری برخورد کرده است  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/662854" target="_blank">📅 11:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b38aa3fa.mp4?token=ZvV6Qf-jaJxcjdv2yz3xCxtIMDz2bjVNblblygHD0HSmmeTGe3YVGi_yTGIsQ8T9xWn9we98IEwWVZ8nwvepBcBULvZv8t0gsW3uTLvQF5i2fGrIK5uQ7YDI0R2FS1ex1lwSLAxsV4iBTmJcc1FxZGfQOw6vGa3CWNdEiHzMF2spNDb-jTUUfpq3pd_OGBj_CgArQcGyXv6pOkDfZ8iMuFWXeLifcWQa0mjt4jJLNUfmzygG2fUPhQuBKqMthfpcJ6e423j2Y9b-P65ZJdbI8ngl90e5sBv-3L27ohRAc8dJZqQX8j-zGjjkHz72J19iqUuhE35a1mhpLZJsRvLrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b38aa3fa.mp4?token=ZvV6Qf-jaJxcjdv2yz3xCxtIMDz2bjVNblblygHD0HSmmeTGe3YVGi_yTGIsQ8T9xWn9we98IEwWVZ8nwvepBcBULvZv8t0gsW3uTLvQF5i2fGrIK5uQ7YDI0R2FS1ex1lwSLAxsV4iBTmJcc1FxZGfQOw6vGa3CWNdEiHzMF2spNDb-jTUUfpq3pd_OGBj_CgArQcGyXv6pOkDfZ8iMuFWXeLifcWQa0mjt4jJLNUfmzygG2fUPhQuBKqMthfpcJ6e423j2Y9b-P65ZJdbI8ngl90e5sBv-3L27ohRAc8dJZqQX8j-zGjjkHz72J19iqUuhE35a1mhpLZJsRvLrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مداحی شور‌انگیز عراقی برای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662853" target="_blank">📅 11:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662852">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae32ebcfa5.mp4?token=f7haCEB1jc2-BLDvdVF6d2jVrLN0RDNAPEb-W0eE2MjLFWwEwts6Rax8Do-9tdQUgLNRC2tBfekcr2cHwqv_h_6nIGHk89ao38NNLUKGrXkH-_6j1GMJoGyiGE1x1h0_kcDu1YloUNQ-WdI_RrEM7BSHRiejry_NQezkNk9uZ5FX1_ECjySySiiDW7IR3C5ox6dpeb95kRzuc6XvFScT7d6Cy-MG1OQC6UThFWOVWXM4cqyHaA9mdExn5ac2DOrXmt6iFPSyzurtkaTL8EwZV_3eQKUXpTJxeTuKZiy5M3IyC42Ecm0vLiBVvIkNsrEyWCCi1c85xBybbvgenZwJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae32ebcfa5.mp4?token=f7haCEB1jc2-BLDvdVF6d2jVrLN0RDNAPEb-W0eE2MjLFWwEwts6Rax8Do-9tdQUgLNRC2tBfekcr2cHwqv_h_6nIGHk89ao38NNLUKGrXkH-_6j1GMJoGyiGE1x1h0_kcDu1YloUNQ-WdI_RrEM7BSHRiejry_NQezkNk9uZ5FX1_ECjySySiiDW7IR3C5ox6dpeb95kRzuc6XvFScT7d6Cy-MG1OQC6UThFWOVWXM4cqyHaA9mdExn5ac2DOrXmt6iFPSyzurtkaTL8EwZV_3eQKUXpTJxeTuKZiy5M3IyC42Ecm0vLiBVvIkNsrEyWCCi1c85xBybbvgenZwJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گزافه‌گویی‌های ترامپ تمامی نداره؛ پست عجیب ترامپ در مورد داشتن سلاح هسته‌ای ایران
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/662852" target="_blank">📅 11:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662851">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOQgRJf28_aXO4LuSHBro1eYl0a3lLfig3x8soHN_4i_UlffEn5rOnlAnBxF-qfckKeF7CiUzY-wiLhzhEtatNXJO9d0LZ00A6T8lawTtDFDCedR2Xgv01KccAe-OkYcb8ksQCm5_Pv9nG-_HCYPP-thMXRFIowO3F_txMYKky8qdU1OKfu3306cuYqdT0MxY6wP4iGpludKwEIIVcREASaGcDJlRazt4lNZ3a3QAsMWjmrjhTQTG5J2XrB575C-KLJTQLvKhI7aS_8LB1uDxc5YIj7pB6pF6t-UrtKmzUJmbUSxw3C9EPIr19Ng47JOZH_aHWyCvsSCS0ah07yU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مخابره کد اضطراری هواپیمای سوخت‌رسان آمریکا بر فراز تنگه هرمز
🔹
یک فروند سوخت‌رسان KC-135R آمریکا که از فرودگاه بن‌گوریون برخاسته بود، هنگام پرواز بر فراز تنگه هرمز کد اضطراری ۷۷۰۰ مخابره کرد و مسیر خود را برای بازگشت به تل‌آویو تغییر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662851" target="_blank">📅 11:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662850">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686d4f02f4.mp4?token=TcGansgpYE8_wJlS61OlbARKogmusdycejdbrEdE5kiWkosSRdQzoQbtJXuQbQAhMtY-wTMB4o3RSKClxZR3xt8qdyDqbwT6gDcSTw7f4tvLoBi-eRTxCFycJ7tVREI5X-Golv9OSHcUxkbTo669x7a8rtG4BTE5RzImDN8-LHNZaYre2qjm6qopkhlPZfU74r_49nOj-Sott4gBmzn2mWCkYQKHDS1tSUFF3kZ0BfnXbY3d8vUai8EFTR67HmIj2TGfDGoc5WHpis6ni4YG6tmHLEhbcM4OGuUbSMWLpketfEqNqw5vfS55X5AoPn1HPrkSK0Sm-oF7VJhd2NfDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686d4f02f4.mp4?token=TcGansgpYE8_wJlS61OlbARKogmusdycejdbrEdE5kiWkosSRdQzoQbtJXuQbQAhMtY-wTMB4o3RSKClxZR3xt8qdyDqbwT6gDcSTw7f4tvLoBi-eRTxCFycJ7tVREI5X-Golv9OSHcUxkbTo669x7a8rtG4BTE5RzImDN8-LHNZaYre2qjm6qopkhlPZfU74r_49nOj-Sott4gBmzn2mWCkYQKHDS1tSUFF3kZ0BfnXbY3d8vUai8EFTR67HmIj2TGfDGoc5WHpis6ni4YG6tmHLEhbcM4OGuUbSMWLpketfEqNqw5vfS55X5AoPn1HPrkSK0Sm-oF7VJhd2NfDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روایت آیت‌الله مجتهدی از مواجهه حضرت ابوالفضل(علیه‌السلام) با صحنه‌ای جانسوز در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/662850" target="_blank">📅 11:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662849">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
قالیباف: امنیت منطقه باید توسط خود کشورهای منطقه تامین شود
؛
یادداشت تفاهم اسلام آباد تبدیل به اعلامیه شکست آمریکا شد
🔹
توقف آتش‌بس و پایان دادن به جنگ در لبنان برای ما به همان اندازه مهم است که توقف آتش‌بس و پایان دادن به جنگ بر ایران اهمیت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/662849" target="_blank">📅 11:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662848">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای وقیحانه گروسی: اولویت اصلی آژانس، اطمینان از محل دقیق نگهداری ذخایر اورانیوم با غنای بالای ایران است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/662848" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38b526605.mp4?token=vGdsTygFlZ41H47TrR5WqJttL4genFl1bMs6jJcZGUovadK3Pph6KRLgZX2NYZx5bXPLHZGYKQ6-pT0OHBp5Y-kvuj6joChlyxMEcugx6rBP6l_SEqA14z2t4PaooscRd9PEXmLQ1ZkLEYhVWi4Z27FZM0UR7demzZXG7fqjfWAeeWnjezjhxDRYhuF7kgW90gCBTLQwiAEScMPYU0Es8Dr19r8o20SfSzxWR-wrOSdEOnZesdJ1EB6gvOW-_YKy70f1VcoA2QyXPi35M9oV6iBkE7v92uxrcKe8m5ah95rX9mM0axXsjni9S72GlnFNkHx2sOLfJfKqanYsW1s6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38b526605.mp4?token=vGdsTygFlZ41H47TrR5WqJttL4genFl1bMs6jJcZGUovadK3Pph6KRLgZX2NYZx5bXPLHZGYKQ6-pT0OHBp5Y-kvuj6joChlyxMEcugx6rBP6l_SEqA14z2t4PaooscRd9PEXmLQ1ZkLEYhVWi4Z27FZM0UR7demzZXG7fqjfWAeeWnjezjhxDRYhuF7kgW90gCBTLQwiAEScMPYU0Es8Dr19r8o20SfSzxWR-wrOSdEOnZesdJ1EB6gvOW-_YKy70f1VcoA2QyXPi35M9oV6iBkE7v92uxrcKe8m5ah95rX9mM0axXsjni9S72GlnFNkHx2sOLfJfKqanYsW1s6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحنه‌ای نادر از تغذیه یک گوزن با مار
🔹
انتشار ویدیویی از یک گوزن در حال بلعیدن مار، تعجب ناظران را برانگیخت؛ این رفتار در میان گوزن‌ها بسیار غیرمعمول است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/662846" target="_blank">📅 11:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
ازسرگیری مذاکرات فنی ایران و آمریکا با میانجی‌گری پاکستان و قطر
وزارت خارجه پاکستان:
🔹
دور جدید مذاکرات فنی تهران و واشنگتن، هفته آینده با هدف اجرای تفاهم‌نامه‌ها و ایجاد خط ارتباط مستقیم برای پیشگیری از تنش‌ها، با میانجی‌گری قطر و پاکستان از سر گرفته خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/662845" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3b188c09.mp4?token=lm43SU29_5ALZBKL-Yth6lke14Ng41TqkOm3Irbqa1iTJl8ck2cr0DgrV6fF9OBNa5Munn7sl0WpxCe_KwdiUIwfEOXhyyjdvPI3-6MTG4KODHrjNUQ8L8wRvFte3qur-lM9nPHrzXEIVj80rTHYgpKMY7-_L9lUC6fritAHcf-We0jzv0rv_sHjSaNEJGQX9-RJtDm8qBc6E26Css88ciHuo-60q0riEPVfJUfvM2bF9c7PGxPw3DNVj7QX7m9zO0BpgrSWM5gF7BzIxPC0yyV4FlKIsPepnZ9ekx6KkX6K6tkExB5UrBNbFbjxLZwjPQX--6qzpBy--QYfno00QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3b188c09.mp4?token=lm43SU29_5ALZBKL-Yth6lke14Ng41TqkOm3Irbqa1iTJl8ck2cr0DgrV6fF9OBNa5Munn7sl0WpxCe_KwdiUIwfEOXhyyjdvPI3-6MTG4KODHrjNUQ8L8wRvFte3qur-lM9nPHrzXEIVj80rTHYgpKMY7-_L9lUC6fritAHcf-We0jzv0rv_sHjSaNEJGQX9-RJtDm8qBc6E26Css88ciHuo-60q0riEPVfJUfvM2bF9c7PGxPw3DNVj7QX7m9zO0BpgrSWM5gF7BzIxPC0yyV4FlKIsPepnZ9ekx6KkX6K6tkExB5UrBNbFbjxLZwjPQX--6qzpBy--QYfno00QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قالیباف: مقاومت ملت ایران نشان داد که دوران تحمیل اراده بر ملت‌های مستقل پایان یافته است و این در دنیا تحسین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/662842" target="_blank">📅 10:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQqa0yqSzpq1NHBloQnZh0_m6Hv1cHOurNmKw67-TyYl31IImToa7ndg23gKGYaXTKytbJLNuMQOAz0OVlUCoDDo1InpWj0iiFTBZIIZWvmOKn7Wi3qaj14V1enCWaKey6jusbGZ_cMELdTw4Awk86cM_1z4wUx9OHlXoPqEv6me1xNCtcbdUqKkp_9uqXKzGxODeCPLueREfG1pa4Z1WBeJIA7SFxzF5rkikGrkC2-zfj8Eo_LK4fFghWebQz00KIoKoTCOhXJmFqjY4VguqIj8RHQdyyRtumUHt9NE8ARgO_bEvGoDwhA7Uk5r2btU5uNHH_riRZxkIwWEC4ESJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دشت بابونه، اردبیل
🇮🇷
#ایران_زیبا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/662841" target="_blank">📅 10:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a77ace8f.mp4?token=DWYRcrpP_LazBrRt780FzrF4hqTkqI1pXiAuyx2jDjzf1hVISYk0sst_z5opWkj_IU5UvZYkmuPiHNoATPQ6SivqBRU8YsLjEsCEAMN33WibEJun66imtuPgONu_KwmHEzLWJ8GHKFC0hOUz2NYRvgD6bMFlVDoTLsbJFvNG7Oc9DQ0QwFGFRsdCd-c6Urc94TjLxYycCfKX6TY00lRt1sAoMZXpksuH7Ghwl6gGo1SjnDNrNGStMLmrry-uF46xVJs3dQp-HZuPh1KsO13ae1fbV9lOtD1FFXcKzc5d63eaF959chrDvt4Z-GDN5S2hVskLweXTRuNcClxWfnK7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a77ace8f.mp4?token=DWYRcrpP_LazBrRt780FzrF4hqTkqI1pXiAuyx2jDjzf1hVISYk0sst_z5opWkj_IU5UvZYkmuPiHNoATPQ6SivqBRU8YsLjEsCEAMN33WibEJun66imtuPgONu_KwmHEzLWJ8GHKFC0hOUz2NYRvgD6bMFlVDoTLsbJFvNG7Oc9DQ0QwFGFRsdCd-c6Urc94TjLxYycCfKX6TY00lRt1sAoMZXpksuH7Ghwl6gGo1SjnDNrNGStMLmrry-uF46xVJs3dQp-HZuPh1KsO13ae1fbV9lOtD1FFXcKzc5d63eaF959chrDvt4Z-GDN5S2hVskLweXTRuNcClxWfnK7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اظهارات شنیدنی فوتبالیست پیشکسوت ایرانی در بی‌بی‌سی؛ ایران، تنها کشوری است که مقابل قدرت‌های زورگو و خفه‌کننده ملت‌ها ایستاده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/662840" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkkKPde03Lt70CoV-Yt1X0smJouIAoWt1vOc3npoU5PH4c4HBLTo7nd9sBVeJfWcTP3aA8tZwJlQ-fIsVvjFrrHM7xMcRrtWEKDsB2-TiVS0VbpHDEUcETMxcN2OkkEOxzhcs6lMrgJ5wv2yW2qFv9urpIeiX4xmUTwO2nahNQLhx9Mw-qLvLdu5r7glYn9KEDY66Rwf2c5fvwtHQgSO-ilevTEPo9hRAGRtdJbZc14WmYm138a7Xg6yJIQnf4lwH7-5ewVM93KG4J0ytXAdVA6cNgDMKAzhrslNUi7lSnZY2vva6czwybIUPF1xpUWCOuoE2HUHb6BW8jTIuethXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پیام سردار مجید موسوی به خانواده ماکان نصیری رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/662839" target="_blank">📅 10:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msLmHFxJ1kTUY9qlSEhIg81WDJcoyUIqgJU_U2bs1kRCKAm3FpAg-SWuRpxzAA91ySSKk0j8qnRkWSPNp2wc3KEO5tastjPxFsdEIIaT0klJlZJSIE8co2yTeHLh_SXInOt1z_tz9Mz2Hw68CfHilJ0V1biS6www7tIE0Fsp65-g__5vxu9dKfqai9b2LWRGT1NzNFLPZeR614m874-ByraCrDdUPXxe3u6re7_tQ-ITIry38h3GXxIme1q8sjEt93coz5ANzsr9r9O7o5OQFHdy6nM0BDDm-7UcV0283pm1GDvZr37O5_TsSIcOIALPM1ySJ5P_L3F5hWgD42BCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLGdIG679oNPKn1ndYj_DaXIKHjuPhJI8nY_L2Y4C9SYuD3yY3n3PqVf8YYEHNyjbKtJn_qSEMTY8XxxBA146DdYO0hjsl_udKv-hyMvv9UlqN6s95uZwqSUCHV2W4HXvEXRMt2H-OwHc7O45s59b8yTcppoMD3l1umiiiWYORBEXU07ScGrshfMXo7laXNfxURwkg4OwBFNsm0yQqeJi38QDYJFmclz8nXnqcvSYn-J-KqGboKQ7NrwGk-fqWTfyvJohZwy9FeqXTRpRpxtc7Jyjx9pA-q4AHxg2IV1OozBeA4It-gXKstuHXyJPS9ij0kyQ3plLofei25URWqUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksloXPaVAz-hdL931_EZnqRMK4HS1o_JkoiCl07y2gtaVyOFxZzAeSs53tOfJHiQ0uOL22szPTi7UdTWjycpqI327ke5UPbliF2kEpTO_TIzv2QMKY5zeYNYJbpiMY-enTyJD6ItP7wG4uR_hKsa7Zeiv3Nceg5iNikTDaQTiAfk3wyPYbH7pVhWicGLHCNE0zyXIG1HOifR49Asc5xh2OUBmQQKWgLXcCGdrpUfDVizbWdKoKlvzeYT1lAx3Iey2nkF6SVOxmMXk4pUQcvmFhz8POEjuU_ShSoqUCtCgl7b_EGLW-MvmIrjTJXWr9mqHCRFQn20uvp-Rc8RL2yRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOk3pRd9OdVSbe6hEK3gxkLoqZbGd03QUdBYKeQoAphKb5HU1_q5ChZBe7tZeqkIVL3VHKZS14gtD9nzNyrXXaOc2uK5AVlfc-QMNiPh6BPHLwMEIcSftAVcL9wF9Nc9s9IGAZdCllqht_jw8abAcB6YLyY7j82bDVeACdBBUIsPZtJLo91_6uYc-NtZ4cw1iUyW8un56PKyCS-sShLkjkWlwyxjiq6M_LcnhOExfdF7qEL8irre27fTPcyVfON0v5nfGv3Bmmm-9tpIbCUb1XzGDvex0ufsvUKYSHst89ZOHeW_Hzg_PmbAbK1uIDkEqAXzlOgZXC4-Wm4VsjFomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aL5NAfKJK_glRY1vxzHjW3JKEeuOch0my22lSqfdQmyypSS1gSJsjA6KgBZHJIddePRw3yJ7Kr30unUomEIwI4EDpCq1oJLyyBMCmAUBNZLcc1Dp8MUYCwwo-Et_2zgkGd0dleTA1c7V6y26Nr5KAIHFqxVchJDPaCQ2-3ssICNlKivjDqnJhJEaA_KfxMSZH8AeP0h5L4xAkwLm53XVSDpTrR1leIuKckMiEn2fHkm-xxusihlXzTXBJnGJ0VhIAdwLzN4QVFeLIsJPcxiJXi_nwYcQm_KUz-lTTZpEgP2rNI289yUYCGn7I_RfcMmbL1nsE3IoMDJfWu-KKTugNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
آیین سنتی "مشعل گردانی" شب تاسوعا - نجفی‌های مقیم مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/662833" target="_blank">📅 10:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abee9ba63.mp4?token=dw3CF2X3Gzo4IyHBr7wMwkYRQuwbJjW9eAB0hcbT2RagisMDus0ZgA1SjuiyHben11BI1r0r2MEI02z8rxjzph_xovWyHKbP2vtImdnOAC4cameI7tAEEGDg72Fvzlubfdj_2yRRdUnhCm-8p_ci_AnHn4BnzFyfv2HKm_L7mIs_9kaj-DulRbZlwb1XTE2C4qtXzxS3A-xQMDg1sE8K-FCc2ZuzoKMaZLoQNnj58fB8uiuMx659YPlr8VQE07PwBVnQ8ccBx-WQQNFpWAEeVeNiWv2og2DaEmv36lgfVvsvPUjkt5fvq6nBQQ6ulfkcmbewlQPzKJJMMM0FsyEyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abee9ba63.mp4?token=dw3CF2X3Gzo4IyHBr7wMwkYRQuwbJjW9eAB0hcbT2RagisMDus0ZgA1SjuiyHben11BI1r0r2MEI02z8rxjzph_xovWyHKbP2vtImdnOAC4cameI7tAEEGDg72Fvzlubfdj_2yRRdUnhCm-8p_ci_AnHn4BnzFyfv2HKm_L7mIs_9kaj-DulRbZlwb1XTE2C4qtXzxS3A-xQMDg1sE8K-FCc2ZuzoKMaZLoQNnj58fB8uiuMx659YPlr8VQE07PwBVnQ8ccBx-WQQNFpWAEeVeNiWv2og2DaEmv36lgfVvsvPUjkt5fvq6nBQQ6ulfkcmbewlQPzKJJMMM0FsyEyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
​​
شاه با وفایی و شهید کربلایی و شاهدِ بزمِ مایی و شمعِ خدا نمایی و شورش سینه هایی؛ یا ابالفضل…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/662832" target="_blank">📅 10:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePRBp0Gp24FIqgJeYfxkoX2U9YcksQBWsQ8cXaNARyAJJWpnafZKa73PYrkQv3G5nxWSBwAYrFjnIEO2Bd9FVqRNXjg69MVj-gjnzm3eTKQOxoVsSUht49UB-2AB5LO1lbrj16l73GRey3drTbcQTFFW5krxWoFDGGPbiSX7VWPttrahkfaNMP0jd6txSPA0vFivxJ7J0UPWzUqTGb-oyuOiQoptkk9WsAMSAmoYK8Eb2xEoL50dGuMZllimFV3PjqommrdKHjGC_3rfihJCLJtfOMzovGb9okl6yYCN3G4OWHU95md1zdFjfXEDnRQlOIpeOsO6FM1oJm2yJDkUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات لفظی جدید ترامپ به ایران، رسانه‌ها و کنگره و سنای آمریکا نشانه چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/662831" target="_blank">📅 10:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr93uhM8r7oCU_oRYPlTa_8DhdmxH5ptpU10zdvqrDHowDzaDKkrwBwDD--O0UxGpuc8Oa33dfMiJ1nLjaRehUfc-nm3eAPxqMMqxT-bB48mR7LE4wqj1ztx2RcsObN1YnlLNIooXu86HWVG2qWOilwk2epQEz-4uSrPR2wyWOn3CkP--e2zXZR1h8ItSjicaAJGeCuut83iozfRAO_0IMfObLoGGc5B1BGUZWNkAGThT_yEeGOk0heQIoDMNMnYDIvGwhNnd6Q6y404TVu1DCq0OKsuIxGhU_gKPyjOaNct8ZkGYaTN3RBYqmy6mHaC5My5w8D7CXH7qB0x-jDV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دومینوی خروج فرماندهان نظامی از پنتاگون؛ یک مقام دیگر استعفا داد
🔹
کریس دوناهو، فرمانده ارشد پنتاگون و گزینه فرماندهی ستاد نیروهای مشترک آمریکا، به دلیل اختلافات کاری با پیت هگست، وزیر جنگ، از سمت خود کناره‌گیری کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/662830" target="_blank">📅 10:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU-4yqQTvaWcUhzTxmNEBo8l2tG04VmIYLXEKuZrwLtCR1Gjxo74ZcrWc87Twt_QYprLXj4zIpbjJHuCl2rpN8tDIS2ovKY_Dvde6R5d032dWiU8vy6gAM15onYygiZZ0yuPP49eZHrSrHcSMxGu64_EGWMq-yoX7RizgpVae_nSjKcDB1ldMDRNR_cIB_JKwg1--3vwYUkZFcs-jUkmJSZxlUiYsIK6ApLrBaR1K9a7zIANkD-aUqUrAXMpt5CbSCpNRHtVTsuukz2J2AjqFOwWH5hiLYyLgbH2mEVdFmrFs5hOqvf6bFwZ1bG69ZHG-27STOvAckhobXPQ6LojeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
توافق به اصطلاح آتش بس در لبنان و ضمانت اجرایی ترامپ!
🔹
محمدعلی رجبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/662829" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_n5hQJ8l2hjeY9a4cxCkT9B6MEVVC4XJXi0ZOPMXwfKxV9yyHBw-xfJnnVgcIhCC8uHKc3Tfy5ksDjuBjCuZHfENh5qvtTuCtcWe_zV_YDm7MwIEMuCPvw2tuBYoI3y9AyGJQZYOWJN-lTXBsoWz_SQd-r1eX_wpffLqJlQnwzc1Z2k1snBNN2LwI0V6xQdJDv6u7EgJuFKnKXAm5pnR5ROunUBxbkfWyz_xtIPt1LZQh6awolkWeryP2cdy6n_y0-rvuf1GV2Fmo9gJZFmD-ktKy5pJIlxpqhTRYDDJXlzL9DQtxtqmidVbC5TPXu-owIQHDHILMQZOMkHSIUFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
استایل تابستونت با mono کامل می‌شه!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/662828" target="_blank">📅 10:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0ujVZjuPOYRoqQEDG0F61au3cx6AL7PeBtbdQdYWAVbr1vcvGwEDzycGsfExBEQo-F1m7ELErRqZOVhEmqh6sYb4kBEFqymUENIrXdTXAPjzfudCMiaU6sh7Wjl9RARggIuiUagu0Ucf5C1a0_u0UL9EKkBOgJtdCEvS2_-KHTsbArM5vUFH5PM5a6RNsYPwKiSgZx9eWtZysUNWCey_2IbN0wBbpXEUEU2ibFp_uhmPAh1gUyQZo0gmp6Ij9_TWxTe021aW7cMXZ-6VO7MdqMwrdvE0d4FcRYXd7c89tn1hjgkiSUgLUAe2tgrcA8YSC4beEXdEhZ9EZV8nevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
انتقاد ترامپ از پمپ بنزین‌های آمریکا: قیمت را با کاهش بهای نفت پایین نمی‌آورند
ترامپ:
🔹
شرکت‌های بزرگ نفتی قیمت‌های خود در پمپ بنزین‌ها را به اندازه کاهش شدید قیمت‌هایی که برای نفت می‌پردازند، پایین نمی‌آورند.
🔹
این قیمت‌ها مثل سنگ سقوط می‌کنند! به عبارت دیگر، مشتریان «سوءاستفاده» می‌شوند.
🔹
من به وزارت دادگستری دستور داده‌ام فوراً به این موضوع رسیدگی کند. قیمت بنزین باید خیلی سریع‌تر از چیزی که من می‌بینم کاهش یابد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/662827" target="_blank">📅 09:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfTGTQ9oYSn0XrcAsFX4YgTZk2sjNSGnYhV93asSQuUfINkKn22rYVl71nvRtbFIUTeEPuEMkRhMW6BzrCSVsYq9OTLmfJmWGNz661JYcGGWnAqIUrTiVKsFBxfRMm0vFVYOryRoKhQ39g1qySMQcIit6EQpPXyZkvcKdNrV94XMuCBosQjqr-5mAZKoYi7dwXMRjY4bG4MHZkOQp7KoQ0lCy9L6qOQg7oFGjxsOlNYeifV7O7ck4DgGRLYjqTUsNlsckoif-MqHctl5d0u00dEguzY6XlxjopF6gHkncA3FMGFhe3mSkyMhHBQf5kV-JESMAJxurLGm2OZfPraSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر فدراسیون فوتبال ایران برای بازی بعد تیم ملی مقابل مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/662825" target="_blank">📅 09:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGAacXbu4YB0q2vP-TV-lRRecd16aRCZdPNeWQjgw5CoNnpk97Zqqls8sGXcHLzDgDdW-FDZwsWmejYSigytspg-qAzrMXsyiAm3efkRGKgC-M__lon29iLOJNfw6IV0RLlMnhEtSvCkpwGV5TBxog-zeJOIXWC72TsbVpl4LWo7MApQMSsnQRw3Eb175kWbBURWaimdRu2ITDu8FjF4WnKpOORAb_6jv0CxTF8xn4uoyLu3RUbdTX3_8yx8iQBXaLLUlLJGdJ6p7908VqYX-jFsI84DUYa1L_rzQcEqQToGzgV4eoGLw7KUOW9eS7rAs1mLpMevCdWFdjVecnt0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول ۱۲ گانه مرحله گروهی جام جهانی ۲۰۲۶ پس از پایان دور دوم مسابقات
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662824" target="_blank">📅 09:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf527ff369.mp4?token=MuSsv0lhnG1pbJ8Q_zdLOPCAUMaVPEFFykJaYaIIz38pOzgquT-MArKwb6J0d7zV_FE7CANaaxn4q3Wj8g7UQFt6cScWEftm6_0xfYz11u28OkVIGVHjI49zmuMX2kOXP8SKRXmAyjVXOvUeyUrjpKh8LiNM6pUalbRn2CIuGAoK8U0V086pQfRr4x0AmBaPdRPo9v7H_JwtZtWRFS4egqRmQXRyGNz4jbiL5iLuGB2Q2ZQxAko36yMftEiTgvaeGZiLzjbnldL2j3nNFbn7W4Zdwy7X8wEydpF_u-EanpnsKUSrHsdOazbNyU951k_BgW9CvhOSc7uuX5nxe-kOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf527ff369.mp4?token=MuSsv0lhnG1pbJ8Q_zdLOPCAUMaVPEFFykJaYaIIz38pOzgquT-MArKwb6J0d7zV_FE7CANaaxn4q3Wj8g7UQFt6cScWEftm6_0xfYz11u28OkVIGVHjI49zmuMX2kOXP8SKRXmAyjVXOvUeyUrjpKh8LiNM6pUalbRn2CIuGAoK8U0V086pQfRr4x0AmBaPdRPo9v7H_JwtZtWRFS4egqRmQXRyGNz4jbiL5iLuGB2Q2ZQxAko36yMftEiTgvaeGZiLzjbnldL2j3nNFbn7W4Zdwy7X8wEydpF_u-EanpnsKUSrHsdOazbNyU951k_BgW9CvhOSc7uuX5nxe-kOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
نخست‌وزیر پیشین رژیم صهیونیستی، نفتالی بنت: جنگ طولانی‌ برای سال‌ها کاملاً برخلاف مفهوم استراتژیک اسرائیل است. این با اسرائیل سازگار نیست
🔹
ما کشوری کوچک هستیم، این اقتصاد را فرسوده می‌کند، نیروهای ذخیره را خسته می‌کند و جایگاه بین‌المللی ما را تضعیف می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/662821" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdCYWgC282n4qlMUGZrHj8DQzdAbBTpw0fwtvjIH1z3BJm2rKVjN2TuFQaSvYihrJQl18Y4n3JOYSLyy30EfxjqFdt37z_tyI9Yu5WF9iMUPH-rFpP6yu8ZLd8mL0BS_bYCx3wtLrEtnQejyYpDwpJ68R2HCDlt_DEi1yUIUE2zIlVA5rdIu9iAqwdD5yqAYRIJTl9ZoayGRds7frKVQjEZi5a65fICkmrzIo1A_XPlRnasFRe7X4p5Z1EdCCfNClSXfndkSZO-oBR1iVhtVLrW1C1OZAvL00Kf8DyItUULZB98L0Lb90tifjequxyGMZ2pc36P7flYwXX79Oc3TyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه مسابقات روز چهاردهم دور گروهی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/662819" target="_blank">📅 09:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
ترامپ: همه از نتانیاهو خسته شدند
🔹
افشای محتوای یک تماس تلفنی محرمانه نشان می‌دهد دونالد ترامپ در اوج مذاکرات پایان جنگ غزه، با لحنی تند نتانیاهو را به تلاش برای برهم زدن توافق متهم کرده و حتی تهدید به قطع روابط کرده است؛ روایتی که از شکاف عمیق میان دو متحد سنتی پرده برمی‌دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/662818" target="_blank">📅 09:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662816">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
نیروی دریایی کره شمالی به سلاح هسته‌ای مجهز می‌شود
🔹
رهبر کره شمالی، اعلام کرد که برنامه تسلیحات هسته‌ای نیروی دریایی این کشور «دقیقاً طبق مسیر برنامه‌ریزی شده» در حال پیشرفت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/662816" target="_blank">📅 08:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662815">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490b048b6f.mp4?token=JnhPiXtdzrpXI0L-Ohp_jGMltDwqS3yoALlMj5wv0hTFW5nhAabe2ZO4CWzJ5usroYWbsTiIPpKRsn6E8di-ps9t8T7CdaiL0ccfvC_ybQtuC3J_08sbDO5YfhEqf0XPE5qUGLhbP753F36UIv0vQQRny5UlCwIfv8P3KekxtXlPwPcGaDUise6DT8jHwwPOtezMJ2wSzUgv2504cSsf2uWnkbMasE6IsOebZ0kKtDZsah1eTsInEOGcZ2Pl3UySBk0oeMfXiEZeGEsYaLbuFuXGJzAcjCF-OFw7iEAjJBRgOCNBJieNscVZLgnagv8yyWS_iSSA6yO1i7VXyunR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490b048b6f.mp4?token=JnhPiXtdzrpXI0L-Ohp_jGMltDwqS3yoALlMj5wv0hTFW5nhAabe2ZO4CWzJ5usroYWbsTiIPpKRsn6E8di-ps9t8T7CdaiL0ccfvC_ybQtuC3J_08sbDO5YfhEqf0XPE5qUGLhbP753F36UIv0vQQRny5UlCwIfv8P3KekxtXlPwPcGaDUise6DT8jHwwPOtezMJ2wSzUgv2504cSsf2uWnkbMasE6IsOebZ0kKtDZsah1eTsInEOGcZ2Pl3UySBk0oeMfXiEZeGEsYaLbuFuXGJzAcjCF-OFw7iEAjJBRgOCNBJieNscVZLgnagv8yyWS_iSSA6yO1i7VXyunR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
​​
ای ساقی لب‌تشنگان، ای جانِ جانان، ای سقای طفلان و مظهر وفاداری...
🔹
هر جا نام تو می‌آید، عطش رنگ امید می‌گیرد و دل‌ها به یاد ایثار و مردانگی آرام می‌شوند.
🔹
السلام علیک یا اباالفضل العباس(ع)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662815" target="_blank">📅 08:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662814">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxfLkGlTiaMr4Ohr8keVtKWRq9ifPoGGHZ-hGhG7DT05Fua2gT7Xdsj8hzpYp7mOvmnOH3jxGYOywxnPx5r9TmFoAHBPykU9rGA0f4bcK-GMmrshW8Dlrb-hbpbC3V_7sHKvg7Di8bkH0bngWO1IN-f2Q7Yg81Yntn_p4yJG0BBCCweeLKXnIjQC7VZfBjChcolLUgvN0AR2tWbSPGE5AceFgG1Nz_PZB8-Ql2pzcUkQ4106_R6iD3OVSqK7yfXLUF66u2zRhn4iValld8iVG4vQ6TXiU-nC8Mrmew0OSxOmiXWC29s9so6yXrItypa0QbKh5XnxH0OsVqX9fH_gzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویرسازی شبکه‌های اجتماعی درپی بازی کسل کننده انگلیس و غنا در جام جهانی
🔹
انگلیس و غنا در دیداری که انتظار می‌رفت بسیار پربرگ‌وبارتر باشد، به تساوی بدون گل رسیدند. با این نتیجه، هر دو تیم به ۴ امتیاز دست یافتند و یک قدم تا صعود فاصله دارند.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/662814" target="_blank">📅 08:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662813">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkVj2CwDvhmWG_t-yICE3osBQY-3h0t52vNAVQxa81_teaA07ye98j6kJkGs3sYMYvi9lNJV_XxUIchLWTp94CVkszrHCyznHDeWuhfvY_5ICCLitAL4x5dIBcurH3iDrFeFNSGGVSfoEog4hLQMctRLtvYZJf--kDMsgosxgAt9lN-8TkOtsmIGEatEl6OR2yjp4BTZ_o6lPLT-doeNRsJ5_XgInEQCJ41pA-Mb-9KNMMXBqgj4jUhsJ8LwNU2877yj87lpS2-NLfQJno-TbUG0Bey755VX2qWkRszY2jadfHW8hoCAn8QW6EjwOL3MJxuxx_B_0063Rc3f8HXoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های صعود کرده به مرحلۀ حذفی جام‌جهانی پس از پایان دور دوم بازی‌های گروهی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/662813" target="_blank">📅 08:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662812">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58697aba5f.mp4?token=r63nGN_Eo0YInFmbxcSdtaKcJgcQs6W5EBXh-HihNszjn5TI1GRH5S73QEDmQrWAbKL3K2bYgpkJuAmpRB0rLEYNEeKMVaz_Y3mdBsVgI6C2uTnUjHg49o6QLyVzhcV8kKtQvQovWmOxYHqn8pV3fDJgSXtKzDD4epr498cMPdResKE2aFukCtMWKFGh00jOwQcjfzA_g9ejipU_ifHUZdL9bXT8E7h7QW-zErJOnlVxbVLf0I3VTTfhU2Hhi0rmo9ZlAHUJtqgzLe9c9rtkDdWnYjWEH30BUpQ1bo6t6PXgji1idFfzbujZzXDHyMMwnUSrtFDL0Xl7RtWNEv-3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58697aba5f.mp4?token=r63nGN_Eo0YInFmbxcSdtaKcJgcQs6W5EBXh-HihNszjn5TI1GRH5S73QEDmQrWAbKL3K2bYgpkJuAmpRB0rLEYNEeKMVaz_Y3mdBsVgI6C2uTnUjHg49o6QLyVzhcV8kKtQvQovWmOxYHqn8pV3fDJgSXtKzDD4epr498cMPdResKE2aFukCtMWKFGh00jOwQcjfzA_g9ejipU_ifHUZdL9bXT8E7h7QW-zErJOnlVxbVLf0I3VTTfhU2Hhi0rmo9ZlAHUJtqgzLe9c9rtkDdWnYjWEH30BUpQ1bo6t6PXgji1idFfzbujZzXDHyMMwnUSrtFDL0Xl7RtWNEv-3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: همسرم به من می‌گوید لطفا نرقص، اما من عاشق رقصیدن هستم
🔹
رئیس‌جمهور آمریکا در ادامه درحالی‌که حرکات غیرعادی انجام می‌داد، گفت: همسر بسیار شیک‌پوش من به من می‌گوید؛ عزیزم، لطفا نرقص! این در شأن ریاست جمهوری نیست. اما من می‌گویم مردم عاشق رقصیدن من هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/662812" target="_blank">📅 08:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662811">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تایید حمله سایبری به سامانه‌های کارت‌محور بانک‌ها؛ اقدامات دفاعی در حال اجراست  فرماندهی سایبری کشور:
🔹
اختلال در خدمات کارت‌محور بانک‌های ملی، صادرات و تجارت ناشی از یک حمله سایبری هدفمند بوده و برای حفظ امنیت دارایی‌های مشتریان، بخشی از خدمات به‌صورت موقت…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/662811" target="_blank">📅 08:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded7ff74f.mp4?token=CNWrQao8kCWlMTanQ7-uGmSap3nah4UYB-gf03DW91xGpoweGRdHxtoFe5r3dMyq8_Fe7-XpS3YzFwnLk0wZAyt_7qTn5HPi3hLxMkUT-CC8ma7K8_RPpGdmspbGD5poIPrk_bKs5JZk_YY6qds-H3pALez--3reaNMsA4KpZm7qAU_qV324j3KdVqwh2K7TEcITUsVtlZ7YXoezyvTFXeA-VjA9NtoLRXx7q9CkL6D2j-R1ROXE6PpudN_JJCaOPx8fV4eyk4ca3E4f39HNNutwROLW1JS5TVxf7SdYLQ_1NSYD_rhtMstO0mt2aCZDrCmF34mKVUlLjczlHUI7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded7ff74f.mp4?token=CNWrQao8kCWlMTanQ7-uGmSap3nah4UYB-gf03DW91xGpoweGRdHxtoFe5r3dMyq8_Fe7-XpS3YzFwnLk0wZAyt_7qTn5HPi3hLxMkUT-CC8ma7K8_RPpGdmspbGD5poIPrk_bKs5JZk_YY6qds-H3pALez--3reaNMsA4KpZm7qAU_qV324j3KdVqwh2K7TEcITUsVtlZ7YXoezyvTFXeA-VjA9NtoLRXx7q9CkL6D2j-R1ROXE6PpudN_JJCaOPx8fV4eyk4ca3E4f39HNNutwROLW1JS5TVxf7SdYLQ_1NSYD_rhtMstO0mt2aCZDrCmF34mKVUlLjczlHUI7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حمله گردشگران اسرائیلی در اسپانیا به یک غذافروشی خیابانی به دلیل برافراشتن پرچم فلسطین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/662809" target="_blank">📅 08:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
عصبانیت ترامپ از مصوبه سنا که اختیارات جنگی‌‌اش را مسدود کرد: دموکرات‌های احمق به داشتن سلاح هسته‌ای برای ایران رأی دادند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/662805" target="_blank">📅 08:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qemF92qFv5XU5ZGRqLIkBR2fcbGu3-jbvbnvdBsb_BuEkAK2qS6GTTRnidzwmGZL4d10MxAGf1nPL_bb1ltGb6S0j6d9eb4CzMEkvKNijTKXqTJGGUHCNTuVtuFblSPRmNyI_oX3Er7MZy6QJvrTcSS6KNvJWnxL5diAliWmhAbqFMBNWzVL8RgwHMvQTKQNqrUKFLT-TjfIYAax9qJWFdKTZ4uXbjF3_-2-FY4EBLdudyhVWJWHu-qkjPia3fyBnPqeoN8cC2PrS3sR8WULP76QC0-3PzC60iAwO1QBk5UtGaJWeOid1hm9VI3zlPC5pFeqnFcq_J-kUTCcxBWbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳ تیر ماه
۹ محرم ۱۴۴۸
۲۴ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/662803" target="_blank">📅 08:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilCsi9szyx2yKi3kp9Gqd4HMipzR_IkvPXFy3Wz5NYa6LzizFYILe4hv_H7HwjFXCrAQUlFaSS_hlCguCARi-JooKdi_xAd-1i7WcOEAlR-mXibkJhjctBTjhMc0Hcs38baxvTvDVhEfv9pi7_2gOWM9bVX41Lni-5i5CvWiSUECk3kGKeBUdZ3V6xxiOVzUSnRrtNLA5B19f6GVJ7kOs9vewU8lAeSQrG6K3xVmFL3CVRASB7Tw2J31R7WgWzuFyXjco5S3ze8bODTpsfH9U4EHFWEv-3PkIFatiQ8WpAko7tMlb3hJuS5mxmFw2gJs3ByEzj__bx5iukjuZEJXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پسته لیام؛ کیفیتی که می‌توانید به آن اعتماد کنید
🌿
مستقیم از کشاورز
💎
کیفیت ممتاز و صادراتی
💰
قیمت مناسب و بدون واسطه
اگر به دنبال پسته‌ای تازه، خندان و خوش‌طعم هستید، انتخاب شما پسته لیام است.
📲
سفارش و مشاوره:
@LiamPistachio2026
🔗
کانال تلگرام:
https://t.me/LiamPistachio
✨
طعم اصیل پسته ایرانی، مستقیم از دل خراسان</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/akhbarefori/662802" target="_blank">📅 01:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFJISrUARMddKoPU0Qi4q_qZ6Tkiy4FG36uOLo56PrnUFvRNfiE2shj7hSU1DjWZG4CraHevZw2uOd9PTog8ErUSt5DpGI8hNL7HanyhWz9go5gDJihGQ6dQ3ZVD6Cl8_nxJ5lyQj5Y_-xKMSfpDFr9MmP30NanZmPbgr65cTCkECUAPD856CleVz2bO9hTcDzfU7UmkTBSbG9ynLzUbf33zVyZM8fztorZGHoWrD5E0tH4m2bEQDPa_nWoKHxBCAB9U_SmHdHHsUrmdFz09LY4lvZrILtiYfNUMdH7EqlVvuJht2gz2GOdS2xFjqSKYmzPPKFhNSKS3DT3oNMrFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bowqOBxW72zSMpKbUSsxFjg1wmTnIzBXqLgO550cPJUpIXSBf7Vns7bGgDxq6AV_sgP_jbbXOkVAJFhRCQ0FifvcKHulbi75at1836DYZ_jQo05gzNG_MFhyo4WUJbMozqaYB1UpnIhCw7G8XwOIVx5NbhvLjBArcvXK7u8Y-cAnOVcuttFtB7YwJGdcy61fze6fu41XsCB9-_MWwhcR2hE6hYsKzS-FzJTMjyZAbhx5bBNN5264aGCfFVbPCJ0Y1ysriF7vb6fadF0X1DVv4ysH4w1X0SAAK4JaKofdxXKwkxiqebBpBahi_Pi1J_ltt8kMyBlL-lBKr2K7SMXQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY-qG-hoTs_9ot93M1NbDwFmYbPydZOtU2q4tTlxkqeeXwDGNm-pa1kXocc3d1wEdaceY8KWIkQsnUteYHc-LWR_uGGCgm8ArhiOaevFyQ1PWHRszY83y5B469Ifd0VKjH5C_EJ1T2EZ5U2CsUYQ6w5Bljg3bkkEWdOQOy0-LZaYuv5o6UyJ-o_igoJafuijupIEGzXHEHkphF5bkIP1ZeW2u2EzqsRijD8fFcGpAVsr_t2VtnUgT7_E5TV0sfpiZvgdwvM_PhYvNOIiCRCQ9CtpMfb5KJVcc7Vsh_F5QFwT5tW9uq9JFDCjHNLBtFNuNKRXSzYNPEN1M-QJ-Y68Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UN-zBVjvwwZLx-YvqCdgu1XwrytuOT_fQphDNXt0om7-AW24N71Y3QLzh-6cWFixMdUquVbO2f5-n81e-A059z486qk8SEWKx3KIBPUmWtz8tnIlVbbQuTZnpMzmemOJa_OFY1AeXaHlOMAJdMw_dhlL3ajecN1PMp8DZ87ontt1dldvf7TlXBpnne9yx7h5fctqUymD_gvgpBzfjgFnq5_tcU0os2i1M4KK--X49FqTsCOVZhrcBbld1_Iq1HunhcHI7Jy6IlUo0a8rQR9yN_z-zf4XMzfHyTzagB4VJ-WhCecrKvuZLYE4-Na_2qaDLWiABQpwMfl6Gn7wEsoyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAJSTQKwj0A5UfTkm5LMwfGrWmXF9Ew9eyq1-R2SnNbjO8Ai8pCVQAJa21CKlNk7_fyL4Ie7i1GJp7sYdsLjYHx5uypGrOzsrRIsjZV83WmV4k3qs61F7Iq1cBLWDKD9cYTQZ3ovmGUPDJoHkdjJx6DplpURRCNRua2E93Bv223HR840GHsePiuwD9m3x5Sz6eYuNHfG0ugNcgap25G_BrdBqLFzTAC0VER0HdR5l1dakF3M3L5sYuCpLerFTqwdz-DgJMUq2DVvvBUfS9XNvJlgl99Om0oCDtujkPGMbze4MfOtxMlbbCP6uF-umTpHg60RA9c5WLJ9MaWzM7BL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQpFFwRNM9a_ZrlKixSSXV4zDA8uWe7H9eA9BuuWUr3OE1VYqecS6NPjjPwocjdibSgBK5wl0MQNCMq846DOliBdVVLEMTGCIDufLo7JutSRAn3TMQ1qER-0QEbVoy2zZWPd1xNcQHsR5izAaVpDCYCdmDhSf-r3xgV0yr-M-o-OGAr_2obbiN23OymG_MjCInGPBRaCvA5CqYnf87kTcXeN41gg_UzU0KavhuTgHYfkDVR0-YcJo3Ti-aLJ7wN6Pq4bOjObzqiZZ0JmnHfLGnE7LchDgZd5zzGJ4Ke6CNtT_7BAY_XUWLgSxAyjbOQ2jUBMcqDNQ2ReW-202k4dJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgFJbon2uyjR-H25KU9Sq2VzOUlOy7t1wGrMVwRejETd0_Ag-ecX3lt63BwZaSd7EYgVywBsVMJmitool9WseILTR28ICKjMaiAgtTSQy9TNnF8NEmICRPAtyInB89xLdvgvrCUB6CmhelL0JWBYFJ3R7lusVSbnSbPG7BeV2C4W4UEywyjpUTf2ttxJs5_r3RKXCueCm7YGW3aI7eP2rlXb6I-p2DKSHAMH9BLYICdkBAnUxNEcdGeUI9lMQ6k3ocmn9Nm_bCW81d85EfHkGkldUHcxCQQCDWdG_LNP57BaG_YFICabMnsmRtEia3O63YyoNyO3hpY070nezjh8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCj-NPUOPiEbr7vcmm9FQPlpgvZ-cR40UjdxlBLnC5Ta55zMoGSc0WRMIgyQym317OEdTXQquQEwZtPSRLXRnTOuhnpeS0St9OemYSYuDq6k7GPv248snFzzr41AZuBVXwZ_c0u0CibedBZSLklfplBvZBi2TSm_tkjTlKGM6BHbTsXpJs2tHV7bLMrDzWZ0VUd5q5cvcmcuSQ-eJJBihNkpUMh28d6OfdBP7l0NmWqHyHhZ7mOSCv-xCTQpUcOt2Lwq0pwi_znEv20YqzMw08sWql9KblPlEYmNV-H0J-Qu69s83jzZUHbc-mEEb1V3gIXgP1fJjMZ-YU9BZjj9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9kk51-RFLivc6xy7fNIPZkfW387GwywN7z48FLy7WmGA2gbwRyMRl8ax3Za9cpY2A9FVCCpNwe47iv_p926VrQwDf44yi2QMIQ3-rGi5mOUhlRxiRYyw2KIHj01_TNQinEiXHZr4Ep8fl7RuqZaK24Tvffh4ADMv6WjmT_DzvQ3kZwuJQ0W7KUDJWSiEvQ7XBOxxEreiwL6C9Nose8EXbpaLrRKEMVQFV2l0QcXepvWvrQBuXCUPxhg6v92nDNTa8oxa_XWoRVLY-Zrg9gI-1Tx1HSnZYze21RqPxbnWwxZC6YHonde34w3GKi0eTNKQPUCg4cBHBe9U26m6ymdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_B-7IqOceL3ze_-2JJdx-b7CU6pajpajhk5qm1KCg535SM-MhbAiKcWGHTCDtk3joNGiC-_N0TnHgAJ7WRs8uPibz3x_q0T0wJzyu1HMA9ToLljeK5Uq8cJH8ZweGJ9jvWlBv82R6y1u-LfMngJ5rlbUnHghAlc5c79zdrfH8CarLu5XbpxsYGcN5O7J8Zo6sTIa-1Gk39qZ5uw4fFexc0aOvblovkxITxINK_nk2OXLjBHyiyWPHFYe0B1euCYHW7i5wyA376xfZ5VvsRHiMzc4aHdQl-fqiKaq1RS4g376DYS4LlWP-X_6aKLRbm90BF0tCB1G8RkNms4zK6-uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فینالیست‌های سال ۲۰۲۶ مسابقه عکاسی Australian Geographic
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/akhbarefori/662792" target="_blank">📅 00:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662791">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عمان از ایجاد یک مسیر دریایی موقت در تنگه هرمز خبر داد
خبرگزاری رسمی عمان:
🔹
سلطنت عمان در راستای تضمین آزادی کشتیرانی و پیرو رایزنی‌های ایران و آمریکا، یک مسیر دریایی موقت در تنگه هرمز با هماهنگی سازمان بین‌المللی دریانوردی تعیین کرد.
🔹
عبور از این مسیر بدون دریافت عوارض بوده و کشتی‌های متقاضی باید هماهنگی‌های لازم را با این سازمان انجام دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/662791" target="_blank">📅 00:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894112c41.mp4?token=GDjJTAsrnx4gy-NFBVx9R_JxTXBJ53r4D51QGhjFpHsg_dt2xm7Dcq1pUNLOsekCKZoccbx2s0NcB1y33tqaOqWlXldI7ysR-XM-7NRoTewfdLO7i7RBkPxZAPvyRxTyOLdMj-j3UIgtO755lG4qW9pAzfBvx6k9t6nH6ygilDCPa-QB3ps_yzgGVcRJV-MmTaHwORMU5mh4MDxHGNPNWRYZDg4282Z0WIfStrWZf7GsBaXP64YeNvPb-PyKnhgZDm7QzHR7WU27tzWtH2sO2e6KQ3we44o8eB9q1dbKTTgeQdx45HyWYkdUUvRlp_Lwbed1m7YTGeg49zjbVZJr1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894112c41.mp4?token=GDjJTAsrnx4gy-NFBVx9R_JxTXBJ53r4D51QGhjFpHsg_dt2xm7Dcq1pUNLOsekCKZoccbx2s0NcB1y33tqaOqWlXldI7ysR-XM-7NRoTewfdLO7i7RBkPxZAPvyRxTyOLdMj-j3UIgtO755lG4qW9pAzfBvx6k9t6nH6ygilDCPa-QB3ps_yzgGVcRJV-MmTaHwORMU5mh4MDxHGNPNWRYZDg4282Z0WIfStrWZf7GsBaXP64YeNvPb-PyKnhgZDm7QzHR7WU27tzWtH2sO2e6KQ3we44o8eB9q1dbKTTgeQdx45HyWYkdUUvRlp_Lwbed1m7YTGeg49zjbVZJr1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارلسون: اسرائیل در معرض تهدیدی جدی است و آمریکا از آن فاصله می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/662790" target="_blank">📅 00:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
رئیس‌جمهور پس از انجام سفری یک روزه به پاکستان و دیدار و گفت‌وگو با مقامات این کشور، اسلام‌آباد را ترک کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/662789" target="_blank">📅 00:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662787">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مهم‌ترین حواشی و اتفاقات جنجالی ۴۸ ساعت گذشته جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/662787" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662786">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8d2be7bc.mp4?token=mSgs_FwpIFLlgpTR-cZriJLUGpnz9oe-G9Vt21r767VHi0bE4UGkQ1bc3Pk3M8NFVp-hCQSlLz-_kbGF759jOnqh59OAtffyTCmpSo7mYfFsvASzfHyllDdRk_KGaxYxeHM3eMMLFPk43kvvcr_XK14nnnxRzXWp3VE424ewFkSro2SmP-dfvdv47ujLl4-q3x7A6ZAclywZIviBllar1I4vOH9Zbsu5A4NfnoI4XM0DMjbcIaMASd_H1OLCAiiCzFi5W8HNK8WwIdgaJ_H06Sa-dnWpH03b6htiDs0uXjhXKYa1M82PUyuf4B-G85w17Yb_Wb9QXUIPJ316TyDQ1XhKwM9-ZQcJIA1vKy-imF-8LSibrhvxONB82nfB8vIN2TmsOsjNNahnWJNlQWlYKZI-3-ME_yGANUC-tskmsj9DGMwy0sx3ste5qz5deNFQHg7MdChyEG4FeQCalF2K-Sc8iClU2Z5elAD6HP0f77UK8TZ77E7IyuKHGeNWFMyV3SysiFadtMuklXWY0YF4A0d24JpnOOkd8EctcgIMgdS9MCyjlfc2KMQqE_rSc5qI2vyytzMlQXiAEDn1EkNEoipUVU8quW3fNpFBt_ItL-w33qyFaEyOoPRpd3L9IIh-0FVNB6cpbN5cYW1wEXicd9W7ie0UWd8_oZqMZrbqX94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8d2be7bc.mp4?token=mSgs_FwpIFLlgpTR-cZriJLUGpnz9oe-G9Vt21r767VHi0bE4UGkQ1bc3Pk3M8NFVp-hCQSlLz-_kbGF759jOnqh59OAtffyTCmpSo7mYfFsvASzfHyllDdRk_KGaxYxeHM3eMMLFPk43kvvcr_XK14nnnxRzXWp3VE424ewFkSro2SmP-dfvdv47ujLl4-q3x7A6ZAclywZIviBllar1I4vOH9Zbsu5A4NfnoI4XM0DMjbcIaMASd_H1OLCAiiCzFi5W8HNK8WwIdgaJ_H06Sa-dnWpH03b6htiDs0uXjhXKYa1M82PUyuf4B-G85w17Yb_Wb9QXUIPJ316TyDQ1XhKwM9-ZQcJIA1vKy-imF-8LSibrhvxONB82nfB8vIN2TmsOsjNNahnWJNlQWlYKZI-3-ME_yGANUC-tskmsj9DGMwy0sx3ste5qz5deNFQHg7MdChyEG4FeQCalF2K-Sc8iClU2Z5elAD6HP0f77UK8TZ77E7IyuKHGeNWFMyV3SysiFadtMuklXWY0YF4A0d24JpnOOkd8EctcgIMgdS9MCyjlfc2KMQqE_rSc5qI2vyytzMlQXiAEDn1EkNEoipUVU8quW3fNpFBt_ItL-w33qyFaEyOoPRpd3L9IIh-0FVNB6cpbN5cYW1wEXicd9W7ie0UWd8_oZqMZrbqX94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعبه‌سیاه پرونده انفجار بندر شهید رجایی
سوالات بی‌پاسخ کارشناسان حمل و نقل و صادرات:
🔹
چرا کسی از محوطه سینا (محل شروع آتش‌سوزی) اسمی نمی‌آورد؟
🔹
همه می‌دانند این محوطه مال کیست!
🔹
بیمه البرز دقیقا چند درصد خسارت ۱۱ هزار کانتینر سوخته را داد؟
🔹
مساله ساده است؛ ماجرا سر پول است/ مدار
ابهامات کامل این پرونده را اینجا ببینید
👇
https://www.aparat.com/v/laibjrj
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/akhbarefori/662786" target="_blank">📅 00:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osv_XmAG5Ol5_Y1QieOwHMBZl4JuNISVOelCYKo1VZ5r9wBWfeOmNIg4Sx7jVu2zouetMEumdIdzml2D9FG-XxgO6XP1BgqOQ-ZwIELUWQGcj9sn179-sikK82qORD00k23wnTFbcWiNHj_NRPXhJhtTmzesLpz9nsEalqOoP1YLNOf4HK3CDFz0Jrg91ndIBcjOHylU-9QlV8TMlF257wS-0DUIbFxmpngewYFI6uUzcX8AqrclcEe30nj9hSNtoAoGErh0DC7jeXxC6dHUMJ1XAfmjtvIBSESmCV9Ub1fGhdbEuaVV-rhcdosA8U1WxsF42y3qI_5TyW-MxgF9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
شب نهم محرم به نیت علمدار انقلاب شهید حاج قاسم سلیمانی
▪️
رحمت الله به عشاقِ ابی‌عبدالله
@Heyate_gharar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/662785" target="_blank">📅 00:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_R_bVKcT1E3V9pDREZC_7LqYToDOhXSYmMc-h3l4sEpwD78dcUHR6mMeLDOtEUNaMtfgTgF8Rjcjqx1jdbmcgVcVFRPGe2Vl891Nh7CKN86bKG8_MO1mo_E5GzaYVwF902uStjWLjK297d0ATvoHgwmW5lq_UlYEHfTI7czNK_lLpx7bPiY_6yMAuFAcQxe4CVlyqf01nK0x_ZCdZgi0lwrlqAYpAnkpGS-abh3B_GvackZXsMmDyHEmQUsjB-90RxZTmo7PmLGPy7atcooZbrQOAzTSGQ8mwk83MEOFopsSRyddEBhoAa5xrcrvasZnEP_ePPWeRunVs5zQUNBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/662784" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f58aa93.mp4?token=Ox8z-z01zMxUuYshSEfV74IDcO7yrd5nF-vly0FWP4v1lTgc8CzGAFEmz8Z14E_CAlM8C_rloLidH9GDQ3RVRz0_VVOphzdu16VtpI_6RrjMp01kFjGKKSoQK1ckr0CLZki1D9BskcCx9BB27Pge5U8Kmglcy3IoW14tyEbnI8Ql8oFnhvenAL-iLRGeJf6HvJD9tNSp837aft3WJDyE48rdnjcT-cv_pIbW8fg2YhgOMiwQ10GxwB4nsl2fHuLLXqVO-KbgrnJorTe9EfNNmBAZotfJJIjzMWqEIR6or7uPHGnJ-jmf0MZ4EtL0rtGPANyNxL1kGUu0uPwVROsDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f58aa93.mp4?token=Ox8z-z01zMxUuYshSEfV74IDcO7yrd5nF-vly0FWP4v1lTgc8CzGAFEmz8Z14E_CAlM8C_rloLidH9GDQ3RVRz0_VVOphzdu16VtpI_6RrjMp01kFjGKKSoQK1ckr0CLZki1D9BskcCx9BB27Pge5U8Kmglcy3IoW14tyEbnI8Ql8oFnhvenAL-iLRGeJf6HvJD9tNSp837aft3WJDyE48rdnjcT-cv_pIbW8fg2YhgOMiwQ10GxwB4nsl2fHuLLXqVO-KbgrnJorTe9EfNNmBAZotfJJIjzMWqEIR6or7uPHGnJ-jmf0MZ4EtL0rtGPANyNxL1kGUu0uPwVROsDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در مراسم درخت‌کاری اسلام‌آباد با واکنش طنز کاربران همراه شد
🔹
بعضی از کاربران با اشاره به پشتکار وی نوشتند که اگر نخست‌وزیر پاکستان مانع نمی‌شد، پزشکیان تمام اسلام‌آباد را بیل می‌زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/akhbarefori/662783" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGgQ3Sbzv1vVuy6eRmWHw9Pc_OX7UqZ6kKmiiTtDllJjQk2zfi4PbYjmA59Vk-Qalukz_PoJf-NJa0MQyvQQtMCARw-K8njDske4tvWs205JT878O9aTAkBUbNtTnwkRK5FT4nWyTRMI2odthYNu8b0hV6MsY4S18Ps_2NEh0YHjC4EkaIP42eIxWUQU0OHaU0zJwbncj5cS_fqAfeDW0Kj4g0YBSrRAoS61UPKc5QXSX4w63o_fpt3mKXMFIkTpD9KPzSCm7LUrmIGhatOw_KziGO6dh_X3seObp2TiuckjlMOGQ8u7vp3PZmJ-5f_QJT-t7qBMK5D1vXxu2kYwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2M23nyPj68Orb9-YDVa4bgvreGB-T6tmHIVDmvHp-XC5DIo8kcjkL_ckqZ8nOzw2eE62POgDwnYV-qDaRud3KqU_8JZN8Jyqj6-96fHcVnWVr2wpz3THwmaCIP_-ofEApcVM4G5JAq_CgIisfwyGcHnMzHqifB7GRHweQQ2ttsMz12h1Zu0Nk7xPic1RPB71gsV2a1qlm1lTAIaL7fK3NYfMAK3WUlEhKQO__IM2lpYdmfxPqP4h9nVUGtH1F1R0DDz7G4NlFbvfV9isInk4oMZMCftmUIzHd7Z0ZN2OARO-5gwSyKQxvH5R8xdA2mk6nw5BYqf3DG8LBJmDrNX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T051qxAQba91ektMTPGdfJq9r3CwZw15FUKVT6ue0XwU1T81m4WVNNHMlllGiiXPLX-x_h-XAdBt_RbOMWvK6pr39L6cvy4scrJD5a4gT4ABCtij3xP9yyT9bI3iXSjcIhlc7vlbz9Pb2ihNOP5f-SLOcbjgi2iuRVe5BuEGXagDMsykqU9b58N2TSjskPTlSJU1XbGZ4rIzjZAUkHwi8IUsY0mLhHFJOIeGEC6Tc2oYzZKNGVUPI_Gzr-NvA0fM3YtdL58dmTS718OgJpRqObAjBtl0exWZk2czEgMLCsI-k3tyMb_Fv4LZqD_hNYd5Uy3PvFdyIKdSFM6YelnMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR4JXnAnfy5cJ0TjPc9xXN9LmFNcPr-xiiIGyvy32_mohzoaFGb3ZOgvSUmcM38APfSP4bbpl5SSoR-dZ_M0gsRw5wRS42Iehm9fKnjSdw3M7SqP1XOmrWl8HhtvKh2DOzVXY2IhUQ3sa3uK31pb0MXrVaKhny0_pM79KOEW2X1dzm669NVmrzwXFo7-I-osqBSpOFRACtH9GGjLJWRkPJXsE9KIn-2M0YUWh77zG4F7w1mmnOzvdvPf11XrT8awd2_I4pZ3YjxiIc3GHCZVmUvfhrGcdW5wW5Dr8gLKdT6FL4Fq9vEQ5LQwfs_vvPw80yNZXMwshDME7jMSdeD6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p48biZcKgqhXp7_ASigKfMMETBi0ZuRfUcr4JSWoBYthgC8_yBKvmzf4TYtmDLIsOf9cHIT13zskDVodbMgJXMWrK2FAkKNCBvfcvBkDJdRA1L99ijTI8fJu-X8uwD-GCj0aR4q6XhZop3m6SvzivmEWl7Kt216hcVkZMNfBgYQOnLZ0hWBip6hJFXQfZTXg0pvhGRU3BrzM51KNtqMSpRdhREBovUyNE4bb0VSCWn87Rp1KbiHS-PoVsYj-w1QyEY6YVRV9kr2xDStOlvN_02vDNRjYOmB2HmrYZFv6Dw2McMeroYvH03qUveinVlQKkFSoEgUfy0HOgV1ejLAHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYSjzuQpxYfq3ZIirMvRGlkIqUqSuRdv7erfx1nKMgXlb-D83UvSo1hgFU3L6Ddl9AR5i-X1DsUxoD7Npm43hv50kHqcTrfNyKZtAMH4HTtKN7vf0fKx9Iv5Mx6Ty_ql-uHc2jLRLBlOF-VshEfSffqUu522vc_X2Y2h1DSII_tWnmfHO7yKFmXS-8D6gGjY4eZTK47VI5keDiigi_Zh2Nr7QZgdE8GFI1znAfhJ-uMlNGSesduylSLbC5_GFYsqU62vH2vQXaz0ehHXz-UCWjLa-FLZnNjb7036oQ1gvwXejzzClWc8caLor9kwdH8_-nlUgNUtqQeBgy3jCWNCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5kKK08Wfs9LYk_dd6itJ935nRf-TDPpXJOYGnDEftp5gENIB59ywz0puWs4FLo_XD1sHA5VgET_ETq3k3xgfjZFXc5km5FDoQr-NRXZhY88YRDtNwWew5Qlny9gxWKY7zqXZ9M9k2dRUJY6cgofKX67GnXGKcZre7aPt7NsZcFF3z4AkF0FK3QhysHy8s8I6mQd3YNDrdXrm92baKUFfyvYHdSE-br6Hb4gb-mCF2OjlfADXr7A7K3RduzVyyGnZkT8HqsvHblb3GxyOUUqShoMiyO3Witazb8xh_tthGeh-Sc8SeeyRxBjPaSeZRLgmt_SG3XidBR0mMXeaW_--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4XgPf8WPfZg-YH6-Hq0_OFBxu8IzpM3EzwepvKZntmmw_3LhYiEHrOadUQKfxMNDYBD_mMgfR1xKbk2xlc5R1syDX7H_jS9gWlGxuLum4-7QmriviR1B5ddYgctOx5WzMC9dx87edg03qHuLbK0J6M3RRF4k71Kz7rvXasb8jne1cG99dHJwdWbwPyjV3JOoAH-qkPjJ4M9kAJ-P_PnUWCZh3vvzLap5wk2UdAcnFB4Ar_js87dC6574SXj1NEADP5PFP625lmpVUNRI7Vu0bJckEO7wCjjjCXd6Yb0fA9ZthwKA8hnSehCo8lU8tPV4bJswwu6CXAqdmYTaQMaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSztffz923kn1zpFrCbPyHurvpy7mDvLr6OiHRsn99zbQShnhkXlDbsv76bOu9y5jTlEdViI3AgOTIKuZqzqcfLkvkHP6eOnr77QdiCLLLHbUJVwoiqyYitNEwh6pTEzglFK_YhRyTEom5b1uM6DhNbV8DhP_JSRM9Chkk-KUMnjkJqoozUcxO8oK7Ob6G1HPo2mvJXhwVD9nKP6THUm1997baCyosTDeODhZp-3_bnr73vNM4NzIadFq2hCTRxMjEXm9PN_vJjM3wFTNukfZAOHn2WuNSJNY61lUvsZiPjYqreHqX7cJz_1sJGNBY5x2-hOA8bqOXu99nuymshfNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
آنچه این روزها ادامه دارد، روایت دل‌هایی‌ست که با
#همدلی
، مسیر خدمت را در
#هیات_قرار
زنده نگه داشته‌اند.
💫
به برکت همراهی شما عزیزان، این راه هر روز با امیدی تازه ادامه پیدا می‌کند و خیری که رقم می‌خورد، حاصل حضور دل‌های بزرگی‌ست که بی‌نام و نشان، همراه این مسیرند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/662774" target="_blank">📅 23:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/662773" target="_blank">📅 23:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
خودکشی دوومیدانی کار ایرانی متهم به تجاوز در زندان کره جنوبی
🔹
گویا یکی از دوومیدانی کاران ایران که در شهر گومی کره جنوبی در بازداشت به سر می برد دست به خودکشی زده که البته این خودکشی نافرجام بوده است.
🔹
«م.ک» یکی از متهمین پرونده تجاوز دوومیدانی کاران تیم…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/662772" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/662771" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e18c61de.mp4?token=SucIe1qyY0N3sxLBYqlwXNSusdyWkv3Ja9sWSjket6OU1I9XMuB-caXwWxradvM6eKsnye4f5Rq0BYfpgo5VBh4Rv29QrIP7va0SluHt0Ie_pFiGG-d61TkO1ELiuiF73-Od-G7-XcuCSLdDo18eERbEr9Slfd2-KCLFInm2s9BEqdQMdVL-TE7ajRQ5KFpeNQJ-KUsHZFm5NLWH4_jQtKqjU-ZAB8p2nKV4aXxfc7FvcBI97AsWk-d43JJcC0FzBbSZ-BTY45TjiBFFBEcdALbz4iqXirHSRkh-I218UBOyczg73YsNC-jQw4ZEkr6aXLionawtU7mQtteHeNxCiEeJGdNXQa0BAD9iAIM7v-RkzWWVcq_DrYnQZvGpkM09e_zM4ptWGbFApRFjaG38UPdu6GY3UKZZTPl7kOhIoT3mxKgXp8pxDsgxavnvxrhBMh8uMN08WTY19PI-4GGOvmRXG1GPJERDpGRQl54zWK63GVPl3z2JtY9izJBeCqOebbmy5a0G3RYn_jZXtjNV9cAd52HyyTH8rG_VmEFi_NYylEZ4pOwCKmm9CNJRPu1F7pvexth9PeWm6oK7nLFibYwuRz2mri1IV9AJ4NuVZl4oANTqe_we265eZCMer8tweKO38zx6mE3As7SQotoVdTbXZ8g0ZzyHP1KZxSJ2V4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e18c61de.mp4?token=SucIe1qyY0N3sxLBYqlwXNSusdyWkv3Ja9sWSjket6OU1I9XMuB-caXwWxradvM6eKsnye4f5Rq0BYfpgo5VBh4Rv29QrIP7va0SluHt0Ie_pFiGG-d61TkO1ELiuiF73-Od-G7-XcuCSLdDo18eERbEr9Slfd2-KCLFInm2s9BEqdQMdVL-TE7ajRQ5KFpeNQJ-KUsHZFm5NLWH4_jQtKqjU-ZAB8p2nKV4aXxfc7FvcBI97AsWk-d43JJcC0FzBbSZ-BTY45TjiBFFBEcdALbz4iqXirHSRkh-I218UBOyczg73YsNC-jQw4ZEkr6aXLionawtU7mQtteHeNxCiEeJGdNXQa0BAD9iAIM7v-RkzWWVcq_DrYnQZvGpkM09e_zM4ptWGbFApRFjaG38UPdu6GY3UKZZTPl7kOhIoT3mxKgXp8pxDsgxavnvxrhBMh8uMN08WTY19PI-4GGOvmRXG1GPJERDpGRQl54zWK63GVPl3z2JtY9izJBeCqOebbmy5a0G3RYn_jZXtjNV9cAd52HyyTH8rG_VmEFi_NYylEZ4pOwCKmm9CNJRPu1F7pvexth9PeWm6oK7nLFibYwuRz2mri1IV9AJ4NuVZl4oANTqe_we265eZCMer8tweKO38zx6mE3As7SQotoVdTbXZ8g0ZzyHP1KZxSJ2V4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا جلائی‌پور، فعال اصلاح‌طلب در برنامه «وضعیت»: بیش از ۵۰ درصد جامعه با تجمعات خیابانی همدلی می‌کنند؛ قدرت موشکی، شبکه‌های بسیج و هیئت، هم‌پیمانان منطقه‌ای و ساختار چندلایه حاکمیت باعث شد ایران از این گردنه عبور کند و در برابر دو قدرت اتمی بایستد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/662770" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رفع کامل اختلال کارت‌های بانک تجارت از ساعت ۲۰ امشب  شرکت خدمات انفورماتیک:
🔹
ظهر امروز، اختلالی در شبکه کارت‌های بانک تجارت، ملی و صادرات رخ داد که باعث  قطعی خدمات خودپردازها، پایانه‌های فروش و اپلیکیشن‌های موبایل این بانک‌ها شد.
🔹
اکنون عملیات مربوط به…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/662769" target="_blank">📅 23:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6bwI_kQfZyI-LUFBvsQl2_WPKUkHHvQ-kwXVD4Evy9W3AxbAuUPPMILxawgmgZYdrqDPCvLlOSUvsdEOHOj2n5T5YeobFpisq7rAKvcjDMWHuueQ2e4KixkT7WWz-juoPw0PXPZ0LbQJT3Aj_ac8sqo2eldrKEuJsODia--PZAnPRjiGoLdkBpYaz5fepehnWxowDLVmKeceQp9OffcypBiUv7KPSGvCuq487G7wXsZbHfVGBVO1VXTjIfwYU0Yvj1DaljdmCBJc9zqtSs05ESw-B5t5MP9cfxwM29iZu0ygbjd2Vosoospc4OlV4rM1KO1PqO-6abyy0Id26kYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسعود شریف
🔹
در ادامه تحرکات دیپلماتیک تهران پس از نهایی شدن تفاهم‌نامه اخیر، ‌مسعود پزشکیان با همراهی اسکورت هوایی ارتش پاکستان وارد اسلام‌آباد شد و در نخستین برنامه سفر خود با نخست‌وزیر این کشور، شهباز شریف دیدار کرد. همزمان، وزیر امور خارجه نیز وارد پایتخت پاکستان شد. پزشکیان هدف این سفر را قدردانی از نقش اسلام‌آباد در پیشبرد تفاهم‌نامه و پیگیری اجرای کامل تعهدات در راستای حقوق ملت ایران، تقویت صلح و کاهش تنش‌های منطقه‌ای عنوان کرد.
🔹
هفتصدوهشتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/662768" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ما می‌توانیم کارذرا در ایران در یک هفته تمام کنیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/662767" target="_blank">📅 23:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTYY4ArfIFiQvqc_pcRPrkzXq3xeXHjfe4OcfLqEgWDMBO9Azsmo7TdLWUwWJgso7HQ2m3XtoQHnpN5qC7503Oxv8BmBM_ZYKR3vEmR78Kxvi4tDEB69RXQts1UeLd2Ig7wZOy1_cVWO-CEgSpPODm0fsRMC592SP6yEz4iKH3JJFnzfAIyWKyXMy2ZHs9SM6EzOCaH5MHbyuDIZuMwx2wKp3uBwlciQluW3iYlqQgV4ztX_rCW5aoL8c46aKgoAwCR_MDtRMoR2G95zYAkX9DjqZF09U-ZIdc6qv3oA8PvO2-tl60kOXB3u1rPvjCnYxRXAxT8OygUUcps6lqo17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/662766" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f776ff7918.mp4?token=cKTTLvrpCT9ky7CMcBjROm063KUImbW9m7hKZWfHDSwJ-lMubwSAxRywi8tCnMv9ho4NWdnBM19J2FqUL3lqIDkN69NWPX95UoM8weoRJIIYdSFGF5a3lXLnF-IKi2fcniiWZDrjxRclw5MCOh6eNR7-ztBjzXWlObrE1_qCvT_ZrBFHKn-15nuPPWzbf965_iqIrLWpOKFcIRWfMo5brDkW5IUaJWbQdzo9JaF9DD1DtLqyQAXdG8QVfX1HicYNpRBmpvIz3Ezopw1HRnNCW_pZV8ndL9m7uxvAZ1wpwkpy8TJqWpzOIMEKPp_31aIDIv_CX4Jk8p7Wi8CTpLhu5Jlbby6YnqrfgOpesDH1DgP9mdBudd9TkTsXIH-Y3XFuzNDg9j1-7qDxQHMwvm8J1dwrjNu5OpFAtqGiION6xrvu-wNV1fW-aPmKXL-0UaZw31XAiiCzT373VZUV7AtK11Xt0rTmJ_Va2qLdsCUvgtFtI2545Ppi2zXSFK9kUrJXtEkJhVMBh0fCBsuFIncSDsC1qRrRgxsYl-NdaoFbfLe4sMHzcndDH6dMolUwdFxVq2Am22JUvBdRPR8cUWLgWw3QD7ORZR6vkLDuFEURe9ZOPfxnQ5K9By4jq3COmtKKC-rSgkpHGhT5-5TwOOYK-mpIOgHJmy8S4RSL5fS9gY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f776ff7918.mp4?token=cKTTLvrpCT9ky7CMcBjROm063KUImbW9m7hKZWfHDSwJ-lMubwSAxRywi8tCnMv9ho4NWdnBM19J2FqUL3lqIDkN69NWPX95UoM8weoRJIIYdSFGF5a3lXLnF-IKi2fcniiWZDrjxRclw5MCOh6eNR7-ztBjzXWlObrE1_qCvT_ZrBFHKn-15nuPPWzbf965_iqIrLWpOKFcIRWfMo5brDkW5IUaJWbQdzo9JaF9DD1DtLqyQAXdG8QVfX1HicYNpRBmpvIz3Ezopw1HRnNCW_pZV8ndL9m7uxvAZ1wpwkpy8TJqWpzOIMEKPp_31aIDIv_CX4Jk8p7Wi8CTpLhu5Jlbby6YnqrfgOpesDH1DgP9mdBudd9TkTsXIH-Y3XFuzNDg9j1-7qDxQHMwvm8J1dwrjNu5OpFAtqGiION6xrvu-wNV1fW-aPmKXL-0UaZw31XAiiCzT373VZUV7AtK11Xt0rTmJ_Va2qLdsCUvgtFtI2545Ppi2zXSFK9kUrJXtEkJhVMBh0fCBsuFIncSDsC1qRrRgxsYl-NdaoFbfLe4sMHzcndDH6dMolUwdFxVq2Am22JUvBdRPR8cUWLgWw3QD7ORZR6vkLDuFEURe9ZOPfxnQ5K9By4jq3COmtKKC-rSgkpHGhT5-5TwOOYK-mpIOgHJmy8S4RSL5fS9gY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی رسولی: ائمه جمعه، نمایندگان رهبری و ذاکران پرچم خون‌خواهی را بلند کنند
🔹
امام‌جمعه‌ها، نمایندگان رهبری، علما، پیرغلامان و ذاکران سراسر کشور؛ روز عاشورا باید پرچم «یالثارات‌الحسین» و «یالثارات‌الامام» را بلند کنید.
🔹
این فقط یک نماد نیست؛ فریاد خون‌خواهی است.این پرچم باید از هر شهر و روستا تا تشییع شهید، تا اربعین و بعد از آن در گلزار شهدا دست‌به‌دست بگردد و بالا بماند؛
تا وعده انتقام نهایی محقق شود و بساط جریان طاغوتی از ریشه برچیده شود.
#خونخواهی
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/662765" target="_blank">📅 23:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fa8a31e0.mp4?token=mSwTdv0stC9FlOwoEWLrnOhNFmF0VsCnyPRvSkT5xmOfr6C1dtTpb0X4-itzwXHBMqcssslr0fXHZyAwsNRlTzDLXnuHD4PvW4zJKMzDrVtJO7G5AvRRbn_fgI3Q1SMcRo9TMJIeoQNBOVh4wgmAjzEFSltfMZiL728_sTXxBhze9WC35fHcqmjZsznvr12D2Dgnbrf8mAqKO-GiffWlu5WqBz52UEnhASqO1KjHWiSfEPHZ32Eq97tu2cle1fjKJorxMfxOwVPx7MFKs5DToW4VCgtQBfY4KaDaBZWQsXIplRm8BEggUe4fbB-aeTbmvFx3I2u1ecsVMgt_9vSCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fa8a31e0.mp4?token=mSwTdv0stC9FlOwoEWLrnOhNFmF0VsCnyPRvSkT5xmOfr6C1dtTpb0X4-itzwXHBMqcssslr0fXHZyAwsNRlTzDLXnuHD4PvW4zJKMzDrVtJO7G5AvRRbn_fgI3Q1SMcRo9TMJIeoQNBOVh4wgmAjzEFSltfMZiL728_sTXxBhze9WC35fHcqmjZsznvr12D2Dgnbrf8mAqKO-GiffWlu5WqBz52UEnhASqO1KjHWiSfEPHZ32Eq97tu2cle1fjKJorxMfxOwVPx7MFKs5DToW4VCgtQBfY4KaDaBZWQsXIplRm8BEggUe4fbB-aeTbmvFx3I2u1ecsVMgt_9vSCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات عجیب و غریب رئیس دولت تروریستی آمریکا در حین سخنرانی امشب خود  #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/662764" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr95p9vZ6MzQtqE0jnNt30WUyi_2ZyS2qHJKsCqcUtAzSjXiM6eAEOeQpbfjLoEuXF7JSj2Rj-uVmRH_1G1oKjTjGrJXUJgfIMDZ8E3vmfTlc2bBzTgWVlU5ob1c7sKTu1Vb6nTbmkojJ6Fq2dsk7mRXoM50-e-HV6eqQq1TkmAG2kwfqXn0AI9YkXFDyKrVuv62Nl6cThKVooWI0ZY07EqX4lXMu2ZSDk_ICLTmoUX4qztb7Rh5I8Cuxammre_FWFFPUcpXtWtvAiURkYEC_wD4JtqF4rFIPl9Btae7hwZz5GVCvj1UK6TvbBeea8vo_JrAXIGh7K45_h06x-kdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سربازان آمریکایی در حال پیدا کردن سلاح‌های کشتار جمعی در آشپزخانه زنان عراقی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/662763" target="_blank">📅 23:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-J1oT9yb-SKt30o_155qasl_CqRLLTVFBBbLliCiR0wgitJaIKkKdh1MS_pKWp9AKPQcWcUOb1oEI5d1lKeUWOU6ffMJesoqrCh2NNfnILQDGHv5scH9EE53HAsMrIIdBBMNX-L0GZbyBa2UwErKXGgJefQh102vvFFW8gvg0xQlZmoIbdMuYkvE46McZq-0vNqEF8Ee_dTuyocwyiBHUooOxyegBwI3CmKtxq2p-bN6n5aO31elFdLqNQW4ftnC2pIlWwbq2lNuVIgeRt-3_b5JnIxAUc0MMXjX8daaXAbpLHAYDR4u2vW2io3MPM7YTabPBesRUbytq4qJYBldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کجا قسطی بخریم میصرفه؟
بعد این پست دیگه حواست به خرید قسطیت جمع باشه!
❌
دیجی‌پی با ۸ درصد کارمزد، تنها شرکتی هست که روی اقساطش کارمزد میگیره.
یعنی اگر ۱۰ میلیون تومن خرید کنی باید ۸۰۰ هزار تومن کارمزد بدی به دیجی‌پی.
✅
تارا و اسنپ‌پی و ازکی‌وام هیچ کارمزدی ندارن.
یعنی برای ۱۰ میلیون تومن خرید، صفر تومن کارمزد پرداخت می‌کنی.
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/662762" target="_blank">📅 23:04 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
