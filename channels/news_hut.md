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
<img src="https://cdn4.telesco.pe/file/akACXgWgq8TrOfKTGn-Ja7LZj12HrceEVcomPGCNpytXJ1UUN-32DA2txMwU87sakSXA6yWue0CsxfDcGzj5m_vt0JIhsSn-lwqS92Wu2zZSakZFvZ-PqS_YNkwZxsGh0iVKtwqzbny_tBIWzCyd5L8_oYKwq6v-CfgJHl4Rpllmk1aOmNO57FB3q-zfELqO6-KSIBhOXO8TtwvKCjsJ6UZGlG0CvJeFfQarrcZj-76QD-Iht5oBVifR4t603YnbVuAII7uDBt2EG_K-S5rQ_6raxM1XFmksCwfBVuejsEQzK_0nPPFXmBC_zi2R4eOezqbt6DEJvDTbfcja3SOPjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIqkSNtisBzGIaIVGgcHTmsc8ECaaRwK0KmbhE7uKkLrj0429bFimk7kD_3eFdY4xhX4CuNkHubUQGJLq98koy7MyNyuCYOJNH43XCRXit2G9_tkIS7alHGOxvecoF78mEJQh5My17sO2iB2mmf9vyArPLewLxgoHNQb1jmJCl8l74wlk7ELuUFc1mB_jGrIKHGfriDMir4gxhJFBGe8xN2zq_K7M0kNwNGiyf8OfTGGUvdcsxURJZYQL2wotPU9EkZlIRlQK4VLYN1fY8y1SZE9VVmSrx-SDd3-A3Wc4OXppunTN2EbEbc3Ri-Xi9ckbYkMHvxi5EX_8s8NPSa-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FafT5U9Ts6n5scDIYyo-UxbOs5gM057a5iogxaUixIto9jwsP5mwQgSq6lZi5tVi-QNaqmg-TIAvlGYWGh2JF2_017cZDTzeqoQ5H6HKTBBWbmOBSMLg3eINyu8np1xDWu490gqciRkYNkgypvucUasL2ZKxQ_lhMt8wndhrflrXFWqn2y4pxdGCQBDIJVeql9X-uT094_8JMC73LjsWTwlLKOq6ygo29qlrnmGq0sQ47qaKOfd-qHRPgKNBkEuoy82r5iE6ir6ErhWjo-C3J3JRyCZM6InmspZnqsfHuJ0UAeCoqJ5wIOAR8BNeghYNAxDKAIjPiT17HB5J-JsiZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=epk4wXPWuUbQ6_2M-qVPFdE8mk5FLD4opgwYoJmFn2lveUECki0LTH7Ijro-T9MK7m6EtZujPjLbSVtJHsqG4lVLdyPMs5ZXZXHgRpBtClyIIihBfPlrxUvaw1UQgJ0gTwta84t2_Mql8tq1OUf_0fut62JK_B22cSkwFezVHbeO_DteYt0dXSeNB6LbjA7ulBHHL10s2w-_3qN7ZAytERSkNZtiEXbIj6iTDxuIMma6G_QJwBjDczMBhXKAkS77kfSbtc8pODqVh6_z16ZT2JJjiNhFJsHN-SYJheKOAHODoVCxksJgK2_59hN_D1S2rNZYB74ghfdY7umE8QJhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWapV8zx45gJHJ6aBlFN4-gythig3R4DE6g1v-ZO5vDR4LSzzrJDYmMWz1mVLj2egAwhYa1SFQvsdvgz7Kq7az78FBf4Fvg5y0PooAeErZ4qdaYANc6mvTggQ7Jj_WNlHjueOB68hEWCFRva6CbQaiFX1OOh-hLAXPL3GGz3qBLiVpewnPpDcqfjwUhzCQQlEapUe85oY-bNgAer_5m1vjeQbfz9neuh233Bt5JqZKq_tyHBF98bsTtUm_wN3aIcTozpXUjfbLRPOreWCre46YKkvaOr6ehzrwmcEG1uAXmCocUbSHHG_-dfm9twlTUVscJ049eT0L68Eo_xtq61Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUtoE_qNZ60rSy4vIwfIzHNgKQ5oNsFIvgGraN9wHIYZ9NlUdtif5eSFtIth2OGHZbQBTKB_yOQmm-xVVPT_5rLPrpSrpeYjM6CQMsnQwAI1gxwqwDy-Kr3Ij1kQqHKta0ZmWf1YFFDVX4ZYC2Ixo5eLQpW4EPzIR6Clu-BMn8PoEj8DIq5EmbJCUgBwkOExP-_7hSF6FnAi7oTyWXPtrw-UWWOZ0_tmFTP2-ziWrMSzH63pTTVf0TZHRq-0h7QhXWHQqAXgKfqSfuEOhWZoh4viGwCgrtpM-3lqugNZNGeCFiYKrez_InK9kqrdKUwRRD9mMDi6eX-6MNezS2PnOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=S7GJx990dVQdSC7VF-bxoH4hrM682PKVXcUHgGjlkY5fsScP0c99Fw6ACa5ea-DZwQ1GfiKT9t6wbCbaBJ7KwIoSOk7H7IQJ6E5gByw5kKx9TNSpqhiIxsHbfsoqVQOP3ZNOOJHVDehNsH-QuCkhvvzISXn7h8ZbV663tlGovB5PQQ0mSYtHMN33xmFbyBcX40jub-3Mg2bZOAknNhbnPZUpl6HK5A7bKMie1a06bFtx_S49_SPiJ-mC6hTUbe0SYIAkWMDb6899sJYICneMSsV_FwfFkKghAQNQQIfwtlUiZE0dwyS6N_4a9XYsr60yNydaet0p0OGz5gfD6dzuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsQZ5lqFrOIjpgZciHtmQA-DroRyBUWI5H9rDicPXVCZs3D8IIpj8QcA3yIoDusRCP131Vr3dGbvgKsPnmY4uif7RBCiUbkaeV3-j4VvSAzgxNypQ4SZbQBhR3H58FwqRUSq6yw6KsMxNQ1zyL8i2O-XeglTRxCyb_Uo_Buxst5xAxod8YLQdaq1qdKfICZ5GKTUxHpE-386BWtsOY39cNw5gAkhBVCHSID_YJL9qPOBT75NdYqWnIGuHoPHKGOaa0mCVHSEPkeO_sS-367dqSBit7cIFJFnYiVt7TQctRHvYUqZaePf2D4DOV8WQrNBCEm_66dEnFmIjuTc46gGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnIQvhpbTSYkZEa-JX4xr6dmQdNhPqQLtddYH2dPSBqj7SeFTx6U3HZd70R9hDKEwEPmjrDo9N4u0GFV4Ucvho6Yu_-czA5KZAI7PA3m6KWCJxN96PGyKthL1AoRs_RLgKp9oA4gdgUkx8D7XMDm876QwS3XLydNV0zWN-LPYfHzN_1HFb1wua8NYPWTYRAdSPg74XqlGup0WnxYTsthxUjHQdboMJ9teJx4cPD2BKB9ky6gj5q5icLBF2Lup16KCPTacjjOoTepgeIBWgN0NByssTLfiBZOQn9CNQQLGJidI_JtMHV6MyJpOCmryrDcISByY6RvdWycOGu3h1Gtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=MbUGYhJOT5LOH-5dagIcCh13Ula4gclyzc5Ad-gDkorVRcwL5Hqhm_O9xK0Qszmv6N03BXm69l4b2ZL4YPo8N91jac_GG0D7CSHJz3zVySMCvQoIkbP3mKqXWHmqwO4nuOv8kgL7hZrzSKntgbM4p6qJOGoFBCPqKtcI5SgK5jYQFf05BRfTWOyiFCzFH1YBOKL7Ex_svY_oqFAB5U5JGfnM6jvIu1E1YWPWUNo2mzdBVf4lq29okbH0VapV7ew6rRUqXljO1hUlNJfFamUiQWgTx3eLRNxQ4RPrn_PfHLiI6dkqagTFDgeYwzCsyK4lmjk2cZGoAdK6lL1Z9Xwl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=PgRyUHNvYn19tOMByyBJBM_Iabew5nJCI0C2yQERKVFcxwVH9a9b1w9jLA_5k-lK5ITXYUAPmKCu7mPW1DBTSlEmYBR3n8---kbuBblBwV2XH9NyZWJsQnbhE5CjxBqsEntAz7EiPu-PJWh-CSa-cQPkm74hHyOgaeb-JPSfF7VBcZTTVg5MS8pooN7TbSBzKh7HBCqGZE36Ak2een5dwYGvxhHwbvNG7AHYCIkJtNv0tiBMDlLlLSaegS7CFff2OG9i1XwFGX0bVyE3fAaq_qon1cwLLPn1MbuHKYWKJNnYyi-6VAuixnJT6vmV6ZVpymS1Xk0dBnX9pgCjGiTCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=PgRyUHNvYn19tOMByyBJBM_Iabew5nJCI0C2yQERKVFcxwVH9a9b1w9jLA_5k-lK5ITXYUAPmKCu7mPW1DBTSlEmYBR3n8---kbuBblBwV2XH9NyZWJsQnbhE5CjxBqsEntAz7EiPu-PJWh-CSa-cQPkm74hHyOgaeb-JPSfF7VBcZTTVg5MS8pooN7TbSBzKh7HBCqGZE36Ak2een5dwYGvxhHwbvNG7AHYCIkJtNv0tiBMDlLlLSaegS7CFff2OG9i1XwFGX0bVyE3fAaq_qon1cwLLPn1MbuHKYWKJNnYyi-6VAuixnJT6vmV6ZVpymS1Xk0dBnX9pgCjGiTCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY4AwX2Kce5hHFjomLMVe62l3SmJ8xcF8fHJqLucFyAYRyp61lRWZsPT_ptgkdxeKOsggYRrjP52nCMHWpDttgX1PXf2jVE5xDAuBnIHRKg26fORivrxedEwRWlEsnN7hgAaDtLOHuLyHHaelJbf8p4Lx0XWXz5GIJhoQ-x0VbPvHG8LmqKhdIv9d1CqgkzeJR9HrVHOQ66jBesZ3SxIagpPrlDyd_lLdPMnXWVtq-XHW0xVPS_6Nt8YVZehow3l0shPatHbfWx1Yd5D5KwdqaHIAiwL3-dYgkZRStKvq1_pU7853I0Rz1rbOjYqoTeROAZzq_RIR4rpeV30x2ke2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=r5fTn9w-T4xrVXBXP16aPrtP6n-XYSX-yVutRpA5O9c-D6fVbQcLODxBvx0G4TCRGBSEY1Kc1k1gnNVqf38LcF7-0bze9vpgsX3k6ycUECXGpz9P8if3PYs60vS2lA0Xj36WPoD7rfmW4845Ax2AbKzvp4vPqNEhi8U_VIJXdLDUuCfVO8bkYP0dzDMR8ZSxdfxFlHUEijuDMJtVNJ4nqz2rhMf7Nt-DzEEnFhHrFv7Im9OqCqUn0X3nDBlMMVypX5-VCPW2JTofsRp8gbPc-xKUOMFQysVOHZjfloFjc2VcWRV3TD_g--z_RJCEbIgRw9MPO9jW0sf66lsi7pwR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=r5fTn9w-T4xrVXBXP16aPrtP6n-XYSX-yVutRpA5O9c-D6fVbQcLODxBvx0G4TCRGBSEY1Kc1k1gnNVqf38LcF7-0bze9vpgsX3k6ycUECXGpz9P8if3PYs60vS2lA0Xj36WPoD7rfmW4845Ax2AbKzvp4vPqNEhi8U_VIJXdLDUuCfVO8bkYP0dzDMR8ZSxdfxFlHUEijuDMJtVNJ4nqz2rhMf7Nt-DzEEnFhHrFv7Im9OqCqUn0X3nDBlMMVypX5-VCPW2JTofsRp8gbPc-xKUOMFQysVOHZjfloFjc2VcWRV3TD_g--z_RJCEbIgRw9MPO9jW0sf66lsi7pwR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=jLyRNWb9izGho30X-DYzcj42C-m_DCvYpBOy3vq4MeRj57TyEWbiLykxMwr_guM6wLXSG3ArEPg6yew_Qnm84lo0S8NW8cANTLS6LfxPQDlY-QyvcYX9kni2T_Rothpidr6tPUekYRZoBlNmFwbDzpWZPHI86HW2o03PNTuO2vHwaCTJsp2cDuR62V-GOFbtBpDmM1IpgrVuPy4On99k-x37ZnB3zOgfiK1qUJ2IpzzTAIixgyVAVLb28kVUxESlHR59moCJm3F-knHkpRqoiNwpRFsBpehaAEFZgOCrqx0uUGuJZNadmk_SzIo9qTt2WvEflI6rM6F9adtBAhPLQauiWOf0R2ZEL9SDcaxhmhwqC7oY1gf3bBRSjAwbyZTwbp3sCBUdGg8H8ptGU7xapZZ3WkmSgD8PDlIKJXc4VtO1AekBYWP03vdqK5FXHTGiyq5RAFQ2AiNyEOmVQ-Uz34zIciGBpK6ndmpdZEzup4N8ukC1Ks9ckr1inbgjrRD950gbv-6wHQL1C_VA2OKYA92lDTp0uj-xIKfy8ocSDUgnMyI5nUs-KF2eVtgixuPRkU2QWJHePSk8F_DawDF-b6W8UyIKhLxZUNWSSpmMZvcfXmeORvXsLuAo3bXywGwrcGGbuse7PhCcr95IIJixS95XVMEQqvw3QCAw54SCzWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=jLyRNWb9izGho30X-DYzcj42C-m_DCvYpBOy3vq4MeRj57TyEWbiLykxMwr_guM6wLXSG3ArEPg6yew_Qnm84lo0S8NW8cANTLS6LfxPQDlY-QyvcYX9kni2T_Rothpidr6tPUekYRZoBlNmFwbDzpWZPHI86HW2o03PNTuO2vHwaCTJsp2cDuR62V-GOFbtBpDmM1IpgrVuPy4On99k-x37ZnB3zOgfiK1qUJ2IpzzTAIixgyVAVLb28kVUxESlHR59moCJm3F-knHkpRqoiNwpRFsBpehaAEFZgOCrqx0uUGuJZNadmk_SzIo9qTt2WvEflI6rM6F9adtBAhPLQauiWOf0R2ZEL9SDcaxhmhwqC7oY1gf3bBRSjAwbyZTwbp3sCBUdGg8H8ptGU7xapZZ3WkmSgD8PDlIKJXc4VtO1AekBYWP03vdqK5FXHTGiyq5RAFQ2AiNyEOmVQ-Uz34zIciGBpK6ndmpdZEzup4N8ukC1Ks9ckr1inbgjrRD950gbv-6wHQL1C_VA2OKYA92lDTp0uj-xIKfy8ocSDUgnMyI5nUs-KF2eVtgixuPRkU2QWJHePSk8F_DawDF-b6W8UyIKhLxZUNWSSpmMZvcfXmeORvXsLuAo3bXywGwrcGGbuse7PhCcr95IIJixS95XVMEQqvw3QCAw54SCzWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=EbDm7XHhxRIk9WDrBf4cz5TXYLKiZFBEuXIb2wpU2beeWTuQpNHViSwjHgHQxVRMXn3FGEePQ669pMoYPqhUQ2xGKyBUCmFuy2SSwvNtK_dEPnAX9OpLf0uGdpiW83AFjzkF7eKaF8BIAhal_x9aCuuYVRgXyoIRJ3Km4LGcxCPs98ZV9wgkWQRrg46rSujgq0jtwZae7AHgz74PTAhX6kVD-R9VeKCh3yJStOF1Ky_gw6S5BqOmNdkMxCi5F_jgd4zECVWjMdXCTspKXdz1JKRRsqcMjtFcfYb7FMgT14YpiLlkFblzAiy518veDvxcAatrRJPzNa6sA5pM4dAq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=EbDm7XHhxRIk9WDrBf4cz5TXYLKiZFBEuXIb2wpU2beeWTuQpNHViSwjHgHQxVRMXn3FGEePQ669pMoYPqhUQ2xGKyBUCmFuy2SSwvNtK_dEPnAX9OpLf0uGdpiW83AFjzkF7eKaF8BIAhal_x9aCuuYVRgXyoIRJ3Km4LGcxCPs98ZV9wgkWQRrg46rSujgq0jtwZae7AHgz74PTAhX6kVD-R9VeKCh3yJStOF1Ky_gw6S5BqOmNdkMxCi5F_jgd4zECVWjMdXCTspKXdz1JKRRsqcMjtFcfYb7FMgT14YpiLlkFblzAiy518veDvxcAatrRJPzNa6sA5pM4dAq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=V8sLEsMyZM_73GlzENuwKUAMAKFMNHNhdDGC1OwKoLy977Mp_sRzALeSJ82RPRuN17iYcdEaSYaPswQhHCZOQym9pueFOrYWMvjz8I-lOpGg0Z9TLMNo0TdJfNdP-VyDyrLlwRcQDqwo8eQ0eNehpL6oloXUAEW8N46RtMCp0EqBu-6NP2pfHy5_Di_-U_GYkzBbMzJ8eZgOi4TxfraMaAIuw8a5u7mi8Ofz_iZLAUXDBONdB-vM0i7etUB8l-km3Khb40m_3kXS8vnXqgXidKXc_DkbHAlVbuJdnva_kYnJCAx8Qrdpkcq-b-2im8X-za2VZ0SQUHEl5-VnWqRpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=V8sLEsMyZM_73GlzENuwKUAMAKFMNHNhdDGC1OwKoLy977Mp_sRzALeSJ82RPRuN17iYcdEaSYaPswQhHCZOQym9pueFOrYWMvjz8I-lOpGg0Z9TLMNo0TdJfNdP-VyDyrLlwRcQDqwo8eQ0eNehpL6oloXUAEW8N46RtMCp0EqBu-6NP2pfHy5_Di_-U_GYkzBbMzJ8eZgOi4TxfraMaAIuw8a5u7mi8Ofz_iZLAUXDBONdB-vM0i7etUB8l-km3Khb40m_3kXS8vnXqgXidKXc_DkbHAlVbuJdnva_kYnJCAx8Qrdpkcq-b-2im8X-za2VZ0SQUHEl5-VnWqRpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqTZJhStxB2NJBIyjpu6B6AWClF9HalYT7YeDzB0x10AImZnTtnyBiIGyvvgq1jyQpGecElYIsR4ZgzJ1jb5otCK4LAVE30u7pqZmV3tqD95GndEHsIpFPyQy_O-YltaNK-a4Kv6t9QQ-WEj-TVuRR7spyny3ElmYOynAGRgccwTy8rmgK4zhy4Wfef_tEQl8fld4g-wLnYhHQI31MEF3XaupiGjbDE6CBwHUA4yzJysxp3nTHVSgyxy0Fa3wKhmhfowz44M9Iw7UyyOush9eTG9vqiZy-pliUXuglBicXoTdOAtmTCc0jg-EcEfHQzE64mGHunYaKSEjX3aInVWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WGGShAjNRfqG82vrGLayiU0NxSiAHFH5ODlzPTxXu1a05rKkWlIrceZLAp9JnaJ2SM8CYf2637HCDkuUaUjLdpOaa-KfeHQ__r6lp0xy4rb-oNAcyrLdQa5JH1km8-YSg5QG46IHbWX60nrsReL_ONZr3tmb0IO6WGLBvDuIaq5zjeeHuAVMh8Jd8Fl0fBwd87fjkS6RGH19rfm8lKBxjbicugNtDUOAMD5ZZGSGjujiTN3gNafVQhRYXmk07uAObw9_Rmc025zPkUrFAOSEB0jj-OUDEP_KstNQUD26TdCn_pqYeuIke0D9DL2FOjdp6f-JKSEjR0DxlTL5Kq8ByhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=TsVctTXq-6Re4eGBX6v_R-eIKWeqfpYW95tb6w2ubKLIGVaP0deFZLcwlaMX3dpirITaQG0GHyS7w4Uem0h49lhV6SFh648GbzWubySe4zkPD_UVAQVsj8nFP0F4WXBGnsRvETT8oDeIiNCwK5yEA6q8Rc0yRwGgkMZmYjRMKhfG-w-xV5bT_LKJcXzlZ4PuJ8Y0NRo40Bl7SFRmHcUHTe-3EGk_RFyZ4byKb1KWy84WDzK5y78fKee0PMwj_r_GmGdGfjSHHqxlQYrEcJjV1xSaoenEN5p-kulJD8J7MbmcEBAXOlT6E_3AeKSgQAbFe8pYJa-bZnMfBzGaTe0_WGGShAjNRfqG82vrGLayiU0NxSiAHFH5ODlzPTxXu1a05rKkWlIrceZLAp9JnaJ2SM8CYf2637HCDkuUaUjLdpOaa-KfeHQ__r6lp0xy4rb-oNAcyrLdQa5JH1km8-YSg5QG46IHbWX60nrsReL_ONZr3tmb0IO6WGLBvDuIaq5zjeeHuAVMh8Jd8Fl0fBwd87fjkS6RGH19rfm8lKBxjbicugNtDUOAMD5ZZGSGjujiTN3gNafVQhRYXmk07uAObw9_Rmc025zPkUrFAOSEB0jj-OUDEP_KstNQUD26TdCn_pqYeuIke0D9DL2FOjdp6f-JKSEjR0DxlTL5Kq8ByhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kszfMqjei4e6Fb6lsm3uojkkYzjk4UqdsDLE7cYMDesSCYVABGirvPZqRbfms8UQQLvUU20vC43UbeOyy7VWMbY93f-lTJOqC7B5IOv_4YhB_cmBD7nt5OrgXRXlYh1pw77AA-kzckMuuuOcfIShAcGhjPPVXaQl2dxQfv5JKK_Zbi4p-45iR17Dm19wbRHX0W29TM7rvsh5O-wwbdYcwfNa3G7genwSz9uSW_eKN287zCDmvnN85qgZ8Lk-YOkJhDQUyWESnS5nslrumgjXXs3N4wsNAfyQbj5wjh460RIdMpiaICMM3cuY3-IjrKFdYI5Ev06YCLvGQkgR3BCaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkBg9exbEXWOpXsDNZdH2Es9v1aNwkZ4Qk469Ra0pkqGNYCdV6mZ2dvLXeTvsYTNkW0bJp-wISWN6Ya-iVo0KukdZKqblQNgplMXbhQpzDJF5UaFWr0g-TYYOOPBXOXFdCV_eusUD1VXXIVV3jmSWn1n-DA_pboIXsmbZfMbST-V1_abzzRtMChjDc9GFEtg3tWk9BEinbibt5u6w7uoJM2aaaMbBfYiD3o3OVQrqSsBVzvQfib4A0fcXXSeka2ztYZijMNTtgqLDrXtK-SjuiowvvtDACVGQBKO5SGuxFqxWp7hAD0kv0bhOpYNnpjOQ_4STzW5lNpwjWvSzAdX1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=L0E4OuL6iAvV0o4GfDnvXabJXxMwr7u5c4c2WV0wko8680V_yVsDUeFn6kj0p-3OM1-P-KKM3VA0R2PQx0NNRblDcBPY-fxQtN4rNz-v0eLG4HvMONa1-dvQzuf8NdWQbUpuX3bzwCWSnl2LlMgJm77E5BKx53j1WD2ooKF6BTaUAM-3DbCmh0wPyP-wvZeiMOtkSGNXS4SONmgORKZ9IGTWdt261h8KH7DF0RJxxWQi3WaLSimiMIgR5DQGAJCN0ENfZOmsFlEaeYI4TSSAIYqObkjp6nghLUeqZbmmXbApJIrVBFeDF025n6YOY6bYOm_cg9acxW-hx-oDO02OWIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=L0E4OuL6iAvV0o4GfDnvXabJXxMwr7u5c4c2WV0wko8680V_yVsDUeFn6kj0p-3OM1-P-KKM3VA0R2PQx0NNRblDcBPY-fxQtN4rNz-v0eLG4HvMONa1-dvQzuf8NdWQbUpuX3bzwCWSnl2LlMgJm77E5BKx53j1WD2ooKF6BTaUAM-3DbCmh0wPyP-wvZeiMOtkSGNXS4SONmgORKZ9IGTWdt261h8KH7DF0RJxxWQi3WaLSimiMIgR5DQGAJCN0ENfZOmsFlEaeYI4TSSAIYqObkjp6nghLUeqZbmmXbApJIrVBFeDF025n6YOY6bYOm_cg9acxW-hx-oDO02OWIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=vtzU4bYmVR-cgLIe6xUd9IZVUoRz3CUVvKljt5IiQibP_ewkBFR2wZtZQsBfaR1YJCWFuONhvEr2J9VXUn5rmc8J4UVCE6OpR9RJiX6IRmdhS_o64CbY_fzVySj1XjagaEzWlNb-gJlZkzNcAn0VBkJ3axIVtksDGeqHG4Wwf5FaVrsqFVgK0owE8Om-u3h13Rh3GFtXZ9FAezyjJZOwJ0VLneNPLnMv5hGYTvD0X3zx6FZLPJvmXnU_h3Jbq9UtEe8vdZaUmFitwWBP3eDkeksbIbhpVQUwGcBq7cl_QoP_ZnnUDk9g_JEt5rgFyOF521R2Xf1U0TK4m3lsu3nlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=vtzU4bYmVR-cgLIe6xUd9IZVUoRz3CUVvKljt5IiQibP_ewkBFR2wZtZQsBfaR1YJCWFuONhvEr2J9VXUn5rmc8J4UVCE6OpR9RJiX6IRmdhS_o64CbY_fzVySj1XjagaEzWlNb-gJlZkzNcAn0VBkJ3axIVtksDGeqHG4Wwf5FaVrsqFVgK0owE8Om-u3h13Rh3GFtXZ9FAezyjJZOwJ0VLneNPLnMv5hGYTvD0X3zx6FZLPJvmXnU_h3Jbq9UtEe8vdZaUmFitwWBP3eDkeksbIbhpVQUwGcBq7cl_QoP_ZnnUDk9g_JEt5rgFyOF521R2Xf1U0TK4m3lsu3nlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=o0b_JB9K69n2VVRBJ1unOKhXw3dAUOJK8usGkfHZ1BBNQhJjVgfkAP37qPGDfSjYiHNIGk2uDeXmg89xiwOFbw29fgXPM8iaAWYhdXuDEx7dHpTSOT8Vb3wwC4M1KRmCEaXh2gdiw70eySw1PWxPPWFNZaupDdVnSjNvZe77kfM_OQxVFiuEJAYkpUTzsr0dIuO75TzPne6f49_IyxCXQlq1DKtYi9-JFq61vVsdTGNYjKe9mEDU5I_MbrZTSBk6Ice47O98mAXcKDagrUpPmVDnlL5ZRh0v5Cs_xfjFnpHwaiGcWF9nBMZb-vh3gtdIcrj8nS2Dabf3uTGqos8qXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=o0b_JB9K69n2VVRBJ1unOKhXw3dAUOJK8usGkfHZ1BBNQhJjVgfkAP37qPGDfSjYiHNIGk2uDeXmg89xiwOFbw29fgXPM8iaAWYhdXuDEx7dHpTSOT8Vb3wwC4M1KRmCEaXh2gdiw70eySw1PWxPPWFNZaupDdVnSjNvZe77kfM_OQxVFiuEJAYkpUTzsr0dIuO75TzPne6f49_IyxCXQlq1DKtYi9-JFq61vVsdTGNYjKe9mEDU5I_MbrZTSBk6Ice47O98mAXcKDagrUpPmVDnlL5ZRh0v5Cs_xfjFnpHwaiGcWF9nBMZb-vh3gtdIcrj8nS2Dabf3uTGqos8qXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMvFEvmXfrLnHSHSi03bWYaZq47GIokiuftX47CEoGYOc5jIlJYIsFhof6W2OeGsy1DmPbfV-gbahVQH2mZY1g0xwoLlTD4Ukkma4XdFvkqEFCukSLWfZsT1TUBkeMayQbjL_IZAFwZ5MKzWUPn1S_83vCJnzHBcALQdp7IA8cvw1nAY1MoTmVmrUmKIc93YYCw6SjqbkDQ4T-7MR4G-x9Xqnldc-jIyKKCPn8PteyCW9cAk9vCU9NtOdmWLsvopMMyCvnvzYStMox2vr9LytosP4PelmS8Ve-8XTL0G1bGmk82yRv20vMyYdrUghDfvhH5cOen62-zegVBcMInr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4xzfB0n6Vw0U1yt3qipwvpO56vew4LoX481imqN4AhwxkpPz-0oGyDYtAsc6m0Wc8ijVhQFmvG74Tv_WQ-OQ-Bu0LUdm0qkDGexoJgGHQsvUhXHRL4KAjbeKOq6SX88ZmXeRO0agd3CwaNIfzOli35ulVchW-BYXYKBAOshPv96wxFLpUtab-hBDhSdDcapWQSKmt4XIoog7BZiPI-bDn6ltGUkaRxXeDNuqjo862mKuaZ8vD10xZHMwvc-4zEs1yB4zBNIn53VaJRZV9JBWP2lgqpBeWO8gynYlwemQOHBp82tD5lltfGDJyADTjRIc6EJZFHpNg1BuRjcOXLSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PimxJFDkkX3vWKGUDpgFiE5pkgWRzdFPqhNKRA7TTpHaB3Lt0njIFWvGS1PoZMcMAl-vjdyZYx4g8jYTkrMQAu-3ROrLT4v2YIc8Z-Y7Oukcvv5a-aDzNSgLxMxmi57fROC1mkSEWccPUwCtHZtwO6EknXTERvsqJ07UsWMjZERaNA9ZNkdaIoy3meDr9pnKNGMOti3HfBg9VWzSBnPVIGGd4-OGLiC8QX7vLuDPIAGs6Hn7jw2J9yl4PZ6pjcWuJD0JIfcFfPOIU0mF6dpiXsZUQtlRUpOhQsM0fembRhozBypmmITs4NDepAtzoSa0sD4Y-jAheOoA_IvWIAp2tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=UkBOfzS_S6ORmOpxRKyWc6BXm95Wmim6mpQUJE2FGk8Cnzu79DUGSKXHNCjAlX60jA9uzfcFok-1Vzs44izITdGdzO6lqJdpfelNNl18Vbhm5Us4zOyXu2w8Hb9aA1AKfwLmeHh_ttj_SWQyDFnCYAxz0z8nQTKUUhW-Zkunfb-0ooVeseUH9_VCrbGwKxihY-0Eaq8sE3ZPh6e2pEDl-NBwaP4niYz4DN228MEyPwj9UOX5skU6g_sYt4WtSvZSlxCTuGgsrOFXK8GHpukLLHCY1Fxq_E5JugUP1axq9CRPzDReaf7Ey9ZPYqqpGWAHFqQmSZuYmX_-e-2L_0xIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=UkBOfzS_S6ORmOpxRKyWc6BXm95Wmim6mpQUJE2FGk8Cnzu79DUGSKXHNCjAlX60jA9uzfcFok-1Vzs44izITdGdzO6lqJdpfelNNl18Vbhm5Us4zOyXu2w8Hb9aA1AKfwLmeHh_ttj_SWQyDFnCYAxz0z8nQTKUUhW-Zkunfb-0ooVeseUH9_VCrbGwKxihY-0Eaq8sE3ZPh6e2pEDl-NBwaP4niYz4DN228MEyPwj9UOX5skU6g_sYt4WtSvZSlxCTuGgsrOFXK8GHpukLLHCY1Fxq_E5JugUP1axq9CRPzDReaf7Ey9ZPYqqpGWAHFqQmSZuYmX_-e-2L_0xIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCJ90WGigNrT5uMBYM5ck4WOYSTYKAdJRkhI3dDT6c0EpBDWLulGscX_qiSw9t-V9Wgu4fWbKLb6dvs1rjReXSVO8jO8ZzKRJy-QgjrFkR5LNT3Q2Nm98W2_icNZXWH5VlZf7ixdJwMffuG8cZXruP2qfwZDeHIkZ3hhdD2wqrDDs4jccpaRjyiG2xiiDiSMybnDQzRK8Z3QXpecloycj6aJzvBP-NF2GalX3-tYY9cgspIbjSqcm4fK6ucKNnJFYgeTYVCxoF53Z2JbMzRPrUZJcQllOWeJliP-ebPWW2ZkTr3q0CuhkrWHfay9lMOa1UEUsMaGGflsc4qd-s2zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bT26vWaSwtxuDpWFb55jMUWqzND_ATh_KJuXRjcUQMsMJvC07KG4kPuvuiuO3u-eEz8IvzQBsUdnLa5O1XJ3h1szKC25CIvJnso5-m5ZyWV9ziL9IILXn_hj2NV-bwGYdkxrv90SUjlfcuHIht9J7CVLBwTX14yPBpAZJbEF_so5AbTgAnMf_o2TaPcZHuCO6XL7ZD4LhaRSXHwG9_RcBf1WGEhUj7VEIrBsWiqU9OUDXP8XgYqjQfj8RvbtJT0gWcMQ8pqxaub7hJ6QyDNifSjRqwMzsQDAGJ5BdZdXPfIvhNSlrkzvOab8t-exgh1FnuStfpy1kPi98-FyxmdftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bT26vWaSwtxuDpWFb55jMUWqzND_ATh_KJuXRjcUQMsMJvC07KG4kPuvuiuO3u-eEz8IvzQBsUdnLa5O1XJ3h1szKC25CIvJnso5-m5ZyWV9ziL9IILXn_hj2NV-bwGYdkxrv90SUjlfcuHIht9J7CVLBwTX14yPBpAZJbEF_so5AbTgAnMf_o2TaPcZHuCO6XL7ZD4LhaRSXHwG9_RcBf1WGEhUj7VEIrBsWiqU9OUDXP8XgYqjQfj8RvbtJT0gWcMQ8pqxaub7hJ6QyDNifSjRqwMzsQDAGJ5BdZdXPfIvhNSlrkzvOab8t-exgh1FnuStfpy1kPi98-FyxmdftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=NA-26Oc9BJY-c76MUwAQm7cyegziW2CtQHfVNLeL1m9KlndQg-JybDa2oBEpyfb4EXQZBQPHwvJ4I4TuIIQx6FPV8bnyeqzpufwf2NKgJa56vBVhRbO8iHlGgbBWsGBfxE2jARyfLfGhhR62V6Htbvw6Zxhlbf86n5-QrtJdK8ByxIcm_35YFMGNqOM3Nb-Q2cnnzPGV07eIjusb63Ltd8riuMNfQrRPfOxlL0e6sXvXrVVDMP0pV0kxLN8vmItiXnsXD1B4jj_pTfto5om7Wi_unRaSG80FFgvfCB-6-LP22NFcjd8IEdGrBT4fIaoG1E7mj45x_82SXQD_FR3dHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=NA-26Oc9BJY-c76MUwAQm7cyegziW2CtQHfVNLeL1m9KlndQg-JybDa2oBEpyfb4EXQZBQPHwvJ4I4TuIIQx6FPV8bnyeqzpufwf2NKgJa56vBVhRbO8iHlGgbBWsGBfxE2jARyfLfGhhR62V6Htbvw6Zxhlbf86n5-QrtJdK8ByxIcm_35YFMGNqOM3Nb-Q2cnnzPGV07eIjusb63Ltd8riuMNfQrRPfOxlL0e6sXvXrVVDMP0pV0kxLN8vmItiXnsXD1B4jj_pTfto5om7Wi_unRaSG80FFgvfCB-6-LP22NFcjd8IEdGrBT4fIaoG1E7mj45x_82SXQD_FR3dHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=bqQYwjSW7UVTXdmc0KjMzD_9J8Afw4FbZgW7M6XAUpO0o1HWaxXd5pr8W6VOTsZA5ccnsvp6P3Z8FexQBGcIroi4kABaeSUWLKi5u19JZFNyF-XnV24uBNNRlvmHbndDSmgX1MGYbcJtDfS9Jh9EPeuYYRtSmYZGdE6FZQslc0rqTEvRg-9_zyeojXouv3rYtIh6RF1f94TZw7LHHody4Tcp0GRupJ8_rJ0ESxwIcZpoKLdcQjlV1laaMQ-83aimQDIHToGeup0IGXxoGkvgKmBbJbRQNs9GAWbVjFeTmsGF7KIHPd2ff2fvx5-6lsGW0-ktYnawdOv2rwtqsjg4ErSeZAhXDpdZUzo1yC9d4GEGRI58WwE88QzT_KqKqPTOMyodm7BQQW7E5Y2PRi4HHGjm43l4e7ADJlihZCU9X-mmqrikWGRiFkpN06owZ3HlOuK2P48sKiDYO4_vFqeRlC65mTcQQTMTJ82fIcRWtJC9B1i7_7Fg7h7JZTlTUdNIKG_K54Uvbdwk-gsf5NBM-IG8IJtPU_zEOtjnrX4hGqzDCDms2G9q6bgEBgleQZbqI00PHnYBTZ_a3VQizBuXf2qUbwXMSLQTpvkzepW1QkqZm0clBlZhnEoEXNsO73B0gu2H2pEPl7y9PtbBowjZKDUSWdwQINyEt9d9-eUfC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=bqQYwjSW7UVTXdmc0KjMzD_9J8Afw4FbZgW7M6XAUpO0o1HWaxXd5pr8W6VOTsZA5ccnsvp6P3Z8FexQBGcIroi4kABaeSUWLKi5u19JZFNyF-XnV24uBNNRlvmHbndDSmgX1MGYbcJtDfS9Jh9EPeuYYRtSmYZGdE6FZQslc0rqTEvRg-9_zyeojXouv3rYtIh6RF1f94TZw7LHHody4Tcp0GRupJ8_rJ0ESxwIcZpoKLdcQjlV1laaMQ-83aimQDIHToGeup0IGXxoGkvgKmBbJbRQNs9GAWbVjFeTmsGF7KIHPd2ff2fvx5-6lsGW0-ktYnawdOv2rwtqsjg4ErSeZAhXDpdZUzo1yC9d4GEGRI58WwE88QzT_KqKqPTOMyodm7BQQW7E5Y2PRi4HHGjm43l4e7ADJlihZCU9X-mmqrikWGRiFkpN06owZ3HlOuK2P48sKiDYO4_vFqeRlC65mTcQQTMTJ82fIcRWtJC9B1i7_7Fg7h7JZTlTUdNIKG_K54Uvbdwk-gsf5NBM-IG8IJtPU_zEOtjnrX4hGqzDCDms2G9q6bgEBgleQZbqI00PHnYBTZ_a3VQizBuXf2qUbwXMSLQTpvkzepW1QkqZm0clBlZhnEoEXNsO73B0gu2H2pEPl7y9PtbBowjZKDUSWdwQINyEt9d9-eUfC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kWOtbxPw9aY__2Cz37ZmJgSBm3FpKZkaMrbn-8Jur8D-LRCJVk9n5vS7mkcWNi4WN1_aPseBj6VrpkQ54TQgqIijKJQtD1h95kxtcGX7BPn0JB7C4rteFutItERWzuLPQIxTow0-aMuYoP7zmr1id3UPFovOBz81f2p61otMK7HDXHjXqTRMi5FwMjVSwHkbe1j3VUl1RX8yK0PMRahHoFmue160IMmPt3jTKpqRIhbwS6l9nh4tLL8SLFHGEaWFs1v8-rB_H2g5A07pzoII-Dh2GoiH8rfuxjdzvaIhrjcB4uHPJr82SsAdyt8TQzvXA1NINb06qaWysmzRgl5U5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kWOtbxPw9aY__2Cz37ZmJgSBm3FpKZkaMrbn-8Jur8D-LRCJVk9n5vS7mkcWNi4WN1_aPseBj6VrpkQ54TQgqIijKJQtD1h95kxtcGX7BPn0JB7C4rteFutItERWzuLPQIxTow0-aMuYoP7zmr1id3UPFovOBz81f2p61otMK7HDXHjXqTRMi5FwMjVSwHkbe1j3VUl1RX8yK0PMRahHoFmue160IMmPt3jTKpqRIhbwS6l9nh4tLL8SLFHGEaWFs1v8-rB_H2g5A07pzoII-Dh2GoiH8rfuxjdzvaIhrjcB4uHPJr82SsAdyt8TQzvXA1NINb06qaWysmzRgl5U5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7QC7-ovNDyk_mFtruaACdLWm9IJ2Qm4FSWfjI4IDxszGHI5hQixIwsGZOtJzQ-DJ0EAbjwtX-F8KiAPf-Tp8Spw6VBjTzXmrjglPjjpgBFoKQPq8VKiLK-iMOtLI6e8_JRj2aLJV3K5VxspNIAF3MySH7cneWm_9CRtH-StDZt10gb3ZpsJ9H3bXmoVTUl2AcISRtvN4nqGD_5yC0uExhhDTnbV-3BxmqG0Te-XrbashMvOm5bnOHc0_4lEJxG2zCiGhs0zBx5FSKTUtM6LFAg5xWUJJo_rLMWNmoTAykMcuA18GbeKS0hibiiTTpakY2jCrVSk9fymztr7R0Xd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6nDFnLeN4VLLVAQvjtW5GwzE2EJTRfpchTKARq-elcc4xcdQQMznJZAd0CCfSNWEggANif4DnqUrr1jIlRsq2EzrLlZg1v4D8azhWUQMrTkidKgOOuFy_vuZSw3Ipwaet9XukbINWgw-XGR0l_pdLljSu7mZRVFEHUWAQJAeHD7G0lVQZvNAq_EV8c3xNl9--18FEbvpiO6PdLJjPmzpmotcISG9aAeSCcVeITmrwdc1igiwGx8zoPen017QrYgumJ5WFbzZucWK3xoYXarY8bzLM71HW-KFEmAErLXZM12TcPo6SgNP0mZnKC-IP2prbFmAs6p6wramCa7zgYJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBNjUNFgzNOm267nYcACQZ9JKJucxbAnmfUrs-zy7SLNOCbV860do4fQrGKvHxBVOAuU6v8s8mUC2hd7oAkoixUkBm69s1K5nPxLkylgOInxntpZat3ZdtMiqXleyWL1kIkOTe3zBo6oezK8FD6-FwiJPPJRkZyb8IeN0znS6THubcaAP40Uml6QGoEN5_U0SR8z-Epfnv1dsNzSsxBf1XaLIYJgzngL8Mn1PtLCUur8e8IUBhNT80KPJvOj8W2K0kJ3sDu9Xed2jPdgzOEbYp7CHNn-92EUmJz_2_FNIJXKW8yXgw5O-5Ph9UEesHLBvp06nRhT4_cSOAmOnuXX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbabiQXapfgFEZZEH-8sJk4x_hO-LaxISzXeG6eKIOqhPtBpa8p_a_npbzSWclc_LTj6RSqVaOHcrHBynOPy9dwyXLlKhFSf9xXs4fUyZPwVcD4Rq0cVFb6vzn3NA-v61r2s_Z96hhxFtUSlk4ToPeU8tzWQaPcnz9G_wjFBlYYrBaxDQAXhag6-WJOfrz5OeChfXv-0tfV3A4ZJUS7RyLxnnhfTEJb4ipQqMqdgruQkrHB-Awturv8cYlOZM-i7nGdDZfGz0paYBM1UoXPlk5wFyDkQll1-NGfnRn10ZutnoZS7oTyDI-0_AIeWWfmlbogBmaBBaHASyKwiUDAKvw.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPrBiQbkGKrtnGYmv6dlfg5B0iUPpcleSONt6-MNh62M5A_MVrMR-n_5NRAWn5Pe1ENdKussvg52XXTLSPXklzi739kNmd2lxbEHEGbFZIM2KjDqV3cwKdEBw8GoE6hcljbowHlHv1LGQXTmXPa5bD8HjN00WZGU9okx-slyFRgiF4aC-lKH-Dh4G9B0rOIKPyCE_QqnpHyA7k3Y5YSsHxWGeO4wRhMcTjFz538Z_mWXkofA-SNUCAxzfb9xQbe665ozWAWZu0Aec5YD2b1WF0MPrBAl48Ofioch4pinzUGa1w6RcN9UJ1qTaaKqKAchGZ16Zv-aIeRtlwyWrwhK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV6NfxfpxVKuIm_ldeWusSXqcArVxYhCxnWKaEEZMA3UR1QMflfejobaHtnM6l0vSKPsXTErzCVbB_IYhvKu6QYuIrMDKn87lqd8tJH3EfetiOREekgvwPCu7ssAVnfynt3xC1LM1t95BZlJCpd8wU8DRuiJgnrCO5PfJwMiZ_PCvlGY26Ux0JB7PTUBMPULMBz5PAwbEXkWYlqIkJrzCmZSvt_YtlaEkapHMq2OK98xU_yjbiEm1iYRPiNj7rGisZb5sbGgnIMG0M3Jn05TkTJigY1gKxouEOOt_9yXdR67RhXpI8rYR31k3gYocBajCPGMKO5xwkyHE7_mthKROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6_xHKagLvFPOKEGDz12oOssnPDZjs7pPpqk5K5ecDx0KaJnSkmyP7HgL73TgtSpadIHvrgsbHmkoiMC_YSpvNknxcyVhRtp16XlebWZm9sD7QBoKSQSnFzCcwqLxG46D4u-naobjrZUmcMPI1JWGOtguW2mXfitdFBC5n5Xv_5SlxzgFBCVeKSPaMT4bAGdErnTPNV4y2HrFeXrXKTJ8wqfOHXhRiV1H-fQrZSyddTqNWwb5wDeagIqX-tflvSWbCmtUDsvN8qL-oPXL6v6WnC5MMbrvWjF528Oq0FglnA3aoyY0dRRZrAXDuicao7_B3sf2BwETfCqcrkertpWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2l2xuEpPSxHk8uAvuKWLgj8GaZB_yTnQJ5t3baifRjnO1yi5clCek0-48281aXzFaFhRd9Vj9ecpcZmODnqDUzAXKbvv1Z9hp0dOKIBFUsp5nLyvT7qD6mb-o-_FY272v8Heg7MWRL1-NZgvGYkPaBPYfacYdmunVi--5BB6K-KVtSO0Z_CIt4tzohQwv4ZfYWEuEEgSlpHdMi1pHTgLnW3-kks3pvGI1go2RL_m85xoRpBvelZY0uiGWmQPYTEmOXheZkcLC_aOOaVrO-9oyJdaeQ_V2VW7XAlDkXMtlI-CIw0ItrJpPPN517DfU83Vv9d_va_NxCGZY2GVhzdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=Yu5sYgPIEcqw34Nx3U0N0tkeF4y21h_v0kFegNRhXKg2_oGnNufiS1femiOGo72d6yQzlF6OOW9YJnrYoivNzDdPNzqxpprF2ghBpxd6T-iAl8CFNfKhbLmWdLuUU_JzZ494cnJqYUFEUoS3HUdvPt59pHLa7YFQVSjtUyObOPdENP4lUldNfx-JEIJgGJgUTu2OkRVIkQ5HWT_5_Zn7DQlpvSuICjgErasY0bzL-53aq7NEIeZh0Z1Zk9e8bQ-sXxfqhAZUA_CNP3LssuSt40YiOpMHONMZUpHdCMm4O1TH6Zr9Q12HfOcRoivzrTSyHZa97LydQpa_OCSyMz3hoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=Yu5sYgPIEcqw34Nx3U0N0tkeF4y21h_v0kFegNRhXKg2_oGnNufiS1femiOGo72d6yQzlF6OOW9YJnrYoivNzDdPNzqxpprF2ghBpxd6T-iAl8CFNfKhbLmWdLuUU_JzZ494cnJqYUFEUoS3HUdvPt59pHLa7YFQVSjtUyObOPdENP4lUldNfx-JEIJgGJgUTu2OkRVIkQ5HWT_5_Zn7DQlpvSuICjgErasY0bzL-53aq7NEIeZh0Z1Zk9e8bQ-sXxfqhAZUA_CNP3LssuSt40YiOpMHONMZUpHdCMm4O1TH6Zr9Q12HfOcRoivzrTSyHZa97LydQpa_OCSyMz3hoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=i4t2jTPwvMLwxWfRRjIYsSqB-Koj-zGahgCgHe9j_idigQ5oGhffhzab_dcpagorpTqJmAGUiOZFJuTaM0so5PevkDUQlddOl9GluaXP5JcWRSymFuZtpZlAmEflIHTaA0yHwtwpivjhWyZEUVYDidHPD3hadaW_P7YQKzvApqISZbRQqKwNGV9tETiyxCF6tmX2k74nKu-1OLB0BVZEsTTtG5PBPHz2tHaxCk7AZD0rzvstPDhimfx2Gt8NRmIjixGVG3MCLgsUXeC2iFcXTUSMXnj6O7fE-qd9-Yw0bDMvRslG6xTw7cySEjfDncIoPJ4ypHKXJixnyETDlNXNdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=i4t2jTPwvMLwxWfRRjIYsSqB-Koj-zGahgCgHe9j_idigQ5oGhffhzab_dcpagorpTqJmAGUiOZFJuTaM0so5PevkDUQlddOl9GluaXP5JcWRSymFuZtpZlAmEflIHTaA0yHwtwpivjhWyZEUVYDidHPD3hadaW_P7YQKzvApqISZbRQqKwNGV9tETiyxCF6tmX2k74nKu-1OLB0BVZEsTTtG5PBPHz2tHaxCk7AZD0rzvstPDhimfx2Gt8NRmIjixGVG3MCLgsUXeC2iFcXTUSMXnj6O7fE-qd9-Yw0bDMvRslG6xTw7cySEjfDncIoPJ4ypHKXJixnyETDlNXNdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP-MDEsM0TtBv2mSJQ_1foA4rFmXQkoDTEmDAQChMappZZYykxhWnP_379h0qbybD4N7Wk_5ivFK3cdTIInY3V_3Lc5_Fmb2fzGmbjH3nxNqwZSEhu20XtqmKU6VMtqGj8DXRAigA2VrIeJwPcuzIMuxNEvNTFTrwU5QCqv_qCMrycPrEgITJZpsOywLj5ddl8P3dS6BDbT0hu4YLQAPjWolfkAuyZKVV5RusE6RRaOVJ6qy4QE5g6G1AJz5dCFf4SHD5rpJP0AF80meyoaTAjv2kqw55NX5CYbPFcBXsx45Rog5KhEwfMFVxX5YElDpg_tOE29hZ8WfBICR8InAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZdHXWvQf9WBA-lotES25nsvTgY9jijThVftHc56Ra4Ozdcz0F7_kSpABh5XQR_t0NtPuYf-f0POtpqe61TJ63brd5sPQmP1y54WNfD00Xs97SXyZpcsxSPWXRAjQZIx616eT9dL8CBDHP7RYWmiAQHGx1N-neJMj93-bL3L1B2PBeP4ejDx5RmlX1U1n2taaS-NTz-zC8WCD6Qt5cCpCvrNWi8bTszshOPKm00_irsjZphJ2RXYFXvvIbW6jnicwO7-9DsYmIoi_SYIeuR8JzlxBarovrYTlTCPPaGxbYrgqlE5D7vT_z9ufBqQRg9Bd9HQUoYqCTFJUFITvDO7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2aOFprJrdsCNw1-Sc65Y-MWSsAxSKUvPh-yISOWfCtHdQSabuyDKzIMMy08WSJpBpbuxWXDf8bu5vFlgJ-PXNE1iqLCqz2-Q0jWtFU_1AOrE0nQz8h-a8b9F0WnYDo7S-SlI1W4eSfmL4vLvsiMF33CLzcgFr_Qj0fYwHN1ygCgZdC3DEfJcCBZzo1kM40TUp2nyJ0h5T17GDjOc1QIHMf4W0VUmAJjY9JUX7vDaZlWZCyAu7PgvIajmEWF9ux-TaZU4WK1dSdPPisQiJpzJhYxjzdBNwd2T2JgElnAT0vkgzT3ViEyLtEmTXHQ1vDw1ABmuc7JdZpKzzwKVqvOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=riJ1cvm4nzr8vrXwuxO-weH0_vLh0NgS8qu4kDlENMD7pkX3VlHf77_FbLR7aNgYf-NXhgjo8GIpptx44bU80RIM-uO1rwlsnUKcTgZYt9WGZBvRQuXUEOI4TGzjbb-XzfVGKvVjIqN7o_d8LZ16-OxQCWHC6JSHqMbdRmC24JB4CKQf9iu5Xgik6DDJ-kmiPQAfP6D5kT2BpCqg4sOXs3Ny6bgFFrzdA6fqlPPpOBIcYGw8051B4mdUfrW6axEwYNFbZjt03EwfAQCOXtxizMxlh89KCXnGdk_Jfl9rYbndx_eeT9OgIrfG5s25nbI_osN6O6pUx1GaTP_Vn_nbBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=riJ1cvm4nzr8vrXwuxO-weH0_vLh0NgS8qu4kDlENMD7pkX3VlHf77_FbLR7aNgYf-NXhgjo8GIpptx44bU80RIM-uO1rwlsnUKcTgZYt9WGZBvRQuXUEOI4TGzjbb-XzfVGKvVjIqN7o_d8LZ16-OxQCWHC6JSHqMbdRmC24JB4CKQf9iu5Xgik6DDJ-kmiPQAfP6D5kT2BpCqg4sOXs3Ny6bgFFrzdA6fqlPPpOBIcYGw8051B4mdUfrW6axEwYNFbZjt03EwfAQCOXtxizMxlh89KCXnGdk_Jfl9rYbndx_eeT9OgIrfG5s25nbI_osN6O6pUx1GaTP_Vn_nbBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=mhI5KL7ajotSHRfg0X9DSDJNM9WsytgCYOuVUlmYolyhR3IqZNAhshbPZFQdrWxLfvp68Y8aumyxsToUFIfbVIRshSSdVd52A5T5ObeoFZfAJ_1BxZfFWC79fixjRqJAA_kH1O_fIO8Z6jD64jyxWNp89fzqer4BxK2fFb5aK1sivG_MpersP_7hYjhZAvw39GGaFMp7YRvl-ITtfs_JOibPQFsQqseQdTASaA1tvDtdmYexMIY3rg0EmOV4cPiSvYwp3Go3wHHPyqDafVyLSgVLZjLMGmFQXPVedmxPT0hlfr-LCiewFU5a_G_CKdCgunMpQ6NsDt6QAGcAaZYiAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=mhI5KL7ajotSHRfg0X9DSDJNM9WsytgCYOuVUlmYolyhR3IqZNAhshbPZFQdrWxLfvp68Y8aumyxsToUFIfbVIRshSSdVd52A5T5ObeoFZfAJ_1BxZfFWC79fixjRqJAA_kH1O_fIO8Z6jD64jyxWNp89fzqer4BxK2fFb5aK1sivG_MpersP_7hYjhZAvw39GGaFMp7YRvl-ITtfs_JOibPQFsQqseQdTASaA1tvDtdmYexMIY3rg0EmOV4cPiSvYwp3Go3wHHPyqDafVyLSgVLZjLMGmFQXPVedmxPT0hlfr-LCiewFU5a_G_CKdCgunMpQ6NsDt6QAGcAaZYiAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=lzfsM9T2dfMDm4fwcmiNUDj5JyjuKT2OcRNdGWwOIk4Vo9AG9-AMyOe2iXxfZ49PO99I7ohZ6iLpxdzo0LoT0LEzWPJmOKg_ebFw1Mc3i_Ylm4x9dkQi326IrP38slfVPiPQhVDtpqzPdUs0H23_z6MDkijbz0j3ydy2G9R8oJqpnKMG6EoXUK0vXup2i5UqYDJ432v-cgniGStNNfIgCXuymlOjGEK-yScnsImu7NNr255vtxp1vT2qU7LRaYbe1p2lImXA5fJx51PEibP_GVdRCea5P0AJmblIKS-HoWwLByXhTk1brombtXp8gHelsHWyo8rMugDrdrusML1MRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=lzfsM9T2dfMDm4fwcmiNUDj5JyjuKT2OcRNdGWwOIk4Vo9AG9-AMyOe2iXxfZ49PO99I7ohZ6iLpxdzo0LoT0LEzWPJmOKg_ebFw1Mc3i_Ylm4x9dkQi326IrP38slfVPiPQhVDtpqzPdUs0H23_z6MDkijbz0j3ydy2G9R8oJqpnKMG6EoXUK0vXup2i5UqYDJ432v-cgniGStNNfIgCXuymlOjGEK-yScnsImu7NNr255vtxp1vT2qU7LRaYbe1p2lImXA5fJx51PEibP_GVdRCea5P0AJmblIKS-HoWwLByXhTk1brombtXp8gHelsHWyo8rMugDrdrusML1MRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=UMivwXDHn_ccHrl9DMqfwfcDPRLAXaBZB9d1m_xFOmRqFHqrXGGPufJUcuUmHs0235-e_Hv9Y8BmHQ4AS-GT-qiyAivXflXMKMjxoCJQJldHnZiR0oIgpK4jpJ-tSZh3zZnGHt73cFuWsuWXFVykzxuiHXj2gZybWzzl0c96ekt7h7oMa-nRGLIDEZm0c_WiZNyAle7b2U_ajEoLeR-Q-MrLbPPwKdmh7IqgCEjd4UfLp30HzfuJGxwRqD_5ZkplJGdJoocugfczR3NUPV7SpGA0jNkECKwoSmywLZkGybIv9TANFR1-X94dkfexFRSuHlXrXp0WrXjK5sJvjcKnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=UMivwXDHn_ccHrl9DMqfwfcDPRLAXaBZB9d1m_xFOmRqFHqrXGGPufJUcuUmHs0235-e_Hv9Y8BmHQ4AS-GT-qiyAivXflXMKMjxoCJQJldHnZiR0oIgpK4jpJ-tSZh3zZnGHt73cFuWsuWXFVykzxuiHXj2gZybWzzl0c96ekt7h7oMa-nRGLIDEZm0c_WiZNyAle7b2U_ajEoLeR-Q-MrLbPPwKdmh7IqgCEjd4UfLp30HzfuJGxwRqD_5ZkplJGdJoocugfczR3NUPV7SpGA0jNkECKwoSmywLZkGybIv9TANFR1-X94dkfexFRSuHlXrXp0WrXjK5sJvjcKnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=Nn_kZwRhLHWWjILTvfamx18Q0b8VIBoyTMk5YDeUXMwDPpy-mkbSDG2Hd8YlvYuz2HNfLMYnym1LlNgo-SIb31SmQr1flbSGW5ZSEYdlzpd2LrA_-mCZJZhgZN_jj8mUvwBNVttBLWb5LrF9Cgp60rD7WfX9ERHseX_DKz81AWTU5kaO6dBI-ErXxaClVoTz-hjmx-MZH6p2zAkK16hHDSOzLx0XNoDNd04kjEScOmDd-TH1xYt944y1YvjdTsRMSS1en3BAZxbxQpOclb8ySFG0bq0QXJnjHofCBkCQOyWzkZgqPXpQFIDXNfTdXsWyLqOdMkwvo1I7vDrKdSsZyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=Nn_kZwRhLHWWjILTvfamx18Q0b8VIBoyTMk5YDeUXMwDPpy-mkbSDG2Hd8YlvYuz2HNfLMYnym1LlNgo-SIb31SmQr1flbSGW5ZSEYdlzpd2LrA_-mCZJZhgZN_jj8mUvwBNVttBLWb5LrF9Cgp60rD7WfX9ERHseX_DKz81AWTU5kaO6dBI-ErXxaClVoTz-hjmx-MZH6p2zAkK16hHDSOzLx0XNoDNd04kjEScOmDd-TH1xYt944y1YvjdTsRMSS1en3BAZxbxQpOclb8ySFG0bq0QXJnjHofCBkCQOyWzkZgqPXpQFIDXNfTdXsWyLqOdMkwvo1I7vDrKdSsZyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl7KVKK6pwyDFiYwco-a5hlN9EypmzSY5oQIpO3snqkXmihEINKQgFYQL82hUfmXRztXEEMorQLy4WUmUZxoi1ZUAbaSmrVwUWrCrocnMhR9WLwuF4uyDR2ki9VfAPvoZbVZL_ssVKRrxt2zKtYTAy-ihfi076hG0OwzsRGVqRkghAV71ykXlymKX74Cxj08rD9wDp9fyEm0tWXPHCuVQY__7vKljDsEg3B2iejYp2iw8KgIXzBtcPt2jll6VTC566vrQR-Zb9cp9Rb6a9_D_6sLYU5hlFsMF5BX61wB_vMEXoqgpaZCBeb5qa6Sdp4WK27mXoG00tw5dj9SRObU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=uYfIHA-T3b5tDQTACZlvhoGL5mlCPMOkl9x6G7-fSPiNbOSme72isOJYrx3i_QxLBHtibisUNpoLFnH6dmj8yOZyhb9NENX937LaWJD5HrBgBURX70MwFfxJ-efB8DVM_qoJKJkzcfYc1yuHzsEnTV9UG-E__hbb2Q9sYiYZZal_vfCEUAmqLMMc560Hb560hbEVz4pWYOUxOfxTfCDsw9DMI5QPdQ6ClwbYWsbddgxTxYAI0KFjloKFz4hZ2FMK7vdChXE0qGwdjlzCZfGxCmpIeT6-Pz2cEhwGfXVnB5a_SUEeNh0ziEPT2_3QuDNbWSiIzd8ZNsOO2QbUHb3eJkoPXNTRuU6rkx8-VV2ob3L2ORGHph8n4u1tu0zbjvKn7wfhOoPZBxOhRkZfvQVfIGYMqeWMnuBXqi8C0F0EFY9A9jbfYfJVN35cCJ2jJq3h_E3NOUohk3pTrEyR56tWSv8iUfWTDwcp__XT3IfwkLUvdcmZ9xQmk8XyJACr4ivz-ZaYjxDrLZ1qKEgXqhDLRejT9y2DZUaDA1wBb_gidI7PwFBcwYV2T0wo5Oq4ogrBxVhpurS8lbjsWSrfsrQAzVG-ombFDlOIlcRaHkK2OZWLe4gtpyy9HMitZiIyQC7uBYEC0pGs2eI_CTsrTcLHK2_UVajOQf7vFp5zHc4ysnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=uYfIHA-T3b5tDQTACZlvhoGL5mlCPMOkl9x6G7-fSPiNbOSme72isOJYrx3i_QxLBHtibisUNpoLFnH6dmj8yOZyhb9NENX937LaWJD5HrBgBURX70MwFfxJ-efB8DVM_qoJKJkzcfYc1yuHzsEnTV9UG-E__hbb2Q9sYiYZZal_vfCEUAmqLMMc560Hb560hbEVz4pWYOUxOfxTfCDsw9DMI5QPdQ6ClwbYWsbddgxTxYAI0KFjloKFz4hZ2FMK7vdChXE0qGwdjlzCZfGxCmpIeT6-Pz2cEhwGfXVnB5a_SUEeNh0ziEPT2_3QuDNbWSiIzd8ZNsOO2QbUHb3eJkoPXNTRuU6rkx8-VV2ob3L2ORGHph8n4u1tu0zbjvKn7wfhOoPZBxOhRkZfvQVfIGYMqeWMnuBXqi8C0F0EFY9A9jbfYfJVN35cCJ2jJq3h_E3NOUohk3pTrEyR56tWSv8iUfWTDwcp__XT3IfwkLUvdcmZ9xQmk8XyJACr4ivz-ZaYjxDrLZ1qKEgXqhDLRejT9y2DZUaDA1wBb_gidI7PwFBcwYV2T0wo5Oq4ogrBxVhpurS8lbjsWSrfsrQAzVG-ombFDlOIlcRaHkK2OZWLe4gtpyy9HMitZiIyQC7uBYEC0pGs2eI_CTsrTcLHK2_UVajOQf7vFp5zHc4ysnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Q35dCFF5BVHOlvDG-xqaZ-wuSo-jZ04nulbi-mcgqJ_9qM57MMPXCUkACdUINWw5e6dF0ZhLUoB65syfA2XQLw4eDX2JdNsOdeSvA__aEyDuqp9C2SyzPNzow9WRO5M4-XV20lLKmPR-5Xrk7spC8_s5UZwh_GCjHxYQrrZjOm0XiraxV8tnqk4LAtO5WvQr9c0_L98QrW9B_aJgawYyS4llBs22bT8jkv8cIWc4cYh6uXAy_kvacXuU0xEDkjS2e8MGNy7_lfJVrt02FGr9WwRKQysCv9lPyCBVUXrkez6POJ6V8yJU9Dn1tpKW5Ld6AR-c0L9ohkYltNCdeLWwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Q35dCFF5BVHOlvDG-xqaZ-wuSo-jZ04nulbi-mcgqJ_9qM57MMPXCUkACdUINWw5e6dF0ZhLUoB65syfA2XQLw4eDX2JdNsOdeSvA__aEyDuqp9C2SyzPNzow9WRO5M4-XV20lLKmPR-5Xrk7spC8_s5UZwh_GCjHxYQrrZjOm0XiraxV8tnqk4LAtO5WvQr9c0_L98QrW9B_aJgawYyS4llBs22bT8jkv8cIWc4cYh6uXAy_kvacXuU0xEDkjS2e8MGNy7_lfJVrt02FGr9WwRKQysCv9lPyCBVUXrkez6POJ6V8yJU9Dn1tpKW5Ld6AR-c0L9ohkYltNCdeLWwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=utd9iMPJhQaKHa3KKBHkZn9yVnpg-DmRFYZGi0GDPcgBTGhMBeSxXTS11EI-2DmACatO6KlkLlyndVTb89fFkuBrZcTvc3kXhHwEMQZ8JB-dlhPkS90A70jf1erH0Y4egm1ryG3kNSNFEWhoIaLEyNpvswU_6hYh8nBYGW5L9shhSgSrl9nNlpl6tLCVTpCdnTgUu0ajKLlkGChGKExemaLcThyQpFMteAXZU1_63q5KZopmGyDGKwjTPqGvQH7GTxhARsUuuhMBzJCaTkpndgxR0QFt1jXJP9vlJh95n64mo3g7_ANzhCN0ocmDlhoVRMjJz7Q5yOqJGUm0UEP5ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=utd9iMPJhQaKHa3KKBHkZn9yVnpg-DmRFYZGi0GDPcgBTGhMBeSxXTS11EI-2DmACatO6KlkLlyndVTb89fFkuBrZcTvc3kXhHwEMQZ8JB-dlhPkS90A70jf1erH0Y4egm1ryG3kNSNFEWhoIaLEyNpvswU_6hYh8nBYGW5L9shhSgSrl9nNlpl6tLCVTpCdnTgUu0ajKLlkGChGKExemaLcThyQpFMteAXZU1_63q5KZopmGyDGKwjTPqGvQH7GTxhARsUuuhMBzJCaTkpndgxR0QFt1jXJP9vlJh95n64mo3g7_ANzhCN0ocmDlhoVRMjJz7Q5yOqJGUm0UEP5ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=lGYd15BgzcbWZlJ0kZoPXQknxab7l6qssa6aHWHV1S5CIwuDmSgJXjeMQiCF2ym1pWJ44MUeaKeRoRUZT0RHQNMNcB6j7kKUoRCLq61p6qWlolb5Rx3BWkptuMsUgHHgpIvQNF4toMOwmQglKqI-lLRpjgBRsgIFgmItS-4NN_e-oZoEZuaQKru7JMQ1jSxkuM_95hWpROUhGlj2HOP6ET6XimIcr4J85C4Bmk9Co7jLTfkFwEOuT8X9LReWuRRjiJ2q9zDlQk6NjyTw6VbDo_W1QKzliGzCKrZK-bUkozBqnirdkbRMe8JjnhSaUIsJUqHmfPbFjnLbHcXcAYYi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=lGYd15BgzcbWZlJ0kZoPXQknxab7l6qssa6aHWHV1S5CIwuDmSgJXjeMQiCF2ym1pWJ44MUeaKeRoRUZT0RHQNMNcB6j7kKUoRCLq61p6qWlolb5Rx3BWkptuMsUgHHgpIvQNF4toMOwmQglKqI-lLRpjgBRsgIFgmItS-4NN_e-oZoEZuaQKru7JMQ1jSxkuM_95hWpROUhGlj2HOP6ET6XimIcr4J85C4Bmk9Co7jLTfkFwEOuT8X9LReWuRRjiJ2q9zDlQk6NjyTw6VbDo_W1QKzliGzCKrZK-bUkozBqnirdkbRMe8JjnhSaUIsJUqHmfPbFjnLbHcXcAYYi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=DbynwPor12Z-dfqRgFhTRsRLeLZzxoTkiSpo_-y-lUJ7E3Wupyjuo8StMt226m4FDTu-zQtKx4PMXyqVucMwMxslhA74M4EeoFXi1rFGBI4i0iJ4NqyojufFNN4FgaoQYOK1_soVAoP_GuWzPAPjtyWDjY5ftXMEkNs6AZLHUQAxaGubU2IzqcDlS3bqq_xS64V8VA7cDn-qe76JkMU_9xE1MelkqhH_EC6iYKcU4lqDfcDzSTcGzykAA0u1WE_P5XraqrQaVbdzo6QBtyANNIbHdU49g1JHVQdVEEwSwQdpzHGaEAfXzwRSmvNxyLsTy6Ys45Ep1l1siSQ3GiJVLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=DbynwPor12Z-dfqRgFhTRsRLeLZzxoTkiSpo_-y-lUJ7E3Wupyjuo8StMt226m4FDTu-zQtKx4PMXyqVucMwMxslhA74M4EeoFXi1rFGBI4i0iJ4NqyojufFNN4FgaoQYOK1_soVAoP_GuWzPAPjtyWDjY5ftXMEkNs6AZLHUQAxaGubU2IzqcDlS3bqq_xS64V8VA7cDn-qe76JkMU_9xE1MelkqhH_EC6iYKcU4lqDfcDzSTcGzykAA0u1WE_P5XraqrQaVbdzo6QBtyANNIbHdU49g1JHVQdVEEwSwQdpzHGaEAfXzwRSmvNxyLsTy6Ys45Ep1l1siSQ3GiJVLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=EOTg019CzjV2PhMFtsnyWPQTf8MAdjCOBCnTBlZHwql_g9hHRj8U32mHX_hM8fnCdvCSL2Uvr9uG8-8RZp4TSu7YSJqr273btg6xA3OQzacUZr_fP5JJIXohA_czXIVPeprt1-Xf9f3XVbBDOrnxEQEP7CVOP1DZ69r15iGNTIy8K7PXaP1B-SWYdvIheCE5RNQcMlyqje97n_uXSQe5ygvGXSxzJanlInw1vxuHvRByPPYlwxRppIovvThIT1NLK4vj3GQHGyhxyurRKPAsNbtseTT5hoHpbFWHpM3trxAiVF2TmM9wcHJV7zc66_0ij2R9ZrXPZErbq4eDfYfsrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=EOTg019CzjV2PhMFtsnyWPQTf8MAdjCOBCnTBlZHwql_g9hHRj8U32mHX_hM8fnCdvCSL2Uvr9uG8-8RZp4TSu7YSJqr273btg6xA3OQzacUZr_fP5JJIXohA_czXIVPeprt1-Xf9f3XVbBDOrnxEQEP7CVOP1DZ69r15iGNTIy8K7PXaP1B-SWYdvIheCE5RNQcMlyqje97n_uXSQe5ygvGXSxzJanlInw1vxuHvRByPPYlwxRppIovvThIT1NLK4vj3GQHGyhxyurRKPAsNbtseTT5hoHpbFWHpM3trxAiVF2TmM9wcHJV7zc66_0ij2R9ZrXPZErbq4eDfYfsrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=mRFZ6ioNGouyc7QfCF2y6ryexBzI6EAoT3H6hfKTPxoANpCY5HQxRiHFpSelCnACg9bJ-GrzUfCJPZiYlczH-9XW0k9T_4jKV5HTC7n2xj67quHFJfvK7XxGu3M3uwYh7exn2VksUUxG_r2K8XZ9bW1cB43MDEl2W4IjwuBKh9ErNYoQMoK8OcW-vJ2L0kAgDgviJPN-0SwFvu9VRRYYn20GLx-RG7MEm0OQeR5RX2NOtY7VFQ4nPSktCKvjjznVC9H7RMpaT3YTPFhDUTpJiZajfXetA9zZ9R17X71HlU0tyN4xtizZrDYzL7GKu2gpVWLv4cnC5R-NbGYhg-FDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=mRFZ6ioNGouyc7QfCF2y6ryexBzI6EAoT3H6hfKTPxoANpCY5HQxRiHFpSelCnACg9bJ-GrzUfCJPZiYlczH-9XW0k9T_4jKV5HTC7n2xj67quHFJfvK7XxGu3M3uwYh7exn2VksUUxG_r2K8XZ9bW1cB43MDEl2W4IjwuBKh9ErNYoQMoK8OcW-vJ2L0kAgDgviJPN-0SwFvu9VRRYYn20GLx-RG7MEm0OQeR5RX2NOtY7VFQ4nPSktCKvjjznVC9H7RMpaT3YTPFhDUTpJiZajfXetA9zZ9R17X71HlU0tyN4xtizZrDYzL7GKu2gpVWLv4cnC5R-NbGYhg-FDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=upSELW08UefdkFVO1CfXN76r18l1glab21rz5R1enXZUWnmk5hV20NARMSEA79fJ-OYr8NzeSc8xnOLov3JkjxjkhMLwQ-Mrko5pJnEZvFVq6ZDL8a9Xg4oORZEGmHN-WVOR9x-GkAkyBglhy6x1V7kT-DJoVGosRtJPYecqZqW5K6tFA7pVM1pu3KMD9JtdUdOiOABCgg4Dpw7MT6nyIb6cu08lk5DBZCLsBT5-ijK4Q6_db3xjxzKh5bXW2MLdr1CKOk9NnK56DBOJEaNREjNcES6QjoW6NSIldZr7NiFXK4IcXWh0bBNwPxn0Y_-JgG2a0XT_9DAl_puYhArb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=upSELW08UefdkFVO1CfXN76r18l1glab21rz5R1enXZUWnmk5hV20NARMSEA79fJ-OYr8NzeSc8xnOLov3JkjxjkhMLwQ-Mrko5pJnEZvFVq6ZDL8a9Xg4oORZEGmHN-WVOR9x-GkAkyBglhy6x1V7kT-DJoVGosRtJPYecqZqW5K6tFA7pVM1pu3KMD9JtdUdOiOABCgg4Dpw7MT6nyIb6cu08lk5DBZCLsBT5-ijK4Q6_db3xjxzKh5bXW2MLdr1CKOk9NnK56DBOJEaNREjNcES6QjoW6NSIldZr7NiFXK4IcXWh0bBNwPxn0Y_-JgG2a0XT_9DAl_puYhArb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=k71cWVR4x4wmyRhTx_Z2NNn7ueDmp26Qte1ALCYYc2j9rM1zFmsfmxLyF8MqJfePELgB_QQK5Oz7Eg5tjslLNv9nQKgdE9Vyh2Pa2xZHbzD57RSQSVZ8mfIQpKPlo9w2MQUZukLVyKmA4T9XobgdZ9ABQLEGmfpDbAU1dhfp7dPpoXsuD5vWFcf0_BaGL5qfR-t1xFs8CM9Sou9Wykb3RJCbqwgKIv0O_OeFSsaO5aVYmn1S_N203mEVhfOKhSE-wZV2vhUONHPBui_jxKBwb2f9WFEI5pwQ1sod515sh7HlSPBpmEtW0nTi8RmHyW3zI8-vpYj7-L2lUYcLXyuzcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=k71cWVR4x4wmyRhTx_Z2NNn7ueDmp26Qte1ALCYYc2j9rM1zFmsfmxLyF8MqJfePELgB_QQK5Oz7Eg5tjslLNv9nQKgdE9Vyh2Pa2xZHbzD57RSQSVZ8mfIQpKPlo9w2MQUZukLVyKmA4T9XobgdZ9ABQLEGmfpDbAU1dhfp7dPpoXsuD5vWFcf0_BaGL5qfR-t1xFs8CM9Sou9Wykb3RJCbqwgKIv0O_OeFSsaO5aVYmn1S_N203mEVhfOKhSE-wZV2vhUONHPBui_jxKBwb2f9WFEI5pwQ1sod515sh7HlSPBpmEtW0nTi8RmHyW3zI8-vpYj7-L2lUYcLXyuzcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I2tp9bw82u8gzkDw5_AbgwSVRzXWPt6HYUF2mc35_8u_fM3qZW9gv3h0onHT4m0V_fxOeo6kK3jV0muPhCaunEqcjRKkPJy1Ax2XeQaDkf_wlP5PAg8ZM2yNVRHb_j4ToopbOYMMaXL4Xp8MdPYm1RM53fQhvKQLQD8OrrcQLoOVDwYwtkaI6Tgd7yR41sXipCQUt-QYQzfLGOWdll4wYzuL5n25o6NhEqALEC35l5wdnhrUdc-IV39L0kWBQQEFaCXVgpRMDCKKcryQLs3AKPRS4K4tXzMQ7fUvnXahQwOQko8dSUrm1DOPfV34zPPwYxk16XqBGYinnSMQhiJb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I2tp9bw82u8gzkDw5_AbgwSVRzXWPt6HYUF2mc35_8u_fM3qZW9gv3h0onHT4m0V_fxOeo6kK3jV0muPhCaunEqcjRKkPJy1Ax2XeQaDkf_wlP5PAg8ZM2yNVRHb_j4ToopbOYMMaXL4Xp8MdPYm1RM53fQhvKQLQD8OrrcQLoOVDwYwtkaI6Tgd7yR41sXipCQUt-QYQzfLGOWdll4wYzuL5n25o6NhEqALEC35l5wdnhrUdc-IV39L0kWBQQEFaCXVgpRMDCKKcryQLs3AKPRS4K4tXzMQ7fUvnXahQwOQko8dSUrm1DOPfV34zPPwYxk16XqBGYinnSMQhiJb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy7FoP-KAwyFFopbfSqPbbPEkZsEqIM0b-QDRYAxHR1tNtp2Pgd0OMdia_ZMGSO76HvQB76vAQurdW65t6UbDRFeaULaeY0QXVHIy22BgwTrlMWs-OPIhTIsc3gdppKCV8QV_WJuwnSgD_X857CBLGoBotDvTzWhV6I8JBJ9WWpQDPPepfXNppFW_Tg4uctwiHHnCBGw8c0rGc3ETE_dM9G2KtDELKa6f_AccIrWV90lXpfL8tYz-GQy7Ar23lqzRHxk12OLOtSwbNmqjAFGSePcXxR8oXfwhiRQhoh8PWK3nRraK0yv_NwMTjbolSz-pzGQM6oXKMaTyJkUQVy1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPTVzwpX4x9YXFk96hjysJUVaIjemYPRF9axsHsHJzmvwcTe56EwkPaKdz4DZWpjLKhGh64bEk33J65SnOhsd3pABZkjg_LetIZ4HdYEE06fny1dEpWVoh6R_hA_gVSoiZWpcKmVz0fUWduDa_B2wtHTo0yqcEsGqUpB1i0C22QvWvjGfCnX03fY8ynEUNzAT1ELlXdl0FBgD6fUFrW0rf5sGF2sKf8XBLNA-fo8oVxWxG84NT6sLSMA3DQFTLdG8Uvrb3f1n38POXT88piGON9n67BY4t0r8nH_bWmEQKFX7mNUuzlnThZ4tIGrnk173ZrkQbFldlAKLMBCr3YBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=a5FZbK-bKvCFim6NTwP7o4rFn2y5bXckM5RY8SjFXpCynGahZgVs75jN6W8b_hseeOmNFx-B1p638e2Nf84AMz_3O5z2_sOjEd-GUVd1RrLdQuS-P8ZBkl-H8uEYqrAvasXjor-YKBa28O1SSVjKHi3CTncVppDviJibt2d9IGkRGoH59jcxWHaKmklrYv-gixJD-PM_d0jfTNqVpcP9CFpHuRKBchPsmmFUuahZRVTGK4sNGz5PRPtDteNm6LCRR8aw9iSB7yHBWoJtCNnagPgnKlMTucWOSVr6Hf1iCO3Jkd8b_wHwvOtu7hXSJbErVM6cvXiZYRQEVM-nNahULQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=a5FZbK-bKvCFim6NTwP7o4rFn2y5bXckM5RY8SjFXpCynGahZgVs75jN6W8b_hseeOmNFx-B1p638e2Nf84AMz_3O5z2_sOjEd-GUVd1RrLdQuS-P8ZBkl-H8uEYqrAvasXjor-YKBa28O1SSVjKHi3CTncVppDviJibt2d9IGkRGoH59jcxWHaKmklrYv-gixJD-PM_d0jfTNqVpcP9CFpHuRKBchPsmmFUuahZRVTGK4sNGz5PRPtDteNm6LCRR8aw9iSB7yHBWoJtCNnagPgnKlMTucWOSVr6Hf1iCO3Jkd8b_wHwvOtu7hXSJbErVM6cvXiZYRQEVM-nNahULQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc-ls2Na4BcNM_xzX9cw9ekDTrUteG2iTqPYKDX5ssnQld5tC8XbJ3bYCXtSQYysfSrT4FwOg4yB-pQhn5cbsJv9NI6U4fDn76B_0Jj33Tl04a2YHWKjhIX0EWSZEUigWt6Xi_oWG0iKTcVYKsMmp-2chMh7mtKX4RGJT8-t-OurS2AQLCPRnblp-ad_JbkjVJJDqnqBH72MiffwyO2yV3PIjuL_XgL3kp75r4rAHRyS76ukK-MbBXlpiYtlPEW35kN2AwbsP1VIeNB4ujS35KOI3QiwOXvgQQrdtkWtbIyN-r80SSEnK4zYXvam-yiEjzSnTQafZ_aEJEZehSTwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhI5W-G-azMmTtZ4ENDHGuwDacqaUu2EfMjKqJtKPlXr1n_AKW0S5dRW2_aP9HEejhE_2apB3Dw7of8JfImT5-nNT-suhN3oKsjYa0hDF1Ak-IKTSatvZJqoyktrKPS7popfZlGviS6hCAYYU_UPTciVpXOWaJcfqyjnLjHEh_-MPHmzkxB9nNP5dDFR93sEqeo2V0GgFsNPIOxCCbc1HjHBCNjH5a3h_A0YDBttQqFz37ab_j5-teb8WfoIA-WHEHukQIAZZ-tiF2FUL8jdddx6UnqShS3_8mVgDtD3Lkt1Up9P12QUNsw9pkRRLZ7DD1_ZzBOKN_TRfF0KzIIwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unStVXFAnbslEdH-gvLXzI5yDRieVX48DTy-b8FpL1bz_nE2bL2z-dSY7X_AplSX4S6l9z6CgAG2EYq5a7_syjf6cpwicULIxL1sICbG_edi5CBH-ekbzX-lgLzzrCGmK1EDJTaslkhXId4DXHwO1nW2OaM7V1jAMlaYakiwRX4emE01m7pb7ck6rG7qeuy1QhZbJn5Tm5-zZxKR1hVAUdf-B4EFOMgafAFUXN6pGrqyjlNer10fDN8EYgptMHNXMGMQzDcoY0z7T8M34f7-5CYiSUFXM_iEvCKe7phQ74KdRgeX5b0PEpd-OwbFvB_gauxbMZrswZil6ZCYMTd_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=jVMHNd4Mh0e-xbzyAc92AhcniBYJ_OvZi6IauGHYSznAhWj8x2j_PHCxBn8OMFr5ZiR2GjD9qO0Y14Kf-5NemMphuxhvvAlRTys6J0t-nY0qk6Fjp_RTMRNQmBD7I0LRyng2jzWg9VAmuRsdlAOhILtIucTCwpPkYTdvzcI_RX5M2YkaeV6s5Ra78owZDLcmd3jv0ZIJBo_afmVl-zHZfsOiyjGGUjaA8yTSJXFR0jNd1_ZdzB6Av-JRc6gXA9IBcuB9SsnF1KJzm-jzhjbbyS5M9Pc1Vs-IhHuXuOJZpUzBemgGeq1N8kB6Lw3L7C7WTTc_O6gr8LwzylMloSipZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=jVMHNd4Mh0e-xbzyAc92AhcniBYJ_OvZi6IauGHYSznAhWj8x2j_PHCxBn8OMFr5ZiR2GjD9qO0Y14Kf-5NemMphuxhvvAlRTys6J0t-nY0qk6Fjp_RTMRNQmBD7I0LRyng2jzWg9VAmuRsdlAOhILtIucTCwpPkYTdvzcI_RX5M2YkaeV6s5Ra78owZDLcmd3jv0ZIJBo_afmVl-zHZfsOiyjGGUjaA8yTSJXFR0jNd1_ZdzB6Av-JRc6gXA9IBcuB9SsnF1KJzm-jzhjbbyS5M9Pc1Vs-IhHuXuOJZpUzBemgGeq1N8kB6Lw3L7C7WTTc_O6gr8LwzylMloSipZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=mlzxf_pf-jn2NSqmR3MLLZurkAPumdGlg-q9CGeeXnr5D9HGCxnHqrEaKmv4QO-MbqXspLr9XeFP_RZ08ylvAhNsx26su20TLMz4QChOacRpPx3WFpu0zTfTO_US2ziflRig3t5Ps4jBoEQtcx-m1tYcPM7bbd6U67kyWZR3gZkMY_Ss1auNRmbxAovQLk45bUjHp9tZLKJasQcdJxtPGJXqo9dVUT2to8MPsNaFJR0ik5ROdxSbS4HDnUfQ5b8GDn4E2SsghyVLUeG4lLLFt8LibCtHWZo_yIRBqD5dqXxuSv_lwxT1DnT5T-esvTurev-TU873ex6Lkt53zRFLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=mlzxf_pf-jn2NSqmR3MLLZurkAPumdGlg-q9CGeeXnr5D9HGCxnHqrEaKmv4QO-MbqXspLr9XeFP_RZ08ylvAhNsx26su20TLMz4QChOacRpPx3WFpu0zTfTO_US2ziflRig3t5Ps4jBoEQtcx-m1tYcPM7bbd6U67kyWZR3gZkMY_Ss1auNRmbxAovQLk45bUjHp9tZLKJasQcdJxtPGJXqo9dVUT2to8MPsNaFJR0ik5ROdxSbS4HDnUfQ5b8GDn4E2SsghyVLUeG4lLLFt8LibCtHWZo_yIRBqD5dqXxuSv_lwxT1DnT5T-esvTurev-TU873ex6Lkt53zRFLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=UTwJqlJ7r3AtIWa7r-adHAIiRjr585DIU_xhZaOQmAELY0MjxlN_wPN_-uiXNjW7vFt8brxMnFVsXB97kDLNd32xRVTmCLJEzuVdUx7pXC_lB2ds5I7DfHKcjF-zvKFYlLy674KC359BQMOYTFzNUHU3R51JSmAYCSdy30Cgvqqu9KIfOPvLckUWxb5LnFWWQPzAVg1oPI2BQ3oEbq2iCaULAWTzwZ8htedF_U6_guF-JbONhN0blI8LLFGu0UHzAQY8XQl1qIrbMgtgQK856xYIICJ6ZzF_e53zqG9jwIEFgExcf_f2vDtMjKSq4tK_WsYKXWsU0UlIbCXZwfxNlRWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=UTwJqlJ7r3AtIWa7r-adHAIiRjr585DIU_xhZaOQmAELY0MjxlN_wPN_-uiXNjW7vFt8brxMnFVsXB97kDLNd32xRVTmCLJEzuVdUx7pXC_lB2ds5I7DfHKcjF-zvKFYlLy674KC359BQMOYTFzNUHU3R51JSmAYCSdy30Cgvqqu9KIfOPvLckUWxb5LnFWWQPzAVg1oPI2BQ3oEbq2iCaULAWTzwZ8htedF_U6_guF-JbONhN0blI8LLFGu0UHzAQY8XQl1qIrbMgtgQK856xYIICJ6ZzF_e53zqG9jwIEFgExcf_f2vDtMjKSq4tK_WsYKXWsU0UlIbCXZwfxNlRWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hGyvBj8qTrhuykOqNwTQeZlTgY1oct4wf99cc1VymiZ4f5GkfTIf0cYH_bHLDBHTuS1NyMZtioWcUve1zG5GysQD7ltZFsDbPwDkllquIz-Mstm9yAivKnZ6ap4gDzy2SvydpU-OO9_dsYiz7HXokZZOK9cNAFZspK381-kLw9DgJrPFHDnihDjKx0M8kSgL0cZs2eF5Uvjo6NXffkiWyqXb5vQ7HiHls9TRTkQFH2s600Fdhk3gdxO0NBeuUE_1b_4vt65dYW24VbLRYLzMSFDCximA_sC62GORhB6jIN_5mb5Ggb8uekRDW7FDxI_ihn4Gyvgd53MDDLQe8w0-PhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=GavkoFeeMIljhECQ7pCrrb8i98BW9zfO6TgpdSYvUjS_zAyFKxWrKTijVoxAax4tt1tUtHBPeqLuaEaGkTWtBoJ3o3zTz13SGv5ZUx-V2v2SNV4V5dzgwPPbi_k6n3MC82PMLackojY1OADA3BXOo_tt2zp_wmScXp8oYK519WxsI8KmFbbt1Uk9gzQ6G_U7gw0XHYdDPEcN6zxSc96iQfz8tPk8mijGjPW4YEEOlfxsDqrVxZJqzU1aXC5cU4I_teih_KAT9bBcRMmPQMxRu29tx9Foe2FQW-rMl4_6AhKStIKl682fm3suDlcJv1-j1gXixw1JMpbYM74C0WI5hGyvBj8qTrhuykOqNwTQeZlTgY1oct4wf99cc1VymiZ4f5GkfTIf0cYH_bHLDBHTuS1NyMZtioWcUve1zG5GysQD7ltZFsDbPwDkllquIz-Mstm9yAivKnZ6ap4gDzy2SvydpU-OO9_dsYiz7HXokZZOK9cNAFZspK381-kLw9DgJrPFHDnihDjKx0M8kSgL0cZs2eF5Uvjo6NXffkiWyqXb5vQ7HiHls9TRTkQFH2s600Fdhk3gdxO0NBeuUE_1b_4vt65dYW24VbLRYLzMSFDCximA_sC62GORhB6jIN_5mb5Ggb8uekRDW7FDxI_ihn4Gyvgd53MDDLQe8w0-PhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9tv27i1CIQ7wA4i2GdzPrM2UXTfRxDjufOxBlSHGFdd_AUECTVRa9kBfkAoNjvle8StToe4yjJvIrEer5bbBjCH1qH_osceX2agW-y5VdRap7VO7_wYLQefruFULPawAK9vqlvqiJArUcB6yf2tW6JLFZk9iQZoAdT6aU5FPzlnPty2Qkdh2Mhm4YslNj3X6EMFQiUwO_e8xvGm_pfLiZN3BMlefnM9L-V3U5m3BxvRs55S_yWzRiZn1eHKDKGpppR7XAfA600PMWnNulco6Rh6x3iKOHzg1isRIwpKjr_uU26qnqxDdOh87z21L0nczDFrInK7eHK5x-7vTfKDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ9JFLdbleOfVuY550E0iLgDCXhFoxGvQ9oL45KZDR5mcfO--x189nz7mYIIZkpWc8ciSHyLbNZFYn06njT19BfCDp87nfkTCM6jIxez5f7E-CsHUG0YXswanj1miu35PFOZnx2nzQZgVRG7eV-DFD_V6zdEEC0iZ1Hkdlb6BI1pf8aJ5U-Bgus6oNwdF6SxRyw4wH5Nt1H-KJ3ACgT6dgIDqLBUwY-dvWYnTwVVYUgHaG5aiBt1suoJuUUwgc9wqzrDI50lnjcO2N9QN9dgRv5u_5jndPhO_3HIFxgm5LLIW3WFiNI86ZNoZaZ5B5CkAqX5LcrnDUIDWAMyQnvICg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=l4Mf4iRps_YIVX3NZMabynswCsjPPlTd7Q9G0qCa3DC5rmLuuFU7iNVTMnDQlGT4eeRRyLd2WWBIDDPo7QgfHEV2LC80OFrZobeeBIs-HMZZojnHpRjpfadeMycgLjv9WVkLbdjdAtHl5OO04pzrAZZuyDI9rF31R4ufpNwIfsWD3Hjm1bd-lAqHC3olazfBBb6blEz9GYnEO2bYOQcQYR_uuTUSH6XjZm4JapgRQTugnBonF4ilKi-6RtwxoWljYsMSbaiI6pxQOH-CJUw0pve-_se4Tl0IgP7L7pxQghgrcJdENr3Kj1O1THhxWT6X8d12J8qNcx_H3-QUQeQNoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=l4Mf4iRps_YIVX3NZMabynswCsjPPlTd7Q9G0qCa3DC5rmLuuFU7iNVTMnDQlGT4eeRRyLd2WWBIDDPo7QgfHEV2LC80OFrZobeeBIs-HMZZojnHpRjpfadeMycgLjv9WVkLbdjdAtHl5OO04pzrAZZuyDI9rF31R4ufpNwIfsWD3Hjm1bd-lAqHC3olazfBBb6blEz9GYnEO2bYOQcQYR_uuTUSH6XjZm4JapgRQTugnBonF4ilKi-6RtwxoWljYsMSbaiI6pxQOH-CJUw0pve-_se4Tl0IgP7L7pxQghgrcJdENr3Kj1O1THhxWT6X8d12J8qNcx_H3-QUQeQNoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=LfxQWrjxP4SF7yXYDlnTvPfg3uAiOu7Ry1NQkfoqSNf4GNMB1xX7T9_zzm8VRhikhUkOy2djmI5H3Dhim8evlcSLQJqe-9yeveSX0txwXWtrS8KotbdBvnv7oyRX6D4jTkLvtwEXIgdNar3GFPA5eWmnXyGzHtsT3boLr2GJdMO-P7LI8JL_Gr0m3XWUvhhvYQLnZozjBUV-hMRWueNErffVMnuC-BoBzn4NddDzHX5T6UOgUF1xvMp-9xYW8fTVaznGKzSwUBdb-ntAvM-89TPSwAaKPoIr92AsoVo0s3EnhAPVWadgGtFALHVj0iZduxJokn8jjJ2ErO_2R8ePOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=LfxQWrjxP4SF7yXYDlnTvPfg3uAiOu7Ry1NQkfoqSNf4GNMB1xX7T9_zzm8VRhikhUkOy2djmI5H3Dhim8evlcSLQJqe-9yeveSX0txwXWtrS8KotbdBvnv7oyRX6D4jTkLvtwEXIgdNar3GFPA5eWmnXyGzHtsT3boLr2GJdMO-P7LI8JL_Gr0m3XWUvhhvYQLnZozjBUV-hMRWueNErffVMnuC-BoBzn4NddDzHX5T6UOgUF1xvMp-9xYW8fTVaznGKzSwUBdb-ntAvM-89TPSwAaKPoIr92AsoVo0s3EnhAPVWadgGtFALHVj0iZduxJokn8jjJ2ErO_2R8ePOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQedfDyKLTZ35Gd7DLVC9Tdg9MaVgiczDrZ5R019W4cB72c8toVyiNB5tAQL1xFWoJ7Y2UR4lOEvdgTpKhhMANHyorbPtTQjBwWjgLKx68acrRIMkNojXR6tI_R12apJDG2vDscToIkdeasHliHrzNH2KuGqUtk0dw1R5Y0svWYhkvIp1AbYjBEMrvRaAoIy8ttfPOCDjV4kR2u_mJ_MPt2HHTAhADLqh5V4LeOp7DifwxhgHiMlbT27xkwfyJQIOhq4GRllT6Iiaa072kf_RPVtY_9v9gwrbEyYhbVCRKZAFg7y3NwFhVZ6ZM07__9mDBfYtFcRbjETfFGZzyJOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=vfnoq0VmZ--6hw30RHoYIHpIM_I6ahIU09RkvAco0_4-tB9HM8p7IRFwEV65CIBGgnIGgO0lxOkvkYEoEr6-oifLqkomctP24QlwuDLupMyWaO1XGeI-FhAo3LRA2r4qHK1H_Jji_ulGETrdWCqKG6GoFJLWlORQ0lczJfl9QtfTrBC0xgfAKufDFFmXzucY5l0EZRi7-OD23F3onuAtF4IxF0U5i8VURKQl-JN_GmAJcFdjaLLQx3MysA4ab9gMWeC6ZnTjEqhopqmiZMIYmozbCF0iinIrhJ_sHzzSjvHLgMzUo4yG2v_88Yk7uhjTq3HbUFHbBXYMbGSvQ9j0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=vfnoq0VmZ--6hw30RHoYIHpIM_I6ahIU09RkvAco0_4-tB9HM8p7IRFwEV65CIBGgnIGgO0lxOkvkYEoEr6-oifLqkomctP24QlwuDLupMyWaO1XGeI-FhAo3LRA2r4qHK1H_Jji_ulGETrdWCqKG6GoFJLWlORQ0lczJfl9QtfTrBC0xgfAKufDFFmXzucY5l0EZRi7-OD23F3onuAtF4IxF0U5i8VURKQl-JN_GmAJcFdjaLLQx3MysA4ab9gMWeC6ZnTjEqhopqmiZMIYmozbCF0iinIrhJ_sHzzSjvHLgMzUo4yG2v_88Yk7uhjTq3HbUFHbBXYMbGSvQ9j0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=NtKTaNDHBjo3_CET_yMkQHqe129oBuKauOL_i3rnpGGtHetTGB4fu9_f_QKcmX41tuYfrftJKvQ6hZAENeoK93f0c4FEJRelvYal7ZqdHK_twNoG-0Tbco1WofffXud4ChIxGGEdG2j6a1QrvqgTB0GfAZocYJq0sa9-W-3v5YtEkvQUuCZ0-s37NtRuLf5GccBFH0SpVO3kWMyxl-KHGH1zIW-_C9H0FA-eiQywobye9J06lsCp1OjLsmNYft3Cms204-UKv4QZmPuQKfh_X-0koajandh2UKzZYGZyBijrKb5YBxH-xA1SHc2ZKspUYatOsQqlQC7r_BdVCPj5Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=NtKTaNDHBjo3_CET_yMkQHqe129oBuKauOL_i3rnpGGtHetTGB4fu9_f_QKcmX41tuYfrftJKvQ6hZAENeoK93f0c4FEJRelvYal7ZqdHK_twNoG-0Tbco1WofffXud4ChIxGGEdG2j6a1QrvqgTB0GfAZocYJq0sa9-W-3v5YtEkvQUuCZ0-s37NtRuLf5GccBFH0SpVO3kWMyxl-KHGH1zIW-_C9H0FA-eiQywobye9J06lsCp1OjLsmNYft3Cms204-UKv4QZmPuQKfh_X-0koajandh2UKzZYGZyBijrKb5YBxH-xA1SHc2ZKspUYatOsQqlQC7r_BdVCPj5Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=ugH-GiVTwb9ICzUwC94CfmX7O6bd5-TRjgH6D97kCmf9zP0FIdwp7Zt8vn9vGFhjtTvtavrEBE5Qnke9FrF6tSVF6kVn4eBduL_o6bkof9bTRXIijdlKjHOZ-_wJdEgQC9DuDNQ0QPODuS3ciTNcaQKbmvidl9vswWPzyKreEgge8xKRaHMZsLL_YgWjRBzmFrtJfDPJ910EA1ceEkVaqZON8-ctggqtsRZK6yPH44lsIypPwZjD3xmGDGc2qGqV6s897iatYMVrWaqHPg4ShjupRhHAbIvsBWbwGScBakAS2XYlTBFUnuZxUdV9IrNi0yfZfvwKkl2wdJBwEH33SA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=ugH-GiVTwb9ICzUwC94CfmX7O6bd5-TRjgH6D97kCmf9zP0FIdwp7Zt8vn9vGFhjtTvtavrEBE5Qnke9FrF6tSVF6kVn4eBduL_o6bkof9bTRXIijdlKjHOZ-_wJdEgQC9DuDNQ0QPODuS3ciTNcaQKbmvidl9vswWPzyKreEgge8xKRaHMZsLL_YgWjRBzmFrtJfDPJ910EA1ceEkVaqZON8-ctggqtsRZK6yPH44lsIypPwZjD3xmGDGc2qGqV6s897iatYMVrWaqHPg4ShjupRhHAbIvsBWbwGScBakAS2XYlTBFUnuZxUdV9IrNi0yfZfvwKkl2wdJBwEH33SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=Laocz4i1NvHuM1g4XiSKxOU3nr9IuJgS8BnYIJiCdI-Uk7UJFf-GghTOH9lB2DbspiPBxqpwOsJtv5rcPphagkzyzSuj3D-ZbGcvYOsfcrH6hWzFaGxGIPVzr-EypupjeiplBwHUoXBrfxBfI3zsX-EhrtYJPIByLgFP8PErSipspxGqISSb15MZVcPTnkMQM1p9aUJrWSWgIGhGqKpUe-2mWSgkODAVNzZyBu_LdgvyzGK03mhZ3L75cPwT_ospmISRchR7MBvSAGaW1DIISUnJNka3qHUuM82xpTXXrrOYoupB_3Q-dvR8wXoMEEnHW-msNTgwhjx2rUDPsWba4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=Laocz4i1NvHuM1g4XiSKxOU3nr9IuJgS8BnYIJiCdI-Uk7UJFf-GghTOH9lB2DbspiPBxqpwOsJtv5rcPphagkzyzSuj3D-ZbGcvYOsfcrH6hWzFaGxGIPVzr-EypupjeiplBwHUoXBrfxBfI3zsX-EhrtYJPIByLgFP8PErSipspxGqISSb15MZVcPTnkMQM1p9aUJrWSWgIGhGqKpUe-2mWSgkODAVNzZyBu_LdgvyzGK03mhZ3L75cPwT_ospmISRchR7MBvSAGaW1DIISUnJNka3qHUuM82xpTXXrrOYoupB_3Q-dvR8wXoMEEnHW-msNTgwhjx2rUDPsWba4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=HQHGy5kAy2aGoSipAka3bw3aIReZRNAsF5adscWswyQphnvwG3oUB5mqb8CHaKf68OcnHBSMYjq-bURxYCilJ7lEaFPzkH_Ukt0pe5orhAoawcJtnO9OCdMnqCp59xkWVg9YC0HvsNzG_YrbhmDg_maUXsU50w7Apl7ELaiX-TZ9FGI0uimacmBh7y1OS9Sl9m9-cIppYgwuBTcjw8hAOQuYTI2bKyIbVFHrYS2H7dAF8dya-PkZBjDGPo2BSRT79vSXoHgLqCMRkc9qCYxx7e34n49xuJTQ2qC2g2xFKNae_pQD-50ubY8--jnC_bcOqdHov7jO_B9Bd44JgPXxmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=HQHGy5kAy2aGoSipAka3bw3aIReZRNAsF5adscWswyQphnvwG3oUB5mqb8CHaKf68OcnHBSMYjq-bURxYCilJ7lEaFPzkH_Ukt0pe5orhAoawcJtnO9OCdMnqCp59xkWVg9YC0HvsNzG_YrbhmDg_maUXsU50w7Apl7ELaiX-TZ9FGI0uimacmBh7y1OS9Sl9m9-cIppYgwuBTcjw8hAOQuYTI2bKyIbVFHrYS2H7dAF8dya-PkZBjDGPo2BSRT79vSXoHgLqCMRkc9qCYxx7e34n49xuJTQ2qC2g2xFKNae_pQD-50ubY8--jnC_bcOqdHov7jO_B9Bd44JgPXxmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ez1fbBT6bF_o6FZxQm9ANLTRJaE5FONGrsf4Xr67q0DwzV4OqT4LRSL28vyvChA9SJXu8lLq3mwSVcOt_F4Od1GnC6IQrY1RT_6Qk_XbxsMEp00m2uLmqBo0EMKBQYg1os2JqGUfToL6B9t35oQmn1PC_0NyveW3culwSwbLTuKrNRYhEwC1SqK4lTI1fCvIn5ptrGu-8mlsFF890dhiPAsQGq38C-i0Y6_6Mx57imQ5lLaOo2i5dufa66C2EPqskzldpK3L290KCmogn6tQBhrQhLDs1re30XfaiuHvEX_kCVRRAsRkCtlViOl5P-Bu9Cvz0wLt8nXb17u2Kskprw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=ez1fbBT6bF_o6FZxQm9ANLTRJaE5FONGrsf4Xr67q0DwzV4OqT4LRSL28vyvChA9SJXu8lLq3mwSVcOt_F4Od1GnC6IQrY1RT_6Qk_XbxsMEp00m2uLmqBo0EMKBQYg1os2JqGUfToL6B9t35oQmn1PC_0NyveW3culwSwbLTuKrNRYhEwC1SqK4lTI1fCvIn5ptrGu-8mlsFF890dhiPAsQGq38C-i0Y6_6Mx57imQ5lLaOo2i5dufa66C2EPqskzldpK3L290KCmogn6tQBhrQhLDs1re30XfaiuHvEX_kCVRRAsRkCtlViOl5P-Bu9Cvz0wLt8nXb17u2Kskprw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=PRBfKDYKfe23okOPGHkOjK6OjQniaAPlJaWqh0iTTsHcsw3C93b4h1MTv1vO3h-4h1wTaiJ99q7TblaSMOkar3GuYEeCVQxvxrvxckZwY08pzMQ-00WDEtXFhwUnXlomPIJ5JbEFLwII1jV5xRCatDpKgSCUUJ5w4tz_iSxAKV8RPaF7tvtmle1fmCH1_WeHj6Uk5-IzxQDAaCgqdkBL9HZS1ma2XLZimN4EXCgRcF2N6W4hORlOnItlfa7x9VyBOUyW_GLs2Lq5YS2x2rXrDNUJg8FYDCWorztcvXB8Oy9P9Phontrk-3BgTQ1pCJxaMQmZOA3FOlgKlGTUR-oRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=PRBfKDYKfe23okOPGHkOjK6OjQniaAPlJaWqh0iTTsHcsw3C93b4h1MTv1vO3h-4h1wTaiJ99q7TblaSMOkar3GuYEeCVQxvxrvxckZwY08pzMQ-00WDEtXFhwUnXlomPIJ5JbEFLwII1jV5xRCatDpKgSCUUJ5w4tz_iSxAKV8RPaF7tvtmle1fmCH1_WeHj6Uk5-IzxQDAaCgqdkBL9HZS1ma2XLZimN4EXCgRcF2N6W4hORlOnItlfa7x9VyBOUyW_GLs2Lq5YS2x2rXrDNUJg8FYDCWorztcvXB8Oy9P9Phontrk-3BgTQ1pCJxaMQmZOA3FOlgKlGTUR-oRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=JwCqPkqxNi6vvV2LD0_FG_p_AGXka91ZzOtjMIFsh0r53T5c2pENfK29yzsmc3LEzjWAcGgqPCL-qhUxqLWPAvBity6kARZrk2i67SKMRf7M-yz_G32xGkmc6c1DMbS8D7lCztBS028bg_OGqz8fOJsXEsq41QgohJbsUGfbV5W6GtitCNdNwhm8VtLb8QF4Q_mrKzBnZAFxX3ousS4QDbUwaIRx40f51-95OpqIQYgGnISI_CK9FlwkjlXIjm684GOZgrGzQtWLzyKkmtm9GKyFMNwI-1fiDbaEWtL_o5s-_8fdRj7d1Njsuey5UUszosDeLHPNsep-rxFulvdaxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=JwCqPkqxNi6vvV2LD0_FG_p_AGXka91ZzOtjMIFsh0r53T5c2pENfK29yzsmc3LEzjWAcGgqPCL-qhUxqLWPAvBity6kARZrk2i67SKMRf7M-yz_G32xGkmc6c1DMbS8D7lCztBS028bg_OGqz8fOJsXEsq41QgohJbsUGfbV5W6GtitCNdNwhm8VtLb8QF4Q_mrKzBnZAFxX3ousS4QDbUwaIRx40f51-95OpqIQYgGnISI_CK9FlwkjlXIjm684GOZgrGzQtWLzyKkmtm9GKyFMNwI-1fiDbaEWtL_o5s-_8fdRj7d1Njsuey5UUszosDeLHPNsep-rxFulvdaxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=TM7RNEFBqKXbekPHzaNY9nJInTs6JoPePgNgycMeClPFLYgderEYr60v57WsUi3BqjQPSCYXP5vZZaf9zceb6CqGbMT5m-iG9vC_wErW1vZyl0SwyNJLUk0QzIyoLKO5qY3mISt9yKaiv-Q1PoEd5Y8DIrQ4OPXtG2VtH0vpb_fxm_f90z1F46nYxevjUI1BRYppGghxK-H2QlVXN3Ks0A9hIY9FUQk7Kc8w5Ud-4yPJcXcdtzQ0QIC5WdiQzB93KM-VEPYxXNPMFPv1UeQkvzKUWift1ULQk2YRwWidWqmPDMpBnnqv5b-o1ycQA3R-iwvBilD7loEosVovqyrmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=TM7RNEFBqKXbekPHzaNY9nJInTs6JoPePgNgycMeClPFLYgderEYr60v57WsUi3BqjQPSCYXP5vZZaf9zceb6CqGbMT5m-iG9vC_wErW1vZyl0SwyNJLUk0QzIyoLKO5qY3mISt9yKaiv-Q1PoEd5Y8DIrQ4OPXtG2VtH0vpb_fxm_f90z1F46nYxevjUI1BRYppGghxK-H2QlVXN3Ks0A9hIY9FUQk7Kc8w5Ud-4yPJcXcdtzQ0QIC5WdiQzB93KM-VEPYxXNPMFPv1UeQkvzKUWift1ULQk2YRwWidWqmPDMpBnnqv5b-o1ycQA3R-iwvBilD7loEosVovqyrmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb_z9oGYORn7ovWdElHnR0Demh6qdbdHOUeb_wGT6t0zTIiSGybbJkMT3I0WPcYAotQ3WKDSlvLxHSuD6jLdtgTWhvANqC8Fsf6Mzmirqo3E_M_aOpoaqY2D6_H9_UjqKY5VI49qukZNB8Ch3av6PyNLR0OHLIvuKy2YHtrwLHSmOFUwmDdsIAyHCx_QqBjqx8GqljG7xIOIqTI7tQEPvA_KOEoC_LBKj-cyxOw3x5Q6lZ61HsTMPvovfH8gMcdO5LcgQkIJGCQzTaMyW7iK_22gw6d3k33C7-7xXBUqbwiWxZff4HqoSOKrTqwqZObEckw39TWWS0-Vk5hjiGHtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=oIJlndzDdnNX4eqBcDeQDWkf_fquoDp6ssgyT7T7RvPOTVYmrKr4ZYkzo8UYk2PnUA1wcuxK7Er5pMv9Mnic22UJumh9BsezkDFetuFFKW7gd7HEP2LrCGAFCqWRs09WT__xkNpBwDlG-unZKChYJpEfMqDf-EGlrJWjynKXNiGi35VpHKEu9LVSNV5TjSwfqqKQL_oECrhKDjLAdbpErWLhHFSpu_OTvIydj-sHN9Z0I3t1iP0MLbOXocHau2iULPVRgzNnj7BISMKAxQT0VI3tIjDwzdWVsrr9yI72pVr9Tin0IAXfk9V_rSoEusg1RZMTJppxXeNmZMSTrfc01g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=oIJlndzDdnNX4eqBcDeQDWkf_fquoDp6ssgyT7T7RvPOTVYmrKr4ZYkzo8UYk2PnUA1wcuxK7Er5pMv9Mnic22UJumh9BsezkDFetuFFKW7gd7HEP2LrCGAFCqWRs09WT__xkNpBwDlG-unZKChYJpEfMqDf-EGlrJWjynKXNiGi35VpHKEu9LVSNV5TjSwfqqKQL_oECrhKDjLAdbpErWLhHFSpu_OTvIydj-sHN9Z0I3t1iP0MLbOXocHau2iULPVRgzNnj7BISMKAxQT0VI3tIjDwzdWVsrr9yI72pVr9Tin0IAXfk9V_rSoEusg1RZMTJppxXeNmZMSTrfc01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=CwRM8JkE44Rcof6xyPU8VXUb56K0YKw2G4rNMcVCaU0J_FQWeLCIxmBQMhYME19e9aA_-atqwSYwZ1hcmklobTVJiTKiHHCHruNMwbu4MuD8VUeZpoETcHXu5YCOsHfp8nb0ggto9AQC-UvuME2pn9k67zUPBL8i9bo70_0Rbi4lyJ_5iZY7zlEnwHiFtdnpb0S5TvK8Y9dOZOtZy3l681L8T3mzZFuCelUZIDXPUwRp043mTIZizgiPH88KWhwMlXCeY2dynUj0tkNDSXt6o6y1CpZTaXN0Sq8VxWm6sWBp0bDRWR2m0e1GbvBByjdMXMtMSs63qeX4t0-iNL22AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=CwRM8JkE44Rcof6xyPU8VXUb56K0YKw2G4rNMcVCaU0J_FQWeLCIxmBQMhYME19e9aA_-atqwSYwZ1hcmklobTVJiTKiHHCHruNMwbu4MuD8VUeZpoETcHXu5YCOsHfp8nb0ggto9AQC-UvuME2pn9k67zUPBL8i9bo70_0Rbi4lyJ_5iZY7zlEnwHiFtdnpb0S5TvK8Y9dOZOtZy3l681L8T3mzZFuCelUZIDXPUwRp043mTIZizgiPH88KWhwMlXCeY2dynUj0tkNDSXt6o6y1CpZTaXN0Sq8VxWm6sWBp0bDRWR2m0e1GbvBByjdMXMtMSs63qeX4t0-iNL22AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFj5ild1MVo932L90JIkzM_jJb1pXCEa90y_S-054fQe0g3Xg1kbzC6KQRObNYU9z1VTbR8AYhrTSzquj-6Z5qjkNw1cFaw2ixYO8PuCogxPGUly96UrBk7J-EcLdxygZgAZqpteGR3WEfm5MtcDR73PH48b8iCXaxJh72s8q-n1eQW4hjk7_mzI5sqQs9IazQOSZUK3qwsO6-_hcSE1Z2RKc_YaUsd5LVURB5YYFcsIwOtD6_HuRfKBzQoMYA5hWVNtZkd-QdIJ10EicS6cPqjgaY0pPehnYYBWvV1ZINoIldkAenxvL8oomJGRqPaROOmsMM79AWkWKxEXjFegoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=rp7hMqp8p8RQYYo6GEjptbCpvx_seoTR-ENhv9TgcnVi1ORD2Rmz0Fs5Tn5wkR9QJQZLrucKxWMsXpSoELcIWfrXWwNinLvsiNsUURNlab_9dmczHUW_Uq_ucuBGSUokhBF8gTECdCzeRcbyoD27qgAZ-lVYgg_9kfHMBtrtbkpZmLN0QPWwllRNp05HHXWie-uMOE_AZhtW4wgjbCLaLtDlD3LFOyMtvkWYe8cSqPTacCfgS69h0R9QjXhy5bnuvOcngR8mCRlOetMVkPLyNIhy0fskX5s_CWLKkit87bNcy7GXSMXdUdBUdJBfN5i3kMsFc4b7JA2XNz-QSRw6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=rp7hMqp8p8RQYYo6GEjptbCpvx_seoTR-ENhv9TgcnVi1ORD2Rmz0Fs5Tn5wkR9QJQZLrucKxWMsXpSoELcIWfrXWwNinLvsiNsUURNlab_9dmczHUW_Uq_ucuBGSUokhBF8gTECdCzeRcbyoD27qgAZ-lVYgg_9kfHMBtrtbkpZmLN0QPWwllRNp05HHXWie-uMOE_AZhtW4wgjbCLaLtDlD3LFOyMtvkWYe8cSqPTacCfgS69h0R9QjXhy5bnuvOcngR8mCRlOetMVkPLyNIhy0fskX5s_CWLKkit87bNcy7GXSMXdUdBUdJBfN5i3kMsFc4b7JA2XNz-QSRw6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=qI2Ck4t4Xjlsg636IxvZxyMbr-MTj-Htm_oRRGZEgHd9OmctpzOq4uOxGzHwO6eZyFBTxcYHHq_YW-Q1UZwmmFiwfMk0YUuqhBDftoc11A2VNTHSfNQEjjG2O639vAhqgvgk9yIlOhgD9Maq9XkLxUdEThJSXz4zXUp37q7BP-9JjjYmTOwURkQwa-OeNfcYhhP6ftBPk1n993sjTg1s1FcYGtfZIkAvo-U9elwux44I8ce1pOT6VK3lQsJ49IWUfgkzwr8x4xFQrKw1KlUDt-QThzGwRY99fAW1z1pmGdVgTwW-eZXndyteAM5Ej5ve3uHSx78wQ0PffaDgfIpFOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=qI2Ck4t4Xjlsg636IxvZxyMbr-MTj-Htm_oRRGZEgHd9OmctpzOq4uOxGzHwO6eZyFBTxcYHHq_YW-Q1UZwmmFiwfMk0YUuqhBDftoc11A2VNTHSfNQEjjG2O639vAhqgvgk9yIlOhgD9Maq9XkLxUdEThJSXz4zXUp37q7BP-9JjjYmTOwURkQwa-OeNfcYhhP6ftBPk1n993sjTg1s1FcYGtfZIkAvo-U9elwux44I8ce1pOT6VK3lQsJ49IWUfgkzwr8x4xFQrKw1KlUDt-QThzGwRY99fAW1z1pmGdVgTwW-eZXndyteAM5Ej5ve3uHSx78wQ0PffaDgfIpFOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=ly8OmonV203W6u9mArfxAeHxfv_oo78-PTKB1cgkSAWT6lC7iI33ZZ8MNrHaNil2jquP2Zvufwk1FhvD4zxyzz7qN7EJeKjAP0ljQQM1_ZglCLqGXudlJl4aMHeEMbz_p7_U2MtuWyefOkzoG01aPRjEnMihrQM4_vjGcNyKZUK_vDMMb9U647q392qBbEeAMd4dIvVBwCxNeTelzqaWGDzkU-4DGDt4ee8-YPXngGlLpPEMQk-UdfaLmF-YupOzvsonRvcWzvxe_S3026vajvq1COoOte7rKCWnIbXRp1vErlc_UgdTQoJtefBIIOlmzZPB7SWyjBjEsRwqxvBjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=ly8OmonV203W6u9mArfxAeHxfv_oo78-PTKB1cgkSAWT6lC7iI33ZZ8MNrHaNil2jquP2Zvufwk1FhvD4zxyzz7qN7EJeKjAP0ljQQM1_ZglCLqGXudlJl4aMHeEMbz_p7_U2MtuWyefOkzoG01aPRjEnMihrQM4_vjGcNyKZUK_vDMMb9U647q392qBbEeAMd4dIvVBwCxNeTelzqaWGDzkU-4DGDt4ee8-YPXngGlLpPEMQk-UdfaLmF-YupOzvsonRvcWzvxe_S3026vajvq1COoOte7rKCWnIbXRp1vErlc_UgdTQoJtefBIIOlmzZPB7SWyjBjEsRwqxvBjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=KtW1HX43qZUsHQdjqh_nWt1Q91k4CBFW5T3cQ1CWZwRW1WHSr0SbJ3v4BReIqjd0Gm8OUQ8lMYOzf3UBl-_1yfcSxfYUQKAcdMCFi_6xJVy-BAIuXifKa2txmvNBWPSqUUSm6DqGXwjAjg2VuehXEi3jhdCaiyzCU2E4TziLiM_N0CmXRH14Suc1eeAs-eeBRqbE6vH-GHHKxxD_e21D92IKcUXRUKSigZ98e3Tt1PqoI8ANyZCcuTQqQbazeGE93ZuYhUCUmSoJMdzNVu_5OrBMRJHq0SWhCjrPfUR_LJgam5DltGcwBPPhVYW1sgxaL4VLS1rHz-oAn7zEFzR1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=KtW1HX43qZUsHQdjqh_nWt1Q91k4CBFW5T3cQ1CWZwRW1WHSr0SbJ3v4BReIqjd0Gm8OUQ8lMYOzf3UBl-_1yfcSxfYUQKAcdMCFi_6xJVy-BAIuXifKa2txmvNBWPSqUUSm6DqGXwjAjg2VuehXEi3jhdCaiyzCU2E4TziLiM_N0CmXRH14Suc1eeAs-eeBRqbE6vH-GHHKxxD_e21D92IKcUXRUKSigZ98e3Tt1PqoI8ANyZCcuTQqQbazeGE93ZuYhUCUmSoJMdzNVu_5OrBMRJHq0SWhCjrPfUR_LJgam5DltGcwBPPhVYW1sgxaL4VLS1rHz-oAn7zEFzR1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
