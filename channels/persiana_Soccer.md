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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 20:46:10</div>
<hr>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ld94ilESsDqG4MfwlMjKWkRyFdR4Io3mxHVnX0E482NuEqIu7rZWmB7WG9uouvBNywXCOkQraqMmW6Q28-DYwyyqh6-tQH142stsrsAdYriTo5qoDjmzy25Ajk58oXvHmLcqob4eGWxXO6rRjXfEGUWBQ4uvmv7meVCpeXgz3_t55hBWqG2ArPR9TYD3xBJlDV62SHBWVubDpNsxi0WVh5bAqbVpkl1ekYXdyW8Mz3gK-TgM4OiM3DszfZoFjnSyFb2WdGbUrfvDiOUWZcAd-FiF0vzL5VFfnfKyK9Famea5qmdGAEUnrIbW-ohiIUCwfRKO3cpaMaZRnp_uFnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJUwjSWx7IxA64IMU_-N05J-3WFsKAS1TCwtxnPTATNtkyxXTECbxiPu-xtTCwa58hreidLMS1FhabYYp78hbVOMRolUvZX_4u3YhIvk8WA_HXsQWvk4tSfPA_KCc-ER72h_nFWAYSxlJ_5zcDgz6jEsNCYTrCSlBdAHaJVo5sMSlO2xi11ba6fnp-kIolx1-vATR8hf_sqo8I6qFAW3C2RRJnXuYUzq5wt0LyQa_WxjG_7T9BlxcgAI2vP9tCDBV3Hjvp70KDOVkJ6fKrV1leP61ObPh_llwQRhd5b3CYxxgHZH-WRIS9CBVUbMGpXdMud-1ISV7G3sxuIiC6ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QskX52oZLzwBnYf65er7ITRZBm4ZP3-m8ZkWR127g81tmE_DxN8fstunF8Y8UIah8PRzSF52AJwKmov-8VO-UTWybxv2kuoe9aF5-L_3K8FZ022NSHYlaUgLk6bJ0ynO2eXxAoPaUZmk9WeXu_oncpfO-yfubeON0FJPTT_BKYSe0ZegADF0D4dPFDPKhVrgdu-8A6AGYcOMtIgsa9rqbsLAxGz8AOwcmw5hZNOvP_Zb7Q7d3xpVy7EMz6vrM5PCHlNDX_86KiPCTV7pQqKVHTol6fYbriUKJDDHxHBViYV5n21SWBXdeonZFyZseJSJe49KL_fyx0fOrxzz68H2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5dTVJCvZHElUxFH-amsOktiPrCmUDkM0N4KuhH78INZtR2LuYD4NBoQeyNDr4cLKS7GyZcevtthYQ-tX6KykeJGV671mKY1gkiW98_kZIZM3U0Csnry3J7ALTxxcK5jVk63Ut1rLhx7XQx2DjZbAl3KqpyGZJ3ezdp7yhdNBoMmN3NhFBo4WUPbSZ82tb9-5K05EekxSQdfMJrtKsziKpj6DzaxP3EJalS88zHvcTI9h2FR8sEuh5rDjeWva8PV6rWG3bIROnvu6rRzBSNICQHnoNXgrOKLu6M_rdtmaW3tOw5w7nopPmA6e_-w2EUCfDsYvdLyiAw1yjxn6Q1Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5CYQ2Ah1cvGlApHvOAxLDOxQUnXYidYJOwuGKrDWsTNnlRBc3yOlf-D_WLYwgO_U8P-VdJem9UFU2lXEVfpPbKdmg9XLxZA4Jt70K87JUJH6xcPmk4FKo5ubTUYvbrBMPtcmH1iKPhXWu0_Ixr8qtvQbFLC2WX6JQeRAGFoT4fxyDtMVeEGp-UrU5ie0H9yQgAhlGqRPFSA33E9E4Tywt6cwG99XhHgjd1s_eZsDuHmo9o69GgdLh7aH2t72LjJwnF9-MMfKOOkLHzUVsbs-b7dtJvSnkcR78E0mj0gcvjimflQSM2AV_uYExdx5sUhfIw5KIUHzSskssMsmnYwAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQxyqEJnaXwlmg5b4XIW1h9FZPeNgVz7vh3YY7cax1Y-wQOILvlnuEEPVjx2RYPedAFr3hrrjYmRguSf9_JZpaawgo6_OAqN4zObFHAJHBjyo8tTD88_oaauA-W2Gbgsh-MNygFx4RNP8XGj3lXaJFW1YR2510SZWcGujRpFOxex4_nhaY2kIWNsvynlSOcwhBIKi_ERop9gV-GImm2T7c7jf-FNv2QW9bcPhyW-C7BfwKZuAxbCK2eNlxy755upwePZL6n0ZcqhUedEnhKFqplUN1-ZMD8m8LxGHjVCrXsPNZ6heVC27yaQ8xN75ANSWmioUR2nDHt9Dl2sOa5z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rHX3nvG68S5NS2Ahi0ZFv1kPZ1OrBuZ0ESiRo7oyQesuQxqrc1N0Ybh-KAR7nRYWot2IDKAuvoJjBmnhHLv5qOTP119ky_AuZdtYyc9oFIvIbbo3--FlFdh6NgRsUyJ0jZxNAqtOiovLRqGPEAdwTTO1M8rbAlH08SyqTvNg4yaxqQYdGrGoCAowBnXpAGD3rHaJDx15oVmRl67j2yYhKa5x5E8RyY1XMRYrdMJjPb2On8uOQ9KO9T2WpvJwf-11jkxnge-sHuxDQXcaSGjneydYADFUoqZAPlcpBEDoL3G6Q48Q3whWdfVsupKaQYvB9bRMYxrCsn_kEJDcHsXx_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rHX3nvG68S5NS2Ahi0ZFv1kPZ1OrBuZ0ESiRo7oyQesuQxqrc1N0Ybh-KAR7nRYWot2IDKAuvoJjBmnhHLv5qOTP119ky_AuZdtYyc9oFIvIbbo3--FlFdh6NgRsUyJ0jZxNAqtOiovLRqGPEAdwTTO1M8rbAlH08SyqTvNg4yaxqQYdGrGoCAowBnXpAGD3rHaJDx15oVmRl67j2yYhKa5x5E8RyY1XMRYrdMJjPb2On8uOQ9KO9T2WpvJwf-11jkxnge-sHuxDQXcaSGjneydYADFUoqZAPlcpBEDoL3G6Q48Q3whWdfVsupKaQYvB9bRMYxrCsn_kEJDcHsXx_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=All9aPiTTvhqt9ulpH8ZLdrAHSmGgd6tpRMD0i_khdzRq8h7iv_2HOXIs7kEoF8EEJDktjJUFRA0h6apZKzVZ0ctKDz037k07FwurasOQ4DVwd13rRMDiPv6GK9tGfq6Dii3OdNtLVLYTlqmNoi4LlVZnpFlvzzxfeSCXtiCFKfwuMG9EvsuO9c5dj8PSAloDx2kiFjny-siJ-VI0_Js5L-bK-DdP-2GnKbyLf3ANWPTz1ySJ5dX8VtJ6uwzFHvxchoM02dw2TVQfnC1ossU1yORy10YIE_hNa5KdwfsFMr1wCbqVKq2DUrU8wkCeGK5YHG7kUpjCwG_UhX0VJXMsaEGgXtWC4apEModhuv56A6-uSWIfKd1DgKHl3p1zPBO62tILr90NaurZng5hSK03BYeirjcjp-6bn7cwLEHhRCuj6YSmbnOurZ7HrfHeEMphfzNBteitcg6SmtKFri-zPCS6DzM63ElasnW3M6ZFUFuuGYcx7-4DyevM8vUeTedVVEx6t0RE3985glS2g3RmEDzGFRh59M7ZJTmzLkckv2r_pOuHqTsLWIo-gGPcJZuHEqEMtwUY-K2rhrOZW9h8z8XBTkKVlEyY_dCxoNLw3qTxn5yc5GXq-o6Sab6N-rQbEEgBhWWfeGTvLA4JErCJa2b6JMawcoBIfoW_rWmcnk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=All9aPiTTvhqt9ulpH8ZLdrAHSmGgd6tpRMD0i_khdzRq8h7iv_2HOXIs7kEoF8EEJDktjJUFRA0h6apZKzVZ0ctKDz037k07FwurasOQ4DVwd13rRMDiPv6GK9tGfq6Dii3OdNtLVLYTlqmNoi4LlVZnpFlvzzxfeSCXtiCFKfwuMG9EvsuO9c5dj8PSAloDx2kiFjny-siJ-VI0_Js5L-bK-DdP-2GnKbyLf3ANWPTz1ySJ5dX8VtJ6uwzFHvxchoM02dw2TVQfnC1ossU1yORy10YIE_hNa5KdwfsFMr1wCbqVKq2DUrU8wkCeGK5YHG7kUpjCwG_UhX0VJXMsaEGgXtWC4apEModhuv56A6-uSWIfKd1DgKHl3p1zPBO62tILr90NaurZng5hSK03BYeirjcjp-6bn7cwLEHhRCuj6YSmbnOurZ7HrfHeEMphfzNBteitcg6SmtKFri-zPCS6DzM63ElasnW3M6ZFUFuuGYcx7-4DyevM8vUeTedVVEx6t0RE3985glS2g3RmEDzGFRh59M7ZJTmzLkckv2r_pOuHqTsLWIo-gGPcJZuHEqEMtwUY-K2rhrOZW9h8z8XBTkKVlEyY_dCxoNLw3qTxn5yc5GXq-o6Sab6N-rQbEEgBhWWfeGTvLA4JErCJa2b6JMawcoBIfoW_rWmcnk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtEok3H_h87S6TLceP8M3iZ6uVkUQ0zgS7N97mtqFugiz1nIP9N5t_Q_QZQSJJDOZNyQwQrX5Tmnx3tDOfDMwTJSCk43qK2TkXlT75vkVGIBCH3oW-JT2PRcPauqvA0h164mxlS4u9RLMl7aaDks4mCaPaU5XVAHAn1X5wNvwPG2SkC6Rr7yaFia8aUicS9JTTfHFdJdM9aFPZweRuE5toDaXYzB3ZcR3r0XBgqQoAYrSfEb96n3Y1XnpuoDFm496gmqrdgUtyIrLqyPuAuwyaMvcK_dDle24-drUDVgjy60Z3Mrnro5TWJK0iexl4kcZmJOlJdZyGr77CF03CeWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao3K9KhUYjnqdA9BGT6mu7mz6rI18UJF--vnvyC2b0nqgKpkEPxgOtCxwZjVLl9HpR5E69SeQ-Y7f17RnsV751gLtYlcLVTi_Bm5hcVWiTFiI2UHbqtI8g3Oy34E2v492Crt47QyT164rQoXmZ4NgkEhNl2HlMgVCR3nlrPEAjF3nmWGiO5vbimN9e_3qAIib7HRVzGrFuywFoMminZaPNJ_RhdxelDR1E-wIq2RJ_oF3B5gr-WeAzUXAq-G4Y1eQ5_C0GV3iwkGDXmhISRrp6Rzo5i9P-fPthW-AYE7ztGpbL6e78rjS0UWVwqLhHU-XOFLUX4ovUg4Ynpv9ifsyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTa4l_RzdNgUhJuiXC3xjX4oI8Op__X7FYH9xbCUa_7op3qoRNnRg4Elf0tSENo7a_aNuhRq3T2cjS8-1eSTZzj2r0Vy4ZEtckuFfCEgGfK5J1m3GuyIZWGkCr_QvD4jEQWF-QcmYLtz3Ms5a0pkEXzf9nE_Gsk7Tq6pRvsmGO0208q6MI7Wa-iOclMowPwOzmfN6Frz7XW1aDO7UM-0aGEs_QpewYxsvaRtarHFxN02kf8bOClqHX60V4d3PjtIfIf6bxSpjhmbHxBn21cWTNIOZ1mFKQyIRtvVgJ9tf-JA__SAc524jnv5RuuJXACpKo6C5rZulvpqDgziH5CJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUvd1YkmsNMYyG1gAU0-akFmp7lFBgnNtH6tmyxUMeevZb5HgY_Z3hMHNyOrq9_OoU73eqIZg_rjxmrc20V2dG9fDk7eZSR__mdr6BPdP-fwZFmMLWsAtwR9ziqU7Lp8oOEvGWX5NGWOQziKVEq4uhLjLt3MoA9B_JMC6Muw6XXvjyzqJwVK8LxbXoee20mQoJwmW3k82nOEZmAfcyVInF_9h53Bzj7buIDPEpQzHwN99WeASs7Ot3gc5ya-SlzO8kcPl2aXQmXNY5qu3Z5KMpiC4Bq1sByrfyHv0Xe1zvR2uZebLOK_qatvKv-27ZZaYduux7HIwxsEsYR-Q0UdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkQFxXpdgm8p2KHA4Ez_wwQisu7Gx-DlIm29G8ztAgAojOOesWcp8SvJeKdSkQ2XeVQseiQptpx22U0GX4jlpzNA_l8WJo8cHLGWQCtkgYg4off-ILCiKDQEPPDjFjZkY2U2LRMouMS4uH3fzPxT2GWEUPHSy9tfhvFOwVY6jW4gG5zhA7ey76l4wVgHlWP6YiIFxqS2GjeckEvQHVuV-nqv5XzxUkaYECkd20CDdfY-REERMwDYDpzsJizUj7nDWgjaEZ7CQzUJR7Nd7GZHFO7vfVKnVOSpKVjT1JZ3oDZrbiZUDncCNE_vpMegcKbWkOqROOo1gW-FxvjGGpVMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzCrH20OniVMAldyO1ty3vbxthdtYHGmUCax63JR-9MCP2xHB41qveLETjDDf9mDk4t9EcstOk6fsvGmVzL-lEIRIS5dAjm6vX-gCpdUHJg6ixUvSQpbO9dl3JBsGdl1WagDGjKJ-S5TFy8jeqAZhXQrIoxNSPWaj9MTS5xAVa6EFpNQ6eQ7bjiRBvqLCbES_3PaTWQeySBzS4BSeUsTY3tYZkBINZEFAoUdsqnuK4EMr9nPDSoE583Ek6CT8557CRq38-p_PCbSo5t4HE6OVGIJAO_hKdxAxo7GntP01-7FaNbIQdTHSi79aDgUo6DqxTsBkY0C2WfBT5DKESC8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=rG8-Os1ydVZu2cjd9fOiE5uu6ctbsuc4HbcSwbYQNZ2cMkomMlL4yVIaa3uiy5RjYw-NaS_XmT9DjmRkSHBnDxrSzvJL2cu3SUwTK3ACUkPRrzXYlfA3m1GAz-GYSrEie29yObbSXAZo0L4tQl9zqNIHF3Bmy4qX97Hqb_iExjAkq6ZaP1W9aWpSYnw_CEF0K76RJKEzJ_3XQbopNBn5cWgndEYT8kCpSL2d3swQHUcL44rjwX8y-KwpLyFFiU9K0BeDmExNXPmbqHjmiSHiKar_-NdCq0G2wwxDfZSiHNAuoqqbHfEQuetTye9PsGry4t--B_23XIyB1BEznOkr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=rG8-Os1ydVZu2cjd9fOiE5uu6ctbsuc4HbcSwbYQNZ2cMkomMlL4yVIaa3uiy5RjYw-NaS_XmT9DjmRkSHBnDxrSzvJL2cu3SUwTK3ACUkPRrzXYlfA3m1GAz-GYSrEie29yObbSXAZo0L4tQl9zqNIHF3Bmy4qX97Hqb_iExjAkq6ZaP1W9aWpSYnw_CEF0K76RJKEzJ_3XQbopNBn5cWgndEYT8kCpSL2d3swQHUcL44rjwX8y-KwpLyFFiU9K0BeDmExNXPmbqHjmiSHiKar_-NdCq0G2wwxDfZSiHNAuoqqbHfEQuetTye9PsGry4t--B_23XIyB1BEznOkr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=MT71bx6lCbR71wmOLBLnG7kd29Pl5SMyP9QH0Srzb6P4jWXI4ylG_ilB7K9SK5koP_SaKEQfkiaoo2LI6W3Z4CzZe5wRuhzEM_8uytzl_EYevwqXJ1rg52KQHfhSbYFYr5Uo_0JVpySlkuczotIubea4mgHiVqBk5xL3qiablod6M5ybGbxP6JJQta6nwIBRMq412gAOioXQ39MMmyNaCP4tu1F1ztqo8etjJXkNe6BV8gysKI9PA2VOaB6V_udmYPIDXhaN7Ng__CQ2GlfetCYA5JM7jAoyVCeFaIR4K-sXCs3gYDx3vr051OP0cMsrLGlbqIRf6DQqXH-F0nE6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=MT71bx6lCbR71wmOLBLnG7kd29Pl5SMyP9QH0Srzb6P4jWXI4ylG_ilB7K9SK5koP_SaKEQfkiaoo2LI6W3Z4CzZe5wRuhzEM_8uytzl_EYevwqXJ1rg52KQHfhSbYFYr5Uo_0JVpySlkuczotIubea4mgHiVqBk5xL3qiablod6M5ybGbxP6JJQta6nwIBRMq412gAOioXQ39MMmyNaCP4tu1F1ztqo8etjJXkNe6BV8gysKI9PA2VOaB6V_udmYPIDXhaN7Ng__CQ2GlfetCYA5JM7jAoyVCeFaIR4K-sXCs3gYDx3vr051OP0cMsrLGlbqIRf6DQqXH-F0nE6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKdCvr6Zo8XLq_QhJ4GhzwIcgPeor6KFjuOX5HRGCnH9K8JXh__DbfDu-r0EuJ4W-GKRjRPkHeM7KIZjYeRHpxy12PPOVSkhN7-piWbgzc4-drU6ve2vJycUlzLEo5ySjdQJmkS_4VpdhhgSaNyTlr0Eblg4tqYqHuMxKILWbOmK7XS3TtedC1UWfMfhQ2GVh_rr3mMUmGxn83lj98NNFt7s5h8DszkO6SvvQl2od4RYmH92H-WQlC2GtOzM9koCxLddndX-LcdAHTiJy41rju5Fw0oCyZkiXrY8UU3KtVlIFutRvFlJO9czbv-LWjd-gQJ0J1L6QvGNP75TkO8uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQM7OdeEuq9rpS04ERezFc9Se_sTMLTqIjz6YQdYRaT694N78MPmH_cTnVtbVduQQDOFs4baaa9ZWkMmhmKQZbzi6atjsK7AmtOEPw8CgiM52qIBuQB4pFbxnZ8gyES0ZlgWyhg4vD1aVhZnQUvF_Oj0FsQxW-zyFFREHXHHUxgXU8uIWNwA-lMkATFawj6ESmjQlZqFzi4IQSHgiCsszuLG3Z_xSRlRzg3SRI9g-ZBd4HdFSY2Fgqf5lDr-f4Vi79c0XOGGAcX6huMj0NDq5AVv_86qyKJtIdWi3EERK8vXCUDi0W-aDR3EfHqDVOnkQFB0M6ANXaXgVfqK9Xf4ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=uRdp6W8W7z2kSOeQ3gioLuVxtwl4N2J1ja2XKYVG5dX1eXyBoZkRC8nMVZdpHWySowZ9ajh_YsnhVjAdYjb09EqcB77FMfjDJ3xPK17gRLhLwY14VUbOn2Bv-O8fTJX3Lm-7KDOMmWf433dndu1_pQxHkUOK3PnyiQ4bkQuESx3p3lU0LCugNTHDhuVjHMhVBf-GX0sSxvzrCl-pNgsX4Ko79Jho-XbiX6lm28zZgPUzHvRPj9TwdtSgfTUgBTB7mSTzQewZelN6U6pCXEhz7DITtQKHNDNcuoY-QW9aBcuJ_30OCbmtVNZOvo6h6t2wdB-j6pOcMpZx7_y1njJ8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=uRdp6W8W7z2kSOeQ3gioLuVxtwl4N2J1ja2XKYVG5dX1eXyBoZkRC8nMVZdpHWySowZ9ajh_YsnhVjAdYjb09EqcB77FMfjDJ3xPK17gRLhLwY14VUbOn2Bv-O8fTJX3Lm-7KDOMmWf433dndu1_pQxHkUOK3PnyiQ4bkQuESx3p3lU0LCugNTHDhuVjHMhVBf-GX0sSxvzrCl-pNgsX4Ko79Jho-XbiX6lm28zZgPUzHvRPj9TwdtSgfTUgBTB7mSTzQewZelN6U6pCXEhz7DITtQKHNDNcuoY-QW9aBcuJ_30OCbmtVNZOvo6h6t2wdB-j6pOcMpZx7_y1njJ8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT-lLlLt5T-CKvi_mEClyJ3T_AnztRt48BruCtx2kENJqR4nIlJv_a9Nqn2jTvtxGS_JoGvDzLJHXDwOs68_lp_ptJERe0Bf_phtnUm-LwwQGGt8qeIX4ZfnvbXdhWMv-ztB8waR952jPNeniqHEdL0oYKS5WIfKxoKj7X3dbJlbCHYVzFfQfBMF5cmO0x47KCMlYza7hisel35i-pJU8uVMnSJmdkCi3vwIDrfzhkVwcOcE5cMJAnwgVh0QWzq5naJvN0IB-_tAb0gY0m95ZPE6TvlRGWzH4pMaBD7-PNSpzaBDtSrQKnp2OUC0UsyV7AMqz3MSmxXsMSAWdnwTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2_CioAzRVPZFk7tuiH2l1qOG4-rmouqxTbzKQBcLhCdSgx4FuHe9s33ohNetxNGKTpNKtRagQY2AHqRhVgCyb-G-wLuNImlbLfTF2OAXTSc5THQFZeHQNBNecnqU-5RJliNc_-huJT64syt-6n9YAB-s9MSk7AmthD03hD2gYQ4HjlvpCKdEEhZyec9jc2rpFaIocb3gdLlYrgoUZvw-k3j-YtB3Vvgtv14mw06u5XB4zmI0o1RgH5gqFyZthz_b5ESzUGzIjZvHPGLBfJUlaV4nswIp71J5tP2Lhcx_LCOJeiHaRau_0hIEwC5GVvxlAksSdxb0_u6pEQA8tZI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=HrdthDRAye4mdvJpVTwdzILWaxAoRH4PcJBW680htxTZr9SsfjwdTvnFi84k4WXkH2-K_WUMt27leJv-AyfIlArGFammsCaPpsIEEbSweJ5I3Pc4aa-j27-NlKQck75L04053FXTjf8Yn_xh0jEaQ-dl1dyFtQ1AGH2ZBiMcg0V3H0ITPheGMUgM2fOx79QyE_j0say6cnNElGwxUv61i8X4ilUYiprB8pm2JqVkAPcuDVqiFkeRsnG-p0UM7UmU1vtXeP0otT7VTG69tFkOQHyKsdB7A4oRvAEoSCVLianwRvq3ceBlMBlJOmvUGC3BESr5qbpfj9Kxh-P-wy-46A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=HrdthDRAye4mdvJpVTwdzILWaxAoRH4PcJBW680htxTZr9SsfjwdTvnFi84k4WXkH2-K_WUMt27leJv-AyfIlArGFammsCaPpsIEEbSweJ5I3Pc4aa-j27-NlKQck75L04053FXTjf8Yn_xh0jEaQ-dl1dyFtQ1AGH2ZBiMcg0V3H0ITPheGMUgM2fOx79QyE_j0say6cnNElGwxUv61i8X4ilUYiprB8pm2JqVkAPcuDVqiFkeRsnG-p0UM7UmU1vtXeP0otT7VTG69tFkOQHyKsdB7A4oRvAEoSCVLianwRvq3ceBlMBlJOmvUGC3BESr5qbpfj9Kxh-P-wy-46A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0f0EAc8xB0gF4Ww6p5AVwGsO2biFQ38HFzPGoee9TENmhF8Uno-RNGvVWGY7WLjvE67z4F-Sw7u62jsDyt5rJ2_4OLmvo3NruvaCYT86P4P80KiP-n6V7wCCx3JzRyBCwQzyDKH-5T-P6_EdYLIAR3dzNCGeQ3Z9s5Xqlin3CCTYIbtI1LNgQX18QIvXcuuo37Yno5RgvWh6pEOcv6HMrlezKPHKUfVtQmp1_tO_8OGC4sSzMhf_sVK7M7dCG8Vr35dwviYkqNTIs2PhIF6wlag1C1Uiah3hgT2rQ-iMzuIK_laIWbtXfDF_2RhEEVduBSgk5ICZKFFPYQ9efj1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4rwhTKZejDhZHQ1pT2g7ZAbC7cHX_5felXipjCwj5ZVyoMJ8NM_K3HrqX8EKCIdGfoKw2t_bPhhJDv9zaipz8KAkXWNB_hgQu5ZjaJi8-UOS7wHcn4rHg5Cs2j0yTUl8xUop6Z9rCNj18N0CZNB9tD6g9vHKGFBgmoIhbH06L4yHMC-TRoGmbHF4MiGjA9nqYl-M4Oc5lrfYU6jhRy4KPjuXz7pX9k7bV5UTd-eCfXcHqM7zrDkFxqg5RZ9JKYCU3-GzvA6lgav-1yB4UaczHVy09UlM0aFjsgS5OMNd721GXhfaPQ9KxXD6yKTHARTYv4d17tWb7g7R-aFNi1tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=p6nFzlryqBxxL7xl9dKCogifcxX2062KRjnqJmhSIoipwg87zoTriXPqITKnbvWXljImV99kVH51d2qqtRD0esPB495X6Cjvg9Q5TxEDPLeCiHBCchPXJNnIJ4ArFqNE6zApHdEpguoDctgofq9q8okq2EXUOmaufaSB6gGUNvsjc79BmlSGjJ3efkOyoD7hDbPZFJkHVS0XZHmzJpthGYLD-FxYWExfOtZy-svwQ2sCbRdAdh-ttK7oxC6fO7C75eMmLB1ANOWyTwwde1pbQMcWl6y9MUN-axsIwGAGbVwza3yVzeJffwiJ9A2wAbz3gHJzisYyAt92kGc2nu9_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=p6nFzlryqBxxL7xl9dKCogifcxX2062KRjnqJmhSIoipwg87zoTriXPqITKnbvWXljImV99kVH51d2qqtRD0esPB495X6Cjvg9Q5TxEDPLeCiHBCchPXJNnIJ4ArFqNE6zApHdEpguoDctgofq9q8okq2EXUOmaufaSB6gGUNvsjc79BmlSGjJ3efkOyoD7hDbPZFJkHVS0XZHmzJpthGYLD-FxYWExfOtZy-svwQ2sCbRdAdh-ttK7oxC6fO7C75eMmLB1ANOWyTwwde1pbQMcWl6y9MUN-axsIwGAGbVwza3yVzeJffwiJ9A2wAbz3gHJzisYyAt92kGc2nu9_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYj019F3lDRUnhoT656rWbhR2Wg15feqtf2Qmsf2xMnIuL9P27EpldQz1TvMGHN1E96BYcraNq4ivoaQQ0Ks5KLiekAun2xo2D3EE5WO9jRu-Gl-UybVltwsVrKV5rp-oyxqRisQ7uJBE2_LUQPTYqBQxzKMdXhaTvBVGynOf04s3vYyBsdKFVMfyfykADuLq_hX0LcIXJbvf8NIS_0LBI19SRAvIc4690gTFiV5fzBz_bpheMoWPkRvQ3wQLFWn6nJhk4lRDfpdnyO3cDDsV_G3Pt-Indmegf9-B3pFFE-qR23J_TH9rgmuEFZsZOWo-ZSvkAbMePI6-KIRzuXa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev2KEcHHcGRNO7V8f2mYVuUdZOSpru1UxNLKirtIVbhX121cap14lJBz4rcA1R5UAXmvuFhzaSaCJ7vkdB-rz09Z_bMQ8ZX3PVToKPNXVq70mm4HtryCPG-K4NApveDyjS0OW1O6Qp4c4rb2ArpePYWADoiN9GVbFhc9ltb9eIDCItsl5_s657L9-Jbq9uRATf6vxfb0v72r6FIjEZqzWGv5-dcXUnNaHZfQ1W-eDuVCOlFpfXj0rGGioqxRYN8XzEg3zQ-z8VthIzjAUbjYrJeFpdRqeIEMGkNoaIDziBSBcZPSxNtBUj7R18bpSyVpdjrVAaabwHUvD_hMEUnczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMzz145MQImvHIFjtTHnBNq8ENjTDLBPuYgfs9CRNgy2TVNg4utOVKWqTSDTjDBQebsWeIFzRgbGXhocf3u0Hj37vWnjmgRgrdTPGLWDijsT8_waJBVdhoj0V-1iC7ouniilptwCb1m_maZ1y-VoW-Tshoa3XiXlcQ0MdhNXA2t7yPOPgIamu_MoN1vVLCfdCwispSxqGodObXDJu6-2d_LmKRSXdKzJ4c8qyfbWDSaA7fBCriJ_6bVs4AaQsJTwSWK5GUoeh-LMpKTN1SaHyR-nH_vJtMVuFKPcis9OnGOU4yYz9FK7g1wLmqbhcGozpf6wORLd53edNN0yLQI8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRzgSt4joF1UheaAmOqnsjH5pAWdGusNjh30ds-vGJweKqAxp4Vng57K_oacY5reMusTO5yU8mdlvxXhRmPMTwYZQYGjYwXWuVju1slP5k93u6U_P57JNq26qfCOEzsnHPLfT1aSiZlXtWIotpv8XqHSVR5ds-MsMw969-CFIDkhG4ymCua7UeBCSwYRJKroiJ5lXs9u83vBmxzkF6b4qfALvOphrXsooOGSSrS12mBklJpfwrThuM-DSU-gy9mc2GhecBbiq5suj5X_lMaYICNfdQFx58q2yiJXYQ2T1Dq6Dy48O-5H0jl_IzWyLTODzh7pvfOoup6ZNLLcpB8uiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSCh8fON_d82xr515xdfUTaMj4Bh4kyHXobSSYsf6sLcp9q9WrztNgUGdT77Yg4YvHq-bOwzOBgx4PeYoPeKeSogXKk2tfUS1yruHPffDgQhVSaaEeint-F2TUQA7wIABvQdEjHbgNAA1bDnNV68mNhaMydCEQsblJfUUjnU1LxHzReCsZRF_sVbDYHjUIQcylDYxXO2fD5KbugjNS0eKa4y9QknqNoVQlcsfU5jS-jdNy1pIzBkP_LffoEhgE_ACSv8K8zS93eCHmnAJ1DrzgaZK3nMlpO1Ce4_h9pDP8eQ5eLqd5F4XnQaNJsSNcRGh1MpwsXJYpQsAftb6tIJkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=D44FbNNJIrUEI4oRJ4aPP-AOI4yF04Ej1cmv8QHwAv8vPlOb-Yd4D3MGDcaJe2afOpzYYG5VgVm25ju4vFXHjaIGtwqTfr2yOIRMOpmGpNoZub3wtlmCtvoTfSMiMKaU1DbeJVFrNfsaruNP_9mOAPeqHs16g-782XMxllZYOTXCjyq7aXij3bpJFAmvt6XqQlozq7n2UC-7-njBaJ4vfXhYpUojaLZCeCx5FPvFxMZgznkyfgT_89ymuk5zNWvCJ-Knlbi3p-L3P_T_Ckcozf0rxDrmUcRo9X_rxwuyTXXihFcqio8TP0Cc1792Pl0bTAHOYX362UzJB7vLRG6PEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=D44FbNNJIrUEI4oRJ4aPP-AOI4yF04Ej1cmv8QHwAv8vPlOb-Yd4D3MGDcaJe2afOpzYYG5VgVm25ju4vFXHjaIGtwqTfr2yOIRMOpmGpNoZub3wtlmCtvoTfSMiMKaU1DbeJVFrNfsaruNP_9mOAPeqHs16g-782XMxllZYOTXCjyq7aXij3bpJFAmvt6XqQlozq7n2UC-7-njBaJ4vfXhYpUojaLZCeCx5FPvFxMZgznkyfgT_89ymuk5zNWvCJ-Knlbi3p-L3P_T_Ckcozf0rxDrmUcRo9X_rxwuyTXXihFcqio8TP0Cc1792Pl0bTAHOYX362UzJB7vLRG6PEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxk_OrWiT--V-xKzb5Q66iStiBTm5Fe10tdIy--tSCbpUJ2PWTjusP6ZO_Y-AaMkYgPm9wrx0V3DRLeCcZihZ-UnVpjviV3jISWZNvEdgzKpf7TErmTZg43AnM3CB4ovy_CC54Wqf_Agoadw-SQHeAzSpIMzGbnFS7AAj8UTqtiZsynw9MLuf4-ri3jvagqLk9Kbs6k8TOxePRS3pp9t4aUK6RuQGoJDOGqH8GXwzESy-JvpXJuQO53fwPKO68zOW0NROmubijcsHS6ety4Oe3EA2mInIkw1tZXybgZjmLdmE58_y7FfLdGrutQAAOMoYwgZHa8Xh_AfYbLpULdQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2G8iTmFS2KG7j28W9A7XX4Oll8F5BuIpFgA7DKs1g3EDCHYd_uTwBgPddMHUEiFYYFMJjwsNjMIwOQkDjRAZc1ZXsyNUUIctEaVJyvjEaCK8IlvcAo5SyqKopijCnWwYf-bLl5sDoCNIsQswi1N68fXn5vBYqT3ULvdic3fxKx8pXkwifvQO_0hjw_mEdI6MdU15MmJOvJPcDtrO06jVfJYCVLrfc0NGIIZOvq2FYMJhy8ZL0DzrIPWkvr3Qoqivt02EumDB7G22sqnCaArxIgYykA47XJfw0ZcaGnWqMGk2hZ9HNzWfBSc8GheQ-zgCUDR37kU_EWXbbnhJmu_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=X95Oh3lzlZHe2e8hZT8B9YYiY19gkCafKmq_tgCfmj8BHiFVSQ53fQ03D-FmAcxznUnqxzxy6jtPCh0NmhgpbEDd_n3hm9RaKmnz0gzE653n0MDAqJJUOT_eoBi9zGPtxlp2KpioW8vxPRgvIJUWO6MdkmNtMmj0TDrXrpFOssAqgFv8dJBYNkydIzIPc9KZ4uVVPhOfOWJL82v2p-DAjRO7NcXoiKtizVV08MoCwzVUoZlskMuJmeArP-gkEeZ1LcV1Sl2NlORNAoTjCcsYiM2f0rQ73FXNTtmeX5LgNwC7SCSsde0a7K-ARPZSo0UQjoFRB-hIkqUeFl3U2RjlzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=X95Oh3lzlZHe2e8hZT8B9YYiY19gkCafKmq_tgCfmj8BHiFVSQ53fQ03D-FmAcxznUnqxzxy6jtPCh0NmhgpbEDd_n3hm9RaKmnz0gzE653n0MDAqJJUOT_eoBi9zGPtxlp2KpioW8vxPRgvIJUWO6MdkmNtMmj0TDrXrpFOssAqgFv8dJBYNkydIzIPc9KZ4uVVPhOfOWJL82v2p-DAjRO7NcXoiKtizVV08MoCwzVUoZlskMuJmeArP-gkEeZ1LcV1Sl2NlORNAoTjCcsYiM2f0rQ73FXNTtmeX5LgNwC7SCSsde0a7K-ARPZSo0UQjoFRB-hIkqUeFl3U2RjlzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8jOk7_DeGHNpM4a8JQDcY9YULILokLhS4QxCD6QevlYzW2n7A3qXV3_4CV9_8517JH7nseiCM5dsZWPJYAJSG6XKrnnOpDk_IaKRvyG-7VFi0_MQk7OZ-P2QWIEq7_2Dd77xL83GjPe2RkFUoa2at4Se19Qo9NI1hN5VMxp5FWLhffB3yljdDyUnvhw0FXYX7o4qp8kCUlyBmJWvBD00y_goMv089O6nK53v8-B2c4Uybs6whjUr1hGRStaB43QV4XzJMdnZqXnXA804PsMwHY0lLBXt1cNInmAXqHEJtrxBPRqDg6Dm-PCCR4rON5BZleRkFskAiQzQxI2VFVYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfeQCCq-eqprEa8_Tbb5mneUVSVV1Sl6rohdROngGQlAyEv4uYOVSTJJH-vWvpknHohLs3qKhLmspvdgYTG_TTtT5lh-nocVdZnNyQp1NN1Zy1gkIwjcfzDYJZcGHt_9hyqfZBiWJUDs3Y3Ysul9elJMWhob37IwXOJkG7gqqaHNZoRo5fqFNeGOK-JXKPHEmIJvAitxbV9bfRgBqtffYH9H7V3y8gA5Dy3_ZO5zT0Ply4tUl_vzV7UdgBod7mR76q6RBaJwGNBCgtmbclDuXHvfA-0u_H_I0AN8i_ptps6zyPFcO-WEJFSLK6EOWc23HhNtAVsCvw5TW5hfN3MhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGuuYxdPsBVyfZH6T9U6ZBxBjzs2scuhcF0_DwJU_K5XBOYQOrJO8rS4V3NXHpX62c5MVzcKmtfuU8jIEMo5brN6w1AEefvGRuLs8C7iu1IO9Tka4DqIDFJu0K8ogBX5ubUKwQs23k5Z3BdT2z2ZQXubyHdxGFDtpRYHJ0PoG67EgLNNHH_qEi4LXmsWJsih2cEH5WWtU2iUcFoc4gZuV04mwZD6y8o8u6_xkWHc1r-mOU3cbErFXaIPGi53xBtsh3U-J0Rj8HXDZvtuTGKbuuP2j9ybZ0l3wg7mYOJylrSIOYb-f8vaG4yHJWUSwR8_GvLCERgDqeXuJnKxseewiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcL-v2OqX2HHKt9wAbydKGw75pRhV50qOomR5fOLtDvewQnEqqfp_7OCGXyKz9i2B0VYpOAMoU9bYLg74ab_1edOglrsK_HALy-2MbkSXQ4pEmB-E-LyN0O4yFz462fQF6o00iOb-gtTPkWXdjHvXkxvA3tITHslJLxwev3Oj0cAL1B4mmwczYpRKvEzlPe1_eWXdIV6QZHpOCOO89PB1pibbh3rDUcDVRdKjX_5r7TdV99LT6Wro3sROSUZ7kkiycPMbVO6pjojmkRzygRyZqlsdVJPB7qsgmr2Znx9996O9qKMJJVq2Su_wuv-9wzRv3kIsTPCoe1_Y3hQMfeSbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShalIlBqmdqv7p-XxgK_CmJpaYjLyp_L21wBtjrK7w3TzzRLB4qHkC4A2FC0yepoHa722G6wFoBPIR7dP5lTs_bimcdJGOXe5HTZPGOwa4VnATrQLtjCD4p-D4esccgTStAqUoK_8I-K_dLIRDHXAbPRC8JDEY4j_3xivPeuw3iSv4ex6W7waiRl9dsL3euQjf5XwuvXnGPTzeS5mQKim5Qk0Yk32VBJ5Q46WiK6jyuUK4-bbr5As5AelF5D4WUYM9ghU32cRY5deJZcbIqz-o8jNpjwEsP2txzIGHtix9ViEZqMEIENbtKYrSSoMfzdPXp3CbLIxVxu8O5_8xaf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=EdrGvisROEnCiVsCLg2aXlLMH4zUQtkgqe-QtOAnVJQY9UOxGdFimd8taLOuDTq-9Rthh0dfL1ggl5etWP2llLcG0_mJTnX_eJhhvkzBfS4OEISqbgDrbY7eCR6fnleJLI0It8sE2UghsQM8yY2Uzvv8gbbcvrxF5tw29dJ9m2ceyzYsmjfl3Fybt2i1ZyspYa4-uchIFeQzzgH1JpyCwT2JCF9yGRINSkl7ZYxE0S51m9PrB6f4vPbF7lBcyChoBEUBDadqh8FwxhbDOU5tL9RqiadXDfICbAGuhoDF9WEtEvTbWqu7595TafzcCoJgsje3KV9UvPIz8Oc3VM8cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=EdrGvisROEnCiVsCLg2aXlLMH4zUQtkgqe-QtOAnVJQY9UOxGdFimd8taLOuDTq-9Rthh0dfL1ggl5etWP2llLcG0_mJTnX_eJhhvkzBfS4OEISqbgDrbY7eCR6fnleJLI0It8sE2UghsQM8yY2Uzvv8gbbcvrxF5tw29dJ9m2ceyzYsmjfl3Fybt2i1ZyspYa4-uchIFeQzzgH1JpyCwT2JCF9yGRINSkl7ZYxE0S51m9PrB6f4vPbF7lBcyChoBEUBDadqh8FwxhbDOU5tL9RqiadXDfICbAGuhoDF9WEtEvTbWqu7595TafzcCoJgsje3KV9UvPIz8Oc3VM8cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhoLmU_Tj-PabIZpso50ElVSUReJvkN5lU_iAyBp9ACizonZC3yeNjC8SqZNn8dPvbnqubYGloGX2TJoJCHhJJ9kiJ-oItHicxju9RS4_pJx5JSxP4iM7_EINT7gbyC5Po7Yr18jeFU806rkb2Jdhf07JXNU31n3A67ZkbeaAKHp1iyfF2Yg5cutmjE6XRZbqsq1Mca1eSDUAbW1p9wRIMGusCL5md6HerBg5lWalV9X6-hbr-re3voUvaI3wKM7xRaIrN0asDIFhFyFY-6cjlwdsawK_EYVnkra-GfyaYcVindxJdzGKYAo1sUdGA9IfdiULxsvbebFe-jbrYIXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQgtFVr3DlnRfaXC9RBshKWyKcP1rAjbRXYFuaIVjU3z6O-QQeb0MyoHB80r3rA31tWr6uhPdC8YFXGa-Cr9evRlOSlzKXvsIZNMk2njJsNiTHCAXVbo6xnrTxYX17YEy9y2pIerh3T_cuFAMpmkefodhEN8QT03Og9k9neEYFi0Sj2ZjoU8odrvUCWIOzSgtPji402BRw9za9IqKCHfCLZq6LzEy1Qa34nc-OPGZBU222_aD78Km_jzM9mzYODGu_g9fvNRftuY1W6aaIoWq5gTMXUs8g01k8Rs3MmEtPLzSmmz8o9nKzct7AQBtEh2GSMDApbRRA4k0LdLUk2jGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=cXZPcQl4UOVUlqzGWOl8Z5iVs8wwd-A0amygwmiU0yDDazDKY0dDqjRDnU9cbHu_2DQhj9aMeaSD3Uvw7iASDvW1BcLDpEkHA_YKJT56PNGT_5MNwVuS3dA3u0kPXhOMThTW_C0DGp7NXPBKWQnBwCJ8313hh3Co1iNvhw2hFejhA3X7aEYMliG0g_1Zh1srZepdrMSjPhaqpp_jG9xK6Ef9spuz1RSrRe34PJ288qGR1ukUb2QoxksLz8VzQPMjQKTMcZPoGHbNAEfyVasfzkM2hi1c5_UrhqJL6wtBlpugtZp2Zy9NMWqwyMn1bPV1DAo4oGdFQvwLHVAJjaBIul8mYbW6fkH_Y4jHmID8YB1ttg5w0ZBHjBE11Wjixluk1ymWw3ESV0SjyfY5YG4XwVRjv0rlz9RyL5YrsYIvdjYC5JFC_P3PVp4uILssqcC2or-4BOJ0ctWkllQuWrJBZvfTWlA_7P4UhHCkHYst2fWBLr_GV41bkMvMm-5xGyd7_2s6ODzgGVCWWc7pGNj1q8VhhleDCDm_AXbir1hdHeS-0YNysHST-bNqJF17hNExxvXT_kkwFNBk0QViOWhjYJVH5gL_z8pLXICRP-1FxJwnxzZvkjwQ5FLz3pYjfetmaCe8sjunzBTLJH297Y5YeGDLp8jfoyjLz3fe7v1B8TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=cXZPcQl4UOVUlqzGWOl8Z5iVs8wwd-A0amygwmiU0yDDazDKY0dDqjRDnU9cbHu_2DQhj9aMeaSD3Uvw7iASDvW1BcLDpEkHA_YKJT56PNGT_5MNwVuS3dA3u0kPXhOMThTW_C0DGp7NXPBKWQnBwCJ8313hh3Co1iNvhw2hFejhA3X7aEYMliG0g_1Zh1srZepdrMSjPhaqpp_jG9xK6Ef9spuz1RSrRe34PJ288qGR1ukUb2QoxksLz8VzQPMjQKTMcZPoGHbNAEfyVasfzkM2hi1c5_UrhqJL6wtBlpugtZp2Zy9NMWqwyMn1bPV1DAo4oGdFQvwLHVAJjaBIul8mYbW6fkH_Y4jHmID8YB1ttg5w0ZBHjBE11Wjixluk1ymWw3ESV0SjyfY5YG4XwVRjv0rlz9RyL5YrsYIvdjYC5JFC_P3PVp4uILssqcC2or-4BOJ0ctWkllQuWrJBZvfTWlA_7P4UhHCkHYst2fWBLr_GV41bkMvMm-5xGyd7_2s6ODzgGVCWWc7pGNj1q8VhhleDCDm_AXbir1hdHeS-0YNysHST-bNqJF17hNExxvXT_kkwFNBk0QViOWhjYJVH5gL_z8pLXICRP-1FxJwnxzZvkjwQ5FLz3pYjfetmaCe8sjunzBTLJH297Y5YeGDLp8jfoyjLz3fe7v1B8TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgY9ih0s-MAhw1N2MSUDqMn7k65_15K07IOCDNeeC7RGVoRJXbRKCdQXVWuGozpUfIOB0I6XvtP4CwUTJ-_zkb3HTbshsGCSlgh07LNkQVODYG499WSQiLYrvDDt4yvLihnECaY74fb796c6QT2GPmpYEGfIvyC9z7Zm9lsnPWTlYjbFQcs0H2NSohdQHRy4qpWAE8dvxlCOybgRKO7Yy0eEGq0-e_8RTiCRUPiCH2pFfKzYqLC7fLmKl8tEUiKFoPJ1ONX5fqYf5XeXIioKazf3eoxwrSvj-9PpSpFUtcg7wxUP_79SiUngsulUmQvhCm2kQYznapPIcXCXXqbR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Euq4JMkfUjoVKa6-bG8qCpvf-fwg6dJXuWP9ktGETIO2hVAKf77Me5QyqbXCx1ssNHeLAM2lvplh0rfUjEKUFsHavCxQrFAumIwr_AWSCyL2VCFRqYXQx7is86s2zZ0boMfbga4YI0r4Hu4JdKFKvBh2sEEvG-grPNBCYTVajR-hgZBzqJV74Nb1FQwnyergvTrGHJzE1BlDA_9an9X-iE4bKndiCYe94T8ZQy4aR6ARLa16-4rcA-xIt7zpffr4zqzKji6iGtPtqreIZ33d5VqBUa68n444mamtlbksImrekvYF-DdjTb7kEEmlrI8k-i86gRMiFo7DtdRfMbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Vv1wC2X3HCvxjf9SJcI7fg_1e6UxiwQl7Whgu2KB_M7FXUdLnDirUeTRSiPQi3dSnicX_vBtpUQzVK9QFJLYmKLYi4SdsriZtSgBjb2tx6_7377-KlcqbVsvnSpcg8IYU1n66o9oOKzqBM8Ej-EGoSHm5ng0uiIRpmMO2vojrna7M7pyDPQgNxTMbXJk3IRZK_dWvA1icxiqlyJxqroneouFXarfdUdGc73qsuheeBR5x2uC23A1D38Fb_iKK2YS-a9IqkSmQg88AgbSL20LmCMvV_6rPIrzIPxw61yrK7KPzhbLe4cDUmzhLxd7i2Z8Kvbx8-hrSEflEgFs39K1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Vv1wC2X3HCvxjf9SJcI7fg_1e6UxiwQl7Whgu2KB_M7FXUdLnDirUeTRSiPQi3dSnicX_vBtpUQzVK9QFJLYmKLYi4SdsriZtSgBjb2tx6_7377-KlcqbVsvnSpcg8IYU1n66o9oOKzqBM8Ej-EGoSHm5ng0uiIRpmMO2vojrna7M7pyDPQgNxTMbXJk3IRZK_dWvA1icxiqlyJxqroneouFXarfdUdGc73qsuheeBR5x2uC23A1D38Fb_iKK2YS-a9IqkSmQg88AgbSL20LmCMvV_6rPIrzIPxw61yrK7KPzhbLe4cDUmzhLxd7i2Z8Kvbx8-hrSEflEgFs39K1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=oyAxhPR34VZBfVdBP6HFUg534x9qhoz_Ki5Y3YzPpvlpJYoNJID7XnNCX2VSDpDGVatXQJDNczY0VJtg4FUOGS7DAkCV2GdTSCJqNTLjqyhLcXZnMyykKOVYrewni0LDsyykyWjh4leTYHBXCi6YzhyyiPI-Nl70WTt6PCeWj0U3sEhT-PXO0L7IyOSqsnebnxpUL5pJooMP83ffLfELaZ3y5CbDXfF_jMc65TZIF5GWlOaWY66UBqFYzyriW6CJi7jfm3I77WKQCKtgfj7ppGxIAoyuK6zX4D7Sz2qaKMgimM7rpOb58ehaYbPgvEdVByiHrvsuGKMWRLiq8Wsddw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=oyAxhPR34VZBfVdBP6HFUg534x9qhoz_Ki5Y3YzPpvlpJYoNJID7XnNCX2VSDpDGVatXQJDNczY0VJtg4FUOGS7DAkCV2GdTSCJqNTLjqyhLcXZnMyykKOVYrewni0LDsyykyWjh4leTYHBXCi6YzhyyiPI-Nl70WTt6PCeWj0U3sEhT-PXO0L7IyOSqsnebnxpUL5pJooMP83ffLfELaZ3y5CbDXfF_jMc65TZIF5GWlOaWY66UBqFYzyriW6CJi7jfm3I77WKQCKtgfj7ppGxIAoyuK6zX4D7Sz2qaKMgimM7rpOb58ehaYbPgvEdVByiHrvsuGKMWRLiq8Wsddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6bGj-RecmKcbXpNONRujJwRUUhzhpjITdQ9DaTf19A7FWWotJfo2qxuD7Ks5ouAwODumM0EfAYnjh26K4RrNe1zN5891-j_PBLQqIQpT5jTOkorzVF2DmyEK6q8uyggN7tYWlgPRo0b_9wCT0tBvPxPWju7ZGS4V9LoHJBPWDK8gSoDdrL1DvVIoAM0T5S3LX8xqfc3n7siGvo4f8V-UlgS--RIzhE9TIgjmPgioZRpbNinkbNDuuelSYea99P6qWFCb-76Q1jZYg8GxBZ6kAZQlpSoeqwnYxF4EYKmHGK12VEBJF9Bbo0ybycCvtjIURhMBddB0zmSo6foxwcstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWNGvGTZ_k0sxjyXIMRb4Jn3QrEpKAaz24ZeewwI4N7hGGyRvf4kcYBYQ4jirgv3yvQxDsKKQ2gIrIKx5ArtH_ey4e9fbkDdQ1RCTn_OLhUU0NqyTg6lbBvm09jXElIsIN1OOjo58_the6bupRWM0PjeFdCTmxygxXBBiTPk2Ijej8ue3nOnponu2jJO93TbdaBMd4Q50TyaIP9Swccp2Z65k-iQ6ad2eC-yVzccV3ySq1ruNRsum8KtEiOb2eAeNA3x30RSV8uSYmJ9JblTLgh7xUt1GOX9_KXWyS0p3_EAhdQZScUh09E6tT7ejaHzUIbosuIwnCFuNwREOBGL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_z-onoz8SXHV9vzzVoI6nagiIVhemnqY4jKbhehJ9iXDs2rM7kHDlIaTtZKZ_KA4nEpp2XzhnH71KbOWwLxH__o8pyadQvidA9__Z14UBPwIXtTJcKDtseNMncoQnIixd9Y7-THCE8aixeg50v01olkxOgvACsvawOr987VfeAWor1tp0V-C4KDhm5AO0Xy14gbi1_BnSOiJcA-b3EJw_9RDumJcQ2KybHNyFqCxeowjaLxjEwVWHNeWpWQVNNB-87vL9eSd5GfaRhvCTpcDtOJoRw8VC-e_rO6rghr28EmPlgXDc1PTTzcC2ELtECnzaKZ93oGJoi0VQ3sroMNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=Fxb7rnfh12AYAGYHlDBxTEv39hNIPbpJsILcLGwBeJ_tzQ17dAgVMSncT5MQdUBzc50S8dPYok3lh1S51oofrW1dFBz2eOGfx_MPiDpAy8WSpL9jWl46ix6hAni9k6oYkZQy5S27X9jI77pBeFWWHDOLgzooVu6JUtJCNvUzuXPx-_em2w0_aV1_OsrsAZuFGQ0N-vN8VC3gL3sSVp_o2N2vkhtxTdA9-4d19Dc5FPMbTLa1xK_Ds5O6ljlH_xU__T01HHNab5Zi6Uwm8GokGFi71NgImV6yu9ys0X8Ulywnkz1CM7XN2qXoeRiSpCEL7yUxZIca4_Gg3fyMn2WeCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=Fxb7rnfh12AYAGYHlDBxTEv39hNIPbpJsILcLGwBeJ_tzQ17dAgVMSncT5MQdUBzc50S8dPYok3lh1S51oofrW1dFBz2eOGfx_MPiDpAy8WSpL9jWl46ix6hAni9k6oYkZQy5S27X9jI77pBeFWWHDOLgzooVu6JUtJCNvUzuXPx-_em2w0_aV1_OsrsAZuFGQ0N-vN8VC3gL3sSVp_o2N2vkhtxTdA9-4d19Dc5FPMbTLa1xK_Ds5O6ljlH_xU__T01HHNab5Zi6Uwm8GokGFi71NgImV6yu9ys0X8Ulywnkz1CM7XN2qXoeRiSpCEL7yUxZIca4_Gg3fyMn2WeCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=m8mbaWxhGBCiJhO9UXDZ_D5anL55YEmUwOS0G5IrwmYNK5VVyPbPkBCVk3X9V3gsOr9HoMGp0Dt5J3sRhHyMr4BK07ulZ--Z8Pltd0wKQtwiWfQOa_ERxFoC-f6_HGGoyGX5av-S1smmu7FlflPdw2Q-Cnpi4GWPvoVVM_LJK--QiuwufGTOIiR4pctV518CdeGJCFpNVLvQ5nBfv7CFYz80jGhr_Jw31Z8g_DyIZzpJqkX-6mbssNpCpwSc8qsMefut6IP-5YrKGHLMdNrXLhA9gDL0kzZlG-eXWNFBanlXoPoLWKmagQ4R85QIhiHV9nW9zzN8aTnZKhh04egH3pGsDadELLb73vXqljydJAtVb_4CN8MSOa3HinM59G9WgVQIK7kqG_pQ2gr2_R4Eop21rh6P5nCL0GIwUGuoatlSzRhlFx_GmAePWnD6kkwM2OX6n9MtH3ZuryGfYz57AksTeGjtHMD-fCv9pQn_5ZkbsVpWHjfYBnqp3S02esuAHkZ7AjnWC9RE1XQdm-RJ81x9nEzXzMr_QUAqHBUh7UZ_XJaGg07mvw4Lc8bAfCOlhQmBD2TbVXp1voMuqZoXpXnz5mGW6zA6FREGfIvBiyTNlHa9Qy-8OosfHpeWDSegPZNN4esTkWr0y6Q-xmq5X3CpWsOMQoGF-Dr2Xgt2-c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=m8mbaWxhGBCiJhO9UXDZ_D5anL55YEmUwOS0G5IrwmYNK5VVyPbPkBCVk3X9V3gsOr9HoMGp0Dt5J3sRhHyMr4BK07ulZ--Z8Pltd0wKQtwiWfQOa_ERxFoC-f6_HGGoyGX5av-S1smmu7FlflPdw2Q-Cnpi4GWPvoVVM_LJK--QiuwufGTOIiR4pctV518CdeGJCFpNVLvQ5nBfv7CFYz80jGhr_Jw31Z8g_DyIZzpJqkX-6mbssNpCpwSc8qsMefut6IP-5YrKGHLMdNrXLhA9gDL0kzZlG-eXWNFBanlXoPoLWKmagQ4R85QIhiHV9nW9zzN8aTnZKhh04egH3pGsDadELLb73vXqljydJAtVb_4CN8MSOa3HinM59G9WgVQIK7kqG_pQ2gr2_R4Eop21rh6P5nCL0GIwUGuoatlSzRhlFx_GmAePWnD6kkwM2OX6n9MtH3ZuryGfYz57AksTeGjtHMD-fCv9pQn_5ZkbsVpWHjfYBnqp3S02esuAHkZ7AjnWC9RE1XQdm-RJ81x9nEzXzMr_QUAqHBUh7UZ_XJaGg07mvw4Lc8bAfCOlhQmBD2TbVXp1voMuqZoXpXnz5mGW6zA6FREGfIvBiyTNlHa9Qy-8OosfHpeWDSegPZNN4esTkWr0y6Q-xmq5X3CpWsOMQoGF-Dr2Xgt2-c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q97_TvrOlW3V_WNCleG3z2cXsrdqKNIfEgHsI35cxsfBVqDsM522tOv-DvMIkr1EWwMdxoODGrh5O8dGaHoOvxGBAwXGMLiuZNom-kRLTxVKlbGVJraM2o11xXHw21TaSIe9OfM_CQV7XG4KxuuVllkBCV-u6wVPq1FGULrJYjlDmktOwPuQac-rrKsw2UQ11VRalZstyCFNW3HH5pXWFguvwKgZ_bRp_qeohY4ShDh9JZnKz6Co9sHNa2Ej-sHEa_ao-lz3etmpJaWdElR63ENudwnP4g2_LQ-wjklod1sJjnX8UqzKWu9tCD3UMKoLO0aINGNnGhA3aW5Hy6nrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwiRJWTqAi64zbrli0pkwZRBkABfwAaJj0sGNqHVk9BBkrMXBnakXw-2pbnWPlhFx6dBjS_ljEX1HdpYlZoLbIMAcfMDE9hoq2HmnNu4aYVoX5oEfmb7qkqtaZErZmgU8EL-1_C02Pz4mk-QJH0XHLOItatQbHUhRGWMo8gj14TsHBr07RQsQEJGeZdvw7eKDwg26lY8fi8a5LB3hNu4r6tG7BkLVfsAlaKzPBjTWKcgalYWpzc8eqn1Zz6xtXgZAgqQYTF3mmxS24fIvNPWVBUQnIbInn3LKMuWkZJvCXZgELrLJv6qOfGuplJ75MlANNorXcNObqI_rkeqGc4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0OL4e6PbnZ5Kis8NF6CPTH4R4apH8ILJTNSVcwTDlaTyzvpsWw_uEbmJb8-kf-n7S5swpiwp9YU_wKvcIjSJ9fSp118oRqD_l8EwWWsfQED7fc3-7BRqngbC3qNOLfy14mdpIOds9thxfOSFUaA0wzzab_YIvpbv4gNN3en4sCIBY02DcFr07o6Lmz6FJp4o9dDPvCFjylH8fUupKff4_MdTRa4Wq-PAmexh3tFPIrLOnhq62RNWY1ymE6vfKdMsqNEo3hYosvBIkofOBeZHTuC8NGsN8pBiSlQnxvWoYADLVM2GmmHGT7j8lF1aEsgkTEuuiTvTiyYbufgcELdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDHXlUiD37GUm5odecrcQmX6CNV0ThgCeJ8wotwhuKjAnFOGfWD2xwddtNTP1h_LWK-cvG7wh4tO6bG1kKVi4uLR3NT0sdRsbMN58_3VWDUJgl_l0eK3ze0_jL3ZaT0DwnnnXlYi2KlrXUupCCjGk5NXzeMCbF6RJNRj3uf_mRda-aUlCdrQw5xYklPzcrgpEAN4HMEgxYAAfizJaQ65B2q88KTz1h78NulUxYgwYmoXJNncyfaUjse_FPYiRQ54zT15zuTs9fMJjWKlMU2KSo2ISnBQzUbN8jbl2NUo8fgtIpSMUOBdYNFXggcirnosCyYDzX2WEkSlknBdA93y8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irKB04rx9wkgt86H5m75u64RS6ppQqEdn_azZoqJlNm4RxEThEGtg4wRcR17t5FJyJzj9eeIc8xpuYu412vRTdRavqmDdjDSafQfA_0JfZqVIJgMNyoJHytXLWPJVMR9XS4uixUxA_-uiK-oDzf13FuS0CFVcSXVttld9zLFSKffZGwtdCmS4GgIS2jCTXolQpLGhylpqwTn3tnpxCd8_UZVD7k8faVNl4Dc2A7rBDmGumkQGfJPntW14gBemiwk1KjOYGYeDyeDLcXxkhgT1Z7f6Q_BDweUg4djvofqsN1YIkL3YlBnfquLcFi9Amw4jWuMIleslXjxLMKVZGs77w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjUHtRelaMUNRVhbcrQwq0ZGhqRDhGDjS8JASIFnBxaO_GjG8qAwINNJ64jHICTCuj30oGSURHjXzlakyRk3W_7i930VSXutAl9JvVjWGazZ_4FtjUANHDFXcU3A1twwxZXL5_3uLlSO0gPEQ1s8jnVOVKMPn86Lq-zIMWaAS70exLhGadnTa2t7tHKB1d0X4YIqu06tLmVWTMEkTQIYbeMzts38qx2bV3AMZLBqy2QCCWkeTmhBgh72h7uPkZv935kT4H0Un3Pz7yE2lJSypDKbfnZWblvnfNcoXCAusFnEj9nzEbWnZSMY2dlVCooxIvM7t0prMBsPzjTsfIzjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsVr_IvIQJk9BtmL29ZHQ5KbZOP1iyvWGuRmQiPPleOVCiaK06h733pvZ6ZDEODFShWM20E9qrLknAUUqvkim-xwZBCFBhbfXkh8d_dtinMHYMeftMP-46HbJOXT5bqudeuE3XDuyfGHdZMlg-8uQJ-gYf27_hmkhw8yR4qZ1ARFWmxWJUDSQSJPgVqxdPQUFDTf_fVEkEkPU7c6v2nMrLiq7JiL1cgxItYYmK54nsnyn2OrcnrcI6qshthZOkC4bsT7F-cbdsmM19fiMkOKul_gW-JiWJyuxnoYlRslQOj-Oqm_aO0Pse3qvJ5ZE7E9SOWqsQI18ZEsIapOYGZn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=XiK-u9O6wGwEINq0PLj0myeuI7aN2m1kFsfFftoM5okmAXnNTa6Q5R2XEFh1kDRP6bj1tclpwJ5BsaGmVVLNOJGUn5wdy73BG3hS84TVuZRQjZKmds8Z9vlVGI64DZ4zkwtkgG-qT1QaUbba0t8vXrI68ulMbJpuI8ahoV6dsw0VaoZEIZswUTf6xgrcSK1MxWtQKrZ_SUBvAgJbeSZNMssALq2IfK0Cb8jfE23nEBqAaVuZjBXdvrEZieD-qcKHVY2f_UmVxF3sq00O0irPCkMJuHT8AJ1CuzVdrVFYYY8y38eKnWKDwVWaYFHmvgcSo64jREiFiey0spgMm9jipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=XiK-u9O6wGwEINq0PLj0myeuI7aN2m1kFsfFftoM5okmAXnNTa6Q5R2XEFh1kDRP6bj1tclpwJ5BsaGmVVLNOJGUn5wdy73BG3hS84TVuZRQjZKmds8Z9vlVGI64DZ4zkwtkgG-qT1QaUbba0t8vXrI68ulMbJpuI8ahoV6dsw0VaoZEIZswUTf6xgrcSK1MxWtQKrZ_SUBvAgJbeSZNMssALq2IfK0Cb8jfE23nEBqAaVuZjBXdvrEZieD-qcKHVY2f_UmVxF3sq00O0irPCkMJuHT8AJ1CuzVdrVFYYY8y38eKnWKDwVWaYFHmvgcSo64jREiFiey0spgMm9jipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlegeBMNDO6ANVLIIDfC8md0wYX7oDrj5vPQSwWF-gAlfkQnftcl3xvYLaH7x4SBrbqOYIELtClixwfW2KNByiG0cWjWJteUCywfIOTqsIJMmB4wJC5kEL9EGJ3tVkXcBsATTynbr2IYxDhYfaOn8rAcr2zxyBQ05SYwmeQc9_s0CWcpJoWMsV817jZZx7zwYcSSmcJwaQrpYmuyoxxByJm-QHCU8W8tPysGAZhGd18O4e4KDDNDL7SyH-nBQdF_DF-F-yxwj6HoE7qaXtWcDU8TI2TMVT-wdMaS6v10puAuelY8uq8beigxFUdFXq9CK149A5e7zzcjtQsikofhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6ThiyuxN8gmumg-83Ti_xIocdpN2TvNqiKxyimyf5l2tFwubZjxswgzTpYBz3DOaj5cjeJdHttmNnMjLsA70fD3Wxu_CvO0Xjjkmb_VtXOnfOoHbT7t-tqeZiIc8HlFPM64qMUjwA2TIj1wbgpd0dKH3yEWVUol1fsBE9zxlEix0Z5sE-a9yk0Rh5g04vw2wbY6faowoFcjpJkJ91VzpXHloaTsQI1Jq5jO4_jle5q-YeR7nnk7gmVCa2gE95amTl-jSI6iXdfY_cxJCV_qlobP_vxsJ-MmCLip0LN_8QzhI2wtsObPIboU1xFnVJUi_N-DmSIA4qAMp2H75j_i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
