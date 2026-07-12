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
<img src="https://cdn4.telesco.pe/file/q7btbIWmJNxPbtsN00J1Zi4cY88SLk0JgU9gtsLuXRYDwwFk70wZuIGYEgyrpU9vpA_FCzMyi9qCVlXIHJzuKj8hTg9qZR4FkvR4maYaRdBEZQnbRtA9arG80gXUDj53vasPCUtLUU2ApBzXfnYvH9AyMUKaikeGFwyIFB2lv1QAMmC_23flN-xjvYaExg9ASNsThwCVom0bY8xChVdNU31d9HoMdM3jme67LFfYwphT3CV6iUFqYlSleg9wSCiWJ0o4uAw8WN2Gv7Uz4BBYSPkRwV7tSqRNxeebqHurVgkBwJqNrbatu-Griaygm7jH-CqdCQ6JQ4vPSfphSWhVUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 19:01:30</div>
<hr>

<div class="tg-post" id="msg-670239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه‌های عراقی: هدف قرار گرفتن سکوهای پرتاب موشک‌های اتکمز (ATACMS)
🔹
گزارش‌ها حاکی از حمله به مواضع پرتاب موشک‌های اتکمز است. همچنین سه فروند موشک بالستیک دقایقی پیش در منطقه بندر در کویت اصابت کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/670239" target="_blank">📅 18:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MssxBTnccIx_aNLqGzn5JH7t6pquC7Ij92ZAGhaiFH5hm3YicivOo5RIu9CnLUB-_vSq1w8-C0mbC53JDelWTdfdS4mwdy8gtypCd29fHcXH1uW84Xq1mAmf4xbX6vSKjW5CCoMMzGX3fLGL8wxn8P54zcwJYNWi2vGqo5mOJeu1OuZg-Se6wzrCdIbSomRqxeMgCW8FbWtzIg6bJ7iGGTQ26e6aIs2Ql_Fk6kWKWOGh_kYA5lwdw4YCTO1w0P9nTls32e8wu29yFv-yNQBwtSbOhEMjIAt8zOEIlw8jPsjts4iYW_RDw4lNJRvSICeQuXDo68t65ANEqz32RHqZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موریانه‌های برق‌خوار در چنگال قانون، کشف ۲۱۴ دستگاه ماینر در مرودشت فارس
احمدرضا خسروی، مدیرعامل شرکت توزیع نیروی برق شیراز:
🔹
استحصال رمز ارز و فعالیت ماینرها به شدت به شبکه برق آسیب می‌زند. در شرایط کنونی که کشور با ناترازی برق مواجه است، فعالیت‌های غیرمجاز ماینرها عملاً سرقتی علنی از حق و حقوق مردم به شمار می‌رود.
🔹
استفاده غیرمجاز از سوله‌های صنعتی و مراکز کارگاهی و کشاورزی برای تولید رمزارز نه تنها بر روی شبکه برق تأثیر منفی می‌گذارد، بلکه باعث افزایش بار مصرفی و بروز مشکلات جدی در تأمین برق مورد نیاز شهروندان می‌شود.
🔹
شناسایی و کشف ۲۱۴ دستگاه ماینر غیرمجاز در شهرستان مرودشت در یک مکان صنعتی رخ داد که این اقدام نتیجه تلاش نیروهای حراست و گزارش‌های مردمی بوده که به شناسایی این مرکز کمک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/670238" target="_blank">📅 18:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWolzNSA4p6RojGGSS2nFtRMRsVlVhGURY7lvnX044Um6Ful0cOzRdUpa8n-qIinj6p6i-ZQLFJw5u_3uY2Biot3-bGPzY4xAqV_9a1gX5mOcW-cVRPMtgz_2iYZepVJiX7FnuWnX8xqXx04OId0PLyV6m3FZyB3nGln3VO4Wo4ONaaMrQcaAm0jQdCxJQORbm9BgJav582NLMzU48RK-zhcYQ65urLIlOm_1tWcL99hHdC_vbtpJCAX7BjeOo9UhfoQb5WOxxHztV21FgACU6kezAgeWW8lwuCFagZnzdTRi5654yvKJzznEyUT6Cs2h6t-rTpv61p256FZg18HPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس حسن اردن منهدم شد  روابط عمومی سپاه:
🔹
بسم الله قاصم الجبارین  قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/670237" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mq-3ITn3wntnYYWP1_SIzbGI77R22XtdekqDWaw2j5Jt-JvfZ9Phn8GworW78MtNCcdP7wjDd7sysxkdPUafgE9vj8g7Jq4Bb2WXXUVXHK_rsJeIcTJVqpCAN9jTsUNrMCXHjd_U1Ie4Sh4ZB4JZhP4Co2s3-SunZIz0rZnYBp2ziDXZ8LuYhqHqjXhfZ3oJEQYqwbmAfbw8G7tRAJDuyl1ZueDIjUkWvUSJ1vhSSzFkK1HTzSMVZS56KSdXIKhj_2mQhhaBVJlQktjoWcv41YzGA9aNZS84QnfFujItNSLKpyprLZH7rYN8M7iJBseoWKBTKJdc0EL1Zj-GGqKJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUYPmo0NfeqOEe8eOkj7REDruift6hb7OwVfL2R1L0VI58dBq8cKH1Hnja7CqCGYYff62cc47slczT9ZMU9Yhi261YIy8TysOqOMSi4I9Pn63umSy9L9nIJsDDQfyZ8wy0TwuWeQB7dZclGdlaBfR2TBsGshWESOzBwiGyMeJyg0Fv7-6SKUCAIvyt0vmRW-PvTkzvFzXxp6-Rq1qY-wpeUDYJSUzFZCx-c9ds16H480OATFtrGb2DbkUrPsGoZhz3kCFIx15-1674zjfnsEyXlbukEndmmViYzbC9V8hI30YpfmOyaS35qn6_ais2XXAnMXN_iNEhHFzgQ6_2oYmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qle0xs24S7UIFXqzwVRCvmNjAsogAnOnldOGyRPiBaHQzscyjvib4tE5XPAp1VLtGHheolzxq3yUfSnKvfhseBx49lt7Nomk94M17gWcK9jDHWaQ21mlMrN4ylAXbZMXoHe3Feae-wrP2194gJiE4YrTG7QBazVcKN317bg5CK-IIBoprj4xJ11L3kn61yyp26zpKI7-lkIzVWIg1762vaCsUBU0YmQ_GjafajNrZJS5Eq9CtAFTct5QyvtHgYnJKKNWg06hc5K00j6RuI0ONd-8WNIkWJD84YAkUrmgFDcRfNCUztYG44kJfyx5cbIa2YNk6lCNW13oTrpL_imTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHzaQ2Hs7O5SuwcYPeKWFxOLcWfnyeQAO4jX7ni-jMTdzb1rB2TC1kHH3XK4DGbyRGcXV8eCXS5mCDbzjG_YCVrW-I1tCCii6ldMAg02nKnAm5bfo6k4y5XriuD1lvlmENUfRg90mcMcZ2YvMepFSol-DcN3U5BmVQJWBz7esDpWVLBlsMEctMZiRPnLRUDSUikHsBBGGdxC94ywecDeA1cgb0XUKezb8s_TmtWPcf4CUMrLkoo0BkTnYbtHrOrn4ySG4dH_dQAnf8bJBRwEYGz5TTajCWhcgUuciwzm-IXtz6RiK1Pw9olFUljPNeI3gzWqnAOBsYtxA6ZAkYYGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jp4E9ANJOUcU5-iI_3-1vEBU5tre5lgPxdgYNT8wD-qbnKxILKw3wgNG0ldQXkkXIgHi0cbW_o4jQCPr6ymSh-8O-gktjlDtrx-vFbUam4Hg9RKfkA_vuIDBngp_OTbHZjWKjk40VBUWK74Qs8b7Qs7Xmn8jPIEsnfw7vDxpJxJD1W8_RZmq2RjK-878nt_qNg5w1afPxRzoxwzuiumg1Oa_WN7gxbdc0oin5oIOOqPQusA9_Zkx7eht-Yj9delTlh-8Qk0p43lBGMz1P3G0oEUzHf8lWpICVHDZtRFYGLcWs4F8r4_H9TAECQqK3rSdAr6wJZawQAA8DRNUJ-zgCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برندگان مسابقه بین‌المللی عکاسی هوایی ۲۰۲۶
🔹
عظیم خان رانی از بنگلادش، قهرمان دومین دوره مسابقه بین‌المللی عکاسی هوایی سال ۲۰۲۶ شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/670232" target="_blank">📅 18:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56954cc835.mp4?token=O47dAh7Sozx2ZFajhX9LLaMb3vOPNoRwQv4S6m9zwJBnRhyWar2kfgN-5iq5LGrnZiuhtWxY8XjlW2_xo5Nr-qcQdoDolRO2_ACUyefA59ajKDfJKDvXfCRh09sKY8OSk5Q3HKqvZdpxJOdiU34x0DIDhBO-utNe_vr55I-D4iKfOgNjBiuXpGbcbhPRqVqJq3ndh_WdVDJQ_pxPxrolf2VmncJamQut0b-7TkEqvWVPf_e_5edeH-gqxjWGJvE2S-P2bPMEqXn4GS9LkAHjqDsSJseD7YofsK41o4EHxiSL32Id8Qz3ZoCfMqHb1Nx-x0bWvYBHUCR84VMBRC8-LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56954cc835.mp4?token=O47dAh7Sozx2ZFajhX9LLaMb3vOPNoRwQv4S6m9zwJBnRhyWar2kfgN-5iq5LGrnZiuhtWxY8XjlW2_xo5Nr-qcQdoDolRO2_ACUyefA59ajKDfJKDvXfCRh09sKY8OSk5Q3HKqvZdpxJOdiU34x0DIDhBO-utNe_vr55I-D4iKfOgNjBiuXpGbcbhPRqVqJq3ndh_WdVDJQ_pxPxrolf2VmncJamQut0b-7TkEqvWVPf_e_5edeH-gqxjWGJvE2S-P2bPMEqXn4GS9LkAHjqDsSJseD7YofsK41o4EHxiSL32Id8Qz3ZoCfMqHb1Nx-x0bWvYBHUCR84VMBRC8-LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده حمله ایران به استراتژیک ترین بندر عمان
🔹
به نظر می رسد ایرانی ها از موضع گیری جدید عمانی ها مبنی بر آزادی دریانوردی بدون پرداخت عوارض در باند جنوبی تنگه هرمز راضی نیستند و آخرین اقدامات ایران در خصوص عمان را می توان در این فضا تحلیل کرد.
🔹
در این ویدئو ببینید.
@Titretejarat</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/670231" target="_blank">📅 18:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_d6-GckZiu-e0zz9IJoX-7mMGH2ZQ0A7bTgBua90IB9RYC39xkNoA-2XHs_C3PoRv55GlZq7kYJrsmm69cIfcKd86e3sUQInfZ8jopYkO0TbnaAeuHekYf8N06JYY4MsWnfoe12uVCEWwMIqDo-hPCo3wtGbSsH6ErZ2gbKtEf6KDiFO2Bbe1p8W-3n358C2p5pudOPrkIw5xN5cOnoKSl_Xw1oongL1dxAUeVTiW4nh2tRZUGGIajUwYyv7Gn8CAJrpf_4-cwkcRGg8CIQqG0Z4BOVwrPnBo_GHuZ3LxqSOqHTI1uwvT1OIGO3mBjUIC8VzZr0My4xO5KHN6O0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه های عربی از وقوع انفجار جدید در کویت خبر میدهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670230" target="_blank">📅 18:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72ed07c50.mp4?token=G0OfDzEYm-u6TuM0jACf3vwOem6D0z-YRBbkam4DYHLlJbNXR5kOkcJAr1KyvoSEBcLwDGKqQuRX796Pp1aWvdLG2OWYbFT8yZJdE2mK9xLlgNfriycyayUjek-58igSn_T6m45MxGX71NJE6PoZJ8pLJyU585-W3PEkmire0YJdF6uh-ctNeYUrtSU52uKLfUnF2_uwJuTeQYJDB-d46cWLClcf1klvD3jQs99Nnas3Su7l0GfRSC-T8vDjZmQReqv9tH230K48XCgnrvcUpNerADsyXMxrWrwDBiQBFpmQiY2yPClDJzqalQbOOp1WUajuJ5aooOpXp0lyfLtLlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72ed07c50.mp4?token=G0OfDzEYm-u6TuM0jACf3vwOem6D0z-YRBbkam4DYHLlJbNXR5kOkcJAr1KyvoSEBcLwDGKqQuRX796Pp1aWvdLG2OWYbFT8yZJdE2mK9xLlgNfriycyayUjek-58igSn_T6m45MxGX71NJE6PoZJ8pLJyU585-W3PEkmire0YJdF6uh-ctNeYUrtSU52uKLfUnF2_uwJuTeQYJDB-d46cWLClcf1klvD3jQs99Nnas3Su7l0GfRSC-T8vDjZmQReqv9tH230K48XCgnrvcUpNerADsyXMxrWrwDBiQBFpmQiY2yPClDJzqalQbOOp1WUajuJ5aooOpXp0lyfLtLlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه های عربی از وقوع انفجار جدید در کویت خبر میدهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/670229" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc97d1f2a.mp4?token=eUekQw058VvLeQd6IWrYQSsnNsUZ6lrnmDo6zp_eWxCVtTjz_Dz-TqYHUdVsBh7tGCxwwoqvqbPd0TtBtvzJGQv8Dm3NgCxnwvDaK2cph61VEorJyUo0oxyJLPc0C_ZK2JuzYmHRG5FjbB8efUlIJJ5-SAaDOWKzUCSiX3naKmDt-7ZUiCkwPTGKBNGLAl_sNz-OnqzOqbIj5fueFZ8bpDinDBPs_dwjE0i56K-j5ndTDCrOSIEkhrvZdzza131p6fID1LSe2kcmCNcYxfoKYFmAAUuwoeQBk75TGWLfPkSQ4tiuDiE7-z4DXK0HWfLuPW_Pp_uvhUies5qgfZ4EEpFOk5DyTDGT7wK3fV7EQl6WL8N3iv48HmsRrWJKBpv3YaGfDgJyeVwMkFOLv3LyoLKwXd8qycmWMgM71AR3j0zw3WxrSfFE2b2kvRsKYqVbjMzodiHU4bjQT-NRF0XWZ69MP3NdpKQXx9Q_eOgtgDvCtuAPKlk5XBVniU8AzvU4u5cL0P8QblLgp36hpPn7DXZJxKfyyhFApR4tmNcLzvr6kzjzAXxCH_cCYdkvmZT5cTk51GBePRovSH8d0DFImExKtes06KENI52P5wHXH83PVKwBYKcvmgDPvvrd7bXiDhW-85huyle_9AZb5G79XylNdYyp4UwXb70g-71CFgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc97d1f2a.mp4?token=eUekQw058VvLeQd6IWrYQSsnNsUZ6lrnmDo6zp_eWxCVtTjz_Dz-TqYHUdVsBh7tGCxwwoqvqbPd0TtBtvzJGQv8Dm3NgCxnwvDaK2cph61VEorJyUo0oxyJLPc0C_ZK2JuzYmHRG5FjbB8efUlIJJ5-SAaDOWKzUCSiX3naKmDt-7ZUiCkwPTGKBNGLAl_sNz-OnqzOqbIj5fueFZ8bpDinDBPs_dwjE0i56K-j5ndTDCrOSIEkhrvZdzza131p6fID1LSe2kcmCNcYxfoKYFmAAUuwoeQBk75TGWLfPkSQ4tiuDiE7-z4DXK0HWfLuPW_Pp_uvhUies5qgfZ4EEpFOk5DyTDGT7wK3fV7EQl6WL8N3iv48HmsRrWJKBpv3YaGfDgJyeVwMkFOLv3LyoLKwXd8qycmWMgM71AR3j0zw3WxrSfFE2b2kvRsKYqVbjMzodiHU4bjQT-NRF0XWZ69MP3NdpKQXx9Q_eOgtgDvCtuAPKlk5XBVniU8AzvU4u5cL0P8QblLgp36hpPn7DXZJxKfyyhFApR4tmNcLzvr6kzjzAXxCH_cCYdkvmZT5cTk51GBePRovSH8d0DFImExKtes06KENI52P5wHXH83PVKwBYKcvmgDPvvrd7bXiDhW-85huyle_9AZb5G79XylNdYyp4UwXb70g-71CFgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان عجیب سناتوری که همیشه علیه ایران بود
🔹
در این ویدئو واقعیت‌هایی کمتر گفته شده از لیندسی گراهام خواهید شنید که همیشه علیه ایران بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/670228" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2REeDkWzPpZ0W6vDNgp7IN0p16iZ3IvIWypIik5FovM7B3rEpCCnMon-qkHj6def1DWeaAOBt5-3lj8lG2fXzY8EB1nACGskncwtVzkh1VFTla05MDAUI7BbXpEi-mOYWt4K0G2m0U--aUX45AzjJXPf959awyhSGfD-B6LfKzYEKnsqDtc_tMXwXZKEcXA0SS5CPuPIV7HS7ow38PSNPw_u9WFYaSglJJ1xtsMBaoH3MfwxvdhAZV1QMI6IcGPhFeLbOS_vxFFxbJaXBB8rxzq8w9WEdoZcdaKo22LwbMTjM-BgJ04ob1vT_uqJ4ryFEkLdHpjJ3aWlq0n_BJPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تولید خودرو در بهار ۱۴۰۵ در مقایسه با بهار ۱۴۰۴
🔹
بر اساس گزارش‌های عملکرد سه‌ ماهه منتشر شده در سامانه کدال، مجموع تولید خودروهای سواری سه خودروساز بزرگ کشور در بهار ۱۴۰۵ به حدود ۱۴۵ هزار دستگاه رسید که نسبت به مدت مشابه سال گذشته با کاهش همراه بوده است.
🔹
ایران‌خودرو: بیش از ۱۰۰ هزار و ۷۰۰ دستگاه تولید کرد؛ ۱۵ درصد کمتر از بهار ۱۴۰۴. تولید خرداد این شرکت به حدود ۴۵ هزار دستگاه رسید و مجموع تولید فصل از مرز ۱۰۰ هزار دستگاه عبور کرد.
🔹
سایپا: با تولید ۲۹ هزار و ۸۰۰ دستگاه، ۵۸ درصد کاهش نسبت به دوره مشابه سال قبل را ثبت کرد؛ کاهشی که در گزارش‌ها به عواملی مانند بحران مالی، ضعف مدیریتی و تأخیر در پرداخت مطالبات قطعه‌سازان نسبت داده شده است.
🔹
پارس‌خودرو: در بهار امسال ۱۴ هزار و ۵۰۰ دستگاه خودرو تولید کرد که ۳۴ درصد کمتر از بهار ۱۴۰۴ است. هرچند روند تولید نسبت به فروردین بهبود یافته، اما عملکرد فصلی همچنان پایین‌تر از سال گذشته قرار دارد.
🔹
منبع: گزارش‌های عملکرد سه‌ماهه منتشر شده در سامانه کدال – خرداد ۱۴۰۵.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/670226" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7f4b8ab7.mp4?token=BgT4oFvUw4X8-bY8GzWj9wu8PiGBAqiPkLAzZhqnMxiTa3G8TJXs_I_pGOK823928lK9mSueAFAA1nCUA8sdXAMB3p3WLDVnyHDARn9q-nRzsjAxIScKuGzRlMp7IBVauQ2d-u-fV_zM6ydzivaXpMBVqw2i7BzfXMyju6WkQIWpww8bnnCBJVWcgG8EiYGd85i-f7qf3ou2-DyW5XwALetMk6M0FoqU3dxbgUIv1K1jVVkl0iIdlfmCkDGJg70t15TgPSPzsjf4L92AhKBEwWeA5Q_ck5-2oNtSrKfOJpM2FCYkZlovJD36zJGtrZQsemfuS3-AcvpPN13TtAaNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7f4b8ab7.mp4?token=BgT4oFvUw4X8-bY8GzWj9wu8PiGBAqiPkLAzZhqnMxiTa3G8TJXs_I_pGOK823928lK9mSueAFAA1nCUA8sdXAMB3p3WLDVnyHDARn9q-nRzsjAxIScKuGzRlMp7IBVauQ2d-u-fV_zM6ydzivaXpMBVqw2i7BzfXMyju6WkQIWpww8bnnCBJVWcgG8EiYGd85i-f7qf3ou2-DyW5XwALetMk6M0FoqU3dxbgUIv1K1jVVkl0iIdlfmCkDGJg70t15TgPSPzsjf4L92AhKBEwWeA5Q_ck5-2oNtSrKfOJpM2FCYkZlovJD36zJGtrZQsemfuS3-AcvpPN13TtAaNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید علی خمینی همان کودکی هست که در صفحه اول کتب درسی داشت امام رو می‌بوسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/670225" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1404919d32.mp4?token=ZREYezckG4RowQYr7Mb7jtSeTUnvvBi9yMLvTge6B6dFqmA2pOctasxHUmWPJFG4oR8BNcFSdaD6WNX6hxqWCER2cTtGbwBAw3ZfoaO97NYIqnF1t3WTkQrV7xt8WWzA-0H5zveYEuBXEhl9E7AtVmoJwSWjtZCH0UfOKfKlpWNldITCvD749PYAG2aM2wu2TnSYZDJmoIXANrRs1p1HPfIE7Lb7FXHkes2kf36nYWkzvnjYuWr-hdpDF3D05jCxNvb6E9H-aKDpHAxxxTlpPt1RG-0O3U-tXswTsJBzg4nV7Gl8Wwrl2pKdo7P3cnjCc7WZ6s-_x6dunbVJXFVr4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1404919d32.mp4?token=ZREYezckG4RowQYr7Mb7jtSeTUnvvBi9yMLvTge6B6dFqmA2pOctasxHUmWPJFG4oR8BNcFSdaD6WNX6hxqWCER2cTtGbwBAw3ZfoaO97NYIqnF1t3WTkQrV7xt8WWzA-0H5zveYEuBXEhl9E7AtVmoJwSWjtZCH0UfOKfKlpWNldITCvD749PYAG2aM2wu2TnSYZDJmoIXANrRs1p1HPfIE7Lb7FXHkes2kf36nYWkzvnjYuWr-hdpDF3D05jCxNvb6E9H-aKDpHAxxxTlpPt1RG-0O3U-tXswTsJBzg4nV7Gl8Wwrl2pKdo7P3cnjCc7WZ6s-_x6dunbVJXFVr4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نه کین، نه هالند/ بلینگام پاروی وایکینگ‌ها را شکست و انگلیس را به نیمه‌نهایی رساند
🏴
2️⃣
🏆
1️⃣
🇳🇴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/670224" target="_blank">📅 18:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd20ba09ea.mp4?token=lwouZqaIuIAD-55Z7bqljP3enuzRUAFrjEW2sMyZfgag8EaccOhzji-fUOX4l9REPDHUF0G8DA3vsqIdq1Gt7SArNEy8t-YcFPYSscchi-4rnRtPjhXGm54f72Tnqr8vZQPWfVCQ2AV0IdL19DrRrqGEY5BIc99AbciEffVefC-wu3upRAGbMiuKnmL9wSWT4J4UnPtH4IfEUiEFf2X9uD62JQsmK-EvLkqHJ39ub_iSdXWghbufAoiYICZ-XUPDlAtck3rWWdD7k00vKeD7Or0w2lQf3w0-XWdwgB1xigFbv9m2lM05QQULViE7Pw-NshD2J-XTEhmtmuU066wcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd20ba09ea.mp4?token=lwouZqaIuIAD-55Z7bqljP3enuzRUAFrjEW2sMyZfgag8EaccOhzji-fUOX4l9REPDHUF0G8DA3vsqIdq1Gt7SArNEy8t-YcFPYSscchi-4rnRtPjhXGm54f72Tnqr8vZQPWfVCQ2AV0IdL19DrRrqGEY5BIc99AbciEffVefC-wu3upRAGbMiuKnmL9wSWT4J4UnPtH4IfEUiEFf2X9uD62JQsmK-EvLkqHJ39ub_iSdXWghbufAoiYICZ-XUPDlAtck3rWWdD7k00vKeD7Or0w2lQf3w0-XWdwgB1xigFbv9m2lM05QQULViE7Pw-NshD2J-XTEhmtmuU066wcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه ناوگان پنجم در استان چهاردهم ایران (بحرین) در حال سوختن است‌‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/670223" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو کمیسیون امنیت ملی: مدیریت تنگه هرمز از این پس با ترتیبات ایرانی اعمال خواهد شد.
🔹
پاکستان: متعهد به ارائه تمام حمایت‌ها برای دستیابی به صلح در منطقه از طریق دیپلماسی هستیم.
🔹
نخست‌وزیر اوکراین استعفا داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/670222" target="_blank">📅 18:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
۴۲۰۰ مگاوات آسیب جنگ به شبکه برق
محمد اله‌داد، مدیرعامل شرکت توانیر:
🔹
در جریان تجاوزهای دشمن، آسیب‌های گسترده‌ای به زیرساخت‌های برق کشور وارد شد. حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
🔹
خسارت وارد شده به شبکه و تجهیزات صنعت برق از مرز ۶۰ هزار میلیارد تومان گذشته است. با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.
🔹
بر شعار «همه سرِ قراریم؛ قرار همدلی با صنعت برق» تاکید داریم و از هم‌وطنان می‌خواهیم با استفاده بهینه از وسایل سرمایشی، کاهش مصارف غیرضروری و رعایت الگوی مصرف، صنعت برق را در عبور از این روزهای دشوار و گرم تابستان همراهی کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/670221" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c4aed33.mp4?token=hCeUp-KLHWMU2K7Lghvy5zPHIs_H5nwbGquCa5-kKVfejZ0BJML0ay0cmj3GkxqaJHg59bl3rh4I1rfhit9Nr6wmjNVzcRIvMD9_CHkU1CAcfRP5lvmLeq2huTwiJsLQspUVkdWQmQORGVhbQmCPk6kZcg_PeaI5pdvxSC1qCt9lp6Kp6npTsRZZaY5UeV4biylmKtKIqHf58bSX-C-c6-SPnX202Wh2cMjUETsgGFz5UkDm8svo6aHVkxXY8dU3cTasQttALHXWEkyHoZxuSzXiJQ7magzKWxr1zPm2Fo7My89ZkKqvmFUBBc6fIxarsEWpdQDsswv9hY8HL-0LDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c4aed33.mp4?token=hCeUp-KLHWMU2K7Lghvy5zPHIs_H5nwbGquCa5-kKVfejZ0BJML0ay0cmj3GkxqaJHg59bl3rh4I1rfhit9Nr6wmjNVzcRIvMD9_CHkU1CAcfRP5lvmLeq2huTwiJsLQspUVkdWQmQORGVhbQmCPk6kZcg_PeaI5pdvxSC1qCt9lp6Kp6npTsRZZaY5UeV4biylmKtKIqHf58bSX-C-c6-SPnX202Wh2cMjUETsgGFz5UkDm8svo6aHVkxXY8dU3cTasQttALHXWEkyHoZxuSzXiJQ7magzKWxr1zPm2Fo7My89ZkKqvmFUBBc6fIxarsEWpdQDsswv9hY8HL-0LDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این زن به اندازه صد مرد در سرنوشت تاریخ معاصر ایران دخیل بود
🔹
بی‌بی مریم بختیاری در دورانی که زنان در سیاست حضوری نداشتند از ایل بختیاری برخاست و در انقلاب مشروطه با لقب «سردار مریم» شخصاً در نبرد فتح تهران حضور یافت و جنگید. در جنگ جهانی اول نیز با تشکیل…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/670220" target="_blank">📅 17:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز به CNN: دیروز با ایرانی‌ها به توافق رسیده بودیم و آن‌ها از همه چیز گذشتند، اما ناگهان دو ساعت بعد، با یک پهپاد به یک کشتی حمله کردند/ جماران #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/670219" target="_blank">📅 17:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c908f091b.mp4?token=UolssiFge3mT2-YZEvTtPuYAJi1JwqBVmEkV5EY972E8KO0sfi19F_9roaZbP8JlKpOSG87IZELkPqwZNXLggLEMOHbfGm4xgYo-8m3XpBz1MVwPC_d6R-9PMO6-V1AVSBh4WxuvtfLuA7ip05WCoUDgh9IebpRoggiqqT68yAy56_KC91jtI29E98WL2_hOT7oGp2cTfv_vwi-uZ_2xDnyw1ggAkt-j4hik9C1ZKTZinknKG_i1wXo8Vea6bvwJ_1ycrkbaDKBQBOE2a995suhFS_vtOl9f4pWO8NwrE-hGqzK9eWq1D0n6PSd9yHGgQdrY0bbcjdzdrhiEMkc80Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c908f091b.mp4?token=UolssiFge3mT2-YZEvTtPuYAJi1JwqBVmEkV5EY972E8KO0sfi19F_9roaZbP8JlKpOSG87IZELkPqwZNXLggLEMOHbfGm4xgYo-8m3XpBz1MVwPC_d6R-9PMO6-V1AVSBh4WxuvtfLuA7ip05WCoUDgh9IebpRoggiqqT68yAy56_KC91jtI29E98WL2_hOT7oGp2cTfv_vwi-uZ_2xDnyw1ggAkt-j4hik9C1ZKTZinknKG_i1wXo8Vea6bvwJ_1ycrkbaDKBQBOE2a995suhFS_vtOl9f4pWO8NwrE-hGqzK9eWq1D0n6PSd9yHGgQdrY0bbcjdzdrhiEMkc80Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره جالب و شنیده نشده از حضور سیدعلی خمینی در ضاحیه لبنان همزمان با حملات اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/670218" target="_blank">📅 17:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تعیین تاریخ انتخابات پارلمانی رژیم صهیونسیتی مشخص شد
🔹
طبق اعلام شبکه ۱۲ تلویزیون رژیم صهیونیستی، انتخابات پارلمانی این رژیم به‌طور رسمی برای تاریخ ۲۷ اکتبر (۵ آبان) تعیین شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/670217" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان در پیامی درگذشت امیر پیشین قطر را تسلیت گفت.
🔹
۳۰ نظامی ارتش مالی در درگیری با تروریست‌های القاعده کشته شدند.
🔹
اردن: اقدامات اسرائیل در کرانه باختری، فرصت‌های صلح را تضعیف می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/670216" target="_blank">📅 17:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d813b27d3.mp4?token=ZL6w05ns_spuE7QRUSqrKVPtqtK6H09tK6iefbZ-hpKTs9zxxwQj1tau3mjAM8sQFzluIdFHA7zOvPmnoKW9J56Fpy8k6WfvXHi3RVMwuEX9mtS67vt0SsecICMTO77bT2X9lZjKbG6rsg8O0csDODwTexd6s6dtvmJB-vVP8hLGf68XiFNC4SpDXyCjsa9ecYKjUYFzDn6nBut0KD-TM44hLkMDj8D98JjtkW1vmPHpE1o0AP3W6DbUJq5g0_5hRdHK9kWUPdla7JzjfOky90fqaq27faaNYeIQbbh_4fMyGz6As4vVWaczejS0WxOKUlAeuNQe-Mwk8LNB6zHnWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d813b27d3.mp4?token=ZL6w05ns_spuE7QRUSqrKVPtqtK6H09tK6iefbZ-hpKTs9zxxwQj1tau3mjAM8sQFzluIdFHA7zOvPmnoKW9J56Fpy8k6WfvXHi3RVMwuEX9mtS67vt0SsecICMTO77bT2X9lZjKbG6rsg8O0csDODwTexd6s6dtvmJB-vVP8hLGf68XiFNC4SpDXyCjsa9ecYKjUYFzDn6nBut0KD-TM44hLkMDj8D98JjtkW1vmPHpE1o0AP3W6DbUJq5g0_5hRdHK9kWUPdla7JzjfOky90fqaq27faaNYeIQbbh_4fMyGz6As4vVWaczejS0WxOKUlAeuNQe-Mwk8LNB6zHnWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی هولناک از بمباران غزه توسط ارتش رژیم صهیونسیتی عصر امروز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/670215" target="_blank">📅 17:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ7tiPSC_EKfnridDXxEXQjpcmJEm8tJklChdo6OKvHpuhJleEdnqliRnQJG0G9ss6JuA9Of8iMDhoXuyrlqOYjlSC7bHwWgAT-IxR_WJwztvPhOPqxcTLyPDLK5OCASthXOcLGjhuaqs8LNMA_jmbqlBhvaUrK33CBk94IFEQ0ICC6RdHRxoQaAHDkZumxDt-inJDjXYSUADd66z3T5VkKD3A1e_KLkHRX_5HvbDaAtkM_eUHpYLjzJBNenxX11JTIxMm79uzs7Ip8zmUevXHEDV8fEPruckfMnUhP3her-Su8p8mmOSUoFXbfqXQNsQpcWqK_N87eQXWocVDPfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمان سفیر ایران را احضار کرد!
🔹
در پی پاسخ نظامی ایران به تجاوزات ایالات متحده و حمله به پایگاه‌های این کشور در منطقه، عمان سفیر ایران را جهت تحویل یادداشت اعتراضی احضار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/670214" target="_blank">📅 17:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر انجمن تولیدکنندگان برنج: حدود ۵۰۰ هزارتن برنج از سال قبل، فروش نرفته است
مسیح کشاورز، دبیر انجمن تولیدکنندگان و تأمین‌کنندگان برنج در
#گفتگو
با خبرفوری:
🔹
در مردادماه ممنوعیت واردات شروع می‌شود و طبق قانون ۴ ماه طول می‌کشد و با توجه به بارش‌های خوب در کشور، پیش‌بینی تولید دو میلیون تن برنج را داریم.
🔹
حدود ۵۰۰ هزار تن برنج سال گذشته در گیلان و مازندران به دلیل شرایط تورمی و رکودی کشور به فروش نرفته و ماندن آن تا فصل بعد، خطر آسیب به محصول و منافع ملی را به همراه دارد. واردات برنج تا ۲۱ خرداد به ۱۷۶ هزار تن رسید که نسبت به سال قبل ۵۰ درصد کاهش داشته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/670213" target="_blank">📅 17:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArUma06abV3mTwsTJ6wayLcOvFZtXHFxaZkCXrCanFTDrkHZwcmsyZmniXyDPmmVpuRetZVoPwVeVDXW1E-Lev78qe8D92n8f3Ql9bQhjpRyj5Lyi-nu1-mhMHykahaDuwL_gZty8F0ypJfQwMGqAqCvhRk_5dsZCFlPlwoL1Bn9NEGIA2r6ZTbtTq2L1EwyS7hbrSrkqD7Di3gROeINZMXSGJ0aGKsJ6rVk3WUvs9_FTkR7Ux7JiJXcHE7gOFc58-6x3QrWo_xu-96hWPyZZ_aMXRPTpJ2Dh9WrZfX3MQprsRKvKSsuzSRM7881zG_qHYjqhrESDi2vRXc9een1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندسی گراهام به مقصد ابدیت اعزام شد
🔹
کارتون از: محمدحسین نیرومند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/670212" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574a85bf98.mp4?token=RNhhj2Eecf7PST5WQ84qdKZX2AvK4rOqgiwjs8mdSCcvmxpJxh9-e3S4VHYblQ7jJMdyXXW4nMNeap8hsYfDUiZaEW6cVXA9sHaMhoOwUsp-VQrJpHgFLL4VPGER8mEe53CVnnUJfifycFDnkPh4oiDvmL6d5jGPNNsIzKRdgwkWEXfnkMSe7Mqu0xr_4VmexjRiQLnIvlo0x0UF2xfyU7aizVzYSJDKjRLMwT66C_76xEliXPBoLgK7NKJcLYRMaCJ_Bzxj0zphdaqj_s3UtnLWwsRXH1em2aOjM1-_6I88FICY0YTLT8jWzKdH4aSBdg2y0K3d3rmPKhQguC-6mTUofj9_54FLoAvSzvbMoTxHsrkBg7GjvecTncMNwl-TA040i8F7e9gjGVA1ymWCIbo4xbtql3AjV1LD8mX8o6-bbX-Oln4kel1nfPrEeZwa7AzuvlEG9z4oKt2no69LFtCq6ODWE55hYp9p-H3-q6L9jP2iCjt_-7FhkLFBU7Y3Qo2YZJBE8-qJq-9iMKl-wzs37WFlTeuK6F3YfmU2WdYRpmH1Ox7c3OP6vhFQUE4a_ugPf39Paez42XmxzIQ0UZGa8T7q8wwAK33Vs_HXQDvOQaj2pOOW2hTM9tOKn3OcYEP8iG8_yFPRRPSCRLFmByCJhNWBx22UjDkUettpolY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574a85bf98.mp4?token=RNhhj2Eecf7PST5WQ84qdKZX2AvK4rOqgiwjs8mdSCcvmxpJxh9-e3S4VHYblQ7jJMdyXXW4nMNeap8hsYfDUiZaEW6cVXA9sHaMhoOwUsp-VQrJpHgFLL4VPGER8mEe53CVnnUJfifycFDnkPh4oiDvmL6d5jGPNNsIzKRdgwkWEXfnkMSe7Mqu0xr_4VmexjRiQLnIvlo0x0UF2xfyU7aizVzYSJDKjRLMwT66C_76xEliXPBoLgK7NKJcLYRMaCJ_Bzxj0zphdaqj_s3UtnLWwsRXH1em2aOjM1-_6I88FICY0YTLT8jWzKdH4aSBdg2y0K3d3rmPKhQguC-6mTUofj9_54FLoAvSzvbMoTxHsrkBg7GjvecTncMNwl-TA040i8F7e9gjGVA1ymWCIbo4xbtql3AjV1LD8mX8o6-bbX-Oln4kel1nfPrEeZwa7AzuvlEG9z4oKt2no69LFtCq6ODWE55hYp9p-H3-q6L9jP2iCjt_-7FhkLFBU7Y3Qo2YZJBE8-qJq-9iMKl-wzs37WFlTeuK6F3YfmU2WdYRpmH1Ox7c3OP6vhFQUE4a_ugPf39Paez42XmxzIQ0UZGa8T7q8wwAK33Vs_HXQDvOQaj2pOOW2hTM9tOKn3OcYEP8iG8_yFPRRPSCRLFmByCJhNWBx22UjDkUettpolY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارلمان جدید سوریه پس از برکناری بشار اسد نخستین نشست خود را برگزار کرد
🔹
۷۰ عضو این پارلمان توسط رئیس‌جمهور خود‌خوانده سوریه منصوب شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/670211" target="_blank">📅 17:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f554d0b6d5.mp4?token=JyiGNDj5Mu1a_aCh1aCuZpGxNkvCAh6oyC1KFeG98XPJK1FDtB2g7lXXCFho9o5o6xAgi2C_4tdhYrvNlwEPZORR9UFIkeoPRhuo2Cxrjeu_dFQPAjlonsDpQo1vy_MNaD25VP7ZrwHP6z_GJQuoenCV9j4C3QI2omHhlbuT-hCWmK0fMGuPj6sGmucohW34uO_Z3q22i0twNNEIgihTaUjvFglE2iZQ8gA83JhINDQ2TxIwI3N6fucrkd0w-LhZndfvCwVc3u3lhXViT0YVW9CqJYm1cDYD9Z33zPsL0fpLxTDC4Tya6G8FX_zzDKBKZ1PvYqziy4_JcoEVAjIi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f554d0b6d5.mp4?token=JyiGNDj5Mu1a_aCh1aCuZpGxNkvCAh6oyC1KFeG98XPJK1FDtB2g7lXXCFho9o5o6xAgi2C_4tdhYrvNlwEPZORR9UFIkeoPRhuo2Cxrjeu_dFQPAjlonsDpQo1vy_MNaD25VP7ZrwHP6z_GJQuoenCV9j4C3QI2omHhlbuT-hCWmK0fMGuPj6sGmucohW34uO_Z3q22i0twNNEIgihTaUjvFglE2iZQ8gA83JhINDQ2TxIwI3N6fucrkd0w-LhZndfvCwVc3u3lhXViT0YVW9CqJYm1cDYD9Z33zPsL0fpLxTDC4Tya6G8FX_zzDKBKZ1PvYqziy4_JcoEVAjIi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک‌هار درباره سناتور به درک واصل شده، لیندسی گراهام: دقایقی قبل از مرگ سناتور لیندسی گراهام با او صحبت کردم و به جز خستگی، حال او خوب بود #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/670210" target="_blank">📅 17:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzP4QmwecrcBxkw34w0cUH6RHW4ulBr6TgWZBt_6Sc5Z_ntck9xS2yzFhDGKkGmDL0a-U4ybCchtfviw_nzC6ute068nqd-Tj6zlDdxwo6L56_Ovhs8ivzfJFp9wbBBoSE6kgsnWpF09upwI36_FaTBaUkO-pWhHIcNwIC6kAXuNJuh746A0nOS3ycSigI-aAkxrKPf8TAmIv5lm_mBz4V0dCaX1KGkAcWlOf-nXfFjwZe0Kf8JzGo0iw9r1rEzMFcAawaFnfaVqh5KK2a2XxIXZEppH5YiUKJ_S2eKIrWnzzMw-m_x2Zd9Wk0xlQqznLOeyWXnAz16cWcjSPgpCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQ53ES0KjEbRpyuSSXui1S5C3riF_AhFo5ryTu15AAQBL15yfMCfpYhJ7KsoRH1jmbHJDfjw7saaLEmtQNQvwEhjt4GNrBGQ9j070dNqAT9pg4R525hKbFfdNxVA5-ArjHrB9xAgmlPyKfquf6q_dR9ZeL9rzbyVixdLiU8WKrif2YP9XVhGhhY-6OcMbDOE8EWk41AwHYiMzE20nque17sW863Zx8pucI72fki3b9duQjFusSc29j_rZbcdT57-iF7rZhmfX5bxwWJhXutgwzFIGX9BzkFE_gCm61wEgtOWGEAYbIJ3Ts03DTtlvsmSFz4F7Gz-_la_8yfAWEYRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp3C7Zv7_eFuhKfXzBftGsphWEEfWGDiTe56OIMGQCQZe7bi15LpUpfr4JkFsNy_viomwnV19vdTaUqKXiSPKzu6P1qBeiu03MvO2pLMMSYGQ1QamVKOP6rkptLOPqiQzsEFuhKbEBf85Sp6lT1nQgN9bW9SNSME1m3Q8ZiA7JwIyeSPM3mq4m1p4xibpPVYKGOnPCQw0ryDSQoQxFcE7W1hvfmreXnyNhipcE16nTdY50YkT523-GdYm20xYv9OpJSgc95rt7SNGP4NRclcmE98vXQLYEYz47RCKDZyq0yRKoABP7xJl3eJcLs8NbYq5miF2_c8u_5evN8IdVHoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wp6j-TSbpBnaZ4yhLWH3zwlX27n1o8Dmkl1CSQPU_V5eGairFGTSb8715xay-oK3hppDI1iBIlumWKF3Vx3fwltNUXnViCuUEiSD0ws2gHPTP1fBY-ha3qNBssMOkCtTOt9kY0KfVXuk1t0FvRaQF8kXu942y9dJADfwvwLuGT3jmfn6Q_2600oAYyLw33yElo8mOTsT_zD5_NpjWxDxIUCKMH1I9Dk-HX0CHOt8zPdQfDLwXe4YqhkVd-QLyhr0ymb11iRCWbrmihOnRsdol5JTO6g8P7vaaTsDlT7G51r8csniGriSpv_kuR8Kpj1MfzKjE7kRYt8o05Bv5aotww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYAsEL-G7W8NL5z8XhxxIiN_YJ4Q-2Gh4t8WE_IXgffo2C08sjIMof0HCp62id9b4MTRGGls_5MvGdLiP_KSQIvtKVihIIjcc6GKaWH52bajWdOnwjtoYUbNs2V1lVeuWbYzqo7w_lZkerRtWg7R04Oq25Or07Q0DTPCoxbZh8QQuKymi0F-A6HkdkpMREQCOGKKd11GszpWoz_5u2EgJ7BHHb7ZayKnG8Cuauo-jcp1oD-VxYkXcNyVWIySf5Q9NmRrJ5eu3KVj7soSb3aE3tHU2j7VnBHrD1Brix9LZyrUdIxgYDcXRSCHM6-wV8NRjYlWQ835oHR0HhFix9-WQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7yQW-U815FxL82dF3LU4efAhj3b_Zmz6ZVIEUBCznNXvd32ZK9kNFZwaNOMMK-ZJ7IJM3q0U1zraJevJu0vu89_sSGZQzE26tfEuiZ-fOYZDNILvnTAoKg24Rp2uBTVFsLrg0DAiOhVqZYTKha10GHIZ6HQ5p_FWYb6NPWzZ3AJxIFswFh3pA-HcCMbdhHxtwHc6-MC353aPNP6CgAxdt_3s-SByOVXu0qb8VBurZA-CwEaGH3aoyAwAI0L1mnqF_u0Cjytu-dwCFd5ao79Rr5mETj-Pb7TzP3BN6DdaUFjU-pAqI5nGIq9ayZVPk2k1tnahYOuSvAotm1uvPHwVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تو هر سنی چطور به بچه‌ها آموزش سوادمالی بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/670204" target="_blank">📅 17:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در مصاحبه با ان‌بی‌سی: تنگه هرمز باز است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/670203" target="_blank">📅 17:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: از ایران در برابر تجاوزات آمریکا حمایت می‌کنیم.
🔹
هماهنگ‌کنندهٔ ویژهٔ سازمان ملل در امور لبنان با عراقچی دیدار کرد.
🔹
زمان ثبت نام آزمون ارشد علوم پزشکی ۱۰ مرداد‌ماه اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/670202" target="_blank">📅 17:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در مصاحبه با ان‌بی‌سی: تنگه هرمز باز است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/670201" target="_blank">📅 17:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318bddf9e8.mp4?token=vg1FKyGpzFq7pf17p1SIJei8x_r-1ri7zIV2B7h4km_BiXH68_U2uwdLmnW-1cEdt4-hZ4PyX74Z5MzWmN1HxFT-MQAHdBtOHV5sxF_DKllM3NgWhH-ex9BW2lZ23ea3Ou2JOn6iqw1TPEC65I3gpuERgBignF3ii0nXTvlVVM5-y1jqMtlJFa7gFw4MHnS1PedC_s1J2Z_cJEnw7YgEsaa0L3UNu0Uyi_egSLl24UkxFnK6PqY0mA3EOxC45GeJ1p12I7AV_4LLYQ0LPGWM8fqqwa2S0sA5fFn19LTGnP-wCMat7RvkGGrAxldujH6OGiFXT5j2emOynODKwtujbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318bddf9e8.mp4?token=vg1FKyGpzFq7pf17p1SIJei8x_r-1ri7zIV2B7h4km_BiXH68_U2uwdLmnW-1cEdt4-hZ4PyX74Z5MzWmN1HxFT-MQAHdBtOHV5sxF_DKllM3NgWhH-ex9BW2lZ23ea3Ou2JOn6iqw1TPEC65I3gpuERgBignF3ii0nXTvlVVM5-y1jqMtlJFa7gFw4MHnS1PedC_s1J2Z_cJEnw7YgEsaa0L3UNu0Uyi_egSLl24UkxFnK6PqY0mA3EOxC45GeJ1p12I7AV_4LLYQ0LPGWM8fqqwa2S0sA5fFn19LTGnP-wCMat7RvkGGrAxldujH6OGiFXT5j2emOynODKwtujbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین‌پاک، کارشناس جبهه مقاومت: اسرائیل در دو روز اول پس از تفاهم ایران و آمریکا، ۲۰۰ نقطه را در لبنان بمباران کرد/ عملیات اسرائیل در جنوب لبنان به هیچ وجه متوقف نشده است/ از لحظه امضای تفاهم ایران و آمریکا، روزانه ۷ نفر توسط اسرائیل در لبنان شهید می‌شوند/ دشمن عملیات‌های بسیار مهمی را در روزهای اخیر انجام داده است/ ۱۱۰ روستا به طور کامل نابود شده‌اند/ آزادی عمل کامل اسرائیل در جنوب لبنان ادامه دارد/ روزانه بین ۱ تا ۱۸ بار آتش‌بس در جنوب لبنان نقض می‌شود/ پایگاه عظیم پهپادی و موشکی حزب‌الله را در مجدل زون دشمن منفجر کرده است/ نیروهای اسرائیلی علاوه بر نابود کردن خانه‌های مردم، حتی درخت‌های زیتون را هم آتش می‌زنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/670200" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d9cda664.mp4?token=ogTRYJk9xVPcQaxepkpBQy-_N5a22_jyGb4ZOVevwqBACq2uN9_XEghC5WrTarkktzflXAa3GpXBps6Uaf0UDUmRKAsky_pfvgnn-dfb7YDX9cSFEzyu8MUdL6JhhvQP4elgh35hVPfZtkTq_w0142rLlAglP7zdkQPRF4YiITIhcBRLDz8NJ5OOkgwqipf7DiEBcobuC87CMBZuuic3GMR7CWWmgcxv8GIeObbWcUOjvcBlxLTEB-Z8Ks7vKRtduIwd9S5woWzSXhwuWPFZHFDuKc50PPi4PjYEbXu1wgM7WzV2foUGI8PD83yHtNpUb5fMG8zCJZj2YmKY_HzUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d9cda664.mp4?token=ogTRYJk9xVPcQaxepkpBQy-_N5a22_jyGb4ZOVevwqBACq2uN9_XEghC5WrTarkktzflXAa3GpXBps6Uaf0UDUmRKAsky_pfvgnn-dfb7YDX9cSFEzyu8MUdL6JhhvQP4elgh35hVPfZtkTq_w0142rLlAglP7zdkQPRF4YiITIhcBRLDz8NJ5OOkgwqipf7DiEBcobuC87CMBZuuic3GMR7CWWmgcxv8GIeObbWcUOjvcBlxLTEB-Z8Ks7vKRtduIwd9S5woWzSXhwuWPFZHFDuKc50PPi4PjYEbXu1wgM7WzV2foUGI8PD83yHtNpUb5fMG8zCJZj2YmKY_HzUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سربازای روسی می‌خواستن مسلسل چرخشی رو روی پایه ثابت نصب کنن که این شاهکار خلق شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670199" target="_blank">📅 17:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL6DhRURYOXjTnj5mBYznmjWSSCYPPBErJ-43ISGeYmS581Hk0SR0GcYIw6JzvXee9v0CA6gjrpoC6p60aZOfOUWlvhcwKUGXPlJslj5KjVUM_1r2drKrmbO64hpJlPM5KORtNZURzkKuPuto6jBNWkEUp98In7v7DNCRnjkl7aqTmQkbIGhpCapBhKeBV-Onw7FaPyrvQq0U14grpOfdym_4YKsR-VgUIKR63OMCPvVcGrk9iZ7RemGjcFsX1bBm9v6eDq34mVoJDxO6uYhym2izG7awzbV4hiBjaupC-WKef-CDlHlZcNDm0WickIi3rnziv3AJqDrg7UpAAfuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان تعویض قطعات خودرو
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/670198" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOl8bHAEo5WIGzB0uicLAn2_b20c1yRjbkYD-AA77nc3dRIpGe4bEiTEk38ZH1cOzHz_HREOCd6sr_xXYgpOMGgQ8U_xj-VJO_UAK5ekMC2E-xLKWyd_5StF6EFXpL3xVf0IrEIX3LL1CHvmCr3Pe8zIvcOHhwSRaVre8kR7M3FR4MgNXo1hLTU0jkcFZWxojmq-VnBUU0iv1-UE26FL568mmp0JRk46KmSOVluYjOyY34yh5b-zJSRsvCgljxPaJlXWOBCUckKO7nK7xM6QNZhAmN7c8b7KmZUPOpqzhQ1jYQvcL2XnkOKhBD5AWnp9DcxIv30zjcVpfZyP0_ZYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه تنش ایران و آمریکا به پایگاه‌های منطقه کشیده شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/670197" target="_blank">📅 16:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f220d6adaa.mp4?token=UajPgFywHUr6CLmhenGykiFyLows8jMMZ844RwyIhTYSwOa5LZHpGPsTfyBhTic1SMJvc8iqDOdmwvmGYdCPlYQO9W87Z-j4qvZR7JLDwsvAA5lCEQa5BAsjx0l-nbq5CrzzSqZn0ZsTrDLLCKS3qeBP1qwpExcvP-Q-JDeeyw5edCgfaZqMhfyvYrGkFwovOsscS-z6h8IBiFRN201jqfAvKcUpFcavw6SgoRu4_8ZXzLUwbg4sXE4raDLJrGDGSomsHXgNfr2_eEBgByQkyZ1Ky5NrNBz6D3esvqXlr28xQcCL2pIjRcqIQqHSngMIUGXPW3eIyn5KK7vl0K57Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f220d6adaa.mp4?token=UajPgFywHUr6CLmhenGykiFyLows8jMMZ844RwyIhTYSwOa5LZHpGPsTfyBhTic1SMJvc8iqDOdmwvmGYdCPlYQO9W87Z-j4qvZR7JLDwsvAA5lCEQa5BAsjx0l-nbq5CrzzSqZn0ZsTrDLLCKS3qeBP1qwpExcvP-Q-JDeeyw5edCgfaZqMhfyvYrGkFwovOsscS-z6h8IBiFRN201jqfAvKcUpFcavw6SgoRu4_8ZXzLUwbg4sXE4raDLJrGDGSomsHXgNfr2_eEBgByQkyZ1Ky5NrNBz6D3esvqXlr28xQcCL2pIjRcqIQqHSngMIUGXPW3eIyn5KK7vl0K57Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهو: ما برای جان انسان‌ها ارزش قائل هستیم!
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/670196" target="_blank">📅 16:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670194">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هیچ برنامه‌ای برای مجازی کردن کلاس‌ها در سال تحصیلی جدید وجود ندارد/ عظیمی‌راد: امسال به‌علت مجازی شدن کلاس‌ها، شاهد افت تحصیلی شدید دانش‌آموزان بودیم
احسان عظیمی‌راد، سخنگوی کمیسیون آموزش در
#گفتگو
با خبرفوری:
🔹
صحبت سخنگوی اتحادیه صادرکنندگان گاز مبنی بر نیمه حضوری کردن مدارس و دانشگاه‌ها در سال تحصیلی جدید صحت ندارد و بنا نداریم چنین اتفاقی بیفتد.
🔹
هیچ برنامه‌ای برای مجازی برگزار کردن کلاس‌ها در سال تحصیلی جدید وجود ندارد، بلکه دغدغه جدی مجلس و وزارت آموزش و پرورش برگزاری کلاس‌ها به‌شکل حضوری است.
🔹
امسال به‌علت مجازی شدن کلاس‌ها شاهد افت تحصیلی شدید دانش‌آموزان بودیم و به‌دنبال مجازی کردن کلاس‌ها در سال تحصیلی جدید نیستیم.
🔹
مجازی بودن یا حضوری بودن آموزش کشور باید توسط مسئولین مربوط به حوزه آموزش بیان شود مانند شورای عالی آموزش و وزارت آموزش و پرورش که مرجع هستند، نه توسط اشخاص غیر مرجع مانند اتحادیه صادرکنندگان نفت و گاز که مرجعیت ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670194" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670193">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bee4a4b5f.mp4?token=eRBDalgqyRdVNdF84XPG2E6mqLJxlHDWqM6hN3orcRC0AGgT2ni8gRMYDYuQ9wzrzh67nwK4ZZRjUeTx_8DxyQIZRpV62MRcZ-zm-7nnlYG6Ej9MErDUvruUZHsJ7TDHU-3GZBxNKw39JGQWqReXAfbtbQloWZFGneklCKoybOumGdKNOfcolxAPVbaNIPVdG2WD7-LG9bspz4V1_-0WWnkb5BIp_mBz7UsMnVc8-Rlp6smPiGY6-ikJ5ILjUDnzFNilPG92puEkhwHfV7XU4Dkvb8C-Kq5wccUkMwiOpbY2IVk1pFPE5unfEeQzmFXcjaXIaxxaNOeTgEsH8Bf-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bee4a4b5f.mp4?token=eRBDalgqyRdVNdF84XPG2E6mqLJxlHDWqM6hN3orcRC0AGgT2ni8gRMYDYuQ9wzrzh67nwK4ZZRjUeTx_8DxyQIZRpV62MRcZ-zm-7nnlYG6Ej9MErDUvruUZHsJ7TDHU-3GZBxNKw39JGQWqReXAfbtbQloWZFGneklCKoybOumGdKNOfcolxAPVbaNIPVdG2WD7-LG9bspz4V1_-0WWnkb5BIp_mBz7UsMnVc8-Rlp6smPiGY6-ikJ5ILjUDnzFNilPG92puEkhwHfV7XU4Dkvb8C-Kq5wccUkMwiOpbY2IVk1pFPE5unfEeQzmFXcjaXIaxxaNOeTgEsH8Bf-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم‌های کاخ سفید به نشانه عزاء برای سناتور ضد ایرانی لیندسی گراهام نیمه‌افراشته شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670193" target="_blank">📅 16:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670192">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFdC8eIERPGxwQePXAsFEvvMWF0X8ik0XzHEv_iTPaCDJf8dbsmMwNlet-HLovCflleZ47_WrNyp_lcMZ07ysNr2V1HUYnpg-dO21gDqaT1R9UAWWrPvURaCfjQiP6dPFLeE-tNDBmNbRRoEFOQYdUEcpc85bwg6bjZ_6ZCi-Lc5QYYvHzwTh7ys-p4kRQ0a_OsnGcz6aDy9Ga_VKMDWJKbAW3pDNxsZQXenWFV35bDWDfAzn6Mej9EoqcZ91ulFgy2F11EOXHLQ-OcJTJpYW2AbYpL-YPxGNZvoofN7iS2eHqFUtgw6dCFbY-GThnyjIEJrq6CFwNmEWEaUCDFjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوبتی هم که باشد، نوبت مسئولین است...
🔹
آقایان مسئولین! مردم مبعوث شده، کارشان را انجام دادند، حالا دیگر نوبت بعثت شماست..
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670192" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtYYeEq1nwNGECVkiK99IZPOBvR01wNcdXheWddAbFyaHYDaFz0fCwWi6t7Wisavqb2xdxmASVq8OAufyaWaZUOyI90yLAQLPuRvqHBlR1LPD53Hl8q0S5nwvU5qzizTyfkckjdzgclYJFV699t2f0Vwj4cenTe9q9g9LR74ld03f0e8e4-gAxcwH01x-j3OP8JF2dguYnx-jF3DUqq1MON8KQBwqd0O6oMrEhKT1E0tRQHwqcsMQsCLAhWEfCQImvL_VAmXXLU7sUh-qyAw9XQTnPzyLXpNsYifkriRLWHpaMb0QLqE6Kz3LOwbiFPUgiRsKEksLSfhpaKtnsm4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZad1Mfg6kDCyEiRyiqokZTJXKndj8eXyTwQxJMqL_ah1n0qazhz5qM5mW8Vm3Aep-nRznLf5tzPRUaSAN_9W9IFrctxf3ieCgOei2mmkQO9glPUXLRhZcEF2B9Vrp3JRdcj23Ql4wiWcJYMmiHycGCxQFh4IRvIZGJjgTJ7llZI-2iCPBvCu43ikWt8adVKNAuMtVgasfkrkyX5doWiZV3QFqOfJfJwqAlXoovMuFkCGW1s_15NWHE5X1ppQDg-31MZ_-VgIdlcxvyz5arl5KjDL8AwxxFhDWv2spGBefVhaCicqDaeiNWb1n6ccxU7abgJlk_P1VEMqQ-PfSnOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sT7eStIXmCp-vkMfmErbebGCSo7RVrgBc9DaeRF6OgGmq_I9m-taufrLYGiLJNkIFNu0vaavfgdRW5kri1tHnYQXeGP9xF5Rb6Qj-Nsqvq0M0qtosOUPqeUXMc4VwMDCqD0A6Jzd71Qj0PzML7pV24FwjtdIw1VRxFqfe582hvNePko7MGkRjao8PU_DQvzaJYkJwpH0rJ11NC9sixQkuYMI8vvjsR_sryOBRtwjnDF2pQiduMvdeHt_7QyFXTE8LgNaYyQAp_bH0yqWBKQWeAVAvp-S5Xwck4Y_KM2mp59nuiQ-DIhGWc5wNiqRNe8WUSAb6R0uQ0Z-Lt19m9kDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hY0lq0lzJ8IXScIJ-Wzv884s5S8nxwHZnF4u4iajgbTztAoljBkZJeFJQ4uDT3xCeByrpBs0LUPAkOi2hQdiiKGieUGZxSHsL40tjYvPHse1tiqOv-Rn0Cy2c_iv7wqAdNDQq2Uy0XxCYsn835y4fl2zCLvg2m7ZCclvzppVVAnpjEYiTy3IVyjbiu2djwUtiveOW-HlUvHTqIGZ-fmdeeijbWxc4XOmMluapW_LfVmrppEr_K0JUqO_Nvo5tvO5MJn2WEP7Q4jewUtwl1YHPZMOcs_YcMpC_k1kTp9Bq6QjM7Z-BTTIxPlmY0iih6YEnsLFqcnEpr8beyTYq23RAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVJFiGjmM2AYtGUSnxgtHWVDOpb95kOO0Gk8m7Py2ioFW1GlVAaCKbRnWxtFQYrc3D-C2ElEPLH4MC-I06E4k3aBLp3yPqJ4YpfY-jY1_QbL5qfIVOBWKPck-YgOzu_TN66ia_tCtCBYYlL6lnskuVZbleR67chDnzEYniEvdK423oY8_gs4u30DkCV647gDVsTVZaw420-dFLBHEFiDvA6bjt_Pfq84enNGcplsjbbBj-rERnATFt_DowrRDDM2CoBMsk1YiFVkWAIpRvgzhnOBNMDMkqGBE3b7CoSv-q_rAciTPxzLoXAe_TsUwkoM0MI0cnvz4_JX18aICGMl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmcsnCBNFPZzjOh4l_sLSjmqo6o1fTkYqNyuGy8-oH8qqTXYXuirWw__Ft4M9bhg7U_eAquQ8EwHZlX7c_C-mnnhb8fSuIU6SSdD_7k7WoCSArrC_uWawVnzIOREPiwI_DaveNZJ6s79fnT0V2cMZbIeWmr0A1C8IqUbq1tuBw0FqGoNLNopsEOw2vWIgBZsRLvhSJ60D0y_9fjcCSLkiQho9N1g9QMKLI5qIdlvBOtauw9xYhUOVn1_7CtlQHE9PC8tSakmF_waG4-ryiOUd5vycY1Sl2HnpXRF9BSUWmNR3SYvWHeFNsob_5-s6DZ2QwnROTFfM9DWEt6OC8Lluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MudJL2ma2Z1zr3Pif83ncmnw3zfjG4LaPvR1LuD7DRsmqcoP2Tk8gdkvb0RzzAf2DOMYFYLX5gMmZThDHTHSE_nUgNOHeGWDxFSUxqkjKvQKHizOKMmLCBeo1qVcRv4jhcOIksQFx3VYv-YZjvjW6n4NKcV2tLP-DpyJUluVVj8-m2AOBIrKUQO4q_m84DTBMMHhdkbThSL8MmDy4us-mdrNnJ-lZe9aCHJhYoniYRroqGInZky5ZEDqup2pU2v46Bp00ff2cBocy_V1wjO3jGUpPDVHy2vYEhuwiDSeHglVvhZSSpdL0eA7TPU5y7iyaBm_fBvC5xPLdcdc2kbW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKGcNyK6eSsjwTubZH5OiPhNxfyd-iIbVP4xswhBTDivLTlvvooUOzKhowFaNy7T8_Yt6J3nVEJWIsKVK58Dhc2DvtXmIflfB6JvmrFAk_wf9toMKXCH85pKwv0f3iii6alBU71HuGsEJdMMZm1uDTWTr5RwKVhlO474JpceTns-qHuxlMtohRS7jZ2daXgMgUsj7qpk9VG8_Ru_rbmFxvC273GiTJl2hXL8oCTn3E58E28Bim0FYDiBlgHbmVCathBv2sJ2s5JR6DLoqnn4IzvshIId1Vlnpu6kvLP9PmSJbhY1EHGUp8lu57bMdT7zhRRRDvX40vfQ5ib0Hzihkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBx3MlTJL5odHinUTRlz4lMfoXM4RzuI2qosx4-LCc1NdgIvbs_9M3ByHaimsLqEJdRA0-GRZw0OafRbx_mccq73cq5EhWyhLYhZSnwhYIzz_SWwSnSD9q8fwzCo4sjjX0NBzY6ZOQe39sNp1NuoVMztmAp4JdMECSfB7Cd448tYWYkjUPpOtOSlRq2RB-Ez0ULlYBZU1-ecM9E2YxlwFmTLF5urlzzEcLskG8tcxcDjXrf_M1didyPw9uGAIK4QU0waiHr6_3FRC7GDbFtW4j19swgRo5R-Z-rTlyOETnZXJU83SkujpQW0URHAbocYBbvS0QOgZ1SrY3w_XtTpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byF8NGYGHg6XYV-DTdJxxedlFyYUB_b0o5pAnnrwfqGEOLT_edGdcqO7gTFGdR_s9YEIHsohPOp7Vc4BkP-9Mq0KJNRD1P6j5jQP1UKl0mnpTGaXn_iR6ZqSL04vifyALvvyxTk4UR-srvqtra1-yXDgUyX6ZtiIW0VEo-J_qsVymBif5qLw4g0oH5sAGKUzdydSQitrfBgJ6fSF9pUUxGIkjZuPvTYwne0s553SQDfoJ7-qjxJVCzJniQKwU_-S_3eLT2FHwemF4pzyF41I6V71KOivLkWaiL99YKVlrqIbDd_Mc9sz1Am44kIUwyPnXLcb-FK0KgnGMVQ-lhp2Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور زائران عزادار برای زیارت مزار مطهر رهبر شهید انقلاب در رواق دارالذکر
؛
حرم امام رضا علیه‌السلام
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/670182" target="_blank">📅 16:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ارز اربعین از بازار آزاد گران‌تر است!
🔹
با کاهش قیمت دینار در بازار آزاد به ۱۱۰ هزار تومان، نرخ ارز اربعین به نزدیکی ۱۲۹ هزار تومان رسیده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670181" target="_blank">📅 16:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzafdWgJ68FspjguBrQ9ByM4ZGG4BGQJLzXJs2IMaof_uIDaDmRCTAD5lpsJ7hqN7ePwtdoJ81B6hD6HORTubLYKZOwsfSGHCW3oWbyB9iMs-EgIwcitwz6EMcFleftZfHDLXN3lLMCAZwzYurXUXC8CPZFTLu7K3YYTn6SG74AUaHxmf8E0Xn9XnQEdSV4MGHuJlLx8IkB7YAyZtUMuIlrHlsByg-1ZK4GXXTOEAePvNfOAhTn2rwciEmEYEgkBDcsuy_vwUoM2cTcO6l6qb70T928jD-CyTlUDFcHfsvSEbRayLaKR6WXirPr2cz4NTdKlw5qJvUd5Tbp8eE3Zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پهپادی اسرائیل به شرق لبنان
🔹
رژیم صهیونیستی در این حمله، منطقه «البقاع» را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/670180" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngJ0Z_uEUNcCF1q7ChqDlZT5TBtMTMSCKs7oVxlQbPUyxGCMHakswrv1mA3CxPobX4cW2QNoOOXM2plXgD_VY-AqDDLNTM-9NDm2bywmZNXFAcM5HJ8cfxCy5jWeCrYXIEmN-6YcYlFHPv9tZwrNccWQDfcanu2TK1TbEkoDJ5hjivmBDFWogAOzKWoEHl3afG-jwYCf2V4yDHcT5_gCMK89fdj99pZQbGD6zvG8ojDzsFrXO1eNcMnFn00nTPB5cZJirMp3cVRLUjRUtgTMMHMXs_tSrK4YC0o0YSpb58DR6BulOS5t0by_4HZvgfdCgQf-XHTGnHdPHKBAOh0lEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یک کاربر آمریکایی به مرگ لیندسی گراهام: یاد و خاطره بیش از ۱۷۵ دختر ایرانی که در ۲۸ فوریه ۲۰۲۶ توسط آمریکا و اسرائیل کشته شدند، گرامی باد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/670179" target="_blank">📅 16:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884e6e97fd.mp4?token=h-d1qw_YuF6TJW1_2RTHhq0tQmnqvRvymv59-6jKyRkItk9EeEuWV1O4FYuWs21dHiTsg_3voUBZVKdWsc2cm9I50rhC1yAZ1u5TQHXMsdVFHmT8DxTGXMY47t6QaBKsjJyW8umFKaukF22T4QZ7TxIva7gbaaisf4N2XOyLE2_s9sMR8450ZgG9AApvbdGg5hyhJA54iIa6zmRprrPm3xyFZaVHkmd9jBd5BpVC1SMb7vIx5xg-SKakkAWiDUzFfRbcvPMiKDtUQQuTR1_bCOVJCg-F5LmednVE1uWYyU4PcnNn5zNCrGhA3hy_T5gEp8uKDaZPOfyFpKzq-sBkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884e6e97fd.mp4?token=h-d1qw_YuF6TJW1_2RTHhq0tQmnqvRvymv59-6jKyRkItk9EeEuWV1O4FYuWs21dHiTsg_3voUBZVKdWsc2cm9I50rhC1yAZ1u5TQHXMsdVFHmT8DxTGXMY47t6QaBKsjJyW8umFKaukF22T4QZ7TxIva7gbaaisf4N2XOyLE2_s9sMR8450ZgG9AApvbdGg5hyhJA54iIa6zmRprrPm3xyFZaVHkmd9jBd5BpVC1SMb7vIx5xg-SKakkAWiDUzFfRbcvPMiKDtUQQuTR1_bCOVJCg-F5LmednVE1uWYyU4PcnNn5zNCrGhA3hy_T5gEp8uKDaZPOfyFpKzq-sBkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی بازسازی شده از قنات اختراع باستاتی ایرانیان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/670178" target="_blank">📅 16:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddeec753ed.mp4?token=KLbCGg0CZ9EWaxOhu9r9bifQpLtHyp_psD8yeVTWRy8oeYYG_W-jgYQEVnbJnVwInL0tzJZ8WfB6vU_xnvc3FJcqLvnNAoZuUu5zTcKVQ2NpeGHn7mmzaX_fOOtbbwLTO9hDbc8VCvGd7cyLDhFlwyO7wQzPymwJ6_qoYr2qd6bR6BbftMRfTNhsb6b5V6BRS4jVqGwScNoHWWf-79UmnRm5pTo1gHKTY3_ekUnBTh8uvJrzgv5ZiXnnwy24C-N3XZEyUMEh58j_XnbpY2-9poHfxA1WcgbQ7sQ9Y8PJs7yUjo7rgku2UB0VZisHWpzj49H4d1lgTGizPIZ0I7QoI2H7i-pdSUaa3cbgC6s3O640Ufpm_SgGp1jLTmVW9pu-oct2fX9lBkb39ERFU9kUjuDRJDBsv2R6c2WkPu5UKUeIaihVZ7uaCmeqoyP7J5LEZOGnYoCXWupt2jyoDmyBc3BajXBsrZ1HQ9hqgxnhi9aaHdyJdPm94NhC2R_HsrBLiH1lWubTqwGlBRuSH-vFWaghsf_92wPpnSqyvwntdNwSJ1UEpAX2m7hZngKZ_trMwYjfEy9zOQTWbIPQn-griNy33_y2WyTpuV6ELY-oh4S0QcAz964AXya81BBFXX4fuZ8tXWPj1uuBiWKnombNAgikqKHpwbtF8cay3S_oVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddeec753ed.mp4?token=KLbCGg0CZ9EWaxOhu9r9bifQpLtHyp_psD8yeVTWRy8oeYYG_W-jgYQEVnbJnVwInL0tzJZ8WfB6vU_xnvc3FJcqLvnNAoZuUu5zTcKVQ2NpeGHn7mmzaX_fOOtbbwLTO9hDbc8VCvGd7cyLDhFlwyO7wQzPymwJ6_qoYr2qd6bR6BbftMRfTNhsb6b5V6BRS4jVqGwScNoHWWf-79UmnRm5pTo1gHKTY3_ekUnBTh8uvJrzgv5ZiXnnwy24C-N3XZEyUMEh58j_XnbpY2-9poHfxA1WcgbQ7sQ9Y8PJs7yUjo7rgku2UB0VZisHWpzj49H4d1lgTGizPIZ0I7QoI2H7i-pdSUaa3cbgC6s3O640Ufpm_SgGp1jLTmVW9pu-oct2fX9lBkb39ERFU9kUjuDRJDBsv2R6c2WkPu5UKUeIaihVZ7uaCmeqoyP7J5LEZOGnYoCXWupt2jyoDmyBc3BajXBsrZ1HQ9hqgxnhi9aaHdyJdPm94NhC2R_HsrBLiH1lWubTqwGlBRuSH-vFWaghsf_92wPpnSqyvwntdNwSJ1UEpAX2m7hZngKZ_trMwYjfEy9zOQTWbIPQn-griNy33_y2WyTpuV6ELY-oh4S0QcAz964AXya81BBFXX4fuZ8tXWPj1uuBiWKnombNAgikqKHpwbtF8cay3S_oVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای هوایی از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در حرم مطهر حضرت عباس علیه‌السلام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/670177" target="_blank">📅 16:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1aa1fff0.mp4?token=B1w2ErDdJQ2Fd8c5B3fkwFJiVyp_bIMWvX9_SuNQifrX4SCxBlx5gs9xVFjDTW80QSdvFun-mq4qT-ktIpiU1uSP8v5G9H37NqxCjjjwZtNblVa46GwyxIMUTHSvNgjAKfZQ3BP-UahiOlRAr0tuWSgG8s-3Ex6ACpCtZvMwbL74_nZB82-JwCFZnjMuv9YY3vBezgD7JgjJcTgKZBDbXW9KQUqyh5sXqmK-Hlc32qYz1ofpuPjE6zW-3YSQgPqVNN5v0q-S0jD1bwhyPh35ZxC3NGbY_mcGwlfZwvotDk4bEVHcGv77rTI5r5d5L5rngMHj__s5A37LnTJUlS4VUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1aa1fff0.mp4?token=B1w2ErDdJQ2Fd8c5B3fkwFJiVyp_bIMWvX9_SuNQifrX4SCxBlx5gs9xVFjDTW80QSdvFun-mq4qT-ktIpiU1uSP8v5G9H37NqxCjjjwZtNblVa46GwyxIMUTHSvNgjAKfZQ3BP-UahiOlRAr0tuWSgG8s-3Ex6ACpCtZvMwbL74_nZB82-JwCFZnjMuv9YY3vBezgD7JgjJcTgKZBDbXW9KQUqyh5sXqmK-Hlc32qYz1ofpuPjE6zW-3YSQgPqVNN5v0q-S0jD1bwhyPh35ZxC3NGbY_mcGwlfZwvotDk4bEVHcGv77rTI5r5d5L5rngMHj__s5A37LnTJUlS4VUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین‌پاک، کارشناس جبهه مقاومت: تمام سرمایه مقاومت،‌ جنوب لبنان است و باید ایستادگی کنیم که اسرائیل از این منطقه عقب‌نشینی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/670176" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCIaWH7BSaew-DcvWJ9VjvI4Wfv-ytOf8gDrS75pkDme9mTj1g45wEsvP9gd2alxsGN-XVf_TiilSNyhl_qMi_FKFB9Q-YgfHYe-b4XBWKZgBd00XEAP52UpdYkuMTdBF2akZHorON7qTnnnzSutol530E0_qoSojbfpwGRwM4QOHG3IFcrR1eqr-VF-CnF6sD_MZqC_oWzFhXE7um1l0G7G_foLoavsa7JPkRcUlb9RLEiskeWXReDlRt74q4VA-HjdFjR9vlB0vUqwa0J-dSGuYSNm3bfpdlSAnCQ1Gt9Qajh7xBYokknp-Nf45roz3SC61x20J5pE1uFt_MJptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: تردد از تنگه هرمز در حال حاضر امکانپذیر نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/670175" target="_blank">📅 16:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9l_QrnVW66H2b4-k4aNICtror0GBL5lu6_naxCo4xsyHQNTZQ4t6jGORw3CWxKDnK_mynFFHp1F1AgUSdUZ5XM0pijNJi45bN7OI8D4M4CAY1nwZd1v2G89Ir6ya7rI_qvBNo__h-TmqKyu8XppDLGEW5D-POGITn7FVBBI26uCdU8UVvek-Y5dcvCyAo1GbpChL08fZE08ejr9sepVZKLP6rl5xVBPMBizDorSkoSPa3qXRxsqKkHnPIz_4XwOjG1QdHN569-oaKVnoVga2-Dft61QhCrdsBdLLbc10St1ybl172TcE5bImmxBt5uzmEx4fku4AvR5CPnrfSh4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار آمریکایی نزدیک به ترامپ: سناتور گراهام یا توسط روسیه یا توسط سپاه پاسداران مسموم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/670174" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTwFWsi8TRzSQ6bJKm4mhEYLzAvmNtTB1g1eJVoKOggq5ewt7IGA_GhG36lvIQx3nT57yhDmvzhl8Ng9WysIkeUG6A-ty3T3f6U6SkReTZptQHQ6s6N0T25BS_wYwcr7oX0CkfxL-Yke5omimROuJRChkjb0c5Milb_bLOdZrwpOXiAnNq7-Z3ekyHdzDIilE0UEKXqCVKE40pMs5RHemuIAwners1w4QEW-jHxMyie0IuMh4qlQU26CCw7pw_10zqEh3st9LYYtv_kr5wVczCSFO8cWbHTP-0H1PloErIgiY2hm-V0ahi7ne8LOGm8slZoaUYa6iBZE-Xn2NrmWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ کاربرد دوربین چت‌جی‌پی‌تی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/670173" target="_blank">📅 16:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovlo83cj6B9idSYLv71kUEIJy1UJz9vl0AFSh-nK2EUwdFTponq22R3ZS15fkgYW7XXZyXUs9ORSTI46_0A4sAH-L9G6JU8aKmWTd6sSGbuhu-2E5iLReWWvYW_pfxExmul8DlkWV4ABTFSB0eoL1k1_oD1Vw-FdshYyXjAk9H5TIoVia71-UxhjZgD0kRlZTZ17-FI0R8lMm7LXdsl5MsgKXDO78jtSUksYylFFX77wI4g6ePJYBUjDmRBm3-w_Y7_RZbETgAPrA9D-kKOTrTYI7e3WZ5usv7lqAjjAM6rgBuDLhQm_ccMGP7o6a0oIsgcKul26Pccaz8d_czdJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رشد یک‌ساله «ونوین»، بیش از دو برابر متوسط بازار
🔹
میانگین رشد ارزش سهم بانک اقتصادنوین در یک سال گذشته، بیش از دو برابر متوسط رشد بازار سرمایه بوده است.
🔻
اطلاعات بیشتر:
🔗
https://www.enbank.ir/s/mfa8Ef
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/670172" target="_blank">📅 16:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff98719558.mp4?token=aFyIwSLHeJAI4QzAiSqPErvHRKsTqsMArj4V4cWci7j52dGrarvAfr2kl29gEj9Yv3QW4XjiFv29KaBRls4D-0aukWqYNcUJdLoVC7RpqZr4j0MAHNSS_D0K8DFPzj2N9D3hXEFCWSRdApe8ksRr5vLzV2dPG-QmqU5wg72blo5Xds2hWoc4wDbEwXOmu_Pl6ywYj2ypCoZjlAOmW5hncjpQjQqYrU2Lk92vKqN0za_rR4Lfk6LwXIoX1SmRfF2TQlARziMM9HbxW0nC7u1vJrDAPI54BmEaKDsBv3hAHH4AM1--8KwUDwRNVfvCQl1X_TFU-vj_A_bY8ufNtZ4efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff98719558.mp4?token=aFyIwSLHeJAI4QzAiSqPErvHRKsTqsMArj4V4cWci7j52dGrarvAfr2kl29gEj9Yv3QW4XjiFv29KaBRls4D-0aukWqYNcUJdLoVC7RpqZr4j0MAHNSS_D0K8DFPzj2N9D3hXEFCWSRdApe8ksRr5vLzV2dPG-QmqU5wg72blo5Xds2hWoc4wDbEwXOmu_Pl6ywYj2ypCoZjlAOmW5hncjpQjQqYrU2Lk92vKqN0za_rR4Lfk6LwXIoX1SmRfF2TQlARziMM9HbxW0nC7u1vJrDAPI54BmEaKDsBv3hAHH4AM1--8KwUDwRNVfvCQl1X_TFU-vj_A_bY8ufNtZ4efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در جنوب لبنان بر اثر حملات توپخانه‌ای اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/670171" target="_blank">📅 16:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b33f1c3c.mp4?token=daMMHrKlWmiyob5qLG5TXcK8JRtRjgarEKUrTAFRkaUwPYELmnQOZNpH1Lnv_NnybulUFqy5VazOfnhdZPgd9FtMHqrvVtKVE3AkoAz-v700tr2Rq9KiRLv3z_K1CEtxcd4YrehXIco1A4eTJzPFoWbj6yMoKnu1wBxI4M_DUwc2Zs_2vnPuKKB5ohlsxGFsLirp8dETd54p75eYjFlRrwa7_qn1zVJsT4kGv1xwdEpuEuODses8gy90n6ibZuvesN0y7raVnWeJWK3UyOVfmGRCsImvgwpRD6ClQWPPNb58oHBGCuOdhtDkdMRzsrAKxF9UcH9fVuT0ERcV-Y6fOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b33f1c3c.mp4?token=daMMHrKlWmiyob5qLG5TXcK8JRtRjgarEKUrTAFRkaUwPYELmnQOZNpH1Lnv_NnybulUFqy5VazOfnhdZPgd9FtMHqrvVtKVE3AkoAz-v700tr2Rq9KiRLv3z_K1CEtxcd4YrehXIco1A4eTJzPFoWbj6yMoKnu1wBxI4M_DUwc2Zs_2vnPuKKB5ohlsxGFsLirp8dETd54p75eYjFlRrwa7_qn1zVJsT4kGv1xwdEpuEuODses8gy90n6ibZuvesN0y7raVnWeJWK3UyOVfmGRCsImvgwpRD6ClQWPPNb58oHBGCuOdhtDkdMRzsrAKxF9UcH9fVuT0ERcV-Y6fOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تکنیک خیلی کاربردی و آسون که توی سفرها به دردت می‌خوره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/670170" target="_blank">📅 16:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: اگر آمریکایی‌ها به درگیری ادامه دهند، جمهوری اسلامی هیچ مشکلی نداشته و آمادگی جهت نبرد را دارد
بهنام سعیدی، عضو کمیسیون امنیت‌ ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
با توجه به سابقه بدعهدی‌های آمریکا و همان‌ طور که رهبر شهید و رهبر جوان ما اعلام کردند، آمریکا قابل اعتماد نیست و ثابت شده که نمی‌تواند به قواعد بین‌المللی پایبند باشد. هرگونه اقدام آمریکا با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد و جمهوری اسلامی آمادگی کامل برای مقابله را دارد.
🔹
نیروهای مسلح ما در اوج آمادگی کامل هستند و تجهیزات بسیار پیشرفته‌ای داریم که خیلی از آن‌ها هنوز رونمایی نشده است. به کشورهای همسایه هشدار می‌دهیم هرگونه همکاری با آمریکا علیه ایران، با واکنش قاطع تهران همراه خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/670169" target="_blank">📅 16:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفارت آمریکا در عمان از شهروندانش خواست در مکان‌های امن پناه بگیرند.
🔹
پولیتیکو: ونس ممکن‌است به دلیل نقض تفاهم‌نامه ایران و آمریکا مورد سرزنش قرار گیرد.
🔹
محسن خلیلی، به‌عنوان سرپرست تیم پرسپولیس انتخاب و جایگزین افشین پیروانی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/670168" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToMratPl-n48hjYpCX6z9aCEnKq4TKj3tgw-V5VTH-x5Xm3tY8nflfwd7MXKgI4V9PJdMArNu-IFlWUCEWWXMsfcB8QtNlRx49uP5RwBc8xm_RtgMBw_x6KRZdhxuKBs-FjTungZK7r54k6ci8FU4PytzklpsHnYcd9ObUmls7OLfz1HimXATWOfJCZMWkPNeRHnYTtKgCQwPHBfyHwTLGWHlm7KLnhalVTkfAiEOflHvr5fiobG3PAyCgqTxlQOFVXCQ7Ra45MbF2hoIScikAxEGlzMQdskJolNxjHQ5TBEO3LUhJqKqhXMLv2mCSldHhp40zx7_rGwLlrcDK5fgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همدستی اردن با آمریکا در حمله به ایران
🔹
داده‌های رصد ناوبری هوایی هم‌دستی اردن با آمریکا در تجاوز دیشب به خاک ایران را تایید می‌کند.
🔹
طبق رصدهای هوانوردی، هواپیمای جنگ الکترونیک نیروی دریایی آمریکا از پایگاه هوایی موفق السلطی برخاسته و هواپیماهای سوخت‌رسان هم از اردن به کمک نیروهای آمریکایی رفته‌اند؛ یک فروند هواپیمای گشت دریایی هم در حال جمع‌آوری اطلاعات ایران بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/670167" target="_blank">📅 15:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hrsh3m_waJ7miItb6ML6-blaK4T3pUFALnKiY4xosUNPrs5Xou_njguHwg2W5y2B2kvlE7U5LA5o4xe0OmqUtZAXCRY9FTcpSQoFwGvWLtppXqOEMl35F-FNSnsFh34PxqXVgzIIL0jUOZ93MN-n0zJXyYF1XMUuz6tv3x1ypQ-K_c1fzOURUq4W8yE_2ociig0pCJj00RAXyIuuXgP1VE6w9dZ3wMedzvmLWkKOWK8uJ1d5rAPujhafWuGJld1q5F05YRd0Br5vW6p3ZvQoZxyhxRwg_F4i7YUEYpoIOnMU1bcJgLrumXsrdFpbqaDKacSVp5bXxg2YgproJpligg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سنتکام: تنگه هرمز باز است
سازمان تروریستی فرماندهی مرکزی ایالات متحده (سنتکام) :
🔹
تنگه هرمز برای همه کشتی‌هایی که مایل به عبور قانونی از این آبراه بین‌المللی هستند، باز است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/670166" target="_blank">📅 15:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9aa6be20.mp4?token=ScjY7-uz359ANBTgVTxC6x7dewaditRQPHRIEr0A8Z9pt53um7se1CTpCOUeF7QZ9Qt0kN66dhZxiAf4azigObotI7bHstIHZbnUQRldcjK5TwlGPPeiPQBLBolpzMhkL-UoMRR-H3fpGJyftZtxAdP8EtIQ72g49FmfzBgOZDsXeApr3Js-G_NnHvItC8rlHKPMcvdhQArrLjAWVFQIhcvfOnFPYUsLsfDb5csA2Mg8dLsUv4iEYtDIUZq-tt3Wt3gZbzTAknVZAJwtdnNBzp9dkzmq1_k1Vfu3VQZBntsGlE6teGZNQ2dZE9Lsd7ezFtsWQBlTwSBAsSFSjPtEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9aa6be20.mp4?token=ScjY7-uz359ANBTgVTxC6x7dewaditRQPHRIEr0A8Z9pt53um7se1CTpCOUeF7QZ9Qt0kN66dhZxiAf4azigObotI7bHstIHZbnUQRldcjK5TwlGPPeiPQBLBolpzMhkL-UoMRR-H3fpGJyftZtxAdP8EtIQ72g49FmfzBgOZDsXeApr3Js-G_NnHvItC8rlHKPMcvdhQArrLjAWVFQIhcvfOnFPYUsLsfDb5csA2Mg8dLsUv4iEYtDIUZq-tt3Wt3gZbzTAknVZAJwtdnNBzp9dkzmq1_k1Vfu3VQZBntsGlE6teGZNQ2dZE9Lsd7ezFtsWQBlTwSBAsSFSjPtEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با اینا بوی بد غذاهارو بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/670165" target="_blank">📅 15:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455123f5e1.mp4?token=lcfshIK0L3BtFn-LO1hqQGs2z1UPMzGvb4qHXyYb5Dypzp7wd5JNeMrviKNA9O2LQaMpC5pO_aTCExXocOZf0l8D83hzpuxZQPJ-4MecYO8kK3onaT_oyMbv-fOEvYM6-Z0PWFQkAan_Cl5YEx7y3eBb_5bb0x4gkCfzYCwzR6yMBiqfkKmJGzmg4Nly0hV4ScmMLOd4NXb845a7hFrwuoJRcyl2WvS264uTdkUIV6aYgy61-1o82wWUGbOtLPMKR6D1uz4A5crUbC1-DYfffjzu8WcV01Lh4hDh6Y2x1OFzHy04JHFBtxFhCvRF4b33ZiC1amLxwZ7bZ3jDWiKXS0G2x0cLC6kXymZkDsvhkArLRrQy8BgOWfL1kuDM9rmJ3GkG-Rct--5KZI9EnBt4LJ9yuN2HeS86cbhhGYsA7-BlWlq_Dvb6n3lS3xY5g4udI7jfhrXcXCtSvtAFe-3TZaLWAM0Af_axq_ValOpl2Db6ov_eBwzSh88T3VHiLxcVO1ybhMnIzXUEYgo2byS6qD8acjcwdbPeLGKoIAcKnYcQbgyyYrsbjrqOHJpS5Za5rzL9NCrfAqjIOm7HadeGrJ9h_YSNbn53H9vV6UzAkwIj4PFjheqkPeyHpk-RVvYbVBshrXu9xxcHma0hQj-0VGYEr-0B1JadGsKyyOcqOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455123f5e1.mp4?token=lcfshIK0L3BtFn-LO1hqQGs2z1UPMzGvb4qHXyYb5Dypzp7wd5JNeMrviKNA9O2LQaMpC5pO_aTCExXocOZf0l8D83hzpuxZQPJ-4MecYO8kK3onaT_oyMbv-fOEvYM6-Z0PWFQkAan_Cl5YEx7y3eBb_5bb0x4gkCfzYCwzR6yMBiqfkKmJGzmg4Nly0hV4ScmMLOd4NXb845a7hFrwuoJRcyl2WvS264uTdkUIV6aYgy61-1o82wWUGbOtLPMKR6D1uz4A5crUbC1-DYfffjzu8WcV01Lh4hDh6Y2x1OFzHy04JHFBtxFhCvRF4b33ZiC1amLxwZ7bZ3jDWiKXS0G2x0cLC6kXymZkDsvhkArLRrQy8BgOWfL1kuDM9rmJ3GkG-Rct--5KZI9EnBt4LJ9yuN2HeS86cbhhGYsA7-BlWlq_Dvb6n3lS3xY5g4udI7jfhrXcXCtSvtAFe-3TZaLWAM0Af_axq_ValOpl2Db6ov_eBwzSh88T3VHiLxcVO1ybhMnIzXUEYgo2byS6qD8acjcwdbPeLGKoIAcKnYcQbgyyYrsbjrqOHJpS5Za5rzL9NCrfAqjIOm7HadeGrJ9h_YSNbn53H9vV6UzAkwIj4PFjheqkPeyHpk-RVvYbVBshrXu9xxcHma0hQj-0VGYEr-0B1JadGsKyyOcqOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
چهار مدعی ماندند؛ فرانسه، اسپانیا، انگلیس و آرژانتین؛ حالا وقت جنگ برای فینالیست شدن است
▪️
قسمت دوازدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/670164" target="_blank">📅 15:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjeO2YRzKdXGiVh_uDbuIs8QDmzFwfsmeGIHfmPH1mMBzwtWBEUVcYX6Ro4ZHbiHMNKpHDUu4fJczRDG0gpyPzmSB5K8sUsrn4nC_SsIh-jRRIYk5kfYtuc17qyCe5B1Mm4ROrIhcOqI4I630oCrz9RYJNJp6q5A2WKxkKGjawt9xVJ5nB5lph6byAPmJyV8MfZZMvTEJm-8qQ8SZmkVZHl_Pcd0T3COlO544CtCOFhcbjvviyaVGtvr350pGQdmFk9m9EhZgOxgg5eTD-DxXAzwS5OlTAVFwWw7nrViCuFoe8UBoTX7iu4WmWYVi0IQXfDA_WxqEmNVGTu-FiVT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روغن موتور پراید طلا شد/ ۲ تا ۲.۵ میلیون تومان ناقابل!
🔹
قیمت روغن موتور مناسب پراید در ارزان‌ترین حالت ممکن به حدود ۲ تا ۲.۵ میلیون تومان رسیده است که با  اجرت ۵٠٠ هزار تومانی تعویض روغن بین ۲.۵ تا ۳ میلیون تومان تمام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/670163" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d45d752bc.mp4?token=B4EkOGgdg3bY2caeLF9lGMh82TXJnzVgUd33-Zt04HFnSZvIdDUw6wzmXHXPwbNvT5eWb5ZYwLYEqbHf3kVySIKlf6BWboxFW_Dh1SrKwr6jKUsyxdSHQ9hLs63Q0TfXp3qK9dplQaLHMycCmAPbTB4RNiex6Xb972356ify3dd7Tz9EVr_b9z1uAT4vHY5dIzLSLtCkfAul_QpMSjbyV1ele3yb916xNBnkoc1qW31CnzwmbGsfDqX41sH4hAo_KiiwE5DHBQo29vN6H7l4DssUXJsL0lFbnaYkke7yyU4ucdSq-2dQifTMmPu976YCakuFZEDqJ8D9EHiX3ox8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d45d752bc.mp4?token=B4EkOGgdg3bY2caeLF9lGMh82TXJnzVgUd33-Zt04HFnSZvIdDUw6wzmXHXPwbNvT5eWb5ZYwLYEqbHf3kVySIKlf6BWboxFW_Dh1SrKwr6jKUsyxdSHQ9hLs63Q0TfXp3qK9dplQaLHMycCmAPbTB4RNiex6Xb972356ify3dd7Tz9EVr_b9z1uAT4vHY5dIzLSLtCkfAul_QpMSjbyV1ele3yb916xNBnkoc1qW31CnzwmbGsfDqX41sH4hAo_KiiwE5DHBQo29vN6H7l4DssUXJsL0lFbnaYkke7yyU4ucdSq-2dQifTMmPu976YCakuFZEDqJ8D9EHiX3ox8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال اردنی: حملات ایران از اردن تا عمان دروغ آمریکایی نابودی توان نظامی ایران را ثابت کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670162" target="_blank">📅 15:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue7Z1AaidKoGpmd29RFuTVUKDcvf2EN_x-BtMHdu72IYL4TsKAMzWaQ-VhS6DflOOqvdP9_-bPFgI4BbjjNVAjmaqq77DM4TqeSD1lXc6EOt8NizwhawYWVjEz6AT7Kna82f1h8g1sdGpipF99V3n_LhMtUWHDoBrjhp4yQo67I42W9dVcRBeRDf3jcVfb6HUz18HPZt0Fg57yugS5BfryzhkZKsR3FkPjy8UakwUE5tXQZ26gY3yrxy0DOX1sS1wsDT6JtwYgFpKiTqQ7qaghzRLMcz6KTEebGL-Y4h5oCmv5JZrtPj-NW23qEsy7s8gO1kySxDX9FuxHNnP5v1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: علت مرگ لیندسی گراهام دیدن تصاویر میلیونی مردم ایران‌ و عراق در ادای احترام به ‎رهبر شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670161" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAwFRL7p4cnlTqgoWQ51SsM7hQsUK269_8o4LHJshYhUd4jScQ-7cz_OVcQYjPnyaFJeHamAHElEH5EK5_zCCN0ibnxr-83rnIGl7NJWmcHZsHi_jpoYEgU_aYJPOyhoDGmytCOnlIMoWkyGNVZ4WTGKpbYFuh_RQhsMLyygf2A9vau66rIFWpqK11v8OGxdOQEEAiiPGdX5hyDfDoWLUD5fos35o4S-9cvkIw0wuBSwEqt3kEbywFYnh4BVoJpQWCa8mJlubbtqLEIlFvqIjyuqV8C2XtbyJ9BO4FB6dQlEaQngyr8jcQ4aONPeL5tHE8Uwt_DANAxkSYxTPudtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود سنگین پول حقیقی به بورس متوقف شد
🔹
داده‌های جدید جریان نقدینگی بازار سرمایه نشان می‌دهد پس از دو ماه ورود بی‌سابقه پول حقیقی به بورس، روند بازار در تیر ۱۴۰۵ تغییر کرده است.
🔹
در حالی که طی اردیبهشت و خرداد بیش از ۶۱ هزار میلیارد تومان سرمایه حقیقی وارد بازار سهام شده بود، تیرماه با خروج ۶.۹ هزار میلیارد تومان پول حقیقی از بورس همراه شد. هم‌زمان، بخشی از این نقدینگی به سمت صندوق‌های طلا و درآمد ثابت حرکت کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/670160" target="_blank">📅 15:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
«عدم تطابق شعبه انتخابی با محل سکونت» دلیل غیر قانونی بانک‌ها در حذف متقاضیان وام ازدواج از صف
🔹
برخی متقاضیان وام ازدواج می‌گویند پس از ماه‌ها انتظار، شعب بعضی بانک‌ها به دلیل «عدم تطابق شعبه انتخابی با محل سکونت» از پذیرش مدارک خودداری کرده و حتی درخواستشان را حذف می‌کنند؛ اقدامی که در صورت صحت در ضوابط و سامانه بانک مرکزی پیش‌بینی نشده و می‌تواند متقاضی را دوباره به انتهای صف بازگرداند.
🔹
از بانک مرکزی، سازمان بازرسی کل کشور و قوه قضائیه درخواست می‌شود این رویه را بررسی و در صورت احراز تخلف با شعب متخلف برخورد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/670159" target="_blank">📅 15:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ca0cdc51.mp4?token=PkxHIPu0ozkEZ_b0wzIEjEj8mZHV3yMfKPx-CoSo6OLvXFWjc2ll6qYxfMCEwBbnzVBdLhwQjlLJ2Ch5Tw6ktBixIq4G0WVl08G30uzpGnjL1gLAUCzbMecwbnrNg21yXn8Dh6mhsm8101ctB2O440NmMnXx5Bj2YyvYt9eBl6Vxr6LXjtFWp2Sc7T8g6KOy8lgmRu7xLfzloYAtS2NsXmRDHZ3-uPfq2CqLZzOCh4nuX0Ys7oVokbWA3RwJlgWJ2Vl8OTMbICyfdVQV8o5_7-IJs0PcLIPED70yxppnv6qrGLTzqorOf5E0fn7o-bJH1ewBAkxk-zPg2jtNFtowkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ca0cdc51.mp4?token=PkxHIPu0ozkEZ_b0wzIEjEj8mZHV3yMfKPx-CoSo6OLvXFWjc2ll6qYxfMCEwBbnzVBdLhwQjlLJ2Ch5Tw6ktBixIq4G0WVl08G30uzpGnjL1gLAUCzbMecwbnrNg21yXn8Dh6mhsm8101ctB2O440NmMnXx5Bj2YyvYt9eBl6Vxr6LXjtFWp2Sc7T8g6KOy8lgmRu7xLfzloYAtS2NsXmRDHZ3-uPfq2CqLZzOCh4nuX0Ys7oVokbWA3RwJlgWJ2Vl8OTMbICyfdVQV8o5_7-IJs0PcLIPED70yxppnv6qrGLTzqorOf5E0fn7o-bJH1ewBAkxk-zPg2jtNFtowkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه طور با یک کاج و قلمه گیاه یه گلدون طبیعی و بسیار زیبا بسازیم؟
🌲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/670158" target="_blank">📅 14:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
یکصد و پنجاهمین حراج شمش طلا برگزار می‌شود
🔹
یکصد و پنجاهمین حراج شمش طلای مرکز مبادله ایران، سه‌شنبه ۲۳ تیر برگزار می‌شود.
🔹
مهلت ثبت‌نام تا پایان روز دوشنبه ۲۲ تیر است و متقاضیان واجد شرایط باید به ازای هر شمش، ۵ میلیارد تومان وجه‌الضمان واریز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/670157" target="_blank">📅 14:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObruXKn83LBjNBcfcBGrhCE0TPIo4uQ4_VomZoggJC7vv_97X0Iw3Wj8rbSdcS0hjddkAoRupx-ar7wwF0F8I7wLOnMmS5gG4TyWCPklPFxAuWngRZ2UwS8jdFbyNeJwxr6Y6R93URw4n4xXgQgzfG73kZPA4s3-5td5-TnwsfsyRWC2HxOdvF_8eKDUwqtXa2Xf5dde-ypk9JBIB3E3VsGcs4czlq7t6az7bXVWNoKbvnnNTi3CYK9YNkxeMaRwFMGAy_5J28TrN23TKKlivS0AHY5F7ikotWIYBHSmaCLcYZZzv7UQgGwKQHL6LqBaYV3fOJ0aNqbDNNe5oETnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله ای که می تواند همه چیز را تغییر دهد/ چرا ایران به عمان حمله کرد؟
🔹
عمان که یکی از میانجی های اصلی مذاکرات ایران و آمریکا بوده، همواره تلاش داشته روابط دیپلماتیک تهران و واشنگتن را بهبود بخشد و فضای سیاسی منطقه را بهتر کند. با این حال، حمله ایران به عمان می تواند روابط سیاسی دو طرف را تیره و تار کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3229730</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/670156" target="_blank">📅 14:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
توصیۀ جنجالی انگلیس به دریانوردان در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس به کشتی‌ها توصیه کرده با وجود اعلام بسته‌بودن تنگۀ هرمز از سوی سپاه پاسداران، از مسیر جنوبی تردد کنند.
🔹
این در حالی است که به‌گفته منابع، دو کشتیِ بی‌توجه به اخطارها هدف قرار گرفته‌اند و یکی از آن‌ها در معرض غرق‌شدن قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/670155" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRRzrZD4ZILMLM0ISM2mLzMuSVh7CXEuN0G4LDu792tb9YOMHUUTdROJ6d73-kCfcACKiGVwMWIe_sv4MHKqBFHdygFkK6oImEs5Vj4Ki1elFQg-dbaI0BXflyEPfGBjeuyUVDVIst4df_zmi5PNjw92g40Ny8JSSzm4yy3J9ZArIfahl_UgQW_Ede9g5125NqhvCqpx3nk1iVsYWvCqkQdSjotkAYyzqd0Bh8eYMDv03p8idi6gaFWnnAnJiyoc7YvVbam2IItpt1sDO_8Yy3tykZ06kIAvXzwQQufxHFIMZ15SOSkSes6pwKFaZ7rGBeT8nPepsMzFz1XMcM-wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZR6ygwrfgF2y9w68zA6646-NMhhH0JnOCw2ltdQfqEO8klCGiNSus2bzoM5yXsIPfFBponyif1ZSLnic-e7GMrgBD2p_nB00ioXmTQYofv7w3xCOw8IWMfp_OLNkLWdJdhb4Bbhdg_yESrn9XFZcDdaBbw9uEtB72g80_ZOs3g-BTtaLZ2HifWAFoO5YkJ8jsY1b80bETyKoVRoXs2Q5P60okXjXNuaODUVxj3DmvUrBKsAb-542ngagQzwFWAM8Rkl6TyibKcki4NysX99g9mwYgMV1cn-zpfoQiGT1HZh02IuCTRZBowZf3QDeXyGyaeZslxxzH5EXnoodvf_HIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EowIDvrdtFXwfZmpzGoTchaOWoE_6JjbngpevqcQj7lSeC9FN1BMoYrOdmgwfaQ5SbgEiin7UDFBrOaq8y74iq4fVtSqH76iIG2JqnwLPvVrZAfViG8z4C1Pe5SxPwpkc7OoaSE1Kz7Uw4pHj3Sw-hMk9Q6fSvy3fjwa2MFIq1oWcSQyjriMgsLvjyjYRbwGbiBy3u_rL1d-oCREitQmYglnyOmZ1TMHJCbdjAOO0sZslUtMKkuGrYh-C43gihJCP0IOsi5S_TiQ3IVwg9x_nhYyMp9xYPzHOTfGSXViDoL9PVhXFevrFxKWoPDU6IBARjXrIEvH6cOfkrit71S-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJYv-Xv4xUTX8zWaJh--U7fSkR1X4N0uMyFvQBFE6aszXDRScq59ZBLr4EBxx3VEPGhWvxpth6pFETEWISQorbHGP3WP2xLC3UgnBMXPxStVPA5pAhnoVlws8tGMHXJKaMht49D47XBMhukJuraMtc2zQBy2-wcRkCP9fqFPJYPdYw5YxWEIbvxysOVvoTQc669DqPUqUV_hs8tyA4hpQ71eJTfHr2c3b2onA_CbzXWvQP6_8QoEOOkWR3NBUHHPj8tdRxSBcYZfva7d7xQgeNDQCYNMG7uxuR-k4Dy444QQw2Gb_AGL4XaAD0ASlb6aqk4K_-78HzR4f3FSJa85XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جام جهانی؛ فراتر از فوتبال
🔹
برای جامعه مهندسان و معماران، جام جهانی فراتر از یک تورنمنت فوتبال است. یکی از جذاب‌ترین بخش‌های آن، استادیوم‌های میزبان ایالات متحده است؛ از جمله استادیوم سوفی در لس‌آنجلس که با هزینه ساخت بیش از ۵.۵ میلیارد دلار، گران‌ترین استادیوم جهان به شمار می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/670151" target="_blank">📅 14:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670148">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgRDDfriTAvxd1kyPayTgfmlSCZI1nZb_NxpCI5SrTJfZ7VOdIk0jvSXADtwXTj5IpnMHAw8IhtDIYozMTr6p23zvaAAskxBkqWscUknjOcov7C4EMY4mQejFZrwV7b_q6Bfr4M7uc9tx9dMZ5UQ_ceno4ddGqfxk2Ci2d4NILbShKJw6O2SFeqjUNlkCR2VxVzNlNko1H5e9GdlyirnWqITYFbV0CRE6jk-ETFiVU3KQOOnoyeZYJ-gRbrVx78K23MVtfBtoBsO1cqmx5MduBRhfSpbZ-QDqQ7ll4u4sr19htLD2dCsojuP_Ev29NfIuAMQBQOj2vKzhUJmBoiQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یک کاربر آمریکایی به مرگ لیندسی گراهام: یاد و خاطره بیش از ۱۷۵ دختر ایرانی که در ۲۸ فوریه ۲۰۲۶ توسط آمریکا و اسرائیل کشته شدند، گرامی باد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670148" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670147">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/790645a23f.mp4?token=n0NJqWWzuJjshfVEimziD0OwTSW5f1LLws9gejVE5C2lFzmWmQJxI1SHXAXbzNBjMHQFYPwjO6go9AXzaDGtCsXNkL76ui6QVwFK-9LQUdXH3XsZR3NVPH7POTQz0Qq2PeZ4voydBMiZtmRNU2YgKzDdBi3ikwBaNld6WxN-DYJeVeWUTUYs8qKezBHxpGjADCBLQg_UXmNSqA_6Wx54_Ve7styW5vdgK9cof8EbSXGTYzdNTP7QuW2kuQuZCDbf93WuwDcu8TohC3i55PehlPtEWUK7PKjWPQbCMKeGYjgf7HVz8ZkO92miJCP2xTVC6ZDLTBhfIHVpNc9RfGrEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/790645a23f.mp4?token=n0NJqWWzuJjshfVEimziD0OwTSW5f1LLws9gejVE5C2lFzmWmQJxI1SHXAXbzNBjMHQFYPwjO6go9AXzaDGtCsXNkL76ui6QVwFK-9LQUdXH3XsZR3NVPH7POTQz0Qq2PeZ4voydBMiZtmRNU2YgKzDdBi3ikwBaNld6WxN-DYJeVeWUTUYs8qKezBHxpGjADCBLQg_UXmNSqA_6Wx54_Ve7styW5vdgK9cof8EbSXGTYzdNTP7QuW2kuQuZCDbf93WuwDcu8TohC3i55PehlPtEWUK7PKjWPQbCMKeGYjgf7HVz8ZkO92miJCP2xTVC6ZDLTBhfIHVpNc9RfGrEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در بنگلادش با ۴۴ کشته و یک میلیون آواره
🔹
سیل و رانش زمین در جنوب شرقی بنگلادش پس از چند روز باران شدید، حداقل ۴۴ کشته و بیش از یک میلیون آواره برجای گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/670147" target="_blank">📅 14:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670146">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صمصامی: ۸ بند از ۱۴ بند تفاهم‌نامه، یا نقض شده و یا ناقص اجرا شده است
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
به شهادت رساندن رهبری، نقض حاکمیت کشور و مغایر با اصول حقوق بین‌الملل است.
🔹
با تفاهم و این صحبت‌ها، آن‌ها دست از جنگ برنمی‌دارند و می‌خواهند از کشور ما به نفع خودشان حداکثر استفاده را کنند و ما هم کشوری هستیم که استقلال، آزادی، جمهوری اسلامی را گفتیم و به خاطر آن شهید دادیم و مردم ما با تشییع نشان دادند که در همه حالات پای نظام هستند.
🔹
از ۱۴ بند تفاهم‌نامه‌ای که با آمریکایی‌ها بستیم، ۸ موردش یا نقض شده و یا ناقص اجرا شده و آمریکا با تفاهم به دنبال صلح واقعی نیست و قصد دارد جنگ را مطابق منافع خود پایان دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/670146" target="_blank">📅 14:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670145">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1d248bfb.mp4?token=GxkU46NlXF5AyjTC0Jr5COVWAwxd1tf2xyAKxWclr4kNhjLLOz6jzjfhhbxGBGMMCP4hrgLjPzpUf1GFPqp29PgfkSQoU8bbJ_4__NlDaQ4HAq7hGEXfi4sCTVfk3RAU18j9OR8RR0v-J7RhY1AlAV30JOTU_lo5AzUC4XMNjka0iRu-sYiHs3WbVIj4pWVzoqp2WxBqVxHrhQtsWrZeUOWWAZz56JKYff_Y-JM8mVEPbljshOgsgUTKYnMqAsrcWuqc3UiLb_M86-h1JJZ2YRtptwGh8fqMkZVttb5bqqfrA4WXs03ftR6bqR6Dd-J_CvF2v2TPnu-8S3WkdP__Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1d248bfb.mp4?token=GxkU46NlXF5AyjTC0Jr5COVWAwxd1tf2xyAKxWclr4kNhjLLOz6jzjfhhbxGBGMMCP4hrgLjPzpUf1GFPqp29PgfkSQoU8bbJ_4__NlDaQ4HAq7hGEXfi4sCTVfk3RAU18j9OR8RR0v-J7RhY1AlAV30JOTU_lo5AzUC4XMNjka0iRu-sYiHs3WbVIj4pWVzoqp2WxBqVxHrhQtsWrZeUOWWAZz56JKYff_Y-JM8mVEPbljshOgsgUTKYnMqAsrcWuqc3UiLb_M86-h1JJZ2YRtptwGh8fqMkZVttb5bqqfrA4WXs03ftR6bqR6Dd-J_CvF2v2TPnu-8S3WkdP__Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/670145" target="_blank">📅 14:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670144">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnpxYJRIhrYTWyO7y8jxBez7jNhOVLP5Z98x64VmAbWZm6XfjHBCTOfYnKUl6-kMIl0FNsv4Uvzx5ioeh8yKAyv8pfnoF4SXqxRU0HKJueb4zQhOpj8cRBx2od9kJv5hf9Nbcf0LSp6ZwatuqxEjpkefeLiAtCB6r8ZeJ_R_VGr-p4yTWifh2wK3gSpyVcCe83511n32MLtmDLJS3c25vYDMVnbAt8iQezbGLdzgYyD7KZoKqTAqWSojVSSoIflB5utxm8bmPAtpBc15VvqUJuRYJEHJZynj3_rkFT8ww2nPalWqF6bHsyR0CsfxjP6VH5_CvZ3swiUycqSWAu5vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرنگونی یک موشک کروز توسط هوافضای سپاه
🔹
صبح امروز در جریان تجاوز ارتش تروریستی آمریکا یک موشک کروز توسط سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در حومهٔ خرم‌آباد سرنگون شد.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670144" target="_blank">📅 14:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670143">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در سواحل عمان  مرکز امنیت دریایی عمان:
🔹
در پاسخ به درخواست کمک یک کشتی تجاری با پرچم قبرس در پی وقوع یک حادثه‌ی دریایی در نزدیکی سواحل "مسندم" هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/670143" target="_blank">📅 14:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670142">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در سواحل عمان
مرکز امنیت دریایی عمان:
🔹
در پاسخ به درخواست کمک یک کشتی تجاری با پرچم قبرس در پی وقوع یک حادثه‌ی دریایی در نزدیکی سواحل "مسندم" هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/670142" target="_blank">📅 14:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670141">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
توانیر: حملات دشمن به زیرساخت‌های برق، ظرفیت شبکه را کاهش داد.
🔹
«حمیدرضا دهقان» افسر پدافند نیروی دریایی ارتش، در حمله بامداد امروز دشمن به جاسک به شهادت رسید.
🔹
هند خواستار کاهش فوری تنش‌ها در تنگه هرمز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/670141" target="_blank">📅 14:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670140">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ببیند چه‌طور هوش مصنوعی روایت‌های تاریخی را درباره چاه چهل دختران یزد، تحریف می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/670140" target="_blank">📅 14:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ib9HPyQP4G2uQXHj0g8FR7t_kXy-2nWyd-BQlQIIeNVdmqHHi37Z4fzw4PzqxJkwFxGu-9l9g8rtjSHcr-BLpwj_BipjmKzvtDvuJwuPIG7G6l8MScuuluai0lT7W0sthZ6QwlMKGyZHBc16iz4jGEuf5rvcs20K6wlp5VxEiiMvVIEihJmx0d7mWued-AJFpieQ__hseo853Jsfq_A92fUoSNoU2uU2qG2GEi_zGL0SBEt_qoTyZs0yksFKtifHjQ3kaqwCgFY0nhjW5ounNIln6tfZF3cPV5kJ7agzyoBlLKjnYneqyW3kSXVjqW2nuby2YQZgG5wR4-2sU1dhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کف دست با تمامی اندام‌های بدن مرتبط است و ماساژ کف دست به درمان تمام بیماری‌های اندام‌های مختلف بدن کمک میکند. هر بخش از کف دست با یک اندام بدن مرتبط است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/670137" target="_blank">📅 14:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4yJemsY38kh-QMR7wQalNfJeMDgsg_eSDfcy4RzIgid5A9_ew7xF2gbve-5efG-iQg2bjz5LVZ5H8xW2LmNvvwEJXbEqlo2Z1fLBIdXQu2qXZy1dIyF2OnslvaG2IiAAC6c7d4LCebMWUxizDi273AP72lnbHSQsDHbpVj4_2TdblAN6XYdsarHn1TWnxAOe0vX8Nsk6ntegf4N7AxMQtE8rzOgEAD_LDMYtWhyIqKEYz-p5GBcv5AE1C1om6A13aOjypz6Mw1aoXzvWqS1lfHkR7uqTXRaW-LgvTso9q052BqQxEVQelO10Gwe8rf_pYHag71E0jmbvaTui-19QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع
تشییع رهبر شهید انقلاب
در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان
«بدرقه یار»
ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: ت
ا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/670136" target="_blank">📅 14:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ودوم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی فضلعلی که با وجود حضور مداوم در هیئت، به خواندن نماز و احترام به والدین اعتقادی نداشته است، اما با تصادف و تجربه نزدیک به مرگ، تغییرات محسوس ایشان زبان زد می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی فضلعلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/670135" target="_blank">📅 14:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43231dfe7.mp4?token=HQBYlDL-0S_L6DoIiRkvio9fM7m7OFJxr-YjT5ytqjXkNJUJ2esSyz92Sq3NObiWrEtRM5BLxguRyc88Ui_863Aj2prJY7K5p1sh_0rAqH4o7-vocgD4jnrP5KPI65CUeErvM4sBTv1ZEI8CGYp320Lid19i3BAAUod22uM5MJfx3A6r6z4Zp9UaawyXroDyjK4BsiAlfFqAkWV0fowbvOiiJoLO9J3nS4SN-Lkfow2pS73OrtotYJdY5uzROVuuL8AIjcvH_SX9oE0f6JHUCKMznw0WiOl8oDBFvwCo-KyZa3Ng38DNbCPUc1Bk4i2SrxekW3AnZMd9rgM1a6-tcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43231dfe7.mp4?token=HQBYlDL-0S_L6DoIiRkvio9fM7m7OFJxr-YjT5ytqjXkNJUJ2esSyz92Sq3NObiWrEtRM5BLxguRyc88Ui_863Aj2prJY7K5p1sh_0rAqH4o7-vocgD4jnrP5KPI65CUeErvM4sBTv1ZEI8CGYp320Lid19i3BAAUod22uM5MJfx3A6r6z4Zp9UaawyXroDyjK4BsiAlfFqAkWV0fowbvOiiJoLO9J3nS4SN-Lkfow2pS73OrtotYJdY5uzROVuuL8AIjcvH_SX9oE0f6JHUCKMznw0WiOl8oDBFvwCo-KyZa3Ng38DNbCPUc1Bk4i2SrxekW3AnZMd9rgM1a6-tcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حفاظت از روشنایی شهر، مسئولیت مشترک ماست!
🔹
با برق دزدی مقابله می‌کنیم. برق حق همه مردم است
🔹
گاهی یک تصمیم نادرست فقط بر زندگی یک نفر تأثیر نمی‌گذارد....
🔹
قاچاق برق
نه‌تنها منابع ما را به خطر می‌اندازد، بلکه حق همه ما را ضایع می‌کند.
🔹
با همکاری شما، می‌توانیم به حفظ و پایداری روشنایی شهر کمک کنیم.
🔹
اگر موارد مشکوک استخراج رمزارز مشاهده کردید، حتماً گزارش دهید!
📩
سامانه پیامکی 30005121
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/670134" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG-UDiJgFAMa3VuVh5Ua_lQ_lZ0xvEWEQ10F_7E2Cm1W2KUllBn1GYvwD4I0HtCf0VWYqXb2vF8U6GCSc1zoEpyHlVRmlZ062M2JA21AFKLA9btud72XzGjQ_aBZY6ZgXr_yomDrgPtsVzq5PJY4b53BFiNbX-9Ionzi4UCgNC6_r_7hMg7HG5Ao4B-KZ65TzVZIL5kGg7uSP9i_CfVt4Q268UHWjAEm8Xvizu5zeHqqC_0h6wYj0Ef-ZELXkrtRwA9qIG6gr0t5xLOcwyicWY4rqR5z6M4KH8AalhxGT4_D-IcWQ3_tGydE-cVh_6VmfydZHuqUlfiiJSMCjKZfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqQLeCZspcu9JjOQ31cavd0OMy66EfwxGPeXVyOA-2K50Et0D-PjUwyns3qJhUD8UUC5FuUqptKQwJin1FH7hy7d17xgYxRNvVvnkctG0MDIMRtvYxN7kc44HOBJuxufImRcIWdbxAp2QhmRilwmOlfWuRFS5WhPHZn-zBC1jPA48ghFDqoa89CM2QDv_xU-3JDxEDMasWEZtZds-JPaMPIXh4h3g5uFqT5gOlLmeZa4Iy7xORgrMRS89wuJ3WAPAzx0I9NEk8EwENfSHe8613MxRaLvqeXpOweGyXlRWumWA73NymPH6vvlD2UYn9PalkSiXL4gPZW-shIwLLiQgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند مدل ایده بستن روسری که شما‌ رو خاص‌تر نشون میده #فوری_استایل @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/670132" target="_blank">📅 13:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03639c19b8.mp4?token=e09EcvxLeAk__UU_O9wAc8apWbCFDvfMxicZsvWsNCYDFVU1gEO6xKd1m3102M_3blBbX7g8qIGrVLyuLfGq3MlMg1ja3QFc94b0Q3R0mKZ5kfz92n1UNUc33hOCkR4aQBl_lOAqESd05XaYfrQF4ZzcLJFXhyszCvWP1pkMuq55_Ahur6UIBt7bFNEj-ab9CpbN2aAJDXrHw1KVCZLqIaMz-l0mNuPmLouajTkVeNaJPfh1doXtL_9ApjzvtkFiot2IaGpelMcsnCaTorAUToW7QdA8MCjvW6LTR76_7qoJasCf64PNLCmiBWOn-ImwflG9QZx7CssPnKF3vHnQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03639c19b8.mp4?token=e09EcvxLeAk__UU_O9wAc8apWbCFDvfMxicZsvWsNCYDFVU1gEO6xKd1m3102M_3blBbX7g8qIGrVLyuLfGq3MlMg1ja3QFc94b0Q3R0mKZ5kfz92n1UNUc33hOCkR4aQBl_lOAqESd05XaYfrQF4ZzcLJFXhyszCvWP1pkMuq55_Ahur6UIBt7bFNEj-ab9CpbN2aAJDXrHw1KVCZLqIaMz-l0mNuPmLouajTkVeNaJPfh1doXtL_9ApjzvtkFiot2IaGpelMcsnCaTorAUToW7QdA8MCjvW6LTR76_7qoJasCf64PNLCmiBWOn-ImwflG9QZx7CssPnKF3vHnQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سناتور جمهوریخواه دیگر به سرنوشت گراهام نزدیک است  ان‌بی‌سی نیوز:
🔹
نیروهای امدادی شامگاه شنبه به‌دلیل ایست قلبی به منزل لیندسی گراهام در واشنگتن اعزام شدند.
🔹
همزمان، میچ مک‌کانل، دیگر سناتور جمهوری‌خواه نیز به‌دلیل ایست قلبی در بیمارستان بستری است و…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/670131" target="_blank">📅 13:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670123">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO3hApN97fZmHrttc1GK-Cx-vd_v0rFKeX-K7TedSwkKUY3vMGQWysQcSVOtYVmCPJ7D-hVB1kVT1M2USqKpAqQxqeP3VJ2A2wKcTgqsDKYfHryW2TRynWkwLlkpztcfNLgGGb1fuS2jlA_zW0dB8sOHfg7l8nj7BV7BaC-Q6d9Et4uzTgziSsotump4J1e6F838srlQsPgg5btbhWYh0SN5zqJqjisbQ03SOhOQNzud0v-eEwbn8zCzT1EMWITBki3JF80-YUwpJhlPe9GyMH0cxiw-CkZLl41LK0Y4uxNhCGxm0TvWuY9F3NqZE9W06LZ7zmLracEED9pNJu6PWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fal4CS6MIjygpayp5SFMVHV6h--dcq61BUl7zSRvLPeFOmnFgKqWlNzEc_gTonKnWcHHgRJzF9jyIAf7Eu6n2iN9kjrYnerBU-drKCyry9jyo9Mk-bdsRWCRzI8IRE1ti77eFCPFdya725rofdr8C5LWPhXaohsOhCLUmROLvm2HP3m08lmygJ4yj57l5T10z2QSPA1Ca_Z-WCiUzYTBDfquHH8nOqvxguL1O_5Yk7_LbwayO-sSeHgzpx-GU7Wj17ILm6cDdJmoUOPvvxY5JAhNz8qR0UnGqHyJefXTGgGWT8z5tn13KjzRCO7JbKWJAZ1WLNELMbW0GuH4CITT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nERThtwC871T_i2D25piR_11qhON_OuMoKprKmJfhVYa8LjqoWS4hLY3NAomVVFoOe-6y_zobGY9qnaghwyWf4htV-CtlORQV3MmlJzGXajp8DQ11S8_jUr26j54qiPaCqq7qKnWBDqkEPB9xdTkYaV4O5_rBsAsfthkao-2LJl8saO9tf127g5SGRUwZc9TFW5zSuth0SWVm-IANwyKACgJ-u1dXrgLB5l4f-sEWo2ts_KouM3TFpsoi1XWAEBPjdI_M83p_P-KqSBhO9ZzPuVU4U4LZyXWNGhVo5qxA2DmFqKz59hAr6hPcZnk9EdVtJh5DOrWUbUHmaVelXl1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRPve6CyL32vF8yyeUZAed57-984WClRzQ4CDMDKsEw0PUJ0-h67dYwmdKTIkgd5bW_glgAnuyD744mVynDzGR9vvwnEJKDUL0CHfUssGl3Fl36eVcQTFBly5dR3DDf1a6F3yLflwoaHt9WuAwQdDOG6X8C9BazLm2MlJsQzZi6GTsy10daJYqs1xVRnhIlCS5JY-RopLS8TTlSVP_YPQdGYDy_8OAKTnoJmiS1pZV2F8BSiHTiF2wkFHeZdQ7xudyjfjeJsT2ri2vLPt2bJy7aswZsIcm9IucQnJDcixHNlEmbxcce5eG3QFdAJEq0AgrE4_-FIw2xrGLNeiWAg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCQJ7Ed8XYE_sbfkyW7XrHzUrNMeGumpu2m8kJqo1tpmE8aSgMvlkFXWmzajHSLO_J1zaHNJrhztm0sqYzwDOokhHTBxzcaPt205OMHxQGz6j8Bpfocj-VMjcIOCrp1fdCSAfN2R_QXntyHrCx3tRr7NOGwdJsK1LwhhXKicdWHEWfhJ5ZaYZIdHfed-U0dLIn0bt8k2EGNi4c9ZT9jU5p9eZzRs50ueiIZFhgjH4yQ0H1T9CaVbgO7a1HiXR1KTmThdxBqApWPoLXfW-8JB7U8rUlZAcvjpuT9HV2Ux6D-qlinplaYRepf2DpW1RDFFZHscs7_jzfveYjO3UTbLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5b_2uTJ5Dzy1hozFol0oH3gfOwLSUDWQ1u8ArweyFV5JcHCdB_kx2Dxy62MxJU49sihtfrLftMVp3Q74Ww0Rsl9M187OFdqZhJUp6wA8cASLPN8ixaTJPY3sqhV_U36EkUHQTJDQUaVR2SHM4i7DjXCyJ4k7t62gTyCdwN1K3FJgTRQ20IhORioBRTsOp2wiMMmF7xuKisEnWtXGsRXmXVsTS2yejhyysBdzBA-blFmccwnGumnOMjHFPEDz-6IKUby_ujijGv2KRt3x4GoD2bDZS8dMs2HXiNPegiy9ew7Z5ETjMx0KwSwHKL-eBBMmbmehZSVTslB8GS-XgFM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvC-EDig0CvVrT-D3mANM4Ey86hanX8_EbfddVzSQdoNZyCDKjp-u9wtGjdJ3WxIK3drGeNJO-RidWDi4ICB_KFcMaZj5T-noDJyRKFHliBKlzGVs2HgjGoaF06tqcsKgYk_pf3XMAdMhNyGEVhkfzgBy0xHS_coE24FyYDkYb9uXJFCOdq_lHDyGYRkpW9rZv2_nLOcoYOZrbtAwdPQ6zRlDKjP6N0RCV5_g2RL7b_8zT2i8E3Fj50YrbLELnXzFxr_VuBgglWH12ldlMmJN6A8vMFRP8eIJdLnO2Ulu4iMuGXAabZNqDvoHsM8LDAyXpE80CYWN64kePewnKxSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3n5kMhDtFKKhq5CwRJk-A86tLKT82vH5iLk2vCPehwH94S9Rq1UVZoxYY3t-P8G_2U_tGYhhGsatdpDD0qn517bn6CQiXYrFFhfOlwBQ2llaK5nTAv66CvqZ8pjMsF-HiltqwSnCG_Cq-g0pg8PWrCWVbKXN_xMTxBE4RjLZHMC_dAXiBNqmI6VUBnnvNETL5wuJeEb3UGV1Ij5XqpieVmtC3wj01pmzyh2WWYHPyiEzT8PxuAeKoQCfk_Ee05fYIIOIR5ZpEZi9buamr79hppRNtmzzYCERtkGSaB6sdJmpPZTD-pCQEgZ5uKtbjI2zaE2LDuCd78QFe4O3_2Wjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پوسترهایی که رسانه‌های فلسطینی برای رهبر مسلمانان جهان منتشر کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/670123" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f13015bdb.mp4?token=o8aihgtFu4KmhOJAojBogHdp_NApQse9hpOTMcHHM7uIVAkcye2kJ_zrwoybn2IOmCkRJa8-QP7ZlAMUcDLrj9298igsr0uVvh7HV7lHqV7IGfTXGn52WwIOWVIuStJ0D2qXpF6WAsIEO4lLjSnRuVYq5lq_7xzjoLwwJiKxXXz9MQUQrZe8XMPhT445tqA5Cl-zVvetC-C_uaEfi8FDeeivvI_yD8_NsCFXZfin_HbxR3C_P6udtpYZOCP6pEDlj2AXZLQLciXNpHYOXQBw8AWUJIN6zCO9nikvbgFuI6bqbG0PAeejRgPikuYcBV35z8_Bw4LrnNxSUJTWWVV_7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f13015bdb.mp4?token=o8aihgtFu4KmhOJAojBogHdp_NApQse9hpOTMcHHM7uIVAkcye2kJ_zrwoybn2IOmCkRJa8-QP7ZlAMUcDLrj9298igsr0uVvh7HV7lHqV7IGfTXGn52WwIOWVIuStJ0D2qXpF6WAsIEO4lLjSnRuVYq5lq_7xzjoLwwJiKxXXz9MQUQrZe8XMPhT445tqA5Cl-zVvetC-C_uaEfi8FDeeivvI_yD8_NsCFXZfin_HbxR3C_P6udtpYZOCP6pEDlj2AXZLQLciXNpHYOXQBw8AWUJIN6zCO9nikvbgFuI6bqbG0PAeejRgPikuYcBV35z8_Bw4LrnNxSUJTWWVV_7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام شهید:
"ترامپ" خوراک مار و مور خواهد شد
بدنش خاک خواهد شد
جمهوری اسلامی همچنان خواهد ایستاد</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/670121" target="_blank">📅 13:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دبیر شورای هماهنگی بانک‌های دولتی: خدمات بانکی به‌تدریج به وضعیت عادی بازمی‌گردد/ برقراری تراکنش‌های کارتی
🔹
خدمات اصلی از جمله تراکنش‌های کارت، خودپردازها و کارتخوان‌ها پایدار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/670120" target="_blank">📅 13:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVZzkU0pMEfF-HtPFl9C2hgPRexcB7ufHiNZV-ZXeVWyuHS8UgziV3-bXPOYY1sjOs6RK1v22k7h7oKgz1IJl5dHk_DGFBBv9ibCc8tfbItbToF9ATj8TyghkSkhgfty5JHeDa3awSdsrINIlbQKpvFlDg0npqxXxECibHRv-zrBpk9nMpYEQIgn0eJiTKahLqzi5ddzZYWU1fsQ_LKkWbYz7vgB2pum-Dl8D4fAmRRkdfcwkgKmtED09DiOkPf9L9fDjaM3QTNyoiqrxfcNQrhH9kpCBYwkkxkOTxCWknEX1-oP-WHKhLX3eSyCdYzxYtrpbNYaBq0PW3YIniEZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز مین‌گذاری سپاه در تنگه هرمز توسط تکاوران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670119" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk-zeNbR2h3NSxsrtyI9YP484PM11w5xqaywLjsPKNJ16bwhagGTW1K4IIPt-YAxsUF9fzbfbyqniFRYE4JJWvgWpn7g4mDggZhX3-pEEprmh25s0lKfooiqFWU_lM7sCX26SMITMmtaCqLs49OkcAnXYwox5LLtvvvRAFEipmIpDjyXooh7F5dXZa4ujNQLRR2SrrbXqqXDNBCb9NVDkaRBzpJUl11zcICxahmxPSNO7cn8Jp2ohuxY1nrnpgvLAnMT1RYkqsoWRylgmJWG95V2V_Fdva0PGZMyZEutRwfIcZe5p0KG8Q-ca0Ccq-uIppkxU73s0wy43USEOoMp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۱ تیر ۱۴۰۵؛ ساعت ۱۳:۲۰
🔹
قیمت طلا و سکه امروز در پی تشدید تنش‌ها میان ایران و آمریکا و رشد نرخ دلار، بار دیگر گارد صعودی گرفت؛ به‌طوری‌که طلا از نیمه کانال ۱۷ میلیون تومانی عبور کرد و سکه‌های سنگین نیز با جهش‌های میلیونی همراه شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/670118" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDZ4k13Tvd9Hq4PQlqpgzmx8b525b4MAC7g0BmRjkF1tCcFSPyQbaeIxNVfVXq13a91smPaRsVOstPV_gk1daaxrJTGh0qS1zbg7bpnKg0VJNhFooFVD3GjFWzkEUprKcr4aTmwRjYlIbOnwoo6KfQmIX8xsK8RfIeSWQ6tojv-7ppsXyBhnbpG2nGGoiHyJimifMFZ5B1bCNfGYlKZhTbQXiPYXi1_Yw2x0CEyvTWoXAotmstgp9MYmobaxtveo7eZ-dA8AIdo2_FUGZnHHboyBHfloXfSbkrlqFtg8MGt8kaTlUeTUMUTCSdkv1l486c5XaKNcdcGgn95mQnOvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: روسیه کامیون‌های نظامی خود را با نوارهای درشت سیاه‌وسفید رنگ‌آمیزی می‌کند تا سیستم‌های دید مبتنی بر هوش مصنوعی را در پهپادهای اوکراینی گیج کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/670117" target="_blank">📅 13:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670114">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hw_ktQdcDGamglUNchTpKWf--1FBtZATvDYV5MauRvC8pLZNyOa4t1bV4sKw45N9zivHR59hcXyFKEA9Y3OfFpFJljT84zf7A25VVhG8JQtX2E44B7zoLq1K9h04JvfbaqkcS0iIPBF68s8ZcrX4bHrBbN3OFgmAyYNiqKvcz0H8t2Dm5otw6CtzRrVVJIDcC4cpvJCxligRfNpAFsR07SCcuL1aOOZ0I_LmqpvBHeJt3Yd58TZJQQyJlgStNnnjbCQ2UC8FmwdjZW-pqKayojVU4g2FaOdcazWYBUISJM_3c1EO3ml0dUXcAYihzB06pQXIteqBpjco-luZ1bWkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8-giZGMnX6em58u9dT1rXaUbBDr5mPZVovn-Y8mCqCer9fL6gdC73z1Spa5ilgs-YPeBTBgMe6gEmQWnVNbQk1602pkFjO0TEz3o5p0N12ZT-Gqwd8XQi-tbOhQLXSifeXcj_tdmQL0AZTwRBgm9f0qEFSBNCzzJdpUdO11fDnKlm2ltT2RlJdZbPGjoCtNVa0IxK4zLi006dZKKI5GrEbRy0atvndIX7X_DQSTpHsgSZu4ial_2Bqdrz6LDncjJuOdwL4E5qtuFwo1Y2JJQfHWTTZPC018POwMGCIqssY3vTORKJKrjV5PvTE3Ml74rAqAjmaAwE_oZdZ_SMlJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feWmiz18AIp6pP2ffKkvC-fxjtWYGfDMhZJwzH8VqKOHeT6KxBeRFzUKNVZBuLDf_ejIi1yd2-TnlqwZs1WiLYdMiZDXlpmYhscUPXMCWVL-igejdtNyLm669OHCaDDOwnxbMK2thntT6-kXsFarfIJdNxt4cTAmi5eve3nfRyjZqNGB2BfcUniCx55KB_XUSigxXW-cxercmgALU5m0grBrsErek55w1GC3bt2dNkKJB3JaZTeb82ixInB1KT0lxhhto0jHezMM9np5SDHAMFRahzIIpsfUkG15aI-FoUALtL84j2l4QmTfUbzX_LSedNlRWSu8r4KId2KSDKGz7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیش از ۶۰۰۰ عملیات فنی ایرانسل برای پایداری ارتباطات در تشییع رهبر شهید
👈
جزئیات بیشتر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/670114" target="_blank">📅 13:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWyq8WqYkmbm3L7broEgQ6nCpdFhNdsoO5A7zlo2Z5ey3epfgh1JvromrnXi4Ao5hv8-ZyeFWnHETlSOCGwT8Ogm9wzWeeygHCKbnbEzr5bAWJBTi5SIo-Edk65fiH5Y4mgGN1Y78VuRzfJ8o-xQ4MzmC5XllikF7pyKHoSL4O13wcYDSQdJk3q8A1YASMDWaHZZIdM4NM5r3StteW8q5sxTFuMei-dcyWTmiYmp2tma9gFM1UThqixLRyy_c41TN6EcHIMVI20aBFUacDTEIwVOOGlDtqVgM7P7gGHKmn3JIvvc3tpgEMJfF6Gzas3xJc7zafFukpMA4fIy4Qtr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از جرثومه های فساد عالم هم داره به سرنوشت عموی لیندزی برعندازا دچار میشه
میچ مک کانل سناتور ضد ایرانی دیگه هم
به سرنوشت گراهام دچار شده و به بیمارستان منتقل شده و هنوز وضعیتش مشخص نیست
هر کی داره اینا رو به درک واصل میکنه ان شاالله سرعتش رو بیشتر کنه و ترامپ و نتانياهو نجس رو هم زودتر به جهنم بفرسته</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/670110" target="_blank">📅 13:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گلایه شدید نماینده مجلس از وزارت نیرو: وزارت نیرو فاقد استراتژی است و عملا هیچ برنامه‌ای برای رفع ناترازی ندارد
امیر توکلی رودی، عضو کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
عدم تخصیص بودجه و مشکلات قیمت گذاری بهانه است و ناترازی ریشه در عدم هماهنگی و نبود برنامه دارد؛ بسیاری از صنایع معدنی حاضر هستند با هزینه شخصی خود برای جبران ناترازی برق وارد میدان شوند.
🔹
فقدان استراتژی در وزارت نیرو به بحث برق محدود نیست؛ در حوزه تامین آب و دیپلماسی آب نیز هیچ تحرکی وجود ندارد؛ در حالی که کشورهای همسایه مانند ترکیه و حتی کشور افغانستان برنامه دقیقی برای مدیریت آب‌های مرزی دارند، ولی ما برنامه‌ای برای جلوگیری از خروج آب یا مدیریت رودخانه‌های حیاتی مثل هریرود و هامون نداریم.
🔹
متاسفانه وزارت نیرو فاقد استراتژی مشخص بوده و به صورت روزمره اداره می‌شود و عملا هیچ برنامه‌ای برای جبران عقب‌ماندگی در حوزه رفع ناترازی و ورود انرژی‌های تجدید پذیر ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/670109" target="_blank">📅 13:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhxvLj0WF30OI7NgqjH7JaQZ7lbSXxLzzrOlMmckFX-MGSelZsu4_-QBu4w2njexHAz4tX6KHLbh7XlBvImlNup2wW7BxpHgd1XwMGto1IlDoC2n8SkshtGyCkbc3V47z4zWwMWcbjyZ0N9sUIzjU_-9ohWxU7rcMfDJ0TGOyIkWOePFupcWkvW2kELG-Jq7oa5eELWMQTBt3EeemNyQav6nIgCBvVd0Th-u7z_87GiyVeR9FuW09vx6LeRkAp7LfheWL_aUfXPxMi0EA1h7cw04pDg434bt4Y81yqsxoWbMVaIBd3kWUVenTFjpXrF__mBdXEKu_XN9ILGA_1xJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست انتقام از جنایتکاران، با حذف سناتور ضدایرانی، به‌ روز شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670108" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1b870e4e.mp4?token=v75xOa74Eg9ufjK_bnVDYY0JhIK017u-uIZdMBC0Cxsxcem_p-PeuAgYSxgXq_-WfwXzANqlbD-Vys0Uhus4t3P_t67tV2SI90bRGSdlYJM1dqHg0HgklOZAOMPjglpslXRAgMRPvpuz-xyCRQ_FJPsV-X2NYKB-tHbTMQthXWnGnE2NeUjRJdK6nSKc8E8DNTtiGt5xNia0Kxbz2AxmQNRrbI1ox7SNUK6jaoSPyJgmMpJnNNQsPhob3ERZhExpuEgQ2OV7T0tcCRwPoyL6rWQX_5fVb8Ut8a7kAD7MNOF5QdQ328z5eReqdM8Cu66UdOTJYd2-XAVPScWnyzhm7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1b870e4e.mp4?token=v75xOa74Eg9ufjK_bnVDYY0JhIK017u-uIZdMBC0Cxsxcem_p-PeuAgYSxgXq_-WfwXzANqlbD-Vys0Uhus4t3P_t67tV2SI90bRGSdlYJM1dqHg0HgklOZAOMPjglpslXRAgMRPvpuz-xyCRQ_FJPsV-X2NYKB-tHbTMQthXWnGnE2NeUjRJdK6nSKc8E8DNTtiGt5xNia0Kxbz2AxmQNRrbI1ox7SNUK6jaoSPyJgmMpJnNNQsPhob3ERZhExpuEgQ2OV7T0tcCRwPoyL6rWQX_5fVb8Ut8a7kAD7MNOF5QdQ328z5eReqdM8Cu66UdOTJYd2-XAVPScWnyzhm7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سایه VAR بر گل‌های تاریخی مارادونا
🔹
در بازی ۱۹۸۶ آرژانتین-انگلیس، مارادونا با «دست خدا» و «گل قرن» درخشید؛ با توجه به تکل خشنِ نادیده گرفته‌شده و گلِ ارژانتین، حضور VAR هر دو گل را مردود می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/670107" target="_blank">📅 13:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcr-06ykV4u06ZPjc8dDQE4Ht_RzjdPW34G8mBMfwIykMqZO9M56SVt3vF8qUsCjT9sVJONvLpycgV1L5u81wpTs1GE1hi5cF1iY1jtcESRFUPuLgZwHhEikzZlHsA97rAEPukgAimwuD_jOLO4zLAOVgKOBH_WJ_T4xOWnVGQJvclYbyAYZDJs2702BJp5_uPItQNXboccwEi7f2u-eEVZ8AkF2riDYJCZQLiUkK3AoFBvzpB3gsKHx4D0oq_qbqNhOBQ8sQAKann_o76OKt5-jqGRa60L0xuXl6uDqb-7LDQpo4CuKK7glpevpB2tZdzwelfDEbDyOZovRvT_7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670105" target="_blank">📅 13:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670103">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBRMFLFmCzDqKsk5fifFNz9yMhegVybGVpqx2OeMwiLpsqRDCCt4AyQrdFFI__8F_3AcA9FmpCQ8HQQssjMBAlu8GqBUVJAEq_aBAyA-hOiuNMVCMMO2Dyft8Ww6-qmfQJAEmoUaRoV-teF3lWBJ3R8D07finDkFjlh1xGJFiTJYwWp2pYGkPiXl10bAmWIkcL3eC8qynS5hsN05zKFxaDnCh_JGJ_FONwi8QgPHVyGZ0fJ8xS4uHGHOrquDdecNXXospSTWscg7aEe_MXCxCr74F7QQAgsOrjiVjsxYWykPpQYfO3ktCkUtV2kx1Kmd1XbC9AmuV7efAwNGfXgFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه شرکت توانیر درباره نحوه اطلاع‌رسانی محدودیت یا خاموشی‌های احتمالی
هم‌وطنان گرامی؛
📢
اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری (جاری) صرفاً از طریق درگاه‌های رسمی زیر انجام خواهد شد:
🔹
وب‌سایت رسمی شرکت‌های توزیع نیروی برق
🔹
اپلیکیشن «برق من»
🔹
نوتیفیکیشن و بازوی (Bot) «برق من» در پیام‌رسان «بله»
🔹
کدهای دستوری USSD
🔗
جزییات بیشتر
روابط عمومی شرکت توانیر</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/670103" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByQ9oBSA7oDNlL8Ux4upC9cBwUqzSL3wTfSCOhaI0SO2GwLPewv3_8abhtaVTawbxUXAB4RV-VfmzFKOdsdj40einpLSCq15apHsCY5osRr8upjX7YdG69RuupmltL9CAQMmM0ViKCtwO_mqGXvBmAOULZkKd0c-RDXJA9m3tv_bms3ryqomQJRzK79vwraUnVACNUSzC4ues5feKBW7MUASWyTo0vOzA9Zr_hTntUbadjqB3rmn7pLVtrVEy4jQh4Vt9aBKMlNUVI_vWk2CwAOgLLiw0seu1G8EtYbzZoDNpRDl4JjkTOjSZn_uzjoVQOWtxC7U9RgSG0S_dpjqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/670101" target="_blank">📅 12:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجید، بازیگر قصه‌های مجید: ۴۸ سال دارم و ۵ سال است که بیکارم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/670098" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE603t4ntRVyYiOC_paJv24F0sPpjK7O6i__oZ_NPRNW97qp882G0NOmp9DZF8sLm9H8cH4xuWGMjq0K3UTIUylJKB5SB3NHJ4cnZXnhWgsO_ybtD9nr4HPp5bqMXf9uIzwqKnoZpL-V8EuYpGA5ZKikoHHbHKzHW0Nf6DzUKRsLqyNQXqgXe4b0t8LAiYThaojgJv1uWg-CelWewV54qKmU-UBpE8dTN-6u6wfRHkzlQMgWTELFNNXaL22H3TEWUamweXtEBOzdgkZzzaBw_2_SYZhCB_eJh6PanMFMv82XtksXQ0T18eBxBCZHKXmqzA2Er-QZqKmavnz7kLkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/670096" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtrCUsUIFUfaW9eWJYhX2XA_P9pE_DM2vI_j0zT0k7IBFQ_PlYFhz5JZdLgEDzdwWYh65CaIrZAT55HZYT35uzO2_EnTPHi6wQ3yvholK_5TrPkgfgUAqXHFPBY6QNaZtC-5_iuG2ZcyEa1pl2_4CJgkjQKm5akXx9iNwzFphii8RE9t0K7h2ShoLWZZsPYNr2OwY4IfNGrOqDz7nsxUuk_YrBlXCupaAdn66V2RtUuQmVGIanPcBNukQZPszl9JrnzppVD-6TWkZeSF5d4rMsu-4nXNM8RQhpYscWD5klMG24O1lYsdZk47WHUdXcaX5uGq77Bx9Cd5w0gN8GnIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_8DbyJYcjbpZDBV1N6VCbqGztXdZaH9ecbBip9e4oZA56vwxixMSdQ_1ZfyWJQBexWBF-NJ1eFJ53-RFROUr30Rt1nyKMsvFBi0dyDGjG_4iORA4hHq0farqFBrXIoho2yIqPX46hd_1hpEpAcd8nPyXgU623p-PLsI08xypBdJejnp2mhG7fBK0XhBlt6csBixpUVFttiNbW6BpdeEtHHGGFKXZPzrcjqYnj3lg01Vy3ZMLIc0ajauo7SSTcm8XdUbtbeyVtgCzbBSn0vbqTlukdSA3RW3QM_pFFfsQG1S2R5QOSo93IIivrlhae2V-cUXIRyLbueEUm0EprJfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAuLlFqpr28SRM8IQB7l9PzHER8O7UAkXtfMJJzji9qOhI80bQPzdcDguw_COYsRZoNwbNc97DTdNZGBIj7Qyq1TyWEMQGWUGHT369eh9CcHrz6WztwcL52dSLcdHFEefsd9rS3MY_QGkleyZldfUIFOZUIDF9B2E_1cUGt07Q6Ca9r79qr6Kt6yb1iuwifKPRY4cZwQNtgUy5JS8w50xlwOKB7g3K3a18d-54sSAtHRlASSrT55aDSqQeNkJ1J3iDkhEFzx_2ys6mF576DHC3iBDW9iT7Ww8p89HvclnJtIPPU7LQaAp1Q0GT1lhaa28Rcm_OPQ5RG0ONr61spi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNOBl4LjCORShrXiYFHqDgkf3Hlqb4JyOPWF84o4jxkyA5o_nSIspSLw0r5gHYO8SKI8UQRz2_QUz4HXW4EzLkaqTec9Sy45lxRjakbkFW-Ify7qweKDfQcdlDHurZ_m-tXUKnpZnEgaNUZRHmwuCwWgS3f3kRQ3x0x7lcxFlSETN_vCvBSlwBkGWBDm58Frwj1E70EdO9365It_Lsrf7a6VCcbnemZniNGweKaCA_mbeg6O7paFt__VCsGV1MvE6rexTi8o9Vc0acK42XUiJnGwgY9NZnE9HQX9DY1a46-qx4RqjopgX8fxW4_xZUcb7h-bJ-njbOj3IBtxwYwAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3JeGNVSZZqvtLk8cSmPOkzpgBbtdZGSJ8XvoIS7eha9VvTEIYjquifHrKV-xDxz6spUZh7RBy9uQ5BoWc-d9VbmH5zz8k-cf_vRxaGzhmycwjvK0Jvqui6xFhKV4zpy33BQIYWAijVWq7YJ_QGmYiTnyH1IDdaNpKwNajkOr4bg53oapZgvfyQ5K0Jm1LQFUklIbY4lXhuxWRWXYQco-uPEb1m7pSRLuV6EDPOyybCHpLDS9z31sIvC-_4hPPu93V18L06wuajgruacOI08axwQLE0veElzWWByLc65PnbaQvIe0Rj39PWJjVAkQwUtfrb4dG9i9BQWRE4aII3u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne8Ks8Ymzw0SrM6zrgWFJAH9XCfbQCQO2zSCO-ylRvmh0NPR6ybK4rMYFv6EjYZnP0qdiT96EcJDsQaw7yAHCZUFlju5TRQ_tdhB0gjV2or3rKDiumIOrzJ3IpHytrwMEDaEOu5a576R9VQpJXFZtH3QyqH-XRQhvUXwGTd4U-8Xy-FEH9f9qt-temSIKofMIDBSsv96uw_PXrDI8qLTNvwhE6ojCFsyA2V-sxD7ER-4Cmt8EqF2qt7Vo9pRQNPUS-uy3pq-msZEcxiMZSj8qtCFArH41igP9jiOmbc9hbRFhMjDbSL_iNroh35OgFAxQL_mXhNtuccb_-x3xMSoOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شما تنبل نیستین، فقط نوع خستگی‌تون رو نمی‌شناسین
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/670090" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670088">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlc1qEJfEe3YWrI6N5pLkGkoOOYd8Hpb2CNBnwSFIvMZLURQrn0bd5eqBTdO0myBre3Qo6AxW_tiwB0mwWDA1vNHtPaG-5tLVMtc0pR0naFpTNWvfm9DcaXNXel61Sru2FaUQHEInpHdpU3GiwGvO8pOPHYryIB-p8_CqSffV9hA8DZU_IE3NPs2xhdy3NdsTDEGCYLyuDcEhe-_RG4NaEmBNqoC3z4udIMXeQWilShwJVEvwiatlbWwoXGlly26yh6B9w_uINzv9kQ-eldbXAYDVM-mCTwGUxd9OKxt0EgbIm4WQa42lqLzD9LEMdpbYjSlddR5z-1k8q0qZA75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلاق‌ بی‌برقی، بر پیکر خسته‌ از جنگ فولاد خوزستان
🔹
در روزهایی که هنوز گرد و غبار جنگ چهل‌ روزه دشمن از شانه‌های صنعت این سرزمین فرو ننشسته، برخی واحدهای بزرگ و حیاتی، مانند فولاد خوزستان، همچنان با زخم‌های باز و عمیق ایستاده‌اند؛ زخم‌هایی که نه از جنس آمار و گزارش، بلکه از جنس دیوارهای ترک‌خورده، خطوط آسیب‌دیده، تجهیزات ازکارافتاده و امیدهایی است که برای بازگشت به مدار، به نفسِ برق نیاز دارند.
🔹
اینجا سخن از تولید نیست؛ سخن از بازسازی است، از احیای آنچه آسیب دیده، از برپا کردن دوباره‌ی چراغ‌هایی که خاموشیِ تحمیلی، خاموش‌ترشان کرده است، اما در کمال تأسف، درست در همین لحظه‌ای که این صنایع باید بیش از هر زمان دیگر مورد حمایت قرار گیرند، زیر فشار محدودیت‌های شدید برق و بی‌برقی قرار گرفته‌اند؛ گویی بر پیکر زخمی، بار دیگر تیغ گذاشته می‌شود.
🔹
ادامه گزارش
👇
https://www.khabarfoori.com/fa/tiny/news-3229687</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/670088" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670087">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRbnXGnN4W49Hf7q_WsfAvlssArA6ELVQmNRxKQyy1y3lAriUV4Df_UmOj_ORKMQoNZcsG8pconwSDFRM4D7trGnrYy533-4caOcRHGZz-NDYzcuOf5TcKAbCM_dhRr96kLnL1oGpqieVp8wqnuy1KIz8eRz359aJrRSgs-uhjtSvP0D6JtdfPJH5TN_nXioQ58fA7oakPHsUTdtRezE_Obbz4kQmEuaDIA06jpLlp3WeWsMGQFc1B4GrRCE5dmgP08MegmRjMzvFvjF92Qptp-nSdvQ9RzzZ4nLqhNUY9mr-9hbIb7dyazLi_e6dBOD0qj-gQ4vGWybWkeXHBJ1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نزاع کرکس با شغال بر سر لاشه
🔹
عکس از فریبرز حیدری
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/670087" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
