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
<img src="https://cdn4.telesco.pe/file/lQ5eBmZuy9sQEKPD5kx9_Zxf0N-ahKEH5AjJHktRR2BCeqUO2GcBQdnx5MM6oVoc3lvpgG7SUYqn2iFsNUfdO4Qu0v6I-zOzcHTGRZZLjtcS9Qn2BTQlYBsdqYSX8tkQy_4x3kRX8DV1i4_B5hsY6NJWAincDByEs_d2dSP9_dY137SE3p_ww3irBvbL0N9vVhgr1316r3gZfRfC0-xnEGEpRAzGLnu8x0wNPO7nn4DDMvElCCbp-4VzkmzX9aUfNl-FQZLV3zmn0IIQcUGiLNAAMzMMfOuRN63zk4kHrft-H_D8Q7z2RTsuIkAWy14OmHCnoKddMrF1d_5IWPx0Ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 248K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-83717">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/funhiphop/83717" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83716">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/83716" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83715">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu3EZ5htXy3gWmCS6pOOWr_K7NxhEGxuDCFet552NbdJpd3sBVuAgJ5lPGswtKZIkPgcPF9_ihjWqBhHaoNnWgYeI5mN4WpIzhfT-jOOHwiO6NyZCFFDwCGsVWXSregQpfJ9ohw0MJ3mIQNnsSHmoqC62B0n8ecC1hagRLR6TXj8mdAcNouKeCG8LiW7z36hRw0HApLq7vLZJLokv52O5WdOpE87Vn_6ASF2WVCW5mEjtYdYcaBSThC4LvjMzoS0BMEk3J5jQs8Bfg-KYZ5QJ-4ZMqkC8xe1b74Hs8cBHk7pvYGDdCVTjKaVUA1qCMQGS5xBTdjcLMXx_QJRS2O5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/83715" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سال ۹۰ یه آلبوم سولو داد واقعا خفن بود</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/funhiphop/83714" target="_blank">📅 19:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/83713" target="_blank">📅 19:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WanuxHNyINX6OamkQS7RrxkDde8U706mG4g87PujNy31Pd2mjbwONHmGYOPEeI1xJK7tP42aWVo_Dx5eYOaeUHEFY2yR14bGRCH8oWDg6NXxFvsTUruUPoJOZLsx0YTkbx_iWqthZxsDcxtgW4TxPO_0VDGER_A9fB70ZrJOlnJM-LtepzAmJ7dVQxqlRLRsTHgqbKYpGFdUEbamE3HL4pptY0aRzBX6UfAbw-4n07bWCTPP5GpVtnaOd1FYiCuuLzW-7Vra2MYcbtxDNHxCs8-6DUzv9Qbu-w6F4fjgrWOV0mLGhExfCdTy7rta5PaIabEo5r2yc40hPUsOFEPXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/83712" target="_blank">📅 19:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgCuwnVybAYjZYDxmHHsMWJfTBOXHXzFJpAk9Lwex7S8hm86zqQd0AmtcK6ATAonJb1T6bvoLdqyDUjCVCyj4fYQ8AUADpI_tViLYaKL9O83A_tH2haP1xzf0bFRN4QdSVGmk91cB3hC7YmAVeE9I1rfQiFrU75RRNmuLvMF6J_Dz7W7OdQLZvomLVygIRbBhynqrXbzBYq66z94wVD_FMlzxbbb1b5wStZcvu3qSzWnyRJwYPFTWZmc2Q1y1FGdkVcx7cFNXuUzj7uKk04alEoNCYldbgv9xVfbxTnFkwZ9-VgCt8BHP2b_Wn4w1r2L4MPvyE3sJFDmp1juRk5t2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست جمعی روانی شدید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/83711" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83710">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصاحبه ها یامال یجوریه که بیشتر از خودش برا امباپه میماله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/83710" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2JbWL9xKfYt-tCWi5tyk_sfOW7VopImwQQsCE0Ih8QMN7JskdXzGIqs2L8_qT7sovq4o9rcwsz-JLv-_W37Er6G2CtvF16JlxXAwIAWIttUTT40a2deiezy21LpmHlgYh_nqtt-sE7mF5SeDWzOpdW9jNg3B7JNsrkXezCECVifbivr1p9iVwCHF4eCK8voe-R_zrhjlyTLH042mAmZempDhWknX4-k7lllpChlq43o_E290tkJTEs57YSJ5vyJ9ObCXYaDAIFLiUcZWTLjYYwvqiy2Ek1aCgEL0mZ7VvrCPR5S2TdfuvUL-g1FXPwtdfutThYt1RQ04tUTM5GR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااین اوبنه ای رفته تو رابطه؟</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/funhiphop/83708" target="_blank">📅 18:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb62JxgB9JbEw1dZy51rcoPw2viENlybyg2yd8MIxc4HyxBogXY2twPHuRlB2tNlqyKUzbz9N6SQl4xfBq61sCp-ve3wV3VxbyqeUf8zH_hVeUYRZeF8doQTtgPhSzGJiCUj_EET9gB7i7ogh0ifiCddLIzqX_NsjzVrdvlvKbXsKCxlYaOQVv3GX92cZM41zlRMBgVXu7cPOZW1ZpcBsRWLaBdzoshEaniEatFA6T5dVinMWQ9Z6JLxK4gFxCj7fAqYQ7KzMTRv5wUQhhzzvc0VBGnIIIMb4LHoxC3-XiacW8I_FdEHixmjJV6150oaNzCg2iQNfxR68MIgP1W0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پوتک همین دیروز با اسباب بازیاش بازی میکرد پوتک ویدیو میذاشت ازش، کی انقد بزرگ شد که بره تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/83707" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMahLaoBIarAF9gREJh3NDZe3Lw7qsj6hS6QQaBGtEoEf4RY-R0-5Ch_eaDL1KQZMkxbE7GI7e3Tmnr2V9xWJxz0sNMu_v7WvND7L-rQNtb71kuhfTkhEZ37MqNG0pgaOgIoRb36yxnGn3zqmP8IeGCRt7Id3PgwvoOc3NoMvQHSXJxxlgBEBYeGu6Im0GtIvpbvpngNHRNJAiXVmaRswYSqBnk8lyPaTk6v-ukutbiq-YriPO1997H2kGRYOJapF0cGyh0UosQhIHTCIRhmXUUOMdJkPQsSh4Q25ksB4xSCM7m5yYduwEE3QYPYynTk3YaNRRs4oTzo3gLP1beug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
27g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/83706" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دلو به منم پول بده تعریف کنم از ترکت</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/83705" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83704">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzOH1qT-uSRQ4v40GQ25tPv1HERIj3eGwBh2h7ta9odGxk7TVafy3ihpqtKhSsr2A9drAS7Ff0cxeeK_hA06xpg0ODyEsciDuH21G2DhvE86p6y9E2bL3eO5-qu1tzYsMTvn_hbNhZ1PFeSR03bJWEiAoBzU9ipZa8azdarbnvFosy5D_HE5KLS7vahrWRtC2RWrw492Puck3grh5e37W9Ht4M3zV_3qcWu6CIxS2-rKJ_OJlPSfRR-3YVCQLO7o2XkpTpO3B5WPdOqOfiRiZZ_YE_P2NhEvgxBdCzBJAmEbyR6hS2XpGqdXUqYp58n93LPxF9m_gFIxuzRJto6S_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام DUH! ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/83704" target="_blank">📅 18:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1dY4jH0Mtwh6ucW7BajgaTEfPatmh3aW-RCCQx2fN0KPb9-LYAmWEH2P30hO89oPzYCFlXrssPgCRnnJMXEGUo91leGaqdL5q3Di6OVDBtvY4QMGmFEHzCTDGvamL1Uxuw9UR_-bNF2_tuB38cOc6Dmp9sDzwYeZvhcJWK_TSJumWn4Yy8BBnzkms_-hiRo9rX4nObqpjcK450-0AQ-YwZTKqcdss-iAmjdqMwUZSEvvxSBSMYSyStBIBtq9crN3dY29qIHcfptYwZKDSS0TyTNKdLkdJKQ9wgJ4N6G7YCTkM0UkvmyHzo_4dCdwNL6ekwBSrcSu-RTFIF7BTNTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا انگار داره آینده ای که نیمار پسش زد رو زندگی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/83701" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83700" target="_blank">📅 17:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ome4hTbySaFfZ68pHQ6n7bvDXEnRxnbYS8kXNUa6X7roiDXSs7wImIBT7mtiF-uKqPWCj26VS1MuEIVauqkwbIQeNun3ZhoifukYAMFy4mH8LIO03GSJgXM0cTilMKAL_-5Uas1hc9lhbjn3bITc2UBMegHJUU0Ik2Bla6syHX8tMHnry3UKMBMct1dxnyHESUDV3uOLOVu57SmpTYnJfKhcY8cxWfWy-MpQIusMwycQ4iSalp9d5ziGhqissmEEhACiQTPjr5D8kzA1KkyGXvSVgUNcvhl3Lp1MZaD5Ib-On2FaB5G9If7ICTHygX6-n3yV0s9-g5BeEk3qeEuUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/83699" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpGdfRVje6_CP-YobtGBqEn1plIp3KSyEEnIzRwaOBHEDHlOpEko913IdVQOJELgye_kRaAZiY2OCmA84CmqSSnx2FSCOx1mdMlxC73rM8QmZf1w-YmNHL1ZIoQ1mrT_lGmwnXZSdwfwlp-RcGwEQissO7O-JjTTp01tKDIwjcxZ0deAon6YZ8qsdrC09I8KUnTGcRpHXNbVu31WdtMmmkG7JIzZDI35Lm6KT7weSzFOYNkv0S6r4HUmHq_XjO_bTX-4SYFDZPRQfK_crKrLhmDjR_bxNuCFAWAIuf4cbVJWBicLpNwGun3MZKmlredWB1csnZ8rAuK7EVpRm9kVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر خونده پوتک: واقعا خنده داره که شما احمقا متوجه نیستید با این کاراتون باعث میشید پیج من بیشتر دیده بشه و فالور بگیرم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83698" target="_blank">📅 17:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UipKYZnV5kzk6XM1kxCDL_AGJCxY-cnpSHB8nhfd3Kwip4rXlEPtJdizEtEVc1tBPk8VRUCefpVWfALcpah6HLW1Rg7Adc44JOhLqcCUSuXurZrNNZlx6xAn_dXi7aKhNTSXkxB5hSP1Vn3JkSNQCPm5d6kqZugCIcnhCPGBQsXcI9iFwnrtwlx0h1f-Mkt4Erv7M0GJ5ImMEh3fsT44JyOeMlnx09zDdeLt5EMQsBSWfEBvtXRkikYuPa9jrC5zAlVb4jK5ZgyRVL-Hfs2f4ACgv9gDMn0c7empicXtzSzTkkOLVpFzZyeR3YcsDuUCtjm5dD-Th85yCccA-Ktn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/83697" target="_blank">📅 16:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l89JEI0nRunJXoNKTf8pSfqCgud9UKbhupQic40-gLiBCKcqFytcnt57_VfhMsuLv6yHTwZkrH39HotEH1JKTjYPtPsjdbU0wdG4pTjuUsfH6ANw3YoM98JPXJUQeggO_xY78m80xl3X9U0_CGslglz5LQud4PQ1bG8KXsfKTUK-wka3aCFMu_8Zooche95E4dj52BI4wDS36CuYnrMEcIp11w9vQSKD-RiRrs60-u6_2VPuyzm-gBGwa6_vU0hm1LQvkf8B46s7Z-iiE58oW0yZurDMFxOqCRbrNxsla5dddcRbMIeBtBMQqr-TpOPB7VC_QBODqRjCGBPy6lHeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=VU7cA-dBhcIKCU_LBCHCpTHihWJ3lUjsBQkeXYRW0LOm_QR8J5HOVdkcpNBEm1RoQ_6J2m71GcTrQbvFivX3ChcqSkoK7tlRukr45OMf_Xob7X_zM6cwET-0FPqJJNCaK3CiLUHtupT1ICZORIwTXe4Ri2wsnZm_KJNp0NUwfX4wf2PTHyU4QP_5y6Eaa6c2f6eCtPcorjAhaQyTx1uVi6VkGqopb7L9KDxu9SUOpf_Jv3t6x1YNYbe7TUJ5QjVbOPg3YM-6-931Ew8xQtQIFbGyXzXJyoWY701jz5I__1jDfVf03s667Mxa1IfiJkUKM_SSPPqfZUzgXhmSxzfvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=VU7cA-dBhcIKCU_LBCHCpTHihWJ3lUjsBQkeXYRW0LOm_QR8J5HOVdkcpNBEm1RoQ_6J2m71GcTrQbvFivX3ChcqSkoK7tlRukr45OMf_Xob7X_zM6cwET-0FPqJJNCaK3CiLUHtupT1ICZORIwTXe4Ri2wsnZm_KJNp0NUwfX4wf2PTHyU4QP_5y6Eaa6c2f6eCtPcorjAhaQyTx1uVi6VkGqopb7L9KDxu9SUOpf_Jv3t6x1YNYbe7TUJ5QjVbOPg3YM-6-931Ew8xQtQIFbGyXzXJyoWY701jz5I__1jDfVf03s667Mxa1IfiJkUKM_SSPPqfZUzgXhmSxzfvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی FC27 وقتی پک جمال موسیالا رو بازکنی، تو انیمیشن ورودش غش میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83695" target="_blank">📅 16:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=v6wnXIoCvIwKmBUUXDM35FHhEEjcC8Jyxus9Ut3jv3bMgAsi9ee194VrtKms9g63-SSzMYF8Y_0zrnHLMYNt0I3Qv6WFoNx3w5gyXHwiJ1jS7EkIVe_g0P48cySXFq83oPq_-1D_0rt5WB-0GGF00AM9NWcdCqV71yE_JecD7BD7ahUTNtTSjJCclLA9Rlbq-LlzstAmHdcVVljFSWIvnoF9966k46FKiUnZCAQ9_T8-9YnkloKya4akyh-ly_pwoBt3M1fBVP4jhZjlld64vXzrgVsTiPtSZ7UssmUz9eZ3hiuT4V4l3vjefjmpRAJSPM3of8FeEnGY5ZrNYOTTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=v6wnXIoCvIwKmBUUXDM35FHhEEjcC8Jyxus9Ut3jv3bMgAsi9ee194VrtKms9g63-SSzMYF8Y_0zrnHLMYNt0I3Qv6WFoNx3w5gyXHwiJ1jS7EkIVe_g0P48cySXFq83oPq_-1D_0rt5WB-0GGF00AM9NWcdCqV71yE_JecD7BD7ahUTNtTSjJCclLA9Rlbq-LlzstAmHdcVVljFSWIvnoF9966k46FKiUnZCAQ9_T8-9YnkloKya4akyh-ly_pwoBt3M1fBVP4jhZjlld64vXzrgVsTiPtSZ7UssmUz9eZ3hiuT4V4l3vjefjmpRAJSPM3of8FeEnGY5ZrNYOTTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من به خدا آدم خوبیم نمی‌دونم چرا خدا این محتواها رو می‌ذاره تو اکسپلور من.
راستی تا یادم نرفته بگم آرتا هم گفت امروز دستش بنده، ولی فردا یه دیس‌بک خیلی خفن به پوریا پوتک می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/83694" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1seRR9hKu07kLjlZob4hc8ieFFZ3mPiTTc7zHihb0vfOJ9ObPxln2FHtOwp-uVEBHYj7Fv2smmBjtRtsROUGxUiE0KqnmjMoPD1TrEMZbLvc7ZOA598o34uNWS-f9lSy2--OWQ6ljk1OYBnxIXx_ur16ZHFG_83KTud-kvGthWkEye0ThB8NY2Ld20XWQVxetHGujFGh_TbekAuDgyJ0_P9pLJKpSjG6KQc4erTYvYcUsOhaOL3SYWMhh64mGSX8E2XniSXXYxT64i7ZTUYb7DibIpitJllESnwHnx0_A6ponVKfDTxk5C21XVEjygeF5tivYZdPp1AM0HXzep2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83693" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83692">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=SYNhRUGTt0JSFWxwohizutElY2LAYgouXvWQxjSgW0FIp1SVjZF-CJ5opZ3EFvwUR2A6yneD0P9_PUqkdviu1U0xKuT-tCY4xopRlQe3edg1jY0DfiAKfmkzC8HdUBH9FcJQHoASWFqlefR6axZzizeY9tCH6zd8oION-Zm-7kzYlSuLgoT86vfq9Y-SHh351gZDeu3tN_sfArfBYASqpC_VA7WmUq0VCtvcb8FJVckUCYg_hY_uWyrYPQ8LqbCA9NEUsT7Xnngw2Lpzul3Faa7m4gKV9LZS-PY70_e0LpnGyfjbQCT930nMQSfDR06fyJ2z4LGsPWmSzdbvljNdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=SYNhRUGTt0JSFWxwohizutElY2LAYgouXvWQxjSgW0FIp1SVjZF-CJ5opZ3EFvwUR2A6yneD0P9_PUqkdviu1U0xKuT-tCY4xopRlQe3edg1jY0DfiAKfmkzC8HdUBH9FcJQHoASWFqlefR6axZzizeY9tCH6zd8oION-Zm-7kzYlSuLgoT86vfq9Y-SHh351gZDeu3tN_sfArfBYASqpC_VA7WmUq0VCtvcb8FJVckUCYg_hY_uWyrYPQ8LqbCA9NEUsT7Xnngw2Lpzul3Faa7m4gKV9LZS-PY70_e0LpnGyfjbQCT930nMQSfDR06fyJ2z4LGsPWmSzdbvljNdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین محمود شوماخر چقد‌ بخت زدس که از سجاد همیلتون اسکی میره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83692" target="_blank">📅 15:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83691">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">محمود کوتاه بیا ناموسا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83691" target="_blank">📅 14:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rq-HbOUdEHYeX1lFbjDnhVjWm4AS9iJ1f4PNTECg4qOTGBCcI03uV9ysSznAhD4O5214cn9HC_R8hryG48jQ82LiiDROn1b6MViS99fnNgbVmEdcbNTBk7DTCScPGHSMH0AAQyTtwe9XXDqHs3TnJ2JqGiVHvax_Ly_9ZoLrko53xfmFSsvl0kLmm-UB2vOWKRXzpUNXZefYgzuIg5ZLHy5PwqjzbfXfteRWek1NrH2bpyWkaAIZr_TJyFI955b7Zy0pHBgUSkaGTtHrDdkAB8Xrj8dgoPesSRmWngQY6FMjJ0pim8GLFUgY7obXtAu3Et786SXrQU8KIHzQ_2nzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKOurTvIXmKKvLSIazsyXje4CcDR1T3imSWCDa60V-NT1_MkxlQdBCMwGF0iwabzkvl78FM-ERYW5lbBsrcqs6ugKF7a_25g5-4OowW9gZLwaqNALoEIhyduRTeq60c9C67CiEaYb89gsBXpmKE1rcnsgGiNaaPt6l6FahyxzyNn1it5MoQYXKulJ2C_PpxFquLhbuYSeFgBM3W1gebFk8yPGCN8rX5EcNkaLDZsVSDGoup1Inh4Cpe3J0TnFL2gNCCUovMNm4Y1A5_M9lyQ59jtmvbbsrlJy-G2AtfFiN46IqA0BEMXDV-feqj0jRIyCWhXlx8U_2vBLYCHZxnSuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یعنی من باور کنم آرتا کیرش از گوریل بزرگ تره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83689" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83688" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpY-K_mR_oe5OaEt3El8UyQzejQ9VWIN1O3mU1d4rY-QsFXDTuf-M1ZRqv0s24cHxeHGS4PSCT7Y6nOx4JoNTKfndhbrkU2BHXGtnXPB1PP5gKzCsu1bSm82RunV770BFjZOmOuADkNimRfEEvd3WKnHLFL_hcMsAD684kbsCDcwhbn7qo9RBZokh3kqIjiHyXMHJnt1Q_-jxcn27XTdVAYdaMC4BtjXebOuhWD2Mu01aRU5YlagxN1NZ7iahtsI-sNqHwz86jcvg8cDjz7Y8W9KkVKXHijfSVEjYJe6-5B9gFh6GRMqulAAEbjyBJp0FZESgg29Y7Nd1FvYIJMekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R27
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83687" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKmX3e3kAgzMEaKgmXFntgDLYRKxGXmixfQ8nABld642QTjn2fgAayjtEkEKqlH6kRyd-7PchNG7BAo2V8yDX-oGny2hAtgXEZj1lPmCEhMvnHz7PiqaDdi0Ke7bgFtMwyL5w7-G56U5Gbe0PW0dgfE_X3wp4PC_4HqD8t6lS49qkBefqBpFbuIMtCdFw4PnhKwx5qglSZAxeDupuoYUTntIWAcDUu2k_6M1ckj9Xch4n6banRT1uX8SMCObnCUzEnQAoD3QD7JPOjP8ZIO28Li3D1rXrxm3c4QoaWlKZX_f-v8-lIGmVpGcSzvIRSv-_3mj75x1Y7YGV20aMY6p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83686" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YEVItaDbo7KDcbcsSq2I8aDnWlJLjRAyV8HOPcckAci4GHaNYcx9ZOF_jSKB7YJKyuMKSaoR4OnqqB8WTNRbLcAhf1gddlrx14obkt26eFRGVBkMUIngnzNpRlXSNgDdIBwaL_bmFDboaQc0p7lOJIW7GQgHZvM6xiWoD4YaKztBzFzQNfEMb3IcczQc-4-zmj1V7DHTAzxNUcp6-aQP7NFM6RqADkEX4PRtO-97Z5injFbcckyhuJdLzrzQHY6pW0d9zUQaB6to3GuWoxUqIvsO-WDQyuUcSwZE6JiOTqLJrG4SB5KbCdmXdrOJutvD84_1qOef8ZzhxAlfMDCaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YEVItaDbo7KDcbcsSq2I8aDnWlJLjRAyV8HOPcckAci4GHaNYcx9ZOF_jSKB7YJKyuMKSaoR4OnqqB8WTNRbLcAhf1gddlrx14obkt26eFRGVBkMUIngnzNpRlXSNgDdIBwaL_bmFDboaQc0p7lOJIW7GQgHZvM6xiWoD4YaKztBzFzQNfEMb3IcczQc-4-zmj1V7DHTAzxNUcp6-aQP7NFM6RqADkEX4PRtO-97Z5injFbcckyhuJdLzrzQHY6pW0d9zUQaB6to3GuWoxUqIvsO-WDQyuUcSwZE6JiOTqLJrG4SB5KbCdmXdrOJutvD84_1qOef8ZzhxAlfMDCaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین دوتا از اسطوره‌های موزیک فارسی برا کنسرت‌های جدیدشون.
کدومشون بهتر بود؟
🔥
👌
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83684" target="_blank">📅 13:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlTsOaxXvsFF0ENsb5AR4ib53JPTy7LKiuazRFZWc2laakZmUTgWRV20am2RzJmxRFk3n_vNM9slShNDSbjshvbVYAPX9qYab9GrmFTJxRN2vd8wgp7O-fXGosJvn1Wks4AeTTRJs5R8DnvppVrP30fRYFVs7xnr88udevPgt645t1dp0IU8j76zyelFIkfjSHSQTEHT7xlidzR660z_tsveFFFi1xnF4gKAs425XKYqtEglpfZv985pvh4PteN1Qm9M7RsPOib1TCpXstNpxeRcucKX-th6ampmq6XYcj4uxcGeHunm9KbzdNaUvWcUHKOzJfw7BR9dJZwddPuU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Yeat
📋
Title:
COCOON
🛑
Featured: Drake
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83683" target="_blank">📅 10:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbwp8_yN54rQqaMtVUXPnfMgyy727wK7stxAxY5CcAChsCXHm3G3lp5IgPVmREUZhQ4fFGofpGxdLQuLc5RAPa_87yNCDKDPgkq4XA8E5ZwRwd4lsuD_GEJ0yvk5Z_5v7vGSgs_vb6Tw-yRxFaeuUxd9k5DzxFtpSOuB_l5lUmXTrqYXCx5uA-wTEt-wWkLU9ot_9GcZ5FUnnvjm4zV19bxCnHpZ9U2jqDoq4mxieIUaXnOCQ6g3ASpgf1WaFmqXqkN37HXrpVH73Yt-lkSxkh8a59TCJFnUcH5Bf9TFYiPfGBLMJvcxWoEWJMYBjvSeWD4kaUqiPIU5_noRL1yD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته آینده قراره به هیئت از ایران بره تو سازمان ملل تو یه نشست سالانه کنار هیئت کشورهای دیگه سخنرانی کنه.
آمریکا هم به چند نفر از مقامات بلند پایه که می‌خواستن برن ویزا نداده و الان هم آمریکا گفته که هیچ‌کس از این هیئت حق نداره از هتل خارج شه برا خودش آزادانه تو آمریکا خرید انجام بده!
معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران تحت سرکوب وحشیانه، کمبود آب و برق و افزایش شدید قیمت‌ها رنج می‌برند، مقامات رژیم قصد دارند به خرید و تفریح در نیویورک بپردازند. این اتفاق تحت نظارت ما نخواهد افتاد.
ما اجازه نخواهیم داد که مقامات رژیم ایران از مجمع عمومی سازمان ملل برای انجام خریدهای لوکس با هزینه رنج مردم ایران سوء استفاده کنند، در حالی که این رژیم ثروت ایران را به حمایت از عوامل تروریستی خود اختصاص می‌دهد.
ایالات متحده به ممنوعیت خرید اعضای ارشد مأموریت ایران در سازمان ملل، مقامات بازدیدکننده و خانواده‌هایشان از فروشگاه‌های عمده‌فروشی یا کالاهای لوکس در این کشور ادامه خواهد داد.
به فروشندگان منطقه نیویورک: هوشیار باشید و در این تخلفات سهیم نشوید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83682" target="_blank">📅 08:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jODj7PPgHzUWxI5_M-q9lnwqxUwp0RolFmbDe2UXYabKxy8XcizxBClMfgRPa-7f8E4An6hfQvM3pbIPCIcbrFniyAY7Lr7234nwNM_5VNIiNSHA_7xg5UBan0Q0zlxNG6hkgzk7s44Il15NulPa_1V7u8oDCkKXsbNtfb69UjQJhjmToZl0J2XyLD7Adrcm8J71YdqaIOLaJCvRP_jIZNV3W0ar_MPze6AGj34hW4amz4fuvUcEKtkX3Ou6zXWTkpPoXhM0I2m3ICJtpVO44Gf2gAji7WgNJBtmfXIrrpniNx-pD7yCrVANHPbawdXxj0WIDleoekPOwqKfLG38_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام عزیزان صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83681" target="_blank">📅 07:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83679">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOIF1T14p3mne8py7Qc7RkCSKecGR0t4ERDzKCX9jwji2GO1GZ7Vqd9Xlsn__hynHzIsBoUKzgMVMWz0gO-j9WYsDRdRRNp0V7G7bndtR_Wz6kCmQxm_D5NLG3_xPgwQMsC0rrwuZNrY7yiRJG7Z7-hMAACghrGub38wc7lz-1YcwTo4KC7PHxxOXckRqGqZDYa3jAvhI8TO6fzm0tHbFse-6q3adEV6QRanHAODbwY4CLXeiuys5YuZHu4FPaEE4O0doZdceR6RUaLkDmVx-vrHIDFwRHTigw9KmY7u6GZeimGZIPWFAnfrHqPQxgZ-h7sfEzX32aHy00cJZxf2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش اینجوریه که بعد از ۵ ساعت بحث می‌گه نه آخه می‌دونی از چی حرصم می‌گیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83679" target="_blank">📅 05:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83678">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us2jyeTellHA6OEFRiIEprGKWgWDG0fx_vyu9YpQRejIIAlIAwb7ryW2sqLEs7GEAo7WT5qFj-UplpYYHm6X8EbyhuBSaqmw3WhmDv-fb-tZ79cIe7OISI4kw2NUJbVlyVHgXqu-qzLGi5GoQiND2jQd964Oyz35dOI2AQZSEhx-g7FZOnZtmjD9s-DYRWUBDEF4CoSMWjCexw572ZyvUlfXB7xdOjYr-fn6y0t8hfw2vhctM1Ntkyf_NkW6gfF2Ra1uoJYF45yVGSWb33dLh2tYwRpHdt0a6LXZki8EL2i1CA9mP0X56s2le3zQwCcETB2h_WXeezhRWspKGCrKPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه.
تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان تبریک و تهنیت عرض می‌کند به امید موفقیت‌های بسیار بزرگ و روز افزون در پناه حق استوار و مانا باشید.
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83678" target="_blank">📅 04:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83677">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعد از اون فاجعه اسکم استارلینکا، فقط چنین معجزه‌ی دور از ذهن و عجیب غریبی از طرف دوتا از بزرگ‌ترین رپرای مارکت (کوروش و آرتا) می‌تونست یکم محبوبیت پوتک خدا زده رو دوباره بالا بیاره که خب نمی‌دونم چرا ولی انجامش دادن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83677" target="_blank">📅 04:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83676">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfRwc9Pkfj23aVyLwPogzX4SN1OjOe6cGVAW8i8QsHCaa7UhfCVLlpTwzQ89CRYItOk-bfMWhMxktAkRcTSVAGcZ_Aq5qE_cIzb3dAa8513SYIYgBi9QQzlmNO1Ayh-q05S284jriUyPNWon9dyWIKmfHmY2lIcJUEEj7TDWdx8ehElR66mRVBGMAv9rvp0Zq3KbL8DMEhmuobGsqmmz-oeIkE1iYJMQFpM6V1dunX1WhtvkPMeCHeC1KUBjM54HhV0oDnvb-viAaE9Lj6WcdgLgLgYA5QLFuWJW5iJLtM2FGgcYul0UUlC3br6sKEL3hCBZ_QqXT6KPBlvs2LwnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک در جواب این همه ویس و ادعاهای مطرح شده، فقط این عکسو از آمار یوتیوبش گذاشت چنلش
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83676" target="_blank">📅 04:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83675">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVQcs-pELhVW9r4GrxrTtV2fzS4Tzm-ymCJ-w-vr6CxYk40FyG57LvAXL4_o0Paa6ax4b7RYPnh32XR4yV7noxA1JLMjOEwkaIBN7afkFylvhsICaLEtTMS-8SDFrB5Iu5WvQXdZ1mDytDTVqZp2TLD52IJsHl4dP5M-vdAzrCc5w4HlqZIxUiNjCqv686_etSb0jsGxunFRFbCKCBp53_qPPh7pIIHfSpKp4n6fktfPJEHnuioufPLOMGy3rkX3SBRSbyBQPdZOLovaym3N36QcweID8KmHjC7UfJSHNrlTV7BHzEREcLjbsaEgLWn6LM3iFPMEuwTYCuCIzuyDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو فکر کنم هر کلمه رو یک پانچ در نظر میگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83675" target="_blank">📅 04:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83674">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">داستان ادعایی کوروش وانتونز از نحوه تولد دختر و پسر پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83674" target="_blank">📅 04:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=Qr8HoP5Np65AO_njBjXQPeiPAkUlJC-vm2W_YRQdaemiRNXK93RNUo8GOmXlXfHTE5gmNAaUuFNoZfbx1vN91ktOEV3zkb1BXCrv3NPelwuxEriJ9kDX3WeSa1yq-aNfo1kIrJzRkhJEKZmAWTggigJ_EAS9sippI8BOfFZ-J_LIjgYu0kVnawvSpvKpX2eOuMOYVieFlpzdnvFF-XAKyKTepfUJba9svIW5JOVopTkT1AERgyIK85J6LpWpdflMS5K_5IRCVAI00JHxbOf6eCsCzPBtl5XEHi8ppjmS7MOBfSzY192nzN0ALK1BM_Pc-P4akzRe4OvaCSABuSzVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=Qr8HoP5Np65AO_njBjXQPeiPAkUlJC-vm2W_YRQdaemiRNXK93RNUo8GOmXlXfHTE5gmNAaUuFNoZfbx1vN91ktOEV3zkb1BXCrv3NPelwuxEriJ9kDX3WeSa1yq-aNfo1kIrJzRkhJEKZmAWTggigJ_EAS9sippI8BOfFZ-J_LIjgYu0kVnawvSpvKpX2eOuMOYVieFlpzdnvFF-XAKyKTepfUJba9svIW5JOVopTkT1AERgyIK85J6LpWpdflMS5K_5IRCVAI00JHxbOf6eCsCzPBtl5XEHi8ppjmS7MOBfSzY192nzN0ALK1BM_Pc-P4akzRe4OvaCSABuSzVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند عدد از افشاگری‌های کوروش درمورد پوریا در این موسیقی: منیجر پوریا وصل است. پوریا با اکس منیجرش لب گرفته است. حق فیت حصین رحمتی ۵۰ هزار دلار است اما پوریا این پول را نداشته است. پوریا موادهای مخدرش را زیر تخت ریچ (پسرش) جاساز کرده است. پوریا به عمد همسر…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83673" target="_blank">📅 04:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83672">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=HpLfkNN4G3BDqjVC3K7frZ6EzoDtH497yKO0jsy9oTp2taKxrI1dBFR_jor8Z3MGe0An--m2Znpcqgh38B05WKkZBwN457pP_PHjWBxmW3LbDJvVBn7ECH5uhwHDBfv2IsZCc0_L5TY7y2UpTPasamfDxfVIa5TA2Dw4m94qUXK_c2L28XlYQuiT0eFDrkH51t6EQCiwEeUYerbo78s8jT3cFqhSan16pgZikZsTa5V-PC00Q4HJUiEjqSyVDXXEiKdMIaNDYtTQ0HLtjgSE_V9v3_oWe4g3nCtknsmtgU5_t1OhJnMGlPv1Lx6J1GQDSWW25yuHb6lPufq_etq4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=HpLfkNN4G3BDqjVC3K7frZ6EzoDtH497yKO0jsy9oTp2taKxrI1dBFR_jor8Z3MGe0An--m2Znpcqgh38B05WKkZBwN457pP_PHjWBxmW3LbDJvVBn7ECH5uhwHDBfv2IsZCc0_L5TY7y2UpTPasamfDxfVIa5TA2Dw4m94qUXK_c2L28XlYQuiT0eFDrkH51t6EQCiwEeUYerbo78s8jT3cFqhSan16pgZikZsTa5V-PC00Q4HJUiEjqSyVDXXEiKdMIaNDYtTQ0HLtjgSE_V9v3_oWe4g3nCtknsmtgU5_t1OhJnMGlPv1Lx6J1GQDSWW25yuHb6lPufq_etq4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب شب خنده داری شده پسر مدعیان حامی حقوق زنان و زن زندگی آزادی دارن زنو بچه همو تو یه درگیری رپی میگان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83672" target="_blank">📅 03:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83671">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کوروش چرا به این اشاره نمیکنی که پوتک نسل دویی‌عه و اصلا نسل سه‌ای نیست و چون تو خودش ندید با فدایی و سورنا رقابت کنه خودشو شاهِ نسل سه جا زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83671" target="_blank">📅 03:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83670">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کوروش وانتونز ادعا کرد زن پوریا پوتک سابقا رقصنده میله یا استریپر بوده و در ادامه برای دفاع از اعمال خود این حرف‌ها را زد:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83670" target="_blank">📅 03:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83669">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrpB-fLQRyqKxZr3RZKngKEevRJ4Pq0C962bYm-h39S3SLdsJkqgNlrKSkjmIDzPBGbYMhIIogwaFLkkUyES6ZhuuTmfn784APh-t_vt6bX_VAJBtXPmGIdLnWD1uRAEb1hZUtbsDotr2602G6DxDG0zekCtjyYW5aRElR-eVshzPDRJQQTDt0Gwh_9niN2VjW81ebUj0tZnb4z0UcnNIR3mvQ-SctNBfp72hJumBYKUxYmNYEg2EhLvFFg4K0uG25trELG1uU83FiTHhSqOp3T4G0bHXep5YSkry83lMtf4Ua4K9LvS4arYymBmuxzju-iIWGE8WHEN1MMHP4cheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا باباش ارتاس جون ناموست برو بخواب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83669" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83668" target="_blank">📅 03:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_5tYFzZxyosTbrIM4LObhY_dtH2OW9UJGU2fCn3LGaZJsiULwoTDDmEOVvpckbr6TDosGmKAmFCZ72N_rQyuL7Zstfi0ZQWtAV29w19-Pko-sAEE79Her-HpH_x2ZyhwjmpU6eQYlkWYUNxmadh5GcQCPTVgQcQ-NuJmPjgjGH-LNZTp6JZrCUOxkDMIW0XrbCxh9wTkdwk4Daf7chXgnJ3Kuj7NUalalHQ6G8Xc8BWndgfsJG6Ex0XVZAQHCR8AU029Ol4DDsiSWAJJ3hD74-3xSa-AMeGdQpf2A7B4OaDbUz0Q36uXNCQKynHJhXBOq6qpr6823lszbniPxqthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83667" target="_blank">📅 03:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گنده لات یک مدرسه رو نگاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83666" target="_blank">📅 03:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1G9MGo-MjS6tmORp9spj8oPMjn-rMJ8bOwXHnVhbbyxg0fGRs4frGctpEY5p1853dct2eL4CS-_-nnKezKGaL-YlUEc5iIviRQHa9JneX-pJKgAuqnQXdGvo7i3CWCfH8Sd7mHATPn91AsVwjN5M5jFRalehviy5sDSt_4zBsAltRtk3htzlyGwalh0AaG4DcDAa6R3wDjoCDQ7IEoYuRZN2_FwARdRniuFfpvUVY70fTfFqDsQ6KfOpkOjfia5yWepPaOAkQ_IykJY0IAA_agzF1g-vEhJ3npQB424N-UHQtyPJAWRlJI2cFme4mgbg-KF9DvGRld8_c6mQbtgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L75R7N7-7WtpzLT-9E8dLFk-ip9ch4ZozwjOW997ky5ozTapL8KLZhoiuQxynAP9sldB6EY7XdpEgKS5lP1b9BP7FuqcXNnWzDlHKthibWFioGRGq4RPmJeAijIFSrEy72GKyawuaYKHbcqFDz67tBhETn_Q1ybCReTqluOZJZBcUKtWZc3rl3BNH2OeJBSEfNwPRm7c9POC_8nxftxyf3AsHkT4-dTwCebWbWiB3Hdqr5fqVbAIWuwreyVEbm_gBI97bNOhXJPYZgqWmI_6wDNHwqg5l9l8Lu67Bk8BlDRIxMsSi76Kb5-BVs5nQAXEcGABfMorEygnbaJRTtCqGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوروش واقعا رد داده
رفته با گوگل ترنسلیت یه طومار فحش به اوکراینی ترجمه کرده به دایرکت پیج دختر پوتک فرستاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83664" target="_blank">📅 03:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حالا خوبه دیس پوتک ضعیف بود که این دو تا اینجوری ولکن نیستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83663" target="_blank">📅 03:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awPVIchozHOCDDEvQI4J-UpFajSiEQA8yNUwptX7nB68C7Iq-i1Vae088Xpg-6OCxPnC4r_cR1IFcnKrPtBgDmn186JezhD2iRN3slaJCDpzPNdzqtg6bY2PkOveIw7xspHE76Si1skawqB0IDXfaWHlV27Xsx67KCZ-d3PSP6nF4cOiYW3MGkltu1MHZZ5uGX45OAHtqOPSrdWNwfLEKAmOLacIGC_2JeLuLWRJM3mWQqbpySxM4VC3o866uvBOPFBA7njpFNkJMGhfjxDSDLGBvx8XKfDo76Tsc_B0pl1bUri9a707z_o6ifjwNocMUu3H46T1yf8yoPixgTzzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان من چیزی به ذهنم نرسید راجبش بگم شما خودتون نظر بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83662" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نه دیگه نشد داری زیاده روی می‌کنی.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83661" target="_blank">📅 03:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جدی یکی از خنده دار ترین بیف ها(بعد از بیف شایان رگ و آدرویت) بیف پوتک و وانتونزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83660" target="_blank">📅 03:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">میگم چرا همش بگ میپوشه، تو شلوار های عادی جا نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83657" target="_blank">📅 02:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArta</strong></div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83656" target="_blank">📅 02:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83655" target="_blank">📅 02:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کوروش: من مثل توی مادرجنده نیستم ناموسی بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83653" target="_blank">📅 01:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تو همون دوران وعده وعید های پوتک، کوروش هم موزیک سیاسی میخوند میفروخت به رادیو جوان
خلاصه کون هردو گوهیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83652" target="_blank">📅 01:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">استارلینکا رفت تو کون کوروش
مگه وظیفه یارو بوده بده</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83651" target="_blank">📅 01:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کوروش: استارلینکا سابات چیشد
پوتک: مادرت جندس دافت جندس به دوس دخترت خیانت کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83650" target="_blank">📅 01:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کوروش جان قصد دخالت ندارما ولی این که اوایل ریلیز ترک لایک رو بیشتر از ویو نشون میده باگ یوتوبه که وقتی اتفاق میفته که حجم زیادی آدم هجوم میارن برا گوش دادن اون موزیک یا دیدن اون ویدیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83649" target="_blank">📅 01:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbRp-I_Qt6pkjC0zQQ3cxG5Na-OX1hiBj1uInIeYTZwYMVMoWpV05aqSfrptg4_D8gkTWGCBKzaU1wDL4NvxiHPTuaH4Y8s8mkPva_b48_aaF2xGkPwtLZQ2SNBoZmoHmfdu7glxAFUmw0rUJafyPxG9Trz_oYZgOYpuxY4Te53n-kP0Ru2T7YTZMHfsMHv2v9IiS4NHZT0Bk1rBHItPOpdD1ScfLsExJVTUj59rlNwpOE-3roE_nD3WPkapMtTo5nhI1CR5JyYB5515RDUBvo8p2GrOrZCoNE7qWJ8--X1Z_kROc09UAbY0HmKbuiEfqMsE2yZwtmCCbhmlRbngOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83648" target="_blank">📅 01:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آقا کوروش یک گنده لاتا مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83647" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83646" target="_blank">📅 01:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب دیگه بسه خیلی حال داد حالا وقتشه طبق عادت بگیم از بیف ملتفت با تعداد کثیری از خواننده ها رسیدیم به بیفِ کیا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83645" target="_blank">📅 00:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNYNblqZEqZPsAl_uOR2h8Zps_qpjcOBzj5izUzhptk94GkGmxdj_hD1aQokpLrsHZirIayOfhlgrK2QOPMZzRytAYVl4O00_SjY6Q8-D-YfderUic8ZzeukZXpZX0UFgo6r8u4og5IknVFMM0M-7YJ5a8Ju98FFW_w9rukI_R_rAGy4_AnHqIvWB3c9rpq6Q4TGTuO8vsEFbPk7KDzy6MI0vQhis34ZAdg6-sVRrruh_IoUhOYkXOot417vjTOLwWbwIrmi-4VrLzRdIeik9Q_IoEvnbp499xw8pUHK0jzoLWGEbDXi294X4ufN0HbJ2fNTG83RxBqByodRYlngMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زودتر از ما گوش داد ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83644" target="_blank">📅 00:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-poll">
<h4>📊 تا اینجا کی</h4>
<ul>
<li>✓ وانتونز با دوستای فرز و شیطونش</li>
<li>✓ پوتک با ریچِ کصکش گو</li>
</ul>
</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83643" target="_blank">📅 00:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عاشق کصکش گفتن ریچ شدم حاجی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83642" target="_blank">📅 00:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83641" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83640" target="_blank">📅 00:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83639" target="_blank">📅 00:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آقا اینطور که بوش میاد کوروش به هلیا خیانت کرده</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83638" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83637" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83636" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بچه کونی اینهمه مدت بلد بودی همچین چیزی بخونی و ده سال کصشر به خورد گوش ما دادی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83635" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83633" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVC8v9__T4vH-XHsFvr0tRhKRqWYz96MmtCFh83jrSTcCPe4QEVfwYP8UPDolT3-ZKghSOcPHTWQlxg1eJsup9AYa2t0J2Kj5yDzlj4AIF4_Hr5-5Bd1s_NNwErt6lHNnM1fFl12hIa8FoSILpOZTCizi-xtOTfpDfMjW8OcCdAkjVoHEndPjKmBtGPv5WE-wY9eigJX5naqd238kL11zYZ7aV541oe-wOihdX-gMd5_lWDAh-0ykLiTeLBvZLGrZVTE7Yms3loi5ek-0xDTt2CVYKhqs6OFbTGOR1_6S_0nKZ6aqq3Cuj1Pk6ZI4dj0oI4dbggL7fA-NCSM93b0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد
YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83632" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ریدم چرا اسمش هلیاعه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83630" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پوتک دیس داد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83629" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoC0DuzCtLj3qZFp1lm-87-YI9L-9Xvj6At02iTmpAC_baenlM84746A_tzRyXZ8Eo3kmku1IhAJ7jLkVfBfBL8GIy8X4C6-L5rWf3P6fliJ-Kb_jP05cpgfNQhOnjDNgQpCRYfyJksUFvlCBPgmpjrhGe62QAHa2B9Tibl2CIl0VHXa-Ydb36NUjxu8tlsp4otHZr-X34tChmPlsvlfCYvpJubeLPVCLXNkTwcggQrkQ3zmBLvDk3OM8Q-l8A7DTBZuf9g7ue5dYryl0cEKM_AqGhNX53dwAc1O9Qve-VV-RZWbJfJilVb9_rVLUwVKQuH0DmpSETlSlNe240A3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک: داف زدم روی داف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83628" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شب زیباتون بخیر عزیزان
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83624" target="_blank">📅 22:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کیرگوزی سمی لو کم بود فقط.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83623" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حالا که جوش خوابیده میخوام با یه حقیقتی روبروتون کنم، بابای من کلا یدونه خواهر داره و اصلا داداشی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83622" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پوتک ترکتو بده بالا میخوام برم بیرون</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83621" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محمد باقر ذوالقدر، مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83620" target="_blank">📅 20:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینایی که تو اینستا میگن "من از این نسل نیستم" منتظرن جایزه کیر طلایی بدیم بهشون؟ خب بکیرم نیستی کصکش به ما چه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83619" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هیئت حقیقت یاب سازمان ملل:
آمریکا تو حملات به میناب و لامرد، مرتکب "جنایت جنگی" شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83618" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgtWJ_ePDNVd5b2In8sDHDt-NeWiwbnQJ_MSpewc8p3UVEdZKj8__YLIogjjxfiwDgcaNSgRB16DNNA2UH8UQuU6pl90bAOVTMQ2Z2tbV0BTQaAUBoscdR9g83IG8Ty93v0G-DDOg2v0HHyw_MxYXB60c_iAo-LSiU_x8jepYdxY3jKwMdB9aCBZSMC2KFDNExiE08_EgKOXe_z1A56go_KrbwbIKaGHFNE4yQrmoaNW4gVcIS1hxpCr5QlRhruW3Vku-go2PqdXy62OsVsHeRAc3FjNgFPbUILLdfapCZz0CmDXmMbTYC6P2sDhf6ISuC4YL8MVHpiczEoHdyP_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی والیبال قطر یه دریافت کننده ۱۳ ساله داره که ۲۱۰ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83617" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این نزول خورا چرا ورشکست نمیشن حاجی هرجور حساب میکنم تو ضررن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83616" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83615" target="_blank">📅 18:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=g7Jw_UyaYBV0bY_ZPCCB5oBfuzkrsx6QMKvxrYstO3Xri9sMt1eIkXqqaEgfD7lzG7PTN1vsTKGSKr_NqV5yYJGMLObOVhAv5mqOTdBr9lHUvpdDZStZ1PPqH0Z9hUaEnaT5-22Cxpluj1rT3ytEqTqJLbZxDnh9lEuyjdcCy_kWcHxw7WSvqgg_wM8ifN_lKfVuNO2yCr6y3EUGcBS6T86DqqaI_QTaHNWFvb0SS1mYDp3D8P7k9uiqfxNztfwu6JjyFveNIZ0Pv6OwagCzpSiqE8hmzcu8qVC8ZIUydz4XqOOXphazYLSQebDO94jJpyLD5qVaVRhjFf7zU8-PPXKVmG0eHI4Tt5i1P3HEfSWhcTTHNlY2AJePWJG2kqkRGfdiX_1QwD660LaaxEMvWzw5-sKB5GOWkKMdosKyS2RRwDQw3SwJPiZTfgeHwQ_fOkI6ETdmgiWXyZIx3qgjo8zfKie-DcoXPJr2YWwIi9Jms1n0PlBsN4WuWywsn733yoKuYNW5nv-mgdAAJn-j22bAeAzV3vA5SIhlYzHIwGfSMNyrjYcZR0uEGemgHv2u69OWhveZy-KE-9_ysvuJvHKp3CAkkfiM1sb7WxCYa2_UhfD7QnxCLcUB4tWJj7VdIYnUEfY8gncwFJ-9glB0uTlbutxrdzPNZa8YAr2SVZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2ff6c50.mp4?token=g7Jw_UyaYBV0bY_ZPCCB5oBfuzkrsx6QMKvxrYstO3Xri9sMt1eIkXqqaEgfD7lzG7PTN1vsTKGSKr_NqV5yYJGMLObOVhAv5mqOTdBr9lHUvpdDZStZ1PPqH0Z9hUaEnaT5-22Cxpluj1rT3ytEqTqJLbZxDnh9lEuyjdcCy_kWcHxw7WSvqgg_wM8ifN_lKfVuNO2yCr6y3EUGcBS6T86DqqaI_QTaHNWFvb0SS1mYDp3D8P7k9uiqfxNztfwu6JjyFveNIZ0Pv6OwagCzpSiqE8hmzcu8qVC8ZIUydz4XqOOXphazYLSQebDO94jJpyLD5qVaVRhjFf7zU8-PPXKVmG0eHI4Tt5i1P3HEfSWhcTTHNlY2AJePWJG2kqkRGfdiX_1QwD660LaaxEMvWzw5-sKB5GOWkKMdosKyS2RRwDQw3SwJPiZTfgeHwQ_fOkI6ETdmgiWXyZIx3qgjo8zfKie-DcoXPJr2YWwIi9Jms1n0PlBsN4WuWywsn733yoKuYNW5nv-mgdAAJn-j22bAeAzV3vA5SIhlYzHIwGfSMNyrjYcZR0uEGemgHv2u69OWhveZy-KE-9_ysvuJvHKp3CAkkfiM1sb7WxCYa2_UhfD7QnxCLcUB4tWJj7VdIYnUEfY8gncwFJ-9glB0uTlbutxrdzPNZa8YAr2SVZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک جدید ویناک بنام تارانتولا ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83614" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZCeat9RXN3kcF_pZlMu1xFCs9cAmNaXVlbzPzWvFiBiE5QjkHIGZ54sy4Cyk1IAuEo3gWR3FAc4QobNrTlGrm941723NdBdCiesHIMqeGED4LDEa7iSnTRKfesCt3vgqbKBugps0nj-Pmo0YB1_85VwgpwkoikG9jOgf1XqQmsiX8wL8n5oyG7wDmoW_pFwytqlpbF6xRcVqMEIhAEXfNBD168jUpNMhnR0CkpaJHK4a9CfVj4fMgbVMzpH42OPQbBWQBOIOFTmT6WYKFdUdP6aS4lZN3lCXSHwwq5hX4-9wyoxNjEcRsHudQIJM_BFGyD6xpSdWj0KQqdcqchQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83613" target="_blank">📅 18:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSuHw3CNTU2Qn75PJaW6_tbizMR0xgv3V1aD338FZSqAizsj0CiqissQZGUdnSxzGKU3AE7tj7R9T0Gu4UmwV4ge5dH3UnPCvvmrtC3tl1i1AGrn-3jJQsOwCEsHLHa9HjeyDm_0zuELCpYCHKv1mgoujamOP72CBMRMici7721vgfCiy9qffVvLGwBTNH616qA50hTEMTM7Ae6ASz-6Y8rtjE1LzYK6VWoZQrqZp1zwxfLBaElfGoK7SWjQsj1NKoHWolcwjATNcpwfgtDELIGRqP1QD4jz4b1Nk6UpooDldOBfpB_hwkrDMsiJmKi2YUPjpBed5GsxvHwVY1R_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایع بازا به محسن پیام بدید برا جیبتون پلن داریو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83612" target="_blank">📅 18:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=PvaUEiI07VqT1EKK2dV32uc6FzIQFBhJj_mCtdR7zu-_S6mHh30KuT3_xuqqSVl7DO0R4qr3ulWViqZCxYMpR7-vr16iseOCNkQ9Ga32kbUlWdhZonoNlIus6veBGJgR48-JjCOcJdX9x02wnbwlZ3pdTww1k7o_hqJjEX_EkCV_z7thJoSpsbk40HK1JJ29b9vEv-0dvw2uk4c4791fxGJVIUDI4NMWwHmuALYhtnLVNW22XO1Eu1DTsC4JQxTE3dXVRnbyvP9AEltiQefOC-Coj0T1QwIkRtwNrk579JqBgFz07PKKzRdMZwU3WvYus72kwu9jq3a4f4Lu3oXjSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=PvaUEiI07VqT1EKK2dV32uc6FzIQFBhJj_mCtdR7zu-_S6mHh30KuT3_xuqqSVl7DO0R4qr3ulWViqZCxYMpR7-vr16iseOCNkQ9Ga32kbUlWdhZonoNlIus6veBGJgR48-JjCOcJdX9x02wnbwlZ3pdTww1k7o_hqJjEX_EkCV_z7thJoSpsbk40HK1JJ29b9vEv-0dvw2uk4c4791fxGJVIUDI4NMWwHmuALYhtnLVNW22XO1Eu1DTsC4JQxTE3dXVRnbyvP9AEltiQefOC-Coj0T1QwIkRtwNrk579JqBgFz07PKKzRdMZwU3WvYus72kwu9jq3a4f4Lu3oXjSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکل ژنتیکیه فکر کنم حاجی زود قضاوت کردیم
پ‌ن: داداش علی گرامیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83611" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83610" target="_blank">📅 17:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83608" target="_blank">📅 17:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxDxbGjRiuuE6yaezSkYop5EIi3Y2AFe0cf6Dd-9CdSMAQP2dPBOndwuPdwGb77Awb2__QPQHnR-LhtHO5tiKHFtmWRDpn21qW6F7n4oRurQjIegeedQg0ERdDwod8vSQxWOJzr-9X2qfUoB5FIPmWY9j8FjPj-VWR6HFcU4uohSOYfo8dSn9c_Mg9gyYOPryBCAcggSYeMmbpHmRp781Cscq1JGJcEG1LtXfKki7_brtzhUEYvi1cXAZF3DO3GrjuRtRJKfpZGDubnfkwab2tnvbuA7y2dJrsOVfZ6hNqbHSLARoZ7Ar4E-3b15JL5Ac9oe-YsyI_Qn0RTKbODGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewReleased
🆕
🗣
Artist: Young Lean & Metro Boomin & Future & Travis Scott & Mogan Wallen &…..
📋
Title: GTA VI
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83607" target="_blank">📅 16:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📶
منبع کانفیگ های رایگان
📶
🎁
هرروز کانفیگ رایگان میزارن
🎁
جوین شو عشق و حال کن
⬇️
⬇️
🕺
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83606" target="_blank">📅 16:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=DbCcvBtrwFgAAKXzZue2nopLCI_z5NoM4O7qYOWxKQXSZCA5Y6EatuYhw880eQbQ-kDqco6W2tr24mIx2bOF0K71wihtinoeXk1wqbUicGPGsrSpHOL5WCLHRHjLbtU2cLruP4zcgjqBrca-3ECfRc9ijzROyazsiEyh5edBMMh5H1fVTCHTQqANhgzU_wVvXURDUUDE9OvkQlw6QiMceKpQG2PwGZBUcz9Kr3RXMvLVO6FcV-8HLwxf_xFUJ64HfA0sh3fGEbhAmz_AluN-HxoqhBt7TATXuLuyogPxJ8qJkD9Gdmc-8GF68F-Wm2Qi3aVQD0rJKC0z1W3MC8pPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=DbCcvBtrwFgAAKXzZue2nopLCI_z5NoM4O7qYOWxKQXSZCA5Y6EatuYhw880eQbQ-kDqco6W2tr24mIx2bOF0K71wihtinoeXk1wqbUicGPGsrSpHOL5WCLHRHjLbtU2cLruP4zcgjqBrca-3ECfRc9ijzROyazsiEyh5edBMMh5H1fVTCHTQqANhgzU_wVvXURDUUDE9OvkQlw6QiMceKpQG2PwGZBUcz9Kr3RXMvLVO6FcV-8HLwxf_xFUJ64HfA0sh3fGEbhAmz_AluN-HxoqhBt7TATXuLuyogPxJ8qJkD9Gdmc-8GF68F-Wm2Qi3aVQD0rJKC0z1W3MC8pPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83600" target="_blank">📅 15:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=T95Zl8gfep6RRvRd4lDk3VcoTrBfwZxCo2nFjGIoObVR7XY_ZiqtUxho1oMCPjTOhDDTSRZVZ5tL4lGkUUDk2rCbp1EF3LCCHzo5kYBdEJlhY3vJv3xEpZJpu7r-4Uibl2MaUn2Y-VKhnuxjvJBR0sF6_jgqhD536tuJ7OB7hp2MC3p8MycczqSVTfHDBw_nvwVX92KVITxJLceJ1-xITeaViQ8AOR2BCxnDKW5NzU4D_EUKa5Zdoz-mqOeIxtBS7uYtQm6kag83eSVNKqB3SgdKm4Vz_qSqE8aMZswQBYHOMjNhI33JdEHIQoUxLKe2qblTzHKM5wTV37vTryqQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=T95Zl8gfep6RRvRd4lDk3VcoTrBfwZxCo2nFjGIoObVR7XY_ZiqtUxho1oMCPjTOhDDTSRZVZ5tL4lGkUUDk2rCbp1EF3LCCHzo5kYBdEJlhY3vJv3xEpZJpu7r-4Uibl2MaUn2Y-VKhnuxjvJBR0sF6_jgqhD536tuJ7OB7hp2MC3p8MycczqSVTfHDBw_nvwVX92KVITxJLceJ1-xITeaViQ8AOR2BCxnDKW5NzU4D_EUKa5Zdoz-mqOeIxtBS7uYtQm6kag83eSVNKqB3SgdKm4Vz_qSqE8aMZswQBYHOMjNhI33JdEHIQoUxLKe2qblTzHKM5wTV37vTryqQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83599" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY9QOCxyOg1jW8vVktenQckBbQ7-yAqEfd2LYh5NGkQ71oWI7GNI9GAfzRdhELQA2jrXorzCtVS2SxbVe2VamjPw--QYEkebLXnq-GCbAvKbkYer3aEE6n-i99jdQfX0I4_Ip2IbcNH498FfgzW4velkPgWPJB6yImcH_uq7nBEUN0NLSOoT3gpzIPyDUbcnMtiKmYbOLr33koSTp8WLm7D3qV7tqwwgBQxawmgpF1ZNHf7L5IKsS0LrDEvG03_y2hBmXrrNQbrDGzHmfBqa2J8vrrSN8pWl-hWuYd6pOY9LNzbUwwPiiAnlOmOwcp_6SqETiGR1gNP_aFTB_VBkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vf1lN4601rIk0JZraabKp3Q8BzQBlzMnwQyWUo68XQv-ip2ksNoW1IoCPo5bAHLVuaGGdTC3dfqvig1_7bahv8LDEGnBZgDqp7MEFQ6ynJrHYUwRQue2SteU8kh-f83uz_CQRflrVqJOw1RFOWkBO29aQCWeveAel86YE4KOw38M-CNGCJr1I51-Hg16gmv18CTWPfFYuZxvkBgJ-3a2OcbtlLi5XXXFJVGuuKM5w9hwA0KDCnfdhETLSssTbRrW9N3YheDbxN8vOX0I4N3b9B7S02CkuqfMUHE8q8Z9tV50rSwjWJu6XtrCjEN9tRKLqOrfiRrJk8gj-a_YWhz1fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استر و پارتنرش تو فیلم جدیدش کم مونده دیگه برا مارکتینگ فیلم جدیدشون پورن بدن ییرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83597" target="_blank">📅 12:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIoOvnbYqhDFWxntHjgSWUfBZnw1271nBsuVy02dNxJfsVtrAzblAxgcuCubBByAOFQPTPQibnXgSi_8QoDTrVm6VbYhyhyAmuNUdqd4BlhhQ_ZVNoQ5Sszd8QnR6jWDd7MACNfHfCnyYNsEY3c3EG47vjz6i0M9VyOQlRBykoCfak3ljGEwkLaybx4Xs8nGqlZmb6Xzqmy3vnOkzbvBnPviphlkbViNX91g2og0mw8Gz_sbsNZrKqP0xc3YUj6SAqVyQ_p_eaQ5uweBrVwVunmyEVUZOZ1j2H2pPqzX_x4EvoTC3EN-cfCCE-yIWOP250yAP095V2u_SvIWuI6BYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی رضا پیشرو از ویناک نپرسیده واقعا صورتی بود یا نه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83596" target="_blank">📅 12:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8rYGSndVBqm-rna_iYDzs1OLX41bf4qN69FLzrZsp5cqda4UIMHi8uPh_czFtqlpvtvFNgvDrTYuY81wPG7ikWSfyl_AF7me7ZvepFgJEOnT4FAdB5Iq9WMBaXQaOprVWsaTVXKdeVSQM6fN2oS0TSaKQfp-Phrng33aY8YyZmXcyo1LaNW-N_AjfJOdE1kXWIcZHBd22B1v2oGXu1cE95xDts6KMRANmKHTYxISDim7Q5tiVuuPR8Sh9Rgc9U32ScnLI-BP0U8MoTLDbjVyKQ6sXXpGYyMAzUZzfPGiAKJ37z-Z-SUSxBnBgZPEYhjeSQ2Bo2CmcsRxs0ifqEROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیگر ترک پیشکسوت که قطعا بچگیاتون تو ماهواره دیدینش هم به جمع فوت فتیشا پیوست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83595" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
